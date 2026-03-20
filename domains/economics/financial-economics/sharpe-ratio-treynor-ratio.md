---
id: sharpe-ratio-treynor-ratio
title: 'Risk-Adjusted Return Measures: Sharpe and Treynor Ratios'
domain: economics
course: financial-economics
prerequisites:
- id: risk-adjusted-performance-measures
  type: hard
- id: expected-return-and-variance-of-assets
  type: hard
tags:
- performance-measurement
- risk-adjustment
- portfolio-evaluation
stage: advanced
status: draft
---

# Risk-Adjusted Return Measures: Sharpe and Treynor Ratios

## Core Idea
Sharpe ratio = (return − risk-free rate) / volatility measures return per unit of total risk. Treynor ratio = (return − risk-free rate) / beta measures return per unit of systematic risk. Sharpe ratio ranks portfolios for investors with undiversified wealth; Treynor ranks for diversified investors.

## Explainer

From your study of expected returns and variance, you know that raw return is an incomplete measure of investment performance. A portfolio that returns 20% by taking enormous risks is not necessarily better than one returning 12% with minimal volatility. Risk-adjusted return measures are designed to make portfolios comparable by asking: how much return did this portfolio earn per unit of risk it took on? The **Sharpe ratio** and **Treynor ratio** are the two most fundamental answers to that question — and they differ precisely in what they consider "risk."

The **Sharpe ratio** divides the portfolio's excess return (return above the risk-free rate) by the portfolio's standard deviation of returns. The risk-free rate is subtracted because you can earn it without any risk — a good manager must beat that baseline. Standard deviation is used as the risk measure because it captures total volatility: both idiosyncratic (company-specific) risk and systematic (market-wide) risk. A portfolio with a Sharpe ratio of 0.8 earns 0.8 units of excess return per unit of total volatility. The Sharpe ratio is the right measure when you're evaluating a portfolio that represents your **entire** investment — for example, a hedge fund investor who puts all their wealth in one fund, or an endowment evaluating a stand-alone allocation. In these cases, you cannot diversify away the idiosyncratic component, so total volatility is the relevant cost.

The **Treynor ratio** divides excess return by **beta** — the portfolio's sensitivity to the market — rather than by total standard deviation. Beta measures only systematic risk, the part that cannot be diversified away by holding a broad portfolio. The Treynor ratio is appropriate when evaluating a portfolio that is one component of a larger diversified portfolio. If you manage a growth equity sleeve within a larger institutional portfolio, the idiosyncratic risk in that sleeve is diversified away at the total portfolio level. What matters is how much market risk your sleeve contributes — its beta — relative to its excess return. A portfolio can have high standard deviation but low beta (it's volatile in idiosyncratic ways that wash out in a large portfolio), making it look poor on the Sharpe ratio but good on the Treynor ratio.

The practical implication is that the two measures can rank portfolios differently, and both rankings can be correct for different investors. Suppose Fund A has Sharpe 0.6, Treynor 0.9, and Fund B has Sharpe 0.8, Treynor 0.5. A pension fund building a diversified multi-manager portfolio prefers Fund A (higher Treynor); an individual who will hold only this fund prefers Fund B (higher Sharpe). Neither ratio is universally superior — the right measure depends on the investment context. A common mistake is applying the Treynor ratio to an undiversified investor, or the Sharpe ratio to a well-diversified institutional portfolio, and drawing incorrect conclusions about manager skill. Always start by asking: what does this portfolio's risk look like from the perspective of the investor who holds it?
