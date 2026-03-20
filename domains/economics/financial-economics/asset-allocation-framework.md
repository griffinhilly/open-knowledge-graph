---
id: asset-allocation-framework
title: Asset Allocation Framework
domain: economics
course: financial-economics
prerequisites:
- id: efficient-frontier-portfolio-theory
  type: hard
- id: capital-asset-pricing-model
  type: soft
builds-toward:
- portfolio-rebalancing-strategies
tags:
- asset-allocation
- portfolio
- strategy
stage: advanced
status: draft
---

# Asset Allocation Framework

## Core Idea
Strategic asset allocation sets long-term target weights for stocks, bonds, and other asset classes based on investor risk tolerance, time horizon, and return objectives. Tactical allocation makes short-term deviations to exploit market opportunities. The allocation decision typically dominates security selection in explaining portfolio returns.

## How It's Best Learned
Build a strategic allocation for a sample investor profile using efficient frontier optimization, then examine how allocation weights would shift across different market regimes.

## Explainer

From your study of the efficient frontier, you know that any combination of risky assets traces out a curve in mean-variance space, and the optimal portfolio lies at the tangency point where the Capital Market Line (CML) touches the frontier. **Asset allocation** is the practical application of this insight: rather than treating portfolio construction as a pure optimization over individual securities, you first decide how to divide wealth across broad **asset classes** — equities, bonds, real estate, commodities, cash — and then, within each class, select specific holdings. The empirical case for this sequencing is strong: studies consistently show that the asset class weights explain the vast majority of long-term portfolio performance variance, while security selection within classes contributes far less.

**Strategic asset allocation (SAA)** sets long-run target weights based on an investor's objectives and constraints. A young investor with a 30-year horizon and high risk tolerance might hold 80% equities and 20% bonds; a retiree drawing down wealth might reverse those proportions. The process maps directly onto efficient frontier mechanics: given expected returns, volatilities, and correlations for each asset class, you find the portfolio on the frontier that matches the investor's risk tolerance. But SAA is forward-looking and must account for constraints OLS-style optimization ignores — regulatory restrictions, liquidity needs, tax treatment, and the investor's total wealth including human capital (a young worker with a stable salary has implicit bond-like income, which should push their financial portfolio toward more equity).

**Tactical asset allocation (TAA)** introduces deliberate short-term deviations from the strategic weights. If bonds appear overvalued relative to historical norms, a manager might temporarily underweight bonds and overweight equities. TAA attempts to exploit predictable return variation — the kind that market anomalies research documents. Unlike SAA, which is driven by investor fundamentals, TAA is a bet on the manager's ability to time markets or identify temporary mispricings. Evidence on whether TAA adds value net of costs is mixed; many practitioners argue that the behavioral discipline of sticking to SAA outperforms opportunistic deviations for most investors.

The practical implementation challenge is **rebalancing**: as asset prices move, the realized weights drift from the strategic targets. A portfolio that started at 60% equity drifts higher in a bull market, increasing risk beyond the investor's intended tolerance. Periodic rebalancing restores target weights, but it incurs transaction costs and triggers taxable events. The asset allocation framework therefore extends beyond a single-period optimization into a dynamic problem — how often to rebalance, whether to use bands or calendar rules, and how tax efficiency should modify the theoretical optimum. This is the bridge toward the portfolio rebalancing strategies this topic builds toward.
