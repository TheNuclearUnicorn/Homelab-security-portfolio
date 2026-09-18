---
    title: "Root-Confined Read-Only AI Knowledge Boundary"
    document_id: "HSP-ADR-007"
    document_type: "architecture-decision-record"
    status: "current-verified"
    environment: "sanitized-public-derivative"
    last_reviewed: "2026-09-18"
    sanitization: "operational-identifiers-substituted"
    ---

    # ADR-0007: Root-Confined Read-Only AI Knowledge Boundary

    ## Status

    **Accepted — current architecture.**

    ## Context

    The local AI environment needs access to approved documentation while avoiding the risk that model tools become a shell, file-management interface, or uncontrolled bridge into infrastructure and canonical knowledge sources.

    ## Decision

    The model-facing knowledge interface is a local stdio MCP service restricted to approved derived roots. The exposed capability surface is limited to source listing, file reading, and search. Write, delete, rename, shell, browser/desktop control, arbitrary host-path access, scanning, and infrastructure actions are not exposed.

    ## Alternatives Considered

    Broad native file tooling was rejected because read and write capabilities were combined and a hard approved-root boundary was not sufficient for the intended trust level. Direct exposure of the live canonical vault was rejected. Network-listening MCP was unnecessary and therefore avoided.

    ## Consequences

    The model can inspect approved derived knowledge without receiving authority to modify the source estate or infrastructure. The AI mirror must be refreshed through controlled ingestion rather than direct write-back. Retrieved content is treated as untrusted data, not executable instruction.

    ## Validation

    The MCP implementation has passed path-traversal, absolute-path, reparse/junction escape, live read/search, denial, protocol, and dashboard/model-path validation. Ollama and Hermes remain loopback-bound.

    ## Related Documentation

    - [Local AI Security Boundary](../docs/security/local-ai-security-boundary.md)
- [Public Documentation Governance](../docs/governance/documentation-governance.md)
