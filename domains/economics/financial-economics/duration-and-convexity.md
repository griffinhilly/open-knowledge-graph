---
id: duration-and-convexity
title: Duration and Convexity
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: yield-to-maturity
  type: hard
- id: derivatives-of-exponential-functions
  type: soft
- id: higher-order-derivatives
  type: soft
builds-toward:
- term-structure-of-interest-rates
tags:
- duration
- convexity
- interest-rate-risk
- fixed-income
- sensitivity
stage: formal-systems
status: validated
---

# Duration and Convexity

## Core Idea
Duration measures a bond's price sensitivity to interest rate changes — specifically, modified duration approximates the percentage change in price for a 1-percentage-point change in yield. Macaulay duration is the weighted average time to receive all cash flows, where weights are each payment's share of total present value. Convexity captures the curvature of the price-yield relationship: duration provides a linear approximation, while convexity corrects for the fact that the true relationship curves favorably — bonds gain more from rate decreases than they lose from equal rate increases. Higher convexity is always preferable, all else equal.

## How It's Best Learned
Calculate Macaulay duration as a weighted average of cash flow timings and compare it to simple maturity. Use modified duration to predict price changes for a 1% yield shift, then compare to the actual change to see where convexity matters. Observe that zero-coupon bonds have duration equal to maturity, the maximum possible.

## Common Misconceptions
- Duration is not simply maturity — for coupon bonds, duration is always less than maturity because interim coupons arrive early.
- For large yield changes, ignoring convexity causes significant error; duration alone systematically underestimates gains and overestimates losses.
