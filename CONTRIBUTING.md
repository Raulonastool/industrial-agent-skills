# Contributing

Contributions that turn real industrial automation experience into reusable agent behavior are welcome.

## Good contributions

Prefer lessons that are repeatable, technically testable, explicit about assumptions, safe to share publicly, and useful while an agent is actually doing work.

Keep durable engineering behavior in `SKILL.md`. Put product-specific facts in `references/`.

Do not turn a one-device observation into a universal rule.

## Public-source rule for vendor-specific content

Vendor-specific facts in this repository must be supportable by public sources such as:

- public vendor product pages
- public manuals and help/documentation sites
- public API documentation
- public release notes
- open-source repositories published by the vendor
- other information the vendor has intentionally made public

When practical, link the public source directly from the vendor reference.

Do not use internal presentations, partner-only material, unreleased product information, employee-only documentation, private support cases, or non-public communications as source material for a public skill.

If it is unclear whether a vendor-specific detail is public, generalize or omit it until a public source can be identified.

## Protect customer information

Do not submit:

- customer names or identifying project names without explicit permission
- credentials, keys, certificates, or secrets
- customer-confidential source code
- proprietary drawings or project files
- real site IP addresses, hostnames, or network diagrams
- real process tag names when they identify a project or process
- sensitive process data or operating limits
- customer-specific container names or deployment topology
- screenshots containing customer/site information
- internal-only documentation

Anonymization should remove identifying details, not merely replace the customer name while leaving a recognizable topology or dataset intact.

## Independence

This is an independent open-source project. References to vendor products are descriptive and do not imply sponsorship, endorsement, or official vendor support unless explicitly stated by the vendor.

## Skill quality bar

A skill should tell an agent:

1. when the workflow applies
2. what to inspect first
3. what not to assume
4. what sequence to follow
5. how to validate success
6. how to handle failure
7. what remains vendor- or site-specific

Prefer instructions that cause an agent to verify reality instead of confidently guessing.
