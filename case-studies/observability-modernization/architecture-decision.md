---
title: "Observability Modernization — Architecture Decision Framework"
document_id: "HSP-CS-001-DECISION"
document_type: "case-study-decision"
status: "planned"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
tags:
  - grafana
  - prometheus
  - architecture-decision
  - observability
  - least-privilege
---

# Architecture Decision Framework

> **Status:** Decision framework only. No final Grafana/Prometheus placement or exporter set is represented as approved runtime until the audit and architecture-approval checkpoints are complete.

## Problem

The current lightweight monitoring model provides useful operational functions but does not yet provide a centralized infrastructure-metrics architecture suitable for:

- cross-system resource trends;
- PromQL-based analysis;
- structured operations dashboards;
- metric-driven alerting;
- capacity tracking;
- backup age/health visualization;
- CI/deployment health visibility;
- network trend analysis;
- SLI/SLO-style thinking.

The modernization must improve those capabilities without replacing useful tools solely for technology-fashion reasons.

## Candidate Core Stack

The first candidate architecture is intentionally narrow:

```text
Prometheus
  -> metrics collection / storage / query backend

Grafana
  -> dashboards / visualization / alerting
```

Only exporters or integrations needed for useful metrics should be added.

The initial phase explicitly does **not** assume deployment of:

```text
Loki
Tempo
Mimir
large OpenTelemetry pipelines
```

Centralized logging remains a later decision.

## Control-Plane Placement Decision

The observability control plane must be placed only after comparing at least:

### Option A — Existing application Docker host / VLAN20

Advantages to evaluate:

- lowest additional infrastructure footprint;
- existing GitOps/Compose workflow;
- existing backup integration;
- existing Caddy ingress path.

Risks to evaluate:

- monitoring control plane shares the application failure domain;
- central polling may require new cross-zone rules from VLAN20;
- resource pressure on an 8-GB production Docker VM;
- observability outage during Docker-host incidents may reduce diagnostic value.

### Option B — Dedicated observability VM

Advantages to evaluate:

- separates observability from the application host;
- clearer monitoring failure domain;
- potentially cleaner cross-zone source identity;
- easier resource accounting.

Costs to evaluate:

- additional VM resources;
- additional patching and backup surface;
- new ingress/recovery considerations;
- another privileged visibility system to secure.

### Option C — Alternative architecture

An alternative may be accepted if it better preserves segmentation with lower complexity.

Examples could include push/agent patterns or selected platform-native integrations, but the final choice must be supported by runtime evidence and explicit firewall analysis.

## Cross-Zone Monitoring Rule

A central metrics collector must not receive broad access such as:

```text
monitoring source -> all RFC1918
```

Permitted design pattern:

```text
specific monitoring source
  -> specific monitored host
  -> specific exporter / metrics port
```

OPNsense remains the inter-zone authority.

If an agent/push model materially reduces trust expansion, its operational tradeoffs should be compared rather than assuming pull is always superior.

## Docker-Socket Decision

Treat:

```text
/var/run/docker.sock
```

as host-equivalent privilege.

Current accepted privileged exceptions remain limited to tools whose existing function requires it.

The following do not automatically receive Docker-socket access:

```text
Grafana
Prometheus
exporters
Loki
Alloy
Caddy
CI jobs
```

If a collector requires Docker API visibility, safer metric interfaces must be evaluated first.

## Component Disposition

### Dashy — Preserve by default

Reason:

```text
service portal / homepage != observability dashboard
```

Grafana may be linked from Dashy, and Grafana may link back to Dashy.

### Portainer — Preserve by default

Reason:

```text
container administration != observability
```

Grafana does not replace the container-management role.

### Uptime Kuma — Evaluate

Retire only after replacement capability is validated one-for-one.

Compare:

- synthetic monitoring;
- alert quality;
- historical availability;
- operational simplicity;
- resource use;
- maintenance burden;
- portfolio/enterprise value.

### Dozzle — Evaluate later

Dozzle remains useful for immediate live container logs.

Do not deploy Loki or another logging platform solely to justify removing it.

### Wazuh — Retain

Wazuh remains the authoritative security-analysis platform.

Grafana may eventually display selected summaries if that adds correlation value without weakening the SIEM boundary.

## Target Dashboard Domains to Evaluate

The future Grafana design should evaluate separate functional dashboards rather than one oversized page:

- Executive / NOC overview;
- infrastructure;
- Docker/applications;
- network;
- DevOps;
- backup/recovery;
- selected security/operational summaries.

This is a target design requirement, not proof that those dashboards exist.

## Data Retention

Prometheus retention must be explicitly bounded.

The final architecture must distinguish:

```text
rebuildable telemetry
```

from:

```text
configuration / dashboards / alerts that require durable recovery
```

Version-controlled provisioning is preferred where practical.

Do not back up regenerable metric history simply because it exists.

## GitOps Requirement

Where practical, maintain as reviewed configuration:

- Prometheus scrape configuration;
- Grafana datasource provisioning;
- dashboard definitions;
- alert rules;
- Compose definitions.

Secrets remain outside Git.

GUI-only configuration should be minimized when a reproducible equivalent exists.

## Decision Gate

A final ADR should be written only after runtime audit answers:

1. where the control plane will live;
2. what systems will be monitored first;
3. which exporters/integrations are actually required;
4. what firewall flows are needed;
5. expected memory/storage cost;
6. Prometheus retention;
7. whether Uptime Kuma remains;
8. whether Dozzle remains;
9. how observability state is recovered;
10. whether remote Grafana access is justified.

Until then, this document is a decision framework rather than a completed ADR.

## Related Documentation

- [Before — Pre-Observability Baseline](before.md)
- [Migration and Validation Plan](migration.md)
- [Network Segmentation](../../docs/architecture/network-segmentation.md)
- [Trust Boundaries](../../docs/architecture/trust-boundaries.md)
- [Backup and Recovery Architecture](../../docs/recovery/backup-recovery-architecture.md)
