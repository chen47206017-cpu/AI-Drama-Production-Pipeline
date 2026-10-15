#!/usr/bin/env python3
"""Export the exact GitHub V23.36R1 text as UTF-8 MD/TXT and Word, without rewriting.

Release status: HOLD. DOCX is a format rendition of the manuscript; MD is byte-exact.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

PROJECT = Path(__file__).resolve().parents[1]
SRC = PROJECT / "scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md"
DEST = PROJECT.parent.parent / "dist/shuangshu_v23_36"
STEM = "双姝商途_V23.36R1_CANDIDATE_E001-E064_完整正文"
EXPECTED_BLOB = "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734"

def blob_sha(b: bytes) -> str:
    return hashlib.sha1(f"blob {len(b)}\0".encode("ascii")+b).hexdigest()

def set_font(st, name="Microsoft YaHei", size=10.0, bold=False, color=None):
    st.font.name = name
    st.font.size = Pt(size)
    st.font.bold = bold
    if color: st.font.color.rgb = RGBColor(*color)
    rpr = st.element.get_or_add_rPr()
    fonts = rpr.rFonts
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    fonts.set(qn("w:eastAsia"), name)
    fonts.set(qn("w:ascii"), name)
    fonts.set(qn("w:hAnsi"), name)

def main():
    raw = SRC.read_bytes()
    blob = blob_sha(raw)
    if blob != EXPECTED_BLOB:
        raise SystemExit(f"SOURCE_BLOB_MISMATCH {blob}")
    s = raw.decode("utf-8")
    episodes = re.findall(r"(?m)^# E(\d{3})《", s)
    scenes = len(re.findall(r"(?m)^### 【", s))
    if episodes != [f"{i:03d}" for i in range(1,65)] or scenes != 268 or not s.rstrip().endswith("【全剧终】"):
        raise SystemExit("SOURCE_STRUCTURE_MISMATCH")

    DEST.mkdir(parents=True, exist_ok=True)
    md = DEST / (STEM + ".md")
    txt = DEST / (STEM + ".txt")
    word = DEST / (STEM + ".docx")
    md.write_bytes(raw)
    txt.write_bytes(raw)
    if md.read_bytes() != raw or txt.read_bytes() != raw:
        raise SystemExit("SOURCE_COPY_ERROR")

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2.0)
    sec.header_distance, sec.footer_distance = Cm(1.0), Cm(1.0)
    normal = doc.styles["Normal"]
    set_font(normal, size=9.5)
    normal.paragraph_format.space_after = Pt(3)
    normal.paragraph_format.line_spacing = 1.14

    h1 = doc.styles["Heading 1"]
    set_font(h1, size=14, bold=True, color=(22,52,84))
    h1.paragraph_format.space_before = Pt(13)
    h1.paragraph_format.space_after = Pt(6)
    h1.paragraph_format.keep_with_next = True
    h2 = doc.styles["Heading 2"]
    set_font(h2, size=10.5, bold=True, color=(50,76,92))
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(3)
    h2.paragraph_format.keep_with_next = True
    title = doc.styles["Title"]
    set_font(title, size=23, bold=True, color=(22,52,84))

    hdr = sec.header.paragraphs[0]
    hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hdr.add_run("《双姝商途》 · V23.36R1-CANDIDATE · 64集 · HOLD")
    ftr = sec.footer.paragraphs[0]
    ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ftr.add_run("完整剧本正文  |  候选审核稿  |  ")
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    ftr._p.append(fld)

    doc.add_paragraph("双姝商途", "Title")
    p = doc.add_paragraph("V23.36R1-CANDIDATE · E001–E064 · 完整64集 / 268场")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph("PGS30 HOLD / NOT PRODUCTION CLEAN")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("来源：GitHub完整候选正文。此Word文件仅重新排版，未修改动作、对白、剧情与场次。")
    doc.add_paragraph(f"源文件Git Blob：{EXPECTED_BLOB}")
    doc.add_page_break()

    # Include every original nonempty textual line. Blank lines become paragraph spacings.
    line_count = 0
    count = 0
    prev_empty = False
    for line in s.splitlines():
        line_count += 1
        if line.startswith("# E") and re.match(r"^# E\d{3}《", line):
            doc.add_paragraph(line[2:], style="Heading 1"); count += 1
        elif line.startswith("### 【"):
            doc.add_paragraph(line[4:], style="Heading 2"); count += 1
        elif line.startswith("# "):
            doc.add_paragraph(line[2:], style="Heading 1"); count += 1
        elif line.strip():
            doc.add_paragraph(line); count += 1
            prev_empty = False
        else:
            prev_empty = True
    doc.core_properties.title = "双姝商途 V23.36R1-CANDIDATE E001-E064 完整正文"
    doc.core_properties.subject = "64集268场 候选审稿版本 PGS30 HOLD"
    doc.core_properties.author = "《双姝商途》项目"
    doc.save(word)

    detail = {
        "source": str(SRC.relative_to(PROJECT)),
        "version": "V23.36R1-CANDIDATE", "release_status": "PGS30 HOLD",
        "source_git_blob": blob, "source_sha256": hashlib.sha256(raw).hexdigest(),
        "episodes": len(episodes), "scenes": scenes, "text_lines": line_count,
        "word_body_paragraphs": count,
        "files": [md.name, txt.name, word.name],
        "warning": "V23.36 was only newly edited in E010,E024,E045 relative to V23.35; 64 episodes are complete but not all newly rewritten"
    }
    (DEST / "SOURCE_VERIFICATION.json").write_text(json.dumps(detail, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(detail, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
