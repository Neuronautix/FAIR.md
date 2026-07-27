# fair.md

A lightweight, human- and machine-readable **FAIR manifest** that you drop at
the root of any repository or website. One file tells readers — and machines —
what data a project holds, which FAIR implementation choices it makes, what
evidence supports its current posture, and where deeper machine-readable
affordances live. It is a declaration, not certification.

**Status: v0.3 — proposed convention**

[![Zenodo version DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21622631.svg)](https://doi.org/10.5281/zenodo.21622631)
[![Validate fair.md](https://github.com/Neuronautix/FAIR.md/actions/workflows/validate.yml/badge.svg)](https://github.com/Neuronautix/FAIR.md/actions/workflows/validate.yml)

The current release is
[`v0.3.1`](https://github.com/Neuronautix/FAIR.md/releases/tag/v0.3.1).
The project is seeking independent review through
[formal community-review issue #4](https://github.com/Neuronautix/FAIR.md/issues/4).
Neither structural validation nor a maintainer-authored assessment is FAIR
certification.

> Companion convention: [trust.md](https://github.com/Neuronautix/trust.md) — declares the
> epistemic status and confidence of the knowledge a repository publishes.

---

## 30-second v0.3 excerpt

Version 0.3 separates resources, implementation profiles, evidence-backed
assessment results, and Open Definition status. The complete
[template](template/fair.md) contains every required FAIR sub-principle.

```yaml
---
fair_md_version: "0.3"
title: "My Research Dataset"
description: >
  Processed electrophysiology recordings for project X.
identifiers:
  repository: "https://github.com/myorg/myproject"
  homepage: "https://myproject.example.org"
  canonical: "https://myproject.example.org/FAIR.md"
  doi: "10.5281/zenodo.1234567"
maintainers:
  - name: "Jane Smith"
    role: "author, data curator"
    orcid: "0000-0000-0000-0001"
    org: "University of Example"
license:
  content: "CC-BY-4.0"
  code: "MIT"
data_resources:
  - id: "recordings"
    path: "/data/recordings/"
    type: "HDF5 electrophysiology files, NWB format"
    identifier: "https://doi.org/10.5281/zenodo.1234567"
    media_type: "application/x-hdf5"
    metadata: ["/ro-crate-metadata.json"]
    license: "CC-BY-4.0"
vocabularies:
  - name: "RO-Crate"
    identifier: "https://w3id.org/ro/crate/1.3"
    version: "1.3"
fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "yes"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D"]
      evidence:
        - id: "https://doi.org/10.5281/zenodo.1234567"
          type: "persistent-identifier"
  # All remaining F/A/I/R entries are required in a complete manifest.
companions:
  trust: "/trust.md"
  sitemap: "/sitemap.xml"
  citation_cff: "/CITATION.cff"
  ro_crate: "/ro-crate-metadata.json"
profiles:
  - name: "RO-Crate 1.3"
    identifier: "https://w3id.org/ro/crate/1.3"
    status: "adopted"
    applies_to: ["recordings"]
openness:
  open_definition_version: "2.1"
  status: "conformant"
  license_status: "open"
  access: "open"
  machine_readable: true
  open_format: true
  source_available: true
  evidence: ["/LICENSE", "/data/recordings/"]
maturity: "beta"
last_reviewed: "2026-07-27"
---

# My Research Dataset — FAIR Manifest

This file is a FAIR manifest ...
```

---

## Why fair.md?

The FAIR principles (Wilkinson et al., 2016) are widely endorsed but unevenly
practiced. There is no lightweight, conventional place for a project to *state
its own FAIR posture* in a way both a human and a crawler can read in five
seconds.

We already have excellent tools, each with a different ergonomic niche:

| Convention | Niche |
|---|---|
| **`llms.txt`** | Root Markdown for language models — fair.md borrows its "one well-known root file, Markdown, human-first" ergonomics |
| **`codemeta.json` / `CITATION.cff`** | Rich, machine-readable metadata for software and citation — excellent but verbose, rarely read by humans |
| **RO-Crate / FAIR Signposting / FAIR Digital Objects** | Robust packaging and navigation for FAIR objects, aimed at repositories and infrastructure |
| **`robots.txt` / `sitemap.xml`** | Discovery signals for crawlers |

`fair.md` sits *in front of* these: a front door that (a) says plainly what data
a repo holds, (b) records an honest, **evidence-backed FAIR self-assessment**,
(c) names concrete implementation profiles, (d) reports openness separately,
and (e) points to heavier machine-readable companions.

### Lineage

`fair.md` is a direct descendant of:

- **llms.txt** — root Markdown for machines; fair.md inherits its location
  convention and human-first format.
- **codemeta.json / CITATION.cff** — machine-readable metadata standards whose
  semantics inform the `identifiers` and `maintainers` fields.
- **RO-Crate** — the FAIR Digital Object packaging standard; fair.md is a
  lightweight front door that points into an RO-Crate when one exists.
- **FAIR Signposting** — HTTP-level links to FAIR affordances; fair.md is the
  Markdown counterpart.
- **FAIR Guiding Principles (Wilkinson et al., 2016)** — the sub-principle keys
  (`F1`–`R1.3`) map directly to the canonical FAIR sub-principles so automated
  assessment tools can consume them.

---

## Worked example and self-manifest

The canonical reference implementation is this repository's root
[`FAIR.md`](FAIR.md), served from its exact-case raw URL.

The Neuronautix knowledge base originally inspired the convention. A legacy
v0.2 worked snapshot is included at
[`examples/neuronautix.fair.md`](examples/neuronautix.fair.md). It is not
asserted to mirror the current live site.

Two complete v0.3 packages demonstrate resource-level metadata and
evidence-backed assessment:

- [`examples/generic-dataset/FAIR.md`](examples/generic-dataset/FAIR.md) for a
  small, domain-neutral tabular dataset.
- [`examples/isa-tab/FAIR.md`](examples/isa-tab/FAIR.md) for an illustrative
  Investigation–Study–Assay project. It declares ISA-Tab alignment without
  claiming external validation or ISA community endorsement.

The fill-in source remains at [`template/fair.md`](template/fair.md); adopters
copy it to `FAIR.md`.

---

## Citation and persistent identifiers

For an exact, reproducible citation of v0.3.1, use the
[version DOI `10.5281/zenodo.21622631`](https://doi.org/10.5281/zenodo.21622631).
For the evolving project across all releases, use the
[concept DOI `10.5281/zenodo.20793968`](https://doi.org/10.5281/zenodo.20793968).
Machine-readable citation metadata are provided in [`CITATION.cff`](CITATION.cff),
and the expanded release description is tracked in
[`docs/releases/v0.3.1.md`](docs/releases/v0.3.1.md).

Use the version DOI when the cited content must be reproducible. Use the concept
DOI when referring to fair.md generally or when following the project across
releases. New releases should receive their own version DOI under the same
Zenodo concept record; an existing archived release should not be overwritten.

---

## Formal community review

The project requests critical review from GO FAIR and FAIR Implementation
Profile practitioners, FAIRsharing curators, RDA FAIR assessment specialists,
RO-Crate maintainers, ISA Tools experts, research data stewards, and working
scientists.

- Read the complete [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md).
- Respond on [formal community-review issue #4](https://github.com/Neuronautix/FAIR.md/issues/4).
- Use the structured
  [standards-review issue form](.github/ISSUE_TEMPLATE/standards-review.yml)
  for a focused review.

Please identify whether feedback is personal expertise or an official
organizational position. Naming a community here is an invitation to review,
not a claim of endorsement, certification, or affiliation.

---

## How to adopt fair.md

1. **Copy** [`template/fair.md`](template/fair.md) (the fill-in template) to the
   root of your repository or website as `FAIR.md`.
2. **Fill in** the YAML front matter with your project's values. Be honest in
   `fair_assessment` — `partial` and `planned` are features, not failures.
3. **Serve** it at `https://yourdomain/FAIR.md`. Do not present
   `/.well-known/FAIR.md` as standardized unless it is registered under RFC 8615.
4. **Add companions** you already have (`CITATION.cff` is the cheapest
   high-value next step; `codemeta.json` for software; RO-Crate for packaged
   objects).
5. **Pair it with [`trust.md`](https://github.com/Neuronautix/trust.md)** if your repo publishes
   knowledge, analysis, or AI-assisted content whose *confidence* matters, not
   just its findability.
6. **Review** the assessment periodically and update `last_reviewed`.

---

## Formal specification

See [`SPEC.md`](SPEC.md) for the complete v0.3 specification, including all
field definitions, the status enum, FAIR sub-principle mappings, validation
rules, and conformance requirements.

A JSON Schema for the YAML front matter is at
[`schema/fair.schema.json`](schema/fair.schema.json).

The [`fair-documented/`](fair-documented/README.md) source pack records the
authoritative standards, crosswalk, evidence model, optional ISA profile, and
implementation roadmap used for v0.3.

### Validating a fair.md

A small validator checks a file's front matter against the schema and the
conformance rules in SPEC.md:

```bash
python -m pip install -r requirements.txt
python tools/validate_fair.py path/to/FAIR.md
python tools/validate_fair.py  # validates FAIR.md and all maintained examples
python -m unittest discover -s tests -v
```

With no path argument, the validator checks the canonical root `FAIR.md`, legacy
`examples/*.fair.md` snapshots, and complete `examples/**/FAIR.md` packages,
including their root-relative data, metadata, and evidence references.

The same validation and behavioral test suite runs in CI on every push and pull request
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)).

---

## Contributing

This is a proposed convention, not yet a standard. Feedback, issues, and pull
requests are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
development workflow, [`GOVERNANCE.md`](GOVERNANCE.md) for change-approval
rules, [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for participation standards,
and [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) for the formal community-review
questions.

Editorial changes require maintainer or editor approval. Backward-compatible
normative changes require a public design issue and at least 14 days for
comment. Breaking or governance-sensitive changes require a 30-day request for
comments and independent community review. See
[`GOVERNANCE.md`](GOVERNANCE.md) for the complete decision and appeal rules.

Manifest values use a two-part convention version during the 0.x proposal
period. Release tags use full [Semantic Versioning](https://semver.org/) form
(for example `v0.3.1`); migration rules are documented in the changelog.

---

## License

Apache-2.0. See [`LICENSE`](LICENSE).

Copyright 2026 Damien Huzard / Neuronautix.
