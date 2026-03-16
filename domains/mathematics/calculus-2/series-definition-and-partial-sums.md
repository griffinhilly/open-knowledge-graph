---
id: series-definition-and-partial-sums
title: Series Definition and Partial Sums
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-convergence
    type: hard
builds-toward:
  - geometric-series
  - divergence-test
tags: [series, partial-sums, definition]
stage: formal-systems
status: validated
---

# Series Definition and Partial Sums

## Core Idea
An infinite series sum from n=1 to infinity of a_n is defined as the limit of its partial sums: S = lim(N->infinity) S_N where S_N = a_1 + a_2 + ... + a_N. If this limit exists and is finite, the series converges to S; otherwise, it diverges. The key insight is that an infinite sum is not computed by adding infinitely many terms, but by analyzing the trend of finite partial sums.

## How It's Best Learned
Compute partial sums for specific series (geometric, telescoping) and observe convergence or divergence. Graph S_N vs. N to visualize. Emphasize that convergence of the series is a statement about the sequence of partial sums, connecting this topic back to sequence convergence.

## Common Misconceptions
- Believing you can add infinitely many terms directly (the series is the limit of partial sums).
- Confusing the terms a_n with the partial sums S_N.
- Assuming the partial sums always have a nice closed form (they usually do not).

## Explainer

An infinite series looks like a sum that goes on forever, but "adding infinitely many terms" is not a well-defined arithmetic operation — you cannot literally perform infinitely many additions. The crucial insight, which mirrors what you learned about sequences, is to turn the infinite process into a limit. Define the **partial sum** S_N = a₁ + a₂ + ⋯ + a_N — a perfectly ordinary finite sum you can compute — and then define the series as the limit of S_N as N → ∞. A series **converges** if this limit exists and is finite; otherwise it **diverges**.

This definition reduces the question of series convergence to sequence convergence, which you already understand. The series Σ aₙ converges to S if and only if the sequence {S_N} converges to S. This is not a semantic trick — it is a precise reduction of one concept to another. When you ask "does the series converge?", you are really asking "does the sequence of partial sums converge?" That question has all the tools of sequence analysis behind it.

A worked example builds the intuition. Consider Σ (1/2)ⁿ = 1/2 + 1/4 + 1/8 + ⋯. The partial sums are S₁ = 1/2, S₂ = 3/4, S₃ = 7/8, and in general S_N = 1 − 1/2^N. As N → ∞, S_N → 1, so the series converges to 1. By contrast, the **harmonic series** Σ 1/n has partial sums that grow without bound — slowly, but unboundedly. The sequence {S_N} diverges, so the series diverges even though the individual terms 1/n go to zero. This example exposes the key asymmetry: terms going to zero is necessary for convergence but not sufficient.

The distinction between the **terms aₙ** and the **partial sums S_N** is the source of most confusion in this topic. Each aₙ is a single term; S_N is the accumulated total of the first N terms. A series converges when the partial sums settle toward a finite limit, which requires the terms to shrink fast enough that their cumulative contribution remains bounded. The convergence tests you will study next — geometric series, the divergence test, comparison, ratio, and integral tests — are all different ways of diagnosing whether the partial sums have that settling behavior.
