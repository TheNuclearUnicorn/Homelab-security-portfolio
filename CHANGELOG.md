# Changelog

This changelog records public-portfolio documentation releases, not production infrastructure releases.

## [Unreleased]

### Added

- automated documentation QA for pull requests and `main`;
- repository-owned sanitization, secret-pattern, lifecycle, whitespace, and relative-link validation;
- repository-owned Markdown structure checks in GitHub Actions;
- completed backup migration case study;
- Wazuh integration and OPNsense `reply-to` troubleshooting case study;
- branded GitHub-native README header and QA status badge.
- public portfolio refresh governance linking validated private runbook changes to sanitized public documentation and AI source-pack refresh;
- controlled Homelab knowledge/RAG documentation covering deterministic default-deny export, durable provenance/state, profile-aware retrieval, stale/deleted/disabled-domain denial, prompt-injection boundary testing, and corpus rebuild/rollback validation;
- public website delivery case study covering Astro build automation, GitHub Pages deployment, Cloudflare-managed custom-domain DNS, repository cleanup, and migration away from a private website ingress path;
### Changed

- case-study navigation expanded;
- stale "later stages" wording removed from the README;
- obsolete first-commit handoff link removed from the README;
- ADR front matter/body indentation normalized after QA exposed invalid formatting;
- local AI security-boundary documentation promoted from a basic read-only MCP description to the accepted controlled knowledge-ingestion and retrieval baseline;
- project maturity and evolution documentation updated to show provenance/refresh/recovery behavior as implemented rather than future work;
- semantic/vector retrieval reclassified from an unfinished requirement to a deliberately deferred design option pending measured need;
- future AI work now centers on domain-routing/provenance orchestration, one-domain-at-a-time expansion, and VLAN60 placement rather than completion of the accepted Homelab retrieval baseline.

- Observability `after` documentation remains blocked pending runtime validation.
- Full ICS/OT, Red Team, VLAN60 AI placement, and domain-routing/provenance expansion remain blocked pending implementation and validation; semantic/vector retrieval is intentionally deferred unless a later decision gate demonstrates material value.

## [1.0.0] - 2026-09-18

### Added

- sanitized architecture overview and network segmentation model;
- trust-boundary and security-design documentation;
- Zero Trust ingress architecture;
- GitOps and isolated CI/CD architecture;
- backup and recovery architecture;
- SSH trust model;
- Wazuh SIEM architecture;
- local AI security boundary;
- observability-modernization baseline and migration framework;
- seven ADRs;
- sanitized diagrams and configuration fragments;
- documentation governance and repository security policies;
- project summary, skills mapping, and project-evolution material.

### Publication Controls

- operational identifiers substituted or removed;
- current/planned/historical states explicitly separated;
- secrets, backups, private keys, recovery artifacts, and raw firewall exports excluded;
- public examples labeled as sanitized fragments rather than production configuration.
