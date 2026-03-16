---
id: borel-cantelli-lemmas
title: Borel-Cantelli Lemmas
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: independence-sigma-algebras
  type: hard
- id: probability-spaces-measure-theoretic
  type: hard
builds-toward:
- almost-sure-convergence
- strong-law-of-large-numbers
tags:
- limit-theorems
- convergence
- probability
stage: advanced
status: draft
---

# Borel-Cantelli Lemmas

## Core Idea
If {Aₙ} are events with Σ P(Aₙ) < ∞, then P(lim sup Aₙ) = 0 (first Borel-Cantelli lemma). Conversely, if {Aₙ} are independent with Σ P(Aₙ) = ∞, then P(lim sup Aₙ) = 1 (second Borel-Cantelli lemma). These lemmas control the tail behavior of event sequences and are crucial for proving almost sure convergence.
