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
- id: bond-duration-application
  type: soft
builds-toward:
- bond-immunization-liability-matching
- bond-portfolio-strategies
tags:
- fixed-income
- risk-management
- interest-rates
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A bond has a modified duration of 6 years. Interest rates rise by 100 basis points (1 percentage point). What is the approximate percentage change in the bond's price?"
  type: multiple-choice
  options:
    - "+6% — bond prices rise when rates rise"
    - "−6% — the bond loses approximately 6% of its price"
    - "−1% — only the coupon payments are affected, not the price"
    - "−0.6% — duration must be divided by 10 when working with basis points"
  answer: 1
  explanation: "The duration approximation is ΔP/P ≈ −D* × Δy. With D* = 6 and Δy = +0.01 (100 bps expressed as a decimal), ΔP/P ≈ −6 × 0.01 = −0.06 = −6%. Bond prices and yields move inversely, so rising rates produce price losses. Option A reverses the relationship. Option D confuses the units — 100 basis points = 1 percentage point = 0.01 in decimal, not 0.001."

- question: "Which of the following bonds has the greatest interest rate sensitivity?"
  type: multiple-choice
  options:
    - "A 5-year bond with a 10% annual coupon"
    - "A 5-year zero-coupon bond"
    - "A 10-year bond with a 10% annual coupon"
    - "A 30-year bond with a 15% annual coupon"
  answer: 1
  explanation: "A zero-coupon bond pays nothing until maturity, so its Macaulay duration equals its maturity exactly — 5 years here. A coupon bond of the same maturity receives intermediate cash flows that pull the weighted-average time forward, giving it duration less than 5 years. The 10-year and 30-year coupon bonds have longer maturities but large coupon payments drag their durations considerably below maturity. The 5-year zero-coupon bond has the highest duration relative to its maturity structure among these choices."

- question: "A pension fund can protect its funding ratio from interest rate movements by setting the duration of its bond portfolio equal to the duration of its future liabilities."
  type: true-false
  answer: true
  explanation: "This is duration matching (immunization). If portfolio duration equals liability duration, a change in rates moves the present value of assets and liabilities by approximately the same percentage, preserving the funding ratio. A 1% rate rise that reduces bond values by 7% also reduces the present value of future liabilities by approximately 7% — leaving the fund just as well-funded. Pension funds and insurance companies use exactly this strategy to guarantee they can meet future obligations regardless of rate movements."

- question: "A bond's duration usually equals its time to maturity."
  type: true-false
  answer: false
  explanation: "Duration equals maturity only for zero-coupon bonds, which pay nothing until maturity. For any coupon bond, intermediate cash flows received before maturity pull the weighted average time below the maturity date. Macaulay duration is always less than or equal to maturity, with equality only at the zero-coupon extreme. A 10-year bond with a 6% annual coupon might have a Macaulay duration of roughly 7–8 years — confusing duration with maturity would significantly overestimate its interest rate risk."

- question: "Why does a zero-coupon bond have greater interest rate sensitivity than a coupon bond of the same maturity, and what does this imply for portfolio construction?"
  type: short-answer
  answer: "A zero-coupon bond's entire value is a single payment at maturity — no early cash flows cushion against rate changes. Its Macaulay duration equals its maturity, the longest possible for a bond of that term. A coupon bond of the same maturity receives coupon payments along the way; those early payments shorten the cash-flow-weighted average time, reducing duration and price sensitivity. For portfolio construction, zero-coupon bonds are the most powerful tool for extending portfolio duration — a small allocation dramatically raises rate sensitivity. Conversely, high-coupon bonds shorten duration without reducing nominal maturity."
  explanation: "The insight connects the mechanical definition (Macaulay duration as a weighted average of cash flow timing) to practical portfolio management. Duration is a design variable: choosing between zero-coupon and coupon bonds lets a manager tune interest rate exposure precisely, which is exactly what immunization and liability-matching strategies require."
```

## Explainer

From bond pricing, you know that bond prices and yields move in opposite directions, and from duration and convexity, you know that **duration** measures the weighted average time until a bond's cash flows are received, serving as a first-order measure of price sensitivity. Here, we connect those mechanics to the practical problem of managing interest rate risk in a portfolio: how do you know how much you stand to lose if rates move, and how do you control that exposure?

The key formula is the duration approximation: ΔP/P ≈ −D* × Δy, where D* is **modified duration** and Δy is the change in yield. If a bond has a modified duration of 7 years and rates rise by 1 percentage point (100 basis points), the bond price falls by approximately 7%. This linear approximation works well for small rate changes; for large shocks, you need to add convexity to get an accurate picture. Modified duration and Macaulay duration are closely related: D* = D_mac / (1 + y), so for bonds priced near par at typical yields, they're nearly the same, but the distinction matters for precise risk calculations.

Duration also functions as a **portfolio management tool**. The duration of a bond portfolio is the value-weighted average duration of its holdings. A portfolio manager who expects rates to fall will lengthen portfolio duration (shift to longer-maturity, lower-coupon bonds) to amplify the price gain. A manager who expects rates to rise — or who needs to hedge a known liability — will shorten duration. **Duration matching** (immunization) involves setting portfolio duration equal to the duration of a liability stream, ensuring that a rate change affects assets and liabilities equally, protecting the funding ratio. Pension funds and insurance companies do exactly this to guarantee they can meet future obligations regardless of interest rate movements.

The limitation of duration alone is that it treats the price-yield relationship as linear. It isn't: bonds have **convexity**, meaning the price rise when yields fall is larger than the price fall when yields rise by the same amount. For large rate shocks — 200 bps or more — ignoring convexity produces material errors in the price forecast. A portfolio of high-convexity bonds will outperform a low-convexity portfolio of equal duration if rates move significantly in either direction. This is why traders pay attention to both duration (sensitivity) and convexity (how that sensitivity changes) when constructing interest rate positions.
