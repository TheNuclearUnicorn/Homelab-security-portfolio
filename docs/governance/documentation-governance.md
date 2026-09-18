---
title: "Public Documentation Governance"
document_id: "HSP-GOV-001"
document_type: "governance"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
tags:
  - governance
  - documentation
  - lifecycle
  - publication
---

# Public Documentation Governance

> **Status:** Current publication-governance model for this repository.

## Purpose

This document defines how the public portfolio is derived, reviewed, and kept distinct from private operational documentation.

The public repository is not an operational source of truth.

## Authority Model

Operational claims are derived using this precedence:

1. verified runtime evidence and newest validated current-state runbooks;
2. current high-level network/topology inventory;
3. current subsystem runbooks;
4. accepted governance and source-registry material;
5. program roadmap for future intent;
6. planned/in-progress material as proposals only;
7. historical or superseded material as dated evidence only.

When sources conflict, the conflict is surfaced rather than silently reconciled.

## Publication Plane

The public repository is a separate derivative plane:

```text
validated private source
  -> deliberate sanitization and synthesis
  -> public portfolio document
```

The public copy does not become authoritative merely because it is published or version controlled.

Operational changes are made in the private canonical plane first. The public portfolio is refreshed afterward when the change is appropriate to disclose.

## Public Lifecycle States

Allowed publication states:

| State | Meaning |
|---|---|
| `current-verified` | Supported by validated current-state evidence |
| `current-with-open-items` | Current and working, with explicitly documented debt |
| `historical-baseline` | Preserved for comparison; not current |
| `case-study` | Decision/migration narrative |
| `planned` | Not implemented; proposal or framework only |

A planned document must never be interpreted as current runtime.

## Sanitization Standard

Normally substitute or generalize:

- hostnames;
- IP addresses;
- DNS names;
- usernames;
- service-account identities;
- filesystem paths;
- repository-owner identities;
- hardware identifiers.

Always omit:

- passwords;
- API keys;
- access tokens;
- tunnel credentials;
- private keys;
- recovery codes;
- private certificate material;
- `.env` contents;
- backup contents;
- database contents;
- raw firewall/router exports;
- actual recovery artifacts.

## Public Addressing

Documentation-only addressing preserves security-zone meaning while breaking the mapping to the private environment.

Example convention:

```text
VLAN20 Applications -> 10.100.20.0/24
VLAN70 CI           -> 10.100.70.0/24
VLAN99 Management   -> 10.100.99.0/24
```

Container networks use separate documentation-only ranges.

Loopback addresses such as `127.0.0.1` remain unchanged when loopback binding is itself a security control.

## Technical Substance

Sanitization must not remove the reason the architecture is worth documenting.

Retain where relevant:

- VLAN purpose;
- firewall policy ordering;
- exact protocol/port intent;
- trust relationships;
- negative security tests;
- rollback behavior;
- deployment gates;
- backup failure behavior;
- recovery methodology;
- Docker-socket privilege decisions;
- AI tool restrictions;
- lessons learned.

## Example Policy

Files under `examples/` are intentionally sanitized and may be partial.

They are not guaranteed to be directly runnable.

Examples must not invent missing production details merely to appear complete.

## Decision Records

ADRs record significant choices whose rationale would otherwise be lost.

An ADR describes:

- context;
- decision;
- alternatives considered;
- security consequences;
- operational consequences;
- validation evidence;
- current status.

If an ADR is later superseded, the original is retained and linked to its replacement.

## Refresh Workflow

Normal publication refresh:

```text
runtime or accepted private change
  -> canonical private runbook updated
  -> public relevance assessed
  -> public document/ADR/case study updated
  -> sanitization scan
  -> link/state review
  -> public commit
```

Do not update the portfolio first and use it to drive private production state.

## Related Documentation

- [Security Design Principles](../architecture/security-design-principles.md)
- [Architecture Overview](../architecture/architecture-overview.md)
- [Repository Security Policy](../../SECURITY.md)
- [Contributing](../../CONTRIBUTING.md)
