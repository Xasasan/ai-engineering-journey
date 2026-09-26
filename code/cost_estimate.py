# Estimate course API cost per provider. Run: python3 code/cost_estimate.py
# Prices are $ per 1M tokens (input, output), cache-miss / uncached, fetched 2026-09-26 -- re-check at Week 8.
# Tiers: "small" = cheap default model, "judge" = stronger model for AI-as-judge, "large" = top model (W13 comparison only)
PROVIDERS = {
    "Claude": {"small": ("Haiku 4.5", 1.00, 5.00),
               "judge": ("Sonnet 5", 2.00, 10.00),
               "large": ("Opus 5", 5.00, 25.00)},
    # Gemini 3.x Flash prices double on 2027-01-01; most API weeks are after that, so use the 2027 price
    "Gemini": {"small": ("3.1 Flash-Lite", 0.25, 1.50),
               "judge": ("3.8 Flash (2027 price)", 1.50, 7.50),
               "large": ("3.1 Pro", 2.00, 12.00)},
    # DeepSeek peak price (worst case); off-peak is exactly half
    "DeepSeek": {"small": ("deepseek-flash", 0.30, 1.20),
                 "judge": ("V4-Pro", 1.32, 3.96),
                 "large": ("V4-Pro", 1.32, 3.96)},
}
# (weeks, task, tier, calls, input_tokens_per_call, output_tokens_per_call)
TASKS = [
    ("8",     "structured outputs + sampling tests",   "small", 300,   500, 300),
    ("10",    "generate answers for exact-eval set",   "small", 200,   300, 200),
    ("11",    "judge position bias (small)",           "small", 400,  1500, 200),
    ("11",    "judge position bias (judge, compare)",  "judge", 400,  1500, 200),
    ("13",    "latency/cost: small",                   "small",  50,   500, 500),
    ("13",    "latency/cost: judge",                   "judge",  50,   500, 500),
    ("13",    "latency/cost: large",                   "large",  50,   500, 500),
    ("15",    "eval pipeline: generate",               "small", 300,   800, 400),
    ("15",    "eval pipeline: judge",                  "judge", 300,  1500, 200),
    ("17",    "A/B two prompts",                       "small", 200,  1000, 300),
    ("17",    "A/B judge",                             "small", 200,  1500, 200),
    ("18",    "red-team attacks",                      "small", 300,   800, 300),
    ("19-20", "RAG answers over book",                 "small", 300,  4000, 400),
    ("19-20", "RAG judge",                             "judge", 100,  5000, 200),
    ("21-22", "agent: 100 tasks x 5 turns",            "small", 500,  3000, 300),
    ("28",    "synthetic data generation",             "small", 1000,  500, 500),
    ("28",    "AI-judge filtering",                    "small", 1000,  800, 100),
    ("32",    "prompt caching (priced uncached)",      "small", 100, 10000, 300),
    ("33-38", "capstone dev + testing",                "small", 1500, 5000, 500),
    ("33-38", "capstone final eval judge",             "judge", 300,  6000, 300),
]
BUFFER = 1.5  # bugs, retries, re-runs

def cost(prices, tier, calls, tin, tout):
    _, pin, pout = prices[tier]
    return calls * (tin * pin + tout * pout) / 1e6  # tokens x $/token

assert abs(cost(PROVIDERS["Claude"], "small", 1_000_000, 1, 0) - 1.0) < 1e-9  # 1M input tokens on Haiku = $1

totals = {}
print(f"{'Weeks':<7}{'Task':<38}" + "".join(f"{p:>10}" for p in PROVIDERS))
for w, t, tier, n, i, o in TASKS:
    row = [cost(PROVIDERS[p], tier, n, i, o) for p in PROVIDERS]
    for p, c in zip(PROVIDERS, row):
        totals[p] = totals.get(p, 0) + c
    print(f"{w:<7}{t:<38}" + "".join(f"{c:>10.2f}" for c in row))
print(f"{'':<7}{'TOTAL planned':<38}" + "".join(f"{totals[p]:>10.2f}" for p in PROVIDERS))
print(f"{'':<7}{'x1.5 buffer':<38}" + "".join(f"{totals[p]*BUFFER:>10.2f}" for p in PROVIDERS))
print(f"\nCalls: {sum(t[3] for t in TASKS)}.  DeepSeek off-peak = half: ${totals['DeepSeek']*BUFFER/2:.2f} with buffer.")
