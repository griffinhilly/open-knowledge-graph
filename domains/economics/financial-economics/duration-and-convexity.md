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

## Explainer

You already know that a bond's price is the present value of its cash flows discounted at the yield to maturity, and that price and yield move in opposite directions. But knowing the direction of that relationship is not enough for risk management — you need to quantify it. **Duration** is the tool that answers the question: if yields rise by one percentage point, how much does this bond's price fall?

**Macaulay duration** starts from the bond pricing formula and asks: what is the average time (in years) until the investor receives the bond's cash flows, weighted by the present value of each payment? A zero-coupon bond paying $1,000 in ten years has a Macaulay duration of exactly ten years — there is only one cash flow, so the wait is ten years with full weight. A coupon bond paying semi-annual coupons and returning principal in ten years has a shorter duration, because some of the present value arrives early as coupons. The coupon rate and yield together determine how much weight those early payments receive. The formula is: D_mac = Σ [t × PV(CFₜ)] / Price, where t is the time to each cash flow.

**Modified duration** converts Macaulay duration into a price sensitivity measure: D_mod = D_mac / (1 + y/m), where y is the yield and m is the number of compounding periods per year. The interpretation is direct: a bond with modified duration of 7 will lose approximately 7% of its price for a 1-percentage-point rise in yield, and gain approximately 7% for a 1-percentage-point fall. This linear approximation is the first-order term in a Taylor expansion of the price-yield function around the current yield.

**Convexity** captures the second-order term — the curvature of the price-yield relationship. The true relationship between price and yield is not a straight line but a curve that bows toward the investor (convex from below). This means two things. First, for a given change in yield, the actual price change is larger than duration predicts when yields fall, and smaller than duration predicts when yields rise. In other words, a bond with high convexity gains more from falling rates than it loses from rising rates by the same amount. Second, for large yield moves, ignoring convexity causes substantial estimation error — the linear approximation is accurate only for small changes. The full approximation is: ΔP/P ≈ −D_mod × Δy + (1/2) × Convexity × (Δy)².

In portfolio management, duration and convexity together drive interest rate risk strategy. A bond portfolio manager seeking to hedge a liability stream will **duration-match** the portfolio to the liabilities, ensuring that a parallel shift in the yield curve affects both sides equally. But a better-hedged portfolio also convexity-matches, which protects against large yield moves and non-parallel shifts. **Convexity is always a desirable property** — higher convexity means better price performance in both rising and falling rate environments — so investors pay for it (higher-convexity bonds trade at higher prices, lower yields). Callable bonds, which the issuer can retire early when rates fall, exhibit **negative convexity** in some yield ranges, because the call caps the price appreciation investors receive when rates decline.


