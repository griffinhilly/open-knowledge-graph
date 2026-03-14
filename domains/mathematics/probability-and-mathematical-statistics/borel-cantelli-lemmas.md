---
id: borel-cantelli-lemmas
title: The Borel-Cantelli Lemmas
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: independence-of-sigma-algebras
  type: hard
- id: series-convergence-rigorous
  type: soft
builds-toward:
- strong-law-of-large-numbers
tags:
- borel-cantelli
- independence
- tail-events
stage: abstract-reasoning
status: draft
---

# The Borel-Cantelli Lemmas

## Core Idea
The first Borel-Cantelli lemma: if Σ P(A_n) < ∞, then P(lim sup A_n) = 0 (only finitely many A_n occur). The second: if Σ P(A_n) = ∞ and the A_n are independent, then P(lim sup A_n) = 1 (infinitely many occur a.s.). Together they characterize behavior of infinite event sequences.
