#!/usr/bin/env python3
"""PGS30 source-integrity checks for 《双姝商途》. Not a production-release gate."""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "scripts"
BASELINE = "V23.33R1"
ARCHIVE_BLOBS = {
    "V23.22R1": "5f08d623c9bcf8397337df8dd28f153485cd7dd5",
    "V23.23R1": "4c93f93762436325f608a874009d36b2cb661e23",
    "V23.24R1": "03b70dff46f1df54af5ed8f157103176775ba3a5",
    "V23.25R1": "78889f3edccd9b5f406aec7473c6f96d5077d94e",
    "V23.26R1": "216fd3afffdadd84f443fd513eca33fa80f63578",
    "V23.27R1": "594bf1bbd0673730fae0ffae4ac0b186a02917d1",
    "V23.28R1": "e62daebe12acc6b39fe72dfc58b4db1a65223774",
    "V23.29R1": "725be6fdb6403f0d77067652171d0a85418f18d4",
    "V23.30R1": "572ac46d92b834295025e93a3fbaca0ca5645a0f",
    "V23.31R1": "cba4847a153e631b401bbc93059094b4c55ffb45",
    "V23.32R1": "08fb797ba0c1be34dcf71d7fa51ef40f60463efa",
    "V23.33R1": "c507624f01f56aa2a4c5799ce0dd9fd415926738",
}
BINARY_BLOBS = {
    "releases/V23.33R1/V23.33R1_full_script_HOLD.docx": "dc7d793f0091ecebdea7bdced5c7d97ee7cc426e",
    "releases/V23.33R1/V23.33R1_audit_report_HOLD.docx": "9d0c3253746f158982127def905a41386f85a4ec",
    "releases/V23.33R1/V23.33R1_complete_delivery_HOLD.zip": "24e8efab13df9fbb8c4584022a91f9c10fbe18ff",
    "skills/story-impact-v2.2/Story_Impact_Adversarial_Audit_Skill_v2.2.zip": "da12ec77fdf8ae7242e9299163b03dd2d732dfff",
}


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def episodes(text: str) -> dict[str, str]:
    marks = list(re.finditer(r"(?m)^# E(\d{3})", text))
    if [int(m.group(1)) for m in marks] != list(range(1, 65)):
        raise ValueError("Expected exactly E001–E064 once, in order")
    return {m.group(1): text[m.start(): marks[i + 1].start() if i < 63 else len(text)] for i, m in enumerate(marks)}


def main() -> int:
    failures = []
    full_path = P / "CURRENT_E001-E064.md"
    if not full_path.is_file():
        print(f"MISSING: {full_path}")
        return 2
    full = full_path.read_text(encoding="utf-8")
    try:
        split = episodes(full)
        base_split = episodes((P / "versions" / f"{BASELINE}.md").read_text(encoding="utf-8"))
    except (ValueError, FileNotFoundError) as ex:
        print("FAIL:", ex)
        return 2
    if len(re.findall(r"(?m)^### 【", full)) != 268:
        failures.append("Expected 268 named scenes in current 64-episode format")
    for number, body in split.items():
        fn = P / "episodes" / f"E{number}.md"
        if not fn.is_file() or fn.read_text(encoding="utf-8") != body:
            failures.append(f"episode mirror mismatch: E{number}")
        if int(number) <= 5 and body != base_split[number]:
            failures.append(f"frozen E{number} changed from {BASELINE}")
    for name, sha in ARCHIVE_BLOBS.items():
        fn = P / "versions" / f"{name}.md"
        if not fn.is_file() or blob_sha(fn.read_bytes()) != sha:
            failures.append(f"historical original changed/missing: {name}")
    for relative, sha in BINARY_BLOBS.items():
        fn = ROOT / relative
        if not fn.is_file() or blob_sha(fn.read_bytes()) != sha:
            failures.append(f"original binary changed/missing: {relative}")
    # Current master must match its *declared* version in the pointer when a new version is accepted.
    pointer = (ROOT / "CURRENT_PROJECT_POINTER.md").read_text(encoding="utf-8")
    marker = re.search(r"Latest verified script:\s*\*\*(V\d+\.\d+R\d+)\*\*", pointer)
    if marker:
        candidate = P / "versions" / f"{marker.group(1)}.md"
        if not candidate.is_file() or candidate.read_bytes() != full_path.read_bytes():
            failures.append("CURRENT master != pointer's declared version archive")
    else:
        failures.append("CURRENT_PROJECT_POINTER missing/invalid version marker")
    print(f"Source checks: {len(split)} episodes / 268 scenes / {len(ARCHIVE_BLOBS)} history / {len(BINARY_BLOBS)} binary snapshots")
    if failures:
        for msg in failures:
            print("FAIL:", msg)
        return 1
    print("STATIC SOURCE INTEGRITY PASS; PGS30 RELEASE REMAINS HOLD")
    return 0


if __name__ == "__main__":
    sys.exit(main())