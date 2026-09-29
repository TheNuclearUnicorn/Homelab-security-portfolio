---

title: "Documentation Integrity Engineering — Recovering from Encoding Corruption and Building a Governed Knowledge Pipeline"  
document_id: "HSP-CS-005"  
document_type: "case-study"  
status: "case-study"  
environment: "sanitized-public-derivative"  
last_reviewed: "2026-09-29"  
sanitization: "operational-identifiers-substituted"  
tags:

- documentation
    
- knowledge-engineering
    
- devsecops
    
- data-integrity
    
- utf-8
    
- automation
    
- governance
    
- rag
    
- change-control
    
- validation
    

---

# Documentation Integrity Engineering — Recovering from Encoding Corruption and Building a Governed Knowledge Pipeline

> **State:** Remediation completed and preventive controls established. Canonical documentation remains authoritative; AI/RAG and other generated representations are treated as derived, rebuildable products.

## Executive Summary

A documentation-quality investigation that began with malformed characters exposed a larger engineering problem: documentation integrity could not be treated as a text-editing issue once the same information existed across canonical notes, historical evidence, generated reports, Git-controlled material, and AI retrieval projections.

The visible symptom was mojibake—valid characters that had been incorrectly decoded and re-encoded—but repairing individual strings would not prove that the documentation estate was trustworthy.

The remediation therefore became a controlled data-integrity project.

The process established a governed pipeline:

```
canonical documentation
        ↓
read-only inventory and classification
        ↓
bounded deterministic remediation
        ↓
encoding + integrity validation
        ↓
lifecycle/state reconciliation
        ↓
derived artifact regeneration
        ↓
post-generation validation
        ↓
AI / retrieval / publication consumers
```

The completed remediation audited 49 files, repaired three affected canonical files, regenerated nine derived retrieval bundles, and reduced actionable mojibake findings to zero. Historical evidence and deliberately malformed test fixtures were preserved rather than "cleaned" simply to produce an empty report.

The more important result was architectural: **generated knowledge products can no longer be treated as interchangeable with their source material.**

## Problem

The initial problem appeared straightforward: portions of the documentation corpus contained malformed punctuation and other suspicious character sequences.

Examples of this class of corruption include transformations such as:

```
intended UTF-8 punctuation
        ↓
decoded using an incompatible character set
        ↓
encoded again
        ↓
visible mojibake
```

The investigation showed that not every unusual terminal rendering represented corruption on disk. Some later anomalous-looking output was attributable to the PowerShell/Git display path rather than damaged source bytes.

That distinction mattered.

A bulk search-and-replace based solely on what appeared in a terminal could have corrupted valid source files while attempting to repair them.

The problem therefore became:

> How do you repair confirmed encoding corruption across a documentation and AI knowledge estate without damaging valid source material, historical evidence, or derived representations?

## Why This Was More Than an Encoding Problem

The documentation existed in several different roles:

```
canonical human-authored documentation
historical and rollback evidence
machine-generated inventories
reviewed version-control representations
AI/RAG knowledge mirrors
commercial-AI retrieval bundles
```

Those copies did not have equal authority.

A generated retrieval bundle might contain text copied from a canonical runbook, but that did not make the bundle an appropriate place to perform the repair.

Likewise, historical evidence might intentionally contain the exact malformed state being investigated.

The remediation therefore required two separate questions for every finding:

1. **Is this actually corrupted?**
    
2. **If it is corrupted, is this copy authoritative and eligible for repair?**
    

That distinction prevented the remediation process itself from becoming a new source of documentation drift.

## Engineering Constraints

The remediation operated under several constraints:

- canonical human-authored documentation had to remain the editing authority;
    
- generated AI/RAG representations could not be manually repaired as substitutes for their source;
    
- historical evidence had to remain point-in-time evidence;
    
- uncertain transformations had to fail closed rather than guess;
    
- backups had to exist before mutation;
    
- repairs had to be deterministic and reversible;
    
- files had to remain valid UTF-8 after modification;
    
- integrity evidence had to survive the repair;
    
- generated representations had to be rebuilt from corrected canonical sources;
    
- unrelated sensitive or excluded material could not be pulled into the remediation merely for convenience.
    

The objective was not to make every scan return zero findings.

The objective was to produce a trustworthy explanation for every finding.

## Phase 1 — Establish a Recovery Point

Before modifying canonical documentation, a validated recovery checkpoint was established.

This changed the remediation model from:

```
find suspicious text
        ↓
edit files
        ↓
hope the result is correct
```

to:

```
validated recovery state
        ↓
inventory
        ↓
classify
        ↓
repair bounded targets
        ↓
validate
        ↓
accept or roll back
```

That sequencing became important once multiple document classes and derived representations were involved.

## Phase 2 — Read-Only Corpus Audit

The first active phase was read-only.

The audit inventoried candidate files and searched for encoding anomalies without modifying the corpus.

The investigation separated findings into classes such as:

```
confirmed reversible mojibake
display/rendering anomaly
valid non-ASCII text
historical evidence
deliberately malformed validation fixture
requires manual review
```

This classification prevented a common failure mode in encoding remediation: treating every non-ASCII character as corruption.

Unicode is not corruption.

A valid em dash, accented character, symbol, or non-English character should survive an integrity cleanup unchanged.

## Phase 3 — Prove the Transformation

Confirmed repair candidates were subjected to a stricter requirement:

> The transformation had to be exactly reversible and deterministic.

The repair process did not assume that a suspicious sequence should simply become whatever punctuation looked visually correct.

Instead, candidate transformations were validated before canonical mutation.

Conceptually:

```
candidate corrupted bytes/text
        ↓
known decoding/encoding reversal
        ↓
expected Unicode result
        ↓
round-trip validation
        ↓
repair permitted
```

If the transformation could not be proven, automation stopped and the item remained for review.

This fail-closed behavior was preferable to a "best effort" repair across a documentation corpus.

## Phase 4 — Canonical-Only Transactional Repair

Only confirmed affected canonical files were modified.

The accepted remediation affected:

```
49 files audited
3 canonical files repaired
```

Before writes, the process created recovery copies and validated them.

Repairs were then applied transactionally to the bounded target set.

Derived AI material was deliberately excluded from direct repair.

The rule became:

```
canonical source is wrong
    -> repair canonical source
    -> validate canonical source
    -> regenerate derivatives

derived copy is wrong because source was wrong
    -> do not hand-edit derivative
```

This prevents two copies of the same logical document from quietly developing independent histories.

## Phase 5 — UTF-8 and Integrity Validation

Repair was not considered successful because the resulting text looked correct in an editor.

Post-repair validation included:

- strict UTF-8 decoding;
    
- byte-order-mark checks;
    
- rescanning for actionable mojibake;
    
- SHA-256 integrity evidence;
    
- comparison against the bounded repair inventory;
    
- confirmation that unrelated files were not silently changed.
    

The accepted remediation state was:

```
strict UTF-8 validation       PASS
unexpected BOM                absent
actionable mojibake           0
hash/integrity validation     PASS
rollback validation           PASS
```

A separate pre-remediation/historical scan still contained findings, but those findings were intentionally preserved where they represented historical build evidence or a deliberately invalid UTF-8 test fixture.

A clean current corpus did not require destroying evidence of the original problem.

## Phase 6 — Derived Knowledge Regeneration

Correcting canonical files was only half of the problem.

The environment also maintained generated retrieval projections used by AI tooling.

Those representations were explicitly treated as:

```
derived
rebuildable
noncanonical
```

After canonical validation, the generation pipeline was run again rather than modifying the generated files directly.

Nine retrieval bundles were regenerated.

The generator itself was subjected to validation before its output replaced the previous derived set.

The resulting model was:

```
canonical sources
        ↓
validated generator
        ↓
coherent generation
        ↓
checksums / provenance
        ↓
derived retrieval bundle
```

This made regeneration part of change control rather than a file-copy operation.

## Phase 7 — Lifecycle Drift Discovered During Validation

Encoding remediation exposed a second documentation-integrity problem.

Some documents contained text that was syntactically valid UTF-8 but semantically stale.

For example, a current document could still describe a program activity as:

```
ready for regeneration
```

after that regeneration had already occurred and been accepted elsewhere.

Encoding checks cannot detect this type of failure.

The remediation therefore expanded from **byte integrity** to **state integrity**.

A targeted lifecycle audit compared current documentation against accepted program state and classified matches as:

```
genuine current-state conflict
valid current statement
historical point-in-time evidence
planned/future work
```

Only genuine current-state conflicts were corrected.

Historical records were not rewritten to make them appear as though they had always known the future.

## Phase 8 — Canonical State Reconciliation

Lifecycle reconciliation followed the same canonical-first rule as encoding remediation.

The process:

1. identified current documents containing stale lifecycle assertions;
    
2. distinguished those from historical evidence;
    
3. backed up canonical targets;
    
4. changed only bounded current-state assertions;
    
5. validated the resulting semantic state;
    
6. regenerated affected derived representations;
    
7. replaced the consumer-side retrieval projection only after successful regeneration.
    

This closed an important gap:

```
encoding integrity
    !=
documentation integrity
```

A document can be perfectly valid UTF-8 and still be operationally wrong.

## Governed Knowledge Architecture

The remediation ultimately reinforced a three-plane model.

### Canonical Plane

Human-authored, governed documentation is authoritative.

Changes happen here first.

### Review / Promotion Plane

Version control provides review, history, and controlled promotion where appropriate.

A Git copy does not automatically become authoritative merely because it is version controlled.

### Derived Knowledge Plane

AI/RAG mirrors, indexes, retrieval bundles, caches, and similar products are generated from approved sources.

They are rebuildable and are not editing authority.

```
flowchart TD
    C["Canonical documentation"]
    A["Audit & validation"]
    G["Reviewed Git / promotion plane"]
    D["Derived AI / RAG knowledge"]
    V["Post-generation validation"]
    R["Retrieval consumers"]

    C --> A
    A --> G
    A --> D
    D --> V
    V --> R

    R -. "never authoritative" .-> C
```

The dashed relationship is intentional: retrieval consumers can identify problems and generate proposals, but they do not silently promote themselves into canonical authority.

## Provenance and Manifest Controls

Generated inventories and knowledge projections now rely on explicit provenance fields such as:

```
stable source identity
source-relative path
canonical plane
source size
source modification time
SHA-256
inventory/generation time
lifecycle classification
ingestion state
sensitivity/exclusion decision
```

Machine-generated path manifests use explicit UTF-8.

A lossy report is not permitted to become path authority.

This matters because an encoding-damaged inventory can become more dangerous than the damaged source if automation subsequently uses that inventory to rename, delete, or overwrite files.

## Fail-Closed Knowledge Operations

The same principle used during encoding repair now applies to knowledge ingestion.

Unexpected conditions stop processing rather than broadening scope.

Examples include:

```
unapproved source
unsupported lifecycle class
unexpected path state
sensitivity exclusion
unresolved canonical authority
stale or deleted source
invalid provenance
```

This is particularly important when AI retrieval is involved.

Retrieval convenience does not override source governance.

## AI/RAG Boundary

The knowledge pipeline deliberately separates retrieval from mutation.

The accepted Homelab pilot uses deterministic export from approved canonical documentation into a derived knowledge plane with provenance and lifecycle-aware retrieval.

The AI-facing interface remains bounded and read-only.

It can list, read, and search approved knowledge, but it cannot use the retrieval interface to modify canonical documentation or infrastructure.

Cross-domain expansion is also default-deny.

Adding another knowledge domain requires its own governance and authorization rather than inheriting permission merely because the Homelab domain was approved.

## Validation Outcome

The completed integrity effort established the following verified outcome:

|Control|Result|
|---|---|
|Files included in encoding audit|49|
|Canonical files requiring repair|3|
|Derived retrieval bundles regenerated|9|
|Strict UTF-8 validation|PASS|
|Unexpected BOM|None|
|Actionable mojibake after remediation|0|
|SHA-256/integrity validation|PASS|
|Rollback validation|PASS|
|Historical evidence preservation|PASS|
|Canonical-first regeneration model|Established|
|Lifecycle-state reconciliation|Completed|
|Derived source-pack refresh|Completed|

The result was not simply a cleaner Markdown repository.

It was a controlled chain from human-authored source to machine-consumed knowledge.

## What Was Deliberately Not "Fixed"

Several categories were intentionally left untouched.

### Historical evidence

Historical documents retain the state that existed when they were produced.

Rewriting them would destroy evidence.

### Deliberately malformed fixtures

A validation fixture designed to test invalid UTF-8 should remain invalid.

Repairing it would make the test meaningless.

### Valid Unicode

Non-ASCII text is not inherently suspicious.

Valid Unicode remains valid content.

### Display-only anomalies

A terminal or tool rendering problem does not justify changing source bytes.

The source must be proven defective first.

### Derived copies

Generated retrieval artifacts are regenerated from canonical sources rather than repaired independently.

## Lessons Learned

### 1. Mojibake is a symptom, not a root-cause analysis

Malformed text tells you that an encoding boundary failed somewhere.

It does not, by itself, prove which command or application caused the failure.

Where originating evidence is insufficient, the correct engineering conclusion is to describe the reversible encoding failure class rather than invent a single causal command.

### 2. Never repair what you have not classified

Bulk replacement is dangerous in a corpus containing valid Unicode, historical evidence, test fixtures, and generated copies.

Inventory and classification come first.

### 3. Canonical authority must be explicit

Once documentation feeds Git, AI, search, reports, and automation, "which copy is the source?" becomes an architectural question.

It should have a deterministic answer.

### 4. Derived knowledge should be disposable

An AI knowledge mirror that cannot be safely rebuilt has become an undocumented source of truth.

Derived systems should be reproducible from governed sources.

### 5. Integrity has both byte and semantic dimensions

A file can pass every encoding and hash check while still describing obsolete operational state.

Documentation integrity therefore requires both:

```
byte-level integrity
+
state/lifecycle integrity
```

### 6. Validation output is not automatically authority

Machine-generated reports can themselves be malformed, stale, incomplete, or lossy.

Automation should not promote an inventory into authority merely because a script produced it.

### 7. Fail closed when the transformation is uncertain

A stopped automation produces a review task.

A guessed transformation can silently rewrite institutional knowledge.

### 8. Preserve evidence instead of optimizing for zero findings

An empty scanner report is not the objective.

The objective is that every remaining finding has an understood and governed disposition.

## Operational Outcome

The resulting knowledge lifecycle is now:

```
authoritative human source
        ↓
controlled change
        ↓
integrity + lifecycle validation
        ↓
reviewed promotion where applicable
        ↓
deterministic derived generation
        ↓
provenance / checksum validation
        ↓
bounded retrieval
```

That architecture turns a one-time encoding incident into a reusable documentation-integrity control system.

The central lesson was simple:

> **AI-ready documentation begins with trustworthy source governance.**

Better retrieval cannot compensate for corrupted, ambiguous, or stale source material.

## Security and Publication Boundary

This case study intentionally omits:

- internal addressing;
    
- private hostnames;
    
- administrative access paths;
    
- credentials or secrets;
    
- private knowledge-domain contents;
    
- detailed internal filesystem locations;
    
- sensitive recovery artifacts;
    
- operational firewall rules;
    
- private repository details.
    

The public artifact documents the engineering method and control model rather than reproducing the protected environment.

## Related Documentation

- [Homelab Security Portfolio](https://chatgpt.com/g/README.md)
    
- [Security Design Principles](https://chatgpt.com/g/docs/architecture/security-design-principles.md)
    
- [Trust Boundaries](https://chatgpt.com/g/docs/architecture/trust-boundaries.md)