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
stage: formal-systems
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

## Questions

```yaml
- question: "A perpetuity pays $200 per year forever. If the discount rate is 4%, what is its present value?"
  type: multiple-choice
  options:
    - "$800"
    - "$5,000"
    - "$4,800"
    - "$200"
  answer: 1
  explanation: "PV = C/r = 200 / 0.04 = $5,000. This is the perpetuity formula derived by summing the infinite geometric series of discounted cash flows. Intuitively, $5,000 invested at 4% earns exactly $200 per year forever — so $5,000 today is precisely equivalent to this perpetuity. Option A ($800) might come from multiplying C × r instead of dividing; the other options reflect different confusions with the formula."

- question: "An investor tries to apply the growing perpetuity formula PV = C/(r−g) to value a stock with dividends growing at 8% per year and a discount rate of 6%. What is the problem?"
  type: multiple-choice
  options:
    - "The formula only applies to finite annuities, not perpetuities"
    - "The growth rate (8%) exceeds the discount rate (6%), making r−g negative and the formula economically meaningless"
    - "The first dividend payment must always be discounted separately before applying the formula"
    - "The formula requires that g = 0; a separate formula handles growth"
  answer: 1
  explanation: "When g ≥ r, the denominator r−g becomes zero or negative, producing an infinite or negative present value — which has no economic meaning. The formula assumes that faster growth is partially offset by discounting, converging to a finite sum only when r > g. Economically, a cash flow stream growing faster than your discount rate forever would be worth infinite money today, which cannot exist in a finite economy. The condition r > g is not a mathematical technicality; it is the economically meaningful boundary."

- question: "A perpetuity paying the same amount forever has a finite present value because distant cash flows are so heavily discounted they contribute negligible value."
  type: true-false
  answer: true
  explanation: "This is correct and is the intuition behind the formula PV = C/r. Each payment C/(1+r)^t shrinks geometrically as t increases. Distant payments (t = 100, 200, …) are discounted to near-zero present value. The infinite series C/(1+r) + C/(1+r)² + … converges to a finite number C/r because the ratio 1/(1+r) is less than 1. An apparently paradoxical 'infinite payments = finite value' is resolved by the logic of compounding."

- question: "The growing perpetuity formula PV = C/(r−g) is valid as long as the growth rate g is positive."
  type: true-false
  answer: false
  explanation: "The formula requires r > g, not merely g > 0. A positive g that still satisfies r > g (e.g., r = 8%, g = 5%) is fine. But a growth rate exceeding the discount rate (g ≥ r) makes the denominator zero or negative, yielding an undefined or negative present value. The intuition: if payments grow faster than they are discounted, the present value of future payments never shrinks enough to converge, and the sum is infinite."

- question: "Explain intuitively why a perpetuity — an infinite stream of payments — has a finite present value. Why does the formula give PV = C/r?"
  type: short-answer
  answer: "Distant payments are discounted so heavily they become negligible. The stream C/(1+r), C/(1+r)², C/(1+r)³, … is a geometric series with ratio 1/(1+r) < 1, which converges to a finite sum. Applying the geometric series formula gives PV = [C/(1+r)] / [1 − 1/(1+r)] = C/r. Alternatively: if you invest PV = C/r today at interest rate r, you earn C each period and never touch the principal — so C/r is exactly the amount needed to replicate the perpetuity, confirming the formula."
  explanation: "The formula's elegance is that an infinite stream of future cash flows collapses to a single ratio. This is why perpetuity pricing appears throughout finance: preferred stock dividends, government consols, endowment payouts, and the Gordon Growth Model all rest on variants of this formula."
```

## Explainer

You already know how to discount a single future cash flow back to present value: divide by (1+r)^t. An annuity and a perpetuity are simply organized collections of such cash flows — the intellectual challenge is finding a compact formula instead of summing thousands of individual discounting calculations.

Start with a **perpetuity**: a payment of $C every period, forever. In year 1 you receive C/(1+r), in year 2 you receive C/(1+r)², in year 3 you receive C/(1+r)³, and so on forever. This is a geometric series with first term C/(1+r) and ratio 1/(1+r). From your geometric series prerequisite, you know the sum of an infinite geometric series a + ar + ar² + … = a/(1−r) whenever |r| < 1. Applying this formula gives PV = [C/(1+r)] / [1 − 1/(1+r)] = C/r. The elegance is striking: an infinite stream of payments collapses to a single fraction. A UK government consol paying £50 per year when the discount rate is 5% is worth exactly £1,000 — nothing more to compute.

An **annuity** is a perpetuity that stops after T periods. You can obtain its formula by thinking of the annuity as a perpetuity starting today minus a perpetuity starting at time T (whose value today is discounted back T periods): PV = C/r − [C/r] × 1/(1+r)^T = C × [1 − (1+r)^(−T)] / r. The bracketed term is the **annuity factor** — a number between 0 and 1 that scales the perpetuity value down for finite lives. Mortgage calculations are annuity problems in disguise: you borrow a lump sum PV today and repay equal monthly amounts C over 30 years; solving for C given PV, r, and T gives the monthly payment formula used by every bank.

The **growing perpetuity** extends the model to payments that grow at rate g each period: C in period 1, C(1+g) in period 2, C(1+g)² in period 3. Discounting each and summing the resulting geometric series (now with ratio (1+g)/(1+r)) yields PV = C/(r−g), valid only when r > g. This formula is the foundation of the **Gordon Growth Model** for stock valuation, which you will encounter next. Intuitively, faster growth means more valuable future payments, so the denominator shrinks and the value rises. But when g approaches r, the denominator approaches zero and value approaches infinity — growth cannot exceed the discount rate forever in a finite economy, so this boundary is economically meaningful, not just a mathematical quirk.
