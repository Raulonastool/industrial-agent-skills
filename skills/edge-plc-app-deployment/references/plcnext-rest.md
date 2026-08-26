# PLCnext REST Reference

Use this reference only when an application communicates with a PLCnext Runtime through the PLCnext REST API.

## Variable exposure

PLC variables that must be accessible through the REST API need to be exposed by the PLCnext project. In the deployment this reference came from, required variables were marked:

```text
HMI = TRUE
```

If the API connection works but variable reads fail, confirm variable exposure in PLCnext Engineer before changing application code.

## Variable discovery

Do not guess namespaces. Use the PLCnext API library to inspect variables actually exposed by the runtime.

```python
from plcnext_api import PLCnextAPI

plc = PLCnextAPI(ip="CONTROLLER_HOST")
plc.connect()
print(plc.variables)
```

A commonly observed namespace format is:

```text
MainInstance.VariableName
```

Use names returned by the runtime rather than names inferred from the PLC program.

## Adapter pattern

Keep PLCnext-specific access inside a reader/adapter module. Application and analytics code should consume normalized process data instead of making PLCnext calls directly.

Recommended behavior:

- reuse the session when supported
- reconnect after failures
- catch expected communication exceptions
- validate returned types
- return a defined disconnected state
- do not allow a failed read to crash the web application

## Troubleshooting order

1. Confirm the runtime is reachable from the application's network context.
2. Confirm the REST service port is reachable.
3. Confirm required variables are HMI-enabled/exposed.
4. Inspect `plc.variables`.
5. Read one known variable.
6. Only then debug application mapping or analytics.
