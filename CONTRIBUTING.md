# Contributing to fair.md

Thank you for helping improve fair.md. The project is a proposed convention, not
an endorsed FAIR standard or certification scheme. Contributions from research
data stewards, scientists, repository operators, standards maintainers,
software developers, and accessibility specialists are welcome.

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md), and
normative decisions follow [GOVERNANCE.md](GOVERNANCE.md).

## Before opening a change

- Search existing issues and pull requests.
- Use an issue first for new fields, renamed fields, status semantics,
  conformance rules, or mappings to external standards.
- Identify the digital object and user community affected by the proposal.
- Link authoritative sources using persistent identifiers where possible.
- Distinguish FAIRness, openness, implementation choices, and assessment
  evidence.

## Contribution types

### Editorial changes

Spelling, examples, explanations, and non-normative guidance may be submitted
directly as a pull request.

### Normative changes

Changes to `SPEC.md`, required fields, status semantics, JSON Schema behavior,
or conformance rules require a design issue using the process in
[`GOVERNANCE.md`](GOVERNANCE.md). The pull request must update all affected
artifacts:

- `SPEC.md`
- `schema/fair.schema.json`
- `template/fair.md`
- at least one valid and one relevant invalid test
- applicable examples
- `README.md` and `CHANGELOG.md`
- migration guidance when compatibility changes

### Domain profiles and examples

Domain profiles should name the community standard, version, persistent
identifier, registry record where available, validation tool, and exact
resources to which it applies. A bare standards label is not evidence of
conformance.

Examples must:

- use the canonical filename `FAIR.md`;
- validate with the current schema and validator;
- include every v0.3 FAIR sub-principle as an evidence object;
- avoid claiming that fictitious URLs resolve or that an external organization
  endorses the example;
- label simulated data and evidence clearly;
- separate FAIR status from Open Definition status.

## Local validation

Install the dependencies and run:

```bash
python -m pip install -r requirements.txt
python tools/validate_fair.py
python -m unittest discover -s tests -v
```

Before submitting, also ensure:

```bash
git diff --check
```

## Pull request expectations

The pull request should explain:

- the problem and affected users;
- whether the change is editorial, backward-compatible, or breaking;
- the authoritative standards or evidence used;
- expected migration impact;
- checks performed;
- unresolved tradeoffs or dissenting views.

Keep commits focused. Do not include generated files without documenting how
they were produced.

## Licensing

Unless explicitly stated otherwise, contributions are submitted under the
repository's Apache-2.0 license. Contributors must have the right to submit all
included text, data, examples, and media.
