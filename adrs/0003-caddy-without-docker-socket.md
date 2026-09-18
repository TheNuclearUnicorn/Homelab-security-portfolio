---
title: "Caddy Reverse Proxy Without Docker-Socket Access"
document_id: "HSP-ADR-003"
document_type: "architecture-decision-record"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
---

# ADR-0003: Caddy Reverse Proxy Without Docker-Socket Access

## Status

**Accepted — current architecture.**

## Context

The production reverse proxy must route to Docker services. Automatic service discovery is convenient, but mounting the Docker socket into a proxy grants a process visibility and control over a root-equivalent host interface.

## Decision

Caddy uses explicit/static routing and required Docker network membership. The Docker socket is not mounted into Caddy, and the Caddy admin API remains disabled.

## Alternatives Considered

Docker-socket-based automatic discovery was rejected because the convenience did not justify host-equivalent privilege in the ingress tier. Direct application host-port publication was also rejected as the normal routing model because it bypasses the central reverse-proxy boundary.

## Consequences

Configuration changes require explicit routing updates, but the reverse proxy retains a smaller privilege surface. Service exposure is more deliberate and easier to review.

## Validation

Caddy routes current applications through internal Docker networks while operating without the Docker socket. Application services are validated through Caddy rather than by publishing arbitrary application ports.

## Related Documentation

- [Zero Trust Ingress](../docs/platform/zero-trust-ingress.md)
- [Trust Boundaries](../docs/architecture/trust-boundaries.md)
