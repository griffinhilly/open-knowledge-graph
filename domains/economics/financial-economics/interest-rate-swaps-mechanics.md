---
id: interest-rate-swaps-mechanics
title: 'Interest Rate Swaps: Mechanics, Valuation, and Uses'
domain: economics
course: financial-economics
prerequisites:
- id: interest-rate-swap-contracts
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- currency-derivatives-and-hedging
tags:
- derivatives
- swaps
- valuation
- hedging
stage: formal-systems
status: draft
---

# Interest Rate Swaps: Mechanics, Valuation, and Uses

## Core Idea
Interest rate swaps exchange fixed-rate payments for floating-rate payments, allowing parties to convert debt structures without changing principal amounts. Swap values depend on the difference between forward LIBOR curves and fixed rates; they can be valued as a portfolio of forward contracts or as the net present value of cash flow differences. Swaps are central to modern financial engineering.

## How It's Best Learned
Value a plain-vanilla IRS by calculating the present value of fixed legs and floating legs separately, then verify the valuation matches market quotes.
