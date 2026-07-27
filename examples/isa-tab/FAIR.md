---
# Complete v0.3 FAIR.md example for an illustrative ISA-Tab project.
fair_md_version: "0.3"
title: "Synthetic temperature assay — ISA-Tab project example"
description: >
  An illustrative ISA-Tab Investigation–Study–Assay package with synthetic
  measurements, used to demonstrate a complete domain-profiled FAIR.md v0.3
  declaration. ISA conformance is aligned but not certified.
identifiers:
  repository: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/isa-tab"
  homepage: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/isa-tab"
  canonical: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/FAIR.md"
  doi: null
maintainers:
  - name: "Example ISA Data Steward"
    role: "example author and ISA data steward"
    org: "Example Life Science Institute"
license:
  content: "CC-BY-4.0"
  code: "Apache-2.0"

data_resources:
  - id: "investigation"
    path: "/examples/isa-tab/i_investigation.txt"
    type: "ISA-Tab Investigation file"
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/i_investigation.txt"
    media_type: "text/tab-separated-values"
    metadata: ["/examples/isa-tab/i_investigation.txt"]
    license: "CC-BY-4.0"
    conforms_to: ["https://isa-specs.readthedocs.io/en/latest/isatab.html"]
  - id: "study"
    path: "/examples/isa-tab/s_study.txt"
    type: "ISA-Tab Study file describing sources and samples"
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/s_study.txt"
    media_type: "text/tab-separated-values"
    metadata: ["/examples/isa-tab/i_investigation.txt"]
    license: "CC-BY-4.0"
    conforms_to: ["https://isa-specs.readthedocs.io/en/latest/isatab.html"]
  - id: "assay"
    path: "/examples/isa-tab/a_assay.txt"
    type: "ISA-Tab Assay file linking samples to measurements"
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/a_assay.txt"
    media_type: "text/tab-separated-values"
    metadata: ["/examples/isa-tab/i_investigation.txt"]
    license: "CC-BY-4.0"
    conforms_to: ["https://isa-specs.readthedocs.io/en/latest/isatab.html"]
  - id: "measurements"
    path: "/examples/isa-tab/data/measurements.csv"
    type: "synthetic temperature measurements in CSV"
    count: 2
    identifier: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/data/measurements.csv"
    media_type: "text/csv"
    metadata:
      - "/examples/isa-tab/i_investigation.txt"
      - "/examples/isa-tab/a_assay.txt"
    license: "CC-BY-4.0"
    conforms_to: ["https://isa-specs.readthedocs.io/en/latest/isatab.html"]

vocabularies:
  - name: "ISA Model and Serialization Specifications"
    identifier: "https://isa-specs.readthedocs.io/en/latest/"
    version: "1.0"
  - name: "Ontology for Biomedical Investigations"
    identifier: "http://purl.obolibrary.org/obo/obi.owl"
  - name: "Phenotype and Trait Ontology"
    identifier: "http://purl.obolibrary.org/obo/pato.owl"
  - name: "Environment Ontology"
    identifier: "http://purl.obolibrary.org/obo/envo.owl"
  - name: "Units of measurement ontology"
    identifier: "http://purl.obolibrary.org/obo/uo.owl"
  - name: "FAIR Guiding Principles"
    identifier: "https://doi.org/10.1038/sdata.2016.18"
    version: "2016"

fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "partial"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D"]
      evidence:
        - id: "/examples/isa-tab/evidence/assessment.md"
          type: "persistent-identifier"
          note: "Web identifiers exist, but the illustrative investigation has no preservation PID."
    F2_rich_metadata:
      status: "yes"
      metric_ids: ["RDA-F2-01M"]
      evidence:
        - id: "/examples/isa-tab/i_investigation.txt"
          type: "metadata-record"
    F3_metadata_references_data_id:
      status: "yes"
      metric_ids: ["RDA-F3-01M"]
      evidence:
        - id: "/examples/isa-tab/a_assay.txt"
          type: "metadata-record"
          note: "The assay graph links samples to the measurement data file."
    F4_indexed_searchable:
      status: "partial"
      metric_ids: ["RDA-F4-01M"]
      evidence:
        - id: "https://github.com/Neuronautix/FAIR.md/tree/main/examples/isa-tab"
          type: "registry-record"
          note: "GitHub is searchable; the example is not registered in a life-science repository."
  accessible:
    A1_retrievable_by_id_open_protocol:
      status: "yes"
      metric_ids: ["RDA-A1-02M"]
      evidence:
        - id: "https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/examples/isa-tab/i_investigation.txt"
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
        - id: "/examples/isa-tab/evidence/assessment.md"
          type: "policy"
          note: "All synthetic example files are public."
    A2_metadata_persist_beyond_data:
      status: "planned"
      metric_ids: ["RDA-A2-01M"]
      evidence:
        - id: "/examples/isa-tab/evidence/assessment.md"
          type: "policy"
          note: "A real ISA deployment must name its archive and tombstone policy."
  interoperable:
    I1_formal_accessible_knowledge_representation:
      status: "partial"
      metric_ids: ["RDA-I1-01M"]
      evidence:
        - id: "https://isa-specs.readthedocs.io/en/latest/isatab.html"
          type: "standard"
          note: "ISA-Tab is a formal shared serialization; no ISA-JSON-LD/RDF representation is included."
    I2_FAIR_vocabularies:
      status: "partial"
      metric_ids: ["RDA-I2-01M"]
      evidence:
        - id: "/examples/isa-tab/i_investigation.txt"
          type: "metadata-record"
          note: "OBI, PATO, ENVO, and UO sources are declared; term coverage is intentionally minimal."
    I3_qualified_references:
      status: "yes"
      metric_ids: ["RDA-I3-01M"]
      evidence:
        - id: "/examples/isa-tab/s_study.txt"
          type: "metadata-record"
        - id: "/examples/isa-tab/a_assay.txt"
          type: "metadata-record"
          note: "Study and assay tables encode qualified material and process relationships."
  reusable:
    R1_plurality_of_attributes:
      status: "yes"
      metric_ids: ["RDA-R1-01M"]
      evidence:
        - id: "/examples/isa-tab/i_investigation.txt"
          type: "metadata-record"
    R1.1_clear_data_usage_license:
      status: "yes"
      metric_ids: ["RDA-R1.1-01M", "RDA-R1.1-02M"]
      evidence:
        - id: "https://creativecommons.org/licenses/by/4.0/"
          type: "policy"
    R1.2_detailed_provenance:
      status: "partial"
      metric_ids: ["RDA-R1.2-01M"]
      evidence:
        - id: "/examples/isa-tab/evidence/assessment.md"
          type: "provenance"
          note: "Protocols and graph lineage are present; tool-version and PROV-O activity metadata are absent."
    R1.3_domain_community_standards:
      status: "partial"
      metric_ids: ["RDA-R1.3-01M", "RDA-R1.3-02M"]
      evidence:
        - id: "https://isa-specs.readthedocs.io/en/latest/isatab.html"
          type: "standard"
          note: "The package is ISA-Tab aligned but has not been certified by an ISA API validation report."

companions:
  trust: null
  sitemap: null
  robots: null
  citation_cff: null
  codemeta: null
  ro_crate: null
  isa_investigation: "/examples/isa-tab/i_investigation.txt"
  isa_study: "/examples/isa-tab/s_study.txt"
  isa_assay: "/examples/isa-tab/a_assay.txt"

profiles:
  - name: "ISA Model and Serialization Specifications"
    identifier: "https://isa-specs.readthedocs.io/en/latest/"
    registry: "https://fairsharing.org/FAIRsharing.53gp75"
    status: "aligned"
    applies_to: ["investigation", "study", "assay", "measurements"]
    note: "Illustrative alignment only; no external ISA validator report is claimed."
  - name: "RDA FAIR Data Maturity Model"
    identifier: "https://doi.org/10.15497/rda00050"
    status: "aligned"
    applies_to: ["investigation", "study", "assay", "measurements"]

openness:
  open_definition_version: "2.1"
  status: "conformant"
  license_status: "open"
  access: "open"
  machine_readable: true
  open_format: true
  source_available: true
  evidence:
    - "https://creativecommons.org/licenses/by/4.0/"
    - "/examples/isa-tab/i_investigation.txt"
    - "/examples/isa-tab/data/measurements.csv"

maturity: "prototype"
last_reviewed: "2026-07-27"
---

# ISA-Tab project worked example

This complete FAIR.md v0.3 example covers one illustrative Investigation, one
Study, one Assay, and one synthetic measurement file.

The ISA profile is deliberately marked `aligned`, not `adopted`: the example
demonstrates the expected declarations and graph, but the repository does not
claim an external ISA API validation result or ISA community endorsement.

An adopting project should place this file at its repository root, run the ISA
validator against `i_investigation.txt`, archive the package in an appropriate
life-science repository, and replace all example identifiers and evidence.

## Citation

This example is part of fair.md v0.3.1:
<https://doi.org/10.5281/zenodo.21622631>.
