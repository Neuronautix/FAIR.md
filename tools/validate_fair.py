#!/usr/bin/env python3
"""Validate fair.md files against the fair.md specification.

Checks each file's YAML front matter against schema/fair.schema.json and applies
the conformance rules and non-blocking warnings from SPEC.md Section 6.

Usage:
    python tools/validate_fair.py [FILE ...]

With no arguments, validates this repo's own manifest (FAIR.md) and
examples/*.fair.md. The fill-in template at template/fair.md is intentionally
non-conformant (it contains <PLACEHOLDER> values) and is not validated.

Requires: pyyaml, jsonschema  (pip install pyyaml jsonschema)
Exit status: 0 if all files are conformant, 1 otherwise.
"""

import glob
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover
    sys.exit(f"Missing dependency: {exc}. Run: pip install pyyaml jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "fair.schema.json"
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


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
            status = value.get("status") if isinstance(value, dict) else value
            if status == "no":
                out.append(f"fair_assessment.{principle}.{key} is 'no'")
    r11 = (
        (data.get("fair_assessment") or {})
        .get("reusable", {})
        .get("R1.1_clear_data_usage_license")
    )
    r11_status = r11.get("status") if isinstance(r11, dict) else r11
    declared = [
        value
        for value in (license_block.get("content"), license_block.get("code"))
        if value and value != "unspecified"
    ]
    if r11_status in {"no", "planned"} and declared:
        out.append(
            "R1.1 says the license is absent/planned, but license identifiers are declared"
        )
    return out


def semantic_errors_for(data):
    """Cross-field rules that JSON Schema cannot express clearly."""
    out = []
    version = data.get("fair_md_version")

    reviewed = data.get("last_reviewed")
    if isinstance(reviewed, str):
        try:
            if date.fromisoformat(reviewed) > date.today():
                out.append("last_reviewed must not be in the future")
        except ValueError:
            pass  # JSON Schema reports malformed dates.

    for index, maintainer in enumerate(data.get("maintainers") or []):
        orcid = maintainer.get("orcid")
        if orcid and not valid_orcid(orcid):
            out.append(f"maintainers[{index}].orcid has an invalid checksum")

    resources = data.get("data_resources") or []
    resource_ids = [resource.get("id") for resource in resources if isinstance(resource, dict)]
    duplicates = sorted({resource_id for resource_id in resource_ids if resource_ids.count(resource_id) > 1})
    if duplicates:
        out.append(f"data_resources ids are not unique: {', '.join(duplicates)}")

    if version == "0.3":
        for principle, entries in (data.get("fair_assessment") or {}).items():
            for key, entry in (entries or {}).items():
                if not isinstance(entry, dict):
                    out.append(
                        f"fair_assessment.{principle}.{key}: v0.3 requires "
                        "an object with status and evidence"
                    )
        for index, vocabulary in enumerate(data.get("vocabularies") or []):
            if not isinstance(vocabulary, dict):
                out.append(
                    f"vocabularies[{index}]: v0.3 requires a resolvable "
                    "identified-vocabulary object"
                )

    known_ids = set(resource_ids)
    for index, profile in enumerate(data.get("profiles") or []):
        for resource_id in profile.get("applies_to", []):
            if resource_id not in known_ids:
                out.append(
                    f"profiles[{index}].applies_to references unknown "
                    f"data resource {resource_id!r}"
                )

    openness = data.get("openness") or {}
    if openness.get("status") == "conformant":
        expected = {
            "license_status": "open",
            "access": "open",
            "machine_readable": True,
            "open_format": True,
            "source_available": True,
        }
        mismatches = [
            key for key, expected_value in expected.items()
            if openness.get(key) != expected_value
        ]
        if mismatches:
            out.append(
                "openness.status is 'conformant' but these Open Definition "
                f"conditions are not satisfied: {', '.join(mismatches)}"
            )

    return out


def valid_orcid(value):
    """Return whether an ORCID string passes ISO 7064 MOD 11-2."""
    compact = value.replace("-", "")
    if not re.fullmatch(r"[0-9]{15}[0-9X]", compact):
        return False
    total = 0
    for character in compact[:15]:
        total = (total + int(character)) * 2
    result = (12 - (total % 11)) % 11
    check = "X" if result == 10 else str(result)
    return compact[-1] == check


def exact_local_path_exists(root, reference):
    """Check a root-relative path component-by-component with exact case."""
    current = root
    for part in Path(reference.lstrip("/")).parts:
        if not current.is_dir():
            return False
        matches = [entry for entry in current.iterdir() if entry.name == part]
        if not matches:
            return False
        current = matches[0]
    return current.exists()


def local_reference_errors(data, manifest_path):
    """Validate this repository's own root-relative declarations."""
    path = Path(manifest_path).resolve()
    if path.parent != ROOT or path.name != "FAIR.md":
        return []

    references = []
    for resource in data.get("data_resources") or []:
        references.append(("data_resources.path", resource.get("path")))
        for reference in resource.get("metadata") or []:
            references.append(("data_resources.metadata", reference))
    for key, reference in (data.get("companions") or {}).items():
        references.append((f"companions.{key}", reference))
    for groups in (data.get("fair_assessment") or {}).values():
        for entry in groups.values():
            if isinstance(entry, dict):
                for evidence in entry.get("evidence") or []:
                    references.append(("fair_assessment.evidence", evidence.get("id")))
    for reference in (data.get("openness") or {}).get("evidence") or []:
        references.append(("openness.evidence", reference))

    errors = []
    for location, reference in references:
        if isinstance(reference, str) and reference.startswith("/"):
            if not exact_local_path_exists(ROOT, reference):
                errors.append(
                    f"{location}: local reference does not exist with exact case: "
                    f"{reference}"
                )
    return errors


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
        data = yaml.load(yaml_text, Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        return [f"YAML front matter does not parse: {exc}"], []

    if not isinstance(data, dict):
        return ["YAML front matter is not a mapping"], []

    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in err.path) or "(root)"
        errors.append(f"{location}: {err.message}")

    errors.extend(semantic_errors_for(data))
    errors.extend(local_reference_errors(data, path))

    if not prose.strip():
        errors.append("prose section is present but empty")

    warnings = warnings_for(data)
    return errors, warnings


def main(argv):
    default_paths = [str(ROOT / "FAIR.md")] + sorted(
        glob.glob(str(ROOT / "examples" / "*.fair.md"))
    )
    paths = argv or default_paths
    if not paths:
        print("No fair.md files to validate.")
        return 0

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

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
