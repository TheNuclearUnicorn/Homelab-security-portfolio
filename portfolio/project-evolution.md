# Project Evolution

This portfolio intentionally distinguishes validated implementation from roadmap work.

## Foundation

The environment established:

- a dedicated lab transit network;
- Proxmox virtualization;
- OPNsense as the inter-zone router/firewall;
- VLAN-based security zones.

## Application Platform

The production application zone added:

- an Ubuntu Docker host;
- separate Docker infrastructure/application/data networks;
- Caddy reverse proxying;
- Cloudflare-protected ingress;
- stateful self-hosted applications.

## Recovery Maturity

Backup design evolved from same-host protection to an external failure domain.

The resulting architecture added:

- dedicated backup network identity;
- narrow SMB policy;
- SMB 3.1.1 encryption;
- fail-closed mount validation;
- application-aware staging;
- Restic retention;
- isolated restore testing.

## DevOps Maturity

Source control evolved into a controlled GitOps/CI workflow:

```text
workstation
  -> feature branch
  -> pull request
  -> isolated CI
  -> approval
  -> restricted production reconciliation
```

The CI runner is deliberately prevented from becoming production root.

## Security Monitoring

Wazuh was introduced in the management/security zone with:

- endpoint agents;
- OPNsense firewall-log ingestion;
- Cloudflare-protected administration;
- source-specific firewall rules;
- host firewall defense in depth.

Recovery, retention, tuning, and notifications remain open maturity work.

## Local AI Boundary

The local AI environment progressed from a loopback-only local model to a governed read-only retrieval and orchestration plane with:

- persistent local inference;
- a protected loopback-only web dashboard;
- Cloudflare-protected remote administration;
- a root-confined read-only retrieval MCP;
- a deterministic default-deny knowledge export;
- a derived, rebuildable knowledge mirror;
- durable provenance and lifecycle state;
- profile-aware retrieval;
- stale/deleted/disabled-domain denial;
- prompt-injection and boundary negative testing;
- tested corpus rebuild and prior-generation rollback;
- a bounded model-facing orchestration MCP;
- deterministic routing to five Homelab agents;
- explicit agent-to-retrieval-profile binding;
- auditable route decisions;
- provenance validation through the orchestrated path;
- tested rollback from orchestration to the prior direct-MCP baseline.

The current model remains intentionally outside the infrastructure control plane, and the canonical human knowledge estate is not exposed directly to either the router or retrieval MCP.

Prompt 03 did not expand the enabled knowledge domain beyond Homelab.

Semantic/vector retrieval remains deliberately deferred because neither Prompt 02 nor Prompt 03 demonstrated a measured need that justified the additional indexing and recovery complexity.

## Current Transition

Observability modernization is in planning/audit state.

The portfolio preserves the pre-modernization baseline and decision framework but does not claim Grafana/Prometheus as current production runtime.

## Future Program Work

Planned work includes:

- validated observability modernization;
- full ICS/OT cyber-range workload implementation;
- Red Team exercise integration;
- VLAN60 AI placement;
- controlled one-domain-at-a-time knowledge expansion beyond Homelab;
- semantic/vector retrieval only if a later measured requirement justifies it.

These remain roadmap items until implemented and validated.
