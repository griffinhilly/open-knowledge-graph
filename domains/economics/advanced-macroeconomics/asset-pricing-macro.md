---
id: asset-pricing-macro
title: Asset Pricing and Macroeconomic Implications
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: hard
- id: euler-equation-consumption
  type: hard
builds-toward:
- financial-frictions-credit-constraints
tags:
- asset-pricing
- returns
- macroeconomy
stage: advanced
status: draft
---

# Asset Pricing and Macroeconomic Implications

## Core Idea
The Euler equation links asset prices to consumption growth and preferences: asset returns must compensate for the consumption risk they carry. Higher expected returns on risky assets (the risk premium) reflect compensation for bearing consumption risk. Macroeconomic conditions affect asset prices by changing expected consumption paths and the covariance of returns with consumption; financial crises and downturns are times when assets become riskier relative to consumption, causing price declines and return spikes.

## Explainer

From your work on expected returns and portfolio variance, you understand that investors care about risk-return tradeoffs. From the consumption Euler equation, you know that an optimizing household equates the marginal cost of consuming one less dollar today to the expected marginal benefit of investing that dollar and consuming the proceeds tomorrow. Asset pricing in a macroeconomic context fuses these two ideas: the price of any asset is determined by how its payoff correlates with the household's future consumption.

The core insight is the **stochastic discount factor** (SDF), which emerges directly from the Euler equation. For a household with time-separable utility, the SDF equals the discounted ratio of future to current marginal utility: β × u'(c_{t+1}) / u'(c_t). An asset's price equals the expected value of its future payoff multiplied by this SDF. When consumption is high, marginal utility is low, so payoffs received in good times are worth less. When consumption is low (recessions), marginal utility is high, so payoffs received in bad times are worth more. This is the fundamental pricing principle: **assets that pay off when you need money most are more valuable than assets that pay off when you are already doing well**.

The **equity premium** — the extra return stocks earn over safe bonds — follows from this logic. Stock returns are procyclical: they tend to be high when the economy is booming and low (or negative) during recessions. This means stocks pay off precisely when marginal utility is low and fail you when marginal utility is high. Investors demand extra compensation for holding this unfavorable pattern of payoffs. The risk premium on any asset is proportional to the negative covariance between its return and the SDF: assets whose returns covary negatively with consumption growth (falling when consumption falls) must offer higher expected returns. Safe bonds, by contrast, offer a guaranteed payoff regardless of the state of the economy, so they earn only the risk-free rate.

A persistent puzzle — the **equity premium puzzle** — is that the observed premium (historically 6-8% per year) is far larger than standard models predict given plausible levels of risk aversion. This has driven macroeconomists to explore richer preference specifications (habit formation, recursive utility, loss aversion) and to examine how macroeconomic tail risks — rare disasters like depressions or financial crises — affect the SDF. During crises, consumption drops sharply, the SDF spikes, and asset prices plummet as investors reprice risk. Understanding this feedback between macroeconomic conditions and asset valuations is essential for analyzing financial stability, monetary policy transmission, and the real effects of financial market disruptions.
