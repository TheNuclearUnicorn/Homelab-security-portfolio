---
title: "Observability Modernization"
document_id: "HSP-CS-001"
document_type: "case-study"
status: "planned"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
tags:
  - observability
  - grafana
  - prometheus
  - docker
  - sre
---

# Observability Modernization

> **Status:** Migration case-study framework. Grafana/Prometheus are **not** represented as current production runtime. The validated pre-modernization stack is preserved as the "before" evidence until a replacement architecture is implemented and accepted.

## Purpose

This case study records the planned modernization of monitoring and observability for the homelab.

The objective is not simply to add Grafana. The work is intended to evaluate whether a small, enterprise-relevant metrics architecture can improve operational visibility without adding unnecessary complexity, widening network trust, or retiring lightweight tools that still perform their role well.

## Publication State

At the current publication checkpoint:

```text
Before / baseline evidence: AVAILABLE
Problem / motivation: DEFINED
Decision criteria: DEFINED
Migration framework: DEFINED
Validated after-state: NOT AVAILABLE
Results: NOT AVAILABLE
Final lessons learned: NOT AVAILABLE
```

No `after.md` is published yet because the target observability architecture has not been validated in runtime.

## Current Baseline

The current Docker estate includes a lightweight operational stack alongside stateful applications:

```text
Caddy
Portainer
Dozzle
Uptime Kuma
Dashy
Actual Budget
Linkwarden
PostgreSQL
Meilisearch
Forgejo
```

The current roles relevant to observability are:

| Component | Current role | Modernization disposition |
|---|---|---|
| Dashy | Human-facing service portal / homepage | **Preserve by default** |
| Portainer | Container administration | **Preserve by default** |
| Uptime Kuma | Lightweight availability/synthetic monitoring | **Evaluate against replacement capability** |
| Dozzle | Convenient live Docker log viewing | **Evaluate later** |
| Wazuh | SIEM / security telemetry | **Retain as authoritative security platform** |
| Grafana | Not current runtime | Candidate visualization/alerting layer |
| Prometheus | Not current runtime | Candidate metrics backend |
| Loki / large logging stack | Not current runtime | Deferred unless justified |

## Case-Study Structure

- [Before — Pre-Observability Baseline](before.md)
- [Architecture Decision Framework](architecture-decision.md)
- [Migration and Validation Plan](migration.md)

The following files will be added only after validated implementation:

```text
after.md
lessons-learned.md
```

The final case study will then compare actual resource use, monitoring coverage, new privileges, new firewall flows, retained tools, and retired tools.

## Governing Constraints

The modernization must preserve:

- OPNsense as the inter-zone security boundary;
- default-deny segmentation;
- the existing Cloudflare Access/Tunnel/Caddy ingress model;
- the Docker-socket privilege boundary;
- the current GitOps source tree;
- the independent backup/recovery path;
- Wazuh as the security-analysis platform;
- Dashy as the service launchpad unless evidence supports replacement.

The observability project must not broaden VLAN20 into a general monitoring bypass across private networks.

## Related Documentation

- [Architecture Overview](../../docs/architecture/architecture-overview.md)
- [Trust Boundaries](../../docs/architecture/trust-boundaries.md)
- [Network Segmentation](../../docs/architecture/network-segmentation.md)
- [Zero Trust Ingress](../../docs/platform/zero-trust-ingress.md)
- [Wazuh SIEM Architecture](../../docs/security/wazuh-siem.md)
