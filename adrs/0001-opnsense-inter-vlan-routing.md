---
title: "OPNsense as the Authoritative Inter-VLAN Router and Firewall"
document_id: "HSP-ADR-001"
document_type: "architecture-decision-record"
status: "current-verified"
environment: "sanitized-public-derivative"
last_reviewed: "2026-09-18"
sanitization: "operational-identifiers-substituted"
---

# ADR-0001: OPNsense as the Authoritative Inter-VLAN Router and Firewall

## Status

**Accepted — current architecture.**

## Context

The environment contains multiple trust zones for applications, CI, management/security, trusted clients, IoT/guest devices, AI, ICS/OT, Red Team activity, and an OT DMZ. A single routing and policy authority is required so that east-west access remains explicit and auditable.

## Decision

OPNsense is the authoritative Layer-3 boundary for the internal VLANs. Workloads use the OPNsense interface in their zone as the default gateway. The upstream edge gateway provides transit/NAT but is not expanded into a general-purpose bypass around inter-zone policy.

## Alternatives Considered

A flat network was rejected because it collapses trust domains. Using the edge gateway as a second inter-zone router was rejected because it would create overlapping policy authorities and harder-to-audit bypass paths. Host firewalls alone were rejected as the primary segmentation control because they do not provide one consistent routing-policy boundary.

## Consequences

The design centralizes zone-to-zone policy and makes narrow source/destination/port rules possible. It also creates a dependency on the firewall for routed east-west traffic, so configuration backup and console recovery remain part of change control.

## Validation

Validated application, CI, backup, and SIEM paths traverse the firewall as intended. Negative testing is used to confirm unauthorized private-zone access remains blocked.

## Related Documentation

- [Network Segmentation](../docs/architecture/network-segmentation.md)
- [Trust Boundaries](../docs/architecture/trust-boundaries.md)
