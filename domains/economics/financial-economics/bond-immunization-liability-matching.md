---
id: bond-immunization-liability-matching
title: Bond Immunization and Liability Matching
domain: economics
course: financial-economics
prerequisites:
- id: interest-rate-risk-duration
  type: hard
- id: net-present-value
  type: hard
tags:
- fixed-income
- portfolio-management
- liability-matching
stage: formal-systems
status: draft
---

# Bond Immunization and Liability Matching

## Core Idea
Immunization constructs a bond portfolio whose duration matches the time horizon of liabilities, eliminating interest rate risk for that specific horizon. Even if rates change, the portfolio value at the liability date remains predictable.

## How It's Best Learned
Work through a liability-matching problem: given a specific payment due in 5 years, construct a bond portfolio that immunizes against rate risk using duration matching.

## Questions

```yaml
- question: "A pension fund immunizes a liability due in 8 years by setting portfolio duration to 8 years. Interest rates then rise by 1%. What best describes the fund's position at the 8-year liability date?"
  type: multiple-choice
  options:
    - "The fund will be short — rising rates reduce the portfolio's present value"
    - "The fund will be overfunded — rising rates increase reinvestment income on coupons"
    - "The fund remains approximately immunized — the price decline and reinvestment gain roughly cancel at the 8-year horizon"
    - "The fund must immediately sell long bonds to avoid losses"
  answer: 2
  explanation: "When rates rise: (1) portfolio market value falls (price effect, bad) and (2) reinvested coupon payments earn more going forward (reinvestment effect, good). Duration matching engineers these two effects to approximately cancel at the target horizon, leaving the terminal portfolio value unchanged. Options A and B each capture one effect while ignoring the other — both are partial and misleading. The key insight of immunization is that both effects exist simultaneously and are set to offset each other."

- question: "Why must an immunized bond portfolio be rebalanced periodically rather than set up once and left alone?"
  type: multiple-choice
  options:
    - "Because bond prices fluctuate randomly, requiring constant monitoring"
    - "Because the portfolio's duration drifts as time passes and rates change, breaking the match between duration and remaining liability horizon"
    - "Because the liability itself changes after the immunization is set up"
    - "Because immunization only holds exactly on the setup date, not at any subsequent date"
  answer: 1
  explanation: "Two forces cause duration drift: (1) as calendar time passes, the remaining liability horizon shortens (from 8 years to 7, then 6, etc.), while the portfolio's duration changes at a different rate; and (2) interest rate changes alter the modified duration of existing bonds. Both effects push portfolio duration away from the target horizon, breaking the offsetting mechanism. Rebalancing — buying or selling bonds to restore the duration match — is necessary to maintain immunization, though transaction costs make this a practical trade-off rather than a continuous process."

- question: "Bond immunization works because rising interest rates hurt bond prices but help reinvestment income, and at the duration-matched horizon these effects approximately cancel."
  type: true-false
  answer: true
  explanation: "This is the core economic mechanism. A bond portfolio's value is affected by interest rates in two opposing ways: higher rates lower present value (price effect) but allow coupons to be reinvested at higher rates (reinvestment effect). Duration measures the weighted-average time at which cash flows are received — it is also the horizon at which these two effects precisely offset under small parallel rate shifts. Matching portfolio duration to the liability horizon places this 'balancing point' exactly at the date the money is needed."

- question: "Cash flow matching and duration matching are equivalent strategies that produce the same portfolio and the same level of interest rate protection."
  type: true-false
  answer: false
  explanation: "They are related but distinct. Duration matching constructs any portfolio achieving the target duration number — bonds whose individual cash flows need not align with the liability date. Cash flow matching (dedication) purchases bonds whose actual payments arrive on exactly the liability payment dates, eliminating reinvestment risk for those matched cash flows. Cash flow matching provides tighter protection but is more expensive and less flexible. Duration matching allows more portfolio choice but requires periodic rebalancing and is only an approximation under small rate shifts. They are not equivalent."

- question: "Explain the economic logic of why matching a bond portfolio's duration to a liability's time horizon protects against interest rate changes."
  type: short-answer
  answer: "When rates change, two effects move in opposite directions: the portfolio's market value changes (price effect) and the rate at which coupons can be reinvested changes (reinvestment effect). Duration measures the weighted-average time to receive cash flows — it is also the horizon at which these two effects exactly offset. By setting portfolio duration equal to the liability horizon, the portfolio is structured so that any rate change that hurts one effect helps the other by an equal amount, leaving the terminal value at the liability date approximately unchanged."
  explanation: "The insight is that a bond is not a single payment — it is a stream of coupons plus a principal payment. Each component has different sensitivity to rate changes. Duration is the weighted average of those timings and also the 'break-even horizon' where price sensitivity and reinvestment sensitivity cancel. Before the duration date, price effects dominate (rate rises hurt); after it, reinvestment effects dominate (rate rises help). At the duration date itself, the two effects are in balance — which is exactly why matching duration to the liability date achieves immunization."
```

## Explainer

A pension fund knows it must pay $10 million to retirees in exactly 8 years. The fund holds a bond portfolio today worth roughly that amount in present value. The problem: interest rates might change between now and the payment date. If rates rise, the portfolio's value falls. If rates fall, reinvested coupon income earns less. **Immunization** is the strategy that makes the fund indifferent to these rate moves — the two effects (price change and reinvestment rate change) are engineered to cancel each other at the target horizon.

The mechanism works through **duration**, which you already understand as the interest-rate sensitivity measure. Recall that duration measures both price sensitivity and the weighted-average time at which you receive cash flows. If you match the duration of your bond portfolio to the time horizon of your liability, a fascinating offsetting dynamic kicks in: when rates rise, your bonds fall in value (price effect is bad) but you reinvest coupons at higher rates (reinvestment effect is good). When rates fall, your bonds rise in value (price effect is good) but you reinvest coupons at lower rates (reinvestment effect is bad). At the duration-matched horizon, these effects precisely offset, leaving the portfolio value at the liability date unchanged regardless of which direction rates moved.

The mechanics require setting the **modified duration** of your portfolio equal to your target horizon. If you need to fund a liability in 8 years, you build a bond portfolio with a duration of 8 years. Since individual bonds have durations limited by their maturity and coupon structure, this typically means combining shorter-duration and longer-duration bonds to hit the target. A portfolio mixing a 4-year bond and a 12-year bond in the right proportions can achieve a duration of 8. The portfolio weights are solved using the duration-weighted-average formula: D_portfolio = w₁D₁ + w₂D₂, where w₁ + w₂ = 1. The **net present value** framework is embedded here — the value of your asset portfolio must equal the present value of liabilities not just today but durably across rate scenarios.

A critical practical caveat: immunization is not a one-time setup. As time passes, rates change, bonds age, and the portfolio's duration drifts away from the target horizon. Maintaining immunization requires **rebalancing** — periodically readjusting the portfolio to restore the duration match. The frequency of rebalancing trades off transaction costs against immunization precision. More sophisticated approaches — **cash flow matching** (literally purchasing bonds whose cash flows occur exactly at each liability payment date) or **convexity matching** (adding a second condition to account for curvature in the price-yield relationship) — can provide tighter protection at the cost of reduced flexibility and higher initial investment. Immunization is not a perfect hedge, but for institutions with predictable fixed liabilities, it remains a foundational fixed-income management technique.
