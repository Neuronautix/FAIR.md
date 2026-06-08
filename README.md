# fair.md

A lightweight, human- and machine-readable **FAIR manifest** that you drop at
the root of any repository or website. One file tells readers — and machines —
what data a project holds, how FAIR it is, and where the deeper machine-readable
affordances live.

**Status: v0.1 — proposed convention**

> Companion convention: [trust.md](https://github.com/Neuronautix/trust.md) — declares the
> epistemic status and confidence of the knowledge a repository publishes.

---

## 30-second example

```yaml
---
fair_md_version: "0.1"
title: "My Research Dataset"
description: >
  Processed electrophysiology recordings for project X.
identifiers:
  repository: "https://github.com/myorg/myproject"
  homepage: "https://myproject.example.org"
  canonical: "https://myproject.example.org/fair.md"
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
vocabularies:
  - "Neurodata Without Borders (NWB)"
  - "schema.org"
fair_assessment:
  findable:
    F1_globally_unique_persistent_id: "yes"
    F2_rich_metadata: "yes"
    F3_metadata_references_data_id: "yes"
    F4_indexed_searchable: "yes"
  accessible:
    A1_retrievable_by_id_open_protocol: "yes"
    A1.1_protocol_open_free: "yes"
    A1.2_auth_where_needed: "n/a"
    A2_metadata_persist_beyond_data: "partial"
  interoperable:
    I1_formal_accessible_knowledge_representation: "yes"
    I2_FAIR_vocabularies: "yes"
    I3_qualified_references: "partial"
  reusable:
    R1_plurality_of_attributes: "yes"
    R1.1_clear_data_usage_license: "yes"
    R1.2_detailed_provenance: "partial"
    R1.3_domain_community_standards: "yes"
companions:
  trust: "/trust.md"
  sitemap: "/sitemap.xml"
  citation_cff: "/CITATION.cff"
maturity: "beta"
last_reviewed: "2026-06-06"
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
a repo holds, (b) gives an honest, structured **FAIR self-assessment** with a
`yes | partial | planned | no | n/a` status per sub-principle, and (c) points to
the heavier machine-readable companions. It is cheap to write, honest about gaps,
and trivially adoptable on any GitHub Pages or static site.

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

## Reference implementation

The canonical `fair.md` for the Neuronautix knowledge base lives at:

**<https://neuronautix.com/fair.md>**

A copy is included in this repository as
[`examples/neuronautix.fair.md`](examples/neuronautix.fair.md).

This repository also dogfoods the convention on itself: its own conformant
manifest is at [`FAIR.md`](FAIR.md), and the fill-in template lives at
[`template/fair.md`](template/fair.md).

---

## How to adopt fair.md

1. **Copy** [`template/fair.md`](template/fair.md) (the fill-in template) to the
   root of your repository or website as `fair.md`.
2. **Fill in** the YAML front matter with your project's values. Be honest in
   `fair_assessment` — `partial` and `planned` are features, not failures.
3. **Serve** it at `https://yourdomain/fair.md`. Optionally redirect
   `/.well-known/fair.md` → `/fair.md` for programmatic discovery.
4. **Add companions** you already have (`CITATION.cff` is the cheapest
   high-value next step; `codemeta.json` for software; RO-Crate for packaged
   objects).
5. **Pair it with [`trust.md`](https://github.com/Neuronautix/trust.md)** if your repo publishes
   knowledge, analysis, or AI-assisted content whose *confidence* matters, not
   just its findability.
6. **Review** the assessment periodically and update `last_reviewed`.

---

## Formal specification

See [`SPEC.md`](SPEC.md) for the complete v0.1 specification, including all
field definitions, the status enum, FAIR sub-principle mappings, validation
rules, and conformance requirements.

A JSON Schema for the YAML front matter is at
[`schema/fair.schema.json`](schema/fair.schema.json).

### Validating a fair.md

A small validator checks a file's front matter against the schema and the
conformance rules in SPEC.md:

```bash
pip install pyyaml jsonschema
python tools/validate_fair.py path/to/fair.md   # defaults to FAIR.md + examples/ if omitted
```

The same check runs in CI on every push and pull request
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)).

---

## Contributing

This is a proposed convention, not yet a standard. Feedback, issues, and pull
requests are welcome:

- Open an issue to discuss field additions, naming, or alignment with existing
  standards.
- Submit a PR with a worked `examples/` entry to show fair.md in a new domain.
- Reference the formal spec in SPEC.md when proposing changes — keep changes
  backward-compatible within the 0.x series.

The convention follows [Semantic Versioning](https://semver.org/): patch releases
for clarifications, minor releases for additive changes, major releases for
breaking changes.

---

## License

Apache-2.0. See [`LICENSE`](LICENSE).

Copyright 2026 Damien Huzard / Neuronautix.
