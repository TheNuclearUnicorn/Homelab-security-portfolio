#!/usr/bin/env python3
"""Publication QA for the sanitized Homelab Security Portfolio."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".mmd", ".fragment", ".txt"}
ALLOWED_FRONTMATTER_STATUS = {
    "current-verified",
    "current-with-open-items",
    "historical-baseline",
    "case-study",
    "planned",
}
REQUIRED_PATHS = {
    "README.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "PUBLICATION-CHECKLIST.md",
    "docs/architecture/architecture-overview.md",
    "docs/architecture/network-segmentation.md",
    "docs/architecture/trust-boundaries.md",
    "docs/recovery/backup-recovery-architecture.md",
    "docs/security/wazuh-siem.md",
    "docs/security/local-ai-security-boundary.md",
    "case-studies/backup-migration/README.md",
    "case-studies/wazuh-integration/README.md",
}
FORBIDDEN_OPERATIONAL_PATTERNS = {
    "live public domain": re.compile(r"thenuclearunicorn\.co", re.I),
    "private Forgejo owner": re.compile(r"\bnuclear_unicorn\b", re.I),
    "known private hostname": re.compile(
        r"\b(?:Host-W-S-01|Host-W-L-01|Host-U-R-00|Host-U-RP-01|"
        r"Host-U-WZ-01|Host-PVE-00|Host-B-FW-00|host-u-d-00|host-u-ci-00)\b",
        re.I,
    ),
    "live lab IPv4 address": re.compile(
        r"\b(?:10\.10\.1|192\.168\.(?:178|10|20|30|40|50|60|70|95|99))\."
        r"(?:25[0-5]|2[0-4]\d|1?\d?\d)\b"
    ),
    "private knowledge path": re.compile(r"F:\\Knowledge-Local", re.I),
    "private AI path": re.compile(r"E:\\AI(?:\\|$)", re.I),
    "private Docker path": re.compile(r"/srv/docker(?:/|$)", re.I),
    "private backup path": re.compile(r"/mnt/nuc-backup(?:/|$)", re.I),
    "private Windows profile path": re.compile(r"C:\\Users\\(?:Chris|cscla)(?:\\|$)", re.I),
}
SECRET_PATTERNS = {
    "private key material": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "secret assignment": re.compile(
        r"(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token|client[_-]?secret)"
        r"\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
    ),
}
PUBLICATION_HYGIENE_PATTERNS = {
    "obsolete first-commit handoff reference": re.compile(r"GIT-FIRST-COMMIT\.md"),
    "internal stage manifest reference": re.compile(r"STAGE\d+-MANIFEST", re.I),
    "stale build-stage wording": re.compile(
        r"Later stages will add ADRs, case studies, portfolio summaries", re.I
    ),
}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", ".gitignore", ".gitattributes"}:
            yield path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_paths(errors):
    for required in sorted(REQUIRED_PATHS):
        if not (ROOT / required).exists():
            errors.append(f"missing required path: {required}")


def check_patterns(errors):
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        name = rel(path)
        for label, pattern in FORBIDDEN_OPERATIONAL_PATTERNS.items():
            match = pattern.search(text)
            if match:
                errors.append(f"{name}: forbidden operational data ({label}): {match.group(0)!r}")
        for label, pattern in SECRET_PATTERNS.items():
            match = pattern.search(text)
            if match:
                errors.append(f"{name}: possible secret ({label}): {match.group(0)!r}")
        for label, pattern in PUBLICATION_HYGIENE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{name}: publication hygiene failure ({label})")


def check_relative_links(errors):
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith("#") or target.startswith("mailto:") or "://" in target:
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel(path)}: relative link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(path)}: broken relative link: {raw_target}")


def extract_frontmatter_status(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return "__MALFORMED__"
    block = text[4:end]
    match = re.search(r"(?m)^status:\s*[\"']?([^\"'\n]+)[\"']?\s*$", block)
    return match.group(1).strip() if match else None


def check_frontmatter(errors):
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        status = extract_frontmatter_status(text)
        if status == "__MALFORMED__":
            errors.append(f"{rel(path)}: malformed YAML front matter")
        elif status is not None and status not in ALLOWED_FRONTMATTER_STATUS:
            errors.append(f"{rel(path)}: unsupported public lifecycle status: {status!r}")


def check_whitespace(errors):
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.endswith((" ", "\t")):
                errors.append(f"{rel(path)}:{lineno}: trailing whitespace")



def check_markdown_structure(errors):
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        fences = sum(1 for line in lines if line.lstrip().startswith("```"))
        if fences % 2:
            errors.append(f"{rel(path)}: unbalanced fenced code block")
        h1_count = sum(1 for line in lines if line.startswith("# "))
        if h1_count > 1:
            errors.append(f"{rel(path)}: multiple Markdown H1 headings ({h1_count})")
        if text and not text.endswith("\n"):
            errors.append(f"{rel(path)}: missing final newline")


def main():
    errors = []
    check_required_paths(errors)
    check_patterns(errors)
    check_relative_links(errors)
    check_frontmatter(errors)
    check_whitespace(errors)
    check_markdown_structure(errors)
    if errors:
        print("Publication QA: FAIL")
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} issue(s) detected.")
        return 1
    checked = sum(1 for _ in iter_text_files())
    print("Publication QA: PASS")
    print(f"Checked {checked} text/configuration files.")
    print("No broken relative links, known private identifiers, or secret patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
