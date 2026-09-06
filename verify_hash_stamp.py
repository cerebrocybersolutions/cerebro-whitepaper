#!/usr/bin/env python3
"""Assert a white-paper review-notes hash block matches the live artifact bytes.

Built 2026-08-15 after the stamp drifted TWICE in one arc: the re-check brief
pinned a full-DOCX sha that existed at no commit, and the review-notes block sat
three commits stale. Both were caught by an adversarial reviewer, not by us. A
prose "restamp in the same change" rule is a checker by intention; this is the
mechanism.

The stamp block names artifacts by their REAL filename, resolved against the
notes file's own directory:

    - cerebro-white-paper-v2.2.docx: `<64 hex>`

ponytail: filenames are literal on purpose. The first cut inferred them from
role labels ("full.docx"/"exec.docx") and the artifact directory holds twelve
docx/pdf files across four paper versions, so every lookup went ambiguous and
red — a false red that would have masked real drift.

    python3 verify_hash_stamp.py <review-notes.md>     # exit 0 clean, 1 drift
    python3 verify_hash_stamp.py --self-test
"""
import hashlib
import re
import sys
from pathlib import Path

STAMP = re.compile(r"^\s*-\s*`?(?P<name>[\w.-]+\.(?:docx|pdf))`?\s*:\s*`(?P<sha>[0-9a-f]{64})`", re.M)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(notes: Path) -> list[str]:
    stamps = list(STAMP.finditer(notes.read_text()))
    if not stamps:
        return [f"no hash stamps found in {notes.name} — block missing or reformatted"]
    bad = []
    for m in stamps:
        name, want = m["name"], m["sha"]
        f = notes.parent / name
        if not f.is_file():
            bad.append(f"{name}: stamped but not present beside {notes.name}")
        elif (got := sha256(f)) != want:
            bad.append(f"{name}: stamped {want[:12]}… but bytes are {got[:12]}…")
    return bad


def self_test() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        doc = d / "paper.docx"
        doc.write_bytes(b"hello")
        notes = d / "notes.md"
        notes.write_text(f"- paper.docx: `{sha256(doc)}`\n")
        assert check(notes) == [], "clean stamp must pass"
        doc.write_bytes(b"tampered")
        assert check(notes), "drifted stamp must FAIL"  # the case that shipped twice
        doc.unlink()
        assert check(notes), "missing artifact must FAIL"
        notes.write_text("no stamps here\n")
        assert check(notes), "missing block must FAIL, not silently pass"
    print("self-test ok (clean pass / drift fail / missing-artifact fail / missing-block fail)")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
        raise SystemExit(0)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    notes = Path(sys.argv[1])
    if not notes.is_file():
        # ponytail: the arg is cwd-relative, but the test runner's --only mode does not
        # apply a suite's cwd. Fall back to script-relative so the check cannot pass or
        # fail for a reason as uninteresting as which directory invoked it.
        notes = Path(__file__).resolve().parent / sys.argv[1]
    findings = check(notes)
    for f in findings:
        print(f"HASH-STAMP DRIFT: {f}")
    print("hash stamp clean" if not findings else f"{len(findings)} drift finding(s)")
    raise SystemExit(1 if findings else 0)
