# AI START HERE — repository reading guide

> For humans and external AI reviewers. This is a **navigation document**, not a production-release certificate.

## Which version is latest?

- Project: **《双姝商途》 / shuangshu-shangtu**
- Verified manuscript: **V23.33R1 — E001–E064 (64 episodes / 268 scenes)**
- Production status: **PGS30 HOLD / NOT PRODUCTION CLEAN**
- Frozen episodes: **E001–E005** (no rewrite without owner authorization)
- Manuscript Git blob: `c507624f01f56aa2a4c5799ce0dd9fd415926738`
- Manuscript SHA256: `564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935`

## Navigate without guessing the default branch

The **main** branch currently has an older V23.5R1 deliverable. V23.33R1 is on the separate branch `ai-import/shuangshu-v23.33r1-20261016`, awaiting review in [PR #1](https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/pull/1). GitHub code search indexes default branches; **do not infer absence from an empty search result**.

- [Project AI access guide](projects/shuangshu-shangtu/AI_ACCESS_GUIDE.md)
- [Machine-readable AI index](projects/shuangshu-shangtu/AI_INDEX.json)
- [Episode-by-episode links](projects/shuangshu-shangtu/EPISODE_INDEX.md)
- [Complete editable master](projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md)
- [Current version pointer](projects/shuangshu-shangtu/CURRENT_PROJECT_POINTER.md)
- [AI work rules](projects/shuangshu-shangtu/AGENTS.md)
- [Canon](projects/shuangshu-shangtu/canon/PROJECT_CANON.md)
- [External AI review prompt](projects/shuangshu-shangtu/EXTERNAL_AI_REVIEW_PROMPT.md)

**Pinned manuscript (independent of branch changes):**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md

## Reading and review requirements

1. Resolve the exact branch or pinned commit; load the current version pointer and the full manuscript.
2. If a platform truncates the full manuscript, read all 64 individual episode files in eight batches: E001–E008, …, E057–E064. Do not claim complete coverage if batches were skipped.
3. Review Canon, AGENTS, PGS HOLD issues and existing audits.
4. Quote exact episode, scene and original text. Separate verified manuscript facts from proposals.
5. **Review only** by default; don't alter scripts, force push, merge PR #1 or declare SSS/Production Clean.

## Security caveat

The repository was verified **PUBLIC** on 2026-10-16, despite an older project README claiming Private. Public files can be viewed and downloaded. Changes to visibility and repository/branch access controls require the owner to configure GitHub settings. AI text instructions are not security enforcement.
