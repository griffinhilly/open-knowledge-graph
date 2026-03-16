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

## Explainer

You already know how to compute the expected return and variance of a single asset. Now the question is: what happens when you combine two assets into a portfolio? The answer depends not just on each asset's individual volatility but on how they move together. **Covariance** (Cov(Rₐ, R_b) = E[(Rₐ − μₐ)(R_b − μ_b)]) captures the direction and magnitude of co-movement. A positive covariance means the two assets tend to move in the same direction — when one is up, the other tends to be up too. A negative covariance means they move in opposite directions, providing a natural hedge.

Covariance has a scaling problem: its magnitude depends on the units of the returns (whether you use percentages or decimals) and the overall volatility of each asset. Two stocks with high individual variances will have a large covariance in absolute terms even if their *relationship* is no stronger than two low-volatility bonds. This is why **correlation** is the more interpretable measure. Correlation ρ(Rₐ, R_b) = Cov(Rₐ, R_b) / (σₐ × σ_b) standardizes covariance by dividing by the product of the two standard deviations. The result is dimensionless and always falls in [−1, 1]. A correlation of +1 means the assets move in perfect lockstep; −1 means they move in perfect opposition; 0 means no linear relationship.

The portfolio implications follow directly from the two-asset portfolio variance formula: σ²_p = w²_a σ²_a + w²_b σ²_b + 2 wₐ w_b Cov(Rₐ, R_b). Notice the covariance term: if correlation is negative, the third term subtracts from portfolio variance, reducing total risk below the weighted average of individual risks. This is the mathematical foundation of diversification. The lower the correlation between two assets, the greater the risk reduction from combining them — even if both assets are individually risky. A portfolio of two assets with ρ = −1 can, with the right weights, achieve zero variance. A portfolio of two perfectly correlated assets (ρ = +1) gets no risk reduction at all.

This is why practitioners speak of correlation as the key input to portfolio construction. Expected returns tell you where you want to go; variances tell you the risk of each vehicle; correlations tell you how the vehicles interact. Historical correlations between asset classes like stocks and bonds, or domestic and international equities, are not stable — they tend to spike toward +1 during market crises, precisely when diversification is most needed. Understanding this instability of correlations under stress is one of the most important practical lessons that builds on the foundational mechanics you are learning here.
