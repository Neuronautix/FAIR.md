# Governance and change approval

fair.md is currently a maintainer-led, community-reviewed proposed convention.
Governance is designed to keep the specification coherent while the contributor
base and independent reviewer group develop.

## Roles

### Maintainer

Maintainers manage releases, repository permissions, security, moderation, and
final integration. The current accountable maintainer is Damien Huzard
([ORCID 0000-0003-4820-7951](https://orcid.org/0000-0003-4820-7951)).

### Specification editor

Editors check consistency across the specification, schema, validator, template,
examples, crosswalks, and migration guidance. A maintainer may also serve as an
editor.

### Community reviewer

Reviewers contribute documented expertise in FAIR implementation, research data
stewardship, repositories, identifiers, metadata, assessment, open knowledge,
or a domain profile. Review participation does not imply endorsement by the
reviewer's employer or community.

### Contributor

Anyone following the contribution workflow and Code of Conduct may contribute.

## Decision classes

### Class 1: editorial

Examples include spelling, link repairs, source updates, explanatory text, and
tests that do not change accepted manifests.

Approval requirement: one maintainer or editor approval and passing CI.

### Class 2: backward-compatible normative

Examples include optional fields, new evidence types, warnings, companion keys,
and clarifications that do not invalidate conforming manifests.

Approval requirements:

1. a public design issue;
2. at least 14 calendar days for comment;
3. one maintainer approval;
4. one additional editor or community-reviewer approval where available;
5. passing CI and synchronized specification artifacts;
6. a changelog entry.

### Class 3: breaking or governance-sensitive

Examples include required fields, renamed or removed fields, changed status
semantics, stricter validation that invalidates conforming manifests, licensing
policy, conformance claims, or governance changes.

Approval requirements:

1. a public request for comments with alternatives and migration impact;
2. at least 30 calendar days for comment;
3. approval from one maintainer and at least one independent community reviewer;
4. explicit disposition of substantive objections;
5. a versioned migration guide, schema tests, examples, and changelog entry;
6. a major-version or documented pre-1.0 breaking release.

If the independent approval requirement cannot be met, the proposal remains
experimental and must not be represented as community consensus.

## Decision process

The default goal is reasoned consensus. The editor records the decision,
evidence considered, dissenting positions, compatibility impact, and follow-up
actions in the issue or pull request.

The maintainer may reject a change that is unsafe, legally problematic,
unsupported by evidence, outside project scope, or inconsistent with the FAIR
principles. A rejection must include a written rationale.

Contributors may appeal by opening a governance issue summarizing the disputed
decision and proposed resolution. Appeals involving the maintainer should seek
two independent community reviewers before closure.

## Release requirements

Every release must:

- identify the exact specification and schema version;
- pass the schema, validator, examples, and tests;
- update `CHANGELOG.md` and `CITATION.cff`;
- preserve backward-compatibility guidance;
- use a signed or annotated Git tag;
- be archived in a preservation repository with a version DOI;
- distinguish project/concept DOI from version DOI;
- state that manifest conformance is not FAIR certification;
- record unresolved limitations and known gaps.

## Conflicts of interest

Decision participants should disclose employment, funding, commercial products,
or standards roles that could reasonably be perceived as influencing the
decision. A disclosed interest does not automatically exclude participation,
but the decision record should show how it was managed.

## Governance evolution

When at least three sustained contributors from at least two independent
organizations are active, the project should review whether to establish a
multi-member steering group, defined terms, recusal rules, and succession
procedures.
