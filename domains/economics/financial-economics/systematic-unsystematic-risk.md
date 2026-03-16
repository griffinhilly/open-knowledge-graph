---
id: systematic-unsystematic-risk
title: Systematic and Unsystematic Risk Decomposition
domain: economics
course: financial-economics
prerequisites:
- id: beta-and-systematic-risk
  type: hard
builds-toward:
- cost-of-equity-capm
tags:
- risk-measurement
- beta
- capm
stage: formal-systems
status: draft
---

# Systematic and Unsystematic Risk Decomposition

## Core Idea
Total risk = systematic risk (market-related, β) + unsystematic risk (firm-specific, diversifiable). Well-diversified portfolios eliminate unsystematic risk; only systematic risk remains and is priced in equilibrium, determining expected returns via CAPM.

## How It's Best Learned
Regress stock returns on market returns; the slope is beta (systematic risk exposure). Calculate R² to see what fraction of risk is systematic versus unsystematic.

## Explainer

You already know that beta measures a stock's sensitivity to market movements — a stock with β = 1.5 tends to move 1.5% for every 1% move in the market. This topic makes that picture more precise by asking: what is the rest of the stock's movement doing? If beta explains the market-related part of a stock's return, something else must explain the departures from that pattern. The answer is **unsystematic risk** — variation driven by firm-specific events that have nothing to do with the broader market.

Think about the sources of stock price movements. When the Fed raises interest rates, nearly every stock falls — this is systematic risk, because the shock hits the whole market. When a pharmaceutical company announces that its flagship drug failed a clinical trial, that company's stock plummets while the rest of the market barely notices — this is unsystematic risk, also called **idiosyncratic risk** or **firm-specific risk**. The decomposition is: Total Risk = Systematic Risk + Unsystematic Risk, or in variance terms: σ²_i = β²_i·σ²_m + σ²_ε, where σ²_m is market variance and σ²_ε is the variance of the firm-specific residual.

The crucial insight is that these two components are treated very differently by the market's pricing mechanism. Unsystematic risk is **diversifiable**: if you hold a portfolio of 30 or more stocks, the firm-specific shocks tend to cancel out across positions. One company's drug failure is offset by another's surprise earnings beat. As you add more stocks, idiosyncratic variance approaches zero in a well-diversified portfolio. Systematic risk, by contrast, cannot be diversified away — when the whole market falls, every stock in your portfolio falls too.

Because rational investors can eliminate unsystematic risk cheaply through diversification, the market does not compensate them for bearing it. You receive no additional expected return for holding a concentrated position in a single volatile stock, because the idiosyncratic volatility could have been eliminated costlessly. What the market does price is **systematic risk** — the component measured by beta that cannot be escaped no matter how broadly you diversify. This is the foundation of CAPM: expected return is a function of beta alone, not total volatility. A stock with high total variance but low beta (because most of its variance is idiosyncratic) should have a low expected return. A stock with modest total variance but high beta should have a high expected return. The R² from regressing a stock's returns on the market tells you exactly what fraction of total risk is systematic — and therefore what fraction is being priced.
