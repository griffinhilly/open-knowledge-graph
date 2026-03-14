---
id: absolute-vs-conditional-convergence
title: Absolute vs. Conditional Convergence
domain: mathematics
course: calculus-2
prerequisites:
- id: alternating-series-test
  type: hard
- id: comparison-test
  type: hard
- id: limit-comparison-test
  type: soft
- id: ratio-test
  type: soft
builds-toward:
- power-series
tags:
- series
- convergence
- absolute
- conditional
stage: formal-systems
status: validated
---
# Absolute vs. Conditional Convergence

## Core Idea
A series converges absolutely if the series of absolute values sum of |a_n| converges. It converges conditionally if it converges but does not converge absolutely. Absolute convergence implies convergence (but not vice versa). The distinction matters because absolutely convergent series can be rearranged without changing the sum, while conditionally convergent series can be rearranged to converge to any value (Riemann Rearrangement Theorem). Absolute convergence is the stronger, more desirable property.

## How It's Best Learned
Test for absolute convergence first (apply convergence tests to |a_n|). If the absolute value series diverges but the original series converges (typically via alternating series test), the convergence is conditional. Classic example: the alternating harmonic series converges conditionally.

## Common Misconceptions
- Believing conditional convergence and absolute convergence are the same thing.
- Not checking absolute convergence before declaring conditional convergence.
- Assuming rearranging terms cannot change the sum of a series.
