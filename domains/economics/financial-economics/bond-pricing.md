---
id: bond-pricing
title: Bond Pricing
domain: economics
course: financial-economics
prerequisites:
- id: bond-basics
  type: hard
- id: present-value-and-discounting
  type: hard
- id: annuities-and-perpetuities
  type: soft
- id: geometric-series
  type: soft
builds-toward:
- yield-to-maturity
- duration-and-convexity
tags:
- bond-pricing
- fixed-income
- inverse-relationship
- discount-premium
stage: formal-systems
status: validated
---

# Bond Pricing

## Core Idea
A bond's price equals the present value of all its future cash flows — coupon payments and face value — discounted at the market interest rate: Price = Σ[C/(1+r)^t] + F/(1+r)^T. Bond prices and interest rates move inversely: when rates rise, existing bond prices fall, because future fixed payments are discounted more heavily. Bonds trade at par (price = face value) when the coupon rate equals the market rate, at a premium when the coupon exceeds market rates, and at a discount otherwise. This inverse relationship is not a market anomaly but a mathematical necessity of present-value discounting.

## How It's Best Learned
Price a 5-year, 5% coupon bond at market rates of 3%, 5%, and 7% to observe the price-rate inverse relationship. Verify that coupon rate equal to market rate always gives a price of par. Use a spreadsheet to handle multi-period discounting for precision.

## Common Misconceptions
- Bonds do not always trade at face value — they do so only when the coupon rate matches the current market rate, which is rarely the case after issuance.
- Confusing the coupon rate (a fixed contractual rate) with the discount rate used in pricing (which reflects current market conditions).

## Questions

```yaml
- question: "A 10-year bond pays a 5% annual coupon on a $1,000 face value. If market interest rates rise to 8%, what happens to the bond's price?"
  type: multiple-choice
  options:
    - "It rises above $1,000, because the coupon payments are now more valuable relative to new bonds"
    - "It stays at $1,000, because the face value is a contractual guarantee"
    - "It falls below $1,000, because investors can earn 8% on new bonds and will only buy this 5% bond at a discount"
    - "It cannot change until the bond matures"
  answer: 2
  explanation: "When market rates exceed the coupon rate, existing bonds must offer a compensating discount to attract buyers. Discounting the fixed cash flows (5% × $1,000 = $50 per year plus $1,000 at maturity) at 8% yields a present value below $1,000. The bond trades at a discount so that its effective return matches the 8% available in the market."

- question: "A bond's coupon rate and its yield to maturity are generally the same number."
  type: true-false
  answer: false
  explanation: "The coupon rate is fixed at issuance and determines the dollar amount of coupon payments. The yield to maturity reflects current market interest rates and changes continuously with supply and demand. They are equal only when the bond trades at exactly par (face value) — which happens only when market rates happen to equal the coupon rate, rarely the case after the initial issuance date."

- question: "Explain intuitively, without using a formula, why a bond's price and prevailing interest rates move in opposite directions."
  type: short-answer
  answer: "A bond's cash flows are fixed in dollar terms. When market rates rise, investors can earn more from new bonds, so they will only buy the old bond at a lower price — a discount that compensates them for receiving below-market coupons."
  explanation: "Think of it as competition. If you own a bond paying $50/year and new bonds now pay $80/year on the same face value, no rational investor pays full price for yours. The price must fall until the effective yield (coupon divided by price, simplified) equals the market rate. The math of present-value discounting formalizes this intuition: discounting fixed cash flows at a higher rate always produces a lower present value."
```

## Explainer

You already know how to calculate the present value of a future cash flow: divide by (1 + r)^t, where r is the discount rate and t is the number of periods. A bond is simply a bundle of future cash flows — a series of coupon payments (typically annual or semiannual) and the return of face value at maturity. Pricing a bond means computing the present value of all those cash flows, discounted at the current market interest rate. That is the entire concept; the rest is application.

The formula makes this explicit: Price = C/(1+r) + C/(1+r)² + ... + C/(1+r)^T + F/(1+r)^T, where C is the coupon payment, r is the market rate, T is time to maturity, and F is face value. The coupon payments form an annuity (hence the soft prerequisite), and the face value is a single lump sum. In a spreadsheet, you sum these terms explicitly; on an exam, you use the annuity formula to collapse the coupon stream.

The inverse price-rate relationship follows directly from the present-value logic. Fix the cash flows — they are contractual and do not change. Now increase the discount rate r. Every term in the sum gets smaller (dividing by a larger number), so the total price falls. This is not a market phenomenon or a coincidence; it is a mathematical necessity. The relationship is also nonlinear: prices fall faster when rates rise starting from low levels than from high levels, a property formalized as *convexity* in more advanced fixed-income analysis.

Whether a bond trades at par, a premium, or a discount tells you immediately how the coupon rate compares to current market rates. When coupon rate = market rate, price = par. When coupon rate > market rate, price > par (premium — investors pay extra for above-market coupon income). When coupon rate < market rate, price < par (discount — buyers demand compensation for below-market income). This three-way classification is worth internalizing because it lets you reason about bond prices qualitatively without any calculation.

One distinction that trips up many students: the coupon rate is a fixed number stamped on the bond contract. The discount rate (or yield to maturity) is the market's current required return, and it changes daily. When you price a bond, you use the market rate as r — not the coupon rate. The coupon rate only determines the size of the coupon cash flows. Mixing these up leads to pricing a bond at par no matter what the market does, which misses the entire point of bond valuation.

