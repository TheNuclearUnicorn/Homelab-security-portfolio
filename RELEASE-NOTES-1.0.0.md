# Homelab Security Portfolio — Release 1.0.0

## Summary

Version 1.0.0 is the first publication-ready snapshot of the sanitized homelab security portfolio.

The release emphasizes security architecture and operating discipline rather than a catalog of self-hosted applications.

## Included Domains

- network segmentation and trust boundaries;
- Zero Trust ingress;
- Docker platform security model;
- Forgejo/GitOps workflow;
- isolated CI/CD and restricted production deployment;
- independent backup and recovery;
- SSH trust architecture;
- Wazuh security monitoring;
- local AI security boundaries;
- architecture decision records and publication governance.

## Security Engineering Highlights

```text
OPNsense inter-zone authority            current
public router ports                      none
Caddy Docker socket                      not mounted
CI production Docker socket              unavailable
CI unrestricted production shell         unavailable
backup local fallback                    prohibited
backup mount validation                  fail-closed
administrative private keys              device-scoped
Ollama/Hermes listeners                  loopback only
AI knowledge MCP                         read-only / root-confined
```

## Explicit Open Work

- observability modernization;
- selected SSH hardening;
- Wazuh recovery, retention, tuning, and notification work;
- broader firewall hardening;
- Docker reproducibility work;
- full ICS/OT and Red Team workload integration;
- VLAN60 AI placement;
- semantic RAG/vector retrieval completion.

## Observability Publication Boundary

The repository includes the pre-modernization baseline, decision framework, and migration plan. It does not claim Grafana or Prometheus as current production runtime.

## Sanitization

Published hostnames, addressing, DNS, identities, and paths are sanitized or generalized. This repository is an engineering derivative, not a live infrastructure inventory.
