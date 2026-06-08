---
# fair.md — a portable, human- and machine-readable FAIR manifest for a repository
# Proposed convention (v0.2). Reference implementation: https://neuronautix.com/fair.md
# Lineage: llms.txt (root markdown for machines) + codemeta.json / CITATION.cff
# (machine-readable metadata) + RO-Crate / FAIR Signposting (FAIR Digital Objects).
# fair.md does NOT replace those — it is a single human-first front door that
# self-declares HOW FAIR a repository's data/knowledge is and WHERE the deeper
# machine-readable affordances live.

fair_md_version: "0.2"
title: "Neuronautix Knowledge Base"
description: >
  Scientific knowledge artifacts on Home-Cage Monitoring, FAIR metadata,
  behavioral neuroscience, AI agents in research, and New Approach
  Methodologies (NAMs) — published as a static website and git repository.
identifiers:
  repository: "https://github.com/Neuronautix/neuronautix.com"
  homepage: "https://neuronautix.com"
  canonical: "https://neuronautix.com/fair.md"
  doi: null            # not yet minted — recommend archiving releases to Zenodo for a DOI
maintainers:
  - name: "Damien Huzard, PhD"
    role: "author, curator, accountable maintainer"
    orcid: "0000-0003-4820-7951"
    org: "Neuronautix — Montpellier, France"
license:
  # Licensed Apache-2.0 (matching the DESIGN.md format this repo follows).
  content: "Apache-2.0"
  code: "Apache-2.0"

# ── What "data" this manifest covers (the FAIR objects) ──
data_resources:
  - id: "knowledge-base"
    path: "/knowledge/"
    type: "structured Markdown knowledge articles (LLM wiki), source-backed"
    topics: ["HCM systems", "behavioral analysis", "FAIR metadata", "AI agents in science", "NAMs & regulatory"]
  - id: "notes"
    path: "/notes/"
    type: "cited analytical essays with inline epistemic markup (see /trust.md)"
    count: 19
  - id: "presentations"
    path: "/presentations/"
    type: "self-contained HTML slide decks with source maps (sources.yaml) and metadata.json"

# ── Vocabularies / standards referenced (Interoperability) ──
vocabularies:
  - "FAIR Guiding Principles (Wilkinson et al., 2016)"
  - "schema.org (web metadata, JSON-LD)"
  - "NAMO — New Approach Methodology Ontology (Monarch Initiative)"
  - "RO-Crate, BioCompute Object (IEEE 2791), W3C PROV (referenced in content)"

# ── FAIR self-assessment ──
# status enum: yes | partial | planned | no | n/a
# This is a transparent SELF-assessment, not a certified audit. It is meant to
# be honest about gaps, and machine-checkable by FAIR assessment tools.
fair_assessment:
  findable:
    F1_globally_unique_persistent_id: "partial"   # canonical HTTPS URLs per page; no DOIs yet
    F2_rich_metadata: "yes"                        # per-page <meta>, OpenGraph, Twitter cards
    F3_metadata_references_data_id: "yes"          # canonical links in every document
    F4_indexed_searchable: "yes"                   # sitemap.xml + robots.txt
  accessible:
    A1_retrievable_by_id_open_protocol: "yes"      # HTTPS, no authentication
    A1.1_protocol_open_free: "yes"
    A1.2_auth_where_needed: "n/a"                  # all content is public
    A2_metadata_persist_beyond_data: "partial"     # git history; no formal tombstoning
  interoperable:
    I1_formal_accessible_knowledge_representation: "partial"  # HTML now; JSON-LD planned
    I2_FAIR_vocabularies: "partial"                # vocabularies referenced, not yet embedded
    I3_qualified_references: "yes"                  # inline [n] citations + References lists
  reusable:
    R1_plurality_of_attributes: "yes"
    R1.1_clear_data_usage_license: "planned"       # license not yet declared (see license:)
    R1.2_detailed_provenance: "yes"                # see /trust.md (authorship, AI oversight, sources)
    R1.3_domain_community_standards: "partial"     # citation practice; ARRIVE/MNMS discussed in content

# ── Companion machine-readable artifacts (present or recommended) ──
companions:
  trust: "/trust.md"                       # epistemic provenance & confidence (present)
  sitemap: "/sitemap.xml"                  # present
  robots: "/robots.txt"                    # present
  citation_cff: "/CITATION.cff"            # recommended (machine-readable citation)
  codemeta: "/codemeta.json"               # recommended (software metadata)
  ro_crate: "/ro-crate-metadata.json"      # recommended (FAIR Digital Object packaging)

maturity: "prototype"
last_reviewed: "2026-06-08"
---

# fair.md — Neuronautix Knowledge Base

This file is a **FAIR manifest**: a single, human-readable and machine-parseable
declaration of how *Findable, Accessible, Interoperable, and Reusable* the data
and knowledge in this repository are, and where the deeper machine-readable
affordances live. The YAML block above is the machine-readable part; this prose
is for people.

It is a **proposed convention (v0.2)**, not yet a standard. This repository is
its reference implementation. See *How to adopt fair.md* below.

## Why fair.md?

The FAIR principles are widely endorsed but unevenly practiced, and there is no
lightweight, conventional place for a project to *state its own FAIR posture* in
a way both a human and a crawler can read in five seconds. We already have:

- **`llms.txt`** — a root Markdown file that tells language models how to use a
  site. fair.md borrows its "one well-known root file, Markdown, human-first"
  ergonomics.
- **`codemeta.json` / `CITATION.cff`** — rich, machine-readable metadata for
  software and citation. These are excellent but verbose and rarely read by
  humans.
- **RO-Crate / FAIR Signposting / FAIR Digital Objects** — robust packaging and
  navigation for FAIR objects, aimed at repositories and infrastructure.

fair.md sits *in front of* these: a front door that (1) says plainly what data a
repo holds, (2) gives an honest, structured **FAIR self-assessment** with a
`yes | partial | planned | no | n/a` status per sub-principle, and (3) points to the
heavier machine-readable companions. It is meant to be cheap to write, honest
about gaps, and trivially adoptable on any GitHub Pages / static site.

## What this repository declares

This repo is a **knowledge base**, not a dataset in the classical sense: its FAIR
objects are *knowledge artifacts* — a source-backed Markdown wiki (`/knowledge/`),
19 cited analytical notes (`/notes/`), and HTML presentations with source maps
(`/presentations/`). The self-assessment above reflects that honestly: discovery
and accessibility are strong (canonical URLs, sitemap, rich meta tags, open
HTTPS); the current gaps are an undeclared license (Reusability) and
not-yet-embedded machine-readable vocabularies / JSON-LD (Interoperability).

The companion **[`/trust.md`](/trust.md)** carries the *provenance and confidence*
half of Reusability (R1.2): who and what produced each claim, and how trustworthy
it is.

## Format specification (v0.2)

A `fair.md` file is Markdown with a YAML front-matter block. Required keys:

| Key | Meaning |
|---|---|
| `fair_md_version` | spec version string |
| `title`, `description` | what the repository is |
| `identifiers` | repository, homepage, canonical URL of this file; `doi` if minted |
| `maintainers` | accountable people, with ORCID where available |
| `license` | content and code license (may be `unspecified` — but say so) |
| `data_resources` | the FAIR objects: `id`, `path`, `type`, optional `topics`/`count` |
| `vocabularies` | controlled vocabularies / standards used |
| `fair_assessment` | self-assessment, grouped `findable`/`accessible`/`interoperable`/`reusable`, each sub-key a status enum `yes \| partial \| planned \| no \| n/a` |
| `companions` | paths to `trust.md`, `sitemap.xml`, and recommended `CITATION.cff` / `codemeta.json` / `ro-crate-metadata.json` |
| `maturity` | `prototype \| beta \| stable` |
| `last_reviewed` | ISO date of last honest review |

The sub-principle keys (`F1…`, `A1…`, `I1…`, `R1…`) follow the canonical FAIR
principles so that automated FAIR assessment tools can map them directly.

## How to adopt fair.md in your repository

1. Copy this file to the root of your repo / site as `fair.md`.
2. Replace the YAML with your project's values. **Be honest in
   `fair_assessment`** — `partial` and `planned` are features, not failures;
   the point is a truthful, improvable baseline.
3. Serve it at `https://yourdomain/fair.md` (and optionally redirect
   `/.well-known/fair.md` → `/fair.md`).
4. Add the companions you can (`CITATION.cff` is the cheapest high-value next
   step; `codemeta.json` for software; RO-Crate for packaged objects).
5. Pair it with a **[`trust.md`](/trust.md)** if your repo publishes knowledge,
   analysis, or AI-assisted content whose *confidence* matters, not just its
   findability.

## Changelog

- **v0.1 (2026-06-06)** — first draft of the fair.md convention and this
  reference implementation.
