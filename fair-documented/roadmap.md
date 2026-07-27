# FAIR roadmap

## Must-haves

### P0 — integrity and honest claims

1. Require evidence objects for all v0.3 FAIR results.
2. Keep FAIR and Open Definition declarations as separate axes.
3. Give every described resource its own identifier, media type, metadata link,
   license scope, conformance declarations, and provenance.
4. Validate duplicate YAML keys, real calendar dates, cross-field references,
   and contradictory openness claims.
5. Keep an authoritative source registry with version, retrieval date, license,
   copy policy, and checksums for any vendored originals.
6. Use the exact lowercase root filename `fair.md`.
7. Treat unregistered `/.well-known/fair.md` discovery as experimental, not
   normative.

### P1 — machine actionability

1. Generate RO-Crate 1.3 JSON-LD and a FAIR Signposting Link Set from the same
   canonical manifest.
2. Add DCAT 3/DataCite mappings and model conceptual resources separately from
   downloadable distributions.
3. Add W3C PROV source-to-output lineage and SHA-256 checksums.
4. Use FAIRsharing/PID-backed identifiers for standards and vocabularies.
5. Add versioned repository deposits, DOI metadata, and a tombstone policy.
6. Add valid/invalid test fixtures for every semantic invariant.

### P2 — profiles and stewardship

1. Build a reusable FAIR Implementation Profile with community-selected
   FAIR-enabling resources.
2. Compile optional domain profiles, beginning with ISA-Tab/ISA-JSON.
3. Add accessible documentation, governance, and reuser feedback workflows.

## Killer features

- **Proof-carrying FAIR manifest:** every positive result has clickable evidence
  and a reproducible test.
- **FAIR diff:** pull requests show which target, criterion, evidence, or
  implementation choice improved or regressed.
- **One-graph multi-export:** generate `fair.md`, RO-Crate, DCAT, DataCite,
  Signposting, and citation metadata without drift.
- **Source-to-claim lineage:** trace a field or statement to its authoritative
  source, exact locator, checksum, transformation, and reviewer.
- **Profile compiler:** combine the core model with ISA or another domain
  profile to generate forms, validators, and crosswalks.
- **Open-rights linter:** flag “FAIR but not open,” license/domain mismatches,
  database/content rights gaps, and third-party exceptions.
- **Actionable remediation:** convert every `partial`, `planned`, or `no` result
  into a ranked task with impact, effort, owner, and due date.

## Acceptance criteria

- Every v0.3 FAIR result is an evidence object; no bare `yes` is accepted.
- Every profile references known resource IDs and a resolvable specification.
- An `openness.status: conformant` declaration passes only when license, access,
  machine readability, open format, and source availability conditions agree.
- Duplicate YAML keys and impossible dates fail validation.
- Every source entry records canonical URI, version/retrieval date, license
  status, and copy policy; every vendored copy has a SHA-256 checksum.
- Every local path declared by this repository exists with exact case.
- The package remains valid JSON/YAML and the automated test suite exercises
  both passing and failing fixtures.

