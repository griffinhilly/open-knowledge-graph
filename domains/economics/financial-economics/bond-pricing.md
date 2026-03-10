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
status: draft
---

# Bond Pricing

## Core Idea
A bond's price equals the present value of all its future cash flows — coupon payments and face value — discounted at the market interest rate: Price = Σ[C/(1+r)^t] + F/(1+r)^T. Bond prices and interest rates move inversely: when rates rise, existing bond prices fall, because future fixed payments are discounted more heavily. Bonds trade at par (price = face value) when the coupon rate equals the market rate, at a premium when the coupon exceeds market rates, and at a discount otherwise. This inverse relationship is not a market anomaly but a mathematical necessity of present-value discounting.

## How It's Best Learned
Price a 5-year, 5% coupon bond at market rates of 3%, 5%, and 7% to observe the price-rate inverse relationship. Verify that coupon rate equal to market rate always gives a price of par. Use a spreadsheet to handle multi-period discounting for precision.

## Common Misconceptions
- Bonds do not always trade at face value — they do so only when the coupon rate matches the current market rate, which is rarely the case after issuance.
- Confusing the coupon rate (a fixed contractual rate) with the discount rate used in pricing (which reflects current market conditions).
