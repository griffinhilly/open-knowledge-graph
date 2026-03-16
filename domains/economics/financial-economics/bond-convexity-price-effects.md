---
id: bond-convexity-price-effects
title: Convexity and Non-Linear Price-Yield Relationships
domain: economics
course: financial-economics
prerequisites:
- id: duration-and-convexity
  type: hard
- id: bond-pricing
  type: soft
builds-toward:
- bond-duration-application
tags:
- bonds
- convexity
- interest-rate-sensitivity
- pricing
stage: formal-systems
status: draft
---

# Convexity and Non-Linear Price-Yield Relationships

## Core Idea
Bond prices are convex functions of yields: large yield changes violate the linear duration approximation. Convexity measures this curvature, and the full price change formula is: ΔP ≈ -D × Δy + (C/2) × (Δy)². Positive convexity means bond prices fall less when yields rise and rise more when yields fall, making long-duration bonds with high convexity especially attractive.

## How It's Best Learned
Compare actual bond price changes from large yield moves against duration-only approximations to see where convexity becomes important.

## Explainer

You already know that **duration** measures a bond's price sensitivity to small yield changes — specifically, the percentage price change is approximately equal to negative modified duration times the yield change. This linear approximation is excellent for small moves in yields. But the price-yield relationship for a bond is not actually linear; it is a curve. As yields move further from their starting value, the duration approximation accumulates error. Convexity measures the curvature of that price-yield curve and provides the second-order correction that fixes the approximation for large moves.

Mathematically, the full approximation is: ΔP/P ≈ −D × Δy + (C/2) × (Δy)². The first term is the duration effect — linear in the yield change. The second term is the **convexity** correction — it is always positive for a standard bond because C > 0 and (Δy)² > 0 regardless of the direction of the move. This positive second term has an important asymmetric implication: when yields rise (Δy > 0), the price falls *less* than duration alone predicts, because convexity partially offsets the loss. When yields fall (Δy < 0), the price rises *more* than duration predicts. Convexity therefore makes the bond's price response asymmetric: it gains more on yield declines than it loses on equal yield increases. This is sometimes called being "long convexity."

The magnitude of convexity matters more as the yield move gets larger. For a 10 basis point move, the (Δy)² term is tiny (0.001²) and convexity barely matters. For a 200 basis point move, (Δy)² = 0.04 — four times the (0.01)² of a 100bp move — and convexity becomes material. This is why convexity is most practically important when yields are volatile or when you need to hedge large positions. In calm markets with small daily moves, managing duration is sufficient; in volatile markets or crisis periods, ignoring convexity leads to significant hedging errors.

Long-duration bonds typically have high convexity, and investors pay for it. A zero-coupon bond with 30-year maturity has extreme convexity — its price-yield curve curves sharply. Bonds with **negative convexity** — like callable bonds, where the issuer has the right to redeem them early — behave differently: as yields fall, the call option caps price appreciation because the issuer will redeem at par. Mortgage-backed securities exhibit negative convexity for the same reason (homeowners prepay when rates fall). Negative convexity means price gains when yields fall are capped while losses when yields rise are not — the opposite of the symmetric benefit of positive convexity. When comparing bonds with similar durations, positive convexity is a desirable property that commands a price premium.
