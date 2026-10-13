#!/usr/bin/env python3
"""Validate archival bundles and deterministically materialize case packets."""

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path


RANGES = {"faithformbench": (1, 99), "proofflow": (101, 199),
          "lost-in-translation": (201, 299), "pistis": (301, 399)}
LABELS = {"ASSUMPTION", "CONCLUSION", "BINDING", "INTERPRETATION",
          "DEPENDENCY", "STRATEGY", "SILENT_REPAIR"}
FIDELITY = {"preserved", "violated", "uncertain", "not_assessable"}
CASE_ENUMS = {
    "case_kind": {"reported_failure", "candidate_failure", "source_defect", "comparison_nonfailure", "theoretical_example"},
    "task_type": {"statement_translation", "proof_translation", "source_proof_checking"},
    "input_kind": {"original", "perturbed", "unknown"},
    "source_validity": {"valid", "invalid", "ambiguous", "unknown"},
    "source_text_status": {"exact_transcription", "partial_transcription", "paraphrase", "unavailable"},
    "published_output_status": {"full", "excerpt", "description_only", "unavailable"},
    "original_prompt_status": {"exact", "partial", "unavailable"},
    "reproduction_readiness": {"ready_for_protocol", "needs_artifacts", "needs_context", "archival_only"},
}
CASE_STRINGS = set(CASE_ENUMS) | {
    "case_id", "proof_family_id", "source_locator", "topic", "source_validity_basis",
    "source_text", "published_output", "license_notes", "original_prompt",
    "reported_model", "reported_environment", "reported_outcome", "notes",
}
FINDING_STRINGS = {
    "finding_id", "content_fidelity", "argument_fidelity", "evidence_status",
    "observed_mismatch", "consequence", "source_span", "lean_location",
    "first_observed_divergence", "evidence", "causal_hypothesis",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def strings(obj, fields, context):
    for field in fields:
        require(isinstance(obj.get(field), str) and obj[field].strip(),
                f"{context}: {field} must be a nonempty string")


def string_list(value, context):
    require(isinstance(value, list) and all(isinstance(x, str) for x in value),
            f"{context}: expected an array of strings")


def validate_bundle(bundle, location):
    strings(bundle, {"paper_id", "paper_title", "paper_url", "paper_version", "collector",
                     "retrieved_at", "coverage_notes"}, location)
    paper = bundle["paper_id"]
    require(paper in RANGES, f"{location}: unknown paper_id")
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", bundle["retrieved_at"]), f"{location}: invalid date")
    string_list(bundle.get("limitations"), f"{location}: limitations")
    require(isinstance(bundle.get("cases"), list), f"{location}: cases must be an array")
    for case in bundle["cases"]:
        strings(case, CASE_STRINGS, location)
        cid = case["case_id"]
        require(re.fullmatch(r"CASE-\d{4}", cid), f"{location}: invalid case ID")
        low, high = RANGES[paper]
        require(low <= int(cid[5:]) <= high, f"{cid}: outside assigned range")
        for field, allowed in CASE_ENUMS.items():
            require(case[field] in allowed, f"{cid}: invalid {field}")
        string_list(case.get("artifact_urls"), f"{cid}: artifact_urls")
        finding = case.get("finding")
        require(isinstance(finding, dict), f"{cid}: missing finding")
        strings(finding, FINDING_STRINGS, cid)
        require(re.fullmatch(r"FIND-\d{4}", finding["finding_id"]), f"{cid}: invalid finding ID")
        require(low <= int(finding["finding_id"][5:]) <= high, f"{cid}: finding outside range")
        string_list(finding.get("labels"), f"{cid}: labels")
        string_list(finding.get("uncertainties"), f"{cid}: uncertainties")
        require(set(finding["labels"]) <= LABELS, f"{cid}: unknown label")
        require(finding["content_fidelity"] in FIDELITY and finding["argument_fidelity"] in FIDELITY,
                f"{cid}: invalid fidelity status")
        require(finding["evidence_status"] in {"reported", "candidate", "disputed"},
                f"{cid}: archival findings cannot be confirmed")


def packet(bundle, case):
    cid = case["case_id"]
    base = f"cases/{cid}"
    source = (f"# {cid}: Source Packet\n\n"
              f"Paper: [{bundle['paper_title']}]({bundle['paper_url']})\n\n"
              f"Version: {bundle['paper_version']}\n\nLocator: {case['source_locator']}\n\n"
              f"Input kind: {case['input_kind']}\n\nTranscription status: {case['source_text_status']}\n\n"
              "## Supplied Mathematical Material\n\n" + case["source_text"] + "\n")
    output = (f"# {cid}: Published Output\n\nStatus: {case['published_output_status']}\n\n"
              "This is archival evidence, not code generated or verified by this study.\n\n"
              + case["published_output"] + "\n")
    f = case["finding"]
    assessment = f"# {cid}: Provisional Assessment\n\nEvaluator-only material.\n\n"
    for label, value in [
        ("Case kind", case["case_kind"]), ("Source validity", case["source_validity"]),
        ("Validity basis", case["source_validity_basis"]), ("Content fidelity", f["content_fidelity"]),
        ("Argument fidelity", f["argument_fidelity"]), ("Evidence status", f["evidence_status"]),
        ("Readiness", case["reproduction_readiness"]), ("Reported model", case["reported_model"]),
        ("Reported environment", case["reported_environment"]), ("Reported outcome", case["reported_outcome"]),
        ("Original prompt status", case["original_prompt_status"]), ("Original prompt", case["original_prompt"]),
        ("Licensing", case["license_notes"]), ("Notes", case["notes"]),
    ]:
        assessment += f"## {label}\n\n{value}\n\n"
    assessment += "## Primary Artifacts\n\n" + "\n".join(f"- {url}" for url in case["artifact_urls"]) + "\n"
    finding_path = f"findings/{f['finding_id']}.md"
    finding_text = (f"# {f['finding_id']}: {cid}\n\n"
                    f"Collector: {bundle['collector']}\n\nStatus: {f['evidence_status']}\n\n"
                    f"Labels: {', '.join(f['labels']) or 'none'}\n\n")
    for key in ["observed_mismatch", "consequence", "source_span", "lean_location",
                "first_observed_divergence", "evidence", "causal_hypothesis"]:
        finding_text += f"## {key.replace('_', ' ').title()}\n\n{f[key]}\n\n"
    finding_text += "## Uncertainties\n\n" + "\n".join(f"- {x}" for x in f["uncertainties"]) + "\n"
    files = {f"{base}/source.md": source, f"{base}/published_output.md": output,
             f"{base}/assessment.md": assessment, finding_path: finding_text}
    row = dict(case_id=cid, proof_family_id=case["proof_family_id"], parent_case_id="",
               source_title=bundle["paper_title"], source_url=bundle["paper_url"],
               source_version=bundle["paper_version"], source_locator=case["source_locator"],
               source_packet_path=f"{base}/source.md", source_sha256=hashlib.sha256(source.encode()).hexdigest(),
               topic=case["topic"], task_type=case["task_type"], source_validity=case["source_validity"],
               validity_evidence_path=f"{base}/assessment.md", input_kind=case["input_kind"],
               selection_method="curated_artifact" if case["case_kind"] == "candidate_failure" else "curated_reported", sampling_seed="", split="development",
               assessment_path=f"{base}/assessment.md", status="archived_" + case["case_kind"],
               notes=f"{case['reproduction_readiness']}; source={case['source_text_status']}; not reproduced")
    dimensions = [name for name in ["content", "argument"] if f[name + "_fidelity"] == "violated"]
    finding_row = dict(finding_id=f["finding_id"], case_id=cid, run_id="", labels=";".join(f["labels"]),
                       fidelity_dimension=";".join(dimensions) or "not_established", source_span=f["source_span"],
                       lean_location=f["lean_location"], first_observed_divergence=f["first_observed_divergence"],
                       observed_mismatch=f["observed_mismatch"], consequence=f["consequence"], evidence_path=finding_path,
                       evidence_status=f["evidence_status"], reviewer="pending", reviewed_at_utc="",
                       causal_hypothesis=f["causal_hypothesis"], causal_evidence_path="",
                       notes=f"Collector: {bundle['collector']}; no independent Lean verification")
    return files, row, finding_row


def merge_csv(path, additions, key):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        require(fields is not None and key in fields, f"{path}: missing header")
        rows = {}
        for row in reader:
            require(None not in row and None not in row.values(), f"{path}: malformed row")
            require(row[key] not in rows, f"{path}: duplicate ID {row[key]}")
            rows[row[key]] = row
    for row in additions:
        require(set(row) == set(fields), f"{path}: registry fields do not match")
        require(row[key] not in rows or rows[row[key]] == row, f"{path}: conflicting existing ID {row[key]}")
        rows[row[key]] = row
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows[k] for k in sorted(rows))
    return out.getvalue()


def collect(root):
    files, rows, findings, seen = {}, [], [], set()
    index = ["# Archival Case Index", "", "Curated published cases; not a frequency sample. No new experiments or independent Lean checks.", "",
             "| Case | Paper | Kind | Evidence | Labels | Readiness | Input status |", "| --- | --- | --- | --- | --- | --- | --- |"]
    bundles = sorted((root / "imports").glob("*/bundle.json"))
    require(bundles, "No import bundles found")
    for path in bundles:
        bundle = json.loads(path.read_text(encoding="utf-8"))
        validate_bundle(bundle, str(path))
        require(path.parent.name == bundle["paper_id"], f"{path}: directory/paper mismatch")
        for case in bundle["cases"]:
            for identifier in [case["case_id"], case["finding"]["finding_id"]]:
                require(identifier not in seen, f"Duplicate ID: {identifier}")
                seen.add(identifier)
            generated, row, finding = packet(bundle, case)
            files.update(generated)
            rows.append(row)
            findings.append(finding)
            index.append(f"| [{case['case_id']}](../cases/{case['case_id']}/assessment.md) | {bundle['paper_id']} | {case['case_kind']} | {case['finding']['evidence_status']} | {'; '.join(case['finding']['labels']) or 'none'} | {case['reproduction_readiness']} | {case['source_text_status']} |")
    # Check every packet before writing anything; importing cannot silently replace a frozen artifact.
    for relative, content in files.items():
        path = root / relative
        require(not path.exists() or path.read_text(encoding="utf-8") == content,
                f"Frozen artifact differs: {relative}; create a new variant or adjudicate explicitly")
    files["registry/cases.csv"] = merge_csv(root / "registry/cases.csv", rows, "case_id")
    files["registry/findings.csv"] = merge_csv(root / "registry/findings.csv", findings, "finding_id")
    files["reports/CASE_INDEX.md"] = "\n".join(index) + "\n"
    return files, len(bundles), len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        files, papers, cases = collect(args.root.resolve())
        if args.write:
            for relative, content in files.items():
                target = args.root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
        print(f"{'Imported' if args.write else 'Validated'} {cases} cases from {papers} paper bundles; no experiments executed.")
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Import rejected: {error}\n")


if __name__ == "__main__":
    main()
