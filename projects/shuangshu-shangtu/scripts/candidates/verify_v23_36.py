#!/usr/bin/env python3
"""Machine-verifiable *structural* provenance: V23.36 candidate, not PGS release authority."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = {
    "official_v23_33": HERE.parent / "CURRENT_E001-E064.md",
    "previous_v23_35": HERE / "V23.35R1_CANDIDATE_E001-E064.md",
    "candidate_v23_36": HERE / "V23.36R1_CANDIDATE_E001-E064.md",
}
BLOBS = {
    "official_v23_33": "c507624f01f56aa2a4c5799ce0dd9fd415926738",
    "previous_v23_35": "d01dad0792d8c80506a97796790ce852a2b578d2",
    "candidate_v23_36": "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734",
}
SHA256_CURRENT = "564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935"
ROUND_CHANGED = [10, 24, 45]
CUMULATIVE_CHANGED = [10, 11, 18, 19, 24, 25, 40, 42, 45, 50, 58]

def git_blob(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()

def episodes(body: str) -> dict[int, str]:
    matches = list(re.finditer(r"(?m)^# E(\d{3})《[^\n]*》", body))
    ids = [int(m.group(1)) for m in matches]
    assert ids == list(range(1, 65)), f"Episode sequence: {ids}"
    return {eid: body[m.start():(matches[i + 1].start() if i + 1 < len(matches) else len(body))].strip()
            for i, (m, eid) in enumerate(zip(matches, ids))}

def main() -> None:
    raw = {key: path.read_bytes() for key, path in FILES.items()}
    for key, blob in BLOBS.items():
        assert git_blob(raw[key]) == blob, f"Git Blob mismatch: {key}"
    assert hashlib.sha256(raw["official_v23_33"]).hexdigest() == SHA256_CURRENT
    decoded = {k: v.decode("utf-8") for k, v in raw.items()}
    parts = {k: episodes(v) for k, v in decoded.items()}
    parent = parts["previous_v23_35"]
    candidate = parts["candidate_v23_36"]
    original = parts["official_v23_33"]
    changed = [n for n in range(1, 65) if parent[n] != candidate[n]]
    total_changed = [n for n in range(1, 65) if original[n] != candidate[n]]
    assert changed == ROUND_CHANGED, f"Incorrect changed episodes: {changed}"
    assert total_changed == CUMULATIVE_CHANGED, f"Incorrect cumulative episodes: {total_changed}"
    assert all(original[n] == candidate[n] for n in range(1, 6)), "Frozen E001–E005 changed"
    scene_count = len(re.findall(r"(?m)^### 【", decoded["candidate_v23_36"]))
    assert scene_count == 268, f"Incorrect scenes: {scene_count}"
    assert decoded["candidate_v23_36"].rstrip().endswith("【全剧终】")
    for token in ("十六席", "四百八十文", "三百", "八十", "四十文",
                  "二十个人", "六块米糕", "31×22＝682", "12×25＝300",
                  "9×34＝306", "940", "460", "四十六户", "四十一户"):
        assert token in decoded["candidate_v23_36"], f"Missing story anchor: {token}"
    for id_, needle in ((10, "合上观灯窗"), (24, "二十个人白等"), (45, "整匣始终未开")):
        assert needle in candidate[id_], f"E{id_:03d} patched content absent"
    print(json.dumps({
        "status": "STRUCTURAL_PASS_ONLY", "pgs30_release": "HOLD",
        "episodes": len(candidate), "scenes": scene_count,
        "round_changed_episodes": changed, "cumulative_changed_episodes": total_changed,
        "frozen_E001_E005_unchanged": True,
        "candidate_blob_sha1": git_blob(raw["candidate_v23_36"]),
        "candidate_sha256": hashlib.sha256(raw["candidate_v23_36"]).hexdigest(),
        "release_authority": "NONE",
        "limits": "No artistic, institutional, financial provenance or production timing PASS implied",
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
