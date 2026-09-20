# Project Summary

## Homelab Security Portfolio

This project documents the design and operation of a segmented homelab built as a small enterprise/cyber-range environment.

The environment combines:

- OPNsense-based VLAN segmentation;
- Proxmox virtualization;
- Docker application hosting;
- Cloudflare Access/Tunnel;
- Caddy reverse proxying;
- Forgejo source control and Actions;
- isolated CI/CD;
- Restic backup and recovery;
- Wazuh security monitoring;
- Windows and Linux administration;
- a constrained local AI platform with controlled read-only knowledge retrieval;
- planned ICS/OT and Red Team range zones.

## Engineering Focus

The project emphasizes controls and operating discipline rather than the number of hosted applications.

Key design themes include:

- default-deny east-west policy;
- no public router ports;
- separation of CI validation from production authority;
- no production Docker socket in CI;
- independent backup failure domain;
- fail-closed backup validation;
- application-consistent recovery artifacts;
- device-scoped administrative credentials;
- SIEM telemetry through narrow firewall exceptions;
- loopback-only local AI services;
- root-confined, provenance-aware read-only AI knowledge access;
- explicit current/planned/historical documentation states.

## Current Maturity

The application, CI/CD, backup, Wazuh, SSH trust, local-AI, and controlled Homelab knowledge-retrieval foundations are operational.

Open work is intentionally documented rather than hidden, including:

- selected SSH hardening;
- Wazuh continuity/retention/tuning;
- broader firewall hardening;
- Docker reproducibility debt;
- observability modernization;
- full ICS/OT/Red Team range completion;
- VLAN60 AI placement;
- domain-routing and provenance orchestration;
- controlled expansion beyond the Homelab knowledge domain;
- semantic/vector retrieval only if a later decision gate demonstrates a material need.

## Portfolio Value

The project demonstrates the ability to design, operate, troubleshoot, document, validate, and recover a multi-zone environment while preserving security boundaries and rollback capability.
