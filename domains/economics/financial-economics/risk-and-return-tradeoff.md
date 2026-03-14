---
id: risk-and-return-tradeoff
title: Risk and Return Tradeoff
domain: economics
course: financial-economics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
- id: consumer-theory-utility
  type: soft
- id: stock-valuation-fundamentals
  type: soft
- id: term-structure-of-interest-rates
  type: soft
- id: yield-to-maturity
  type: soft
builds-toward:
- expected-return-and-variance-of-assets
- portfolio-diversification
- capital-asset-pricing-model
tags:
- risk-premium
- risk-aversion
- return
- sharpe-ratio
stage: formal-systems
status: validated
---
# Risk and Return Tradeoff

## Core Idea
In competitive financial markets, higher expected returns come only by accepting higher risk — there is no risk-free arbitrage. Risk-averse investors require a risk premium above the risk-free rate as compensation for bearing uncertainty. Standard measures of investment risk are the variance and standard deviation of returns. The fundamental question of asset pricing is: exactly which risks command a premium and how large is that premium? The risk-return tradeoff is the organizing principle of modern portfolio theory and the motivation for every asset pricing model.

## How It's Best Learned
Examine historical return data for T-bills, government bonds, and equities to see the empirical risk-return gradient across asset classes. Formalize risk aversion with a utility function and show how it implies a demand for a risk premium. Compute Sharpe ratios to compare risk-adjusted performance.

## Common Misconceptions
- Total volatility (standard deviation) is one measure of risk but not the only relevant one — downside risk, tail risk, and illiquidity are separately important in practice.
- Diversification eliminates idiosyncratic risk but not systematic (market-wide) risk; the latter is what the market actually compensates investors for bearing.
