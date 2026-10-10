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
- Pushed the first commit `3a473cc` to https://github.com/Xasasan/ai-engineering-journey (public, author Xasasan via noreply email).

## 2026-10-10 — Session 0e: Plan re-check against a job-ad roadmap
- Compared PLAN.md with the "AI Engineer Roadmap: Built From 40,000 Real Job Ads" video (Core / AI Core / Stack / Project).
- Already covered: LLMs, RAG, agents, evals (stronger than the video), safety/speed. Missing: building APIs, CI/CD, Docker, LangChain/LangGraph, cloud deploy, running the project live.
- Decided: course **not started yet**. Add a 2-week **Core bootcamp** (B1 Oct 12, B2 Oct 19) and the "branch → PR → green CI" rule for every week. Book W1 is now **Oct 26**; all dates +4 weeks; end ≈ Jul 25 2027.
- Added: CI eval gate (W15), FastAPI capstone (W19), LangChain RAG (W20), LangGraph agent (W22), Docker (W27), AWS account (W33) + deploy (W34), CD + 1 week live (W36–38).
- Capstone is now a **study agent** that takes actions (quiz, grade notes, store weak spots, schedule review), not a PDF Q&A demo. Cloud = **AWS**.
- Updated PLAN.md, README.md, CAREER.md (dates + roadmap notes).

**Next:** B1 Day 1 (Mon Oct 12): baseline self-test on all 8 skills, then start Python for engineers.

## 2026-10-10 — Session 0f: API practice gap
- Found a 4-month gap with no API building between B2 and W19. Added FastAPI endpoints to the B2 app: `/extract` (W8), `/score` (W10), `/eval` (W15).
- Started B1 Day 1 early (Sat): baseline self-test (20 questions, /40) handed out; answers go in `notes/b1_baseline.md`.

**Next:** Xasan finishes the baseline → I check it and log per-skill scores → Day 1 exercise (`code/b1/`: pydantic `Transcript` + JSONL loader + pytest).
- Docker had a 6-month gap (B2 → W27). Fixed: `docker build` in CI from B2 on; capstone Dockerfile from W19; W27 = `docker compose` (app + DB); W32 = vLLM in its official Docker image.
