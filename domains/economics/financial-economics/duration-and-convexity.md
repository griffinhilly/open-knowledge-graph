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

## Questions

```yaml
- question: "Two bonds have the same modified duration of 8 years, but Bond A has much higher convexity than Bond B. Interest rates fall by 3 percentage points. Which statement correctly describes the outcome?"
  type: multiple-choice
  options:
    - "Both bonds gain the same amount — duration determines price sensitivity and they have equal duration"
    - "Bond A gains more than Bond B — higher convexity means larger price increases for the same rate decline"
    - "Bond B gains more — higher convexity bonds trade at a premium and thus have lower starting prices to rise from"
    - "The outcome depends on the bonds' maturities, not their convexity"
  answer: 1
  explanation: "Duration gives only the first-order (linear) approximation of price change. For a large yield move like 3 percentage points, the second-order convexity term matters significantly. Higher convexity means the price-yield curve bows more favorably toward the investor: the actual price gain from falling rates exceeds the duration prediction, and by more for higher-convexity bonds. Bond A, with higher convexity, will gain more than Bond B from the same rate decline, even though both have the same duration. This asymmetric benefit — gaining more from rate decreases than losing from equivalent increases — is exactly why investors pay a premium for convexity."

- question: "A 10-year bond pays semi-annual coupons. What is its Macaulay duration relative to its 10-year maturity?"
  type: multiple-choice
  options:
    - "Exactly 10 years — maturity and duration are the same for all bonds"
    - "Greater than 10 years — coupons extend the effective life of the investment beyond maturity"
    - "Less than 10 years — early coupon payments reduce the weighted-average time to receive cash flows"
    - "It cannot be determined without knowing the specific coupon rate"
  answer: 2
  explanation: "Macaulay duration is the present-value-weighted average time to receive all cash flows. A coupon bond pays cash flows before maturity (the semi-annual coupons), and those early payments receive positive weight in the average. Since some present value arrives earlier than maturity, the weighted average time must be *less than* maturity. Only a zero-coupon bond, where all cash flow arrives exactly at maturity, has duration equal to maturity. The higher the coupon rate (and the lower the yield), the more weight the early coupons receive and the further duration falls below maturity. Duration ≠ maturity is one of the most important corrections in fixed income."

- question: "A bond with higher convexity will gain more in price from a rate decrease than it will lose from an equal rate increase."
  type: true-false
  answer: true
  explanation: "This asymmetry is the defining property of convexity and the reason it is universally valued. The price-yield relationship curves toward the investor (convex from below): as yields fall, price rises faster than the duration prediction; as yields rise, price falls more slowly than the duration prediction. For equal up and down yield moves, the gain is larger than the loss. This means convexity provides a 'free lunch' in terms of asymmetric price performance — higher convexity is always preferable, all else equal, and investors bid up prices of high-convexity bonds accordingly."

- question: "A bond's modified duration equals its time to maturity."
  type: true-false
  answer: false
  explanation: "Modified duration equals maturity only for zero-coupon bonds, which pay no interim cash flows — all value arrives at maturity, so the weighted average time to receive cash flows is exactly the maturity date. For coupon-paying bonds, Macaulay duration is always less than maturity because early coupon payments pull the weighted average forward in time. Modified duration (= Macaulay duration divided by (1 + y/m)) is then also less than maturity. This is a persistent misconception: students often use maturity as a proxy for interest rate sensitivity, which overestimates the risk of coupon bonds."

- question: "Why is convexity described as a 'favorable' property, and what does it imply about the symmetry of price changes around a yield shift?"
  type: short-answer
  answer: "Convexity is favorable because it creates an asymmetry that benefits the investor: for a given change in yield, the price gain from a rate decrease exceeds the price loss from an equal rate increase. This happens because the true price-yield relationship is a curve that bows toward the investor, not a straight line. Duration (the linear approximation) predicts symmetrical gains and losses for equal rate moves; convexity corrects this by accounting for the curve's favorable bend. A bond with high convexity 'runs away' from you when rates rise (loses less than predicted) and 'races toward' you when rates fall (gains more than predicted). Investors pay for this asymmetric benefit by accepting lower yields on high-convexity bonds."
  explanation: "The full Taylor expansion approximation is ΔP/P ≈ −D_mod × Δy + (1/2) × Convexity × (Δy)². The convexity term always adds a positive contribution regardless of the sign of Δy, because (Δy)² is always positive. This is why convexity always helps: it increases price gains when rates fall and reduces price losses when rates rise. For small yield moves, this effect is negligible; for large moves (like 3%), it is the dominant source of estimation error if ignored."
```

## Explainer

You already know that a bond's price is the present value of its cash flows discounted at the yield to maturity, and that price and yield move in opposite directions. But knowing the direction of that relationship is not enough for risk management — you need to quantify it. **Duration** is the tool that answers the question: if yields rise by one percentage point, how much does this bond's price fall?

**Macaulay duration** starts from the bond pricing formula and asks: what is the average time (in years) until the investor receives the bond's cash flows, weighted by the present value of each payment? A zero-coupon bond paying $1,000 in ten years has a Macaulay duration of exactly ten years — there is only one cash flow, so the wait is ten years with full weight. A coupon bond paying semi-annual coupons and returning principal in ten years has a shorter duration, because some of the present value arrives early as coupons. The coupon rate and yield together determine how much weight those early payments receive. The formula is: D_mac = Σ [t × PV(CFₜ)] / Price, where t is the time to each cash flow.

**Modified duration** converts Macaulay duration into a price sensitivity measure: D_mod = D_mac / (1 + y/m), where y is the yield and m is the number of compounding periods per year. The interpretation is direct: a bond with modified duration of 7 will lose approximately 7% of its price for a 1-percentage-point rise in yield, and gain approximately 7% for a 1-percentage-point fall. This linear approximation is the first-order term in a Taylor expansion of the price-yield function around the current yield.

**Convexity** captures the second-order term — the curvature of the price-yield relationship. The true relationship between price and yield is not a straight line but a curve that bows toward the investor (convex from below). This means two things. First, for a given change in yield, the actual price change is larger than duration predicts when yields fall, and smaller than duration predicts when yields rise. In other words, a bond with high convexity gains more from falling rates than it loses from rising rates by the same amount. Second, for large yield moves, ignoring convexity causes substantial estimation error — the linear approximation is accurate only for small changes. The full approximation is: ΔP/P ≈ −D_mod × Δy + (1/2) × Convexity × (Δy)².

In portfolio management, duration and convexity together drive interest rate risk strategy. A bond portfolio manager seeking to hedge a liability stream will **duration-match** the portfolio to the liabilities, ensuring that a parallel shift in the yield curve affects both sides equally. But a better-hedged portfolio also convexity-matches, which protects against large yield moves and non-parallel shifts. **Convexity is always a desirable property** — higher convexity means better price performance in both rising and falling rate environments — so investors pay for it (higher-convexity bonds trade at higher prices, lower yields). Callable bonds, which the issuer can retire early when rates fall, exhibit **negative convexity** in some yield ranges, because the call caps the price appreciation investors receive when rates decline.


