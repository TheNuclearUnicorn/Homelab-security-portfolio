---

title: "Public Website Delivery Case Study"  
document_id: "HSP-CS-004"  
document_type: "case-study"  
status: "case-study"  
environment: "sanitized-public-derivative"  
last_reviewed: "2026-09-20"  
sanitization: "operational-identifiers-substituted"  
tags:

- astro
    
- github-pages
    
- github-actions
    
- cloudflare
    
- dns
    
- ci-cd
    
- static-site
    
- custom-domain
    

---
# Public Website Delivery — Astro, GitHub Pages, Cloudflare DNS, and CI/CD

> **State:** Completed. The production website is delivered as a static Astro site through GitHub Actions and GitHub Pages. Cloudflare remains the DNS authority for the custom domain, while the website delivery path remains separate from private homelab application ingress.

## Executive Summary

The public professional website originally shared a DNS zone with privately operated infrastructure services.

The final design deliberately separates those concerns.

The website is **not self-hosted**. Its production delivery path is:

```text
source-controlled website
        ↓
GitHub
        ↓
GitHub Actions
        ↓
Astro static build
        ↓
GitHub Pages
        ↓
custom domain + HTTPS
```

Cloudflare remains responsible for DNS management, but the website apex and `www` records resolve to GitHub Pages rather than a private application origin.

Private infrastructure subdomains retain their existing, independent ingress paths.

The result is a public website that demonstrates CI/CD, DNS, source-control hygiene, custom-domain management, and deployment troubleshooting without creating a dependency on the homelab for public availability.

## Problem

The domain served more than one purpose:

```text
public professional website

and

private infrastructure services
```

That created an important architectural distinction.

The website needed to move to a static hosting platform without disturbing unrelated subdomains that continued to use private ingress services.

At the same time, the website repository had accumulated deployment ambiguity and source-control hygiene issues:

- more than one GitHub Pages deployment path existed;
- the authoritative Astro workflow was not initially the only Pages workflow;
- generated site artifacts had been committed previously;
- dependency directories had been tracked;
- local and remote Git history required reconciliation;
- the apex website hostname had previously participated in a different delivery path;
- DNS, Pages custom-domain validation, and HTTPS had to converge before the migration could be considered complete.

The objective was therefore broader than making the website reachable.

The target was a single, understandable deployment authority with a clean source repository and an independently hosted public website.

## Design Decision

The website was assigned its own delivery architecture:

```mermaid
flowchart LR
    Author["Source authoring"]
    Repo["Website Git repository"]
    Actions["GitHub Actions"]
    Astro["Astro static build"]
    Pages["GitHub Pages"]
    DNS["Cloudflare DNS"]
    Browser["Public browser"]

    Author --> Repo
    Repo --> Actions
    Actions --> Astro
    Astro --> Pages
    DNS --> Pages
    Pages --> Browser
```

The private homelab application path is intentionally absent from this diagram.

The public website does not require:

```text
home-router port forwarding
private reverse proxy
Docker application hosting
homelab tunnel connector
private application VLAN
```

for normal delivery.

## Cloudflare as DNS, Not Website Hosting

A central design point was separating **DNS authority** from **hosting authority**.

Cloudflare continues to manage the DNS zone.

GitHub Pages hosts the website.

For the public site:

```text
apex
www
    ↓
GitHub Pages
```

Other service-specific subdomains can continue to use their independently defined delivery paths.

This allowed the website migration to change only the records and routing relevant to the public site rather than redesigning the entire DNS zone.

## Single Deployment Authority

The repository previously contained overlapping GitHub Pages deployment mechanisms.

That creates ambiguity:

```text
source change
   ↓
which workflow owns production?
```

The duplicate static Pages workflow was removed.

The Astro deployment workflow became the single authoritative build-and-deploy path:

```text
tracked source
    ↓
authoritative workflow
    ↓
Astro build
    ↓
GitHub Pages
```

This reduces troubleshooting ambiguity and makes the relationship between a Git commit and a deployed site easier to audit.

## Repository Hygiene

The deployment work also exposed an important source-control issue.

Generated dependencies and build output should not represent authored source.

The repository was cleaned so that items such as:

```text
node_modules
generated build output
other reproducible artifacts
```

are not treated as source-controlled application content.

The repository therefore represents the material required to reproduce the website rather than a mixture of source and locally generated state.

This is particularly important for CI/CD because the deployment workflow should prove that production can be created from the tracked source.

## Git History Reconciliation

During the website redesign, the local working branch and remote `main` had diverged.

Rather than force-pushing or blindly merging unrelated generated changes, the local state was preserved on a backup branch before the canonical working branch was reconciled with the remote repository.

The important engineering principle was:

```text
preserve uncertain history
        ↓
identify authoritative source state
        ↓
reconcile deliberately
        ↓
continue from a clean baseline
```

Generated output from the older local history was not allowed to redefine the authoritative source tree.

## Custom-Domain Migration

The website custom domain was migrated to GitHub Pages without moving unrelated private service hostnames.

The migration sequence conceptually separated:

```text
website DNS
```

from:

```text
private-service DNS
```

Only the public website hostnames were moved to the GitHub Pages delivery path.

This avoided turning a website migration into an unnecessary infrastructure migration.

## HTTPS and Domain Validation

DNS resolution alone was not treated as completion.

Acceptance required the hosting platform to recognize the custom domain and successfully provide HTTPS.

The completed state therefore required:

```text
DNS resolution
+
Pages custom-domain validation
+
valid HTTPS
+
correct website content
```

rather than relying on a single successful DNS lookup.

## Validation

The release was accepted only after validating the complete delivery chain.

```text
repository working tree clean

authoritative Astro workflow succeeds

GitHub Pages deployment succeeds

custom-domain DNS validation passes

apex resolves to the Pages-hosted site

www resolves to the Pages-hosted site

HTTPS is enabled and valid

expected Astro content is rendered

unrelated private service routes remain independent
```

This validates both the positive path—public website delivery—and the negative requirement that the migration did not absorb unrelated infrastructure into the website architecture.

## Operational Outcome

The resulting architecture provides a clear separation of responsibility:

```text
Git
  -> source authority

GitHub Actions
  -> build and deployment automation

Astro
  -> static site generation

GitHub Pages
  -> public hosting

Cloudflare
  -> DNS authority

private infrastructure
  -> separate operational domain
```

A failure or maintenance event inside the private homelab is therefore not part of the public website's normal hosting dependency chain.

## Security and Engineering Benefits

### Reduced public infrastructure dependency

The public website does not require inbound connectivity to privately operated infrastructure.

### Smaller public attack surface

No home-hosted web server or public router port is required to deliver the site.

### Clear deployment authority

One workflow owns production deployment rather than multiple competing Pages workflows.

### Reproducible source model

Generated dependencies and build output are excluded from source authority.

### Narrow DNS migration

Website records can change without unnecessarily modifying private service routes.

### Independent failure domains

Public site hosting and private homelab application hosting are operationally separate.

## Lessons Learned

### DNS provider and hosting provider do not need to be the same platform

Cloudflare can remain authoritative for DNS while GitHub Pages provides the actual website hosting.

### A shared DNS zone does not require a shared delivery architecture

The apex website and service-specific subdomains can use different hosting and ingress mechanisms when those boundaries are intentional.

### One production workflow should own deployment

Multiple Pages workflows make failures and stale deployments substantially harder to reason about.

### Generated artifacts should not become source authority

If CI can reproduce an artifact, that artifact generally should not be committed merely to make deployment work.

### Preserve before reconciling Git divergence

A backup branch is inexpensive. Destructive history manipulation before understanding the divergence is not.

### Validate the complete user path

A successful build, a valid DNS response, and an issued certificate each prove different parts of the system. Production acceptance requires the full chain to work.

## Related Documentation

- [Security Design Principles](https://chatgpt.com/g/docs/architecture/security-design-principles.md)
- [Portfolio Refresh Policy](https://chatgpt.com/g/docs/governance/portfolio-refresh-policy.md)
- [Project Summary](https://chatgpt.com/g/portfolio/project-summary.md)