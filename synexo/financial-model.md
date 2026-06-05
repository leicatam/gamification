# Synapep — Financial Model

> Currency: USD. Base case shown; `[ASSUMPTION]` marks an input that was **not provided**
> and must be confirmed. All figures are illustrative projections, not guarantees.

## 1. Unit economics

### 1.1 Cost formula (as given)

> "Manufacturing cost is 10% of ex-factory price, plus the material cost, plus another 10%."

Interpreted as:

```
COGS / vial = (10% × EXW)        ← conversion / manufacturing labor & overhead
            + material cost       ← API peptide + vial + lyophilization + packaging  [ASSUMPTION]
            + (10% × EXW)         ← second 10% (QC / overhead / distribution allowance)
            = 20% × EXW + material cost
```

If "another 10%" was meant as 10% **of the material cost** instead of EXW, the model
changes slightly — please confirm. This draft uses **20% × EXW + material**.

### 1.2 Per-vial economics — base case

Base case: EXW = **$32.50** (midpoint of $30–35), material cost = **$6.00 `[ASSUMPTION]`**.

| Line | $/vial |
|------|-------:|
| Ex-factory price (EXW) | 32.50 |
| – Manufacturing (10% × EXW) | 3.25 |
| – Material cost `[ASSUMPTION]` | 6.00 |
| – Second 10% (10% × EXW) | 3.25 |
| **= COGS** | **12.50** |
| **Gross profit / vial** | **20.00** |
| **Gross margin** | **61.5%** |

### 1.3 Price sensitivity (material held at $6.00)

| EXW price | COGS | GP/vial | GM% |
|----------:|-----:|--------:|----:|
| $30.00 | 12.00 | 18.00 | 60.0% |
| $32.50 | 12.50 | 20.00 | 61.5% |
| $35.00 | 13.00 | 22.00 | 62.9% |

### 1.4 Material-cost sensitivity (EXW held at $32.50) — **the key swing factor**

| Material $/vial | COGS | GP/vial | GM% |
|----------------:|-----:|--------:|----:|
| 4.00 | 10.50 | 22.00 | 67.7% |
| 6.00 (base) | 12.50 | 20.00 | 61.5% |
| 8.00 | 14.50 | 18.00 | 55.4% |
| 10.00 | 16.50 | 16.00 | 49.2% |
| 12.00 | 18.50 | 14.00 | 43.1% |

> **Action:** provide the real per-vial material cost for each of the 5–6 products.
> Until then, treat margins as a range of roughly **43%–68%**.

## 2. Capacity & volume ramp

Capacity is 50–100K vials/month. **Selling, not making, is the constraint in year one.**
The ramp below assumes demand builds gradually after the Feb-2027 launch, reaching
mid-capacity in 2028 and upper-capacity by 2030.

### 2.1 2027 monthly ramp (launch year)

| Month | Vials |
|-------|------:|
| Feb | 2,000 |
| Mar | 4,000 |
| Apr | 6,000 |
| May | 8,000 |
| Jun | 10,000 |
| Jul | 12,000 |
| Aug | 15,000 |
| Sep | 18,000 |
| Oct | 21,000 |
| Nov | 24,000 |
| Dec | 28,000 |
| **2027 total** | **148,000** |

Exit run-rate Dec 2027 = 28K/month ≈ 56% of the 50K floor.

### 2.2 Annual volume

| Year | Avg vials/mo | Vials/yr | % of 100K cap |
|------|-------------:|---------:|--------------:|
| 2027 | ~12,300 (ramp) | 148,000 | — |
| 2028 | 50,000 | 600,000 | 50% |
| 2029 | 75,000 | 900,000 | 75% |
| 2030 | 100,000 | 1,200,000 | 100% |
| 2031 | 100,000 | 1,200,000 | 100% |

## 3. P&L (base case: EXW $32.50, material $6.00, GP $20/vial)

OpEx note: the provided running capital ($400K/yr) covers the lean prep + early launch.
Scaling revenue to $20–39M requires a real commercial organization (sales, regulatory,
QA, R&D for ai.peptide, G&A), so OpEx is built up below and **exceeds** the bare running
capital from 2027 onward — this is why the $1M raise funds the *kickoff*, with a likely
Series A needed in 2028 to fund the scale-up (see valuation).

| $ thousands | 2026 (prep) | 2027 | 2028 | 2029 | 2030 |
|-------------|------------:|-----:|-----:|-----:|-----:|
| Vials sold (000s) | 0 | 148 | 600 | 900 | 1,200 |
| **Revenue** | 0 | 4,810 | 19,500 | 29,250 | 39,000 |
| COGS | 0 | 1,850 | 7,500 | 11,250 | 15,000 |
| **Gross profit** | 0 | 2,960 | 12,000 | 18,000 | 24,000 |
| Gross margin | — | 61.5% | 61.5% | 61.5% | 61.5% |
| OpEx (S&M, R&D, G&A) `[ASSUMPTION]` | 700 | 2,400 | 6,000 | 8,500 | 10,500 |
| **EBITDA** | (700) | 560 | 6,000 | 9,500 | 13,500 |
| EBITDA margin | — | 11.6% | 30.8% | 32.5% | 34.6% |

> 2026 reflects the 6–9 month prep: $500K initial Lab investment (capex/setup, not in EBITDA
> above) plus ~$700K pre-launch operating burn. The $1M raise + the implied own funds carry
> the company from kickoff through the launch ramp.

### 3.1 Cash / funding bridge (first 18 months)

| Use of funds (kickoff, ~$1.0M raise) | $ |
|--------------------------------------|--:|
| Synapep Lab initial investment | 500,000 |
| Running capital, 3 half-years (prep → launch) | 600,000 |
| Buffer / contingency | (covered by revenue from Feb 2027) |
| **Total committed** | **1,100,000** |

The $1.0M raise plus early 2027 gross profit ($2.96M for the year) is sufficient to reach
EBITDA-positive in 2027 **in this base case**. Thinner margins (high material cost) or a
slower ramp would require either a larger raise or a 2028 Series A.

## 4. Scenarios (full-year 2029, the first "steady scale" year)

| Scenario | EXW | Material | Vials/yr | Revenue | GP | GM% |
|----------|----:|---------:|---------:|--------:|---:|----:|
| Conservative | $30 | $9 | 720,000 (60% cap) | $21.6M | $9.0M | 41.7% |
| **Base** | $32.50 | $6 | 900,000 (75% cap) | $29.25M | $18.0M | 61.5% |
| Upside | $35 | $5 | 1,080,000 (90% cap) | $37.8M | $24.5M | 64.9% |

These three columns are the inputs that drive the valuation range in `valuation.md`.
