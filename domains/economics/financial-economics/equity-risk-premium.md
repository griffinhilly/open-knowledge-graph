---
id: equity-risk-premium
title: Equity Risk Premium and Market Return Expectations
domain: economics
course: financial-economics
prerequisites:
- id: risk-and-return-tradeoff
  type: hard
- id: expected-return-and-variance-of-assets
  type: hard
builds-toward:
- cost-of-equity-capm
tags:
- capm
- expected-return
- risk-premium
stage: formal-systems
status: validated
---

# Equity Risk Premium and Market Return Expectations

## Core Idea
The equity risk premium is the expected return on stocks minus the risk-free rate. Historical estimates ≈ 5–7%; forward-looking estimates use dividend growth projections or earnings yields. This premium drives the slope of the security market line.

## How It's Best Learned
Compare historical equity risk premium (annualized stock returns minus Treasury returns) across decades. Estimate forward premium using dividend growth model or compare to current equity yields.

## Questions

```yaml
- question: "An analyst uses the CAPM to value a stock with β = 2.0. The current risk-free rate is 3% and the equity risk premium is estimated at 5%. What expected return should she use?"
  type: multiple-choice
  options:
    - "8% — the risk-free rate plus the ERP, unadjusted for beta"
    - "10% — she should halve the ERP since beta exceeds 1.0"
    - "13% — the risk-free rate plus beta times the ERP"
    - "5% — only the ERP matters for equities, not the risk-free rate"
  answer: 2
  explanation: "The CAPM formula is E[R] = r_f + β × ERP = 3% + 2.0 × 5% = 13%. The ERP is the return premium for one unit of market risk (β = 1). A stock with β = 2.0 has twice the systematic risk of the market, so it earns twice the risk premium above the risk-free rate. Option A (8%) ignores beta entirely; this would only be correct for a stock with β = 1. The ERP is the slope of the security market line — multiply it by beta to get each stock's specific risk premium."

- question: "When current price-to-earnings (P/E) ratios in the stock market are extremely high, what does the forward-looking equity risk premium estimate typically show?"
  type: multiple-choice
  options:
    - "A higher-than-average ERP, because high prices signal high future returns"
    - "A lower-than-average ERP, because the market has priced in optimistic expectations leaving little additional return"
    - "An unchanged ERP, because the ERP is a long-run constant independent of current valuations"
    - "A higher-than-average ERP, because high P/E ratios indicate elevated market risk"
  answer: 1
  explanation: "The forward-looking ERP uses E[R] = D₁/P₀ + g (Gordon Growth Model), then subtracts the risk-free rate. When prices (P₀) are high relative to earnings/dividends, the implied expected return falls, and so does the ERP. High valuations mean investors are paying a lot for each dollar of earnings — implying they accept a lower return going forward. This is the opposite of what option A claims: high past prices reflect past returns, not high future returns. The late 1990s dotcom bubble and 2020s valuations both showed compressed forward-looking ERPs."

- question: "The equity risk premium is directly observable in real-time market data."
  type: true-false
  answer: false
  explanation: "False. The ERP is expected future returns minus the risk-free rate — and expected future returns are unobservable. We can only estimate the ERP, using either historical realized returns (backward-looking) or current prices and earnings/dividend forecasts (forward-looking). Both approaches have significant limitations: historical estimates reflect luck and survivorship bias; forward-looking estimates depend on growth assumptions. This is why estimates of the ERP range from about 3% to 8% depending on method and time period, and why it remains a central source of uncertainty in valuation."

- question: "In the CAPM framework, the equity risk premium equals the expected return of the market portfolio minus the risk-free rate."
  type: true-false
  answer: true
  explanation: "True. In CAPM, the security market line is E[R_i] = r_f + β_i × (E[R_m] − r_f), where (E[R_m] − r_f) is the equity risk premium. The market portfolio by definition has β = 1, so its expected return is E[R_m] = r_f + 1 × ERP. The ERP is precisely the excess expected return of the market over the risk-free rate — the slope of the SML. Every other asset's expected return is scaled from this baseline by its beta."

- question: "What is the equity premium puzzle, and why does it challenge standard consumption-based asset pricing models?"
  type: short-answer
  answer: "The equity premium puzzle (Mehra and Prescott, 1985) is the observation that historical U.S. stock returns have exceeded risk-free returns by about 5–7% annually, while standard consumption-based models predict a premium of only 1–2%. In these models, investors care about consumption smoothing; to justify a 6% premium, investors would need implausibly high risk aversion coefficients. The puzzle matters because standard models cannot explain why equities demand so much compensation for their risk, suggesting that either the models are wrong (omitting habit formation, rare disaster risk, or market frictions) or that historical returns are not a reliable guide to future expectations."
  explanation: "The puzzle is not merely academic: whatever drives the ERP also determines the discount rate used to value every company and investment. If the ERP is explained by rare disaster risk, then the premium could vanish in a world with fewer catastrophic risks. If it reflects investor irrationality or limited participation, the implications for capital allocation differ entirely. The equity premium puzzle is one reason financial economists cannot simply look up the ERP — the right number depends on which theory of risk and compensation you believe."
```

## Explainer

From your study of the risk-return tradeoff and expected returns, you know that investors require compensation for bearing risk. The **equity risk premium** (ERP) is the most important instance of this principle in asset pricing: it is the extra return investors demand for holding stocks instead of risk-free assets like Treasury bills. If you can earn 4% on a T-bill with no risk, rational investors will only hold equities if they expect to earn more — the premium is the "price of equity risk." Historically, this premium has been around 5–7% annually in the United States, making stocks the dominant asset class for long-run wealth accumulation.

The ERP is not directly observable — it must be estimated. The two main approaches differ in whether they look backward or forward. The **historical approach** takes realized stock returns (dividends plus capital gains) minus realized risk-free rates over a long period. The appeal is simplicity; the problem is that historical returns reflect random luck, changing economic conditions, and survivorship bias (we study the U.S. stock market partly because it survived and thrived). The **forward-looking approach** instead uses current market prices and earnings or dividend projections to infer what return investors appear to require. The Gordon Growth Model offers one such estimate: if stocks are priced fairly, E[R] = D₁/P₀ + g, where D₁/P₀ is the forward dividend yield and g is the expected long-run growth rate. Subtracting the risk-free rate gives an implied ERP. When P/E ratios are high (as they were in the late 1990s or 2020s), this forward-looking estimate often falls below historical averages, signaling that markets have priced in optimistic expectations.

The ERP is not just an empirical curiosity — it is structurally embedded in the Capital Asset Pricing Model (CAPM). In the security market line, the expected return of any asset is r_f + β × ERP. The ERP is the **slope of the security market line**: it sets the compensation per unit of systematic risk. A larger ERP means investors are collectively more fearful or more risk-averse; each unit of beta earns more. This makes the ERP a gauge of aggregate risk appetite in markets. During crises (2008, 2020), implied ERPs spike as prices fall and investors flee to safety; during bull markets, they compress as investors accept less compensation for risk.

The "equity premium puzzle," identified by Mehra and Prescott in 1985, remains one of the most intriguing puzzles in financial economics. Standard consumption-based asset pricing models imply that rational investors, smoothing consumption over time, should require only a small premium — around 1–2% — to hold equities. Yet observed premiums are 5–7%. Resolving this gap requires either much higher risk aversion than the standard model assumes, habit formation (investors are especially averse to losses near their prior consumption level), rare disaster risk (the small probability of catastrophic events demands large compensation), or market frictions and heterogeneous investors. The puzzle matters because whichever explanation is correct changes how we think about discount rates, capital allocation, and the cost of equity for firms.
