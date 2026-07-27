# Optional ISA-Tab profile

ISA is a domain profile for experimental life-science and related research
objects. It is not a universal requirement for `fair.md`.

## Required model

```text
Investigation
└── one or more Studies
    └── one or more Assays
```

An ISA-enabled resource should declare:

- an Investigation identifier, title, description, submission/public-release
  dates, publications, and contacts;
- Study identifiers, design type, factors, protocols, source/sample
  characteristics, and sample provenance;
- Assay measurement type, technology type, platform, protocols, and links from
  samples through processes to raw and derived data;
- ontology annotations with term accession/URI and ontology source name, URI,
  and version;
- actual ISA-Tab or ISA-JSON files and an ISA validation result.

The Study and Assay process graphs should be directed and acyclic, with stable
node identifiers. Process nodes should record protocols, parameters, performer,
and date. Data nodes should resolve to actual files.

## `fair.md` declaration pattern

Declare the ISA specification under `profiles` with `status: adopted` only when
the package validates. `applies_to` must list the resource IDs that use ISA.
Reference the specification by URI and, when available, a FAIRsharing record.
Do not place the bare string `ISA-Tab` in `vocabularies` and treat that as
conformance.

The source of truth for this profile is the
[ISA Model and Serialization Specifications](https://isa-specs.readthedocs.io/en/latest/).

