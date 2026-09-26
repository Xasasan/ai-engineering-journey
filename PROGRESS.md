# PROGRESS

## 2026-09-26 — Session 0: Setup
- Decided: English, generic English projects, Claude API, 2 h/day × 39 weeks (start Mon 2026-09-28).
- Installed `poppler` (brew) and `pypdf` (in `.venv/`).
- Converted the book PDF → `OceanofPDF.com_AI_Engineering_Building_Applications_-_Chip_Huyen.md` (991 pages, `<!-- page N -->` markers, 66 chapter/section headings from the PDF bookmarks).
- Mapped Marina's video timestamps to chapters.
- Created `CLAUDE.md`, `README.md`, `PLAN.md`, `PROGRESS.md`, `ERRORS.md`.

**Next:** Week 1 Day 1: Preface p. 9–31, Claude API setup, baseline self-test.

## 2026-09-26 — Session 0b: Plan re-check
- Learned: the Max plan does not include the Claude API (separate billing). `claude -p` uses Max limits but can't do raw tool use, timing, or cache control.
- Fixed PLAN.md week splits to match the book's real section pages (W12–13, 16–17, 19–22, 25–26, 31–34).
- Tagged every exercise `[—]` / `[local]` / `[API]` / `[claude -p]`.
- API choice deferred to **Week 8**. Claude API estimate ≈ $36 planned, ≈ $53 with buffer (`code/cost_estimate.py`).
- Weak spot to revisit: what logprobs are (Book p. 195–196). It's covered properly in Week 8.

**Next:** Week 1 Day 1: Preface p. 9–31, first model call via `claude -p` (no API key needed), baseline self-test.

## 2026-09-26 — Session 0c: Provider cost comparison
- Fetched Gemini (page updated 2026-09-24) and DeepSeek pricing. `code/cost_estimate.py` now compares 3 providers on the same 7,550-call workload.
- With buffer: Claude ≈ $53 · Gemini ≈ $22 (free tier $0) · DeepSeek ≈ $19 (off-peak ≈ $9.50). Decision is still at Week 8.
- Updated PLAN.md (Week 8 section) and CLAUDE.md.
- Checked the Gemini free tier: usable for the whole course with workarounds (W13 2.5 Pro, W28 spread over days, W32 3.8 Flash). Fixed the wrong "all models free" claim.

## 2026-09-26 — Session 0d: GitHub setup
- Added a private local plan (`CAREER.md`, gitignored).
- Added GitHub rules to CLAUDE.md; rewrote README.md as the public front page; created .gitignore (book, transcript, .venv, secrets, weights excluded).
- `git init -b main` done. **Waiting on:** `gh auth login` as Xasasan, then create the public repo `ai-engineering-journey` and make the first push.
