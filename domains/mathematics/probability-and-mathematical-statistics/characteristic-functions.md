---
id: characteristic-functions
title: Characteristic Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: complex-exponential-function
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- convergence-in-distribution
tags:
- characteristic-functions
- fourier-transforms
- uniqueness
stage: abstract-reasoning
status: draft
---

# Characteristic Functions

## Core Idea
The characteristic function φ_X(t) = E[e^{itX}] is the Fourier transform of the distribution. Unlike MGFs, it exists for all distributions and uniquely determines the distribution. The continuity theorem states φ_n → φ uniformly iff distributions converge weakly (in distribution). Essential for rigorous CLT proofs.
