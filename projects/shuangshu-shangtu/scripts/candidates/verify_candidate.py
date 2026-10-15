#!/usr/bin/env python3
"""Deterministic *structural* verifier for V23.34R1 candidate; not PGS release approval."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "CURRENT_E001-E064.md"
CANDIDATE = HERE / "V23.34R1_CANDIDATE_E001-E064.md"
EXPECTED_SOURCE_SHA256 = "564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935"
EXPECTED_CANDIDATE_BLOB = "0f58bfd58e3df3a73257ac8925483375cc1528a4"
EXPECTED_CHANGED = [11, 18, 19, 50]
EXPECTED_SCENE_COUNT = 268

def extract(body: str) -> dict[int, str]:
    hits = list(re.finditer(r"(?m)^# E(\d{3})《[^\n]+》", body))
    numbers = [int(m.group(1)) for m in hits]
    assert numbers == list(range(1, 65)), f"Episode sequence mismatch: {numbers}"
    return {n: body[m.start():(hits[i + 1].start() if i + 1 < len(hits) else len(body))].strip()
            for i, (m, n) in enumerate(zip(hits, numbers))}

def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()

def main() -> None:
    a_bytes, b_bytes = SOURCE.read_bytes(), CANDIDATE.read_bytes()
    assert hashlib.sha256(a_bytes).hexdigest() == EXPECTED_SOURCE_SHA256, "Parent SHA256 mismatch"
    assert git_blob_sha1(b_bytes) == EXPECTED_CANDIDATE_BLOB, "Candidate Git Blob mismatch"
    a = extract(a_bytes.decode("utf-8"))
    b = extract(b_bytes.decode("utf-8"))
    changed = [n for n in range(1, 65) if a[n] != b[n]]
    assert changed == EXPECTED_CHANGED, f"Unexpected changed episodes: {changed}"
    for n in range(1, 6):
        assert a[n] == b[n], f"Frozen E{n:03d} changed"
    assert len(re.findall(r"(?m)^### 【", b_bytes.decode("utf-8"))) == EXPECTED_SCENE_COUNT
    for token in ["31×22＝682", "12×25＝300", "9×34＝306", "1288", "940", "460", "【全剧终】"]:
        assert token in b_bytes.decode("utf-8"), f"Missing required structural token: {token}"
    print(json.dumps({"status": "STRUCTURAL_PASS_ONLY",
                      "episodes": len(b), "scenes": EXPECTED_SCENE_COUNT,
                      "changed": changed, "frozen_unchanged": True,
                      "candidate_blob_sha1": git_blob_sha1(b_bytes),
                      "candidate_sha256": hashlib.sha256(b_bytes).hexdigest(),
                      "pgs_release": "HOLD"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
