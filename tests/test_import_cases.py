import copy
import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("import_cases", ROOT / "scripts/import_cases.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def fixture():
    finding = {key: "unknown" for key in MODULE.FINDING_STRINGS}
    finding.update(finding_id="FIND-0001", content_fidelity="uncertain",
                   argument_fidelity="not_assessable", evidence_status="reported",
                   labels=["ASSUMPTION"], uncertainties=["Synthetic test fixture only"])
    case = {key: "unknown" for key in MODULE.CASE_STRINGS}
    case.update(case_id="CASE-0001", proof_family_id="TEST-1", case_kind="reported_failure",
                task_type="statement_translation", input_kind="unknown", source_validity="unknown",
                source_text_status="paraphrase", published_output_status="description_only",
                original_prompt_status="unavailable", reproduction_readiness="needs_artifacts",
                source_text="Synthetic fixture, not research data.", artifact_urls=[], finding=finding)
    return dict(paper_id="faithformbench", paper_title="Synthetic fixture", paper_url="https://example.org",
                paper_version="unknown", collector="test", retrieved_at="2026-10-12",
                coverage_notes="Test only", limitations=[], cases=[case])


class ImportTests(unittest.TestCase):
    def test_valid_fixture(self):
        MODULE.validate_bundle(fixture(), "fixture")

    def test_no_confirmed_archival_findings(self):
        value = fixture()
        value["cases"][0]["finding"]["evidence_status"] = "confirmed"
        with self.assertRaisesRegex(ValueError, "cannot be confirmed"):
            MODULE.validate_bundle(value, "fixture")

    def test_reject_wrong_owner(self):
        value = fixture()
        value["cases"][0]["case_id"] = "CASE-0101"
        with self.assertRaisesRegex(ValueError, "outside assigned range"):
            MODULE.validate_bundle(value, "fixture")

    def test_reject_unknown_label(self):
        value = fixture()
        value["cases"][0]["finding"]["labels"] = ["BAD_PROOF"]
        with self.assertRaisesRegex(ValueError, "unknown label"):
            MODULE.validate_bundle(value, "fixture")

    def test_reject_missing_source_status(self):
        value = fixture()
        del value["cases"][0]["source_text_status"]
        with self.assertRaisesRegex(ValueError, "source_text_status"):
            MODULE.validate_bundle(value, "fixture")

    def setup_root(self, root):
        (root / "registry").mkdir()
        for filename in ["cases.csv", "findings.csv"]:
            with (ROOT / "registry" / filename).open(newline="") as handle:
                fields = next(csv.reader(handle))
            with (root / "registry" / filename).open("w", newline="") as handle:
                csv.writer(handle).writerow(fields)
        path = root / "imports/faithformbench/bundle.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(fixture()))
        return path

    def test_collect_is_read_only_and_import_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.setup_root(root)
            files, papers, cases = MODULE.collect(root)
            self.assertEqual((papers, cases), (1, 1))
            self.assertFalse((root / "cases").exists())
            for relative, text in files.items():
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text)
            again, _, _ = MODULE.collect(root)
            self.assertEqual(files, again)
            self.assertFalse((root / "registry/runs.csv").exists())

    def test_reject_changed_frozen_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.setup_root(root)
            target = root / "cases/CASE-0001/source.md"
            target.parent.mkdir(parents=True)
            target.write_text("Existing different input")
            with self.assertRaisesRegex(ValueError, "Frozen artifact differs"):
                MODULE.collect(root)

    def test_reject_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.setup_root(root)
            data = fixture()
            data["cases"].append(copy.deepcopy(data["cases"][0]))
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "Duplicate ID"):
                MODULE.collect(root)


if __name__ == "__main__":
    unittest.main()
