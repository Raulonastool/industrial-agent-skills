---
name: edge-plc-app-deployment
description: Build, containerize, deploy, troubleshoot, and harden Python edge applications that communicate with PLCs, soft PLCs, gateways, or industrial runtimes through REST APIs, OPC UA, MQTT, vendor SDKs, or similar interfaces. Use for industrial dashboards, analytics, condition monitoring, ML, custom HMIs, container networking, controller tag access, Podman/Docker deployment, and rollback validation.
---

# Edge PLC Application Deployment

## Goal

Use this skill to help build or troubleshoot an edge application with this general shape:

```text
PLC / Industrial Runtime
        ↓
API or Industrial Protocol
        ↓
Controller Adapter
        ↓
Normalized Process Data
        ↓
Analytics / Engineering Logic
        ↓
Flask / FastAPI / Other Service
        ↓
OCI Container
        ↓
Edge Host
        ↓
Browser / Client
```

Optimize for:

- reliable controller communication
- clear separation of concerns
- container portability
- graceful failure
- reproducible deployment
- simple rollback
- fast troubleshooting

## Core Rules

1. Inspect before changing.
2. Never invent controller IPs, ports, namespaces, tag names, credentials, or network topology.
3. Separate controller access from analytics and UI logic.
4. Treat development networking and deployed container networking as different until verified.
5. Test connectivity from inside the deployed application container.
6. Externalize environment-specific configuration.
7. Controller communication failures must not crash the application.
8. Preserve the previous known-good image before deployment.
9. Prefer small, reversible changes over broad rewrites.
10. Do not claim success until applicable acceptance tests have been performed.

# Workflow

## 1. Inspect the Project

Before editing, identify:

```text
application entry point
Python version
dependency files
Dockerfile / Containerfile
controller communication library
controller host and port configuration
environment-variable handling
web framework
web listen port
templates/static files
deployment scripts
existing tests
```

Preserve working project conventions unless there is a specific reason to change them.

## 2. Identify the Controller Interface

Determine:

```text
Protocol:
Host:
Port:
Authentication:
Namespace:
Required tags/variables:
Read/write behavior:
Expected update rate:
Failure behavior:
```

The interface may be:

```text
REST / HTTPS
OPC UA
MQTT
Modbus TCP
vendor SDK
vendor REST library
other industrial API
```

If the runtime supports browsing or discovery, use it to verify the actual exposed variable names.

If controller variables must be published, HMI-enabled, whitelisted, or otherwise exposed to external applications, verify that configuration before debugging application code.

## 3. Create a Controller Adapter

Prefer a dedicated module such as:

```text
controller_reader.py
plc_reader.py
data_source.py
```

Expose a small interface:

```python
def get_process_data():
    ...
```

Return normalized application data:

```python
{
    "connected": True,
    "pressure": 0.6,
    "flow": 0.82,
    "pump_running": True,
    "temperature": 72.4
}
```

Analytics and web routes should consume normalized data rather than directly resolving controller tags or opening connections.

Preferred:

```python
data = get_process_data()
result = calculate_model(data["pressure"], data["flow"])
```

Avoid spreading controller-specific logic across routes, templates, and analytics functions.

## 4. Harden Controller Communication

The controller adapter should, where supported:

- reuse connections or sessions
- reconnect after communication loss
- use bounded connection/request timeouts
- validate returned values
- handle missing or stale values
- normalize controller-specific types
- catch expected communication exceptions
- log useful diagnostics
- return a defined disconnected state
- avoid unhandled exceptions escaping into the web layer

Example fallback:

```python
{
    "connected": False,
    "pressure": None,
    "flow": None,
    "pump_running": None,
    "temperature": None
}
```

Use zero as a fallback only when zero cannot be confused with a legitimate process value.

## 5. Externalize Deployment Configuration

Prefer environment variables or a deployment config file for values that may change:

```text
CONTROLLER_HOST
CONTROLLER_PORT
CONTROLLER_PROTOCOL
CONTROLLER_NAMESPACE
CONTROLLER_TIMEOUT
WEB_HOST
WEB_PORT
REFRESH_INTERVAL
LOG_LEVEL
```

Example:

```python
import os

CONTROLLER_HOST = os.getenv("CONTROLLER_HOST", "127.0.0.1")
CONTROLLER_PORT = int(os.getenv("CONTROLLER_PORT", "443"))
```

Do not commit secrets into source code.

Do not assume the controller address used during local development is correct from inside the deployed container.

## 6. Resolve Container Networking

Treat networking as a discovery problem.

A PLC or soft PLC may expose different addresses on:

```text
field network
management network
host network
container bridge
application network
```

If the host can reach the controller but the application container cannot:

1. list running containers
2. identify the controller/runtime container if applicable
3. inspect attached networks
4. identify the network shared with the application
5. determine the controller address or service name reachable on that network
6. test the actual target port from inside the application container
7. update configuration only after reachability is proven

Typical commands:

```bash
podman ps
podman inspect <container>
podman exec -it <app> sh
```

or:

```bash
docker ps
docker inspect <container>
docker exec -it <app> sh
```

Minimal TCP test:

```bash
python3 -c "import socket; print(socket.create_connection(('HOST', PORT), 5))"
```

Use `curl`, `wget`, or `nc` instead when they are available and more appropriate.

Do not debug the analytics or UI layer before proving basic network reachability.

Prefer stable DNS/container names or supported service discovery over hardcoded bridge IPs when available.

## 7. Harden Engineering Calculations

Treat live process values as untrusted runtime input.

Protect calculations from:

```text
None
NaN / infinity
divide by zero
sqrt of negative values
bad strings
unexpected payload shapes
stale values
out-of-range measurements
invalid enum or boolean states
```

Example:

```python
def system_coefficient(flow, dp):
    flow = float(flow)
    dp = max(float(dp), 0.001)
    return flow / (dp ** 0.5)
```

Do not silently mask an important process fault. When practical, preserve a quality/status indicator alongside any computational fallback.

## 8. Containerize Reproducibly

Reuse the repository's existing container strategy when possible.

Ensure that:

- dependencies are explicit
- the correct application files are copied
- the application listens on the intended interface and port
- logs are written to stdout/stderr
- environment-specific values are not baked into the image unnecessarily

Build with the runtime already used by the target system:

```bash
podman build -t <app>:<version> .
```

or:

```bash
docker build -t <app>:<version> .
```

## 9. Validate the Container

Before deployment, verify as many as possible:

```text
container starts
application remains running
web endpoint responds
required Python modules import
configuration is loaded
controller port is reachable
controller authentication succeeds
required variables are discoverable
a minimal controller read succeeds
analytics work with live values
communication failure does not crash the app
logs contain no unhandled tracebacks
```

Prefer testing the exact image that will be deployed.

## 10. Deploy with Versioning and Rollback

Use explicit image versions rather than replacing an anonymous `latest` build when practical.

Examples:

```text
app:1.0.0
app:1.0.1
app:demo-2026-08-25
```

For offline deployment:

```bash
podman save -o <app>-<version>.tar <image>
podman load -i <app>-<version>.tar
```

Before replacing a working deployment:

- record the current image/tag
- preserve the current runtime configuration
- retain the previous known-good image
- know the commands needed to restore it
- avoid destructive cleanup until the new version passes acceptance testing

Rollback should not require rebuilding source code.

# Web Application Reliability

A controller outage should produce a useful application state such as:

```text
CONTROLLER DISCONNECTED
LAST SUCCESSFUL UPDATE: <timestamp>
DATA QUALITY: STALE
```

It should not produce:

```text
500 Internal Server Error
framework exception page
blank dashboard
```

When appropriate, display:

- controller connection state
- last successful update
- data timestamp
- stale/invalid status

Use the simplest update mechanism that satisfies the requirement:

```text
page refresh
fetch/AJAX polling
server-sent events
WebSocket
```

# Troubleshooting Order

Use this order unless evidence points elsewhere.

## 1. Process

Are the controller runtime and application containers/processes running?

## 2. Configuration

Verify actual values for:

```text
controller host
controller port
credentials
namespace
application port
environment variables
```

## 3. Network

Can the application container reach the controller service?

## 4. Controller Exposure

Are the required variables/tags/endpoints exposed externally?

## 5. Discovery

Does the controller API report the names/namespaces the application expects?

## 6. Minimal Read

Can one known value be read outside the full application flow?

## 7. Adapter

Does the controller adapter return correct normalized data?

## 8. Analytics

Do calculations work with known-good test values?

## 9. Web Layer

Do routes, templates, static files, generated charts, and refresh logic work?

# Common Failure Patterns

## Works locally, fails on edge device

Check:

- different controller address
- different network interface
- container bridge routing
- firewall
- TLS/certificate behavior
- DNS/container-name resolution
- missing environment variables
- missing dependencies

## Host reaches controller, container does not

Inspect container networks and test from inside the application container.

Host connectivity is not proof of container connectivity.

## API connects, variable reads fail

Check:

- variable exposure/publishing
- permissions
- namespace
- case sensitivity
- runtime project version
- discovery results

## Web UI works but reports disconnected

Test the controller adapter independently from the web route.

## Application crashes on process data

Validate values at both boundaries:

```text
controller → adapter
adapter → engineering calculations
```

# Acceptance Checklist

Before declaring completion:

```text
[ ] Container starts successfully
[ ] Container remains running
[ ] Browser/client reaches the application
[ ] Controller service is reachable from inside the app container
[ ] Authentication succeeds if required
[ ] Required variables/tags are discoverable
[ ] Required values can be read
[ ] Data types/scaling are correct
[ ] Analytics execute correctly
[ ] UI updates correctly
[ ] Controller disconnect is handled gracefully
[ ] Controller reconnect succeeds if supported
[ ] Invalid data does not crash calculations
[ ] No framework exception page is exposed
[ ] Logs support diagnosis
[ ] Deployment configuration is known
[ ] Previous known-good version can be restored
```

If a required test cannot be performed in the current environment, state exactly what remains unverified.

# Agent Behavior

When this skill is active:

1. Inspect before editing.
2. Use discovered runtime values instead of guessing.
3. Make the smallest change that addresses the actual failure.
4. Test incrementally.
5. Keep controller-specific code localized.
6. Preserve rollback.
7. Distinguish clearly between:
   - verified facts
   - inferred configuration
   - assumptions
   - unverified tests
8. When implementation tools are available, perform the change and validation rather than only describing what the user should do.
9. When a required test cannot be performed, provide the smallest next diagnostic command.

# Keep Vendor Details in References

Do not make the core skill depend on one PLC vendor, one edge computer, or one container-network address.

Put product-specific details in optional references, for example:

```text
edge-plc-app-deployment/
├── SKILL.md
├── references/
│   ├── plcnext-rest.md
│   ├── vl3-networking.md
│   ├── opc-ua.md
│   └── mqtt.md
└── scripts/
    ├── test_tcp.py
    └── validate_deployment.sh
```

Vendor references may contain:

- API-specific code
- variable exposure requirements
- default ports
- runtime naming conventions
- device-specific network topology
- authentication steps
- firmware/version-specific behavior

Keep durable engineering workflow in `SKILL.md`. Keep product-specific facts in references.
