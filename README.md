# Industrial Agent Skills

Practical industrial automation knowledge for AI coding agents.

This repository packages field-informed workflows for agents working around PLCs, industrial edge computers, containerized applications, industrial data, and Industry 4.0 software.

**Goal:** teach general-purpose coding agents the industrial deployment lessons they usually do not know yet.

## Available skills

### `edge-plc-app-deployment`

Build, containerize, deploy, troubleshoot, and harden applications that communicate with PLCs or industrial runtimes.

The skill teaches an agent to:

- separate controller I/O from analytics and UI code
- discover rather than guess controller endpoints and tag namespaces
- troubleshoot container networking from the application's network namespace
- harden process-data calculations
- fail gracefully when a PLC/controller disconnects
- validate deployments in a useful order
- preserve a known-good rollback path

Vendor-specific knowledge is kept in optional references so the core workflow stays portable.

Current references:

- PLCnext REST
- Phoenix Contact VL3/vPLC edge networking

## Structure

```text
industrial-agent-skills/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── edge-plc-app-deployment/
│       ├── SKILL.md
│       ├── references/
│       │   ├── plcnext-rest.md
│       │   └── vl3-edge.md
│       └── scripts/
│           └── test_tcp.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Why this exists

Coding agents are strong at Python, JavaScript, containers, APIs, and web applications. Industrial projects add constraints that are easy to miss:

- controller variables may need to be explicitly exposed
- field-network addresses may differ from container-network addresses
- real process data is messy
- losing communication cannot be allowed to crash an operator-facing application
- troubleshooting should begin with process/config/network checks before rewriting code
- a demo or production deployment needs a rollback path

These are often learned through deployment experience rather than ordinary software documentation.

## Claude Code

This repository is packaged as a Claude Code plugin and marketplace.

Add the marketplace:

```text
/plugin marketplace add raulonastool/industrial-agent-skills
```

Install the plugin:

```text
/plugin install industrial-agent-skills@industrial-agent-skills
```

For local development:

```bash
claude --plugin-dir .
```

## Codex and other Agent Skills clients

The portable skill bundle lives at:

```text
skills/edge-plc-app-deployment/
```

The core uses the open `SKILL.md` Agent Skills format. Product-specific install wrappers should stay separate from the skill itself.

## Safety and scope

This repository focuses on software architecture, observability, networking, data acquisition, analytics, and deployment around industrial systems.

A successful software test does not make a control-system change safe for production. Site procedures, cybersecurity requirements, process safety, management of change, validation, and qualified human review still apply.

## Contributing

Contributions are welcome, especially vendor references, troubleshooting workflows, protocol integrations, safe simulation/test tooling, and anonymized lessons learned from real projects.

Do not commit customer secrets, credentials, confidential code/drawings, or identifying site information.

## Planned skills

- industrial MQTT integration
- OPC UA integration and troubleshooting
- Modbus integration
- PROFINET troubleshooting
- synthetic industrial data generation
- industrial dashboard development
- condition-monitoring / anomaly-detection workflows

## License

Apache-2.0
