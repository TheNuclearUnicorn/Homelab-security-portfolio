# Contributing

This repository is primarily a professional engineering portfolio, but corrections and documentation improvements are welcome.

## Good Contributions

Useful contributions include:

- correcting broken internal links;
- improving accessibility or Mermaid readability;
- correcting spelling, grammar, or ambiguous technical wording;
- identifying contradictions between public documents;
- suggesting clearer explanations of security or recovery concepts;
- improving sanitized, non-secret examples.

## Contribution Requirements

Any contribution must preserve the repository's publication model:

- use only public identifiers such as `FW-01`, `DOCKER-01`, and `CI-01`;
- use only the documented example address ranges;
- use `example.com` for DNS examples;
- do not add private usernames or filesystem paths;
- do not add key fingerprints, secrets, tokens, tunnel credentials, recovery artifacts, or raw backups;
- do not infer unverified implementation details;
- do not convert planned architecture into current-state language;
- do not weaken the distinction between historical baseline and current runtime.

## Technical Claims

A technical claim should be supported by one of the existing public documents or introduced explicitly as a proposal.

Do not silently "fix" the architecture based on common practice. This repository intentionally documents the decisions and constraints of one environment.

## Configuration Examples

Examples are intentionally partial and sanitized.

Do not make them look production-ready by inventing:

- credentials;
- image versions;
- private CA material;
- real hostnames;
- real IP addresses;
- unsupported service definitions.

If an example is a fragment, keep it labeled as a fragment.

## Pull Requests

A focused pull request should:

1. explain what changed;
2. identify the affected document(s);
3. state whether the change is editorial, architectural clarification, or example-only;
4. preserve all sanitization boundaries;
5. avoid unrelated formatting churn.

## Security Issues

Do not submit suspected leaked secrets or live operational identifiers through a public issue or ordinary pull request.

See [SECURITY.md](SECURITY.md).
