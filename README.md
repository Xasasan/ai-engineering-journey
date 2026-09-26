# AI Engineering Journey

A 9-month, hands-on study of **AI Engineering: Building Applications with Foundation Models** (Chip Huyen, O'Reilly 2025), by **Xasan**, an AI/ML/NLP engineer working on Uzbek speech and NLP in Tashkent.

Every chapter ends with runnable code, a cheat sheet, and an exam. The capstone is **"Book Mentor"**: a RAG + agent assistant with a full evaluation pipeline, guardrails, caching, and user feedback.

| | |
|---|---|
| Schedule | 2 h/day, 39 weeks (2026-09-28 → 2027-06-27), see [`PLAN.md`](PLAN.md) |
| Progress | Session log in [`PROGRESS.md`](PROGRESS.md); fixed errors in [`ERRORS.md`](ERRORS.md) |
| Code | [`code/`](code/): one folder per week |
| Notes | `notes/`: own-words chapter notes + cheat sheets |
| Stack | Python · local open models (HF, vLLM) · a hosted LLM API, chosen in Week 8 |
| Source #2 | Marina Wyss, ["AI Engineering in 76 Minutes"](https://www.youtube.com/watch?v=JV3pL1_mn2M) |

> **The book is not included in this repo** (it's copyrighted). Get your own copy from O'Reilly. Notes cite page numbers and use only short quotes.

## Local setup
```bash
python3 -m venv .venv && source .venv/bin/activate
python3 code/cost_estimate.py   # example: API cost estimate across providers
```

## Search the book locally (with your own converted copy)
```bash
BOOK=OceanofPDF.com_AI_Engineering_Building_Applications_-_Chip_Huyen.md
grep -n -i "perplexity" "$BOOK" | head                  # find a term
grep -n "^##" "$BOOK"                                   # list chapters/sections with pages
sed -n '/<!-- page 495 -->/,/<!-- page 496 -->/p' "$BOOK"  # read one page
```
