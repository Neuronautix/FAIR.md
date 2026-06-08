#!/usr/bin/env python3
"""Validate fair.md files against the fair.md specification v0.1.

Checks each file's YAML front matter against schema/fair.schema.json and applies
the conformance rules and non-blocking warnings from SPEC.md Section 6.

Usage:
    python tools/validate_fair.py [FILE ...]

With no arguments, validates examples/*.fair.md. The root FAIR.md is the blank
template (it intentionally contains <PLACEHOLDER> values) and is not validated.

Requires: pyyaml, jsonschema  (pip install pyyaml jsonschema)
Exit status: 0 if all files are conformant, 1 otherwise.
"""

import glob
import json
import re
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    sys.exit(f"Missing dependency: {exc}. Run: pip install pyyaml jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "fair.schema.json"
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)


def split_front_matter(text):
    """Return (yaml_text, prose) or raise ValueError if no front matter block."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError("no YAML front-matter block delimited by '---' at the top of the file")
    return match.group(1), match.group(2)


def warnings_for(data):
    """Non-blocking warnings from SPEC.md Section 6."""
    out = []
    license_block = data.get("license") or {}
    for key in ("content", "code"):
        if license_block.get(key) == "unspecified":
            out.append(f"license.{key} is 'unspecified'")
    for i, m in enumerate(data.get("maintainers") or []):
        if not m.get("orcid"):
            out.append(f"maintainers[{i}] ({m.get('name', '?')}) has no ORCID")
    if (data.get("identifiers") or {}).get("doi") is None:
        out.append("identifiers.doi is null (no DOI minted)")
    for principle, subs in (data.get("fair_assessment") or {}).items():
        for key, value in (subs or {}).items():
            if value == "no":
                out.append(f"fair_assessment.{principle}.{key} is 'no'")
    return out


def validate_file(path, validator):
    """Return (errors, warnings) for one fair.md file."""
    errors, warnings = [], []
    try:
        text = Path(path).read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["file is not valid UTF-8"], []
    except OSError as exc:
        return [f"cannot read file: {exc}"], []

    try:
        yaml_text, prose = split_front_matter(text)
    except ValueError as exc:
        return [str(exc)], []

    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as exc:
        return [f"YAML front matter does not parse: {exc}"], []

    if not isinstance(data, dict):
        return ["YAML front matter is not a mapping"], []

    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in err.path) or "(root)"
        errors.append(f"{location}: {err.message}")

    if not prose.strip():
        errors.append("prose section is present but empty")

    warnings = warnings_for(data)
    return errors, warnings


def main(argv):
    paths = argv or sorted(glob.glob(str(ROOT / "examples" / "*.fair.md")))
    if not paths:
        print("No fair.md files to validate.")
        return 0

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    failed = False
    for path in paths:
        errors, warnings = validate_file(path, validator)
        rel = Path(path).resolve()
        try:
            rel = rel.relative_to(ROOT)
        except ValueError:
            pass
        if errors:
            failed = True
            print(f"FAIL  {rel}")
            for e in errors:
                print(f"  error:   {e}")
        else:
            print(f"PASS  {rel}")
        for w in warnings:
            print(f"  warning: {w}")

    print()
    print("Conformant." if not failed else "Validation failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
