# Changelog — fair.md specification

All notable changes to the fair.md specification are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1] — 2026-06-06

### Added

- Initial specification (SPEC.md) defining:
  - File location and discovery conventions (`/fair.md`, optional `/.well-known/fair.md` redirect)
  - YAML front-matter format with all required fields: `fair_md_version`, `title`, `description`, `identifiers`, `maintainers`, `license`, `data_resources`, `vocabularies`, `fair_assessment`, `companions`, `maturity`, `last_reviewed`
  - FAIR self-assessment status enum: `yes | partial | planned | no | n/a`
  - Canonical FAIR sub-principle key mapping (F1–F4, A1–A2, I1–I3, R1–R1.3)
  - Validation rules and three conformance levels (Conformant, Recommended, Extended)
  - Relationship to llms.txt, codemeta.json, CITATION.cff, RO-Crate, FAIR Signposting, trust.md
- Template file (`fair.md`) with all fields as `<PLACEHOLDER>` values and inline comments
- Reference implementation example (`examples/neuronautix.fair.md`) — the Neuronautix knowledge base
- JSON Schema (draft 2020-12) for the YAML front matter (`schema/fair.schema.json`)
- README with lineage, 30-second example, and adoption instructions
- LICENSE (Apache-2.0)

[0.1]: https://github.com/Neuronautix/fair-md/releases/tag/v0.1
