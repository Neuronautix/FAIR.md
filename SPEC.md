# fair.md — Formal Specification v0.1

**Status:** Proposed convention — v0.1
**Date:** 2026-06-06
**Author:** Damien Huzard, PhD (ORCID [0000-0003-4820-7951](https://orcid.org/0000-0003-4820-7951)), Neuronautix
**License:** Apache-2.0
**Reference implementation:** <https://neuronautix.com/fair.md>

---

## 1. Abstract

`fair.md` is a lightweight, human- and machine-readable FAIR manifest placed at
the root of a repository or website. It declares what data a project holds, gives
a structured self-assessment of the project's FAIR posture (Findable, Accessible,
Interoperable, Reusable), and points to deeper machine-readable affordances. It
is a front door, not a replacement, for heavier standards such as RO-Crate,
codemeta.json, or CITATION.cff.

---

## 2. File location and discovery

### 2.1 Primary location

A conforming `fair.md` file MUST be placed at the root of the repository or
website and served at:

```
https://<domain>/fair.md
```

For a Git repository without an associated web host, the file MUST be at the
repository root so it is accessible at:

```
https://raw.githubusercontent.com/<org>/<repo>/main/fair.md
```
(or the equivalent for other Git hosting platforms).

### 2.2 Optional well-known redirect

A server MAY additionally respond to:

```
https://<domain>/.well-known/fair.md
```

with a redirect (HTTP 301 or 302) to `https://<domain>/fair.md`. This provides a
stable, programmatically discoverable endpoint for crawlers and FAIR assessment
tools.

### 2.3 Content-Type

When served over HTTP, the file SHOULD be served with Content-Type
`text/markdown; charset=utf-8`.

---

## 3. File format

A `fair.md` file is a **Markdown document with a YAML front-matter block**.

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

The following fields are REQUIRED in every conforming `fair.md`.

#### `fair_md_version`

- **Type:** string
- **Required:** yes
- **Allowed values:** `"0.1"` (for this version of the specification)
- **Description:** The version of the fair.md specification this file conforms
  to. MUST be a quoted string.

```yaml
fair_md_version: "0.1"
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
| `canonical` | URI string | yes | The stable URL where this `fair.md` file is served |
| `doi` | string or `null` | yes | DOI if minted (e.g. `"10.5281/zenodo.1234567"`); `null` if not yet assigned |

```yaml
identifiers:
  repository: "https://github.com/myorg/myproject"
  homepage: "https://myproject.example.org"
  canonical: "https://myproject.example.org/fair.md"
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

```yaml
data_resources:
  - id: "recordings"
    path: "/data/recordings/"
    type: "HDF5 electrophysiology files, NWB format"
    topics: ["electrophysiology", "calcium imaging"]
    count: 42
```

#### `vocabularies`

- **Type:** sequence of strings
- **Required:** yes (may be an empty list `[]` if none apply, but the field MUST
  be present)
- **Description:** Controlled vocabularies, ontologies, and/or data standards
  referenced or used within this repository.

```yaml
vocabularies:
  - "Neurodata Without Borders (NWB)"
  - "schema.org"
  - "FAIR Guiding Principles (Wilkinson et al., 2016)"
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

Every sub-principle value MUST be one of:

| Value | Meaning |
|---|---|
| `"yes"` | The sub-principle is fully satisfied |
| `"partial"` | The sub-principle is partially satisfied; gaps exist |
| `"planned"` | Not yet satisfied but actively planned |
| `"no"` | Not satisfied and not currently planned |
| `"n/a"` | Not applicable to this repository or resource type |

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
path string (e.g. `"/trust.md"`) or `null`.

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

A `fair.md` file is considered **conformant** if:

1. The file is valid UTF-8.
2. The YAML front matter parses without errors.
3. All REQUIRED fields (Section 4.1) are present.
4. `fair_md_version` is a known version string (`"0.1"` for this specification).
5. All `fair_assessment` values are members of the status enum
   (`yes | partial | planned | no | n/a`).
6. `maturity` is one of `prototype | beta | stable`.
7. `last_reviewed` is a valid ISO 8601 date string in `YYYY-MM-DD` format.
8. `identifiers.canonical` is a valid URI.
9. All `companions` values are either `null` or a string beginning with `/`.
10. The prose section is present and non-empty.

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
| **Conformant** | All validation rules in Section 6 pass |
| **Recommended** | Conformant + no warnings from Section 6 |
| **Extended** | Recommended + `ro_crate` companion present + all FAIR sub-principles are `yes` or `n/a` |

### 7.2 Claiming conformance

A repository claiming fair.md conformance SHOULD include in its README or
documentation a statement such as:

> This repository provides a `fair.md` FAIR manifest conforming to the fair.md
> specification v0.1. See [fair.md](https://yourdomain/fair.md).

---

## 8. Relationship to other standards

| Standard | Relationship |
|---|---|
| **llms.txt** | Ergonomic model: one root Markdown file, machine-parseable YAML, human-readable prose |
| **codemeta.json / CITATION.cff** | fair.md points to these as companions; does not duplicate their semantics |
| **RO-Crate** | fair.md is a lightweight front door; `ro_crate` companion field links to the full package |
| **FAIR Signposting** | fair.md is the Markdown counterpart to HTTP-level FAIR Signposting links |
| **FAIR Guiding Principles (Wilkinson et al., 2016)** | Sub-principle keys map directly to F1–R1.3 |
| **trust.md** | Companion convention covering epistemic provenance and confidence (Section 4.1: `companions.trust`) |

---

## 9. Changelog

- **v0.1 (2026-06-06)** — initial specification, derived from the reference
  implementation at <https://neuronautix.com/fair.md>.
