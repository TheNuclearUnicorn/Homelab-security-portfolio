---
title: "Local AI Security Boundary"
document_id: "HSP-SEC-003"
document_type: "security-architecture"
status: "current-with-open-items"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-20"
sanitization: "operational-identifiers-substituted"
tags:
  - local-ai
  - ollama
  - hermes
  - mcp
  - zero-trust
---

# Local AI Security Boundary

> **Status:** Current Windows-native local AI and controlled Homelab knowledge-retrieval baseline are operational. VLAN60 placement and broader domain-routing/provenance orchestration remain planned. Semantic/vector retrieval was evaluated and deliberately deferred.

## Purpose

This document describes how the local AI environment is prevented from becoming an uncontrolled infrastructure control plane.

The core requirement is:

```text
AI may inspect approved data.
AI must not receive unrestricted authority over infrastructure or source knowledge.
```

## Current Architecture

```mermaid
flowchart TD
    User["Remote administrator"]
    Access["Cloudflare Access"]
    Tunnel["Host-local Cloudflare Tunnel"]
    Dashboard["Hermes dashboard<br/>loopback only"]
    Model["Ollama<br/>loopback only"]
    MCP["bounded read-only MCP<br/>local stdio"]
    Retrieval["profile-aware retrieval"]
    Mirror["derived knowledge mirror"]
    Controls["provenance / lifecycle state"]
    Canonical["canonical human knowledge<br/>not model-visible"]

    User --> Access
    Access --> Tunnel
    Tunnel --> Dashboard
    Dashboard --> Model
    Dashboard --> MCP
    MCP --> Retrieval
    Retrieval --> Mirror
    Retrieval --> Controls
    Canonical -->|"controlled default-deny export"| Mirror
    Canonical -->|"export metadata only"| Controls
```

The AI runtime currently shares `ADMIN-WS-01` with other administrative roles. It is not represented as already migrated into VLAN60.

The live canonical knowledge estate is not exposed directly to the model or MCP service. Retrieval operates against a derived, rebuildable mirror plus copied control metadata used for provenance and lifecycle enforcement.

## Model Runtime Boundary

Ollama listens only on loopback.

The model-facing API is therefore available to local processes but not directly to the LAN.

The current primary model is a local Qwen 3.5 deployment with an operational 64K context. The exact model build and storage paths are intentionally omitted from the public derivative because they are implementation details rather than trust boundaries.

## Dashboard Boundary

Hermes also listens only on loopback.

Remote access is provided through a host-local Cloudflare Tunnel protected by Cloudflare Access and the dashboard's own authentication layer.

The origin remains loopback, so remote administration does not require:

- a LAN listener;
- public router forwarding;
- exposing Ollama directly;
- routing through the production Docker/Caddy application plane.

The dashboard is treated as a privileged management surface rather than as a normal public application.

## Tool-Surface Restriction

The validated dashboard process is explicitly restricted to the approved read-only MCP surface.

Broad native tool families are not exposed to the validated model session.

The allowed MCP service exposes only:

```text
list approved sources
read approved knowledge file
search approved knowledge
```

It does not expose:

- write/create/patch;
- delete/rename/move;
- shell or PowerShell;
- process execution;
- browser control;
- desktop control;
- arbitrary host-path reads;
- network scanning;
- infrastructure actions.

## Read-Only MCP Boundary

The MCP service uses local `stdio`, not a network listener.

Approved roots are derived AI knowledge and observation trees, not the live canonical knowledge estate.

Security validation covered:

- path traversal;
- absolute paths;
- junction/reparse-point escape;
- unsupported extensions;
- protocol error handling;
- live read/search behavior;
- denial behavior through the model/dashboard path.

The MCP service is therefore a data-inspection boundary, not a file-management interface.

## Untrusted Retrieved Content

Retrieved documents are treated as untrusted data.

A document can describe a command or instruct an operator to modify infrastructure, but that text does not become model authority to execute the command or widen permissions.

Runtime evidence and validated runbooks remain higher-precedence operational sources.

## Current Remote-Access Controls

Required layers:

```text
Cloudflare Access
  -> Cloudflare Tunnel
  -> loopback-only Hermes origin
  -> dashboard authentication
  -> process-scoped tool restriction
  -> read-only MCP
```

Removing one layer is not assumed safe merely because the others remain.

## Persistence

The validated design restores the model runtime and dashboard through controlled Windows startup mechanisms.

Reboot validation confirmed:

- Ollama returns;
- Hermes dashboard returns;
- loopback-only listeners are preserved;
- the host-local tunnel service returns;
- remote inference still works;
- no visible persistent console is required.

## Controlled Knowledge / RAG Baseline

The Homelab knowledge-ingestion baseline is accepted and operational.

The design deliberately separates:

```text
canonical human knowledge
    -> controlled default-deny export
    -> derived read-only mirror
    -> profile-aware MCP retrieval
    -> model
```

The model-facing retrieval layer does not receive direct access to the live canonical source tree.

The accepted baseline includes:

- deterministic export of approved Homelab material;
- default-deny source eligibility;
- staged publication of a new derived generation;
- durable source identity and content-hash provenance;
- lifecycle/state tracking for current, stale, deleted, and renamed material;
- explicit domain enablement rather than similarity-based cross-domain access;
- profile-aware retrieval for current-state, planning, troubleshooting, recovery, historical, and reconciliation use cases;
- provenance enforcement outside the model-visible knowledge roots;
- fail-closed behavior for disabled domains and excluded source classes.

Current-state retrieval specifically rejects records that are no longer eligible because they are stale, deleted, disabled, or otherwise outside the approved current-state profile.

Retrieved text remains untrusted data. A retrieved document cannot grant itself tool authority, execute a command, widen a filesystem boundary, or convert planning content into implemented runtime state.

### Semantic / Vector Retrieval Decision

A semantic/vector backend was evaluated but is not part of the accepted baseline.

The validated lexical/profile-aware design met the current Homelab retrieval requirement without introducing an additional index, recovery dependency, or provenance-synchronization problem.

Vector retrieval is therefore **deferred by design**, not an unfinished prerequisite.

It should be reconsidered only if measured retrieval quality, corpus heterogeneity, or a later approved routing/orchestration use case demonstrates a material need.

## VLAN60 Target State

VLAN60 exists as the intended long-term AI security zone.

The current runtime remains Windows-native on `ADMIN-WS-01`.

Future documentation may move the AI runtime into VLAN60 only after:

- attachment is implemented;
- explicit allowed flows are defined;
- denied flows are tested;
- required monitoring is validated;
- rollback is available.

## Validation

Current expected outcomes:

```text
Ollama listener -> loopback only
Hermes listener -> loopback only
remote dashboard through Access/Tunnel -> PASS
direct LAN listener -> absent
MCP network listener -> absent

approved knowledge list/read/search -> PASS
write/delete/shell/browser/control capability through MCP -> unavailable
broad native model toolsets in restricted dashboard session -> unavailable

deterministic approved-source export -> PASS
staged derived-generation publication -> PASS
provenance/state enforcement -> PASS
current/planning/troubleshooting/recovery/historical/reconciliation profiles -> PASS

path traversal / absolute-path / junction escape -> DENIED
disabled-domain retrieval -> DENIED
secret-class retrieval -> DENIED
stale/deleted current-state retrieval -> DENIED
cross-domain retrieval without approval -> DENIED
prompt-injection-triggered shell execution -> DENIED

derived-corpus rebuild -> PASS
prior-generation rollback -> PASS
reboot recovery -> PASS
```

## Troubleshooting

Inspect in this order:

```text
Ollama service/listener
Hermes process/listener
dashboard authentication
Cloudflare tunnel/service
process-scoped tool restriction
MCP registration
MCP stdio process
approved root existence
path-policy validation
model request
```

Do not expose Ollama or Hermes on `0.0.0.0` merely to work around a tunnel or dashboard problem.

## Rollback / Recovery

Recovery boundaries are intentionally staged:

1. restore the known-good local Ollama runtime;
2. restore the known-good Hermes configuration;
3. restore the validated bounded read-only MCP service;
4. rebuild the derived knowledge mirror from approved canonical sources;
5. validate provenance/state metadata before publication;
6. validate profile-aware retrieval and negative tests;
7. if the new generation fails acceptance, restore the prior accepted derived generation;
8. validate local restricted inference;
9. restore persistent dashboard startup;
10. restore protected remote access;
11. revalidate the restricted tool surface.

This keeps the derived AI corpus rebuildable and prevents recovery of the model-facing layer from redefining canonical human-source authority.

## Security Considerations

Do not publish or commit:

- OAuth/client secrets;
- tunnel tokens;
- private certificate material;
- local authentication tokens;
- exact private filesystem roots;
- raw source-knowledge contents;
- hashes that expose unnecessary operational artifacts;
- private source manifests that expose live internal paths;
- raw provenance inventories containing operationally sensitive filenames;
- excluded-domain contents;
- stale/deleted source payloads retained only for private rollback;
- private corpus generations or recovery checkpoints.

## Lessons Learned

"Local AI" is not automatically low risk.

The critical security question is not only where the model runs, but what tools, files, network paths, and write capabilities the model can reach. A loopback-only runtime with a root-confined read-only MCP creates a substantially different risk profile from a model with shell and unrestricted filesystem tools.

A useful RAG boundary is not defined only by whether retrieval works. It is defined by whether source eligibility, lifecycle, provenance, stale-state handling, rollback, and negative security behavior remain deterministic.

For this environment, a smaller lexical/profile-aware baseline with explicit provenance was preferable to adding vector infrastructure before a measured retrieval need justified it.

## Future Work

The following remain planned rather than implemented:

- domain-routing and provenance orchestration;
- controlled expansion beyond the Homelab domain;
- independent policy and negative tests for each newly approved domain;
- dedicated VLAN60 placement and policy validation;
- semantic/vector retrieval only if a later decision gate demonstrates a material requirement.

Personal content remains outside general AI retrieval. Other domains remain disabled until explicitly approved.

## Related Documentation

- [Architecture Overview](../architecture/architecture-overview.md)
- [Trust Boundaries](../architecture/trust-boundaries.md)
- [Security Design Principles](../architecture/security-design-principles.md)
- [Zero Trust Ingress](../platform/zero-trust-ingress.md)
