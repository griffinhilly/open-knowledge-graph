---
id: two-asset-portfolio-optimization
title: Two-Asset Portfolio Optimization
domain: economics
course: financial-economics
prerequisites:
- id: mean-variance-optimization
  type: hard
- id: correlation-covariance-assets
  type: hard
- id: diversification-benefits-correlated
  type: soft
- id: correlation-and-covariance-matrices
  type: soft
builds-toward:
- efficient-frontier-construction
tags:
- portfolio-theory
- optimization
- diversification
stage: formal-systems
status: validated
---
# Two-Asset Portfolio Optimization

## Core Idea
For two assets, the minimum-variance portfolio weight allocation depends on their variances and correlation. Frontier portfolios are parameterized by expected return; as correlation decreases, diversification benefits increase, pulling the frontier inward.

## How It's Best Learned
Compute the minimum-variance portfolio for two stocks with different correlations. Plot efficient frontiers for high, zero, and negative correlation to visualize diversification benefits.

## Questions

```yaml
- question: "Two assets have equal expected returns and equal standard deviations of 20%. An investor calculates the portfolio variance as (0.5)²(0.04) + (0.5)²(0.04) = 0.02, assuming no interaction between assets. Why is this calculation wrong?"
  type: multiple-choice
  options:
    - "It's correct — equal weights produce a simple average of the variances"
    - "It ignores the covariance term; the true portfolio variance includes 2·w·(1−w)·σ₁·σ₂·ρ, which reduces variance when ρ < 1"
    - "It uses the wrong weights — the minimum-variance weights are not 50/50"
    - "It should multiply by 2 to account for holding two assets instead of one"
  answer: 1
  explanation: "Portfolio variance is NOT the weighted average of individual variances. The correct formula is σₚ² = w²σ₁² + (1−w)²σ₂² + 2w(1−w)σ₁σ₂ρ. The third term — the covariance contribution — reduces total variance whenever ρ < 1. If ρ = 0 and each asset has σ = 20% with equal weights, σₚ² = (0.25)(0.04) + (0.25)(0.04) = 0.02, which is 14.1% volatility — less than either asset individually. Omitting the covariance term ignores the entire engine of diversification."

- question: "As the correlation between two assets decreases from +1 to −1, what happens to the portfolio frontier plotted in mean–standard-deviation space?"
  type: multiple-choice
  options:
    - "It shifts rightward, increasing risk at every return level"
    - "It flattens into a horizontal line, since expected returns don't change"
    - "It bows further leftward, offering lower portfolio variance at every return level"
    - "It collapses to a single point representing the risk-free rate"
  answer: 2
  explanation: "The covariance term 2w(1−w)σ₁σ₂ρ decreases as ρ falls, reducing portfolio variance for any given weight allocation. In the limit ρ = −1, a zero-variance portfolio is achievable. Visually, as correlation decreases, the frontier bows further to the left in mean-SD space — meaning investors can achieve the same expected return at lower risk, or more return at the same risk. This leftward bow is the geometric representation of diversification benefit. At ρ = +1, there's no bow at all — the frontier is a straight line, and holding both assets gives no variance reduction."

- question: "A portfolio that lies below the minimum-variance point on the two-asset frontier is dominated: you could achieve the same expected return with less risk."
  type: true-false
  answer: true
  explanation: "The minimum-variance portfolio is the leftmost point of the frontier curve. Portfolios above it (higher expected return for similar or slightly higher risk) are efficient. Portfolios below it are inefficient — for any such portfolio, you could shift weight toward the minimum-variance point and get the same expected return with lower variance, or hold a portfolio above the minimum-variance point with higher return and the same risk. No rational mean-variance investor would choose a dominated portfolio."

- question: "When two assets have perfect positive correlation (ρ = 1), combining them in any proportion still reduces portfolio variance below the variance of the higher-variance asset."
  type: true-false
  answer: false
  explanation: "At ρ = 1, the portfolio standard deviation is exactly the weighted average of the individual standard deviations: σₚ = w·σ₁ + (1−w)·σ₂. There is no diversification benefit whatsoever. Portfolio variance lies on a straight line between the two assets' risk-return combinations — it is bounded below by the lower-variance asset's variance (achieved by putting all weight there), but no intermediate combination reduces risk below the lower individual variance. The leftward bow in the frontier disappears entirely at ρ = 1."

- question: "Why is portfolio variance less than the weighted average of the individual variances when the two assets have correlation less than 1? Identify the key term in the variance formula."
  type: short-answer
  answer: "The portfolio variance formula is σₚ² = w²σ₁² + (1−w)²σ₂² + 2w(1−w)σ₁σ₂ρ. When ρ < 1, the cross-term 2w(1−w)σ₁σ₂ρ is smaller than it would be at ρ = 1, so the total variance is less than the weighted average of σ₁² and σ₂². The lower the correlation, the smaller this term, and the greater the variance reduction — reaching zero variance when ρ = −1."
  explanation: "At ρ = 1, the portfolio variance equals [wσ₁ + (1−w)σ₂]² — exactly the square of the weighted-average standard deviation, meaning no benefit from combining. For ρ < 1, the cross-term shrinks, pulling variance below that level. This is the mathematical basis of diversification: combining assets whose returns are not perfectly correlated (the typical case) produces a portfolio with less variance than a naive weighted-average calculation would suggest."
```

## Explainer

From mean-variance optimization, you know that a rational investor cares only about the expected return and variance of their portfolio, and from your study of correlation and covariance between assets, you know that combining assets with imperfect correlation reduces total portfolio variance even when each asset individually is risky. The two-asset case makes these ideas fully concrete before extending to the full efficient frontier.

Suppose you have two assets with expected returns μ₁ and μ₂, standard deviations σ₁ and σ₂, and correlation ρ. You invest weight w in asset 1 and (1−w) in asset 2. The portfolio's expected return is simply the weighted average: μₚ = wμ₁ + (1−w)μ₂. But the portfolio's variance is not the weighted average of the individual variances — it is: σₚ² = w²σ₁² + (1−w)²σ₂² + 2w(1−w)σ₁σ₂ρ. The last term — the covariance contribution — is the engine of diversification. When ρ < 1, this cross-term is smaller than it would be if returns were perfectly correlated, so σₚ² is less than the weighted average of the individual variances.

The **minimum-variance portfolio** is the weight allocation w* that minimizes σₚ². Taking the derivative of σₚ² with respect to w and setting it to zero yields: w* = (σ₂² − σ₁σ₂ρ) / (σ₁² + σ₂² − 2σ₁σ₂ρ). This formula rewards assets whose returns are dissimilar from the other asset — the lower the correlation, the higher the weight placed on the asset with lower absolute variance. As ρ approaches −1 (perfect negative correlation), it becomes possible to construct a portfolio with zero variance — a risk-free combination from two risky assets. As ρ approaches +1, the assets move in lockstep and no diversification is possible; the "frontier" collapses to a straight line between the two assets in expected-return/standard-deviation space.

Plotting the full set of achievable portfolios as w varies from 0 to 1 traces out the **portfolio frontier** — a curve in mean-standard-deviation space that bows leftward, toward lower volatility, when ρ < 1. The leftward bow is the visual representation of diversification: the portfolio frontier offers more return per unit of risk than any individual asset. The minimum-variance portfolio is the leftmost point of this curve. Portfolios on the upper portion of the curve (above the minimum-variance point) are **efficient** — they offer the maximum expected return for a given level of risk. Portfolios below that point are dominated: you could get the same return with less risk, or more return with the same risk, by holding a different combination. This geometry — and the intuition that correlation drives the shape of the frontier — is the foundation you will need to construct the full efficient frontier with N assets.
