---
id: technical-analysis-and-market-efficiency
title: Technical Analysis and Market Efficiency Evidence
domain: economics
course: financial-economics
prerequisites:
- id: market-efficiency-weak-form
  type: hard
builds-toward:
- behavioral-biases-investor-psychology
tags:
- technical-analysis
- market-efficiency
- empirical-evidence
stage: formal-systems
status: draft
---

# Technical Analysis and Market Efficiency Evidence

## Core Idea
Technical analysis uses price and volume patterns to forecast returns. If markets are weak-form efficient, technical analysis should not persistently outperform. Empirical evidence is mixed: short-term momentum exists, contradicting weak-form efficiency, while long-term mean reversion also appears.

## How It's Best Learned
Test a simple technical trading rule (e.g., moving average crossover) on historical data. Calculate excess returns and assess statistical significance while controlling for look-ahead bias.

## Explainer

Your weak-form efficiency prerequisite establishes the baseline claim: if markets are weak-form efficient, all information contained in past prices and volume is already reflected in current prices, so no trading strategy based solely on price history can earn persistent excess returns. Technical analysis is the practice that this claim says should not work. The empirical evidence creates a genuine tension, and understanding that tension carefully is more valuable than resolving it too quickly in either direction.

**Technical analysis** encompasses a wide range of tools — moving averages, support and resistance levels, head-and-shoulders patterns, relative strength indicators — all united by the premise that price and volume history contains information about future price movements. A **moving average crossover** strategy, for example, buys a stock when its short-term average (say, 50-day) crosses above its long-term average (200-day) and sells when the reverse occurs. The theory is that such crossovers signal momentum: prices that have recently accelerated upward will continue rising. If weak-form efficiency held strictly, this strategy should yield no risk-adjusted excess return — any predictability in price patterns would be immediately arbitraged away.

The empirical record is more complicated. **Short-term momentum** — the tendency of assets that have recently outperformed to continue outperforming over the next 3–12 months — is one of the most replicated anomalies in academic finance. Jegadeesh and Titman documented it in U.S. equities in 1993, and it has been found in most major markets and asset classes since. This is a direct challenge to weak-form efficiency. Conversely, **long-term mean reversion** — the tendency for assets that have dramatically outperformed over 3–5 years to underperform subsequently — was documented by De Bondt and Thaler and interpreted as evidence of investor overreaction. These two findings are logically consistent (momentum at medium horizons, reversal at long horizons) but together suggest price history contains information, contradicting the weak-form claim.

The correct interpretation remains contested. One view is that momentum reflects **risk premia** rather than inefficiency: momentum stocks might simply be more exposed to some systematic risk factor, and their higher returns are fair compensation. A second view is that momentum reflects **behavioral biases** — investors underreact to information initially (supporting continued price movement in the original direction) and then overreact eventually (causing mean reversion). A third view is that documented anomalies suffer from **data mining**: with enough variables and enough historical data, some strategy will appear to work by chance, especially when survivorship bias inflates the apparent performance of historical studies. The deeper lesson is that weak-form efficiency is not a binary fact but a claim about the magnitude and exploitability of price predictability, after accounting for transaction costs, risk, and the limits of arbitrage.
