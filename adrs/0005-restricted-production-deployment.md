---
title: "Restricted Production Deployment Gate"
document_id: "HSP-ADR-005"
document_type: "architecture-decision-record"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
---

# ADR-0005: Restricted Production Deployment Gate

## Status

**Accepted — current architecture.**

## Context

The environment needs controlled deployment from approved Git state without turning CI into an unrestricted production administrator.

## Decision

CI may request deployment through a dedicated restricted identity. A forced deployment gate validates the request, verifies the approved Git revision, runs the production backup, reconciles allowed application stacks, checks runtime health, and rolls back on failure.

## Alternatives Considered

Unrestricted root SSH from CI was rejected. Direct workflow access to the Docker daemon was rejected. Routine manual editing of the production Compose tree was rejected because it bypasses review and makes drift harder to attribute.

## Consequences

The deployment path is more explicit and requires maintained gate logic, but it creates a narrow, auditable production authority boundary. Backup and health validation become part of the deployment transaction rather than optional operator steps.

## Validation

The feature-branch/PR/CI/approval workflow and restricted deployment path are current architecture. Runtime rollback is included in the deployment reconciler rather than delegated to arbitrary workflow commands.

## Related Documentation

- [GitOps and Isolated CI/CD](../docs/devops/gitops-ci-cd.md)
- [Backup and Recovery Architecture](../docs/recovery/backup-recovery-architecture.md)
