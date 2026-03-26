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
- id: hedging-with-derivatives
  type: soft
builds-toward:
- portfolio-insurance-strategy
tags:
- hedging
- derivatives
- risk-management
- optimization
stage: formal-systems
status: validated
---
# Optimal Hedging Ratios and Hedge Effectiveness

## Core Idea
The optimal hedge ratio minimizes the variance of a hedged position: h* = ρ(σ_spot/σ_futures) where ρ is the correlation between spot and futures price changes. Perfect hedges (ρ = 1, matched maturities) eliminate all price risk, while imperfect hedges leave basis risk. Calculating optimal ratios requires understanding the correlation between the asset being hedged and available derivatives.

## Questions

```yaml
- question: "An airline holds jet fuel exposure (spot volatility σ_S = 12%) and hedges using crude oil futures (σ_F = 20%). The correlation between jet fuel and crude oil price changes is ρ = 0.90. What is the optimal hedge ratio?"
  type: multiple-choice
  options:
    - "0.90 — the hedge ratio equals the correlation between the assets"
    - "1.00 — one futures contract per unit of spot exposure is always optimal"
    - "0.54 — calculated as ρ × (σ_S / σ_F) = 0.90 × (12/20)"
    - "1.67 — you need more futures contracts because crude is more volatile than jet fuel"
  answer: 2
  explanation: "The minimum-variance hedge ratio is h* = ρ × (σ_S / σ_F) = 0.90 × (0.12/0.20) = 0.54. Because crude oil futures are more volatile than jet fuel, each futures contract provides more price movement than one unit of spot exposure, so you need fewer contracts per unit hedged. The common mistake (option B) assumes 1:1 is always correct; that only holds when spot and futures have identical volatility AND perfect correlation. Option A confuses correlation with the hedge ratio."

- question: "A risk manager uses a regression of daily spot price changes on futures price changes and finds an R² of 0.64. What does this tell her about the hedge?"
  type: multiple-choice
  options:
    - "The hedge eliminates 64% of spot price variance — correlation between spot and futures is 0.80"
    - "The hedge eliminates 80% of spot price variance — the hedge ratio itself is 0.80"
    - "The hedge is unreliable — an R² below 0.9 indicates the futures contract is the wrong hedging instrument"
    - "The remaining 36% of variance is due to systematic market risk that no hedge can reduce"
  answer: 0
  explanation: "Hedge effectiveness equals ρ², which is the R² from the regression of ΔS on ΔF. R² = 0.64 means the correlation is ρ = √0.64 = 0.80, and the hedge eliminates 64% of spot price variance. The remaining 36% is basis risk — the portion of spot price movement uncorrelated with futures — which cannot be eliminated regardless of the number of contracts held. R² values in the 0.6–0.8 range are common for cross-hedges and still represent meaningful risk reduction."

- question: "A cross-hedge using crude oil futures to hedge jet fuel price exposure can eliminate most jet fuel price risk if enough futures contracts are held."
  type: true-false
  answer: false
  explanation: "No number of futures contracts eliminates all basis risk when the correlation ρ < 1. The minimum-variance hedge ratio is optimal — it reduces variance as much as the available instrument allows — but residual variance equal to (1 − ρ²) × Var(ΔS) remains. For a cross-hedge where two commodities are related but distinct, ρ < 1 always, so basis risk is unavoidable. The only way to eliminate all price risk is a perfect hedge: ρ = 1, matched maturity, and identical underlying."

- question: "If the futures contract used for hedging is more volatile than the spot asset being hedged, the optimal hedge ratio will be less than 1."
  type: true-false
  answer: true
  explanation: "The formula h* = ρ × (σ_S / σ_F) shows this directly: when σ_F > σ_S, the ratio σ_S/σ_F < 1, and multiplying by ρ ≤ 1 only reduces it further. Intuitively, each futures contract moves more than one unit of spot exposure, so you need fewer contracts to offset a given spot position. Holding one-for-one would over-hedge, actually introducing more variance than the original unhedged position relative to the minimum-variance solution."

- question: "Why is the optimal hedge ratio derived from a regression of spot price changes on futures price changes, and what does the R² of that regression tell you about the quality of the hedge?"
  type: short-answer
  answer: "The OLS regression of ΔS on ΔF directly delivers the minimum-variance hedge ratio as the slope coefficient β = Cov(ΔS, ΔF) / Var(ΔF) = h*. This is not a coincidence — OLS minimizes the sum of squared residuals, which is equivalent to minimizing the variance of the hedged P&L (ΔS − h·ΔF). The R² measures what fraction of spot price variance is explained by the futures instrument and equals ρ², directly quantifying hedge effectiveness — the fraction of spot risk the hedge eliminates."
  explanation: "The regression framework is powerful because it simultaneously gives you the hedge ratio (slope), the hedge effectiveness (R²), and statistical confidence intervals — all from a single estimation. It also allows you to detect instability: if the hedge ratio has changed significantly between estimation periods, you need to rebalance your futures position."
```

## Explainer

You know from your study of futures and forward contracts that a hedge works by taking an offsetting position: if you own an asset and fear a price drop, you sell futures contracts so that gains on the short futures position offset losses on the underlying. The question the optimal hedge ratio answers is: how many futures contracts should you sell per unit of spot exposure? The naive answer — one-for-one — is only correct under specific conditions.

The fundamental problem is that the price of your asset and the price of the futures contract do not move in perfect lockstep. They may be on different maturities, different but related commodities (cross-hedging), or affected by different local supply and demand conditions. The gap between spot and futures prices is called the **basis**, and the uncertainty about how that basis will evolve is **basis risk**. Your goal is to minimize the total variance of your combined position (spot + futures), not just the variance of the spot position.

Think about it this way: you hold 1 unit of the spot asset with price changes ΔS. You short h units of futures with price changes ΔF. Your hedged P&L is ΔS − h·ΔF. The variance of this is Var(ΔS) − 2h·Cov(ΔS, ΔF) + h²·Var(ΔF). Minimizing over h by taking the derivative and setting it to zero gives h* = Cov(ΔS, ΔF) / Var(ΔF), which simplifies to h* = ρ·(σ_S / σ_F). This is the **minimum variance hedge ratio**. You can estimate it directly as the slope coefficient from a regression of ΔS on ΔF — the OLS regression framework you know from prerequisites naturally delivers the minimum-variance solution.

The formula has clear intuition: if the spot and futures move perfectly together (ρ = 1) and have the same volatility (σ_S = σ_F), then h* = 1 — a one-for-one hedge is optimal. If the futures are more volatile than the spot (σ_F > σ_S), you need fewer futures contracts to offset a given spot exposure — h* < 1. If correlation is imperfect (ρ < 1), no hedge fully eliminates risk, but the minimum-variance ratio still reduces it as much as possible given the available instrument. **Hedge effectiveness**, measured as the R² from the regression of ΔS on ΔF, tells you what fraction of price variance the hedge eliminates — it equals ρ², so a correlation of 0.9 eliminates 81% of spot price variance.

From your portfolio diversification background, this analysis should feel familiar: it is an application of the same variance-minimization principle that underlies optimal portfolio weights, now applied to a hedging context. Cross-hedges — hedging one commodity with a futures contract on a related but distinct commodity (e.g., jet fuel with crude oil futures) — work on exactly this logic. The higher the correlation, the more effective the cross-hedge. When correlation is low or unstable over time, the hedger must regularly re-estimate h* using recent data and rebalance the futures position accordingly.
