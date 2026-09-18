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

### Changed

- case-study navigation expanded;
- stale "later stages" wording removed from the README;
- obsolete first-commit handoff link removed from the README;
- ADR front matter/body indentation normalized after QA exposed invalid formatting.

- Observability `after` documentation remains blocked pending runtime validation.
- Full ICS/OT, Red Team, VLAN60 AI, and semantic RAG documentation remains blocked pending implementation and validation.

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
