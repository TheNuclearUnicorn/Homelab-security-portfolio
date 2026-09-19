---
title: "Portfolio Refresh Policy"
document_id: "HSP-GOV-003"
document_type: "publication-governance"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-19"
sanitization: "operational-identifiers-substituted"
tags:
  - governance
  - documentation
  - publication
  - change-control
  - portfolio
---

# Portfolio Refresh Policy

> **Status:** Current verified publication-governance model for this sanitized public portfolio.

## Purpose

This repository is a sanitized professional derivative of a privately operated security-focused homelab and cyber range.

The portfolio is updated when validated engineering work materially changes the architecture, security model, recovery capability, operational maturity, or reusable engineering lessons.

It is not updated simply because routine maintenance occurred.

## Authority Model

The publication flow is intentionally one-way:

```text
validated runtime
    ↓
canonical private engineering documentation
    ↓
public-impact assessment
    ↓
sanitized portfolio derivative
    ↓
feature branch
    ↓
automated publication QA
    ↓
pull request
    ↓
main
```

The public repository is not the authority for live private infrastructure state.

## Publication Delta Test

A public update is considered when validated work changes one or more of:

- architecture;
- trust boundaries;
- network segmentation or routing;
- security controls;
- deployment authority;
- backup or recovery capability;
- monitoring or observability maturity;
- local-AI security boundaries;
- validation methodology;
- implementation status of a previously planned capability;
- a significant architecture decision;
- a completed migration;
- a reusable troubleshooting lesson.

Routine package updates, restarts, minor operational maintenance, and identifier changes that do not alter the engineering model normally do not trigger publication.

## Artifact Selection

Typical public destinations are:

| Engineering change | Public artifact |
|---|---|
| Architecture or segmentation | `docs/architecture/` |
| Platform or ingress | `docs/platform/` |
| GitOps / CI-CD | `docs/devops/` |
| Security boundary | `docs/security/` |
| Backup / restore | `docs/recovery/` |
| Governance | `docs/governance/` |
| Accepted design decision | `adrs/` |
| Completed migration / troubleshooting narrative | `case-studies/` |
| Material navigation or maturity change | `README.md` / `CHANGELOG.md` |

## Sanitization

Publication removes or abstracts details that primarily help map or attack the live environment.

Normally sanitized:

- live hostnames and addresses;
- live DNS names;
- account identities;
- sensitive filesystem paths;
- private repository identities where unnecessary;
- secrets, keys, credentials, tokens, cookies, recovery codes;
- raw firewall backups;
- private recovery artifacts;
- database/application contents;
- protected certificate material.

Preserved where safe and technically useful:

- architectural relationships;
- trust-boundary purpose;
- VLAN roles;
- least-privilege firewall concepts;
- meaningful protocol dependencies;
- CI isolation;
- backup fail-closed behavior;
- recovery testing;
- validation methodology;
- negative tests;
- rollback design;
- lessons learned.

## Lifecycle Accuracy

Public documents distinguish:

```text
planned
current-with-open-items
current-verified
historical-baseline
case-study
```

Planned work is not presented as implemented.

A before-state becomes historical only after the replacement architecture is validated.

## Change Workflow

Normal publication flow:

```text
validated engineering change
        ↓
sanitized derivative
        ↓
feature branch
        ↓
pull request
        ↓
Publication quality
        ↓
rendered-diff review
        ↓
merge to main
```

The automated publication gate checks for structural and publication-quality defects before normal promotion.

## Release Guidance

Not every documentation change requires a release.

A release is appropriate when several merged changes form a meaningful public milestone, such as:

- a newly validated architecture domain;
- a completed modernization;
- major new case studies;
- a substantial governance or automation capability;
- a major portfolio-generation change.

## Drift Handling

If public documentation disagrees with validated private engineering state, the private validated source is reconciled first and the public derivative is then refreshed.

The public portfolio is not used to redefine private runtime state.

## Related Documentation

- [Public Documentation Governance](documentation-governance.md)
- [Publication Readiness Review](publication-readiness-review.md)
- [Repository README](../../README.md)
- [Changelog](../../CHANGELOG.md)
