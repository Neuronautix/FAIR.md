# Changelog — fair.md specification

All notable changes to the fair.md specification are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- Official expansion of the name: **fair.md — FAIR Assessment In a Repository**
  (`.md` = Markdown). Documentation-only; surfaced in the README, SPEC.md
  abstract, root manifest, and CITATION.cff. The file is still described as a
  "FAIR manifest."

---

## [0.2] — 2026-06-08

Minor, backward-compatible release: existing v0.1 manifests remain conformant
and `fair_md_version: "0.1"` is still accepted.

### Added

- Real, conformant `FAIR.md` manifest for this repository (the project now
  dogfoods its own convention; validated in CI alongside the example).
- `CITATION.cff` for machine-readable citation of the fair.md convention.
- `tools/validate_fair.py` — validates a fair.md file's YAML front matter against
  the JSON Schema and reports the Section 6 conformance warnings.
- GitHub Actions workflow (`.github/workflows/validate.yml`) running the validator
  on every push and pull request.

### Changed

- The fill-in template moved from the repository root to `template/fair.md`, so
  the root `FAIR.md` can be the project's real manifest. README links updated.
- `companions` values may now be absolute `http(s)` URLs (for companions hosted on
  another domain), not only root-relative paths. Schema and SPEC.md §4.1 / §6
  rule 9 updated accordingly.
- `fair_md_version` accepts `"0.2"` (and still `"0.1"`); spec, schema, template,
  example, and the root manifest bumped to 0.2.
- JSON Schema: `last_reviewed` now also asserts `format: date` in addition to the
  `YYYY-MM-DD` pattern.

### Fixed

- Repository URLs corrected from the non-existent `Neuronautix/fair-md` to
  `Neuronautix/FAIR.md` (schema `$id`, template, CHANGELOG).
- Broken README links: the template link (`fair.md` → `FAIR.md`) and the companion
  `trust.md` links (previously a broken `../trust-md/` relative path).
- Dropped `n/a` in the status enum mentioned in the example manifest's prose.

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

[0.2]: https://github.com/Neuronautix/FAIR.md/releases/tag/v0.2
[0.1]: https://github.com/Neuronautix/FAIR.md/releases/tag/v0.1
