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

## Questions

```yaml
- question: "A bond has modified duration of 8 and convexity of 100. Yields rise by 200 basis points. Compared to what duration alone predicts, the actual price decline will be:"
  type: multiple-choice
  options:
    - "Larger — convexity amplifies losses when yields rise"
    - "Smaller — convexity partially offsets the loss because the convexity term is always positive"
    - "The same — convexity only matters when yields fall, not when they rise"
    - "Larger only if the bond is a zero-coupon bond"
  answer: 1
  explanation: "The full formula is ΔP/P ≈ −D·Δy + (C/2)·(Δy)². The convexity term (C/2)·(Δy)² is always positive regardless of the direction of the yield move, because (Δy)² is always positive. When yields rise, this positive term partially offsets the negative duration term, making the actual price fall smaller than duration alone predicts. Convexity benefits the bondholder symmetrically in both directions."

- question: "Two bonds have identical durations of 7. Bond A has convexity 120; Bond B has convexity 40. In a volatile rate environment with potentially large moves in either direction, which is preferable?"
  type: multiple-choice
  options:
    - "Bond B — lower convexity means more predictable, stable price behavior"
    - "Bond A — higher convexity means better price performance whether rates rise or fall"
    - "They are equally attractive since duration determines rate sensitivity"
    - "Bond A only if rates are expected to fall; Bond B if rates are expected to rise"
  answer: 1
  explanation: "Higher convexity is always preferable when holding duration constant, because it provides an asymmetric benefit: the bond gains more when yields fall than it loses when yields rise by the same amount. In volatile environments, large yield moves in either direction favor high convexity. Option D reflects the misconception that convexity helps only when rates fall — but it reduces losses equally when rates rise."

- question: "Because the convexity correction term is always positive, a bond with positive convexity gains more when yields fall than it loses when yields rise by the same amount."
  type: true-false
  answer: true
  explanation: "This is the key asymmetric property of positive convexity. In both directions of yield change, the (C/2)·(Δy)² term adds back to the price change — it reduces losses when yields rise and amplifies gains when yields fall. This makes price response to yield changes asymmetric: the gains exceed the losses for equal-sized moves, which is why high convexity is a desirable bond characteristic that commands a price premium."

- question: "Convexity matters most when managing small, day-to-day interest rate fluctuations, and is less important for large rate moves."
  type: true-false
  answer: false
  explanation: "The opposite is true. The convexity correction is proportional to (Δy)², which grows rapidly for larger moves. For a 10 basis point move, (Δy)² = 0.0001; for a 200 basis point move, (Δy)² = 0.04 — four hundred times larger. For small daily fluctuations, the duration approximation is highly accurate and convexity adds negligible correction. Convexity becomes material precisely when yields make large moves, such as during rate shocks or crises."

- question: "Why does a callable bond exhibit negative convexity at low yields, and how does this differ from a standard non-callable bond?"
  type: short-answer
  answer: "A callable bond gives the issuer the right to redeem it at par when rates fall. As yields decline, the bond's price rises toward the call price — but once yields fall far enough, the issuer will call the bond, capping price appreciation at par. The bondholder cannot benefit from further yield declines because the bond will be redeemed. Meanwhile, if yields rise, there's no such cap on losses. This produces negative convexity: price gains from falling rates are truncated while price losses from rising rates are not. A standard non-callable bond has no such cap — its price keeps rising as yields fall, giving it positive convexity with symmetric asymmetric benefit."
  explanation: "The call option effectively transfers upside convexity from the bondholder to the issuer, reversing the asymmetry that defines positive convexity."
```

## Explainer

You already know that **duration** measures a bond's price sensitivity to small yield changes — specifically, the percentage price change is approximately equal to negative modified duration times the yield change. This linear approximation is excellent for small moves in yields. But the price-yield relationship for a bond is not actually linear; it is a curve. As yields move further from their starting value, the duration approximation accumulates error. Convexity measures the curvature of that price-yield curve and provides the second-order correction that fixes the approximation for large moves.

Mathematically, the full approximation is: ΔP/P ≈ −D × Δy + (C/2) × (Δy)². The first term is the duration effect — linear in the yield change. The second term is the **convexity** correction — it is always positive for a standard bond because C > 0 and (Δy)² > 0 regardless of the direction of the move. This positive second term has an important asymmetric implication: when yields rise (Δy > 0), the price falls *less* than duration alone predicts, because convexity partially offsets the loss. When yields fall (Δy < 0), the price rises *more* than duration predicts. Convexity therefore makes the bond's price response asymmetric: it gains more on yield declines than it loses on equal yield increases. This is sometimes called being "long convexity."

The magnitude of convexity matters more as the yield move gets larger. For a 10 basis point move, the (Δy)² term is tiny (0.001²) and convexity barely matters. For a 200 basis point move, (Δy)² = 0.04 — four times the (0.01)² of a 100bp move — and convexity becomes material. This is why convexity is most practically important when yields are volatile or when you need to hedge large positions. In calm markets with small daily moves, managing duration is sufficient; in volatile markets or crisis periods, ignoring convexity leads to significant hedging errors.

Long-duration bonds typically have high convexity, and investors pay for it. A zero-coupon bond with 30-year maturity has extreme convexity — its price-yield curve curves sharply. Bonds with **negative convexity** — like callable bonds, where the issuer has the right to redeem them early — behave differently: as yields fall, the call option caps price appreciation because the issuer will redeem at par. Mortgage-backed securities exhibit negative convexity for the same reason (homeowners prepay when rates fall). Negative convexity means price gains when yields fall are capped while losses when yields rise are not — the opposite of the symmetric benefit of positive convexity. When comparing bonds with similar durations, positive convexity is a desirable property that commands a price premium.
