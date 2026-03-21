---
id: correlation-covariance-assets
title: Correlation and Covariance Between Assets
domain: economics
course: financial-economics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: hard
builds-toward:
- two-asset-portfolio-optimization
- efficient-frontier-construction
tags:
- portfolio-theory
- risk-measurement
- statistics
stage: formal-systems
status: draft
---

# Correlation and Covariance Between Assets

## Core Idea
Covariance measures how two assets move together (positive = move in same direction, negative = move opposite). Correlation standardizes covariance to range [−1, 1], making cross-asset relationships comparable and essential for portfolio construction.

## How It's Best Learned
Calculate correlations between stock returns and bond returns, then between two stocks. Observe how historical correlations vary across market regimes and asset types.

## Questions

```yaml
- question: "Two asset pairs have identical expected returns and identical individual variances. Pair A has correlation ρ = +0.9. Pair B has correlation ρ = −0.2. Which pair delivers greater risk reduction when combined in an equal-weight portfolio?"
  type: multiple-choice
  options:
    - "Pair A — the high positive correlation means the assets reinforce each other, creating more stable combined returns"
    - "Pair B — the lower (negative) correlation means the assets partially offset each other, reducing portfolio variance more"
    - "They are identical — same individual variances means the same portfolio risk regardless of correlation"
    - "Pair A — positive correlation means the assets diversify each other by moving in the same direction"
  answer: 1
  explanation: "Portfolio variance = w²σ²_a + w²σ²_b + 2w²·Cov(a,b), and Cov = ρ·σ_a·σ_b. With ρ = −0.2, the covariance term is negative, subtracting from portfolio variance. With ρ = +0.9, it adds substantially. The lower the correlation, the greater the diversification benefit. A common misconception is that 'moving together' is good for a portfolio — synchronized movement means no risk reduction."

- question: "An investor finds that Stock A and Bond B each have a standard deviation of 20%, and their covariance is 0.02. She computes the correlation as 0.02 / (0.20 × 0.20) = 0.5. Why is this correlation figure more useful for comparing relationships across asset pairs than the raw covariance?"
  type: multiple-choice
  options:
    - "Because covariance can only be negative, while correlation reflects both positive and negative relationships"
    - "Because correlation is dimensionless and bounded to [−1, 1], making the strength of relationships directly comparable across asset pairs with different volatilities"
    - "Because covariance measures absolute risk while correlation measures relative return"
    - "Because correlation adjusts for differences in expected returns between the two assets"
  answer: 1
  explanation: "Covariance's magnitude depends on the units and individual volatilities of both assets. Two high-volatility stocks will have a large covariance in absolute terms even if their co-movement relationship is no tighter than two low-volatility bonds. Dividing by σ_a·σ_b standardizes the measure to [−1, 1], making correlation comparable across all asset pairs regardless of scale."

- question: "If two assets have a correlation of exactly −1, it is theoretically possible to construct a portfolio with zero variance by choosing the right weights."
  type: true-false
  answer: true
  explanation: "With perfect negative correlation, portfolio variance σ²_p = (wₐσ_a − w_bσ_b)². This equals zero when wₐσ_a = w_bσ_b, i.e., when weights are chosen inversely proportional to the assets' standard deviations. In this portfolio, every gain in one asset is perfectly offset by a loss in the other. ρ = −1 is the theoretical maximum diversification benefit."

- question: "A portfolio of two assets with zero correlation (ρ = 0) achieves no reduction in portfolio risk compared to holding either asset alone at full weight."
  type: true-false
  answer: false
  explanation: "Zero correlation still provides diversification benefits. With ρ = 0, portfolio variance = w²_a σ²_a + w²_b σ²_b (the covariance term vanishes). For equal weights, σ²_p = (σ²_a + σ²_b)/4, which is typically less than holding either asset alone (σ²_a or σ²_b). No risk reduction only occurs when ρ = +1. Even uncorrelated assets reduce variance when combined."

- question: "Why does the correlation between two assets — rather than their individual variances — determine how much risk reduction is achieved by combining them in a portfolio?"
  type: short-answer
  answer: "Because portfolio variance includes an interaction term: 2·wₐ·w_b·Cov(a,b) = 2·wₐ·w_b·ρ·σ_a·σ_b. The individual variances set what you'd have if ρ = +1 (no diversification benefit), but correlation determines how much the interaction term reduces that floor. When ρ < 1, the assets partially offset each other's fluctuations, reducing total risk below the weighted average of individual risks."
  explanation: "With ρ = +1, assets move in lockstep and there is no diversification benefit. With ρ = 0, portfolio variance is simply the weighted sum of variances. With ρ < 0, assets actively offset each other, potentially reducing variance dramatically. Individual variances determine how volatile each asset is alone; correlation determines how the combination behaves."
```

## Explainer

You already know how to compute the expected return and variance of a single asset. Now the question is: what happens when you combine two assets into a portfolio? The answer depends not just on each asset's individual volatility but on how they move together. **Covariance** (Cov(Rₐ, R_b) = E[(Rₐ − μₐ)(R_b − μ_b)]) captures the direction and magnitude of co-movement. A positive covariance means the two assets tend to move in the same direction — when one is up, the other tends to be up too. A negative covariance means they move in opposite directions, providing a natural hedge.

Covariance has a scaling problem: its magnitude depends on the units of the returns (whether you use percentages or decimals) and the overall volatility of each asset. Two stocks with high individual variances will have a large covariance in absolute terms even if their *relationship* is no stronger than two low-volatility bonds. This is why **correlation** is the more interpretable measure. Correlation ρ(Rₐ, R_b) = Cov(Rₐ, R_b) / (σₐ × σ_b) standardizes covariance by dividing by the product of the two standard deviations. The result is dimensionless and always falls in [−1, 1]. A correlation of +1 means the assets move in perfect lockstep; −1 means they move in perfect opposition; 0 means no linear relationship.

The portfolio implications follow directly from the two-asset portfolio variance formula: σ²_p = w²_a σ²_a + w²_b σ²_b + 2 wₐ w_b Cov(Rₐ, R_b). Notice the covariance term: if correlation is negative, the third term subtracts from portfolio variance, reducing total risk below the weighted average of individual risks. This is the mathematical foundation of diversification. The lower the correlation between two assets, the greater the risk reduction from combining them — even if both assets are individually risky. A portfolio of two assets with ρ = −1 can, with the right weights, achieve zero variance. A portfolio of two perfectly correlated assets (ρ = +1) gets no risk reduction at all.

This is why practitioners speak of correlation as the key input to portfolio construction. Expected returns tell you where you want to go; variances tell you the risk of each vehicle; correlations tell you how the vehicles interact. Historical correlations between asset classes like stocks and bonds, or domestic and international equities, are not stable — they tend to spike toward +1 during market crises, precisely when diversification is most needed. Understanding this instability of correlations under stress is one of the most important practical lessons that builds on the foundational mechanics you are learning here.
