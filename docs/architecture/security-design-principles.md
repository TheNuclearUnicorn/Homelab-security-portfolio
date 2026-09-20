---
title: "Security Design Principles"
document_id: "HSP-ARCH-004"
document_type: "architecture"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-21"
sanitization: "operational-identifiers-substituted"
tags:
  - security
  - governance
  - change-control
  - recovery
---

# Security Design Principles

> **Status:** Current governing principles for the public architecture.

## Purpose

These principles define how infrastructure changes are designed, validated, documented, and recovered.

They are intended to prevent convenience-driven architecture from silently eroding segmentation, recoverability, or operational clarity.

## 1. Runtime Evidence Outranks Stale Documentation

Documentation is authoritative only within its validated scope and date.

When newer verified runtime evidence conflicts with an older document:

1. use the newer validated evidence for the immediate factual claim;
2. record the conflict;
3. reconcile the affected documentation;
4. do not revive an older architecture simply because it exists in historical material.

Historical build notes and troubleshooting records remain useful evidence but do not override the current validated state.

## 2. Data Integrity Before Convenience

Destructive cleanup, migration, or architecture change is not considered complete until:

- replacement functionality is validated;
- recovery or rollback exists;
- dependent services have been checked;
- protected data has not been discarded merely to simplify troubleshooting.

This principle applies to firewall changes, backup migration, GitOps reconciliation, application state, knowledge migration, and AI integration.

## 3. Least Privilege and Segmentation

OPNsense remains the authoritative inter-zone boundary.

Permanent policy favors:

```text
required infrastructure access
explicit approved inter-zone access
private-network isolation
controlled egress
default deny
```

Broad `any -> any` rules are not accepted as a permanent architecture.

Temporary troubleshooting access must not silently become baseline policy.

## 4. Zero Public Router Ports

Normal public access uses identity-aware tunnel ingress rather than inbound router port forwarding.

The application pattern is:

```text
Cloudflare Access
  -> Cloudflare Tunnel
  -> edge connector
  -> OPNsense
  -> reverse proxy
  -> application
```

Privileged services may use separate protected tunnel paths when required, but this does not justify public router exposure.

## 5. Git Is Configuration, Not State

Git may contain:

- Compose definitions;
- infrastructure scripts;
- documentation;
- reviewed configuration.

Git must not contain:

- passwords or tokens;
- private keys;
- `.env` contents;
- databases;
- application data;
- backup contents;
- Restic repositories;
- recovery artifacts.

Desired state and runtime state are separate concerns.

## 6. CI Is Untrusted Execution Infrastructure

Repository workflows can execute code and therefore must not inherit production trust.

CI remains:

- isolated;
- capacity constrained;
- without the production Docker socket;
- without unrestricted production shell access;
- without a bastion role.

Production deployment authority is mediated through a restricted interface that validates the requested revision and performs backup, reconciliation, health checking, and rollback.

## 7. Backups Require an Independent Failure Domain

A backup stored only on production storage is insufficient disaster recovery.

The authoritative backup design therefore crosses into a separate storage tier through a narrow encrypted transport and must fail closed when that tier is unavailable.

Recovery capability is validated through restore tests rather than inferred from successful backup creation.

## 8. Administrative Credentials Are Device-Scoped

Independent administration workstations maintain independent SSH keys and Git working copies.

Private keys are not synchronized between endpoints.

This supports per-device revocation and reduces the blast radius of workstation compromise.

## 9. AI Is Not an Infrastructure Control Plane

The local AI environment may inspect approved derived data through a constrained, profile-aware interface backed by deterministic export and provenance/state controls.

The live canonical knowledge source is not exposed directly to the model-facing retrieval boundary. Domain access is explicit and fail-closed rather than inferred from semantic similarity.

The current model-facing architecture also uses deterministic bounded orchestration. A request is routed only to an approved Homelab agent and retrieval profile, with provenance validation retained underneath the routing layer.

The orchestration layer does not replace or bypass the read-only retrieval boundary.

It must not gain unrestricted capability to:

- write authoritative documentation;
- execute shell commands;
- scan networks;
- modify production configuration;
- browse arbitrary host paths;
- bridge security zones.

Retrieved content is untrusted input, not an instruction source.

## 10. Validate Positive and Negative Behavior

A successful connection proves only that required traffic works.

Security acceptance also requires testing that prohibited behavior fails.

Examples:

```text
required service succeeds
unauthorized lateral connection fails
approved deployment works
interactive CI shell fails
backup succeeds with valid mount
backup fails with invalid mount
read-only AI retrieval succeeds
stale/deleted current-state retrieval fails
disabled-domain retrieval fails
approved orchestration route succeeds
unsupported-domain route fails
cross-domain route without approval fails
agent/profile boundary violation fails
orchestration rollback preserves read-only retrieval baseline
AI write/execute capability remains unavailable
```

Negative tests are part of the design, not optional troubleshooting.

## 11. Troubleshoot Before Redesigning

When a service fails, inspect the existing dependency chain first:

```text
addressing
routing
DNS
firewall
service state
logs
```

Do not weaken segmentation, publish ports, change architecture, or bypass controls merely to make a test pass.

## 12. Change One Dependency at a Time

Before risky changes:

1. verify service health;
2. confirm backup/recovery state;
3. preserve configuration backups;
4. take a hypervisor snapshot when appropriate;
5. change one dependency or control group;
6. validate;
7. retain rollback until acceptance.

This makes failure attribution possible and reduces compound-risk troubleshooting.

## 13. Current, Historical, and Planned State Must Stay Distinct

Public documentation uses explicit state labels.

- **Current / verified** describes validated runtime.
- **Current with open items** describes working architecture with known debt.
- **Historical baseline** preserves useful engineering evidence but is not current.
- **Planned** describes future work only.

Grafana/Prometheus modernization, full ICS/OT range completion, Red Team integration, VLAN60 AI placement, and expansion beyond the Homelab knowledge domain are not represented as current until validated.

The controlled Homelab knowledge/RAG baseline is current and validated. Semantic/vector retrieval remains deliberately deferred unless a later decision gate demonstrates material value.

Bounded Homelab orchestration is current and validated. It uses deterministic routing, bounded agent/profile selection, provenance enforcement, negative testing, and rollback to the prior direct read-only MCP baseline.

## 14. Sanitization Must Preserve Engineering Value

Public documentation removes reconnaissance value without erasing technical substance.

Retained where useful:

- VLAN roles;
- trust relationships;
- protocol/port intent;
- validation methods;
- rollback design;
- CI isolation;
- backup failure behavior;
- reverse-proxy and tunnel architecture;
- lessons learned.

Removed or substituted:

- live IP addresses;
- actual public DNS;
- private usernames;
- key fingerprints;
- credentials;
- recovery artifacts;
- exact secret filenames;
- raw firewall/router backups;
- private filesystem identities.

## Related Documentation

- [Architecture Overview](architecture-overview.md)
- [Network Segmentation](network-segmentation.md)
- [Trust Boundaries](trust-boundaries.md)
