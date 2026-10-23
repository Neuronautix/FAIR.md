# AGENTS.md — FAIR.md convention

## Role and maturity
This is an independently versioned **proposed human- and machine-readable FAIR manifest convention**, not a FAIR certification authority, repository-hosted assessment service or substitute for RO-Crate/DataCite. The authoritative format is `SPEC.md` (v0.3); `schema/fair.schema.json`, `template/fair.md`, examples and validator must remain consistent.

## Rules for agents
- Separate facts about available resources, declared implementation choices, evidence supporting a local assessment, and *unknown* or not-assessed statements.
- Do not infer that a project is FAIR, open, scientifically reusable or legally redistributable merely because its manifest validates.
- Do not upgrade self-assessment to independent verification or generate fake DOIs/ORCIDs/links. If a resource is restricted or offline, preserve that status.
- Never rewrite users' manifest contents or issue an external public release without explicit review.
- Version any schema or normative terminology change and provide valid/invalid fixtures plus migration notes. Do not present the experimental `/.well-known/FAIR.md` redirect as an IANA-registered convention.
- This repository and `Neuronautix/TRUST.md` are separate conventions: one declares data/resource FAIR posture; the other records attributable, contextual evidence assessments. Neither owns the other's scientific semantics.

## Development and checks
Read `README.md`, `SPEC.md`, `schema/fair.schema.json`, `tests/`, `tools/validate_fair.py` and `CHANGELOG.md`.
```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/validate_fair.py
```
Before a PR, verify the exact version of fixtures and explain any changed validation behavior. A passed check proves structural compatibility only.
