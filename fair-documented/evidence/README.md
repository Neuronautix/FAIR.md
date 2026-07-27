# Evidence model

Version 0.3 assessment entries replace bare conclusions with objects containing
`status`, `evidence`, optional RDA `metric_ids`, and a note. Each evidence item
has a resolvable/root-relative `id`, a controlled `type`, and an optional note.

Rules:

- `yes` requires target-specific passing evidence.
- `partial` names the implemented part and the remaining gap.
- `planned` names a concrete action in the roadmap; future versions should also
  require owner and target date.
- `no` records evidence for the missing capability or failed test.
- `n/a` explains why the criterion does not apply.
- A broken, stale, or non-resolving evidence reference invalidates the claim.
- Aggregate posture is derived from resource-level results; it is not a
  certification or a hand-entered score.

Recommended future assessment fields are `target`, `method`, `assessor`,
`assessed_at`, `tool`, `tool_version`, `review_by`, and `remediation`. The RDA
FAIR Data Maturity Model should supply reusable metric identifiers and priorities.

