---
id: interest-rate-risk-management
title: Interest Rate Risk Management
domain: economics
course: financial-economics
prerequisites:
- id: bond-immunization-strategies
  type: hard
- id: duration-and-convexity
  type: hard
tags:
- interest-rate
- risk
- bonds
stage: formal-systems
status: validated
---

# Interest Rate Risk Management

## Core Idea
Interest rate risk arises from changes in market rates affecting bond values and cash flows. Managing this risk involves duration matching, immunization, and using interest rate derivatives. Parallel shifts, slope changes (butterfly trades), and curve convexity create different sources of risk requiring different hedging strategies.

## Questions

```yaml
- question: "A pension fund has matched the duration of its bond portfolio exactly to its liability duration. The yield curve then steepens dramatically — long-term rates rise by 100 basis points while short-term rates remain unchanged. Is the fund fully immunized against this move?"
  type: multiple-choice
  options:
    - "Yes — duration matching fully protects against all interest rate movements"
    - "No — duration matching only immunizes against parallel shifts; a curve steepening changes the relative value of short and long bonds in ways that aggregate duration cannot capture"
    - "Yes — the portfolio's convexity automatically compensates for non-parallel shifts"
    - "No — duration matching only works for fixed-rate bonds with a single maturity"
  answer: 1
  explanation: "Duration-based immunization is designed specifically for parallel shifts — where all yields move by the same amount at every maturity. A steepening (long rates rising more than short rates) creates different price impacts at different maturities. A portfolio with the right aggregate duration but the wrong maturity distribution (e.g., a barbell of short and long bonds) will behave very differently from one with bonds concentrated at the liability horizon. Managing this requires key rate durations — sensitivity to changes at specific maturities — rather than a single number."

- question: "A bond portfolio has high convexity relative to its liabilities. Interest rates then make a large, unexpected move — either sharply up or sharply down. Relative to a lower-convexity portfolio of equal duration, how does the high-convexity portfolio perform?"
  type: multiple-choice
  options:
    - "It performs worse — high convexity means greater sensitivity to large rate moves"
    - "It performs the same — convexity only matters for very small rate moves, not large ones"
    - "It outperforms — it gains more when rates fall and loses less when rates rise, due to the asymmetric price-yield relationship"
    - "It underperforms only if rates rise, not if they fall"
  answer: 2
  explanation: "Convexity captures the curvature of the price-yield relationship. Because of convexity, when rates fall, the bond price rises by more than duration alone predicts; when rates rise, the price falls by less. This asymmetry favors the bondholder under large moves in either direction. Portfolios with higher convexity outperform lower-convexity portfolios of the same duration whenever rates move significantly, which is why convexity has a cost — it is priced in through lower yields."

- question: "A bond portfolio that has been immunized against parallel yield curve shifts is also protected against changes in the slope or curvature of the yield curve."
  type: true-false
  answer: false
  explanation: "Duration-based immunization targets one specific scenario: all yields moving up or down by the same amount (a parallel shift). It says nothing about the portfolio's behavior when the curve steepens, flattens, or twists. A barbell portfolio and a bullet portfolio can have identical durations but respond very differently to non-parallel shifts. Managing slope and curvature risk requires thinking about key rate durations at multiple points on the curve, not just aggregate duration."

- question: "Higher convexity is a desirable property for bondholders, which is why bonds with higher convexity typically offer lower yields than otherwise-equivalent lower-convexity bonds."
  type: true-false
  answer: true
  explanation: "Convexity benefits the bondholder: when rates fall, the price rises by more than duration predicts; when rates rise, the price falls by less. This favorable asymmetry has value, especially in volatile rate environments. Because the market prices this benefit, higher-convexity bonds trade at higher prices — equivalently, lower yields — than lower-convexity bonds with the same duration. Callable bonds reduce convexity (the call option caps price appreciation when rates fall), which is why they yield more than equivalent non-callable bonds."

- question: "A corporate treasurer has issued fixed-rate debt but now expects interest rates to fall. Without selling the bonds, how might interest rate derivatives help manage this exposure, and what would be the goal of the hedge?"
  type: short-answer
  answer: "The treasurer's fixed-rate debt is costing them more than necessary if rates fall — they cannot benefit from lower rates. They could enter a receive-fixed, pay-floating interest rate swap: the treasurer receives fixed payments (which offset their fixed debt coupon) and pays floating (which will be lower if rates fall as expected). The net effect is that the economics of the debt become variable-rate — the treasurer benefits if rates fall — without altering the underlying bond obligations or balance sheet. The goal is to change the effective duration and rate sensitivity of the position without liquidating the underlying instrument."
  explanation: "This is the core logic of interest rate swap usage: swaps separate the rate exposure from the underlying instrument. A corporation locked into high fixed rates can synthetically convert to floating. A bank with variable-rate assets can synthetically convert to fixed. The key management principle is identifying which rate scenario creates the most risk, then using derivatives that hedge precisely that scenario without introducing other exposures."
```

## Explainer

From duration and convexity you know how to measure a bond's price sensitivity to rate changes: duration gives a first-order approximation, and convexity corrects for the curvature that duration misses. From immunization you know how to construct a portfolio whose value is shielded from small parallel shifts in rates by matching duration to a target horizon. Interest rate risk management extends these tools into active practice: how do institutions actually protect themselves when rates can move in complex, unpredictable ways?

The simplest case — a **parallel shift** of the yield curve — is what duration-based immunization is designed to handle. If all yields rise by the same amount across every maturity, a portfolio whose dollar duration matches its liability duration will experience roughly offsetting price changes. But real yield curve moves are rarely perfectly parallel. The curve can **steepen** (long rates rise more than short rates), **flatten** (short rates rise more), or **twist** in more complex ways. A portfolio immunized against parallel shifts can still lose value if the slope or curvature of the curve changes unexpectedly. Managing these exposures requires thinking about multiple **key rate durations** — the sensitivity to rate changes at specific maturities — rather than a single aggregate duration.

**Convexity** is the interest rate risk manager's friend under large moves. Because of convexity, a bond gains more price when rates fall by a given amount than it loses when rates rise by the same amount. Portfolios with higher convexity outperform lower-convexity portfolios of the same duration if rates move significantly in either direction. Managers who expect high rate volatility therefore seek **convexity-rich** portfolios (bonds with embedded options like callables reduce convexity; zero-coupon bonds and bullet maturities maximize it). This is why convexity has a cost — it is priced in through lower yields.

When immunization through portfolio construction is insufficient, **interest rate derivatives** extend the toolkit. Interest rate **swaps** convert fixed-rate cash flows to floating or vice versa, effectively changing the duration of a position without selling the underlying bonds. **Interest rate futures** and **options** (caps, floors, swaptions) allow targeted hedges against specific yield curve scenarios. A corporate treasurer who issued fixed-rate debt but expects rates to fall might enter a receive-fixed swap, transforming the effective economics without altering the balance sheet. The key principle across all these strategies is the same: identify which dimension of rate movement creates the most risk for your specific portfolio or liability structure, then use instruments that hedge precisely that dimension without introducing unwanted exposures elsewhere.
