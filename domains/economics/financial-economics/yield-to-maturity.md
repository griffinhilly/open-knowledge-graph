---
id: yield-to-maturity
title: Yield to Maturity
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
builds-toward:
- term-structure-of-interest-rates
- risk-and-return-tradeoff
- duration-and-convexity
tags:
- ytm
- yield
- internal-rate-of-return
- fixed-income
stage: formal-systems
status: validated
---

# Yield to Maturity

## Core Idea
Yield to maturity (YTM) is the single discount rate that equates a bond's current price to the present value of all its future cash flows — the bond's internal rate of return. It represents the annualized return an investor earns if they hold the bond to maturity and all coupons are reinvested at the same rate. Because YTM is embedded in the bond pricing equation, it must generally be solved numerically. YTM is the standard metric for comparing bonds with different coupon rates and maturities on equal footing.

## How It's Best Learned
Use trial and error or a financial calculator to find YTM for a given price, then verify by plugging back into the bond pricing formula. Understand that YTM assumes reinvestment at the YTM rate — an assumption that rarely holds exactly in practice.

## Common Misconceptions
- YTM equals the coupon rate only when the bond trades at par; for a discounted bond, YTM exceeds the coupon rate.
- YTM is not a guaranteed return — it depends on the reinvestment rate assumption and on holding to maturity without default.
