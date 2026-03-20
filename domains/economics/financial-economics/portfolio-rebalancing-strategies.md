---
id: portfolio-rebalancing-strategies
title: Portfolio Rebalancing Strategies
domain: economics
course: financial-economics
prerequisites:
- id: asset-allocation-framework
  type: hard
- id: portfolio-diversification
  type: soft
builds-toward:
- value-at-risk-measurement
tags:
- rebalancing
- portfolio
- discipline
stage: advanced
status: draft
---

# Portfolio Rebalancing Strategies

## Core Idea
Rebalancing realigns portfolio weights to target allocations, either on a fixed calendar schedule or when weights drift beyond tolerance bands. Rebalancing enforces buy-low, sell-high discipline and manages drift from changing market values. The frequency and trigger rules balance transaction costs against drift risk.

## Explainer

From your asset allocation work, you know that a portfolio's risk-return profile depends critically on how assets are weighted. A target of 60% equities and 40% bonds reflects a deliberate choice about expected return, volatility, and downside risk. But markets do not hold still. If equities return 20% while bonds return 2%, the equity weight drifts upward — perhaps to 65% or 68% — making the portfolio more aggressive than intended. The investor's actual risk exposure has changed simply due to market movements, without any active decision being made. **Rebalancing** is the discipline of restoring the original intended weights by selling what has grown above target and buying what has fallen below.

The mechanical consequence of systematic rebalancing is a **contrarian discipline**: it forces you to sell recent winners and buy recent losers at regular intervals. This is behaviorally difficult — selling an asset that just performed well feels like leaving money on the table, and buying an underperformer feels uncomfortable. But across long time horizons with mean-reverting assets, this systematic contrarianism has historically added incremental return (the "rebalancing bonus"), particularly in portfolios with volatile, uncorrelated asset classes. The intuition from your diversification background: when two assets have low or negative correlation, they take turns outperforming, and rebalancing captures this by harvesting the out-performer's gains and repositioning into the laggard before the cycle reverses.

There are two primary trigger mechanisms. **Calendar-based rebalancing** rebalances on a fixed schedule — monthly, quarterly, or annually — regardless of current drift. It is simple to execute and communicate but may trade unnecessarily when weights are near target or miss large drifts between dates. **Tolerance-band rebalancing** trades only when an asset weight drifts beyond a specified boundary — for example, ±5 percentage points from target. The portfolio is monitored continuously (or daily), and a trade is triggered only when a threshold is breached. This is more responsive to actual drift but requires ongoing monitoring. Many practitioners use a hybrid: check on a calendar schedule, but only execute a trade if weights have drifted beyond the tolerance band.

The fundamental tradeoff in rebalancing design is **transaction costs versus drift risk**. Every rebalancing trade incurs costs: brokerage commissions, bid-ask spreads, and in taxable accounts, realized capital gains taxes. More frequent rebalancing keeps drift small but generates more taxable events and transaction costs. Wider tolerance bands allow more drift before triggering trades, reducing turnover but allowing the portfolio's risk profile to wander further from target. The optimal strategy depends on the portfolio's size (larger portfolios absorb fixed costs more easily), the liquidity of the asset classes involved, and the account's tax treatment. In tax-advantaged accounts (IRAs, 401ks), rebalancing is relatively low-cost and should be done aggressively. In taxable accounts, directing new contributions into underweight assets is often preferable to selling overweight assets and realizing gains — achieving the same rebalancing effect without a tax trigger.
