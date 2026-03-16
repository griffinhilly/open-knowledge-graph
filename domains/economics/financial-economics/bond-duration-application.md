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
builds-toward:
- bond-convexity-price-effects
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

## Explainer

You've learned that duration is the weighted average time to receive a bond's cash flows, where weights are the present values of each payment as a fraction of the bond's total price. That abstract definition becomes powerful when you recognize what duration actually measures: **price sensitivity to yield changes**. A bond with duration 7 will lose approximately 7% of its value for every 1 percentage point rise in yields. This linear approximation, called the **modified duration** relationship, is the foundation of interest rate risk management.

To see why duration measures sensitivity, use your calculus background. The bond price is the sum of discounted cash flows: P = Σ CFₜ/(1+y)ᵗ. Taking the derivative dP/dy and dividing by -P gives you **modified duration** = Macaulay duration / (1+y). So the percentage price change is approximately: ΔP/P ≈ -D_mod × Δy. A 10-year zero-coupon bond has duration equal to its maturity (10 years) because there's only one cash flow at the end. A 10-year coupon bond has shorter duration — maybe 7-8 years — because early coupon payments pull the average earlier in time and reduce sensitivity to yield changes.

The most direct application is **portfolio immunization**: matching the duration of a portfolio of assets to the duration of a portfolio of liabilities so that interest rate changes affect both sides equally. A pension fund knows it must pay $50 million in 12 years. If it holds a bond portfolio with duration of 12, both sides respond almost identically to yield changes — the funded status is protected. This is why institutional investors track duration obsessively. A mismatch creates **duration gap** risk, which materialized dramatically during the 2023 banking crisis when banks held long-duration assets (mortgages, Treasuries) funded by short-duration liabilities (deposits), and rising rates crushed their balance sheets.

The limitation of the duration approximation becomes important at larger yield changes. Duration assumes a linear price-yield relationship, but the actual relationship is convex — bonds fall less than duration predicts when yields rise and gain more than duration predicts when yields fall. This asymmetry (positive **convexity**) is generally favorable, but the approximation error grows with both the yield change and the duration of the bond. For hedging large movements or for precision pricing, the convexity correction (the next topic you'll study) becomes necessary. Duration gives you the first-order sensitivity; convexity gives you the second-order correction.
