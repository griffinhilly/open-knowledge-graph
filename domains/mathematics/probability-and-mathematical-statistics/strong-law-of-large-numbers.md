---
id: strong-law-of-large-numbers
title: Strong Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: almost-sure-convergence
  type: hard
- id: borel-cantelli-lemmas
  type: hard
builds-toward:
- markov-chains-convergence
- bayesian-inference-foundations
tags:
- limit-theorems
- slln
- sample-paths
stage: abstract-reasoning
status: draft
---

# Strong Law of Large Numbers

## Core Idea
If X_1, X_2, ... are i.i.d. with E[X_i] = μ, then (X_1 + ... + X_n)/n → μ almost surely. This is convergence of sample paths themselves, stronger than the weak law. The proof uses Kronecker's lemma; convergence is nearly certain, not merely probable.
