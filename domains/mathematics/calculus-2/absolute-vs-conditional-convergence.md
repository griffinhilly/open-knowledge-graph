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

## Explainer

You've tested series for convergence using the alternating series test, comparison test, and ratio test. Now comes a crucial refinement: not all convergence is equal. A series can converge for reasons that are sturdy and robust, or for reasons that are fragile and sign-dependent. **Absolute convergence** is the sturdy kind; **conditional convergence** is the fragile kind.

A series ∑aₙ converges **absolutely** if the series of absolute values ∑|aₙ| also converges. When you take absolute values, you strip away the sign information — any cancellation between positive and negative terms disappears. If the series still converges, it's doing so on pure magnitude, not cancellation. Absolute convergence is the stronger condition: if ∑|aₙ| converges, then ∑aₙ necessarily converges too. The implication goes one way only.

The prototypical example is the **alternating harmonic series** ∑(−1)ⁿ⁺¹/n = 1 − 1/2 + 1/3 − 1/4 + ···. The alternating series test confirms it converges (terms decrease to zero in absolute value). But ∑1/n is the harmonic series, which diverges. So ∑(−1)ⁿ⁺¹/n converges conditionally: it converges, but not absolutely. The convergence depends entirely on the alternating signs providing cancellation.

Here's why the distinction matters: the **Riemann Rearrangement Theorem** states that a conditionally convergent series can be rearranged to converge to any real number you choose — or even to diverge. You can achieve 0, π, or 10,000 by choosing the right permutation of the terms. This sounds paradoxical but follows from a precise property: the positive terms alone form a divergent series that grows without bound, and the negative terms alone form a divergent series that grows negatively without bound. By interleaving them strategically, you can hit any target. For absolutely convergent series, this phenomenon cannot happen — rearranging terms never changes the sum, which is why absolute convergence is the reliable, "bank-on-it" kind.

The practical algorithm: always test for absolute convergence first by applying your ratio test, comparison test, or other tools to ∑|aₙ|. If ∑|aₙ| converges, you're done — the series converges absolutely. If ∑|aₙ| diverges but ∑aₙ converges (typically confirmed by the alternating series test), then convergence is conditional. This two-step check fully classifies any convergent series.
