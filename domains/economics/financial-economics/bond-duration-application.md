---
id: bond-duration-application
title: Duration and Interest Rate Sensitivity Applications
domain: economics
course: financial-economics
prerequisites:
- id: duration-and-convexity
  type: hard
- id: interest-rate-risk-management
  type: soft
- id: calculus
  type: hard
- id: derivatives-of-logarithmic-functions
  type: soft
builds-toward: []
tags:
- bonds
- duration
- risk-management
- interest-rate-sensitivity
stage: formal-systems
status: draft
---
# Duration and Interest Rate Sensitivity Applications

## Core Idea
Duration measures the average maturity-weighted time to receive a bond's cash flows and quantifies price sensitivity to yield changes. A bond's percentage price change approximately equals negative duration times the change in yield. This metric enables portfolio managers to construct immunization strategies and hedge interest rate risk.

## How It's Best Learned
Calculate duration for different bonds and compare their price changes when yields move by 1%. Verify the duration approximation against actual price changes to see when it breaks down.

## Common Misconceptions
- Confusing duration with maturity; duration is always less than maturity for coupon-paying bonds.
- Assuming duration is constant; it changes as yields and time to maturity change.

## Questions

```yaml
- question: "A 10-year zero-coupon bond and a 10-year 8%-coupon bond have the same maturity. Which has greater price sensitivity to a 1% rise in yields, and why?"
  type: multiple-choice
  options:
    - "The coupon bond — it pays more total cash, so yield changes affect it more"
    - "The zero-coupon bond — all its cash flow is at maturity, giving it the longest possible duration for a 10-year instrument"
    - "They are identical — same maturity means identical price sensitivity"
    - "The coupon bond — higher coupon payments amplify the effect of yield changes"
  answer: 1
  explanation: "Duration measures interest rate sensitivity, and duration ≤ maturity for coupon-paying bonds. A zero-coupon bond has duration equal to its maturity (10 years) because there is only one cash flow at the end — nothing to pull the weighted average earlier. A 10-year coupon bond has duration of perhaps 7–8 years because early coupon payments arrive sooner and reduce the time-weighted average. Since ΔP/P ≈ −D_mod × Δy, the zero-coupon bond drops more in price for the same yield increase. Option C is the most common misconception: equating maturity with duration."

- question: "A pension fund must pay $100 million in 15 years. To immunize this liability against interest rate risk, the fund manager should:"
  type: multiple-choice
  options:
    - "Buy bonds with maturities of exactly 15 years, since maturity matches the liability date"
    - "Hold only short-term bonds to minimize duration and thus minimize all interest rate risk"
    - "Construct a bond portfolio with duration equal to 15 years, so assets and liabilities respond equally to yield changes"
    - "Match the total face value of bonds to $100 million, since face value determines the final payment"
  answer: 2
  explanation: "Immunization requires matching the *duration* of assets to the *duration* of liabilities — not their maturities. When asset duration equals liability duration, a given change in yields affects both sides by approximately the same amount, preserving the funded ratio. A 15-year coupon bond has duration less than 15 years; the manager must blend instruments to reach exactly 15-year duration. Option B is wrong: short-duration assets expose the fund to reinvestment risk and will not grow to match the liability if rates fall."

- question: "A bond with a higher coupon rate (all else equal) will have a longer duration and therefore greater price sensitivity to interest rate changes."
  type: true-false
  answer: false
  explanation: "Higher coupon rates *reduce* duration, not increase it. Larger early coupon payments shift more of the bond's total cash flow toward the present, pulling the time-weighted average forward and shortening duration. A high-coupon bond is *less* sensitive to interest rate changes than a low-coupon bond of the same maturity. The zero-coupon bond has the longest duration of any bond with a given maturity — precisely because it has no early payments to reduce sensitivity."

- question: "Duration provides only an approximation of bond price changes because the actual price-yield relationship is convex, not linear."
  type: true-false
  answer: true
  explanation: "Duration captures the first-order (linear) sensitivity: ΔP/P ≈ −D_mod × Δy. But the true price-yield curve is convex — for a given yield change, a bond falls less than duration predicts when yields rise and gains more than duration predicts when yields fall. For small yield changes, the linear approximation is excellent. For larger changes or for precision hedging, the convexity correction (the second-order term) becomes necessary. Positive convexity is generally favorable — it represents an asymmetric advantage compared to a purely linear instrument."

- question: "Why does a duration mismatch between long-duration assets and short-duration liabilities (such as long-term mortgages funded by deposits) create a risk when interest rates rise rapidly?"
  type: short-answer
  answer: "When rates rise, the market value of long-duration assets falls sharply — approximately duration × rate change × asset value. Short-duration liabilities lose much less value because their cash flows are near-term and barely discounted by higher rates. The result is that the asset side shrinks relative to the liability side, eroding the institution's equity. If the duration gap is large enough and the rate rise severe enough, equity can fall to zero — insolvency."
  explanation: "This is the mechanism behind the 2023 US banking crisis. Banks like Silicon Valley Bank held portfolios of long-duration bonds (10–15 year duration) funded by demand deposits (near-zero duration). A 2–3 percentage point rate rise caused asset market values to fall 15–30%, while deposit values were unchanged. Duration gap risk transforms from academic theory to existential threat when combined with leverage and liquidity mismatch."
```

## Explainer

You've learned that duration is the weighted average time to receive a bond's cash flows, where weights are the present values of each payment as a fraction of the bond's total price. That abstract definition becomes powerful when you recognize what duration actually measures: **price sensitivity to yield changes**. A bond with duration 7 will lose approximately 7% of its value for every 1 percentage point rise in yields. This linear approximation, called the **modified duration** relationship, is the foundation of interest rate risk management.

To see why duration measures sensitivity, use your calculus background. The bond price is the sum of discounted cash flows: P = Σ CFₜ/(1+y)ᵗ. Taking the derivative dP/dy and dividing by -P gives you **modified duration** = Macaulay duration / (1+y). So the percentage price change is approximately: ΔP/P ≈ -D_mod × Δy. A 10-year zero-coupon bond has duration equal to its maturity (10 years) because there's only one cash flow at the end. A 10-year coupon bond has shorter duration — maybe 7-8 years — because early coupon payments pull the average earlier in time and reduce sensitivity to yield changes.

The most direct application is **portfolio immunization**: matching the duration of a portfolio of assets to the duration of a portfolio of liabilities so that interest rate changes affect both sides equally. A pension fund knows it must pay $50 million in 12 years. If it holds a bond portfolio with duration of 12, both sides respond almost identically to yield changes — the funded status is protected. This is why institutional investors track duration obsessively. A mismatch creates **duration gap** risk, which materialized dramatically during the 2023 banking crisis when banks held long-duration assets (mortgages, Treasuries) funded by short-duration liabilities (deposits), and rising rates crushed their balance sheets.

The limitation of the duration approximation becomes important at larger yield changes. Duration assumes a linear price-yield relationship, but the actual relationship is convex — bonds fall less than duration predicts when yields rise and gain more than duration predicts when yields fall. This asymmetry (positive **convexity**) is generally favorable, but the approximation error grows with both the yield change and the duration of the bond. For hedging large movements or for precision pricing, the convexity correction (the next topic you'll study) becomes necessary. Duration gives you the first-order sensitivity; convexity gives you the second-order correction.
