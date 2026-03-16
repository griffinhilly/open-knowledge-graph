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
- interest-rate-term-structure
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

## Explainer

Your prerequisite work on present value and discounting established the core principle: a dollar received in the future is worth less than a dollar today, and the discount rate reflects the opportunity cost of waiting. A **zero-coupon bond** is the purest application of that principle. Unlike a coupon bond that pays periodic interest, a zero-coupon bond makes exactly one payment — the **face value** (or **par value**) — at a specified maturity date. You buy it today at a discount and receive the full face value at maturity; the difference is your return.

The pricing formula is a direct application of present value: P = FV / (1 + y)^n, where P is today's price, FV is the face value, y is the **yield to maturity** (the discount rate), and n is the number of periods to maturity. If a zero-coupon bond promises $1,000 in 5 years and the prevailing yield for 5-year instruments is 4%, then P = 1000 / (1.04)^5 = $821.93. The bond trades at a discount to face value; at maturity, the holder simply receives the $1,000 without any intermediate cash flows.

The **yield to maturity** here is both an input and an output depending on what you know. If you know the market price and the face value, you can solve for y: y = (FV/P)^(1/n) − 1. This is the bond's **implied discount rate** — the constant rate that, applied each period, turns today's price into the future face value. This inverted view of the formula is essential: bond yields are derived from prices, not set by the issuer. When market interest rates rise, existing bond prices must fall to offer competitive yields to new buyers, and this price-yield relationship is especially clean and transparent for zero-coupon bonds because there is only one cash flow to discount.

Zero-coupon bonds are particularly valuable as building blocks in fixed income analysis. Any coupon bond can be decomposed into a bundle of zero-coupon bonds — each coupon payment is a small zero-coupon bond, and the final principal payment is a larger one. This decomposition underpins the concept of the **spot rate curve** (also called the zero curve or term structure): the collection of yields implied by zero-coupon bonds of different maturities. Since each maturity has exactly one cash flow, each point on the spot rate curve is identified cleanly, without the coupon reinvestment complications that muddy coupon bond yields. When you go on to study the term structure of interest rates, zero-coupon bond prices are the raw material from which all other fixed-income relationships are built.
