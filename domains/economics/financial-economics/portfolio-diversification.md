---
id: portfolio-diversification
title: Portfolio Diversification
domain: economics
course: financial-economics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: hard
- id: correlation-coefficient
  type: hard
- id: variance-of-random-variables
  type: soft
- id: constrained-optimization-lagrange
  type: soft
- id: eigenvalues-eigenvectors
  type: soft
- id: linear-algebra
  type: hard
- id: expected-value-theory
  type: hard
builds-toward:
- mean-variance-optimization
- efficient-frontier-portfolio-theory
- beta-and-systematic-risk
tags:
- diversification
- idiosyncratic-risk
- systematic-risk
- portfolio
stage: abstract-reasoning
status: validated
---

# Portfolio Diversification

## Core Idea
Diversification reduces portfolio risk by combining assets whose returns are not perfectly correlated, so that losses in some positions are offset by gains in others. As more assets are added, idiosyncratic (firm-specific) risk averages away, but systematic (market-wide) risk that affects all assets simultaneously cannot be diversified away. The benefit of adding another asset depends on its correlations with existing holdings, not on its standalone volatility. This distinction between diversifiable and non-diversifiable risk is fundamental: rational markets should only compensate investors for systematic risk, since idiosyncratic risk can be cheaply eliminated through diversification.

## How It's Best Learned
Simulate adding randomly chosen stocks to a portfolio and plot how the portfolio's standard deviation decreases with N, eventually flattening at the systematic risk floor. Compare portfolios that are diversified across industries vs. concentrated in a single sector to see the limits of naive diversification.

## Common Misconceptions
- Holding many stocks in the same industry provides little true diversification — sector correlation is high, leaving large systematic and sector-specific risk.
- Diversification guarantees neither positive returns nor avoidance of loss — it reduces risk but cannot eliminate it.
