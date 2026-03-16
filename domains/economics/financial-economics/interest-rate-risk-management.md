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
status: draft
---

# Interest Rate Risk Management

## Core Idea
Interest rate risk arises from changes in market rates affecting bond values and cash flows. Managing this risk involves duration matching, immunization, and using interest rate derivatives. Parallel shifts, slope changes (butterfly trades), and curve convexity create different sources of risk requiring different hedging strategies.

## Explainer

From duration and convexity you know how to measure a bond's price sensitivity to rate changes: duration gives a first-order approximation, and convexity corrects for the curvature that duration misses. From immunization you know how to construct a portfolio whose value is shielded from small parallel shifts in rates by matching duration to a target horizon. Interest rate risk management extends these tools into active practice: how do institutions actually protect themselves when rates can move in complex, unpredictable ways?

The simplest case — a **parallel shift** of the yield curve — is what duration-based immunization is designed to handle. If all yields rise by the same amount across every maturity, a portfolio whose dollar duration matches its liability duration will experience roughly offsetting price changes. But real yield curve moves are rarely perfectly parallel. The curve can **steepen** (long rates rise more than short rates), **flatten** (short rates rise more), or **twist** in more complex ways. A portfolio immunized against parallel shifts can still lose value if the slope or curvature of the curve changes unexpectedly. Managing these exposures requires thinking about multiple **key rate durations** — the sensitivity to rate changes at specific maturities — rather than a single aggregate duration.

**Convexity** is the interest rate risk manager's friend under large moves. Because of convexity, a bond gains more price when rates fall by a given amount than it loses when rates rise by the same amount. Portfolios with higher convexity outperform lower-convexity portfolios of the same duration if rates move significantly in either direction. Managers who expect high rate volatility therefore seek **convexity-rich** portfolios (bonds with embedded options like callables reduce convexity; zero-coupon bonds and bullet maturities maximize it). This is why convexity has a cost — it is priced in through lower yields.

When immunization through portfolio construction is insufficient, **interest rate derivatives** extend the toolkit. Interest rate **swaps** convert fixed-rate cash flows to floating or vice versa, effectively changing the duration of a position without selling the underlying bonds. **Interest rate futures** and **options** (caps, floors, swaptions) allow targeted hedges against specific yield curve scenarios. A corporate treasurer who issued fixed-rate debt but expects rates to fall might enter a receive-fixed swap, transforming the effective economics without altering the balance sheet. The key principle across all these strategies is the same: identify which dimension of rate movement creates the most risk for your specific portfolio or liability structure, then use instruments that hedge precisely that dimension without introducing unwanted exposures elsewhere.
