---
id: annuities-and-perpetuities
title: Annuities and Perpetuities
domain: economics
course: financial-economics
prerequisites:
- id: present-value-and-discounting
  type: hard
- id: geometric-series
  type: soft
- id: geometric-sequences-and-series
  type: soft
- id: future-value-and-compounding
  type: soft
builds-toward:
- bond-pricing
- dividend-discount-model
tags:
- annuity
- perpetuity
- cash-flow-streams
- gordon-growth
stage: abstract-reasoning
status: validated
---
# Annuities and Perpetuities

## Core Idea
An annuity is a series of equal cash flows paid at regular intervals; its present value is PV = C × [1 − (1+r)^(−t)] / r. A perpetuity pays equal cash flows forever and has the elegantly simple formula PV = C/r, derived by taking the annuity formula to the limit as t → ∞. A growing perpetuity, where payments grow at constant rate g, gives PV = C/(r−g), the foundation of the Gordon Growth Model for equity valuation. These formulas are derived by summing geometric series and appear throughout finance in pricing bonds, mortgages, preferred stock, and endowments.

## How It's Best Learned
Derive the perpetuity formula as the limit of the annuity formula to see where C/r comes from. Apply annuity formulas to compute monthly mortgage payments and retirement income streams. Recognize the growing perpetuity as a direct precursor to dividend discount stock valuation.

## Common Misconceptions
- Perpetuities seem impractical but government consols and preferred stocks closely approximate them in real markets.
- The growing perpetuity formula breaks down entirely when g ≥ r, producing negative or infinite values — students must check this condition before applying.
