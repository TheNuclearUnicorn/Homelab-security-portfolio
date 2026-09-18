# Security Policy

## Scope

This repository is a **sanitized public documentation derivative** of a privately operated homelab and cyber-range environment.

The hostnames, IP addresses, DNS names, account identities, paths, and configuration fragments published here are intentionally substituted, generalized, or illustrative.

This repository is **not** an authorization to identify, scan, probe, authenticate to, exploit, or otherwise test any system that might be inferred to exist behind the documentation.

## What to Report

Please report repository-security issues such as:

- an accidentally committed password, token, key, certificate private key, or recovery code;
- a real operational hostname or IP address that appears to have escaped sanitization;
- a private username, account identifier, key fingerprint, filesystem path, or other reconnaissance-sensitive value;
- backup or recovery content accidentally committed to the repository;
- a configuration example that unintentionally contains a real secret or live endpoint;
- a repository workflow that could expose secrets if CI is later added.

## What Not to Report Here

Do not use this repository to report or test:

- vulnerabilities in third-party products such as OPNsense, Docker, Cloudflare, Wazuh, Forgejo, Ollama, Hermes, Caddy, Grafana, or Prometheus;
- vulnerabilities discovered by probing systems you believe may correspond to the private environment;
- guessed credentials, inferred live addresses, or social-engineering findings;
- general hardening suggestions that are not repository-security defects.

## Reporting Method

If GitHub private vulnerability reporting is enabled for this repository, use that mechanism for sensitive reports.

Do **not** open a public issue containing a suspected credential, secret, live endpoint, or other sensitive value.

If private vulnerability reporting is unavailable, avoid publishing the sensitive value and use an available private contact method associated with the repository owner.

## Response Philosophy

A valid disclosure involving accidental publication will be handled by:

1. removing the exposed value from the current tree;
2. determining whether Git history also contains it;
3. rotating or revoking the affected operational credential if applicable;
4. evaluating whether additional sanitization rules are required;
5. documenting the remediation without republishing the sensitive value.

## Safe Research Boundary

The repository documents security architecture; it does not create permission to test the private systems from which the architecture was derived.
