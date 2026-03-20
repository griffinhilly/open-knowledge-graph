---
id: merger-arbitrage-valuation
title: Merger Arbitrage and Deal Valuation
domain: economics
course: financial-economics
prerequisites:
- id: enterprise-value-calculation
  type: hard
builds-toward:
- market-anomalies-and-puzzles
tags:
- m&a
- arbitrage
- valuation
- risk
stage: advanced
status: draft
---

# Merger Arbitrage and Deal Valuation

## Core Idea
Merger arbitrage involves buying an acquisition target at a discount to deal price, betting the deal closes. The discount compensates for deal completion risk (regulatory rejection, financing failure, renegotiation). Target stocks trade below deal price by an amount reflecting deal risk premium, completion probability, and time to closing. Arbitrageurs profit by accurately estimating risk and pricing it.

## Explainer

When a company announces it will acquire another at $50 per share, the target's stock — which might have been trading at $32 before the announcement — typically jumps to around $47 or $48 rather than all the way to $50. That $2-to-$3 gap is the **merger spread**, and it exists for a simple reason: the deal might not close. Regulatory authorities could block it, the acquirer's financing could fall through, the target's board might reject the terms, or a material adverse change might void the contract. The spread is the market's aggregate estimate of the present value of that deal failure risk.

**Merger arbitrageurs** take the opposite position from the uncertainty: they buy the target at $47, betting the deal closes at $50. If it closes in six months, they earn roughly $3 on a $47 investment over six months — about 6% in six months, or ~13% annualized. This sounds attractive until you realize the loss scenario: if the deal breaks, the target's stock typically collapses back toward its pre-announcement price of ~$32, a loss of roughly $15 on the same investment. The payoff profile is therefore **asymmetric**: a small frequent gain when deals succeed, a large occasional loss when they fail. The expected return is positive only if the arbitrageur prices deal risk accurately enough that the spread compensates for the loss probability.

Formally, if *p* is the probability the deal closes, and the closing price is $50 while the break price (stock price if deal fails) is $32, then the fair value of the target today is: V = p × $50 + (1 - p) × $32. If the market sets the price at $47, we can back out the implied probability: $47 = p × $50 + (1 - p) × $32 → p = ($47 - $32) / ($50 - $32) ≈ 83%. The arbitrageur who thinks the actual completion probability is higher than 83% should buy; one who thinks it is lower should avoid or short the spread. Enterprise value calculation is central here — in a stock-for-stock deal, the "deal price" moves with the acquirer's stock price, and the arbitrageur must also model the acquirer's value to assess the real spread.

The main deal risks to assess are: **regulatory risk** (antitrust and sector-specific approvals, which are public and quantifiable via regulatory timelines), **financing risk** (debt-financed deals can fail if credit markets seize), **shareholder vote risk** (especially for the acquirer in stock deals), and **material adverse change (MAC) clauses** (which allow the acquirer to walk away if the target's business deteriorates significantly before closing). Experienced merger arbitrageurs develop expertise in reading regulatory precedent and financing documentation rather than primarily in fundamental equity analysis — the valuation work was done when the deal was announced; the arbitrage is a bet on execution. The strategy earns persistent positive returns as compensation for bearing the concentrated, positively-skewed loss risk that other investors prefer to avoid.
