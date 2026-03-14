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
