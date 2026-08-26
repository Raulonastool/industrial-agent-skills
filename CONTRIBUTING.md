# Contributing

Contributions that turn real industrial automation experience into reusable agent behavior are welcome.

## Good contributions

Prefer lessons that are repeatable, technically testable, explicit about assumptions, safe to share publicly, and useful while an agent is actually doing work.

Keep durable engineering behavior in `SKILL.md`. Put product-specific facts in `references/`.

Do not turn a one-device observation into a universal rule.

## Protect customer information

Do not submit credentials, customer-confidential source code, proprietary drawings, identifying site network diagrams, sensitive process data, or internal-only documentation.

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
