#!/usr/bin/env python3
"""V23.35 structural provenance gate; never an artistic or PGS release authority."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "V23.34R1_CANDIDATE_E001-E064.md"
CANDIDATE = HERE / "V23.35R1_CANDIDATE_E001-E064.md"
CURRENT = HERE.parent / "CURRENT_E001-E064.md"
EXPECTED_BLOBS = {
    "current": "c507624f01f56aa2a4c5799ce0dd9fd415926738",
    "parent": "0f58bfd58e3df3a73257ac8925483375cc1528a4",
    "candidate": "d01dad0792d8c80506a97796790ce852a2b578d2",
}
EXPECTED_CURRENT_SHA256 = "564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935"
NEW_CHANGED = [25, 40, 42, 58]
ALL_CHANGED = [11, 18, 19, 25, 40, 42, 50, 58]
EPISODES = 64
SCENES = 268

def blob_sha(data: bytes) -> str:
    prefix = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(prefix + data).hexdigest()

def sectionize(text: str) -> dict[int, str]:
    markers = list(re.finditer(r"(?m)^# E(\d{3})《[^\n]*》", text))
    numbers = [int(x.group(1)) for x in markers]
    assert numbers == list(range(1, EPISODES + 1)), f"Episode order: {numbers}"
    return {
        num: text[m.start() : (markers[i+1].start() if i+1 < len(markers) else len(text))].strip()
        for i, (m, num) in enumerate(zip(markers, numbers))
    }

def main() -> None:
    raw = {"current": CURRENT.read_bytes(), "parent": PARENT.read_bytes(),
           "candidate": CANDIDATE.read_bytes()}
    for name, expected in EXPECTED_BLOBS.items():
        actual = blob_sha(raw[name])
        assert actual == expected, f"{name} git blob mismatch: {actual} != {expected}"
    assert hashlib.sha256(raw["current"]).hexdigest() == EXPECTED_CURRENT_SHA256
    parsed = {name: sectionize(data.decode("utf-8")) for name, data in raw.items()}
    diff_parent = [n for n in range(1, 65) if parsed["parent"][n] != parsed["candidate"][n]]
    diff_current = [n for n in range(1, 65) if parsed["current"][n] != parsed["candidate"][n]]
    assert diff_parent == NEW_CHANGED, f"New episode diff incorrect: {diff_parent}"
    assert diff_current == ALL_CHANGED, f"Cumulative episode diff incorrect: {diff_current}"
    for n in range(1, 6):
        assert parsed["candidate"][n] == parsed["current"][n], f"Frozen E{n:03d} changed"
    text = raw["candidate"].decode("utf-8")
    assert len(re.findall(r"(?m)^### 【", text)) == SCENES
    assert text.rstrip().endswith("【全剧终】")
    for anchor in ("31×22＝682", "12×25＝300", "9×34＝306", "940", "460",
                   "四十六户", "两名巡夜人", "二十文", "十文"):
        assert anchor in text, f"Missing source anchor {anchor}"
    print(json.dumps({
        "gate": "STRUCTURAL_PASS_ONLY",
        "release_authority": "NONE",
        "pgs30": "HOLD",
        "episodes": 64,
        "scenes": 268,
        "changed_from_v23_34": diff_parent,
        "changed_from_v23_33": diff_current,
        "frozen_episodes_unchanged": True,
        "candidate_git_blob": blob_sha(raw["candidate"]),
        "candidate_sha256": hashlib.sha256(raw["candidate"]).hexdigest(),
        "warning": "No cash-source, studio-timing, canon institution or dramatic-value PASS implied",
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
