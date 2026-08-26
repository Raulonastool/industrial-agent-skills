# PLCnext REST Reference

Use this reference only when an application communicates with a PLCnext Runtime through its publicly documented REST/eHMI interfaces or another supported public integration path.

## Publicly documented behavior

Phoenix Contact publicly documents that the PLCnext Runtime REST interface can be enabled in PLCnext Engineer and that tags selected as HMI tags can be exposed to connected applications such as the PLCnext Edge Gateway.

Public source:

- https://www.phoenixcontact.com/en-us/us-lp-us-plcnextedgegateway/us-lp-us-plcnextedgegateway-drivers/us-lp-us-plcnextedgegateway-plcnextapi

Use the public documentation appropriate to the installed PLCnext Engineer/runtime version when configuring the REST interface.

## Variable exposure

If an application can reach the PLCnext Runtime but expected process variables are unavailable, verify that the required variables have been intentionally exposed through the supported project configuration before changing application code.

Do not assume that every PLC variable is externally visible.

## Variable discovery

Do not guess variable names or namespaces from another project.

Use the supported API/client discovery mechanism for the target runtime, when available, or verify the exposed names in the PLCnext Engineer project and public API documentation.

Do not publish real customer process tag names in examples. Prefer placeholders such as:

```text
Process.Pressure
Process.Flow
Machine.Running
```

## Adapter pattern

Keep PLCnext-specific access inside a reader/adapter module. Application and analytics code should consume normalized process data instead of making PLCnext calls directly.

Recommended behavior:

- reuse sessions when supported
- reconnect after failures
- use bounded timeouts
- catch expected communication exceptions
- validate returned values
- return a defined disconnected state
- do not allow a failed read to crash the web application

## Troubleshooting order

1. Confirm the runtime is reachable from the application's network context.
2. Confirm the documented REST/eHMI interface is enabled as required.
3. Confirm required variables are intentionally exposed/HMI-enabled as appropriate.
4. Verify variable names using the target project's supported discovery/configuration path.
5. Read one known, non-sensitive test variable.
6. Only then debug application mapping or analytics.

## Publication boundary

Keep this public reference limited to public Phoenix Contact documentation and generic integration practices. Do not add internal documentation, unreleased behavior, credentials, customer tag names, project files, customer network details, or installation-specific configuration.