---
title: "Isolated CI Without the Production Docker Socket"
document_id: "HSP-ADR-004"
document_type: "architecture-decision-record"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
---

# ADR-0004: Isolated CI Without the Production Docker Socket

## Status

**Accepted — current architecture.**

## Context

CI workflows execute repository-controlled code and therefore must be treated as remote-code-execution infrastructure. Giving a runner the production Docker socket would effectively provide production-root authority to workflow jobs.

## Decision

The CI runner is isolated in its own VLAN, constrained in capacity, and uses Docker-in-Docker for job execution. It does not receive the production Docker socket, arbitrary host bind mounts, unrestricted production shell access, or a bastion role.

## Alternatives Considered

Running CI directly on the production Docker host was rejected. Mounting the production Docker socket into workflow jobs was rejected. Using the CI host as an administrative jump host was rejected because those patterns collapse the separation between validation and production control.

## Consequences

The runner remains rebuildable and disposable. Additional deployment mediation is required because CI cannot directly control production. This increases implementation complexity but reduces compromise blast radius.

## Validation

Repository workflows have been validated on the isolated runner, while production modification occurs through a separate restricted path. The security model explicitly prohibits runner access to the production Docker socket.

## Related Documentation

- [GitOps and Isolated CI/CD](../docs/devops/gitops-ci-cd.md)
- [Trust Boundaries](../docs/architecture/trust-boundaries.md)
