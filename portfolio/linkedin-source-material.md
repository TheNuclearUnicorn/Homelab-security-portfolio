# LinkedIn / Portfolio Source Material

This file contains factual source material for shorter public posts. It avoids claims beyond the validated architecture.

## One-Line Project Description

Designed and operated a segmented security-focused homelab combining Zero Trust ingress, isolated CI/CD, independent recovery, centralized security monitoring, and a constrained local-AI boundary.

## Short Portfolio Summary

Built a small enterprise-style homelab with OPNsense VLAN segmentation, Proxmox virtualization, Docker application hosting, Cloudflare Access/Tunnel, Forgejo GitOps, isolated CI, Restic recovery, Wazuh SIEM, and local AI tooling.

The focus is not simply self-hosting. The environment is designed around least privilege, narrow firewall rules, controlled production deployment, independent recovery, negative security testing, and explicit trust boundaries.

## Technical Highlights

- segmented application, CI, management/security, AI, ICS/OT, Red Team, and OT-DMZ zones;
- zero public router ports;
- Cloudflare-protected application and administrative ingress;
- Caddy reverse proxy without Docker-socket access;
- isolated CI runner with no production Docker socket;
- restricted production deployment with backup, health validation, and rollback;
- encrypted SMB backup path into an independent production-storage failure domain;
- Restic retention and restore testing;
- Wazuh agents plus OPNsense firewall-log ingestion;
- independently revocable administrative workstation SSH identities;
- loopback-only Ollama/Hermes runtime;
- root-confined read-only MCP for approved AI knowledge access;
- lifecycle-aware documentation governance and ADRs.

## Safe Roadmap Language

### Observability

> I am evaluating an observability modernization using Prometheus and Grafana, with a focus on measurable operational value, narrow cross-zone telemetry flows, and avoiding unnecessary Docker-socket privilege.

Do not state that Grafana/Prometheus are deployed until runtime validation is complete.

### Cyber Range

> The network zones for ICS/OT, Red Team, and an OT DMZ are established as part of the architecture, while the full exercise workload remains future program work.

### Local AI

> The local AI platform is operational on a Windows GPU host with loopback-only services and read-only knowledge access; migration into the dedicated AI VLAN remains planned.

## Evidence-Backed Resume Bullets

- Designed a multi-zone OPNsense network architecture with explicit trust boundaries for applications, CI, security monitoring, AI, ICS/OT, Red Team, and OT-DMZ workloads.
- Implemented Cloudflare Access/Tunnel ingress with zero public router ports and a Caddy reverse-proxy tier that does not mount the Docker socket.
- Built an isolated CI/CD workflow using Forgejo and Docker-in-Docker while preventing CI access to the production Docker socket and unrestricted production shell.
- Implemented a restricted production deployment gate with approved-revision verification, pre-deployment backup, runtime health checks, and rollback.
- Migrated application backups to an independent encrypted SMB/Restic tier with fail-closed mount validation and isolated restore testing.
- Integrated Wazuh endpoint telemetry and OPNsense firewall logs through narrow source-specific network policy.
- Implemented a loopback-only local AI environment with a root-confined, read-only MCP interface for approved knowledge retrieval.
- Established lifecycle-aware technical documentation governance with source precedence, ADRs, sanitized publication rules, and explicit current/planned/historical states.
