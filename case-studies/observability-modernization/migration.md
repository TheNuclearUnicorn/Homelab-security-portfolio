---
title: "Observability Modernization — Migration and Validation Plan"
document_id: "HSP-CS-001-MIGRATION"
document_type: "case-study-plan"
status: "planned"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
tags:
  - observability
  - migration
  - validation
  - rollback
  - grafana
  - prometheus
---

# Migration and Validation Plan

> **Status:** Planned migration framework. The steps below are acceptance gates for future implementation, not a record of completed Grafana/Prometheus deployment.

## Objective

Introduce enterprise-relevant metrics capability incrementally while preserving current production behavior, segmentation, recovery controls, and useful lightweight tooling.

## Phase 1 — Audit Only

Do not install or remove services.

Capture:

- Docker host CPU/RAM/storage baseline;
- per-container CPU/RAM/storage;
- current container health;
- Uptime Kuma checks;
- Dashy role and links;
- Dozzle operational use;
- Portainer operational use;
- current Docker socket mounts;
- Caddy routing;
- available Docker host resources;
- existing monitoring capabilities on edge, hypervisor, firewall, Docker, CI, SIEM, and Windows systems;
- existing metrics/exporter endpoints;
- current firewall restrictions.

Outputs:

```text
current-state monitoring diagram
monitoring coverage matrix
container redundancy matrix
recommended observability placement
candidate initial architecture
estimated resources
required firewall flows
candidate retirement list
definite-retain list
```

No production modification occurs in this phase.

## Phase 2 — Architecture Approval

Document and approve:

- Grafana role;
- Prometheus role;
- each exporter/integration;
- Dashy role;
- Portainer role;
- Uptime Kuma disposition;
- Dozzle disposition;
- Wazuh relationship;
- telemetry storage location;
- retention;
- remote Grafana access model, if any;
- cross-VLAN firewall flows;
- Git-provisioned configuration;
- recovery model.

The chosen design should be the smallest architecture that still provides meaningful metrics and SRE experience.

## Phase 3 — Recovery Checkpoint

Before production changes:

1. verify current application health;
2. verify the independent backup mount;
3. confirm a recent application-aware backup and Restic snapshot;
4. preserve current Compose/Caddy/firewall state;
5. take a hypervisor snapshot if risk justifies it.

Do not mix backup redesign with observability deployment.

## Phase 4 — Core Metrics Deployment

After approval:

- deploy only the approved Prometheus/Grafana core;
- use the existing GitOps/Compose source tree;
- place persistent state in the established application-data model;
- keep secrets outside Git;
- attach only required Docker networks;
- avoid new Docker-socket privileges;
- expose Grafana only through the established protected ingress model if remote access is approved;
- do not expose Prometheus/exporters publicly.

Validate the core before adding broad coverage.

## Phase 5 — Monitoring Coverage Expansion

Add monitoring one domain at a time.

Candidate domains:

```text
edge gateway
hypervisor
firewall
Docker host
Docker workloads
CI runner
SIEM server
Windows / Hyper-V
Caddy
PostgreSQL
Forgejo
backup infrastructure
```

For each target:

1. identify metric source/exporter;
2. identify collection direction;
3. identify exact source/destination/port;
4. implement only the narrow firewall rule required;
5. validate metric quality;
6. validate expected blocked paths remain blocked;
7. document the dependency.

## Phase 6 — Dashboards and Alerting

Develop functional dashboards rather than one monolithic dashboard.

Candidate views:

```text
Executive / NOC
Infrastructure
Docker / Applications
Network
DevOps
Backup / Recovery
Security / SIEM operational summaries
```

Alerting should start with actionable conditions, such as:

- host/resource saturation;
- monitored target unavailable;
- backup age beyond threshold;
- backup failure;
- storage capacity risk;
- critical ingress/service loss;
- CI/deployment health failures.

Alert volume and quality must be measured before expanding coverage.

## Phase 7 — Container Rationalization

Do not retire tools merely because Grafana/Prometheus exists.

### Dashy

Default:

```text
KEEP
```

### Portainer

Default:

```text
KEEP
```

### Uptime Kuma

Retirement gate:

```text
replacement synthetic checks mapped one-for-one
replacement alerts validated
historical/operational needs covered
soak period passed
```

Otherwise retain.

### Dozzle

Retirement gate:

```text
centralized logging architecture exists
operator workflow is demonstrably better
privilege does not increase unjustifiably
resource/storage cost is acceptable
```

Otherwise retain.

## Phase 8 — Before / After Measurement

Capture the same measurements used in the baseline.

Compare:

| Dimension | Before | After |
|---|---:|---:|
| Component count | measured | measured |
| Steady-state RAM | measured | measured |
| Steady-state CPU | measured | measured |
| Storage consumption | measured | measured |
| Persistent-data growth | measured | measured |
| Cross-zone monitoring flows | measured | measured |
| New firewall rules | measured | measured |
| New privileged mounts | measured | measured |
| Availability coverage | inventoried | inventoried |
| Alert coverage | inventoried | inventoried |

Do not claim resource savings or reduced complexity unless the measured comparison supports the claim.

## Phase 9 — Soak and Acceptance

Before changing public documentation to "current":

- monitoring remains stable through the soak period;
- Prometheus retention behaves as designed;
- dashboards remain usable;
- alerting is actionable;
- backups still pass;
- CI/deployment behavior remains unaffected;
- Caddy/Cloudflare ingress remains correct;
- cross-zone rules remain narrow;
- retained tools have explicit roles;
- any retired tool has a validated replacement.

Only after these checks can `after.md` be created.

## Rollback

Rollback should preserve the existing lightweight tools until replacement capability is proven.

If the new metrics stack causes instability:

1. disable or remove the new observability services;
2. revert changed Caddy/firewall rules;
3. restore previous Compose state;
4. verify existing applications and lightweight monitoring;
5. retain collected evidence for redesign.

Do not delete current monitoring configuration in the same change that introduces its replacement.

## Publication Gate

The public portfolio remains in this state until validated runtime evidence exists:

```text
before.md                    publishable
architecture-decision.md    publishable as planned framework
migration.md                publishable as planned framework
after.md                     WITHHELD
lessons-learned.md          WITHHELD
current observability doc   WITHHELD
```

## Related Documentation

- [Observability Modernization](homelab-security-portfolio-stage7/case-studies/observability-modernization/README.md)
- [Before — Pre-Observability Baseline](before.md)
- [Architecture Decision Framework](architecture-decision.md)
- [Security Design Principles](../../docs/architecture/security-design-principles.md)
- [GitOps and Isolated CI/CD](../../docs/devops/gitops-ci-cd.md)
- [Backup and Recovery Architecture](../../docs/recovery/backup-recovery-architecture.md)
