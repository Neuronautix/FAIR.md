# fair.md — Formal Specification v0.3

**Status:** Proposed convention — v0.3
**Date:** 2026-07-27
**Author:** Damien Huzard, PhD (ORCID [0000-0003-4820-7951](https://orcid.org/0000-0003-4820-7951)), Neuronautix
**License:** Apache-2.0
**Reference implementation:** <https://raw.githubusercontent.com/Neuronautix/FAIR.md/main/FAIR.md>

---

## 1. Abstract

`FAIR.md` is a lightweight, human- and machine-readable FAIR manifest placed at
the root of a repository or website. It declares what data a project holds, gives
a structured self-assessment of the project's FAIR posture (Findable, Accessible,
Interoperable, Reusable), and points to deeper machine-readable affordances. It
is a front door, not a replacement, for heavier standards such as RO-Crate,
codemeta.json, or CITATION.cff.

---

## 2. File location and discovery

### 2.1 Primary location

A conforming `FAIR.md` file MUST be placed at the root of the repository or
website and served at:

```
https://<domain>/FAIR.md
```

For a Git repository without an associated web host, the file MUST be at the
repository root so it is accessible at:

```
https://raw.githubusercontent.com/<org>/<repo>/main/FAIR.md
```
(or the equivalent for other Git hosting platforms).

### 2.2 Experimental well-known redirect

A deployment may experiment with:

```
https://<domain>/.well-known/fair.md
```

redirecting to `https://<domain>/FAIR.md`, but this is **not a normative
discovery mechanism**. `fair.md` is not currently registered in the IANA
Well-Known URI registry. Implementers MUST NOT present `/.well-known/fair.md` as
standardized unless it is registered under RFC 8615.

### 2.3 Content-Type

When served over HTTP, the file SHOULD be served with Content-Type
`text/markdown; charset=utf-8`.

---

## 3. File format

A `FAIR.md` file is a **Markdown document with a YAML front-matter block**.

### 3.1 Structure

```
---
<YAML front matter>
---

<Markdown prose>
```

- The YAML front matter MUST be the first element of the file, enclosed by `---`
  delimiters.
- The prose section is REQUIRED and MUST provide a human-readable narrative
  expanding on the machine-readable front matter.
- Both sections MUST be present in a conforming file.

### 3.2 Encoding

The file MUST be encoded in UTF-8. Line endings SHOULD be LF (`\n`).

---

## 4. YAML front-matter specification

### 4.1 Required fields

The following fields are REQUIRED in every conforming `FAIR.md`.

#### `fair_md_version`

- **Type:** string
- **Required:** yes
- **Allowed values:** `"0.3"` (current), `"0.2"`, or `"0.1"` (legacy versions
  remain accepted)
- **Description:** The version of the fair.md specification this file conforms
  to. MUST be a quoted string.

```yaml
fair_md_version: "0.3"
```

#### `title`

- **Type:** string
- **Required:** yes
- **Description:** A short, human-readable name for the repository or dataset
  this manifest covers.

```yaml
title: "My Research Repository"
```

#### `description`

- **Type:** string (scalar or YAML block scalar)
- **Required:** yes
- **Description:** A paragraph-length description of what the repository
  contains. May use the YAML `>` (folded) or `|` (literal) block scalar
  syntax for multi-line values.

```yaml
description: >
  Processed electrophysiology recordings for project X,
  including metadata in NWB format.
```

#### `identifiers`

- **Type:** mapping
- **Required:** yes
- **Sub-fields:**

| Sub-field | Type | Required | Description |
|---|---|---|---|
| `repository` | URI string | yes | URL of the source code / data repository (e.g. GitHub URL) |
| `homepage` | URI string | yes | Canonical homepage of the project |
| `canonical` | URI string | yes | The stable URL where this `FAIR.md` file is served |
| `doi` | string or `null` | yes | DOI if minted (e.g. `"10.5281/zenodo.1234567"`); `null` if not yet assigned |

```yaml
identifiers:
  repository: "https://github.com/myorg/myproject"
  homepage: "https://myproject.example.org"
  canonical: "https://myproject.example.org/FAIR.md"
  doi: null
```

#### `maintainers`

- **Type:** sequence of mappings
- **Required:** yes (at least one entry)
- **Each entry sub-fields:**

| Sub-field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Full name of the person |
| `role` | string | yes | Role(s) with respect to the repository (e.g. `"author, data curator"`) |
| `orcid` | string | recommended | ORCID iD in the format `"0000-0000-0000-000X"` |
| `org` | string | recommended | Institutional affiliation |

```yaml
maintainers:
  - name: "Jane Smith"
    role: "author, data curator"
    orcid: "0000-0000-0000-0001"
    org: "University of Example"
```

#### `license`

- **Type:** mapping
- **Required:** yes
- **Sub-fields:**

| Sub-field | Type | Required | Description |
|---|---|---|---|
| `content` | string | yes | SPDX license identifier for content/data (e.g. `"CC-BY-4.0"`). Use `"unspecified"` if not yet declared — but the field MUST be present. |
| `code` | string | yes | SPDX license identifier for code. Use `"unspecified"` if not declared. |

```yaml
license:
  content: "CC-BY-4.0"
  code: "Apache-2.0"
```

#### `data_resources`

- **Type:** sequence of mappings
- **Required:** yes (at least one entry)
- **Description:** Declares the FAIR objects this manifest covers. Not every file
  in the repository needs a separate entry — group by type or collection.
- **Each entry sub-fields:**

| Sub-field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | A short identifier for this resource (no spaces; use hyphens) |
| `path` | string | yes | Root path of this resource within the repository/site (e.g. `"/data/"`) |
| `type` | string | yes | Human-readable description of the resource type and format |
| `topics` | sequence of strings | optional | Topical keywords |
| `count` | integer | optional | Number of items in the collection, if applicable |
| `identifier` | URI string or `null` | required in v0.3 | Globally unique, preferably persistent and resolvable identifier for this resource |
| `media_type` | string | required in v0.3 | IANA media type for the representation |
| `metadata` | sequence of references | required in v0.3 | Root-relative paths or HTTP(S) URIs of metadata records that describe this resource |
| `license` | string | required in v0.3 | SPDX identifier or license URI applying to this resource |
| `conforms_to` | sequence of URIs | optional | Standards or profiles implemented by this resource |

```yaml
data_resources:
  - id: "recordings"
    path: "/data/recordings/"
    type: "HDF5 electrophysiology files, NWB format"
    topics: ["electrophysiology", "calcium imaging"]
    count: 42
    identifier: "https://doi.org/10.1234/example.recordings"
    media_type: "application/x-hdf5"
    metadata: ["/ro-crate-metadata.json"]
    license: "CC-BY-4.0"
    conforms_to: ["https://w3id.org/ro/crate/1.3"]
```

Version 0.3 authors SHOULD additionally describe distributions, access URLs,
checksums, byte sizes, creators, dates, and provenance in a companion such as
DCAT 3, DataCite metadata, or RO-Crate. A repository path is a locator, not
necessarily a persistent identifier.

#### `vocabularies`

- **Type:** sequence of strings in v0.1/v0.2; sequence of identified objects in v0.3
- **Required:** yes (may be an empty list `[]` if none apply, but the field MUST
  be present)
- **Description:** Controlled vocabularies, ontologies, and/or data standards
  referenced or used within this repository.

Version 0.3 entries MUST contain `name` and a resolvable `identifier`; `version`
and `registry` are optional. A label alone does not demonstrate vocabulary use
or conformance.

```yaml
vocabularies:
  - name: "RO-Crate"
    identifier: "https://w3id.org/ro/crate/1.3"
    version: "1.3"
  - name: "FAIR Guiding Principles"
    identifier: "https://doi.org/10.1038/sdata.2016.18"
```

#### `fair_assessment`

- **Type:** mapping (four sub-mappings)
- **Required:** yes
- **Description:** A transparent self-assessment of the repository's FAIR posture.
  This is NOT a certified audit — it is a maintainer-supplied, honest baseline
  intended to be improvable over time.
- **Structure:** Four top-level keys (`findable`, `accessible`, `interoperable`,
  `reusable`), each containing one sub-key per canonical FAIR sub-principle.

##### Status enum

Legacy v0.1/v0.2 manifests use a scalar status. Every status MUST be one of:

| Value | Meaning |
|---|---|
| `"yes"` | The sub-principle is fully satisfied |
| `"partial"` | The sub-principle is partially satisfied; gaps exist |
| `"planned"` | Not yet satisfied but actively planned |
| `"no"` | Not satisfied and not currently planned |
| `"n/a"` | Not applicable to this repository or resource type |

##### Evidence-backed assessment entries (v0.3)

Version 0.3 MUST represent every sub-principle as an object:

| Field | Required | Description |
|---|---|---|
| `status` | yes | One status from the enum above |
| `evidence` | yes | Non-empty sequence of evidence objects |
| `metric_ids` | no | Assessment indicator IDs, preferably from the RDA FAIR Data Maturity Model |
| `note` | no | Human-readable scope, gap, or rationale |

Each evidence object MUST contain `id`, a root-relative path or absolute HTTP(S)
URI, and `type`, one of `automated-test`, `metadata-record`,
`persistent-identifier`, `policy`, `provenance`, `registry-record`, `standard`,
or `other`. An optional `note` may explain what the evidence establishes.

A positive result is a scoped claim, not certification. `yes` requires passing,
target-specific evidence; `partial` MUST explain the remaining gap; `planned`
SHOULD link to a concrete roadmap action; and `n/a` MUST include a rationale.

##### Sub-principle keys and canonical mapping

The key names are deliberately prefixed with the canonical FAIR sub-principle
identifier so that automated assessment tools can map them directly.

**Findable**

| Key | FAIR sub-principle | Description |
|---|---|---|
| `F1_globally_unique_persistent_id` | F1 | Data/metadata have a globally unique and persistent identifier |
| `F2_rich_metadata` | F2 | Data are described with rich metadata |
| `F3_metadata_references_data_id` | F3 | Metadata clearly and explicitly include the identifier of the data they describe |
| `F4_indexed_searchable` | F4 | Data/metadata are registered or indexed in a searchable resource |

**Accessible**

| Key | FAIR sub-principle | Description |
|---|---|---|
| `A1_retrievable_by_id_open_protocol` | A1 | Data/metadata are retrievable by their identifier using a standardised communications protocol |
| `A1.1_protocol_open_free` | A1.1 | The protocol is open, free, and universally implementable |
| `A1.2_auth_where_needed` | A1.2 | The protocol allows for an authentication/authorisation procedure where necessary |
| `A2_metadata_persist_beyond_data` | A2 | Metadata are accessible even when the data are no longer available |

**Interoperable**

| Key | FAIR sub-principle | Description |
|---|---|---|
| `I1_formal_accessible_knowledge_representation` | I1 | Data/metadata use a formal, accessible, shared, and broadly applicable language for knowledge representation |
| `I2_FAIR_vocabularies` | I2 | Data/metadata use vocabularies that follow FAIR principles |
| `I3_qualified_references` | I3 | Data/metadata include qualified references to other data/metadata |

**Reusable**

| Key | FAIR sub-principle | Description |
|---|---|---|
| `R1_plurality_of_attributes` | R1 | Data/metadata are richly described with a plurality of accurate and relevant attributes |
| `R1.1_clear_data_usage_license` | R1.1 | Data/metadata are released with a clear and accessible data usage license |
| `R1.2_detailed_provenance` | R1.2 | Data/metadata are associated with detailed provenance |
| `R1.3_domain_community_standards` | R1.3 | Data/metadata meet domain-relevant community standards |

Legacy v0.1/v0.2 example:

```yaml
fair_assessment:
  findable:
    F1_globally_unique_persistent_id: "yes"
    F2_rich_metadata: "partial"
    F3_metadata_references_data_id: "yes"
    F4_indexed_searchable: "yes"
  accessible:
    A1_retrievable_by_id_open_protocol: "yes"
    A1.1_protocol_open_free: "yes"
    A1.2_auth_where_needed: "n/a"
    A2_metadata_persist_beyond_data: "partial"
  interoperable:
    I1_formal_accessible_knowledge_representation: "partial"
    I2_FAIR_vocabularies: "partial"
    I3_qualified_references: "yes"
  reusable:
    R1_plurality_of_attributes: "yes"
    R1.1_clear_data_usage_license: "yes"
    R1.2_detailed_provenance: "planned"
    R1.3_domain_community_standards: "partial"
```

Version 0.3 example:

```yaml
fair_assessment:
  findable:
    F1_globally_unique_persistent_id:
      status: "partial"
      metric_ids: ["RDA-F1-01M", "RDA-F1-01D"]
      evidence:
        - id: "https://doi.org/10.1234/example"
          type: "persistent-identifier"
          note: "Dataset PID exists; metadata record lacks an independent PID."
  # All remaining canonical sub-principles are required in the same form.
```

#### `companions`

- **Type:** mapping
- **Required:** yes
- **Description:** Paths to companion machine-readable artifacts. Use `null` for
  items that do not exist yet (do not omit them — their absence is informative).
- **Recommended sub-fields:**

| Sub-field | Description |
|---|---|
| `trust` | Path to `trust.md` (epistemic provenance companion) |
| `sitemap` | Path to `sitemap.xml` |
| `robots` | Path to `robots.txt` |
| `citation_cff` | Path to `CITATION.cff` (machine-readable citation) |
| `codemeta` | Path to `codemeta.json` (software metadata) |
| `ro_crate` | Path to `ro-crate-metadata.json` (FAIR Digital Object packaging) |

Additional companion keys are permitted. Values MUST be either a root-relative
path string (e.g. `"/trust.md"`), an absolute `http(s)` URL (e.g.
`"https://example.org/trust.md"`, for a companion hosted on another domain),
or `null`.

```yaml
companions:
  trust: "/trust.md"
  sitemap: "/sitemap.xml"
  robots: "/robots.txt"
  citation_cff: null
  codemeta: null
  ro_crate: null
```

#### `maturity`

- **Type:** string
- **Required:** yes
- **Allowed values:**

| Value | Meaning |
|---|---|
| `"prototype"` | Early-stage; the FAIR posture may change substantially |
| `"beta"` | Mostly stable; known gaps are actively being addressed |
| `"stable"` | Stable; the FAIR posture is maintained and reviewed regularly |

```yaml
maturity: "beta"
```

#### `last_reviewed`

- **Type:** string
- **Required:** yes
- **Format:** ISO 8601 date: `YYYY-MM-DD`
- **Description:** The date when the maintainer last honestly reviewed the
  self-assessment and confirmed it is up to date.

```yaml
last_reviewed: "2026-06-06"
```

---

#### `profiles` (v0.3)

- **Type:** non-empty sequence of mappings
- **Required:** v0.3 only
- **Description:** Concrete implementation or community profiles used to
  operationalize the generic FAIR principles.

Each entry MUST contain `name`, an absolute URI `identifier`, `status`
(`adopted | aligned | planned | not-applicable`), and a non-empty `applies_to`
list of IDs declared in `data_resources`. `registry` and `note` are optional.
ISA-Tab is an optional domain profile for relevant experimental data; it is not
a universal FAIR requirement.

#### `openness` (v0.3)

- **Type:** mapping
- **Required:** v0.3 only
- **Description:** A separate Open Definition 2.1 posture. FAIR does not imply
  open, and access-controlled data can still be FAIR.

Required fields are `open_definition_version` (`"2.1"`), `status`
(`conformant | partly-conformant | not-conformant | not-assessed`),
`license_status`, `access`, the booleans `machine_readable`, `open_format`, and
`source_available`, plus non-empty `evidence`. If `status` is `conformant`, the
license and access MUST be open and all three booleans MUST be true.

---

### 4.2 Optional fields

Additional YAML fields MAY be added by implementers for domain-specific purposes.
They MUST NOT conflict with the names defined in this specification. Implementers
are encouraged to namespace custom fields (e.g. `x_myproject_fieldname`).

---

### 4.3 YAML comments

YAML comments (lines beginning with `#`) are permitted and encouraged in the
front matter to explain assessments and link to evidence.

---

## 5. Prose section

The Markdown prose section following the `---` closing delimiter SHOULD include:

1. A short statement of what the repository is and what the manifest covers.
2. A human-readable explanation of the FAIR self-assessment — especially the
   `partial` and `planned` items and what they mean in practice.
3. A pointer to the companion `trust.md` if present.
4. A "How to adopt" or "How to use" section if the repository is itself defining
   a convention.
5. A changelog.

The prose section MUST NOT contradict the YAML front matter.

---

## 6. Validation rules

A `FAIR.md` file is considered **conformant** if:

1. The file is valid UTF-8.
2. The YAML front matter parses without errors.
3. All REQUIRED fields (Section 4.1) are present.
4. `fair_md_version` is a known version string (`"0.1"`, `"0.2"`, or `"0.3"`).
5. Legacy `fair_assessment` values are status strings; v0.3 values are
   evidence-backed objects containing a valid status and non-empty evidence.
6. `maturity` is one of `prototype | beta | stable`.
7. `last_reviewed` is a real ISO 8601 calendar date in `YYYY-MM-DD` format.
8. All identifier fields declared as URIs pass URI format validation.
9. All `companions` values are either `null`, a root-relative path beginning
   with `/`, or an absolute `http(s)` URL.
10. The prose section is present and non-empty.
11. Mapping keys and `data_resources[].id` values are unique.
12. In v0.3, `profiles` references only declared resource IDs and `openness`
    passes its cross-field consistency rules.

A **warning** (non-blocking) SHOULD be issued if:

- `license.content` or `license.code` is `"unspecified"`.
- `maintainers[*].orcid` is absent for any maintainer.
- `identifiers.doi` is `null`.
- Any `fair_assessment` value is `"no"` (not a failure — but worth flagging for
  attention).

---

## 7. Conformance

### 7.1 Levels

| Level | Requirements |
|---|---|
| **Legacy structural** | A v0.1/v0.2 manifest passes the structural rules |
| **Evidence-backed** | A v0.3 manifest passes the structural and semantic rules, with evidence for every result |
| **Packaged** | Evidence-backed + a valid RO-Crate companion and a versioned source registry |

These are manifest conformance levels, not FAIRness scores or certification.
No level requires all sub-principles to be `yes`; such a rule would reward
unsupported claims and misuse of `n/a`.

### 7.2 Claiming conformance

A repository claiming fair.md conformance SHOULD include in its README or
documentation a statement such as:

> This repository provides a `FAIR.md` FAIR manifest conforming to the fair.md
> specification v0.3. See [FAIR.md](https://yourdomain/FAIR.md).

---

## 8. Relationship to other standards

| Standard | Relationship |
|---|---|
| **llms.txt** | Ergonomic model: one root Markdown file, machine-parseable YAML, human-readable prose |
| **codemeta.json / CITATION.cff** | fair.md points to these as companions; does not duplicate their semantics |
| **RO-Crate** | fair.md is a lightweight front door; `ro_crate` companion field links to the full package |
| **FAIR Signposting** | fair.md is the Markdown counterpart to HTTP-level FAIR Signposting links |
| **FAIR Guiding Principles (Wilkinson et al., 2016)** | Sub-principle keys map directly to F1–R1.3 |
| **RDA FAIR Data Maturity Model** | v0.3 assessment entries can cite reusable metric identifiers |
| **GO FAIR Implementation Profiles** | `profiles` declares concrete community implementation choices; it is not an assessment score |
| **FAIR Cookbook** | Non-normative implementation recipes and maturity guidance |
| **FAIRsharing** | Preferred registry for persistent identifiers of standards, databases, and policies |
| **Open Definition 2.1** | `openness` reports permissions and technical openness separately from FAIR |
| **ISA-Tab / ISA-JSON** | Optional Investigation–Study–Assay domain profile for applicable experimental data |
| **DCAT 3 / DataCite** | Recommended companions for dataset, distribution, catalog, and citation metadata |
| **trust.md** | Companion convention covering epistemic provenance and confidence (Section 4.1: `companions.trust`) |

---

## 9. Changelog

- **v0.3 (2026-07-27)** — evidence-backed assessment objects, identified
  vocabularies, richer resource metadata, implementation profiles, a separate
  Open Definition declaration, canonical `FAIR.md` filename enforcement, real URI/date
  checks, duplicate-key rejection, and source-backed FAIR documentation.
- **v0.2 (2026-06-08)** — backward-compatible additions: `companions` values may
  now be absolute `http(s)` URLs in addition to root-relative paths (§4.1, §6
  rule 9); `fair_md_version` accepts `"0.2"` (and still `"0.1"`). Repository
  additions (non-normative): JSON Schema asserts `format: date` for
  `last_reviewed`, a validator (`tools/validate_fair.py`) with CI, a
  `CITATION.cff`, and a real root manifest for this repository.
- **v0.1 (2026-06-06)** — initial specification, derived from the reference
  implementation at <https://neuronautix.com/fair.md>.
