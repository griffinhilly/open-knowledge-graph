---
id: interest-rate-term-structure
title: Term Structure of Interest Rates
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: interest-rates-and-loanable-funds
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- spot-forward-rate-relationships
- zero-coupon-bond-valuation
tags:
- bonds
- yield-curve
- interest-rates
- term-structure
stage: formal-systems
status: draft
---

# Term Structure of Interest Rates

## Core Idea
The term structure describes how interest rates vary across different maturity horizons. Yield curves can be upward-sloping, downward-sloping, or flat, reflecting market expectations about future rates, inflation, and risk premiums. The shape of the yield curve contains information about economic expectations and relative valuations of securities across maturities.

## How It's Best Learned
Start by plotting actual yield curve data from different time periods and learning to interpret the shapes. Then study the expectations hypothesis and liquidity preference theory to understand what drives different curve shapes.

## Common Misconceptions
- Assuming all interest rates move proportionally; different maturities respond differently to economic changes.
- Confusing the level of rates with the shape of the curve; they are independent phenomena.

## Explainer

From present value and discounting, you know that the value of a future cash flow depends critically on the interest rate used to discount it — and that different cash flows arrive at different times. The term structure formalizes the fact that there is not one interest rate but a whole schedule of rates, one for each maturity. A **yield curve** is a snapshot of this schedule: plot maturity on the x-axis and the annualized interest rate on the y-axis, and you get a curve that reveals how the market prices time across different horizons.

The most common shape is **upward-sloping**: longer maturities carry higher rates. There are two main reasons for this. First, the **expectations hypothesis** says that long-term rates reflect the market's average expected short-term rates over that horizon. If the Fed is expected to raise rates over the next two years, a 2-year rate will be higher than today's 1-year rate to compensate investors for rolling over at expected higher future rates. Second, the **liquidity premium theory** adds a risk premium on top: longer bonds have more interest rate sensitivity (duration), meaning their prices fluctuate more when rates move. Investors demand a premium to bear this extra risk, so long-term rates tend to exceed the pure expectations value.

An **inverted (downward-sloping)** yield curve is unusual and closely watched. It signals that short-term rates exceed long-term rates — typically because markets expect the central bank to cut rates in the future, usually in response to an anticipated recession. Historically, yield curve inversions have reliably preceded economic downturns with a lag of 6–18 months. This makes the yield curve shape a leading economic indicator: the market is aggregating millions of investors' expectations about future growth and monetary policy into a single observable curve.

The **flat yield curve** is a transitional shape, often seen when the economy is at an inflection point between expansion and contraction, or when the central bank has raised short rates sharply while long-term inflation expectations remain anchored. A key point from the misconceptions: the overall level of the curve (whether rates are high or low) is independent of its slope (upward, flat, or inverted). You could have a steeply upward-sloping curve at either 2% or 7% average rates. Understanding the term structure means reading both pieces of information — the level reflects current monetary conditions; the shape encodes market expectations about where rates are headed.
