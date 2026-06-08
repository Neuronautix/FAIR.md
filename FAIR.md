---
# This is the fair.md FAIR manifest for the fair.md repository itself — a real,
# conformant manifest (not the template). The fill-in template lives at
# template/fair.md. Specification: SPEC.md. Schema: schema/fair.schema.json.

fair_md_version: "0.1"
title: "fair.md — a FAIR manifest convention"
description: >
  The fair.md convention: a lightweight, human- and machine-readable FAIR
  manifest placed at the root of a repository or website. This repository holds
  the formal specification, a fill-in template, a JSON Schema for the YAML front
  matter, a reference example, and a validator with CI.
identifiers:
  repository: "https://github.com/Neuronautix/FAIR.md"
  homepage: "https://github.com/Neuronautix/FAIR.md"
  canonical: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/FAIR.md"
  doi: null            # not yet minted — recommend archiving a release to Zenodo for a DOI
maintainers:
  - name: "Damien Huzard, PhD"
    role: "author, specification editor, maintainer"
    orcid: "0000-0003-4820-7951"
    org: "Neuronautix — Montpellier, France"
license:
  content: "Apache-2.0"
  code: "Apache-2.0"

# ── What "data" this manifest covers (the FAIR objects) ──
# This repo's "data" is the convention itself: spec, schema, template, example, tooling.
data_resources:
  - id: "specification"
    path: "/SPEC.md"
    type: "formal specification of the fair.md convention (Markdown)"
    topics: ["FAIR", "metadata", "specification"]
  - id: "schema"
    path: "/schema/fair.schema.json"
    type: "JSON Schema (draft 2020-12) for the YAML front matter"
  - id: "template"
    path: "/template/fair.md"
    type: "fill-in template with placeholder values and inline guidance"
  - id: "examples"
    path: "/examples/"
    type: "reference fair.md manifests (worked examples)"
    count: 1
  - id: "validator"
    path: "/tools/"
    type: "Python validator for fair.md front matter (pyyaml + jsonschema)"

# ── Vocabularies / standards referenced (Interoperability) ──
vocabularies:
  - "FAIR Guiding Principles (Wilkinson et al., 2016)"
  - "SPDX License List"
  - "Citation File Format (CFF) 1.2.0"
  - "JSON Schema (draft 2020-12)"
  - "Keep a Changelog 1.1.0; Semantic Versioning 2.0.0"

# ── FAIR self-assessment ──
# status enum: yes | partial | planned | no | n/a
# Transparent SELF-assessment of THIS repository, not a certified audit.
fair_assessment:
  findable:
    F1_globally_unique_persistent_id: "partial"   # canonical GitHub/raw URLs; no DOI yet
    F2_rich_metadata: "yes"                        # this manifest + CITATION.cff + README/SPEC
    F3_metadata_references_data_id: "yes"          # data_resources reference repo paths/ids
    F4_indexed_searchable: "yes"                   # public on GitHub (indexed/searchable)
  accessible:
    A1_retrievable_by_id_open_protocol: "yes"      # HTTPS + git, no authentication
    A1.1_protocol_open_free: "yes"
    A1.2_auth_where_needed: "n/a"                  # all content is public
    A2_metadata_persist_beyond_data: "partial"     # git history; no formal tombstoning
  interoperable:
    I1_formal_accessible_knowledge_representation: "partial"  # YAML validated by JSON Schema; no JSON-LD/RDF yet
    I2_FAIR_vocabularies: "partial"                # standards referenced, not embedded as ontology IRIs
    I3_qualified_references: "yes"                  # qualified links to llms.txt, RO-Crate, codemeta, CFF, Wilkinson 2016
  reusable:
    R1_plurality_of_attributes: "yes"
    R1.1_clear_data_usage_license: "yes"           # Apache-2.0 (LICENSE + CITATION.cff)
    R1.2_detailed_provenance: "partial"            # authorship + git history + CHANGELOG; no formal PROV
    R1.3_domain_community_standards: "yes"         # SPDX, CFF, JSON Schema, Keep a Changelog, SemVer

# ── Companion machine-readable artifacts (present or recommended) ──
companions:
  trust: null                              # no trust.md for this repo
  sitemap: null                            # not a website
  robots: null                             # not a website
  citation_cff: "/CITATION.cff"            # present — machine-readable citation
  codemeta: null                           # recommended for software metadata
  ro_crate: null                           # recommended for FAIR Digital Object packaging

maturity: "beta"
last_reviewed: "2026-06-08"
---

# fair.md — FAIR manifest for this repository

This file is the **fair.md FAIR manifest for the fair.md repository itself**: a
real, conformant manifest that self-declares how *Findable, Accessible,
Interoperable, and Reusable* this project is, and where the deeper
machine-readable affordances live. The YAML block above is the machine-readable
part; this prose is for people.

The repository "eats its own dog food": the manifest above conforms to the very
[specification](SPEC.md) it defines and validates against
[`schema/fair.schema.json`](schema/fair.schema.json) in CI.

## What this repository declares

This repo is the home of the **fair.md convention** — a proposed convention
(v0.1), not yet a standard. Its FAIR objects are the convention's artifacts:

- the formal [specification](SPEC.md),
- the JSON Schema for the YAML front matter ([`schema/`](schema/)),
- a fill-in [template](template/fair.md),
- a reference [example](examples/neuronautix.fair.md), and
- a [validator](tools/validate_fair.py) wired into CI.

## FAIR posture

Discovery and accessibility are strong: every artifact has a canonical
GitHub/raw URL over open HTTPS, and the project is publicly indexed and
searchable. The honest gaps are: no minted DOI yet (F1 — archiving a release to
Zenodo would close this), no JSON-LD/RDF representation (I1) and standards
referenced rather than embedded as ontology IRIs (I2), and provenance carried by
git history and the CHANGELOG rather than formal PROV (R1.2). Reusability is
otherwise strong — Apache-2.0 is declared in both `LICENSE` and `CITATION.cff`,
and the project follows SPDX, CFF, JSON Schema, Keep a Changelog, and SemVer.

## Companion artifacts

- **[`CITATION.cff`](CITATION.cff)** — machine-readable citation for the convention.
- `codemeta.json` and an RO-Crate are recommended next steps (currently `null`).

## How to adopt fair.md

This is the manifest for the repository, not the template. To adopt fair.md in
*your* project, copy [`template/fair.md`](template/fair.md) and follow the
instructions in the [README](README.md#how-to-adopt-fairmd).

## How to cite

See [`CITATION.cff`](CITATION.cff). In plain text:

> Huzard, D. (2026). *fair.md — a portable, human- and machine-readable FAIR
> manifest* (v0.1). https://github.com/Neuronautix/FAIR.md

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md) for the specification changelog.
