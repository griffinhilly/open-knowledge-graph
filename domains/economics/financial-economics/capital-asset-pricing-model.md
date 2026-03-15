---
id: capital-asset-pricing-model
title: Capital Asset Pricing Model (CAPM)
domain: economics
course: financial-economics
prerequisites:
- id: efficient-frontier-portfolio-theory
  type: hard
- id: beta-and-systematic-risk
  type: hard
- id: expected-value
  type: soft
- id: variance-of-random-variables
  type: soft
- id: linear-regression
  type: soft
- id: dividend-discount-model
  type: soft
- id: covariance-between-random-variables
  type: soft
- id: eigenvalues-eigenvectors
  type: soft
- id: constrained-optimization-lagrange
  type: soft
- id: linear-algebra
  type: hard
- id: correlation-coefficient
  type: hard
- id: covariance-correlation-theory
  type: hard
- id: optimization-multivariable-basics
  type: hard
builds-toward:
- arbitrage-pricing-theory
- risk-adjusted-performance-measures
- efficient-market-hypothesis
tags:
- capm
- security-market-line
- expected-return
- cost-of-equity
stage: formal-systems
status: validated
---
# Capital Asset Pricing Model (CAPM)

## Core Idea
The Capital Asset Pricing Model (CAPM) is an equilibrium model determining the required return of any asset solely from its systematic risk: E[rᵢ] = rₓ + βᵢ(E[rₘ] − rₓ). The Security Market Line (SML) graphs this relationship — correctly priced assets lie on the SML; assets above are underpriced (offering return above what risk warrants) and those below are overpriced. CAPM's core insight is that because all other risk can be diversified away in a large portfolio, only beta — the covariance with the market — earns a compensation. Despite restrictive assumptions (homogeneous expectations, no taxes, perfect markets), CAPM remains the dominant framework in practice for estimating the cost of equity capital.

## How It's Best Learned
Estimate a stock's beta from historical returns and apply CAPM to compute the cost of equity for discounting cash flows in a valuation model. Plot stocks on the SML and identify apparent mispricings. Study the empirical literature — the size and value factors reveal where CAPM fails cross-sectionally.

## Common Misconceptions
- CAPM's empirical predictions are mixed at best — the Fama-French multi-factor model explains cross-sectional returns substantially better.
- The true market portfolio includes all investable assets globally, not just a stock index — in practice we use an index as an imperfect proxy.
