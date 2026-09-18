---
    title: "Cloudflare Access and Tunnel for Protected Ingress"
    document_id: "HSP-ADR-002"
    document_type: "architecture-decision-record"
    status: "current-verified"
    environment: "sanitized-public-derivative"
    last_reviewed: "2026-09-18"
    sanitization: "operational-identifiers-substituted"
    ---

    # ADR-0002: Cloudflare Access and Tunnel for Protected Ingress

    ## Status

    **Accepted — current architecture.**

    ## Context

    The environment needs remote access to selected web and administrative services without exposing the upstream router or publishing management interfaces directly to the Internet.

    ## Decision

    Externally initiated access uses Cloudflare Access and outbound Cloudflare Tunnel connectors. Normal application HTTP traffic reaches the reverse proxy through the approved edge/firewall path. Selected privileged services use separate protected tunnel paths when their trust model differs from ordinary applications.

    ## Alternatives Considered

    Direct router port forwarding was rejected because it increases exposed attack surface and moves authentication closer to private services. A VPN-only model was not selected as the sole ingress mechanism because identity-aware application access and service-specific policies are useful for the intended workflows.

    ## Consequences

    The design preserves zero public router ports and supports identity-aware access. It introduces dependency on the tunnel provider and connector health, so origin routing, firewall rules, and connector recovery must be documented and tested.

    ## Validation

    Public application access, Git SSH, Wazuh administration, and host-local AI administration have been validated through their intended protected paths without router port forwarding.

    ## Related Documentation

    - [Zero Trust Ingress](../docs/platform/zero-trust-ingress.md)
- [SSH Trust Model](../docs/security/ssh-trust-model.md)
- [Wazuh SIEM Architecture](../docs/security/wazuh-siem.md)
