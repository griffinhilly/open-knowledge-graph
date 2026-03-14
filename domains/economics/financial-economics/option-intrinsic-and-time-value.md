---
id: option-intrinsic-and-time-value
title: Option Intrinsic Value and Time Value
domain: economics
course: financial-economics
prerequisites:
- id: call-and-put-options-mechanics
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- option-greeks-delta-gamma-vega-theta
tags:
- options
- valuation
- option-pricing
stage: formal-systems
status: draft
---

# Option Intrinsic Value and Time Value

## Core Idea
Option price = intrinsic value + time value. Intrinsic value is immediate exercise payoff (never negative for European options; can be negative for an option to sell if out-of-the-money). Time value erodes as expiration approaches and reflects uncertainty; deep out-of-the-money options are mostly time value.

## How It's Best Learned
Track how option prices behave as underlying price and time-to-expiration change. Observe that time decay accelerates near expiration, especially for out-of-the-money options.
