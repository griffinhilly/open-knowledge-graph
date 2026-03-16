---
id: market-maker-economics
title: Market Maker Economics and Bid-Ask Spreads
domain: economics
course: financial-economics
prerequisites:
- id: bid-ask-spreads-and-liquidity
  type: hard
- id: market-microstructure-fundamentals
  type: soft
builds-toward:
- market-microstructure-fundamentals
tags:
- market-microstructure
- liquidity
- trading
- spreads
stage: formal-systems
status: draft
---

# Market Maker Economics and Bid-Ask Spreads

## Core Idea
Market makers profit from the bid-ask spread but face inventory and adverse selection risks. The spread compensates for three costs: adverse selection (informed traders trade before prices adjust), inventory holding costs, and order processing costs. Understanding these components explains why spreads widen for illiquid assets, volatile markets, and during high-information environments.

## Explainer

From your study of bid-ask spreads and liquidity, you know that the bid-ask spread is the difference between the price at which a market maker will buy (the bid) and the price at which they will sell (the ask). A market maker is always on the other side of every trade: when you want to buy, the market maker sells to you at the ask; when you want to sell, the market maker buys from you at the bid. The spread is their compensation. But compensation for what, exactly? The three-component model of the spread gives a precise answer.

The **order processing cost component** is the simplest. Running a market-making operation requires technology, staff, and infrastructure. The spread must cover these fixed and variable costs spread across the volume of trades. For heavily traded assets like S&P 500 stocks, volume is so high that even a tiny spread generates enormous revenue; for thinly traded small-cap stocks or illiquid bonds, the same operating costs must be recovered from fewer trades, so spreads must be wider. This component alone explains why spread widths are inversely related to trading volume.

The **inventory holding cost component** reflects the risk that a market maker accumulates over time. When buyers arrive faster than sellers, the market maker's inventory grows — they end up holding more of the asset than they want. This inventory exposes them to price risk: if the asset falls in value while they are holding it, they take a loss. To manage this, market makers adjust their quotes: if they have too much inventory, they lower both bid and ask slightly to attract sellers and discourage buyers, gradually working back to neutral. The spread must be wide enough to compensate for this expected cost. Inventory risk is higher for more volatile assets (prices can move a lot against the market maker before they rebalance) and for assets with less frequent trading (slower inventory turnover means longer holding periods).

The **adverse selection cost component** is the most subtle and arguably the most important. Not all traders are equal. Some traders are **informed** — they know something about the true value of the asset that is not yet reflected in the price, and they trade precisely because of this advantage. The market maker cannot tell informed traders from uninformed ones (liquidity traders who need to buy or sell for portfolio rebalancing or cash needs). When an informed trader buys from the market maker, it is likely because the true value is above the ask price — and the market maker sold at a disadvantageous price. The market maker loses on trades with informed investors and only profits from trades with uninformed ones. The spread must be wide enough that profits from uninformed trading offset losses from informed trading. The Glosten-Milgrom model formalizes this: the bid-ask spread is directly proportional to the probability that the counterparty is informed and the expected magnitude of their information advantage.

These three components together explain several empirical patterns. Spreads widen around earnings announcements, central bank decisions, and other scheduled information events — because the fraction of informed traders rises sharply. Spreads widen during market stress and high volatility — inventory risk increases. Spreads narrow dramatically for large-cap stocks over the past two decades as electronic trading reduced order processing costs to near zero and competition among market makers intensified. **High-frequency trading (HFT)** firms now dominate market making in equity markets; they earn the spread while managing inventory risk through rapid position adjustments and earning the adverse selection component through superior speed rather than information.


