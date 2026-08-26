# Security Policy

Industrial Agent Skills contains reusable agent instructions, references, and small diagnostic utilities. It is not a substitute for site cybersecurity policy, process-safety review, management of change, or qualified engineering approval.

## Reporting repository security issues

If you find a security issue in code or guidance published by this repository, report it without including secrets, customer-identifying information, or private infrastructure details.

If the issue can be described safely in public, open a GitHub issue with a minimal sanitized reproduction.

If describing the issue would require customer-confidential information, credentials, real network details, proprietary project files, or other sensitive material, **do not post those details in a public GitHub issue**.

## Vendor product vulnerabilities

This project is independent from the vendors referenced in its skills.

Potential vulnerabilities in a vendor's product, firmware, cloud service, runtime, or engineering software should be reported through that vendor's official security or PSIRT process rather than disclosed through this repository.

## Operational safety

Examples and diagnostic commands in this repository should be tested in a lab, simulated environment, or otherwise authorized system before use in production.

Do not treat an AI agent's recommendation as authorization to:

- modify a production controller
- alter safety logic or safety functions
- bypass access controls
- expose an industrial service to an untrusted network
- change firewall or segmentation rules
- deploy unreviewed software to a production control system

Users remain responsible for validating changes against their site's cybersecurity, functional-safety, process-safety, and change-management requirements.
