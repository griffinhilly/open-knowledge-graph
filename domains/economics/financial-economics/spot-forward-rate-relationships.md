---
id: spot-forward-rate-relationships
title: Spot Rates, Forward Rates, and No-Arbitrage Relationships
domain: economics
course: financial-economics
prerequisites:
- id: interest-rate-term-structure
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- interest-rate-swaps-mechanics
- covered-and-uncovered-interest-parity
tags:
- interest-rates
- arbitrage
- forward-contracts
- no-arbitrage
stage: formal-systems
status: draft
---

# Spot Rates, Forward Rates, and No-Arbitrage Relationships

## Core Idea
Spot rates are today's interest rates for lending over specified periods, while forward rates are implicit rates for future lending periods derived from the term structure. No-arbitrage relationships lock in mathematical connections: forward rates must be consistent with spot rates to prevent riskless profit opportunities. These relationships form the foundation for pricing all fixed-income instruments.

## Explainer

From the term structure of interest rates you know that different maturities carry different yields — the yield curve slopes upward, downward, or lies flat depending on expectations and risk premia. From present value discounting you know how to value a single cash flow by dividing it by an appropriate discount factor. Spot and forward rates give precise names to the discount rates being used and show how they must logically relate to each other.

A **spot rate** s(t) is simply today's rate for lending or borrowing over a specific horizon from now until time t. The 2-year spot rate is the yield on a zero-coupon bond that pays $1 in two years; the 5-year spot rate is the same for five years. These rates are the fundamental building blocks — every coupon bond is priced by discounting each of its cash flows at the spot rate for that cash flow's specific maturity. The yield to maturity is a weighted average of these spot rates, which is why YTM changes even when the issuer's credit quality is unchanged but the shape of the spot curve shifts.

A **forward rate** f(t₁, t₂) is the interest rate agreed upon today for lending that will begin at time t₁ and end at time t₂ — it is a rate for a future period, locked in now. Forward rates are not directly observable in the market; they are *implied* by the relationship between spot rates. The key relationship is the **no-arbitrage condition**: lending for two years at the 2-year spot rate must produce the same terminal value as lending for one year at the 1-year spot rate and then reinvesting for a second year at the 1-year forward rate starting at year one. In formula form: (1 + s₂)² = (1 + s₁)(1 + f(1,2)). If this equality did not hold, an arbitrageur could borrow at the cheap side and lend at the expensive side to earn a riskless profit — the no-arbitrage logic forces the equation to hold exactly.

This connection is what makes forward rates useful for fixed-income pricing and monetary policy analysis. If the yield curve is upward-sloping, the implied forward rates are higher than the current short rate — the curve embeds the expectation (or compensation for risk) that short rates will rise. Central bankers and traders use forward rate curves extracted from Treasury yields to infer market expectations about the path of policy rates. An important caveat: forward rates are not pure forecasts of future spot rates. They bundle together expected future rates, **term premia** (compensation for the uncertainty of holding long-duration instruments), and convexity adjustments. Disentangling these components requires additional model assumptions, which is why interpreting forward curves is more art than arithmetic.
