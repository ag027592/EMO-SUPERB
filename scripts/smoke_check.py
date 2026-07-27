"""Fast, dataset-free integrity checks for EMO-SUPERB."""
from __future__ import annotations

import ast
import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "run_all_dataset_and_fold.sh",
        "emo-superb/config_IEMOCAP.yaml",
        "data/IEMOCAP/Secondary/config.json",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"missing {relative}")

    python_files = [
        path for path in ROOT.rglob("*.py") if ".git" not in path.parts
    ]
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as exc:
            fail(f"invalid Python in {path.relative_to(ROOT)}: {exc}")

    json_files = list((ROOT / "data").rglob("config.json"))
    for path in json_files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        if not isinstance(payload, dict):
            fail(f"expected JSON object in {path.relative_to(ROOT)}")

    label_files = list((ROOT / "data").rglob("labels_consensus_*.csv"))
    if len(label_files) < 10:
        fail(f"too few published partition files: {len(label_files)}")
    for path in label_files:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            if not next(csv.reader(handle), None):
                fail(f"empty CSV: {path.relative_to(ROOT)}")

    print(
        "OK: "
        f"{len(python_files)} Python files, "
        f"{len(json_files)} dataset configs, "
        f"{len(label_files)} partition files"
    )


if __name__ == "__main__":
    main()
