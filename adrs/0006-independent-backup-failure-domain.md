---
    title: "Independent Backup Failure Domain"
    document_id: "HSP-ADR-006"
    document_type: "architecture-decision-record"
    status: "current-verified"
    environment: "sanitized-public-derivative"
    last_reviewed: "2026-09-18"
    sanitization: "operational-identifiers-substituted"
    ---

    # ADR-0006: Independent Backup Failure Domain

    ## Status

    **Accepted — current architecture.**

    ## Context

    A Restic repository on the same storage tier as production protects against some logical failures but does not provide sufficient recovery from loss or corruption of the production Docker storage tier.

    ## Decision

    The authoritative application backup repository resides on an external Windows-hosted storage tier reached through a dedicated backup source identity, narrow SMB policy, SMB 3.1.1 encryption, a fail-closed mount guard, application-aware staging, Restic retention, and isolated restore testing.

    ## Alternatives Considered

    Same-host backup storage was superseded as the authoritative design. Broad application-subnet SMB access was rejected. Silent fallback to local Docker storage was rejected because it would create false backup success during failure of the independent tier.

    ## Consequences

    The design adds network and mount dependencies to backup execution. In return, backup success now proves use of a separate production-storage failure domain. Restore testing is required because snapshot creation alone is not considered recovery evidence.

    ## Validation

    The migration to the external tier is complete, the mount guard is part of backup/maintenance execution, Restic maintenance is scheduled, and isolated restore testing has been successfully performed.

    ## Related Documentation

    - [Backup and Recovery Architecture](../docs/recovery/backup-recovery-architecture.md)
- [Trust Boundaries](../docs/architecture/trust-boundaries.md)
