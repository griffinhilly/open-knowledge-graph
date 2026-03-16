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
status: draft
---

# Equity Risk Premium and Market Return Expectations

## Core Idea
The equity risk premium is the expected return on stocks minus the risk-free rate. Historical estimates ≈ 5–7%; forward-looking estimates use dividend growth projections or earnings yields. This premium drives the slope of the security market line.

## How It's Best Learned
Compare historical equity risk premium (annualized stock returns minus Treasury returns) across decades. Estimate forward premium using dividend growth model or compare to current equity yields.

## Explainer

From your study of the risk-return tradeoff and expected returns, you know that investors require compensation for bearing risk. The **equity risk premium** (ERP) is the most important instance of this principle in asset pricing: it is the extra return investors demand for holding stocks instead of risk-free assets like Treasury bills. If you can earn 4% on a T-bill with no risk, rational investors will only hold equities if they expect to earn more — the premium is the "price of equity risk." Historically, this premium has been around 5–7% annually in the United States, making stocks the dominant asset class for long-run wealth accumulation.

The ERP is not directly observable — it must be estimated. The two main approaches differ in whether they look backward or forward. The **historical approach** takes realized stock returns (dividends plus capital gains) minus realized risk-free rates over a long period. The appeal is simplicity; the problem is that historical returns reflect random luck, changing economic conditions, and survivorship bias (we study the U.S. stock market partly because it survived and thrived). The **forward-looking approach** instead uses current market prices and earnings or dividend projections to infer what return investors appear to require. The Gordon Growth Model offers one such estimate: if stocks are priced fairly, E[R] = D₁/P₀ + g, where D₁/P₀ is the forward dividend yield and g is the expected long-run growth rate. Subtracting the risk-free rate gives an implied ERP. When P/E ratios are high (as they were in the late 1990s or 2020s), this forward-looking estimate often falls below historical averages, signaling that markets have priced in optimistic expectations.

The ERP is not just an empirical curiosity — it is structurally embedded in the Capital Asset Pricing Model (CAPM). In the security market line, the expected return of any asset is r_f + β × ERP. The ERP is the **slope of the security market line**: it sets the compensation per unit of systematic risk. A larger ERP means investors are collectively more fearful or more risk-averse; each unit of beta earns more. This makes the ERP a gauge of aggregate risk appetite in markets. During crises (2008, 2020), implied ERPs spike as prices fall and investors flee to safety; during bull markets, they compress as investors accept less compensation for risk.

The "equity premium puzzle," identified by Mehra and Prescott in 1985, remains one of the most intriguing puzzles in financial economics. Standard consumption-based asset pricing models imply that rational investors, smoothing consumption over time, should require only a small premium — around 1–2% — to hold equities. Yet observed premiums are 5–7%. Resolving this gap requires either much higher risk aversion than the standard model assumes, habit formation (investors are especially averse to losses near their prior consumption level), rare disaster risk (the small probability of catastrophic events demands large compensation), or market frictions and heterogeneous investors. The puzzle matters because whichever explanation is correct changes how we think about discount rates, capital allocation, and the cost of equity for firms.
