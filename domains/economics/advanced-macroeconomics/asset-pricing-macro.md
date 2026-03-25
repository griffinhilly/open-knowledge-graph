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
- id: asset-pricing-macroeconomy
  type: soft
builds-toward:
- financial-frictions-credit-constraints
tags:
- asset-pricing
- returns
- macroeconomy
stage: expert
status: validated
---
# Asset Pricing and Macroeconomic Implications

## Core Idea
The Euler equation links asset prices to consumption growth and preferences: asset returns must compensate for the consumption risk they carry. Higher expected returns on risky assets (the risk premium) reflect compensation for bearing consumption risk. Macroeconomic conditions affect asset prices by changing expected consumption paths and the covariance of returns with consumption; financial crises and downturns are times when assets become riskier relative to consumption, causing price declines and return spikes.

## Questions

```yaml
- question: "Investor A holds stocks that pay high returns during economic booms but fall sharply during recessions. Investor B holds government bonds that pay a small but guaranteed return regardless of economic conditions. Which investor demands a higher expected return, and what is the fundamental reason?"
  type: multiple-choice
  options:
    - "Investor B, because guaranteed returns are rarer and therefore command a scarcity premium"
    - "Investor A, because stocks pay off when the investor is already consuming well and fail when consumption is most needed, so they carry consumption risk that requires compensation"
    - "Investor A, simply because stocks have higher return variance, and all variance must be compensated"
    - "Neither; in an efficient market, risk-adjusted returns equalize across all assets"
  answer: 1
  explanation: "The key insight is that risk is defined by WHEN an asset fails you, not just how variable its returns are. Stocks are procyclical: they pay off in booms (when household consumption and marginal utility are low) and fail in recessions (when consumption is low and marginal utility is high). This is the worst possible pattern — the asset disappoints exactly when additional income would be most valuable. Investors demand extra return to hold this pattern of payoffs. Option C is wrong because variance alone is insufficient — an asset that is highly variable but uncorrelated with consumption growth would not earn a premium in this framework."

- question: "The 'equity premium puzzle' refers to which of the following observations?"
  type: multiple-choice
  options:
    - "Stock prices are too volatile to be explained by rational expectations about future dividends"
    - "The observed historical premium of stocks over bonds (~6–8% per year) is far larger than standard consumption-based models can explain using plausible levels of risk aversion"
    - "Equity markets are systematically inefficient because prices do not fully reflect macroeconomic information"
    - "Investors demand a premium for holding equities due to their higher transaction costs relative to bonds"
  answer: 1
  explanation: "The equity premium puzzle (Mehra and Prescott, 1985) is that the observed extra return on stocks over bonds is too large to be rationalized by the stochastic discount factor framework unless households have implausibly high risk aversion (coefficients of 30–50 or more, when empirical estimates suggest values of 1–5). This has spawned research into habit formation, recursive utility, rare disasters, and long-run risk as ways to generate higher effective risk aversion without requiring unrealistic preference parameters. It is a puzzle about model fit, not about market efficiency."

- question: "An asset that reliably pays off during recessions — when aggregate consumption is falling and marginal utility is high — is more valuable and will carry a lower expected return than an otherwise comparable procyclical asset."
  type: true-false
  answer: true
  explanation: "This follows directly from the stochastic discount factor (SDF) framework. The SDF = β·u'(c_{t+1})/u'(c_t) is high in recessions (when future consumption is low and marginal utility is high) and low in booms. An asset that pays off when the SDF is high (i.e., in recessions) has a high expected SDF-weighted payoff, so it commands a high price today — and a high current price means a lower expected return. Counter-cyclical assets are effectively insurance; people pay for insurance, accepting lower expected returns in exchange for payoffs precisely when they are most needed."

- question: "In the stochastic discount factor framework, the expected return premium an asset must offer above the risk-free rate depends primarily on the variance of the asset's own returns."
  type: true-false
  answer: false
  explanation: "The risk premium depends on the COVARIANCE between the asset's return and the stochastic discount factor — equivalently, the covariance between the return and (marginal utility of) consumption growth. An asset that is highly volatile but whose volatility is uncorrelated with consumption growth carries no consumption risk and earns no premium above the risk-free rate. An asset with low variance but high negative covariance with consumption growth (failing in recessions) earns a large premium. Variance is not the relevant measure — covariance with the SDF is."

- question: "Explain why stocks must offer a positive expected return premium over safe bonds in the macroeconomic asset pricing framework, using the concept of marginal utility of consumption."
  type: short-answer
  answer: "Stock returns are procyclical: they are high in booms and low or negative in recessions. When stocks fail (recessions), household consumption is falling and the marginal utility of each additional dollar is high — that is exactly when investors most need their assets to perform. Safe bonds, by contrast, pay off regardless of economic conditions, providing income when it may be most needed. Investors rationally require extra compensation — a positive risk premium — for holding an asset that systematically disappoints them when marginal utility is highest and performs well when marginal utility is already low."
  explanation: "The formal expression is: E[R_stock] − R_f = −Cov(R_stock, m)/E[m], where m = β·u'(c_{t+1})/u'(c_t) is the stochastic discount factor. Since stocks covary negatively with m (stocks fall when m is high, i.e., in recessions), the covariance term is negative, yielding a positive premium. Safe bonds have near-zero covariance with m, so their premium is near zero. The equity premium is essentially the market price of consumption risk."
```

## Explainer

From your work on expected returns and portfolio variance, you understand that investors care about risk-return tradeoffs. From the consumption Euler equation, you know that an optimizing household equates the marginal cost of consuming one less dollar today to the expected marginal benefit of investing that dollar and consuming the proceeds tomorrow. Asset pricing in a macroeconomic context fuses these two ideas: the price of any asset is determined by how its payoff correlates with the household's future consumption.

The core insight is the **stochastic discount factor** (SDF), which emerges directly from the Euler equation. For a household with time-separable utility, the SDF equals the discounted ratio of future to current marginal utility: β × u'(c_{t+1}) / u'(c_t). An asset's price equals the expected value of its future payoff multiplied by this SDF. When consumption is high, marginal utility is low, so payoffs received in good times are worth less. When consumption is low (recessions), marginal utility is high, so payoffs received in bad times are worth more. This is the fundamental pricing principle: **assets that pay off when you need money most are more valuable than assets that pay off when you are already doing well**.

The **equity premium** — the extra return stocks earn over safe bonds — follows from this logic. Stock returns are procyclical: they tend to be high when the economy is booming and low (or negative) during recessions. This means stocks pay off precisely when marginal utility is low and fail you when marginal utility is high. Investors demand extra compensation for holding this unfavorable pattern of payoffs. The risk premium on any asset is proportional to the negative covariance between its return and the SDF: assets whose returns covary negatively with consumption growth (falling when consumption falls) must offer higher expected returns. Safe bonds, by contrast, offer a guaranteed payoff regardless of the state of the economy, so they earn only the risk-free rate.

A persistent puzzle — the **equity premium puzzle** — is that the observed premium (historically 6-8% per year) is far larger than standard models predict given plausible levels of risk aversion. This has driven macroeconomists to explore richer preference specifications (habit formation, recursive utility, loss aversion) and to examine how macroeconomic tail risks — rare disasters like depressions or financial crises — affect the SDF. During crises, consumption drops sharply, the SDF spikes, and asset prices plummet as investors reprice risk. Understanding this feedback between macroeconomic conditions and asset valuations is essential for analyzing financial stability, monetary policy transmission, and the real effects of financial market disruptions.
