# Standards crosswalk

The crosswalk is guidance, not a claim that one field fully satisfies a FAIR
principle. A valid value shows that metadata is structurally present; an
evidence-backed assessment determines whether the implementation works.

| `fair.md` concept | FAIR / RDA concern | Companion standard | Required evidence |
|---|---|---|---|
| `identifiers.canonical` | F1 metadata identifier | DataCite, Handle/DOI | Resolvable, persistent metadata-record PID |
| `data_resources[].identifier` | F1 data identifier | DataCite, domain PID scheme | Resolvable identifier for each described object |
| `data_resources[].metadata` | F2/F3 rich metadata and data link | DCAT 3, DataCite, RO-Crate | Metadata explicitly names the object PID |
| Resource discovery | F4 indexing | Repository/catalog, FAIR Data Point | Public catalog record or harvesting result |
| Access URL and protocol | A1/A1.1/A1.2 | HTTP, FAIR Signposting | Successful retrieval; auth policy when required |
| Preservation declaration | A2 | Repository preservation policy | Tombstone/retention policy and persistent metadata |
| Structured `vocabularies` | I1/I2 | RDF/JSON-LD, FAIRsharing | Resolvable vocabulary IRI, version, registry record |
| Qualified relations | I3 | DCAT 3, PROV-O, Schema.org | Predicate URI plus target URI |
| Resource metadata | R1 | DataCite, DCAT 3, RO-Crate | Accurate target-specific attributes |
| Per-resource license | R1.1 | SPDX/license URI | License text/URI, scope, rights holder, exceptions |
| Provenance companion | R1.2 | W3C PROV-O, RO-Crate | Source, activity, agent, time, and generated output |
| `profiles` | R1.3 | GO FAIR FIP, FAIRsharing | Community-selected standard/profile and conformance result |
| `openness` | Separate from FAIR | Open Definition 2.1 | License, whole-work access, machine readability, open format |
| ISA profile | Domain-specific R1.3 | ISA-Tab / ISA-JSON | Valid Investigation–Study–Assay package and ontology terms |

## Important distinctions

- A repository URL is not automatically a persistent identifier.
- A name such as `ISA-Tab` or `schema.org` is not a machine-actionable vocabulary
  declaration; use its resolvable identifier and version.
- Public GitHub visibility is not equivalent to registration in a searchable
  research metadata catalog.
- `CITATION.cff` improves software citation but does not replace resource,
  distribution, access, provenance, or preservation metadata.
- Apache-2.0 is appropriate for software. Documentation, data, database rights,
  and third-party content may need separate licenses and scopes.
- `/.well-known/FAIR.md` is not currently in the IANA registry; it must not be a
  normative discovery requirement unless registered under RFC 8615.
