---
id: strong-law-of-large-numbers
title: Strong Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: weak-law-of-large-numbers
  type: soft
- id: almost-sure-convergence
  type: hard
- id: borel-cantelli-lemmas
  type: hard
builds-toward:
- central-limit-theorem-rigorous
tags:
- law-of-large-numbers
- limit-theorems
- probability
stage: abstract-reasoning
status: draft
---

# Strong Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. with finite mean μ, then Sₙ/n converges almost surely to μ: P(lim_{n→∞} Sₙ/n = μ) = 1. This is stronger than the weak law. The proof uses the Borel-Cantelli lemmas (for bounded random variables) or truncation arguments. The SLLN provides certainty (up to sets of probability zero) rather than just high probability.
