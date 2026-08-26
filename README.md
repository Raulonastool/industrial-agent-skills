# Industrial Agent Skills

Practical industrial automation knowledge for AI coding agents.

> **Status: v0.1.0 — early public testing**  
> Looking for controls engineers, OT/IIoT developers, industrial software engineers, and AI-agent users to try the skills, break them, report what is missing, and contribute publicly verifiable industrial knowledge.

This repository packages field-informed workflows for agents working around PLCs, industrial edge computers, containerized applications, industrial data, and Industry 4.0 software.

**Goal:** teach general-purpose coding agents the industrial deployment lessons they usually do not know yet.

## Start here

The first skill is [`edge-plc-app-deployment`](skills/edge-plc-app-deployment/SKILL.md).

It helps an agent build, containerize, deploy, troubleshoot, and harden applications that communicate with PLCs or industrial runtimes.

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

- [PLCnext REST](skills/edge-plc-app-deployment/references/plcnext-rest.md)
- [Phoenix Contact VL3 / Virtual PLCnext Control edge computing](skills/edge-plc-app-deployment/references/vl3-edge.md)

## What I would love people to test

Try the skill against a lab, simulated, or non-production edge application and watch how the agent behaves.

Useful questions include:

- Does the skill activate for the right kinds of tasks?
- Does the agent inspect the project before changing it?
- Does it verify controller connectivity instead of guessing?
- Does it test networking from inside the deployed container when appropriate?
- Does it keep controller-specific code isolated from the UI and analytics layers?
- Does it handle controller disconnects and bad process values safely?
- Does it preserve rollback and distinguish verified facts from assumptions?
- Where does the agent still misunderstand industrial automation?

If you find a gap, open an issue. Real-world counterexamples and publicly sourced corrections are especially valuable.

## Why PLCnext first?

PLCnext was selected as the first vendor reference intentionally, not because the core skill is PLCnext-specific.

Phoenix Contact describes PLCnext Technology as an **open industrial automation platform**, and the public PLCnext ecosystem includes extensive documentation, open-source tooling, examples, APIs, container workflows, and community resources. That makes it a useful environment for building industrial agent knowledge that can be independently verified in public sources.

Useful public PLCnext sources include:

- [PLCnext Engineer online help](https://engineer.plcnext.help/)
- [PLCnext Technology API documentation](https://api.plcnext.help/)
- [Official PLCnext GitHub organization](https://github.com/PLCnext)
- [PLCnext app examples](https://github.com/PLCnext/PLCnextAppExamples)
- [PLCnext Store](https://www.plcnextstore.com/)

PLCnext is the first reference implementation. The durable workflow in `SKILL.md` is intended to remain vendor-neutral.

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

The core uses the open `SKILL.md` Agent Skills format. Product-specific install wrappers stay separate from the skill itself.

## Public-source and confidentiality policy

This is an independent open-source project. Vendor-specific references are intended to contain only information available from public vendor documentation plus generic engineering practices.

This repository must not contain customer-confidential information, real customer/site network details, credentials, proprietary project files, private process data, internal-only vendor documentation, or unreleased product information.

If a vendor-specific detail cannot be supported by a public source, it should be generalized or omitted until a public source can be identified. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution policy.

References to Phoenix Contact, PLCnext Technology, VL3, or other vendor products are descriptive and do not imply sponsorship, endorsement, or official vendor support.

## Why this exists

Coding agents are strong at Python, JavaScript, containers, APIs, and web applications. Industrial projects add constraints that are easy to miss:

- controller variables may need to be explicitly exposed
- field-network addresses may differ from container-network addresses
- real process data is messy
- losing communication cannot be allowed to crash an operator-facing application
- troubleshooting should begin with process/config/network checks before rewriting code
- a demo or production deployment needs a rollback path

The project turns those general lessons into reusable agent workflows without publishing customer-specific implementations.

## Repository structure

```text
industrial-agent-skills/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .github/
│   └── ISSUE_TEMPLATE/
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
├── SECURITY.md
├── LICENSE
└── README.md
```

## Safety and scope

This repository focuses on software architecture, observability, networking, data acquisition, analytics, and deployment around industrial systems.

A successful software test does not make a control-system change safe for production. Site procedures, cybersecurity requirements, process safety, management of change, validation, and qualified human review still apply.

Do not use examples from this repository as authorization to modify a production control system.

## Contributing

Contributions are welcome, especially:

- vendor-specific references backed by public documentation
- repeatable troubleshooting workflows
- protocol integration patterns
- safe simulation and test tooling
- generalized lessons learned from real deployments
- examples of where an AI agent misunderstood an industrial task

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting vendor- or customer-derived material.

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
