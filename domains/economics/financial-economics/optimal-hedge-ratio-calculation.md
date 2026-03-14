---
id: optimal-hedge-ratio-calculation
title: Optimal Hedging Ratios and Hedge Effectiveness
domain: economics
course: financial-economics
prerequisites:
- id: futures-and-forward-contracts
  type: hard
- id: portfolio-diversification
  type: soft
builds-toward:
- portfolio-insurance-strategy
tags:
- hedging
- derivatives
- risk-management
- optimization
stage: formal-systems
status: draft
---

# Optimal Hedging Ratios and Hedge Effectiveness

## Core Idea
The optimal hedge ratio minimizes the variance of a hedged position: h* = ρ(σ_spot/σ_futures) where ρ is the correlation between spot and futures price changes. Perfect hedges (ρ = 1, matched maturities) eliminate all price risk, while imperfect hedges leave basis risk. Calculating optimal ratios requires understanding the correlation between the asset being hedged and available derivatives.
