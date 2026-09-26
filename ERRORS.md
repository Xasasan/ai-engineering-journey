# ERRORS

| Date | What broke | Root cause | Fix | File/line |
|---|---|---|---|---|
| 2026-09-26 | Claude's PDF reader failed: "pdftoppm is not installed" | poppler not installed on the Mac | `brew install poppler`; converted the book to .md so the PDF is rarely needed | book PDF |
| 2026-09-26 | (avoided) `pip install` into Homebrew Python is blocked | PEP 668 "externally managed environment" | Created a project venv: `python3 -m venv .venv` | `.venv/` |
| 2026-09-26 | Told Xasan the "Gemini free tier covers all models" | Trusted a one-line web-page summary without checking the per-model table | Re-fetched the per-model free-tier rows: 3.1 Pro Preview is not free; no Batch API; caching only on 3.8/3.5 Flash | PLAN.md footnote ² |
