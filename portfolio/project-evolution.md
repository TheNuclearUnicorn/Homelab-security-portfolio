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

The local AI environment progressed from a loopback-only local model to:

- persistent local inference;
- a protected loopback-only web dashboard;
- Cloudflare-protected remote administration;
- a root-confined read-only MCP;
- approved derived knowledge roots.

The current model is intentionally not an infrastructure control plane.

## Current Transition

Observability modernization is in planning/audit state.

The portfolio preserves the pre-modernization baseline and decision framework but does not claim Grafana/Prometheus as current production runtime.

## Future Program Work

Planned work includes:

- validated observability modernization;
- full ICS/OT cyber-range workload implementation;
- Red Team exercise integration;
- VLAN60 AI placement;
- semantic RAG/provenance/recovery completion.

These remain roadmap items until implemented and validated.
