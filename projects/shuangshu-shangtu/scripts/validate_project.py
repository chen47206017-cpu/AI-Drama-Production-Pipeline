#!/usr/bin/env python3
"""Read-only structural and SHA gate for 《双姝商途》 GitHub imports."""
from pathlib import Path
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests/verified_script_versions.json"
ACTIVE = ROOT / "scripts/CURRENT_E001-E064.md"
VERSIONS = ROOT / "scripts/versions"
EPISODES = ROOT / "scripts/episodes"
FREEZE = {
 "E001":"d3e050d9b218ee2de4cf0ffce66a41ca4bdf71639ffe0b28a3d09d23839324e8",
 "E002":"17ce0080204f8d6af300fd5d3004229d02dd2a8966fe9713673cd0d165f707b3",
 "E003":"b85510f61716334eebd4e95703273d2bb0517a510e42596cab176486bc0d0ff9",
 "E004":"e325a25212a3d53f3054319b3bee4dfa04a78dd13872f293b56e5616296787f1",
 "E005":"a7a84e897c20feba5ae5938847f989a4bd1911cb65d0e6b219c7db16cd10d47f",
}
def sha(b): return hashlib.sha256(b).hexdigest()
def gate():
    problems=[]
    data=json.loads(MANIFEST.read_text(encoding="utf-8"))
    for v in data["versions"]:
        f=ROOT / v["path"]
        if not f.exists(): problems.append("missing history: "+str(f));continue
        b=f.read_bytes()
        if len(b)!=v["bytes"] or sha(b)!=v["sha256"]:
            problems.append("history bytes/SHA mismatch: "+v["version"])
    active=ACTIVE.read_bytes()
    expected=next(v for v in data["versions"] if v["version"]==data["accepted_source"])
    if sha(active)!=expected["sha256"]: problems.append("ACTIVE NOT VERIFIED VERSION")
    s=active.decode("utf-8")
    markers=list(re.finditer(r"(?m)^# E(\d{3})",s))
    if len(markers)!=64 or [int(m.group(1)) for m in markers]!=list(range(1,65)):
        problems.append("episode numbering/count")
    scene_count=len(re.findall(r"(?m)^### 【",s))
    if scene_count!=268: problems.append(f"expected 268 scenes, got {scene_count}")
    if len(markers)==64:
        for i,m in enumerate(markers):
            n=m.group(1); f=EPISODES / ("E"+n+".md")
            part=s[m.start():markers[i+1].start() if i<63 else len(s)]
            if not f.exists(): problems.append("missing episode E"+n);continue
            b=f.read_bytes()
            if b != part.encode("utf-8"): problems.append("episode differs from full text: E"+n)
            if ("E"+n) in FREEZE and sha(b)!=FREEZE["E"+n]:
                problems.append("frozen episode changed: E"+n)
    if not s.rstrip().endswith("【全剧终】"): problems.append("missing 全剧终")
    if problems:
        print("STATIC HOLD FAIL:",*problems,sep="\n- ")
        return 1
    print("PASS — immutable histories, active full 64 episodes, all 64 split files, five frozen episodes, 268 scenes, ending.")
    print("This is NOT a production-release authorization; PGS30 remains HOLD.")
    return 0
if __name__=="__main__":sys.exit(gate())
