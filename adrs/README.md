# Architecture Decision Records

Architecture Decision Records preserve significant design choices and their tradeoffs.

| ADR | Decision |
|---|---|
| [ADR-0001](0001-opnsense-inter-vlan-routing.md) | OPNsense remains the authoritative inter-VLAN router/firewall |
| [ADR-0002](0002-cloudflare-tunnel-ingress.md) | Use Cloudflare Access/Tunnel instead of public router ports |
| [ADR-0003](0003-caddy-without-docker-socket.md) | Keep Caddy static and avoid Docker-socket access |
| [ADR-0004](0004-isolated-ci-no-production-socket.md) | Treat CI as untrusted and deny the production Docker socket |
| [ADR-0005](0005-restricted-production-deployment.md) | Use a restricted deployment gate rather than unrestricted CI shell |
| [ADR-0006](0006-independent-backup-failure-domain.md) | Keep authoritative backups outside production Docker storage |
| [ADR-0007](0007-read-only-ai-knowledge-boundary.md) | Expose approved AI knowledge through a root-confined read-only MCP |

ADRs describe the current accepted public architecture. If a decision is later replaced, the old ADR remains as historical decision evidence and links to the superseding record.
