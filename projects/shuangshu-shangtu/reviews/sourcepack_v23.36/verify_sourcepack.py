#!/usr/bin/env python3
"""Verify V23.36 reading pack copies its authoritative full manuscript exactly.

A PASS here verifies source text identity only, never artistic quality or release authority.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
MASTER = PROJECT / "scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md"
EXPECTED_BLOB = "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734"
EXPECTED_EPISODES = 64
EXPECTED_SCENES = 268


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def split_episodes(text: str) -> dict[str, str]:
    markers = list(re.finditer(r"(?m)^# E(\d{3})《([^》]+)》", text))
    ids = ["E" + m.group(1) for m in markers]
    assert ids == [f"E{n:03d}" for n in range(1, 65)], f"Bad episode IDs: {ids}"
    return {
        e: text[m.start():markers[i + 1].start() if i + 1 < len(markers) else len(text)].rstrip() + "\n"
        for i, (e, m) in enumerate(zip(ids, markers))
    }


def main() -> None:
    raw = MASTER.read_bytes()
    assert git_blob(raw) == EXPECTED_BLOB, "Authoritative source Git blob mismatch"
    master = raw.decode("utf-8")
    sections = split_episodes(master)
    assert len(sections) == EXPECTED_EPISODES
    assert len(re.findall(r"(?m)^### 【", master)) == EXPECTED_SCENES
    manifest = json.loads((HERE / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["source_git_blob"] == EXPECTED_BLOB
    assert manifest["episodes"] == EXPECTED_EPISODES
    assert manifest["scenes"] == EXPECTED_SCENES

    for entry in manifest["episode_files"]:
        episode = entry["id"]
        actual = (HERE / "episodes" / f"{episode}.md").read_text(encoding="utf-8")
        expected = sections[episode]
        assert actual == expected, f"{episode} split text differs from master"
        assert actual.count("### 【") == entry["scenes"], f"{episode}: scene count wrong"

    for b in manifest["batch_files"]:
        first, last = int(b["first"][1:]), int(b["last"][1:])
        wanted = "\n\n".join(sections[f"E{x:03d}"].rstrip()
                             for x in range(first, last + 1)) + "\n"
        got = (HERE / "batches" / (b["id"] + ".md")).read_text(encoding="utf-8")
        assert got == wanted, f"{b['id']} batch does not reconstruct source"

    # Exact location / scene anchors: tests are not a substitute for reading full stories.
    assert "无钱、来处又说不清，我不敢收" in sections["E002"]
    assert "门外女工" in sections["E024"] and "买了热饼" in sections["E024"]
    for i in range(40, 49):
        assert sections[f"E{i:03d}"], f"Missing E{i:03d}"
    assert "护行钱" in sections["E058"]
    assert "提前写下的“已查”" in sections["E062"]

    print(json.dumps({
        "status": "SOURCEPACK_STRUCTURAL_PASS_ONLY",
        "source_blob": EXPECTED_BLOB,
        "episodes": 64,
        "scenes": 268,
        "episode_files_verified": 64,
        "batch_files_verified": 8,
        "release_status": "PGS30 HOLD",
        "limitations": "Cannot prove an AI actually read, understood or cited each episode"
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
