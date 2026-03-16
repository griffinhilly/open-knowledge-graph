---
id: interest-rate-risk-duration
title: Interest Rate Risk and Duration Strategy
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: duration-and-convexity
  type: hard
builds-toward:
- bond-immunization-liability-matching
- bond-portfolio-strategies
tags:
- fixed-income
- risk-management
- interest-rates
stage: formal-systems
status: draft
---

# Interest Rate Risk and Duration Strategy

## Core Idea
Duration measures bond price sensitivity to interest rate changes. A bond's duration determines how much its price falls when rates rise (or rises when rates fall), allowing investors to quantify and manage interest rate risk in fixed income portfolios.

## How It's Best Learned
Start with calculating duration for simple bonds, then compare duration-adjusted returns across bonds with different coupons and maturities. Use scenario analysis (e.g., rates up/down 100 bps) to verify predicted price changes.

## Common Misconceptions
- Duration is not maturity; a bond's duration is always less than or equal to its maturity.
- Modified duration and Macaulay duration differ by a factor related to yield.
- Convexity matters more for larger rate shocks.

## Explainer

From bond pricing, you know that bond prices and yields move in opposite directions, and from duration and convexity, you know that **duration** measures the weighted average time until a bond's cash flows are received, serving as a first-order measure of price sensitivity. Here, we connect those mechanics to the practical problem of managing interest rate risk in a portfolio: how do you know how much you stand to lose if rates move, and how do you control that exposure?

The key formula is the duration approximation: ΔP/P ≈ −D* × Δy, where D* is **modified duration** and Δy is the change in yield. If a bond has a modified duration of 7 years and rates rise by 1 percentage point (100 basis points), the bond price falls by approximately 7%. This linear approximation works well for small rate changes; for large shocks, you need to add convexity to get an accurate picture. Modified duration and Macaulay duration are closely related: D* = D_mac / (1 + y), so for bonds priced near par at typical yields, they're nearly the same, but the distinction matters for precise risk calculations.

Duration also functions as a **portfolio management tool**. The duration of a bond portfolio is the value-weighted average duration of its holdings. A portfolio manager who expects rates to fall will lengthen portfolio duration (shift to longer-maturity, lower-coupon bonds) to amplify the price gain. A manager who expects rates to rise — or who needs to hedge a known liability — will shorten duration. **Duration matching** (immunization) involves setting portfolio duration equal to the duration of a liability stream, ensuring that a rate change affects assets and liabilities equally, protecting the funding ratio. Pension funds and insurance companies do exactly this to guarantee they can meet future obligations regardless of interest rate movements.

The limitation of duration alone is that it treats the price-yield relationship as linear. It isn't: bonds have **convexity**, meaning the price rise when yields fall is larger than the price fall when yields rise by the same amount. For large rate shocks — 200 bps or more — ignoring convexity produces material errors in the price forecast. A portfolio of high-convexity bonds will outperform a low-convexity portfolio of equal duration if rates move significantly in either direction. This is why traders pay attention to both duration (sensitivity) and convexity (how that sensitivity changes) when constructing interest rate positions.
