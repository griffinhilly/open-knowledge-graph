---
id: bond-immunization-liability-matching
title: Bond Immunization and Liability Matching
domain: economics
course: financial-economics
prerequisites:
- id: interest-rate-risk-duration
  type: hard
- id: net-present-value
  type: hard
tags:
- fixed-income
- portfolio-management
- liability-matching
stage: formal-systems
status: draft
---

# Bond Immunization and Liability Matching

## Core Idea
Immunization constructs a bond portfolio whose duration matches the time horizon of liabilities, eliminating interest rate risk for that specific horizon. Even if rates change, the portfolio value at the liability date remains predictable.

## How It's Best Learned
Work through a liability-matching problem: given a specific payment due in 5 years, construct a bond portfolio that immunizes against rate risk using duration matching.

## Explainer

A pension fund knows it must pay $10 million to retirees in exactly 8 years. The fund holds a bond portfolio today worth roughly that amount in present value. The problem: interest rates might change between now and the payment date. If rates rise, the portfolio's value falls. If rates fall, reinvested coupon income earns less. **Immunization** is the strategy that makes the fund indifferent to these rate moves — the two effects (price change and reinvestment rate change) are engineered to cancel each other at the target horizon.

The mechanism works through **duration**, which you already understand as the interest-rate sensitivity measure. Recall that duration measures both price sensitivity and the weighted-average time at which you receive cash flows. If you match the duration of your bond portfolio to the time horizon of your liability, a fascinating offsetting dynamic kicks in: when rates rise, your bonds fall in value (price effect is bad) but you reinvest coupons at higher rates (reinvestment effect is good). When rates fall, your bonds rise in value (price effect is good) but you reinvest coupons at lower rates (reinvestment effect is bad). At the duration-matched horizon, these effects precisely offset, leaving the portfolio value at the liability date unchanged regardless of which direction rates moved.

The mechanics require setting the **modified duration** of your portfolio equal to your target horizon. If you need to fund a liability in 8 years, you build a bond portfolio with a duration of 8 years. Since individual bonds have durations limited by their maturity and coupon structure, this typically means combining shorter-duration and longer-duration bonds to hit the target. A portfolio mixing a 4-year bond and a 12-year bond in the right proportions can achieve a duration of 8. The portfolio weights are solved using the duration-weighted-average formula: D_portfolio = w₁D₁ + w₂D₂, where w₁ + w₂ = 1. The **net present value** framework is embedded here — the value of your asset portfolio must equal the present value of liabilities not just today but durably across rate scenarios.

A critical practical caveat: immunization is not a one-time setup. As time passes, rates change, bonds age, and the portfolio's duration drifts away from the target horizon. Maintaining immunization requires **rebalancing** — periodically readjusting the portfolio to restore the duration match. The frequency of rebalancing trades off transaction costs against immunization precision. More sophisticated approaches — **cash flow matching** (literally purchasing bonds whose cash flows occur exactly at each liability payment date) or **convexity matching** (adding a second condition to account for curvature in the price-yield relationship) — can provide tighter protection at the cost of reduced flexibility and higher initial investment. Immunization is not a perfect hedge, but for institutions with predictable fixed liabilities, it remains a foundational fixed-income management technique.
