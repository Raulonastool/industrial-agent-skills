# Phoenix Contact VL3 Edge / vPLC Reference

Use this reference for deployments where an application container and PLCnext vPLC run on a Phoenix Contact VL3/UPC Edge or a materially similar Podman topology.

## Key networking lesson

A vPLC may expose more than one network interface. One deployment used this topology:

```text
Profinet-facing network
└── 192.168.1.10

Podman network
└── 10.88.0.2
```

The Profinet-facing address worked during development from an external machine but was not the correct path for the application container on the VL3.

The reusable rule is:

> Discover the address reachable from the application container. Do not assume the field-network address is the correct container-to-container address.

The addresses above are examples from one deployment, not universal defaults.

## Discover the runtime network

```bash
sudo podman ps
sudo podman inspect <vplc-container>
```

Inspect attached networks and assigned addresses. Then enter the application container:

```bash
podman exec -it <app> sh
```

Test the actual controller service from there:

```bash
python3 -c "import socket; print(socket.create_connection(('CONTROLLER_HOST', 443), 5))"
```

Replace the host and port with values discovered from the actual runtime.

A successful host-side test is not enough. Validate from inside the deployed application's network namespace.

## Deployment pattern

```bash
podman build -t <app>:<version> .
podman save -o <app>-<version>.tar <app>:<version>
podman load -i <app>-<version>.tar
```

Run with explicit deployment configuration rather than baking environment-specific controller addresses into the image.

## Rollback

Keep at least one known-good image available before a customer demonstration or production change. Do not delete the previous image until the replacement passes acceptance testing.

## Diagnostic order

```text
vPLC running
↓
app container running
↓
shared/reachable network identified
↓
target TCP port reachable from app container
↓
REST/API read works
↓
adapter works
↓
analytics works
↓
dashboard works
```
