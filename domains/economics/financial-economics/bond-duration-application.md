---
id: bond-duration-application
title: Duration and Interest Rate Sensitivity Applications
domain: economics
course: financial-economics
prerequisites:
- id: duration-and-convexity
  type: hard
- id: interest-rate-risk-management
  type: soft
- id: calculus
  type: hard
- id: derivatives-of-logarithmic-functions
  type: soft
builds-toward:
- bond-convexity-price-effects
tags:
- bonds
- duration
- risk-management
- interest-rate-sensitivity
stage: formal-systems
status: draft
---

# Duration and Interest Rate Sensitivity Applications

## Core Idea
Duration measures the average maturity-weighted time to receive a bond's cash flows and quantifies price sensitivity to yield changes. A bond's percentage price change approximately equals negative duration times the change in yield. This metric enables portfolio managers to construct immunization strategies and hedge interest rate risk.

## How It's Best Learned
Calculate duration for different bonds and compare their price changes when yields move by 1%. Verify the duration approximation against actual price changes to see when it breaks down.

## Common Misconceptions
- Confusing duration with maturity; duration is always less than maturity for coupon-paying bonds.
- Assuming duration is constant; it changes as yields and time to maturity change.
