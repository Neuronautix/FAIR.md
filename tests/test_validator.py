"""Behavioral tests for the fair.md schema and validator."""

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "validate_fair", ROOT / "tools" / "validate_fair.py"
)
validate_fair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_fair)


class ValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads(
            (ROOT / "schema" / "fair.schema.json").read_text(encoding="utf-8")
        )
        Draft202012Validator.check_schema(schema)
        cls.validator = Draft202012Validator(
            schema, format_checker=FormatChecker()
        )
        text = (ROOT / "FAIR.md").read_text(encoding="utf-8")
        yaml_text, _ = validate_fair.split_front_matter(text)
        cls.valid_v03 = validate_fair.yaml.load(
            yaml_text, Loader=validate_fair.UniqueKeyLoader
        )

    def schema_errors(self, data):
        return list(self.validator.iter_errors(data))

    def test_repository_manifest_is_valid(self):
        errors, _ = validate_fair.validate_file(ROOT / "FAIR.md", self.validator)
        self.assertEqual([], errors)

    def test_complete_v03_examples_are_valid(self):
        examples = sorted((ROOT / "examples").glob("*/FAIR.md"))
        self.assertGreaterEqual(len(examples), 2)
        for example in examples:
            with self.subTest(example=example):
                errors, _ = validate_fair.validate_file(example, self.validator)
                self.assertEqual([], errors)

    def test_real_calendar_date_is_enforced(self):
        data = copy.deepcopy(self.valid_v03)
        data["last_reviewed"] = "2026-99-99"
        self.assertTrue(self.schema_errors(data))

    def test_uri_format_is_enforced(self):
        data = copy.deepcopy(self.valid_v03)
        data["identifiers"]["canonical"] = "not a URI"
        self.assertTrue(self.schema_errors(data))

    def test_malformed_doi_is_rejected(self):
        data = copy.deepcopy(self.valid_v03)
        data["identifiers"]["doi"] = "not-a-doi"
        self.assertTrue(self.schema_errors(data))

    def test_orcid_checksum_is_enforced(self):
        data = copy.deepcopy(self.valid_v03)
        data["maintainers"][0]["orcid"] = "0000-0003-4820-7952"
        errors = validate_fair.semantic_errors_for(data)
        self.assertTrue(any("invalid checksum" in error for error in errors))

    def test_duplicate_yaml_key_fails(self):
        text = """---
fair_md_version: "0.2"
title: first
title: second
---
prose
"""
        with tempfile.NamedTemporaryFile(
            "w", suffix=".md", encoding="utf-8", delete=False
        ) as handle:
            handle.write(text)
            path = Path(handle.name)
        try:
            errors, _ = validate_fair.validate_file(path, self.validator)
            self.assertTrue(any("duplicate key" in error for error in errors))
        finally:
            path.unlink()

    def test_v03_rejects_scalar_assessment(self):
        data = copy.deepcopy(self.valid_v03)
        data["fair_assessment"]["findable"][
            "F1_globally_unique_persistent_id"
        ] = "yes"
        self.assertTrue(self.schema_errors(data))
        self.assertTrue(validate_fair.semantic_errors_for(data))

    def test_v03_requires_identified_vocabularies(self):
        data = copy.deepcopy(self.valid_v03)
        data["vocabularies"][0] = "FAIR"
        self.assertTrue(self.schema_errors(data))

    def test_unknown_profile_resource_fails_semantic_check(self):
        data = copy.deepcopy(self.valid_v03)
        data["profiles"][0]["applies_to"].append("missing-resource")
        errors = validate_fair.semantic_errors_for(data)
        self.assertTrue(any("unknown data resource" in error for error in errors))

    def test_conformant_openness_must_satisfy_all_conditions(self):
        data = copy.deepcopy(self.valid_v03)
        data["openness"]["status"] = "conformant"
        data["openness"]["license_status"] = "restricted"
        errors = validate_fair.semantic_errors_for(data)
        self.assertTrue(any("Open Definition conditions" in error for error in errors))

    def test_custom_companion_value_must_be_a_reference(self):
        data = copy.deepcopy(self.valid_v03)
        data["companions"]["x_evidence"] = 42
        self.assertTrue(self.schema_errors(data))

    def test_duplicate_resource_ids_fail_semantic_check(self):
        data = copy.deepcopy(self.valid_v03)
        data["data_resources"].append(copy.deepcopy(data["data_resources"][0]))
        errors = validate_fair.semantic_errors_for(data)
        self.assertTrue(any("not unique" in error for error in errors))

    def test_missing_local_reference_fails_for_repository_manifest(self):
        data = copy.deepcopy(self.valid_v03)
        data["companions"]["x_missing"] = "/DOES-NOT-EXIST"
        errors = validate_fair.local_reference_errors(data, ROOT / "FAIR.md")
        self.assertTrue(any("does not exist with exact case" in error for error in errors))

    def test_missing_local_reference_fails_for_complete_example(self):
        example = ROOT / "examples" / "generic-dataset" / "FAIR.md"
        text = example.read_text(encoding="utf-8")
        yaml_text, _ = validate_fair.split_front_matter(text)
        data = validate_fair.yaml.load(
            yaml_text, Loader=validate_fair.UniqueKeyLoader
        )
        data["companions"]["x_missing"] = "/examples/DOES-NOT-EXIST"
        errors = validate_fair.local_reference_errors(data, example)
        self.assertTrue(any("does not exist with exact case" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
