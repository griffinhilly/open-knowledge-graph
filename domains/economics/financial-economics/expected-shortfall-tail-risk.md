---
id: expected-shortfall-tail-risk
title: Expected Shortfall and Tail Risk Measurement
domain: economics
course: financial-economics
prerequisites:
- id: value-at-risk-measurement
  type: hard
- id: risk-and-return-tradeoff
  type: soft
builds-toward:
- risk-and-return-tradeoff
tags:
- risk-management
- var
- tail-risk
- measurement
stage: formal-systems
status: draft
---

# Expected Shortfall and Tail Risk Measurement

## Core Idea
Expected shortfall (ES) or conditional value-at-risk measures the expected loss in the tail beyond the VaR threshold, addressing VaR's key weakness: it ignores loss severity. ES = E[Loss | Loss > VaR], and is coherent, satisfying desirable risk measure properties that VaR violates. ES is increasingly preferred for capital allocation and stress testing in regulated financial institutions.

## How It's Best Learned
Calculate both VaR and ES for a portfolio at the same confidence level and observe how ES better captures tail risk from extreme scenarios.

## Explainer

From your study of Value at Risk, you know that VaR at a given confidence level (say 99%) answers the question: what is the worst loss I can expect on 99% of trading days? If a portfolio's 1-day 99% VaR is $5 million, it means losses will exceed $5 million only 1% of the time. This is a useful threshold measure — it tells you the cutoff point where the tail begins. But VaR says nothing about what happens *inside* that worst 1% of scenarios. A portfolio could have a 99% VaR of $5 million with a maximum possible loss of $6 million (a mild tail), or with a maximum possible loss of $500 million (a catastrophic tail). The VaR number is identical in both cases.

**Expected shortfall (ES)**, also called **conditional value at risk (CVaR)**, fixes this blind spot by asking: given that we are in the worst 1% of scenarios, what is the average loss? Formally, ES at the α confidence level equals E[Loss | Loss > VaR_α] — the expected value of the loss distribution, conditional on losses exceeding the VaR threshold. This turns the threshold into a window: instead of just marking where the tail begins, ES integrates over the entire tail and reports its average severity. Using the rain analogy from risk-return: VaR tells you there is a 1% chance of more than 2 inches of rain; ES tells you that when it does exceed 2 inches, it averages 3.5 inches.

The technical importance of ES over VaR relates to a property called **coherence**. A coherent risk measure satisfies four axioms that any reasonable measure of portfolio risk should obey; the most practically important is **subadditivity** — the risk of a combined portfolio should be no greater than the sum of the risks of its parts. Subadditivity formalizes the principle that diversification reduces risk. VaR violates subadditivity: it is mathematically possible to construct two portfolios such that their individual VaRs are low but their combined VaR is high, implying that merging them increases measured risk. This is not just a theoretical curiosity — it could incentivize institutions to split portfolios to game capital requirements. ES is subadditive and passes all four coherence axioms, making it a more defensible basis for capital allocation and risk aggregation across business units.

In practice, ES is computed differently depending on whether you use a **parametric** or **historical simulation** approach. Under a parametric normal distribution, ES has a closed-form expression: at the 99% confidence level, ES = μ + σ × φ(z_α)/α, where φ is the normal PDF and z_α is the critical value. Under historical simulation, you identify all scenarios in the worst 1% of the historical return distribution and average their losses — no distributional assumption needed. Under a fat-tailed distribution (like a Student-t, which better describes financial returns), both VaR and ES are larger than the normal distribution predicts, with ES being more sensitive to the tail shape. This sensitivity to tail structure is both ES's strength (it reflects catastrophic scenarios more accurately) and a practical challenge (tail distributions are hard to estimate with limited historical data). Regulators, including the Basel III/IV framework, have shifted from VaR to ES for bank capital requirements precisely because ES forces institutions to confront — and hold capital against — the severity of extreme losses, not just their probability.
