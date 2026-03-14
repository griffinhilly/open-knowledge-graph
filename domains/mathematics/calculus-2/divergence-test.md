---
id: divergence-test
title: Divergence Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-convergence
    type: hard
  - id: series-definition-and-partial-sums
    type: hard
builds-toward:
  - integral-test
  - comparison-test
tags: [series, convergence-tests, divergence]
stage: formal-systems
status: validated
---

# Divergence Test

## Core Idea
The Divergence Test (nth-term test) states: if lim(n->infinity) a_n is not zero (or does not exist), then the series sum of a_n diverges. This is the first and simplest convergence test. However, it is one-directional: if a_n -> 0, the test is inconclusive (the series may converge or diverge). The harmonic series is the classic example of a_n -> 0 but the series diverging.

## How It's Best Learned
Apply as the first check for any series: if the terms do not approach zero, stop immediately and declare divergence. Practice with series like sum of n/(2n + 1), sum of (-1)^n, sum of cos(n). Emphasize the critical limitation: the converse is false.

## Common Misconceptions
- Concluding convergence because a_n -> 0 (the test cannot prove convergence, only divergence).
- Skipping this test and jumping to more complex tests when a simple limit would show divergence.
- Confusing this test with the comparison test or limit comparison test.
