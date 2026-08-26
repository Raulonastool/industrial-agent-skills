# Phoenix Contact VL3 Edge / vPLC Reference

Use this reference for deployments involving a Phoenix Contact VL3 edge device with Virtual PLCnext Control, or for materially similar containerized industrial-edge topologies.

## Public product context

Phoenix Contact publicly describes the VL3 UPC 2440 EDGE as an edge device with Virtual PLCnext Control and Ubuntu Pro Desktop, intended for local data collection, evaluation, and expandable software-based analytics. Phoenix Contact also publicly documents containerized application deployment with Podman in the PLCnext Technology ecosystem.

Public sources:

- https://www.phoenixcontact.com/en-us/products/plcnext-technology
- https://www.phoenixcontact.com/en-pc/products/edge-computing

## Key networking lesson

When an application and an industrial runtime execute in containers, the address used from a developer workstation or field network may not be reachable from the application container.

The reusable rule is:

> Discover the endpoint reachable from the application container. Do not assume a host-facing or field-network address is also the correct container-to-container address.

Do not copy example IP addresses from another installation. Inspect the target system and use only values discovered from that deployment.

## Discover the runtime network

Use the container runtime's standard inspection tools, for example:

```bash
sudo podman ps
sudo podman inspect <runtime-container>
```

Inspect attached networks and assigned addresses. Then enter the application container:

```bash
podman exec -it <app> sh
```

Test the actual service from there using the host and port configured for the target installation:

```bash
python3 -c "import socket; print(socket.create_connection(('CONTROLLER_HOST', CONTROLLER_PORT), 5))"
```

A successful host-side test is not proof that the same endpoint is reachable from the deployed application's network namespace.

## Deployment pattern

```bash
podman build -t <app>:<version> .
podman save -o <app>-<version>.tar <app>:<version>
podman load -i <app>-<version>.tar
```

Run with explicit deployment configuration rather than baking site-specific controller addresses into the image.

## Rollback

Keep at least one known-good image available before a demonstration or production change. Do not delete the previous image until the replacement passes acceptance testing.

## Diagnostic order

```text
industrial runtime running
↓
app container running
↓
shared/reachable network identified
↓
target TCP service reachable from app container
↓
application API read works
↓
adapter works
↓
analytics works
↓
dashboard works
```

## Publication boundary

Do not add customer hostnames, IP addresses, container names, network diagrams, credentials, process tag names, or installation-specific topology to this public reference. Product-specific facts should be traceable to public vendor documentation.