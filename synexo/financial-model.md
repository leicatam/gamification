# Synapep — Financial Model (v0.4)

> Currency: USD. Model for the **AI-personalised aesthetic medical device** business: an
> applicator **device** placed in clinics + recurring **personalised treatment kits**
> (razor-and-blades). Illustrative projections, not guarantees.

## 1. Unit economics

### 1.1 Treatment kit (the recurring "blade")

Kit price ≈ **$30–35 ex-factory** (base $32.50). Cost formula unchanged from prior model:

```
COGS / kit = (10% × EXW) + material cost + (10% × EXW) = 20% × EXW + material
           = $6.50 + $4.50 = $11.00   →   GP $21.50/kit, 66.2% margin
```

| EXW | COGS | GP/kit | GM% |
|----:|-----:|-------:|----:|
| $30.00 | 10.50 | 19.50 | 65.0% |
| $32.50 | 11.00 | 21.50 | 66.2% |
| $35.00 | 11.50 | 23.50 | 67.1% |

### 1.2 Applicator device (the "razor")

ASP **$3,000** per clinic, **40% gross margin** (GP $1,200/device). Sold/placed once per clinic;
low-margin hardware that pulls high-margin recurring kits.

## 2. Volume build (bottom-up by clinics)

Driver = clinics onboarded (Korea first, then Hong Kong) × ~**100–125 kits/clinic/month** at
maturity. This reconciles to the ~50–100K kits/month capacity.

| Driver | 2026 prep | 2027 | 2028 | 2029 | 2030 |
|--------|----------:|-----:|-----:|-----:|-----:|
| Clinics (cumulative) | 0 | 150 | 400 | 700 | 1,000 |
| New clinics (devices sold) | 0 | 150 | 250 | 300 | 300 |
| Treatment kits (000s) | 0 | 148 | 600 | 900 | 1,200 |

## 3. P&L ($ thousands)

| Line | 2026 | 2027 | 2028 | 2029 | 2030 |
|------|-----:|-----:|-----:|-----:|-----:|
| Kit revenue ($32.50) | 0 | 4,810 | 19,500 | 29,250 | 39,000 |
| Device revenue ($3k ASP) | 0 | 450 | 750 | 900 | 900 |
| **Total revenue** | 0 | **5,260** | **20,250** | **30,150** | **39,900** |
| Kit gross profit (66.2%) | 0 | 3,182 | 12,900 | 19,350 | 25,800 |
| Device gross profit (40%) | 0 | 180 | 300 | 360 | 360 |
| **Total gross profit** | 0 | **3,362** | **13,200** | **19,710** | **26,160** |
| Blended gross margin | — | 63.9% | 65.2% | 65.4% | 65.6% |
| OpEx (clinical sales, reg, R&D incl. AI, G&A) `[ASSUMPTION]` | 700 | 2,600 | 6,000 | 8,200 | 10,000 |
| **EBITDA** | (700) | 762 | 7,200 | 11,510 | 16,160 |
| EBITDA margin | — | 14.5% | 35.6% | 38.2% | 40.5% |

## 4. Scenarios (full-year 2029)

| Scenario | Clinics | EXW | Device GM | Revenue | Gross profit |
|----------|--------:|----:|----------:|--------:|-------------:|
| Conservative | ~500 | $30 | 35% | ~$22M | ~$14M |
| **Base** | 700 | $32.50 | 40% | $30.2M | $19.7M |
| Upside | ~850 | $35 | 45% | ~$38M | ~$25M |

## 5. Upside not in the base case (Pillar 3)

Data monetisation — licensing the CodeLife model/insights, physician outcome analytics, R&D
partnerships — is deliberately **excluded** from the base P&L and treated as valuation upside
(see `valuation.md`, Lens B).

## 5b. Multi-market view (same product, more markets)

The base P&L above is the **Korea-anchored** single-line view. A bottom-up **multi-market** model —
the **same** Korean-developed device + CodeLife kit exported across 12 markets (no per-market
product development) — is in [`multimarket-model.md`](./multimarket-model.md) /
`Synapep_MultiMarket_Model.docx`. Because the product (and therefore unit economics) is identical
everywhere, the uplift comes purely from **distribution reach**:

| 2030 metric | Korea-only base | Multi-market: Conservative | Base | Upside |
|---|--:|--:|--:|--:|
| Markets | 1 | 11 (China excl.) | 12 | 12 |
| Clinics | ~1,000 | ~1,167 | ~2,020 | ~2,626 |
| Revenue | $39.9M | ~$35.0M | ~$75.1M | ~$112.2M |
| EBITDA | $16.2M | ~$10.3M | ~$33.0M | ~$55.5M |
| Blended GM | ~65.6% | ~63.8% | ~65.3% | ~66.4% |

Scenarios flex only the **clinic ramp, price and utilisation** — never the product — so margins
are stable and R&D is not duplicated. The Conservative case lands near the Korea-only base but
across 11 markets (less single-country risk). Per-market clinic ramps are assumptions pending
anchor-clinic evidence; kit regulatory class varies by market (see `export-strategy.md`).

## 5c. SKU-portfolio engine (capital efficiency)

Revenue above is driven by the **clinic ramp**; the **product side** is a doctor-originated **SKU
portfolio** built by the regulatory **modification engine** (see `model-clarification.md`). Company
working assumptions: **<3% formulation change, ~3-month cycle, <$30K per SKU**, **~20 SKUs in ~6
months** → **<$600K** total regulatory development for the whole catalog. This sits **inside** the
R&D/regulatory OpEx lines (not additional), and makes the portfolio unusually capital-efficient:
many doctor-personalised SKUs from one master spec + one applicator device family, each a minor
modification rather than a new approval. *(Assumptions to be validated; cosmetic/quasi-drug vs
device routes differ.)*

## 6. Open assumptions to confirm

- **Device ASP / GM** ($3,000 / 40%) — confirm vs the chosen applicator.
- **Clinic ramp** (150 → 1,000) and **kits/clinic/month** (~100–125) vs Korea/HK clinic counts.
- **OpEx** — needs a real headcount/spend plan, including an **AI/data-science team** line.
- **Material cost** ($4.50/kit) and that cold-chain/fill-finish sit inside the COGS formula.
