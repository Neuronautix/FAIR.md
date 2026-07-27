# Formal community review request: fair.md v0.3

The fair.md project requests critical review of
[release v0.3.1](https://github.com/Neuronautix/FAIR.md/releases/tag/v0.3.1).
The proposal is a lightweight root `FAIR.md` declaration with evidence-backed
FAIR results, explicit implementation profiles, and a separate Open Definition
posture.

This request does **not** claim endorsement, standardization, certification, or
affiliation with any organization named below.

## Review requested from

- GO FAIR practitioners and FAIR Implementation Profile specialists;
- FAIRsharing curators and standards-registry specialists;
- RDA FAIR Data Maturity Model authors, implementers, and assessment experts;
- the RO-Crate community;
- the ISA Tools and ISA-Tab/ISA-JSON community;
- institutional, disciplinary, and repository research data stewards;
- scientists and software maintainers who would author or consume `FAIR.md`.

## Questions for all reviewers

1. Is the role of `FAIR.md` clear, appropriately narrow, and non-duplicative?
2. Does the specification avoid implying that self-declaration is certification?
3. Are FAIRness, openness, implementation choices, and assessment results
   separated correctly?
4. Are evidence objects sufficiently scoped and machine-actionable?
5. Which required fields are too burdensome, too weak, or missing?
6. Can a restricted-but-FAIR resource be represented honestly?
7. What would prevent adoption by your community or infrastructure?
8. Which statements should be softened, removed, or backed by stronger evidence?

## Community-specific questions

### GO FAIR and FIP reviewers

- Does `profiles` accurately complement a FAIR Implementation Profile without
  pretending to replace one?
- Should FAIR-Enabling Resource identifiers or FIP nanopublication identifiers
  be represented differently?

### FAIRsharing

- Are standard, vocabulary, repository, and policy identifiers modeled in a way
  that can reuse FAIRsharing records reliably?
- What evidence and governance would be required before fair.md could be
  considered for a FAIRsharing record?

### RDA assessment specialists

- Is the use of RDA metric identifiers accurate and sufficiently target-specific?
- Should assessment results adopt the RDA maturity levels directly rather than
  mapping to `yes | partial | planned | no | n/a`?

### RO-Crate

- Is a front-door manifest useful alongside RO-Crate, or does any part duplicate
  or conflict with RO-Crate conventions?
- What is the safest mapping from `FAIR.md` resources, relations, and evidence
  to RO-Crate 1.3?

### ISA Tools

- Does the optional ISA profile correctly represent
  Investigation–Study–Assay scope?
- Which ISA validation result, profile identifier, ontology annotations, and
  provenance links should be mandatory?

### Research data stewards and scientists

- Can a researcher complete the template without specialist intervention?
- Which fields need examples, controlled choices, or automated scaffolding?
- Would the declaration improve review, reuse, or repository deposit workflows?

## How to respond

Reviewers may:

- comment on the public review issue;
- open a focused issue for a substantive design concern;
- submit a pull request with evidence and tests;
- provide a structured review using the issue template in
  `.github/ISSUE_TEMPLATE/standards-review.yml`.

Please identify whether comments are personal expertise or an official
organizational position. Reviews are welcome continuously; the initial v0.3
review round will be summarized after **2026-09-30**.

All feedback will be dispositioned publicly as accepted, accepted with changes,
deferred, or declined with rationale under [`GOVERNANCE.md`](GOVERNANCE.md).
