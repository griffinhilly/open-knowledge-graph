---
id: term-structure-of-interest-rates
title: Term Structure of Interest Rates
domain: economics
course: financial-economics
prerequisites:
- id: yield-to-maturity
  type: hard
- id: inflation-and-price-level
  type: soft
- id: monetary-policy-tools
  type: soft
builds-toward:
- risk-and-return-tradeoff
tags:
- yield-curve
- term-structure
- spot-rates
- forward-rates
- expectations
stage: formal-systems
status: draft
---

# Term Structure of Interest Rates

## Core Idea
The term structure of interest rates describes how yields on otherwise equivalent bonds vary with maturity, visualized as the yield curve. Three main theories explain its shape: the pure expectations theory (long rates equal the geometric average of expected future short rates), the liquidity preference theory (investors demand a term premium for longer maturities), and the market segmentation theory (supply and demand in each maturity segment independently determine yields). An inverted yield curve — where short-term rates exceed long-term rates — has historically been a reliable recession predictor. Forward rates, derived from spot rates, represent market expectations of future short-term rates.

## How It's Best Learned
Plot the current Treasury yield curve and identify its shape: normal (upward-sloping), flat, or inverted. Study historical inversions before the 2001 and 2008 recessions. Bootstrap forward rates from spot rates to extract implied expectations about future policy rates.

## Common Misconceptions
- A normal, upward-sloping yield curve is not 'natural' or mathematically required — it reflects term premiums and growth expectations that can and do disappear.
- The yield curve is not the same as the discount rate schedule used in DCF analysis; risk-appropriate discount rates depend on project risk, not just maturity.
