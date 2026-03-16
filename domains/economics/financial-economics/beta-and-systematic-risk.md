---
id: beta-and-systematic-risk
title: Beta and Systematic Risk
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: bivariate-regression
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- capital-asset-pricing-model
tags:
- beta
- systematic-risk
- market-risk
- covariance
- capm
stage: formal-systems
status: validated
---

# Beta and Systematic Risk

## Core Idea
Beta (β) measures an asset's sensitivity to market-wide movements — its systematic (non-diversifiable) risk. Formally, β = Cov(rᵢ, rₘ) / Var(rₘ), estimated by regressing historical asset returns on market returns. A beta of 1 means the asset moves in lockstep with the market; beta > 1 amplifies market swings (cyclical or technology stocks); beta < 1 dampens them (utilities, consumer staples); negative beta means the asset tends to move against the market. Because idiosyncratic risk can be freely diversified away, only beta — not total volatility — determines the risk premium in equilibrium.

## How It's Best Learned
Estimate beta by regressing monthly stock returns on index returns over a 5-year window and interpret the slope coefficient. Compare betas across cyclical (high beta) and defensive (low beta) sectors. Understand the Hamada equation relating levered and unlevered beta to see how financial leverage raises beta.

## Common Misconceptions
- A highly volatile stock with low correlation to the market can have low beta — volatility and systematic risk are distinct concepts.
- Beta estimated from historical data is unstable and sensitive to the chosen time window and market proxy, making forward-looking beta a source of significant estimation error.

## Explainer

From portfolio diversification, you know that combining assets reduces risk — but not all risk goes away. Idiosyncratic risks (a company's CEO resigns, a product fails a safety test, a competitor wins a key contract) wash out when you hold many stocks, because these events are uncorrelated across firms. What cannot be diversified away is **systematic risk**: the risk that moves the whole market at once — recessions, interest rate spikes, geopolitical crises. Every stock is exposed to this background noise, and the question beta answers is: *how exposed?*

Beta is the slope coefficient from regressing an asset's historical returns on the market's returns — precisely the bivariate regression you studied as a prerequisite. If you plot monthly returns of a stock against the S&P 500 over five years, the slope of the best-fit line is beta. A slope of 1 means the asset tracks the market one-for-one: when the market rises 10%, the stock rises about 10%. A beta of 1.5 means the stock amplifies market moves — up 15% when the market rises 10%, down 15% when it falls 10%. A beta of 0.5 means the stock is relatively insulated from market swings. The formally correct expression is β = Cov(rᵢ, rₘ) / Var(rₘ), which from your correlation work you can recognize as the ratio that captures how much of the market's variance the asset shares, normalized by total market variance.

The critical insight — which follows directly from why diversification works — is that only beta, not total volatility, should command a risk premium in a well-functioning market. If a stock has high volatility but low correlation to the market (think: a biotech company whose outcomes depend on drug trial results, not the economic cycle), you can neutralize its idiosyncratic risk by holding it alongside other assets. The market will not pay you extra expected return for bearing risk you could have easily eliminated by diversifying. But systematic risk is unavoidable — no amount of diversification removes it — so investors rationally demand higher expected return to hold high-beta assets. This is the economic logic that CAPM will formalize.

In practice, measuring beta involves several judgment calls. The choice of time window (1 year vs. 5 years), return frequency (daily, weekly, monthly), and market proxy (S&P 500, total market index, global index) all affect the estimate significantly. Furthermore, **beta is not stable**: a company's beta changes as its business mix, leverage, and macro exposure evolve. Financial leverage also mechanically raises beta — the **Hamada equation** shows that levered beta equals unlevered (asset) beta scaled up by (1 + D(1-T)/E), because debt amplifies equity's sensitivity to business fluctuations. For valuation and cost-of-capital work, analysts often "unlever" beta to isolate pure business risk, then re-lever at the target capital structure. This distinction between asset beta and equity beta is essential when comparing firms with different financing structures.
