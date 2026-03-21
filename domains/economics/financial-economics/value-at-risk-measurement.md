---
id: value-at-risk-measurement
title: Value-at-Risk Measurement
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: variance-of-random-variables
  type: hard
- id: quantiles-and-percentiles
  type: hard
- id: probability-distributions
  type: hard
- id: normal-distribution-theory
  type: soft
tags:
- var
- risk-measurement
- quantitative
stage: formal-systems
status: draft
---

# Value-at-Risk Measurement

## Core Idea
Value at Risk (VaR) quantifies the maximum portfolio loss over a given time horizon at a specified confidence level (e.g., 95% or 99%). VaR can be calculated parametrically (assuming normal returns), historically, or through Monte Carlo simulation. VaR is widely used in regulation and risk management but underestimates tail risk (extreme losses).

## Questions

```yaml
- question: "A portfolio manager reports a one-day 99% VaR of $500,000. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The portfolio will lose no more than $500,000 on any given trading day"
    - "There is a 1% probability that the daily loss will exceed $500,000"
    - "The portfolio is expected to lose $500,000 on 99% of trading days"
    - "In the worst-case scenario, losses will be exactly $500,000"
  answer: 1
  explanation: "99% VaR of $500,000 means: with 99% probability, the daily loss will be $500,000 or less — equivalently, there is a 1% chance of losing MORE than $500,000. Option A is the most dangerous misconception: VaR is not a loss cap or maximum. In the worst 1% of days, losses can be $500,001 or $50 million — VaR says nothing about that. Option C reverses the probability completely."

- question: "Portfolio A has a 99% one-day VaR of $1 million with average tail losses of $1.1 million. Portfolio B also has a 99% VaR of $1 million but average tail losses of $10 million. What does this illustrate?"
  type: multiple-choice
  options:
    - "Portfolio B is better diversified because larger tail losses indicate wider exposure"
    - "VaR fails to distinguish between portfolios with identical threshold losses but very different tail severities"
    - "This situation is impossible — equal VaR implies equal tail risk by definition"
    - "Portfolio A is riskier because its tail losses are closer to the VaR figure, indicating the model underestimates losses"
  answer: 1
  explanation: "This is VaR's fundamental limitation: it only specifies the 1st-percentile loss threshold, not what happens beyond it. Portfolios A and B are indistinguishable by VaR, but B is catastrophically riskier — its average loss in the worst 1% of days is nearly 10× larger. Expected Shortfall (ES/CVaR) would correctly separate them: approximately $1.1M vs $10M. VaR is blind to the shape of the tail beyond the threshold."

- question: "Two portfolios can have identical 99% VaR while one has dramatically larger expected losses in the worst 1% of scenarios."
  type: true-false
  answer: true
  explanation: "True. VaR is a single percentile — it identifies the threshold but says nothing about the distribution of losses beyond that threshold. A portfolio of vanilla bonds and a portfolio of short deep out-of-the-money options can have the same VaR threshold while the latter has catastrophically fat tails. This is precisely why Expected Shortfall (the average loss conditional on being in the worst 1%) was adopted in Basel III/IV: it penalizes fat tails that VaR ignores."

- question: "A 99% VaR of $2 million means that the portfolio cannot lose more than $2 million in a single day."
  type: true-false
  answer: false
  explanation: "False. A 99% VaR of $2 million means that in 99% of trading days, the loss will be $2 million or less — equivalently, in 1% of days, the loss will EXCEED $2 million. VaR explicitly does not cap losses. In the tail (the worst 1% of days), actual losses could be $2.1 million or $200 million; VaR provides zero information about that range. Treating VaR as a maximum loss is among the most dangerous misinterpretations in risk management."

- question: "Why do risk managers compute Expected Shortfall (ES) in addition to VaR, and what information does ES provide that VaR cannot?"
  type: short-answer
  answer: "VaR identifies the loss threshold at a given percentile but is completely silent about how large losses are beyond that threshold. Expected Shortfall is the average loss conditional on being in the worst 1% (or α%) of scenarios. ES answers the question VaR ignores: when things go very badly, how badly do they go on average? Two portfolios with identical VaR can have very different ES values, revealing very different tail risk profiles — a difference that matters enormously for capital adequacy and systemic risk."
  explanation: "During the 2008 financial crisis, many institutions met their VaR limits while sustaining tail losses orders of magnitude larger. A portfolio short of deep out-of-the-money options might show modest VaR because the 1% threshold stays low — but in the extreme scenarios beyond the threshold, losses are catastrophic. ES penalizes fat tails; VaR is indifferent to them. This is why Basel III/IV shifted from requiring VaR to requiring ES at the 97.5% level for regulatory capital calculations."
```

## Explainer

You already know how to work with quantiles and probability distributions, and you know that portfolio diversification reduces variance. **Value at Risk (VaR)** puts those tools together into a single risk number: given a portfolio's return distribution, what is the threshold loss that will be exceeded only α% of the time over the next T days? A "one-day 99% VaR of $1 million" means: over the next trading day, there is a 1% probability of losing more than $1 million. Equivalently, the 1st percentile of the one-day loss distribution is $1 million.

The most common calculation method is **parametric VaR**, which assumes portfolio returns are normally distributed. You need three inputs: the portfolio's expected return (often assumed to be zero for short horizons), its standard deviation σ, and the desired confidence level. For a 99% one-tailed VaR, the critical value from the standard normal distribution is z = 2.326. So parametric VaR = −(μ + z × σ) × Portfolio value, where μ is the expected return. For a $10 million portfolio with daily standard deviation of 1%, one-day 99% VaR = 2.326 × 0.01 × $10M = $232,600. The appeal is simplicity: if you can estimate covariance matrices, you can compute VaR for any portfolio.

**Historical simulation VaR** avoids the normality assumption entirely by using actual past returns. Take the last 500 (or 1,000) trading days of portfolio returns, sort them, and find the 1st percentile — that is your 99% VaR. No distributional assumption required. The drawback is that historical VaR is only as good as the historical record: if the tail events in the lookback window were mild, the estimated VaR will be too small. And it weights all historical days equally regardless of how relevant the market conditions were.

**Monte Carlo VaR** generates thousands of simulated portfolio return paths by drawing from assumed distributions for each risk factor (interest rates, equity returns, exchange rates), applying the portfolio's sensitivity to each factor, and building the full simulated loss distribution. The VaR is then the appropriate percentile of this simulated distribution. Monte Carlo handles complex, nonlinear portfolios (with options, structured products) that violate the linearity assumptions underlying parametric VaR, but requires careful specification of correlation structures and tail behavior.

The fundamental limitation of VaR — regardless of method — is that it tells you nothing about what happens beyond the threshold. A 99% VaR of $1 million means that in the worst 1% of days, you lose *more* than $1 million, but it could be $1.1 million or $100 million. Two portfolios can have identical VaR while one has manageable tail losses and the other is catastrophically exposed. This is why risk managers also compute **Expected Shortfall (ES)**, also called Conditional VaR or CVaR: the expected loss given that you are in the worst 1% of outcomes. ES penalizes fat tails properly, and the Basel III/IV regulatory framework shifted from requiring VaR to requiring ES at the 97.5% level precisely for this reason. Despite its limitations, VaR remains the dominant risk reporting metric because its single-number simplicity makes it easy to communicate, aggregate across desks, and set limits.


