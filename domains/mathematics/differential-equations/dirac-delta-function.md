---
id: dirac-delta-function
title: Dirac Delta Function and Impulse Response
domain: mathematics
course: differential-equations
prerequisites:
- id: convolution-theorem
  type: hard
builds-toward:
- systems-first-order-linear-odes
tags:
- delta-function
- impulse
- distribution
stage: advanced
status: draft
---

# Dirac Delta Function and Impulse Response

## Core Idea
The Dirac delta δ(t) models an instantaneous impulse: zero everywhere except at t = 0, with ∫_{-∞}^∞ δ(t)dt = 1. Its Laplace transform is L[δ(t)] = 1. The impulse response of a system is the solution when forced by δ(t), and convolution with the impulse response gives the response to any input. Deltas are essential for modeling sudden shocks and discontinuous inputs.
