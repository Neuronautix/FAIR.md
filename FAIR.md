---
# fair.md — a portable, human- and machine-readable FAIR manifest for a repository
# Proposed convention (v0.1). Specification: https://github.com/Neuronautix/FAIR.md
# Reference implementation: https://neuronautix.com/fair.md
#
# HOW TO USE THIS TEMPLATE
# 1. Copy this file to the root of your repository/site as `fair.md`.
# 2. Replace every <PLACEHOLDER> with your project's values.
# 3. Fill in fair_assessment honestly — partial/planned are features, not failures.
# 4. Serve at https://yourdomain/fair.md.
# 5. Review periodically; update last_reviewed each time.

fair_md_version: "0.1"
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
  # Add more resources as needed

# ── Vocabularies / standards referenced (Interoperability) ──
vocabularies:
  - "<Standard or ontology name, e.g. 'schema.org'>"
  - "<e.g. 'FAIR Guiding Principles (Wilkinson et al., 2016)'>"
  # Use [] if no vocabularies apply (unusual — but the field must be present)

# ── FAIR self-assessment ──
# status enum: yes | partial | planned | no | n/a
# This is a TRANSPARENT SELF-ASSESSMENT, not a certified audit.
# Be honest: partial and planned are informative and improvable.
# Add a comment on each line explaining why.
fair_assessment:
  findable:
    F1_globally_unique_persistent_id: "<yes|partial|planned|no|n/a>"   # DOIs, persistent URLs?
    F2_rich_metadata: "<yes|partial|planned|no|n/a>"                    # per-item metadata?
    F3_metadata_references_data_id: "<yes|partial|planned|no|n/a>"     # metadata links back to data?
    F4_indexed_searchable: "<yes|partial|planned|no|n/a>"              # sitemap, registry, index?
  accessible:
    A1_retrievable_by_id_open_protocol: "<yes|partial|planned|no|n/a>" # HTTPS, OAI-PMH, etc.?
    A1.1_protocol_open_free: "<yes|partial|planned|no|n/a>"            # is the protocol open?
    A1.2_auth_where_needed: "<yes|partial|planned|no|n/a>"             # auth available if needed?
    A2_metadata_persist_beyond_data: "<yes|partial|planned|no|n/a>"    # tombstoning / archiving?
  interoperable:
    I1_formal_accessible_knowledge_representation: "<yes|partial|planned|no|n/a>"  # JSON-LD, RDF, etc.?
    I2_FAIR_vocabularies: "<yes|partial|planned|no|n/a>"               # ontologies embedded?
    I3_qualified_references: "<yes|partial|planned|no|n/a>"            # citations / links to related data?
  reusable:
    R1_plurality_of_attributes: "<yes|partial|planned|no|n/a>"         # rich descriptive metadata?
    R1.1_clear_data_usage_license: "<yes|partial|planned|no|n/a>"      # SPDX license declared?
    R1.2_detailed_provenance: "<yes|partial|planned|no|n/a>"           # authorship, methods, history?
    R1.3_domain_community_standards: "<yes|partial|planned|no|n/a>"    # community metadata standards met?

# ── Companion machine-readable artifacts (present or recommended) ──
# Use null for items you plan to add; do not omit lines — absence is informative.
companions:
  trust: null            # "/trust.md" — epistemic provenance & confidence
  sitemap: null          # "/sitemap.xml"
  robots: null           # "/robots.txt"
  citation_cff: null     # "/CITATION.cff" — machine-readable citation (recommended)
  codemeta: null         # "/codemeta.json" — software metadata
  ro_crate: null         # "/ro-crate-metadata.json" — FAIR Digital Object packaging

maturity: "prototype"    # prototype | beta | stable
last_reviewed: "<YYYY-MM-DD>"
---

# fair.md — <Repository or Dataset Title>

This file is a **FAIR manifest**: a single, human-readable and machine-parseable
declaration of how *Findable, Accessible, Interoperable, and Reusable* the data
and knowledge in this repository are, and where the deeper machine-readable
affordances live. The YAML block above is the machine-readable part; this prose
is for people.

It is a **proposed convention (v0.1)**. See the
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
