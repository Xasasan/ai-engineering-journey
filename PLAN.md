# PLAN — AI Engineering in 2 + 39 Weeks

Two goals: master the book **and** the engineering core that AI-engineer job ads ask for (Python, APIs, Git, CI/CD + LangChain/LangGraph, RAG, agents, evals, cloud deploy). Core items come from a job-ad roadmap video (Data with Baraa, "AI Engineer Roadmap: Built From 40,000 Real Job Ads"), so they are **[Beyond the book]**.

"p." means a PDF page of the book. "M" means a Marina Wyss video timestamp.
**Daily (2 h):** 60 min reading · 30 min own-words note (checked against the book) · 30 min code.
**Day 7:** a 10-question quiz, a weak-spot review, and a project step. **Each chapter ends with** an exam and a one-page cheat sheet.
Reading pace is about 5–7 PDF pages/day, leaving time to re-read the hard parts. Week splits follow the book's real section starts.

**What each exercise needs:**
`[—]` no model · `[local]` a free open model on the Mac or Linux server · `[API]` a paid LLM API (provider chosen in **Week 8**) · `[claude -p]` Claude Code headless mode, included in Max

**Core rule (from B2 on, every week):** all code goes branch → PR → green CI (ruff + pytest + `docker build`) → merge. When the B2 app gets a new endpoint, rebuild and run its container locally. Functions are typed, and every exercise has at least one test. This is how the core becomes habit, not a one-off.

## Core bootcamp (before Chapter 1) [Beyond the book]
| Week | Dates | Learn | Build / Check |
|---|---|---|---|
| B1 | Oct 12 | **Day 1: baseline self-test** (Python, APIs, Git, CI/CD, LLM/RAG/agents/evals; 1 h, scores logged). **Python for engineers:** type hints, dataclasses + pydantic, `pyproject.toml`, logging, exceptions, `pytest`. **Git:** branches, PRs, rebase, merge conflicts | A small typed package with tests, merged through your own PR `[—]` |
| B2 | Oct 19 | **APIs:** HTTP, REST, status codes, JSON, `httpx`, **FastAPI** + async. **CI/CD:** GitHub Actions (ruff + pytest on every push). **Docker** basics | Wrap the B1 package in a FastAPI service in Docker; CI must be green on the PR `[—]` |

## Month 1 — Orientation & Chapter 1: Introduction (p. 32–118) · M 00:00
| Week | Dates | Read | Build / Check |
|---|---|---|---|
| 1 | Oct 26 | Preface p. 9–31; re-watch the full Marina video, taking notes | Setup: `notes/`, `code/`, book search. First model call from a script via `claude -p` `[claude -p]` |
| 2 | Nov 2 | The Rise of AI Engineering p. 34–56 | Note: AI eng vs ML eng (write the table yourself) `[—]` |
| 3 | Nov 9 | Foundation Model Use Cases p. 57–77 · Planning AI Applications p. 78–90 | Write a use-case evaluation for one idea (the book's planning questions) `[—]` |
| 4 | Nov 16 | The AI Engineering Stack p. 91–118 | **Ch 1 exam** + cheat sheet `[—]` |

## Month 2 — Chapter 2: Understanding Foundation Models (p. 119–231) · M 01:53
| 5 | Nov 23 | Training Data p. 121–134 · Model Architecture p. 135–150 | Draw the attention + prefill/decode diagram from memory `[—]` |
| 6 | Nov 30 | Model Size p. 151–168 (scaling laws, Chinchilla) | Compute: params → memory, Chinchilla token budget `[—]` |
| 7 | Dec 7 | Post-Training p. 169–186 (SFT p. 173, preference finetuning p. 179) | Explain RLHF vs DPO in 5 sentences `[—]` |
| 8 | Dec 14 | Sampling p. 187–231 (strategies 191, test-time compute 199, structured outputs 206, probabilistic nature 214). Heavy week: 45 pages | Temperature/top-k/top-p from logits in NumPy `[—]` · the same knobs on a real model `[local]` · structured output with a pydantic schema via an OpenAI-compatible SDK `[API]`, served as a `/extract` endpoint in the B2 FastAPI app · **Ch 2 exam**. **⚑ API decision** (see below) |

## Month 3 — Chapter 3: Evaluation Methodology (p. 232–314) · M 08:37
| 9 | Dec 21 | Challenges p. 234–239 · Language Modeling Metrics p. 240–251 | Entropy / cross-entropy / perplexity with GPT-2 via HF (needs logprobs, p. 195–196) `[local]` |
| 10 | Dec 28 | Exact Evaluation p. 252–270 · AI as a Judge p. 271–280 | Exact match, BLEU/ROUGE `[—]` · embedding similarity with `sentence-transformers` `[local]` · generate answers `[API]` · expose the scorers as a `/score` endpoint |
| 11 | Jan 4 | AI as a Judge p. 281–294 (limitations 281) · Comparative Evaluation p. 295–314 | AI judge: **measure position bias** by swapping order `[API]` · **Ch 3 exam** |

## Month 4 — Chapter 4: Evaluate AI Systems (p. 315–415) · M 14:50
| 12 | Jan 11 | Evaluation Criteria p. 316–338 (domain-specific 319, generation 324) | Write a rubric for a real task `[—]` |
| 13 | Jan 18 | Instruction-Following p. 339–350 · Cost and Latency p. 351–354 | Measure TTFT/latency/cost across small, medium, and large models `[API]` |
| 14 | Jan 25 | Model Selection p. 355–392 (workflow 356, build vs buy 359, benchmarks 377) | Model-selection memo: hard vs soft attributes `[—]` |
| 15 | Feb 1 | Design Your Evaluation Pipeline p. 393–415 | Eval pipeline v1 + **bootstrap reliability check** `[API]` · runs in CI and **fails the build if the score drops** · `/eval` endpoint returns the scores · **Ch 4 exam** |

## Month 5 — Chapter 5: Prompt Engineering (p. 416–493) · M 23:13
| 16 | Feb 8 | Introduction to Prompting p. 417–430 · Clear Instructions p. 432 · Sufficient Context p. 440 (to p. 441) | Prompts stored as versioned files, not in code `[—]` |
| 17 | Feb 15 | Break Tasks p. 442 · Time to Think p. 448 · Iterate p. 452 · Tools p. 453 · Organize & Version p. 458 (to p. 461) | A/B two prompts through your eval pipeline `[API]` |
| 18 | Feb 22 | Defensive Prompt Engineering p. 462–493 | Red-team your own app: violation rate vs false-refusal rate `[API]` · **Ch 5 exam** |

## Months 5–6 — Chapter 6: RAG and Agents (p. 494–593) · M 30:20 (RAG), 36:56 (Agents)
| 19 | Mar 1 | RAG Architecture p. 498 · Retrieval Algorithms p. 500–519 | **Capstone start** as a **FastAPI** service (`/search` endpoint): BM25 retriever over this book's .md, from scratch, with a **Dockerfile from day one** `[—]` |
| 20 | Mar 8 | Retrieval Optimization p. 520–529 · RAG Beyond Texts p. 530–534 | Embeddings + hybrid search `[local]`; retrieval eval (recall@k) `[—]`; answer generation `[API]` · rebuild the same RAG in **LangChain**, compare recall@k + code size (Book p. 892–893: build without an orchestrator first) |
| 21 | Mar 15 | Agent Overview p. 536 · Tools p. 540 · Planning p. 546–560 | Tool-use agent with 2 of *your own* tools `[API]` |
| 22 | Mar 22 | Planning p. 561–575 · Agent Failure Modes & Evaluation p. 576 · Memory p. 581–593 | Agent eval + memory `[API]` · port the agent to **LangGraph**, same eval, compare debuggability · **Ch 6 exam** |

## Month 7 — Chapter 7: Finetuning (p. 594–693) · M 43:02
| 23 | Mar 29 | Finetuning Overview p. 596 · When to Finetune p. 601–617 | Decision memo: prompt vs RAG vs finetune for 3 cases `[—]` |
| 24 | Apr 5 | Memory Bottlenecks p. 618–637 (memory math 622, numerics 627, quantization 631) | Compute training/inference memory by hand, then verify on a real model `[local]` |
| 25 | Apr 12 | Parameter-Efficient Finetuning p. 638–663 (LoRA) | LoRA on a small open model (Linux server) `[local]` |
| 26 | Apr 19 | Model Merging p. 664–679 · Finetuning Tactics p. 680–693 | Evaluate your LoRA vs base `[local]` · **Ch 7 exam** |

## Month 8 — Chapter 8: Dataset Engineering (p. 694–772) · M 52:43
| 27 | Apr 26 | Data Curation p. 697–725 | Data-quality checklist for your LoRA data `[—]` · Day 7: **`docker compose`** for the capstone: app container + a database container for weak spots |
| 28 | May 3 | Data Augmentation and Synthesis p. 726–754 (AI-powered 738, distillation 753) | Synthetic dataset + AI-judge filtering `[API]` (the Batch API cuts this cost by 50%) |
| 29 | May 10 | Data Processing p. 755–772 (inspect, dedup 759, clean, format) | Dedup (exact + near-dup) pipeline `[—]` · **Ch 8 exam** |

## Month 8–9 — Chapter 9: Inference Optimization (p. 773–851) · M 59:45
| 30 | May 17 | Understanding Inference Optimization p. 775–807 (metrics 784, accelerators 796) | Benchmark TTFT/TPOT/throughput on a local model `[local]` |
| 31 | May 24 | Model Optimization p. 808–832 (compression, speculative decoding, attention/KV cache) | Quantized vs full model: speed + quality `[local]` |
| 32 | May 31 | Inference Service Optimization p. 833–851 (batching, prefill/decode, prompt caching, parallelism) | Batching with vLLM on the server, run from its **official Docker image** with GPU passthrough `[local]` · prompt caching: measure the cost drop `[API]` · **Ch 9 exam** |

## Month 9 — Chapter 10: Architecture & User Feedback (p. 852–931) · M 01:08:53
| 33 | Jun 7 | Architecture Steps 1–4 p. 853–874 (context 854, guardrails 856, router & gateway 863, caches 871) | Add guardrails + model router + cache to the capstone `[API]` · create the **AWS** account now (new-account credits expire, so not earlier) |
| 34 | Jun 14 | Agent Patterns p. 875 · Monitoring & Observability p. 877 · Pipeline Orchestration p. 890 (to p. 893) | Logging + monitoring for the capstone `[API]` · **deploy the container to AWS**, logs to CloudWatch |
| 35 | Jun 21 | User Feedback p. 894–929 (conversational 895, design 907, limitations 921) · Epilogue p. 930 | Feedback collection in the capstone `[API]` · **Ch 10 exam** |

## Capstone & mastery check
| 36–38 | Jun 28 – Jul 18 | Re-read your cheat sheets | Finish the **study agent** (see Capstone below) · CD: deploy on every merge to `main` · **run it live 1 week** and write up incidents from the logs · design doc `[API]` |
| 39 | Jul 19 | — | **Final exam** (full book) + a final mock system-design interview + retrospective |

## ⚑ Week 8 — API decision (deferred on purpose)
Choose the cheapest option that still supports what Weeks 8–38 need: **structured outputs, tool use, streaming, prompt caching, token usage in responses, and a spend limit**.
Candidates: Claude API · a cheaper provider · `claude -p` (free on Max, but no own tools, raw timing, or cache control) · local open models only.

### Estimated cost: same workload on 3 providers
The workload is 7,550 calls. Prices were fetched 2026-09-26 (uncached input, $ per 1M tokens); **re-check at Week 8**. Script: `code/cost_estimate.py`.

| Role | Claude | Gemini | DeepSeek (peak) |
|---|---|---|---|
| Small (default) | Haiku 4.5: $1.00 / $5.00 | 3.1 Flash-Lite: $0.25 / $1.50 | deepseek-flash: $0.30 / $1.20 |
| Judge | Sonnet 5: $2.00 / $10.00 | 3.8 Flash: $1.50 / $7.50 ¹ | V4-Pro: $1.32 / $3.96 |
| Large (W13 only) | Opus 5: $5.00 / $25.00 | 3.1 Pro: $2.00 / $12.00 | V4-Pro: $1.32 / $3.96 |

| Weeks | Task | Calls | Claude | Gemini | DeepSeek |
|---|---|---|---|---|---|
| 8 | Structured outputs + sampling | 300 | $0.60 | $0.17 | $0.15 |
| 10 | Answers for exact-eval set | 200 | $0.26 | $0.07 | $0.07 |
| 11 | Judge position bias (small + judge) | 800 | $3.00 | $1.77 | $1.39 |
| 13 | Latency/cost: small / judge / large | 150 | $1.20 | $0.62 | $0.30 |
| 15 | Eval pipeline: generate + judge | 600 | $2.34 | $1.36 | $1.05 |
| 17 | A/B two prompts + judge | 400 | $1.00 | $0.28 | $0.27 |
| 18 | Red-team attacks | 300 | $0.69 | $0.20 | $0.18 |
| 19–20 | RAG answers + judge | 400 | $3.00 | $1.38 | $1.24 |
| 21–22 | Agent: 100 tasks × 5 turns | 500 | $2.25 | $0.60 | $0.63 |
| 28 | Synthetic data + filtering | 2000 | $4.30 | $1.23 | $1.11 |
| 32 | Prompt caching (priced uncached = upper bound) | 100 | $1.15 | $0.29 | $0.34 |
| 33–38 | Capstone dev/testing + final eval | 1800 | $15.75 | $6.38 | $5.88 |
| | **Planned total** | **7550** | **$35.54** | **$14.35** | **$12.60** |
| | **With 1.5× buffer** | | **≈ $53** | **≈ $22** | **≈ $19** |
| | Cheapest way to run it | | Batch API 50% off bulk jobs → ≈ $40 | **Free tier: $0** ² | Off-peak → **≈ $9.50** ³ |

¹ Gemini 3.x Flash prices double on 2027-01-01 (from $0.75/$3.75). Most API weeks are after that date, so the 2027 price is used.
² Gemini's free tier (checked 2026-09-26; Uzbekistan supported) covers 3.1 Flash-Lite, 3.8/3.5 Flash, 2.5 Pro and 2.5 Flash(-Lite); **3.1 Pro Preview is not free**. No Batch API on the free tier; context caching is free only on 3.8/3.5 Flash. Workarounds: W13 use 2.5 Pro as the large model · W28 spread calls over days · W32 use 3.8 Flash. Rate limits aren't published; check aistudio.google.com/rate-limit (daily limits reset at midnight Pacific = 13:00 Tashkent). On the free tier, *"content used to improve our products"*, so no Mohirdev data.
³ DeepSeek off-peak is exactly half price. Peak is 01:00–04:00 and 06:00–10:00 UTC on weekdays, which is **06:00–09:00 and 11:00–15:00 Tashkent time**. Evenings and weekends are off-peak.

**Week 8 checklist, beyond price:** structured outputs · tool use · streaming · prompt caching · token usage in the response · a hard spend limit or prepaid balance · data policy.
Never send Mohirdev or private data on a free tier, or to any provider your company hasn't approved.
Code tip: DeepSeek's docs say it accepts the Anthropic API format, so one SDK could talk to both. Verify this at Week 8.
Job-market note [Beyond the book]: job ads split about evenly between OpenAI and Anthropic (roadmap video 05:52), so the provider barely matters for hiring. DeepSeek and Gemini both offer OpenAI-compatible endpoints, so the cheap option can still use the OpenAI SDK. Verify at Week 8.

## Capstone: study agent (decided 2026-10-10)
Not a "chat with a PDF" demo: the agent **takes actions**. It answers from the book with page cites (RAG), generates quizzes from given pages, grades a `notes/` file against the book, stores weak spots in a DB, and schedules reviews. FastAPI service · LangGraph agent · eval set in CI · guardrails (refuse off-topic, never leak the system prompt) · Docker · AWS · 1 week of real use (yours).

## Rules for the plan
- If a week slips, we move forward, not skip. Weekly quizzes show when to slow down.
- **Why `[local]` in Ch 3, 7, and 9:** hosted APIs don't give logprobs (Book p. 196, 369) or weights, so perplexity, LoRA, quantization, and batching need a model you run yourself.
- **[Beyond the book]:** newer Claude models (Opus 4.7+, Sonnet 5, Opus 5) reject `temperature`/`top_p`/`top_k`, while Haiku 4.5 still accepts them. The book was written before this change.
