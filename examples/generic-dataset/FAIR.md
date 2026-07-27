---
# Complete v0.3 worked example. The data are synthetic and carry no endorsement.
fair_md_version: "0.3"
title: "Synthetic field observations — generic dataset example"
description: >
  A small synthetic CSV dataset used to demonstrate a complete evidence-backed
  FAIR.md v0.3 declaration for a generic research dataset.
identifiers:
  repository: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/generic-dataset"
  homepage: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/generic-dataset"
  canonical: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/generic-dataset/FAIR.md"
  doi: null
maintainers:
  - name: "Example Data Steward"
    role: "example author and data steward"
    org: "Example Research Institute"
license:
  content: "CC0-1.0"
  code: "Apache-2.0"

data_resources:
  - id: "observations"
    path: "/examples/generic-dataset/data/observations.csv"
    type: "synthetic tabular field observations in CSV"
    topics: ["field observations", "synthetic data", "FAIR example"]
    count: 3
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/generic-dataset/data/observations.csv"
    media_type: "text/csv"
    metadata: ["/examples/generic-dataset/metadata.json"]
    license: "CC0-1.0"
    conforms_to: ["https://www.w3.org/TR/tabular-data-primer/"]

vocabularies:
  - name: "FAIR Guiding Principles"
    identifier: "https://doi.org/10.1038/sdata.2016.18"
    version: "2016"
  - name: "Schema.org"
    identifier: "https://schema.org/"
  - name: "CSV on the Web"
    identifier: "https://www.w3.org/TR/tabular-data-model/"
    version: "W3C Recommendation"

fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "partial"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D"]
      evidence:
        - id: "/examples/generic-dataset/evidence/assessment.md"
          type: "persistent-identifier"
          note: "Stable web identifiers are shown; the synthetic dataset has no preservation PID."
    F2_rich_metadata:
      status: "yes"
      metric_ids: ["RDA-F2-01M"]
      evidence:
        - id: "/examples/generic-dataset/metadata.json"
          type: "metadata-record"
    F3_metadata_references_data_id:
      status: "yes"
      metric_ids: ["RDA-F3-01M"]
      evidence:
        - id: "/examples/generic-dataset/metadata.json"
          type: "metadata-record"
          note: "The JSON-LD distribution explicitly names the CSV content URL."
    F4_indexed_searchable:
      status: "partial"
      metric_ids: ["RDA-F4-01M"]
      evidence:
        - id: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/generic-dataset"
          type: "registry-record"
          note: "The example is indexed by GitHub, not a research-data catalog."
  accessible:
    A1_retrievable_by_id_open_protocol:
      status: "yes"
      metric_ids: ["RDA-A1-02M"]
      evidence:
        - id: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/generic-dataset/data/observations.csv"
          type: "automated-test"
    A1.1_protocol_open_free:
      status: "yes"
      metric_ids: ["RDA-A1.1-01M"]
      evidence:
        - id: "https://www.rfc-editor.org/rfc/rfc9110"
          type: "standard"
    A1.2_auth_where_needed:
      status: "n/a"
      metric_ids: ["RDA-A1.2-01D"]
      evidence:
        - id: "/examples/generic-dataset/evidence/assessment.md"
          type: "policy"
          note: "The synthetic example is intentionally public and requires no authorization."
    A2_metadata_persist_beyond_data:
      status: "planned"
      metric_ids: ["RDA-A2-01M"]
      evidence:
        - id: "/examples/generic-dataset/evidence/assessment.md"
          type: "policy"
          note: "A real deployment must identify a retention and tombstone policy."
  interoperable:
    I1_formal_accessible_knowledge_representation:
      status: "yes"
      metric_ids: ["RDA-I1-01M"]
      evidence:
        - id: "/examples/generic-dataset/metadata.json"
          type: "metadata-record"
          note: "Dataset metadata are expressed as Schema.org JSON-LD."
    I2_FAIR_vocabularies:
      status: "partial"
      metric_ids: ["RDA-I2-01M"]
      evidence:
        - id: "https://schema.org/"
          type: "standard"
          note: "Schema.org terms are used; domain terminology is intentionally absent."
    I3_qualified_references:
      status: "partial"
      metric_ids: ["RDA-I3-01M"]
      evidence:
        - id: "/examples/generic-dataset/metadata.json"
          type: "metadata-record"
          note: "The distribution relation is typed; broader qualified relations are not modeled."
  reusable:
    R1_plurality_of_attributes:
      status: "yes"
      metric_ids: ["RDA-R1-01M"]
      evidence:
        - id: "/examples/generic-dataset/metadata.json"
          type: "metadata-record"
    R1.1_clear_data_usage_license:
      status: "yes"
      metric_ids: ["RDA-R1.1-01M", "RDA-R1.1-02M"]
      evidence:
        - id: "https://creativecommons.org/publicdomain/zero/1.0/"
          type: "policy"
    R1.2_detailed_provenance:
      status: "partial"
      metric_ids: ["RDA-R1.2-01M"]
      evidence:
        - id: "/examples/generic-dataset/evidence/assessment.md"
          type: "provenance"
          note: "Synthetic generation is documented, but no PROV-O activity graph is supplied."
    R1.3_domain_community_standards:
      status: "partial"
      metric_ids: ["RDA-R1.3-01M"]
      evidence:
        - id: "https://www.w3.org/TR/tabular-data-model/"
          type: "standard"
          note: "The CSV example is aligned with generic tabular-data guidance only."

companions:
  trust: null
  sitemap: null
  robots: null
  citation_cff: null
  codemeta: null
  ro_crate: null
  metadata_jsonld: "/examples/generic-dataset/metadata.json"

profiles:
  - name: "RDA FAIR Data Maturity Model"
    identifier: "https://doi.org/10.15497/rda00050"
    status: "aligned"
    applies_to: ["observations"]
  - name: "W3C CSV on the Web"
    identifier: "https://www.w3.org/TR/tabular-data-model/"
    status: "aligned"
    applies_to: ["observations"]

openness:
  open_definition_version: "2.1"
  status: "conformant"
  license_status: "open"
  access: "open"
  machine_readable: true
  open_format: true
  source_available: true
  evidence:
    - "https://creativecommons.org/publicdomain/zero/1.0/"
    - "/examples/generic-dataset/data/observations.csv"

maturity: "prototype"
last_reviewed: "2026-07-27"
---

# Generic dataset worked example

This complete v0.3 example describes a small synthetic CSV file and its JSON-LD
metadata. It demonstrates honest mixed results: a capability is not marked
`yes` merely because a field exists.

The example is stored below the repository root for documentation. An adopting
project would place this file at its own root as `FAIR.md`, replace every
identifier and assessment with project-specific values, and provide a real
preservation policy and persistent dataset identifier.

## Evidence boundaries

The CSV and metadata are real files in this example. The observations are
synthetic. The example is not deposited in a research data repository, so F1,
F4, and A2 remain incomplete.

## Citation

This example is part of fair.md v0.3.1. Cite the version-specific DOI published
on <https://github.com/Neuronautix/FAIR.md/releases/tag/v0.3.1>.
