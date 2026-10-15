#!/usr/bin/env python3
"""Exact V23.36 → V23.37 provenance; structural, not creative approval."""
import hashlib
import json
import re
from pathlib import Path
here=Path(__file__).resolve().parent
old=here/"V23.36R1_CANDIDATE_E001-E064.md"
new=here/"V23.37R1_CANDIDATE_E001-E064.md"
control=here.parent/"CURRENT_E001-E064.md"
def blob(b):return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def eps(s):
    m=list(re.finditer(r"(?m)^# E(\d{3})《",s))
    assert [int(x.group(1)) for x in m]==list(range(1,65))
    return {int(x.group(1)):s[x.start():m[i+1].start() if i+1<len(m) else len(s)].rstrip() for i,x in enumerate(m)}
oldb=old.read_bytes();newb=new.read_bytes();controlb=control.read_bytes()
assert blob(oldb)=="edeb513edcfe9552c13e56bd1c9c5ed7fbf50734"
assert blob(newb)=="674be611a21e494e7261dd83a5652a0e8a0d2825"
assert blob(controlb)=="c507624f01f56aa2a4c5799ce0dd9fd415926738"
assert hashlib.sha256(controlb).hexdigest()=="564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935"
a=eps(oldb.decode("utf-8"));b=eps(newb.decode("utf-8"));c=eps(controlb.decode("utf-8"))
changed=[n for n in b if a[n]!=b[n]]
assert changed==[24],changed
assert all(b[n]==c[n] for n in range(1,6))
assert len(re.findall(r"(?m)^### 【",newb.decode("utf-8")))==268
assert newb.decode("utf-8").rstrip().endswith("【全剧终】")
assert "买来一张热饼，先吹凉一角才递给他" in b[24]
assert "最后一名女工领到工钱，先在顾娘子面前点清，转身买了一包热食" not in b[24]
assert "让工资匣打开" not in b[24]
assert "明日头场" in b[24] or "翌日头场" in b[24]
print(json.dumps({"status":"STRUCTURAL_PASS_ONLY","version":"V23.37R1-CANDIDATE","changed_episodes":[24],"frozen_E001_E005":True,"episodes":64,"scenes":268,"new_git_blob":blob(newb),"sha256":hashlib.sha256(newb).hexdigest(),"release":"PGS30 HOLD","warning":"No 150s, story, financial or historical identity release implied"},ensure_ascii=False,indent=2))
