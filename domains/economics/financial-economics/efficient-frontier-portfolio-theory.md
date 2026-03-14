---
id: efficient-frontier-portfolio-theory
title: Efficient Frontier and Capital Market Line
domain: economics
course: financial-economics
prerequisites:
- id: mean-variance-optimization
  type: hard
- id: risk-and-return-tradeoff
  type: hard
- id: matrices-intro
  type: soft
- id: variance-of-random-variables
  type: soft
builds-toward:
- capital-asset-pricing-model
- risk-adjusted-performance-measures
tags:
- efficient-frontier
- capital-market-line
- tangency-portfolio
- separation-theorem
stage: formal-systems
status: validated
---

# Efficient Frontier and Capital Market Line

## Core Idea
The efficient frontier is the set of portfolios that offer the maximum expected return for each level of risk. When a risk-free asset is added, investors can combine it with any risky portfolio — the optimal combination is the line from the risk-free rate tangent to the efficient frontier, called the Capital Market Line (CML). The tangency point — the market portfolio — is the unique optimal risky portfolio for all investors regardless of risk aversion; the only choice is how much to allocate to it versus the risk-free asset. This separation theorem dramatically simplifies portfolio selection and lays the foundation for CAPM.

## How It's Best Learned
Graphically derive the CML by rotating a line from the risk-free rate until it is tangent to the efficient frontier. Understand that the tangency portfolio maximizes the Sharpe ratio. Contrast investors at different risk tolerances: a conservative investor holds mostly the risk-free asset; an aggressive investor levers up the tangency portfolio.

## Common Misconceptions
- The efficient frontier is not static — it shifts with changing expected returns, variances, and correlations, so optimal portfolios change over time.
- The Capital Market Line applies to efficient portfolios (combinations of risk-free asset and tangency portfolio); individual assets generally lie below the CML.
