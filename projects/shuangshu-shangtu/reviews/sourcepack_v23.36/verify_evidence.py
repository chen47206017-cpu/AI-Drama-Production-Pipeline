#!/usr/bin/env python3
"""Validate review facts against exact V23.36 episode/scene text.

Usage: python3 verify_evidence.py path/to/review_evidence.json
A PASS guarantees literal quote / episode / scene matching, NOT truthful reading or interpretation.
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERSION = "V23.36R1-CANDIDATE"
BLOB = "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734"
EXPECTED_EPISODES = [f"E{n:03d}" for n in range(1, 65)]


def scenes_of(body: str) -> list[tuple[str, str]]:
    m = list(re.finditer(r"(?m)^### 【([^\n]+)$", body))
    return [
        (q.group(1), body[q.end():m[i + 1].start() if i + 1 < len(m) else len(body)])
        for i, q in enumerate(m)
    ]


def fail(message: str) -> None:
    raise ValueError(message)


def check(path: Path) -> dict:
    report = json.loads(path.read_text(encoding="utf-8"))
    if report.get("source_version") != VERSION or report.get("source_git_blob") != BLOB:
        fail("Wrong source_version or source_git_blob; cannot use an older manuscript.")
    read = report.get("episodes_read")
    if not isinstance(read, list) or any(x not in EXPECTED_EPISODES for x in read):
        fail("episodes_read must be a list of E001..E064")
    if len(read) != len(set(read)):
        fail("episodes_read includes duplicate episode IDs")
    claims = report.get("claims", [])
    if not isinstance(claims, list):
        fail("claims must be an array")
    counted: dict[str, set[str]] = collections.defaultdict(set)
    checked = 0
    for j, item in enumerate(claims, start=1):
        ep, kind = item.get("episode"), item.get("kind")
        if ep not in EXPECTED_EPISODES:
            fail(f"Claim {j}: invalid episode")
        if kind not in ("FACT_VERIFIED", "INFERENCE", "PROPOSAL", "UNKNOWN"):
            fail(f"Claim {j}: invalid kind")
        if kind != "FACT_VERIFIED":
            continue
        if ep not in read:
            fail(f"Claim {j}: fact for {ep} but episode missing from episodes_read")
        quote, heading = item.get("quote"), item.get("scene")
        if not isinstance(quote, str) or len(quote) < 12:
            fail(f"Claim {j}: quote too short / absent")
        if not isinstance(heading, str) or not heading.strip():
            fail(f"Claim {j}: scene title missing")
        body = (HERE / "episodes" / f"{ep}.md").read_text(encoding="utf-8")
        matches = [(title, scene) for title, scene in scenes_of(body)
                   if heading.strip() in title]
        if not matches:
            fail(f"Claim {j}: declared scene {heading!r} does not appear in {ep}")
        found = [(title, scene) for title, scene in matches if quote in scene]
        if not found:
            fail(f"Claim {j}: exact quote not in the declared scene of {ep}")
        counted[ep].add(found[0][0])
        checked += 1
    if report.get("full_audit") is True:
        if sorted(read) != EXPECTED_EPISODES:
            fail(f"full_audit claims 64, but has only {len(read)} distinct episodes")
        missing = [e for e in EXPECTED_EPISODES if len(counted[e]) < 2]
        if missing:
            fail("full_audit needs two exact quotes from two different scenes for every "
                 f"episode; missing: {', '.join(missing)}")
    return {
        "status": "QUOTE_MATCH_ONLY",
        "review_file": str(path),
        "episodes_declared_read": len(read),
        "exact_fact_quotes_matched": checked,
        "full_audit_structural_claim_accepted": report.get("full_audit") is True,
        "limits": "Proves only source/episode/scene literal matching; not comprehension, honest reading, or creative quality"
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 verify_evidence.py path/to/review_evidence.json")
    try:
        print(json.dumps(check(Path(sys.argv[1])), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"EVIDENCE_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
