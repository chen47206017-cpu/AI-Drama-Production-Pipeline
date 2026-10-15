#!/usr/bin/env python3
"""Negative-control tests: reject fabricated quote and false coverage claims."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from verify_evidence import BLOB, VERSION, check


class EvidenceGateTests(unittest.TestCase):
    def _save(self, obj: dict) -> Path:
        # The directory persists only for the unit test; sourcepack files remain untouched.
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as f:
            json.dump(obj, f, ensure_ascii=False)
            return Path(f.name)

    def test_true_quote_passes(self):
        item = {
            "source_version": VERSION,
            "source_git_blob": BLOB,
            "episodes_read": ["E024"],
            "full_audit": False,
            "claims": [{"episode": "E024", "scene": "算对了也得付钱",
                        "quote": "先排队的装卸工亲眼看到账房重新开工资匣",
                        "kind": "FACT_VERIFIED"}],
        }
        f = self._save(item)
        try:
            self.assertEqual(check(f)["exact_fact_quotes_matched"], 1)
        finally:
            f.unlink()

    def test_fabricated_quote_is_rejected(self):
        item = {
            "source_version": VERSION,
            "source_git_blob": BLOB,
            "episodes_read": ["E024"],
            "claims": [{"episode": "E024", "scene": "算对了也得付钱",
                        "quote": "程晚凤随后回到了现代写真园",
                        "kind": "FACT_VERIFIED"}],
        }
        f = self._save(item)
        try:
            with self.assertRaises(ValueError):
                check(f)
        finally:
            f.unlink()

    def test_false_full_read_is_rejected(self):
        item = {
            "source_version": VERSION,
            "source_git_blob": BLOB,
            "episodes_read": ["E024"],
            "full_audit": True,
            "claims": [{"episode": "E024", "scene": "算对了也得付钱",
                        "quote": "先排队的装卸工亲眼看到账房重新开工资匣",
                        "kind": "FACT_VERIFIED"}],
        }
        f = self._save(item)
        try:
            with self.assertRaises(ValueError):
                check(f)
        finally:
            f.unlink()


if __name__ == "__main__":
    unittest.main()
