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

## Explainer

You know from your study of futures and forward contracts that a hedge works by taking an offsetting position: if you own an asset and fear a price drop, you sell futures contracts so that gains on the short futures position offset losses on the underlying. The question the optimal hedge ratio answers is: how many futures contracts should you sell per unit of spot exposure? The naive answer — one-for-one — is only correct under specific conditions.

The fundamental problem is that the price of your asset and the price of the futures contract do not move in perfect lockstep. They may be on different maturities, different but related commodities (cross-hedging), or affected by different local supply and demand conditions. The gap between spot and futures prices is called the **basis**, and the uncertainty about how that basis will evolve is **basis risk**. Your goal is to minimize the total variance of your combined position (spot + futures), not just the variance of the spot position.

Think about it this way: you hold 1 unit of the spot asset with price changes ΔS. You short h units of futures with price changes ΔF. Your hedged P&L is ΔS − h·ΔF. The variance of this is Var(ΔS) − 2h·Cov(ΔS, ΔF) + h²·Var(ΔF). Minimizing over h by taking the derivative and setting it to zero gives h* = Cov(ΔS, ΔF) / Var(ΔF), which simplifies to h* = ρ·(σ_S / σ_F). This is the **minimum variance hedge ratio**. You can estimate it directly as the slope coefficient from a regression of ΔS on ΔF — the OLS regression framework you know from prerequisites naturally delivers the minimum-variance solution.

The formula has clear intuition: if the spot and futures move perfectly together (ρ = 1) and have the same volatility (σ_S = σ_F), then h* = 1 — a one-for-one hedge is optimal. If the futures are more volatile than the spot (σ_F > σ_S), you need fewer futures contracts to offset a given spot exposure — h* < 1. If correlation is imperfect (ρ < 1), no hedge fully eliminates risk, but the minimum-variance ratio still reduces it as much as possible given the available instrument. **Hedge effectiveness**, measured as the R² from the regression of ΔS on ΔF, tells you what fraction of price variance the hedge eliminates — it equals ρ², so a correlation of 0.9 eliminates 81% of spot price variance.

From your portfolio diversification background, this analysis should feel familiar: it is an application of the same variance-minimization principle that underlies optimal portfolio weights, now applied to a hedging context. Cross-hedges — hedging one commodity with a futures contract on a related but distinct commodity (e.g., jet fuel with crude oil futures) — work on exactly this logic. The higher the correlation, the more effective the cross-hedge. When correlation is low or unstable over time, the hedger must regularly re-estimate h* using recent data and rebalance the futures position accordingly.
