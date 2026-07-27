---
# fair.md — a portable, human- and machine-readable FAIR manifest for a repository
# Proposed convention (v0.3). Specification: https://github.com/Neuronautix/FAIR.md
# Reference implementation: https://neuronautix.com/fair.md
#
# HOW TO USE THIS TEMPLATE
# 1. Copy this file to the root of your repository/site as `fair.md`.
# 2. Replace every <PLACEHOLDER> with your project's values.
# 3. Attach evidence to every FAIR result; bare statuses are invalid in v0.3.
# 4. Serve at https://yourdomain/fair.md.
# 5. Review periodically; update last_reviewed each time.

fair_md_version: "0.3"
title: "<Repository or Dataset Title>"
description: >
  <A paragraph-length description of what this repository contains and what
  the FAIR objects are. Be specific about data types, domains, and purpose.>

identifiers:
  repository: "<https://github.com/yourorg/yourrepo>"
  homepage: "<https://yourproject.example.org>"
  canonical: "<https://yourproject.example.org/fair.md>"
  doi: null   # replace with "10.xxxx/xxxxx" once minted; null is valid

maintainers:
  - name: "<Full Name>"
    role: "<author | curator | maintainer — list all that apply>"
    orcid: "<0000-0000-0000-0000>"   # strongly recommended; remove line if unknown
    org: "<Institutional affiliation>"
  # Add more maintainers as needed:
  # - name: "<Full Name>"
  #   role: "<role>"
  #   orcid: "<0000-0000-0000-0000>"

license:
  # Use SPDX identifiers: https://spdx.org/licenses/
  # Common values: CC-BY-4.0, CC0-1.0, Apache-2.0, MIT, GPL-3.0-only
  # Use "unspecified" if not yet declared — but the field MUST be present.
  content: "<CC-BY-4.0>"
  code: "<Apache-2.0>"

# ── What "data" this manifest covers (the FAIR objects) ──
data_resources:
  - id: "<resource-id>"             # short identifier, no spaces (use hyphens)
    path: "/<path/to/resource/>"
    type: "<file format and nature, e.g. 'CSV tabular data, sample metadata'>"
    topics: ["<topic1>", "<topic2>"]   # optional; remove if not applicable
    count: null                        # optional; number of items/files
    identifier: null                   # resolvable PID/URI; null while unavailable
    media_type: "<text/csv>"
    metadata: ["/<metadata-record.json>"]
    license: "<CC-BY-4.0>"
    conforms_to: ["<https://identifier.for/community-standard>"]
  # Add more resources as needed

# ── Vocabularies / standards referenced (Interoperability) ──
vocabularies:
  - name: "<Standard or ontology name>"
    identifier: "<https://persistent.identifier/for/standard>"
    version: "<version>"               # optional
    registry: "<https://fairsharing.org/...>"  # optional

# ── FAIR self-assessment ──
# status enum: yes | partial | planned | no | n/a
# This is a TRANSPARENT SELF-ASSESSMENT, not a certified audit.
# Evidence type: automated-test | metadata-record | persistent-identifier |
# policy | provenance | registry-record | standard | other
fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "<yes|partial|planned|no|n/a>"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D"]
      evidence: [{id: "<https://pid.example/object>", type: "persistent-identifier"}]
    F2_rich_metadata:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<metadata-record>", type: "metadata-record"}]
    F3_metadata_references_data_id:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<metadata-record>", type: "metadata-record"}]
    F4_indexed_searchable:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "<https://catalog.example/record>", type: "registry-record"}]
  accessible:
    A1_retrievable_by_id_open_protocol:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "<https://access.example/object>", type: "automated-test"}]
    A1.1_protocol_open_free:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "<https://protocol-spec.example>", type: "standard"}]
    A1.2_auth_where_needed:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<access-policy>", type: "policy"}]
    A2_metadata_persist_beyond_data:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<preservation-policy>", type: "policy"}]
  interoperable:
    I1_formal_accessible_knowledge_representation:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<metadata.jsonld>", type: "metadata-record"}]
    I2_FAIR_vocabularies:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "<https://vocabulary.example>", type: "registry-record"}]
    I3_qualified_references:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<metadata.jsonld>", type: "metadata-record"}]
  reusable:
    R1_plurality_of_attributes:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<metadata-record>", type: "metadata-record"}]
    R1.1_clear_data_usage_license:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/LICENSE", type: "policy"}]
    R1.2_detailed_provenance:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "/<provenance.jsonld>", type: "provenance"}]
    R1.3_domain_community_standards:
      status: "<yes|partial|planned|no|n/a>"
      evidence: [{id: "<https://profile.example>", type: "standard"}]

# ── Companion machine-readable artifacts (present or recommended) ──
# Use null for items you plan to add; do not omit lines — absence is informative.
companions:
  trust: null            # "/trust.md" — epistemic provenance & confidence
  sitemap: null          # "/sitemap.xml"
  robots: null           # "/robots.txt"
  citation_cff: null     # "/CITATION.cff" — machine-readable citation (recommended)
  codemeta: null         # "/codemeta.json" — software metadata
  ro_crate: null         # "/ro-crate-metadata.json" — FAIR Digital Object packaging

# Concrete implementation choices; these are not assessment scores.
profiles:
  - name: "<Community or domain profile>"
    identifier: "<https://persistent.identifier/profile>"
    registry: "<https://fairsharing.org/...>"  # optional
    status: "<adopted|aligned|planned|not-applicable>"
    applies_to: ["<resource-id>"]

# Openness is separate from FAIR. Restricted-but-FAIR data are valid.
openness:
  open_definition_version: "2.1"
  status: "<conformant|partly-conformant|not-conformant|not-assessed>"
  license_status: "<open|mixed|restricted|unspecified>"
  access: "<open|conditional|restricted|closed>"
  machine_readable: true
  open_format: true
  source_available: true
  evidence: ["/LICENSE"]

maturity: "prototype"    # prototype | beta | stable
last_reviewed: "<YYYY-MM-DD>"
---

# fair.md — <Repository or Dataset Title>

This file is a **FAIR manifest**: a single, human-readable and machine-parseable
declaration of how *Findable, Accessible, Interoperable, and Reusable* the data
and knowledge in this repository are, and where the deeper machine-readable
affordances live. The YAML block above is the machine-readable part; this prose
is for people.

It is a **proposed convention (v0.3)**. See the
[fair.md specification](https://github.com/Neuronautix/FAIR.md) and the
[reference implementation](https://neuronautix.com/fair.md).

## What this repository declares

<!-- Replace this section with a short narrative of what data/knowledge is here,
     and what the FAIR self-assessment means in practice for your project.
     Explain any "partial" or "planned" entries. -->

## FAIR posture

<!-- Summarise the assessment: what is strong, what are the known gaps, and
     what is planned to improve. Honest gaps are features. -->

## Companion artifacts

<!-- List the companion files that exist and what they add. -->

## How to cite

<!-- If CITATION.cff is not present yet, add a plain-text citation here. -->

## Changelog

- **v0.1 (<YYYY-MM-DD>)** — initial fair.md for this repository.
