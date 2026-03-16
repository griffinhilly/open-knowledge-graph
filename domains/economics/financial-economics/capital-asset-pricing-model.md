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
  type: soft
- id: correlation-coefficient
  type: hard
- id: covariance-correlation-theory
  type: hard
- id: optimization-multivariable-basics
  type: soft
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

## Questions

```yaml
- question: "According to CAPM, what does a stock's beta measure?"
  type: multiple-choice
  options:
    - "The stock's total return volatility (standard deviation)"
    - "The stock's expected return above the risk-free rate"
    - "The stock's sensitivity to market-wide movements — its systematic risk relative to the market"
    - "The stock's idiosyncratic risk that can be eliminated through diversification"
  answer: 2
  explanation: "Beta measures how much the stock moves with the market — technically, it is the covariance of the stock's returns with the market's returns divided by the variance of the market. A beta of 1.5 means the stock tends to move 1.5% for every 1% market move. Total volatility (standard deviation) includes both systematic and idiosyncratic risk; CAPM says only the systematic component (beta) is priced because idiosyncratic risk can be diversified away."

- question: "According to CAPM, a fully diversified investor should demand compensation for all risk in a stock, including company-specific (idiosyncratic) risk."
  type: true-false
  answer: false
  explanation: "This is the central insight of CAPM: idiosyncratic risk — risk unique to a single company, like a CEO departure or a product recall — can be eliminated by holding a diversified portfolio. Rational investors will not pay a premium to avoid risk they can diversify away for free. Therefore, the market only compensates for systematic risk (beta), which cannot be eliminated through diversification because it comes from economy-wide factors."

- question: "What does it mean for a stock to plot above the Security Market Line (SML), and what would a CAPM investor do?"
  type: short-answer
  answer: "A stock above the SML offers a higher expected return than CAPM predicts for its level of beta — it is underpriced (alpha is positive). A CAPM investor would buy it, since it delivers more return per unit of systematic risk than equilibrium requires."
  explanation: "The SML maps every level of beta to the return that exactly compensates for systematic risk. Points above the line have positive alpha — they are delivering excess return for their risk. In a CAPM world, investors would rush to buy such stocks, bidding up the price and driving the expected return down until the stock sits back on the SML. Points below the line are overpriced and would be sold. In equilibrium, all assets lie exactly on the SML."
```

## Explainer

CAPM builds directly on portfolio theory. You learned from the efficient frontier that adding assets to a portfolio reduces risk through diversification — but only up to a point. Some risk cannot be diversified away no matter how many assets you hold, because it comes from economy-wide forces (recessions, interest rate changes, inflation) that affect all assets simultaneously. CAPM calls this systematic risk. The remaining risk — unique to a single company — is idiosyncratic risk, and a well-diversified portfolio eliminates it entirely.

The punchline is a pricing implication: if rational investors can eliminate idiosyncratic risk for free by diversifying, they will not demand extra return for bearing it. The market will price assets so that only systematic risk earns a return premium. This is why CAPM collapses the entire risk of an asset into a single number: beta (β), defined as the covariance of the asset's returns with the market portfolio, divided by the variance of the market. Beta is a pure measure of systematic risk — how much the asset moves with the overall market.

The CAPM equation is then: E[rᵢ] = rᶠ + βᵢ(E[rₘ] − rᶠ). Read it as: the expected return on asset i equals the risk-free rate (what you earn for waiting, with no risk) plus beta times the market risk premium (what the market pays per unit of systematic risk). If an asset has β = 0, it moves independently of the market, so you only earn the risk-free rate. If β = 2, the asset is twice as sensitive to market swings and commands twice the market risk premium.

The Security Market Line (SML) is the graph of this relationship — expected return on the y-axis, beta on the x-axis. In equilibrium, every correctly priced asset lies exactly on the SML. A stock plotting above the line has a positive alpha: it offers more return than its beta justifies. In theory, investors would buy it until the price rises enough to push expected return back to the SML. A stock below the line is overpriced and would be sold. Alpha — deviation from the SML — is the central concept in active portfolio management.

CAPM's assumptions are strong: homogeneous expectations, perfect markets, a single period, no taxes or transaction costs, and a market portfolio that includes every investable asset in the world. In practice, we use an index like the S&P 500 as a rough proxy for the market, and the empirical track record is mixed. Fama and French showed that small-cap and value stocks earn returns that CAPM cannot explain with beta alone. Yet CAPM persists as the baseline for cost-of-equity estimation in corporate finance — its clarity and simplicity make it hard to replace even when its predictions are imperfect.
