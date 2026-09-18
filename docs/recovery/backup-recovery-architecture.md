---
title: "Backup and Recovery Architecture"
document_id: "HSP-REC-001"
document_type: "recovery-architecture"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
tags:
  - backup
  - restic
  - recovery
  - smb
  - disaster-recovery
---

# Backup and Recovery Architecture

> **Status:** Current verified production recovery architecture. The earlier same-host backup model is superseded.

## Purpose

This document describes how application state is protected outside the production Docker storage failure domain and how backup integrity is validated before a restore is trusted.

## Architecture

```mermaid
flowchart LR
    Apps["DOCKER-01<br/>production applications"]
    Stage["application-consistent staging"]
    FW["FW-01"]
    SMB["encrypted SMB 3.1.1"]
    Tier["ADMIN-WS-01<br/>independent backup tier"]
    Restic["Restic repository"]
    Restore["isolated restore tests"]

    Apps --> Stage
    Stage --> FW
    FW --> SMB
    SMB --> Tier
    Tier --> Restic
    Restic --> Restore
```

Although the backup tier shares a physical Windows host with other administrative roles, it is independent from the production Docker storage tier. The public documentation therefore describes it as an independent production failure domain rather than as a wholly independent site.

## Security Model

The backup architecture follows these controls:

- dedicated backup source identity on the production host;
- narrow firewall policy to the backup endpoint;
- SMB 3.1.1 encryption;
- root-controlled Linux credentials;
- constrained Windows service identity;
- CIFS mount hardening;
- fail-closed mount verification;
- application-aware staging;
- database logical dumps;
- integrity manifests;
- encrypted/versioned Restic repository;
- no silent local-disk fallback;
- isolated restore testing.

## Dedicated Backup Identity

The production host uses a separate network identity for backup transport.

The objective is to make firewall policy specific enough to express:

```text
backup source identity
  -> backup endpoint
  -> TCP/445 only
```

rather than allowing the entire application subnet to reach Windows file sharing.

This identity is not used as the normal application or administrative address.

## Encrypted SMB Transport

The Linux backup mount requires:

```text
SMB version: 3.1.1
encryption: required
dedicated source address: required
root ownership: required
nosuid/nodev/noexec: enabled
systemd automount: used
```

The Windows firewall and OPNsense policies both restrict the path to the intended source identity.

## Fail-Closed Mount Guard

Backup and maintenance workflows call a mount-validation guard before using the backup tier.

The guard verifies properties such as:

- expected remote source;
- CIFS filesystem;
- expected mount point;
- expected source address;
- SMB version;
- encryption;
- a sentinel identifying the correct backup root.

The safety property is:

```text
valid independent mount -> backup may proceed
missing / wrong / insecure mount -> backup fails
```

The production host must never reinterpret an ordinary local directory as the external backup tier.

## Application-Aware Backup

The backup chain captures more than raw container directories.

Current patterns include:

- Docker/platform inventory;
- application configuration/data archives;
- application-consistent capture for workloads that require it;
- PostgreSQL logical dumps for database-backed applications;
- source-control service backup;
- integrity manifest generation;
- completion-marker validation.

The exact application inventory may change over time, but the consistency and integrity model remains the architectural requirement.

## Restic

Restic provides encrypted, versioned retention on the external tier.

The active repository resides on the independent backup storage, not on Docker-local storage.

Retention is applied through scheduled maintenance rather than ad-hoc deletion.

Destructive maintenance is intentionally scheduled so that missed maintenance does not automatically execute an overdue prune immediately after downtime.

## Scheduling

The production model separates:

- regular application backup/snapshot creation;
- repository maintenance/retention.

The scheduled backup supports catch-up behavior after missed runtime where appropriate.

Repository pruning uses a more conservative schedule because destructive maintenance should not unexpectedly "catch up" after an outage.

## Restore Validation

A successful snapshot is not treated as proof of recoverability.

Restore testing validates:

- repository access;
- snapshot restoration;
- completion markers;
- integrity manifests;
- expected archives;
- logical database dumps;
- application recovery inputs.

Restore tests run into isolated paths and must not overwrite production.

## Frozen Migration Rollback

The previous Docker-local Restic repository is retained only as a historical migration rollback artifact during its governed soak/retirement process.

It is not part of normal production backup operations.

It must not receive routine:

```text
backup
forget
prune
init
```

operations.

A review date is not an automatic deletion authorization.

## Validation

Routine checks include:

```text
dedicated backup address present
normal egress still uses production identity
SMB firewall path remains narrow
SMB encryption active
mount guard passes
no local raw-staging fallback exists
integrity manifest validates
completion marker exists
Restic repository opens
recent staging set maps to a snapshot
no unexplained repository locks exist
backup timer active
maintenance timer active
time synchronization healthy
periodic isolated restore test completed
```

Negative validation is equally important:

```text
invalid backup mount -> backup must fail
missing sentinel -> backup must fail
wrong SMB source -> backup must fail
local fallback path -> must not be used
```

## Troubleshooting

Inspect in this order:

```text
production backup identity
routing
OPNsense rule
Windows firewall rule
SMB service
CIFS mount state/options
mount guard
staging output
integrity manifest
Restic repository state
systemd timer/service logs
```

Do not initialize a new repository or delete a lock until repository identity and active operations have been verified.

## Recovery / Rollback

Recovery procedures favor reconstructing runtime from:

- reviewed configuration;
- application archives;
- database logical dumps;
- Restic snapshots;
- independent backup storage.

CI infrastructure is treated as reconstructible rather than authoritative application state.

## Security Considerations

Do not publish or commit:

- SMB credentials;
- Restic passwords;
- repository IDs when unnecessary;
- snapshot IDs when unnecessary;
- backup contents;
- recovery artifacts;
- raw credential files.

## Lessons Learned

Backup reliability depends on proving that data reached the intended failure domain.

A mount that merely exists is not sufficient. Verifying mount source, encryption, identity, sentinel, and restore behavior converts a storage copy into an auditable recovery control.

## Related Documentation

- [Architecture Overview](../architecture/architecture-overview.md)
- [Trust Boundaries](../architecture/trust-boundaries.md)
- [Security Design Principles](../architecture/security-design-principles.md)
- [GitOps and Isolated CI/CD](../devops/gitops-ci-cd.md)
