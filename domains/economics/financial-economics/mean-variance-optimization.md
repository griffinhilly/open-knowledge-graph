---
id: mean-variance-optimization
title: Mean-Variance Optimization (Markowitz Framework)
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: expected-return-and-variance-of-assets
  type: hard
- id: lagrange-multipliers
  type: soft
- id: matrices-intro
  type: soft
- id: optimization-problems
  type: soft
- id: constrained-optimization-lagrange
  type: soft
- id: linear-algebra
  type: hard
- id: constrained-optimization
  type: hard
- id: expected-value-theory
  type: hard
- id: linear-programming
  type: soft
builds-toward:
- efficient-frontier-portfolio-theory
- capital-asset-pricing-model
tags:
- markowitz
- portfolio-optimization
- covariance-matrix
- modern-portfolio-theory
stage: formal-systems
status: validated
---

# Mean-Variance Optimization (Markowitz Framework)

## Core Idea
Harry Markowitz (1952) formalized portfolio selection as an optimization problem: for any target expected return, find the portfolio weights that minimize variance, subject to weights summing to one. The inputs are expected returns, variances, and all pairwise covariances — summarized in the covariance matrix. Solving this quadratic optimization for all feasible return levels traces out the minimum-variance frontier, and the upper portion — where no portfolio can offer higher expected return for the same variance — is the efficient frontier. This was the first rigorous mathematical treatment of diversification, earning Markowitz a Nobel Prize in Economics in 1990.

## How It's Best Learned
Set up the optimization in matrix form for three assets to see the role of the covariance matrix. Use software (Python/scipy or Excel Solver) to trace the full efficient frontier. Observe how the frontier shifts when correlations change, highlighting the central role of covariance structure.

## Common Misconceptions
- The framework does not identify a unique 'best' portfolio — it gives a frontier; the investor's risk tolerance determines which point on the frontier is optimal.
- The framework is extremely sensitive to expected return inputs — small estimation errors produce large changes in optimal weights, limiting practical reliability.

## Questions

```yaml
- question: "The efficient frontier is best described as the set of portfolios that..."
  type: multiple-choice
  options: ["Maximize expected return without any constraint on risk", "Minimize portfolio variance for every possible level of expected return", "Offer the maximum expected return for each level of variance, forming the upper portion of the minimum-variance frontier", "Have zero correlation with every other available asset"]
  answer: 2
  explanation: "The minimum-variance frontier contains the lowest-variance portfolio for each target expected return — including the bottom half where higher variance comes with *lower* expected return. The efficient frontier is only the upper portion: portfolios where no other portfolio offers strictly higher expected return for the same variance. Option B describes the full minimum-variance frontier, not the efficient subset. An investor would never rationally choose an inefficient portfolio."

- question: "Adding a new asset to the investment universe can only keep the efficient frontier the same or move it outward (toward better risk-return combinations) — it can never make it worse."
  type: true-false
  answer: true
  explanation: "Expanding the opportunity set is weakly beneficial. Any portfolio achievable before is still achievable after adding the new asset (by setting its weight to zero). If the new asset has any correlation less than +1 with the existing portfolio, it creates diversification opportunities that shift the frontier outward. In the degenerate case of perfect positive correlation with an existing asset, the frontier is unchanged."

- question: "Why is mean-variance optimization sometimes described as an 'error maximizer' in practice?"
  type: short-answer
  answer: "Small errors in expected return estimates cause the optimizer to concentrate large portfolio weights in the slightly-overestimated assets. Because the objective function is very sensitive to expected return inputs, estimation noise gets amplified into extreme and unstable weight allocations, rather than being averaged out."
  explanation: "This is a well-known critique of Markowitz optimization in implementation. Expected returns are notoriously difficult to estimate reliably from historical data. Practitioners use techniques like shrinkage estimators, Black-Litterman views, or constraints on maximum weights to reduce this sensitivity and produce more robust portfolios."
```

## Explainer

You already know from portfolio diversification that combining assets with imperfect correlation reduces portfolio risk without necessarily reducing expected return. Markowitz's contribution was to formalize exactly *how* to do this optimally. Instead of relying on intuition about which assets to combine, he posed it as a precise mathematical problem: given a target expected return, find the portfolio weights that minimize variance. Solving this for every possible target return generates a curve in expected-return/standard-deviation space — the minimum-variance frontier.

The inputs to this optimization are three things: a vector of expected returns (one per asset), a vector of variances, and — crucially — the full matrix of pairwise covariances between every pair of assets. This covariance matrix is what captures the diversification structure of the portfolio. Two assets that are individually volatile but negatively correlated create a combined portfolio with dramatically lower variance. The optimization exploits all of these correlations simultaneously, which is why it requires matrix algebra rather than simple arithmetic.

The efficient frontier is the upper portion of the minimum-variance frontier. For a given level of variance (horizontal axis), the efficient portfolio maximizes expected return; equivalently, for a given expected return, it minimizes variance. Portfolios below the minimum-variance point are dominated — there exists another portfolio with the same variance but higher expected return — so no rational investor would choose them. The efficient frontier does not specify a single best portfolio; which point on it is optimal depends on the investor's risk tolerance, which is encoded in their utility function.

A critical and counterintuitive property of the framework is its sensitivity to expected return inputs. Small changes in projected returns — well within the range of estimation error — can cause the optimizer to shift portfolio weights dramatically, concentrating heavily in assets whose expected return is only trivially higher. This "error maximization" problem means that naïvely applying Markowitz optimization to historical return estimates often produces unstable, concentrated portfolios that perform poorly out of sample. Practitioners respond with robust estimation methods, Bayesian shrinkage, or by constraining weights directly.

The mean-variance framework earned Markowitz the 1990 Nobel Prize not because it is perfectly practical in its raw form, but because it established the foundational principle: return and risk must be traded off *at the portfolio level*, accounting for correlations, not just asset by asset. Every subsequent asset pricing model — the CAPM, factor models, Black-Litterman — builds directly on this foundation.
