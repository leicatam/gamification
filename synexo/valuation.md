# Synapep — Valuation (Draft v0.1)

> All figures USD, illustrative, base case from `financial-model.md` (EXW $32.50, material
> $6.00 `[ASSUMPTION]`, ramp to 75% capacity by 2029). Valuation date: mid-2026 (pre-revenue).

## Headline

Synapep today is a **pre-revenue, pre-product company** raising **$1.0M** to kick off. Two
numbers matter and they are deliberately different:

1. **What to price *this* round at:** **$3–4M pre-money / $4–5M post-money** — $1.0M buys
   ~20–25%. This is the defensible seed price.
2. **The prize if it executes:** a risk-*un*adjusted enterprise value of **~$25–35M** by
   ~2030–31 on the base-case model. This is the upside story, not today's price.

The gap between the two is normal early-stage risk discounting; the methods below show how
both are derived and why they reconcile.

---

## Method 1 — Seed-stage convention (what comparable rounds price at)

A pre-revenue company with proprietary AI + a credible path to manufacturing typically raises
its first institutional/angel money at a **$2–5M pre-money** valuation. Drivers that push
Synapep toward the **upper** half: differentiated AI IP (IT-exo, ai.peptide), a concrete
product line (5–6 SKUs), near-term revenue (Feb 2027), and high gross margins. Drivers that
pull **down**: unproven demand, undefined regulatory path, unspecified material cost, team not
yet named.

**Net: $3–4M pre-money is a fair, raiseable price for the $1M kickoff.**

| Pre-money | Raise | Post-money | Investor % |
|----------:|------:|-----------:|-----------:|
| $3.0M | $1.0M | $4.0M | 25.0% |
| $3.5M | $1.0M | $4.5M | 22.2% |
| $4.0M | $1.0M | $5.0M | 20.0% |

---

## Method 2 — Discounted cash flow (the "if it works" enterprise value)

Base-case EBITDA, converted to a simplified free cash flow (after HK profits tax ~16.5%,
working-capital build, and modest capex), discounted at **40%** (early-stage cost of capital).

| $000s | 2027 | 2028 | 2029 | 2030 | 2031 |
|-------|-----:|-----:|-----:|-----:|-----:|
| EBITDA | 560 | 6,000 | 9,500 | 13,500 | 14,000 |
| ≈ Free cash flow | 300 | 4,000 | 6,500 | 10,000 | 11,000 |
| Discount factor @40% | 0.714 | 0.510 | 0.364 | 0.260 | 0.186 |
| PV of FCF | 214 | 2,041 | 2,369 | 2,603 | 2,046 |

- **PV of explicit FCF (2027–31): ≈ $9.3M**
- **Terminal value** (exit end-2031 at **8× EBITDA** = $112M) → PV = $112M × 0.186 ≈ **$20.8M**
- **Enterprise value (DCF) ≈ $30M** *(un-risk-adjusted — assumes full execution)*

Risk-adjustment for a pre-revenue company (probability of reaching the base case ≈ **15%**):
**$30M × 0.15 ≈ $4.5M** — which lands right on top of the seed-convention price above.

---

## Method 3 — Forward revenue / EBITDA multiple (cross-check)

| Basis (2029, base case) | Value | Metric | EV (2029) |
|-------------------------|------:|-------:|----------:|
| Revenue $29.25M | × 2–4× | specialty/AI peptide | $58.5M – $117M |
| EBITDA $9.5M | × 6–10× | | $57M – $95M |

Discount a ~$60–95M 2029 EV back ~3 years at 40% (÷2.744) → **$21M – $35M** present
(un-risk-adjusted). Risk-adjusted ×15–25% → **$3.2M – $8.7M** — again consistent with a
$3–4M pre-money entry.

---

## Reconciliation

| Method | Un-risk-adjusted | Risk-adjusted | Implication for today's round |
|--------|-----------------:|--------------:|-------------------------------|
| Seed convention | — | $3–4M | direct |
| DCF | ~$30M (EV) | ~$4.5M | matches |
| Forward multiple | $21–35M (PV of EV) | $3–9M | matches |

**Recommendation: price the $1.0M kickoff at $3–4M pre-money ($4–5M post).** Present the
$25–35M execution case as the investor's upside, not the entry price.

---

## VC-method check (does the investor get a return?)

A seed investor seeking ~10× wants ~$10M back. If Synapep exits ~2031 around **$80–112M**
(8× EBITDA) and the seed stake is diluted ~2× by a 2028 Series A, the investor needs roughly
**18–25% today** to clear 10×. $1M at $3–4M pre-money gives **20–25%** — so the math works.

---

## How material cost moves the valuation

Because valuation is anchored to base-case cash flows, the unspecified material cost flows
straight through. Holding everything else at base case and re-running 2029:

| Material $/vial | 2029 GM% | 2029 GP | Rough EV impact |
|----------------:|---------:|--------:|-----------------|
| 4.00 | 67.7% | ~$19.8M | upside case, EV toward high end |
| 6.00 (base) | 61.5% | ~$18.0M | base ~$30M EV (un-adj.) |
| 9.00 | 52.3% | ~$15.3M | conservative, EV ~20–25% lower |
| 12.00 | 43.1% | ~$12.6M | margin-pressured, revisit raise size |

> **Bottom line:** the $3–4M pre-money recommendation is robust across the margin range
> because seed pricing is set more by stage/risk than by a model that is itself built on an
> assumed cost. Once you give the real material cost, the *upside* numbers (Methods 2 & 3)
> tighten, but the recommended **entry** price for the $1M round stays ~$3–4M pre.
