---
id: continued-fractions
title: Continued Fractions
domain: mathematics
course: number-theory
prerequisites:
- id: euclidean-algorithm
  type: hard
builds-toward:
- best-rational-approximations
- pell-equation
tags:
- continued-fractions
- approximations
- diophantine
stage: advanced
status: draft
---

# Continued Fractions

## Core Idea
Every real number has a unique continued fraction expansion [a_0; a_1, a_2, ...]. For rationals, the expansion terminates in O(log n) steps (connected to the Euclidean algorithm); for irrationals like √D, periodic patterns encode Diophantine information crucial for solving Pell equations and approximation problems.
