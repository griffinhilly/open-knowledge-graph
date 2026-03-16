---
id: annuities-and-perpetuities
title: Annuities and Perpetuities
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: geometric-series
  type: soft
- id: geometric-sequences-and-series
  type: soft
- id: future-value-and-compounding
  type: soft
builds-toward:
- bond-pricing
- dividend-discount-model
tags:
- annuity
- perpetuity
- cash-flow-streams
- gordon-growth
stage: abstract-reasoning
status: validated
---
# Annuities and Perpetuities

## Core Idea
An annuity is a series of equal cash flows paid at regular intervals; its present value is PV = C × [1 − (1+r)^(−t)] / r. A perpetuity pays equal cash flows forever and has the elegantly simple formula PV = C/r, derived by taking the annuity formula to the limit as t → ∞. A growing perpetuity, where payments grow at constant rate g, gives PV = C/(r−g), the foundation of the Gordon Growth Model for equity valuation. These formulas are derived by summing geometric series and appear throughout finance in pricing bonds, mortgages, preferred stock, and endowments.

## How It's Best Learned
Derive the perpetuity formula as the limit of the annuity formula to see where C/r comes from. Apply annuity formulas to compute monthly mortgage payments and retirement income streams. Recognize the growing perpetuity as a direct precursor to dividend discount stock valuation.

## Common Misconceptions
- Perpetuities seem impractical but government consols and preferred stocks closely approximate them in real markets.
- The growing perpetuity formula breaks down entirely when g ≥ r, producing negative or infinite values — students must check this condition before applying.

## Explainer

You already know how to discount a single future cash flow back to present value: divide by (1+r)^t. An annuity and a perpetuity are simply organized collections of such cash flows — the intellectual challenge is finding a compact formula instead of summing thousands of individual discounting calculations.

Start with a **perpetuity**: a payment of $C every period, forever. In year 1 you receive C/(1+r), in year 2 you receive C/(1+r)², in year 3 you receive C/(1+r)³, and so on forever. This is a geometric series with first term C/(1+r) and ratio 1/(1+r). From your geometric series prerequisite, you know the sum of an infinite geometric series a + ar + ar² + … = a/(1−r) whenever |r| < 1. Applying this formula gives PV = [C/(1+r)] / [1 − 1/(1+r)] = C/r. The elegance is striking: an infinite stream of payments collapses to a single fraction. A UK government consol paying £50 per year when the discount rate is 5% is worth exactly £1,000 — nothing more to compute.

An **annuity** is a perpetuity that stops after T periods. You can obtain its formula by thinking of the annuity as a perpetuity starting today minus a perpetuity starting at time T (whose value today is discounted back T periods): PV = C/r − [C/r] × 1/(1+r)^T = C × [1 − (1+r)^(−T)] / r. The bracketed term is the **annuity factor** — a number between 0 and 1 that scales the perpetuity value down for finite lives. Mortgage calculations are annuity problems in disguise: you borrow a lump sum PV today and repay equal monthly amounts C over 30 years; solving for C given PV, r, and T gives the monthly payment formula used by every bank.

The **growing perpetuity** extends the model to payments that grow at rate g each period: C in period 1, C(1+g) in period 2, C(1+g)² in period 3. Discounting each and summing the resulting geometric series (now with ratio (1+g)/(1+r)) yields PV = C/(r−g), valid only when r > g. This formula is the foundation of the **Gordon Growth Model** for stock valuation, which you will encounter next. Intuitively, faster growth means more valuable future payments, so the denominator shrinks and the value rises. But when g approaches r, the denominator approaches zero and value approaches infinity — growth cannot exceed the discount rate forever in a finite economy, so this boundary is economically meaningful, not just a mathematical quirk.
