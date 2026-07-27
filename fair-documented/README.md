# FAIR-documented source pack

This folder records the authoritative sources and implementation decisions used
to evolve `fair.md`. It separates four things that must not be conflated:

1. **FAIR principles** describe desired behavior for digital objects and their
   metadata.
2. **Implementation profiles** name the standards, services, vocabularies, and
   policies chosen by a community.
3. **Assessments** test a named target and attach evidence to each result.
4. **Openness** concerns permissions, access, machine readability, and open
   formats. A resource can be FAIR without being open.

No third-party source is copied here. The [source registry](sources/registry.yaml)
links to canonical originals and records a `reference-only` copy policy until
redistribution rights and version-specific checksums are verified.

## Contents

- [`sources/registry.yaml`](sources/registry.yaml) — authoritative source
  inventory with persistent identifiers, versions, licenses, and copy policy.
- [`crosswalk.md`](crosswalk.md) — mapping from `fair.md` to FAIR, RDA, Open
  Definition, RO-Crate, Signposting, and ISA concepts.
- [`profiles/isa-tab.md`](profiles/isa-tab.md) — optional life-science profile
  based on the ISA Investigation–Study–Assay model.
- [`evidence/README.md`](evidence/README.md) — evidence rules for FAIR claims.
- [`roadmap.md`](roadmap.md) — prioritized must-haves, killer features, and
  acceptance criteria.
- [`ro-crate-metadata.json`](ro-crate-metadata.json) — RO-Crate 1.3 metadata for
  this documentation pack.

## Maintenance rules

- Prefer persistent identifiers over organization home pages.
- Record the exact version and retrieval date used for every source.
- Do not vendor a source unless its license permits redistribution; record a
  SHA-256 checksum when a byte-identical copy is vendored.
- Link every normative change to at least one source ID and exact section.
- Treat positive FAIR results as claims requiring target-specific evidence, not
  as certification.
- Re-review the registry and crosswalk before each specification release.

