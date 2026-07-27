# fair.md

A lightweight, human- and machine-readable **FAIR manifest** that you drop at
the root of any repository or website. One file tells readers — and machines —
what data a project holds, which FAIR implementation choices it makes, what
evidence supports its current posture, and where deeper machine-readable
affordances live. It is a declaration, not certification.

**Status: v0.3 — proposed convention**

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

For an exact, reproducible citation of v0.3.0, use the
[version DOI `10.5281/zenodo.21621349`](https://doi.org/10.5281/zenodo.21621349).
For the evolving project across all releases, use the
[concept DOI `10.5281/zenodo.20793968`](https://doi.org/10.5281/zenodo.20793968).
Machine-readable citation metadata are provided in [`CITATION.cff`](CITATION.cff).

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
pip install pyyaml jsonschema
python tools/validate_fair.py path/to/FAIR.md   # defaults to FAIR.md + examples/ if omitted
```

The same check runs in CI on every push and pull request
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)).

---

## Contributing

This is a proposed convention, not yet a standard. Feedback, issues, and pull
requests are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
development workflow, [`GOVERNANCE.md`](GOVERNANCE.md) for change-approval
rules, [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for participation standards,
and [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) for the formal community-review
questions.

Manifest values use a two-part convention version during the 0.x proposal
period. Release tags use full [Semantic Versioning](https://semver.org/) form
(for example `v0.3.0`); migration rules are documented in the changelog.

---

## License

Apache-2.0. See [`LICENSE`](LICENSE).

Copyright 2026 Damien Huzard / Neuronautix.
