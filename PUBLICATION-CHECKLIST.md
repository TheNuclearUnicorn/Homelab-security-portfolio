# Publication Checklist

Use this checklist before making the repository public or publishing a new release.

## Source Authority

- [ ] Current-state claims match the newest validated private sources.
- [ ] Planned work remains labeled as planned.
- [ ] Historical baseline material is not presented as current runtime.
- [ ] Source conflicts are surfaced rather than silently reconciled.

## Sanitization

- [ ] No live public DNS names are present.
- [ ] No live private infrastructure IP addresses are present.
- [ ] No private hostnames, usernames, or service-account names are present.
- [ ] No private filesystem paths, SSH fingerprints, MAC addresses, or serial numbers are present.
- [ ] No raw firewall/router backup or recovery artifact is present.

## Secrets

- [ ] No passwords, API keys, tokens, tunnel credentials, private SSH keys, private certificate keys, recovery codes, `.env` contents, Restic credentials, SMB credentials, or OAuth secrets are present.

## Technical Accuracy

- [ ] OPNsense remains the authoritative inter-zone firewall.
- [ ] CI is not described as having the production Docker socket or unrestricted production shell.
- [ ] Restricted production deployment remains accurately represented.
- [ ] Backup remains outside the production Docker storage failure domain and fails closed.
- [ ] Wazuh maturity limitations remain explicit.
- [ ] SSH client policy is not represented as universal server-side hardening.
- [ ] Local AI remains loopback-bound in the current architecture.
- [ ] VLAN60 AI placement is not described as implemented.
- [ ] Grafana/Prometheus are not described as current runtime until validated.
- [ ] ICS/OT and Red Team workload maturity is not overstated.

## Documentation Quality

- [ ] Relative Markdown links pass validation.
- [ ] Mermaid diagrams render correctly.
- [ ] Public identifiers are consistent.
- [ ] `example.com` is used for public DNS examples.
- [ ] Documentation-only address ranges are used consistently.
- [ ] Current, planned, case-study, and historical states are explicit.
- [ ] Partial examples are labeled as fragments.

## Repository Metadata

- [ ] `README.md`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `.gitignore`, ADR index, portfolio summaries, changelog, and release notes are current.

## Release Gate

Release only when:

```text
broken relative links = 0
known live/private identifier findings = 0
secret-pattern findings = 0
known current-vs-planned contradiction findings = 0
```
