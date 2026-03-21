---
id: zero-coupon-bond-valuation
title: Zero-Coupon Bond Pricing and Valuation
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: bond-pricing
  type: soft
builds-toward:
  - bond-duration-application
tags:
- bonds
- fixed-income
- valuation
- discounting
stage: formal-systems
status: draft
---
# Zero-Coupon Bond Pricing and Valuation

## Core Idea
Zero-coupon bonds make a single payment at maturity, making them the simplest fixed-income instruments to value. Their price equals the discounted present value of the face amount using the yield to maturity: P = FV / (1+y)^n. These bonds are particularly useful for studying term structure because each maturity has a single cash flow.

## Questions

```yaml
- question: "A 10-year zero-coupon bond with face value $1,000 is priced at $614 when the yield is 5%. Market rates for 10-year instruments then rise to 7%. What happens to the bond's price?"
  type: multiple-choice
  options:
    - "The price rises above $614 because higher rates signal a stronger economy"
    - "The price stays at $614 because zero-coupon bonds have no coupon rate to change"
    - "The price falls below $614 because higher discount rates reduce the present value of the future payment"
    - "The price falls to $0 because the bond becomes worthless when market rates exceed its yield"
  answer: 2
  explanation: "P = FV/(1+y)^n. As y increases, the denominator grows, so P falls. At y = 7%, P = 1000/(1.07)^10 ≈ $508 — well below $614. Price and yield always move in opposite directions: the fixed future payment is worth less when discounted at a higher rate. Zero-coupon bonds are especially sensitive to rate changes (they have high duration) because all cash flow is concentrated at maturity with no intermediate coupons to partially offset the repricing."

- question: "A zero-coupon bond with face value $1,000 matures in 3 years and currently trades at $864. What is its yield to maturity?"
  type: multiple-choice
  options:
    - "Approximately 15.7%, calculated as (1000 − 864) / 864"
    - "Approximately 5%, calculated as (1000/864)^(1/3) − 1"
    - "Approximately 5%, calculated as (1000 − 864) / 1000"
    - "Cannot be determined without knowing the bond's coupon rate"
  answer: 1
  explanation: "Solving P = FV/(1+y)^n for y: y = (FV/P)^(1/n) − 1 = (1000/864)^(1/3) − 1 ≈ 0.050 = 5%. Option A computes a simple (uncompounded) return over three years, ignoring the time value of compounding. Option D is wrong because zero-coupon bonds have no coupon — the yield is entirely derived from the discount at which the bond trades. Yield to maturity is the implied compound annual return that equates today's price to the discounted face value."

- question: "A zero-coupon bond with a positive yield always trades below its face value prior to maturity."
  type: true-false
  answer: true
  explanation: "P = FV/(1+y)^n. If y > 0 and n > 0, then (1+y)^n > 1, so P < FV. The only exception is a negative yield (y < 0), which occurs in some markets when investors pay a premium for safety. At maturity (n = 0), (1+y)^0 = 1, so P = FV — the bond redeems at exactly face value. The investor's entire return is the difference between the purchase price and par, accruing as the bond approaches maturity."

- question: "The yield to maturity on a zero-coupon bond is set by the issuer at issuance and does not change over the bond's lifetime."
  type: true-false
  answer: false
  explanation: "Yield to maturity is derived from the bond's market price, not set by the issuer. The issuer determines the face value and maturity date; the market determines the trading price, and yield is whatever rate makes the discounted face value equal to that price. As market interest rates change, the bond's price adjusts to remain competitive, and the implied yield changes accordingly. Yields are prices in disguise — a more convenient way to express the relationship between today's price and the promised future payment."

- question: "Why are zero-coupon bonds especially useful as building blocks for constructing the spot rate curve, compared to coupon bonds?"
  type: short-answer
  answer: "Each zero-coupon bond has exactly one cash flow at a single maturity date. Its yield is therefore an unambiguous discount rate for that specific maturity — a 'pure' interest rate for that horizon. Coupon bonds have multiple cash flows at different dates, so their yield to maturity is a blend of rates across multiple maturities rather than a clean rate for any single point on the curve. Zero-coupon bonds provide direct, unambiguous readings of the price of money at each horizon without coupon reinvestment complications."
  explanation: "The spot rate curve represents the pure cost of money at each time horizon, free from reinvestment assumptions. Coupon bonds carry reinvestment risk — intermediate coupons must be reinvested at future rates that are unknown today. A zero-coupon bond eliminates this: one investment today, one payment at maturity. That simplicity makes them the natural instrument for building the term structure, which is why even when zero-coupon bonds don't directly exist for a maturity, analysts 'strip' coupon bonds to synthetically construct them."
```

## Explainer

Your prerequisite work on present value and discounting established the core principle: a dollar received in the future is worth less than a dollar today, and the discount rate reflects the opportunity cost of waiting. A **zero-coupon bond** is the purest application of that principle. Unlike a coupon bond that pays periodic interest, a zero-coupon bond makes exactly one payment — the **face value** (or **par value**) — at a specified maturity date. You buy it today at a discount and receive the full face value at maturity; the difference is your return.

The pricing formula is a direct application of present value: P = FV / (1 + y)^n, where P is today's price, FV is the face value, y is the **yield to maturity** (the discount rate), and n is the number of periods to maturity. If a zero-coupon bond promises $1,000 in 5 years and the prevailing yield for 5-year instruments is 4%, then P = 1000 / (1.04)^5 = $821.93. The bond trades at a discount to face value; at maturity, the holder simply receives the $1,000 without any intermediate cash flows.

The **yield to maturity** here is both an input and an output depending on what you know. If you know the market price and the face value, you can solve for y: y = (FV/P)^(1/n) − 1. This is the bond's **implied discount rate** — the constant rate that, applied each period, turns today's price into the future face value. This inverted view of the formula is essential: bond yields are derived from prices, not set by the issuer. When market interest rates rise, existing bond prices must fall to offer competitive yields to new buyers, and this price-yield relationship is especially clean and transparent for zero-coupon bonds because there is only one cash flow to discount.

Zero-coupon bonds are particularly valuable as building blocks in fixed income analysis. Any coupon bond can be decomposed into a bundle of zero-coupon bonds — each coupon payment is a small zero-coupon bond, and the final principal payment is a larger one. This decomposition underpins the concept of the **spot rate curve** (also called the zero curve or term structure): the collection of yields implied by zero-coupon bonds of different maturities. Since each maturity has exactly one cash flow, each point on the spot rate curve is identified cleanly, without the coupon reinvestment complications that muddy coupon bond yields. When you go on to study the term structure of interest rates, zero-coupon bond prices are the raw material from which all other fixed-income relationships are built.
