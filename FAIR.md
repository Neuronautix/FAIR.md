---
# Evidence-backed v0.3 manifest for this repository. This is not a certification.
fair_md_version: "0.3"
title: "fair.md — a FAIR manifest convention"
description: >
  The fair.md convention: a lightweight, human- and machine-readable FAIR
  manifest placed at the root of a repository or website. This repository holds
  the specification, schema, template, examples, validator, and a source-backed
  FAIR documentation pack.
identifiers:
  repository: "https://github.com/Neuronautix/FAIR.md"
  homepage: "https://github.com/Neuronautix/FAIR.md"
  canonical: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/FAIR.md"
  doi: "10.5281/zenodo.20793968"
maintainers:
  - name: "Damien Huzard, PhD"
    role: "author, specification editor, maintainer"
    orcid: "0000-0003-4820-7951"
    org: "Neuronautix — Montpellier, France"
license:
  content: "Apache-2.0"
  code: "Apache-2.0"

data_resources:
  - id: "specification"
    path: "/SPEC.md"
    type: "formal specification of the fair.md convention (Markdown)"
    topics: ["FAIR", "metadata", "specification"]
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/SPEC.md"
    media_type: "text/markdown"
    metadata: ["/FAIR.md", "/CITATION.cff"]
    license: "Apache-2.0"
    conforms_to: ["https://semver.org/spec/v2.0.0.html"]
  - id: "schema"
    path: "/schema/fair.schema.json"
    type: "JSON Schema (draft 2020-12) for the YAML front matter"
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/schema/fair.schema.json"
    media_type: "application/schema+json"
    metadata: ["/FAIR.md"]
    license: "Apache-2.0"
    conforms_to: ["https://json-schema.org/draft/2020-12/schema"]
  - id: "template"
    path: "/template/fair.md"
    type: "fill-in template with placeholder values and inline guidance"
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/template/fair.md"
    media_type: "text/markdown"
    metadata: ["/FAIR.md"]
    license: "Apache-2.0"
  - id: "examples"
    path: "/examples/"
    type: "reference fair.md manifests (worked examples)"
    count: 3
    identifier: "https://github.com/Neuronautix/FAIR.md/tree/main/examples"
    media_type: "text/markdown"
    metadata: ["/FAIR.md"]
    license: "Apache-2.0"
  - id: "validator"
    path: "/tools/"
    type: "Python validator for fair.md front matter (pyyaml + jsonschema)"
    identifier: "https://github.com/Neuronautix/FAIR.md/tree/main/tools"
    media_type: "text/x-python"
    metadata: ["/FAIR.md", "/CITATION.cff"]
    license: "Apache-2.0"
  - id: "fair-documentation"
    path: "/fair-documented/"
    type: "source registry, crosswalk, evidence rules, profiles, roadmap, and RO-Crate"
    identifier: "https://github.com/Neuronautix/FAIR.md/tree/main/fair-documented"
    media_type: "application/ld+json"
    metadata: ["/FAIR.md", "/fair-documented/ro-crate-metadata.json"]
    license: "Apache-2.0"
    conforms_to: ["https://w3id.org/ro/crate/1.3"]

vocabularies:
  - name: "FAIR Guiding Principles"
    identifier: "https://doi.org/10.1038/sdata.2016.18"
    version: "2016"
  - name: "RDA FAIR Data Maturity Model"
    identifier: "https://doi.org/10.15497/rda00050"
    version: "1.0"
  - name: "SPDX License List"
    identifier: "https://spdx.org/licenses/"
  - name: "Citation File Format"
    identifier: "https://citation-file-format.github.io/"
    version: "1.2.0"
  - name: "JSON Schema"
    identifier: "https://json-schema.org/draft/2020-12/schema"
    version: "2020-12"
  - name: "RO-Crate"
    identifier: "https://w3id.org/ro/crate/1.3"
    version: "1.3"

# Evidence documents what supports each result and what remains incomplete.
fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "partial"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D", "RDA-F1-02M", "RDA-F1-02D"]
      evidence:
        - id: "https://doi.org/10.5281/zenodo.20793968"
          type: "persistent-identifier"
          note: "A concept DOI covers all releases; most component resources still lack independent PIDs."
    F2_rich_metadata:
      status: "partial"
      metric_ids: ["RDA-F2-01M"]
      evidence:
        - id: "/FAIR.md"
          type: "metadata-record"
          note: "Project and resource metadata are present; distribution detail remains limited."
    F3_metadata_references_data_id:
      status: "partial"
      metric_ids: ["RDA-F3-01M"]
      evidence:
        - id: "/FAIR.md"
          type: "metadata-record"
          note: "Resources have identifiers, but most do not yet have independent metadata PIDs."
    F4_indexed_searchable:
      status: "partial"
      metric_ids: ["RDA-F4-01M"]
      evidence:
        - id: "https://github.com/Neuronautix/FAIR.md"
          type: "registry-record"
          note: "GitHub is searchable; no research-data catalog record exists yet."
  accessible:
    A1_retrievable_by_id_open_protocol:
      status: "yes"
      metric_ids: ["RDA-A1-02M", "RDA-A1-03M"]
      evidence:
        - id: "https://github.com/Neuronautix/FAIR.md"
          type: "automated-test"
          note: "Repository and raw resources are retrievable over HTTPS and git."
    A1.1_protocol_open_free:
      status: "yes"
      metric_ids: ["RDA-A1.1-01M"]
      evidence:
        - id: "https://www.rfc-editor.org/rfc/rfc9110"
          type: "standard"
          note: "HTTPS semantics are openly standardized and broadly implementable."
    A1.2_auth_where_needed:
      status: "n/a"
      metric_ids: ["RDA-A1.2-01D"]
      evidence:
        - id: "https://github.com/Neuronautix/FAIR.md"
          type: "policy"
          note: "All declared resources are public; no controlled-access data are in scope."
    A2_metadata_persist_beyond_data:
      status: "partial"
      metric_ids: ["RDA-A2-01M"]
      evidence:
        - id: "/fair-documented/roadmap.md"
          type: "policy"
          note: "Git history exists; an independent retention and tombstone policy is planned."
  interoperable:
    I1_formal_accessible_knowledge_representation:
      status: "partial"
      metric_ids: ["RDA-I1-01M"]
      evidence:
        - id: "/schema/fair.schema.json"
          type: "standard"
        - id: "/fair-documented/ro-crate-metadata.json"
          type: "metadata-record"
          note: "JSON Schema and one JSON-LD crate exist; full semantic export is not implemented."
    I2_FAIR_vocabularies:
      status: "partial"
      metric_ids: ["RDA-I2-01M"]
      evidence:
        - id: "/fair-documented/sources/registry.yaml"
          type: "registry-record"
          note: "Standards have resolvable IDs; field-level term mappings remain incomplete."
    I3_qualified_references:
      status: "partial"
      metric_ids: ["RDA-I3-01M"]
      evidence:
        - id: "/fair-documented/ro-crate-metadata.json"
          type: "metadata-record"
          note: "RO-Crate supplies typed relations for the documentation pack only."
  reusable:
    R1_plurality_of_attributes:
      status: "partial"
      metric_ids: ["RDA-R1-01M"]
      evidence:
        - id: "/FAIR.md"
          type: "metadata-record"
          note: "Core attributes exist; creators, dates, checksums, and distributions need expansion."
    R1.1_clear_data_usage_license:
      status: "partial"
      metric_ids: ["RDA-R1.1-01M", "RDA-R1.1-02M"]
      evidence:
        - id: "/LICENSE"
          type: "policy"
          note: "Apache-2.0 text is present, but content/data/database scopes need explicit treatment."
    R1.2_detailed_provenance:
      status: "partial"
      metric_ids: ["RDA-R1.2-01M", "RDA-R1.2-02M"]
      evidence:
        - id: "/CHANGELOG.md"
          type: "provenance"
        - id: "https://github.com/Neuronautix/FAIR.md/commits/main/"
          type: "provenance"
          note: "Human/git provenance exists; a PROV-O activity graph is not yet present."
    R1.3_domain_community_standards:
      status: "partial"
      metric_ids: ["RDA-R1.3-01M", "RDA-R1.3-02M"]
      evidence:
        - id: "/fair-documented/crosswalk.md"
          type: "standard"
          note: "Crosswalk and profiles are documented; a community-approved FIP is not yet published."

companions:
  trust: null
  sitemap: null
  robots: null
  citation_cff: "/CITATION.cff"
  codemeta: null
  ro_crate: "/fair-documented/ro-crate-metadata.json"
  source_registry: "/fair-documented/sources/registry.yaml"
  contributing: "/CONTRIBUTING.md"
  governance: "/GOVERNANCE.md"
  code_of_conduct: "/CODE_OF_CONDUCT.md"
  review_request: "/REVIEW_REQUEST.md"

profiles:
  - name: "RDA FAIR Data Maturity Model"
    identifier: "https://doi.org/10.15497/rda00050"
    status: "aligned"
    applies_to: ["specification", "schema", "template", "examples", "validator", "fair-documentation"]
    note: "Metric IDs are used, but complete 41-indicator assessment is future work."
  - name: "RO-Crate 1.3"
    identifier: "https://w3id.org/ro/crate/1.3"
    status: "adopted"
    applies_to: ["fair-documentation"]

openness:
  open_definition_version: "2.1"
  status: "partly-conformant"
  license_status: "mixed"
  access: "open"
  machine_readable: true
  open_format: true
  source_available: true
  evidence:
    - "/LICENSE"
    - "https://github.com/Neuronautix/FAIR.md"
    - "/fair-documented/crosswalk.md"

maturity: "beta"
last_reviewed: "2026-07-27"
---

# fair.md — FAIR manifest for this repository

This is the **fair.md manifest for the fair.md repository itself**. It records
an evidence-backed self-assessment of specific FAIR capabilities and points to
deeper machine-readable artifacts. It is not a certification or a claim that
every object in the repository is fully FAIR.

The repository "eats its own dog food": the manifest above conforms to the very
[specification](SPEC.md) it defines and validates against
[`schema/fair.schema.json`](schema/fair.schema.json) in CI.

## What this repository declares

This repo is the home of the **fair.md convention** — a proposed convention
(v0.3), not yet a standard. Its declared objects are the convention's artifacts:

- the formal [specification](SPEC.md),
- the JSON Schema for the YAML front matter ([`schema/`](schema/)),
- a fill-in [template](template/fair.md),
- complete v0.3 [generic dataset](examples/generic-dataset/FAIR.md) and
  [ISA-Tab](examples/isa-tab/FAIR.md) examples, plus a legacy
  [Neuronautix snapshot](examples/neuronautix.fair.md),
- a [validator](tools/validate_fair.py) wired into CI, and
- a [FAIR-documented source pack](fair-documented/README.md) containing the
  authoritative source registry, standards crosswalk, evidence rules, ISA
  profile, roadmap, and an RO-Crate 1.3 description.

## FAIR posture

HTTPS access is strong and releases are archived under the concept DOI
[10.5281/zenodo.20793968](https://doi.org/10.5281/zenodo.20793968), but the
manifest intentionally records most principles as `partial`. There is no
research catalog record, independent metadata-retention commitment, complete
semantic export, formal PROV-O graph, or community-approved FAIR Implementation
Profile. The evidence attached to each result identifies what exists and what
remains missing.

FAIR and openness are separate. The repository is openly accessible and uses
machine-readable open formats, but its single Apache-2.0 declaration does not yet
express separate software, documentation, data, database-rights, and third-party
content scopes. The Open Definition posture is therefore only
`partly-conformant`.

## Companion artifacts

- **[`CITATION.cff`](CITATION.cff)** — machine-readable citation for the convention.
- **[`fair-documented/ro-crate-metadata.json`](fair-documented/ro-crate-metadata.json)**
  — RO-Crate 1.3 metadata for the source pack.
- **[`fair-documented/sources/registry.yaml`](fair-documented/sources/registry.yaml)**
  — versioned registry of authoritative sources.
- `codemeta.json` remains planned.

## How to adopt fair.md

This is the manifest for the repository, not the template. To adopt fair.md in
*your* project, copy [`template/fair.md`](template/fair.md) and follow the
instructions in the [README](README.md#how-to-adopt-fairmd).

## How to cite

See [`CITATION.cff`](CITATION.cff). In plain text:

> Huzard, D. (2026). *fair.md — a portable, human- and machine-readable FAIR
> manifest* (v0.3.1). GitHub and Zenodo.
> https://github.com/Neuronautix/FAIR.md/releases/tag/v0.3.1

The v0.3.1 version DOI is assigned by Zenodo when the GitHub release is
published and is then added to the release page and citation metadata. Use the
[concept DOI](https://doi.org/10.5281/zenodo.20793968) when referring to the
fair.md project across all versions.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md) for the specification changelog.
