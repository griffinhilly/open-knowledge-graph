---
id: expected-return-and-variance-of-assets
title: Expected Return and Variance of Financial Assets
domain: economics
course: financial-economics
prerequisites:
- id: risk-and-return-tradeoff
  type: hard
- id: variance-of-random-variables
  type: hard
- id: normal-distribution-intro
  type: soft
- id: expected-value
  type: soft
builds-toward:
- portfolio-diversification
- mean-variance-optimization
tags:
- expected-return
- variance
- covariance
- asset-returns
- statistics
stage: formal-systems
status: validated
---

# Expected Return and Variance of Financial Assets

## Core Idea
The expected return of an asset is the probability-weighted average of its possible returns: E[r] = Σ pᵢrᵢ. Variance measures dispersion around the mean: σ² = Σ pᵢ(rᵢ − E[r])². For a portfolio of two assets with weights w₁ and w₂, portfolio variance is σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(r₁,r₂). This covariance term is the key insight behind diversification: assets that do not move perfectly together reduce portfolio risk below the weighted average of individual risks. The magnitude of this reduction depends entirely on the correlation between the two assets.

## How It's Best Learned
Calculate expected return and variance from a probability distribution, then repeat using historical return data to see how the statistical formulas apply empirically. Compute two-asset portfolio variance at correlations of −1, 0, and +1 to see the full range of what diversification can achieve.

## Common Misconceptions
- Omitting the covariance term from portfolio variance is the most common calculation error and entirely misses the point of diversification.
- Assuming returns are normally distributed is convenient but wrong — financial returns exhibit fat tails and negative skewness that the normal distribution systematically underestimates.

## Questions

```yaml
- question: "Two assets each have a variance of 0.04. You form an equally weighted portfolio (w₁ = w₂ = 0.5). If the correlation between the assets is 0 (rather than +1), what happens to portfolio variance compared to the weighted average of individual variances?"
  type: multiple-choice
  options:
    - "Portfolio variance equals 0.04 — the same as each individual asset"
    - "Portfolio variance is 0.02 — lower than the individual variance"
    - "Portfolio variance is 0.04 — equal to the weighted average"
    - "Portfolio variance is 0.08 — higher because you hold two risky assets"
  answer: 1
  explanation: "With w₁ = w₂ = 0.5, σ₁² = σ₂² = 0.04, and Cov(r₁,r₂) = ρσ₁σ₂ = 0: σ²_p = (0.5)²(0.04) + (0.5)²(0.04) + 2(0.5)(0.5)(0) = 0.01 + 0.01 = 0.02. The weighted average of individual variances would be 0.04. Zero correlation cuts variance in half — this is diversification at work. The covariance term vanishes entirely, so you get the full benefit of combining two independent risks."

- question: "Adding a second asset to a portfolio usually reduces portfolio variance, regardless of the correlation between the two assets."
  type: true-false
  answer: false
  explanation: "When the correlation between two assets equals +1, the portfolio variance formula gives σ²_p = (w₁σ₁ + w₂σ₂)², which equals the weighted average of standard deviations squared. There is zero diversification benefit. If you add an asset perfectly correlated with your existing holding, you gain no risk reduction — portfolio risk is simply a weighted blend of the two. Only when correlation is less than +1 does diversification reduce variance below the weighted average."

- question: "In the two-asset portfolio variance formula σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(r₁,r₂), why is the covariance term the key insight rather than the individual variance terms?"
  type: short-answer
  answer: "The individual variance terms simply scale each asset's own risk by its portfolio weight. The covariance term determines how much those risks offset or amplify each other — it captures whether the assets tend to move together or in opposite directions. Diversification benefit comes entirely from the covariance term: if it is negative, portfolio risk falls below the weighted average of individual risks."
  explanation: "The covariance term 2w₁w₂Cov(r₁,r₂) encodes the interaction between the two assets. When covariance is negative (assets move oppositely), it subtracts from portfolio variance, creating diversification benefit. When covariance is positive (assets move together), it adds to variance, reducing diversification. This is why investors seek assets with low or negative correlation — the benefit of combining them comes entirely from this cross-term, not from the individual variance terms."
```

## Explainer

You already know from probability theory that the expected value of a random variable is its probability-weighted average, and that variance measures how spread out the outcomes are around that average. Financial assets are random variables: their returns are uncertain. Applying those statistical definitions to returns gives you the expected return E[r] = Σ pᵢrᵢ and variance σ² = Σ pᵢ(rᵢ − E[r])². These are the same formulas you learned — just applied to future returns instead of abstract outcomes.

The interesting material begins when you combine assets into a portfolio. Portfolio expected return is simply the weighted average of individual expected returns: E[rₚ] = w₁E[r₁] + w₂E[r₂]. Simple and intuitive. Portfolio variance, however, is not the weighted average of individual variances. The formula is σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(r₁,r₂). That third term — the covariance — is where all the action is. It measures whether the two assets tend to move together or in opposite directions.

The covariance term is the mathematical basis for diversification. If two assets have zero correlation, their covariance is zero, and the portfolio variance is less than the weighted average of the individual variances — you got risk reduction for free, just by combining them. If they have negative correlation, the covariance term is negative, reducing portfolio variance further. In the extreme case of correlation = −1, you can combine the assets in specific weights to achieve zero portfolio variance entirely. The intuition: when one asset zigs, the other zags, and the movements cancel out.

The practical upshot is that what matters for a portfolio is not just an asset's own variance but its covariance with everything else already in the portfolio. An asset with high individual variance but low correlation with the rest of the portfolio can actually reduce total portfolio risk when added. This is why international diversification works (equity markets across countries have historically been less than perfectly correlated) and why bonds are valuable in equity-heavy portfolios (bond and equity returns often move in opposite directions during market stress).

One important caveat: correlations between assets are not stable. During market crises, correlations across asset classes tend to spike toward +1 — the assets that were supposed to diversify each other start moving together exactly when you need diversification most. This "correlation breakdown" is one reason why realized portfolio losses during crashes are often larger than models predicted, and why variance alone understates actual risk in tail scenarios.
