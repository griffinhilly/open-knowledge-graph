---
id: future-value-and-compounding
title: Future Value and Compounding
domain: economics
course: financial-economics
prerequisites:
- id: time-value-of-money
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: geometric-sequences-and-series
  type: soft
builds-toward:
- annuities-and-perpetuities
tags:
- future-value
- compounding
- interest
- growth
stage: formal-systems
status: validated
---

# Future Value and Compounding

## Core Idea
Future value (FV) measures how much a present sum will be worth after earning returns over time: FV = PV × (1+r)^t. Compounding means earning returns on previously earned returns, causing wealth to grow exponentially rather than linearly. More frequent compounding periods (monthly vs. annual) raise the effective annual yield; in the continuous limit, FV = PV × e^(rt). The power of compounding over long horizons is often dramatically underestimated by intuition calibrated to linear thinking.

## How It's Best Learned
Compare simple interest vs. compound interest over 30-year horizons to see the difference compounding makes. The Rule of 72 — divide 72 by the interest rate to approximate the doubling time — is a powerful shortcut for building intuition. Simulate different compounding frequencies in a spreadsheet.

## Common Misconceptions
- Daily vs. monthly compounding makes little practical difference compared to the effect of the interest rate itself — students overweight compounding frequency.
- Forgetting taxes and fees when projecting future wealth leads to significant over-optimism in retirement planning.
