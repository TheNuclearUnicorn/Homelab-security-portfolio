# Firewall Policy Example

This is a logical policy example, not an OPNsense configuration export.

The architecture uses narrow source/destination/port rules rather than broad zone-to-zone access.

| Order | Source | Destination | Protocol/Port | Purpose |
|---:|---|---|---|---|
| 1 | required workload | `FW-01` | DNS/NTP as required | local infrastructure |
| 2 | `CI-01` | approved Git origin | TCP/443 | CI Git/API |
| 3 | backup-only identity | backup tier | TCP/445 | encrypted SMB backup |
| 4 | approved agents | `SIEM-01` | TCP/1514,1515 | Wazuh telemetry/enrollment |
| 5 | zone net | private networks | block | lateral isolation |
| 6 | approved workload | Internet | controlled egress | updates/dependencies |
| 7 | any unmatched | any | block | default deny |

Validation includes expected-success and expected-failure tests. The public portfolio intentionally does not include raw firewall backups or live aliases.
