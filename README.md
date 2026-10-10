# AI Engineering Journey

A 9-month, hands-on study of **AI Engineering: Building Applications with Foundation Models** (Chip Huyen, O'Reilly 2025), by **Xasan**, an AI/ML/NLP engineer working on Uzbek speech and NLP in Tashkent.

Every chapter ends with runnable code, a cheat sheet, and an exam. It also builds the engineering core around it: Python, FastAPI, Git, CI/CD, Docker, LangChain/LangGraph, and AWS. The capstone is a **study agent**: RAG + tool-using agent with an eval suite in CI, guardrails, caching, and user feedback, deployed to AWS.

| | |
|---|---|
| Schedule | 2 h/day, 2-week core bootcamp + 39 weeks (2026-10-12 → 2027-07-25), see [`PLAN.md`](PLAN.md) |
| Progress | Session log in [`PROGRESS.md`](PROGRESS.md); fixed errors in [`ERRORS.md`](ERRORS.md) |
| Code | [`code/`](code/): one folder per week |
| Notes | `notes/`: own-words chapter notes + cheat sheets |
| Stack | Python · FastAPI · LangChain/LangGraph · Docker · GitHub Actions · AWS · local open models (HF, vLLM) · a hosted LLM API, chosen in Week 8 |
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
