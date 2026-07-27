# Changelog — fair.md specification

All notable changes to the fair.md specification are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- Complete v0.3 worked packages for a generic dataset and an illustrative
  ISA-Tab Investigation–Study–Assay project.
- Contribution guidance, governance and change-approval rules, a Code of
  Conduct, a formal-review brief, and a structured standards-review issue
  template.

### Changed

- The root manifest now records Zenodo concept DOI
  `10.5281/zenodo.20793968`; citation documentation and `CITATION.cff` identify
  the exact v0.3.0 DOI `10.5281/zenodo.21621349`.
- Default validation now includes complete nested v0.3 example packages and
  checks their root-relative evidence and data references.

## [0.3] — 2026-07-27

Major integrity and FAIR-logic revision. Legacy v0.1/v0.2 manifests remain
supported.

### Added

- Evidence-backed v0.3 assessment objects with optional RDA FAIR Data Maturity
  Model metric identifiers.
- Structured, resolvable vocabulary declarations and implementation profiles.
- Separate Open Definition 2.1 declaration so FAIR is not conflated with open.
- Resource identifiers, media types, metadata links, licenses, and conformance
  references.
- `fair-documented/` source registry, standards crosswalk, evidence rules,
  optional ISA profile, roadmap, and RO-Crate 1.3 metadata.
- Behavioral validator tests and reproducible dependency ranges.

### Changed

- Confirmed `FAIR.md` as the canonical root manifest and aligned discovery,
  validation, examples, and documentation on its exact case.
- Replaced unsupported repository-wide positive claims with evidence-backed,
  conservative results.
- Reclassified `/.well-known/FAIR.md` as experimental until an RFC 8615
  registration exists.
- CI now validates the schema and runs the test suite before validating manifests.

### Fixed

- URI and calendar-date formats are now actually checked.
- Duplicate YAML keys, duplicate resource IDs, unknown profile targets, invalid
  ORCID checksums, malformed DOIs, invalid custom companions, contradictory
  openness declarations, and missing local references now fail validation.
- Corrected contradictory licensing and nonexistent companion declarations in
  the Neuronautix example.
- Replaced the schema's broken `$id` with a raw canonical URL.

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
[0.3]: https://github.com/Neuronautix/FAIR.md/compare/v0.2...HEAD
