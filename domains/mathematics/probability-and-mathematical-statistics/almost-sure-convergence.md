---
id: almost-sure-convergence
title: Almost Sure Convergence
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: soft
- id: borel-cantelli-lemmas
  type: hard
builds-toward:
- relationships-modes-convergence
- strong-law-of-large-numbers
tags:
- convergence
- almost-sure
- limit-theorems
stage: advanced
status: draft
---

# Almost Sure Convergence

## Core Idea
A sequence {Xₙ} converges almost surely to X if P(lim_{n→∞} Xₙ = X) = 1, equivalently P({ω: lim_{n→∞} Xₙ(ω) = X(ω)}) = 1. This is the strongest form of convergence, meaning the pointwise limit exists for all ω except on a set of probability zero.
