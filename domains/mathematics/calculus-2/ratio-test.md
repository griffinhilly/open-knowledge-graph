---
id: ratio-test
title: Ratio Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: geometric-series
    type: hard
  - id: sequences-convergence
    type: hard
builds-toward:
  - radius-and-interval-of-convergence
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, ratio-test]
stage: formal-systems
status: draft
---

# Ratio Test

## Core Idea
The Ratio Test examines L = lim(n->infinity) |a_(n+1)/a_n|. If L < 1, the series converges absolutely. If L > 1, the series diverges. If L = 1, the test is inconclusive. The ratio test is particularly effective for series involving factorials (n!) and exponentials (r^n), where the ratio of consecutive terms simplifies nicely. It is also the key tool for finding the radius of convergence of power series.

## How It's Best Learned
Apply to series with factorials and exponentials where the ratio simplifies. Compare with the geometric series (the ratio test essentially checks whether terms decrease geometrically in the limit). Practice recognizing when the test is inconclusive (p-series, for example) and switching to another test.

## Common Misconceptions
- Concluding convergence or divergence when L = 1 (the test is inconclusive).
- Computing the ratio incorrectly, especially with factorials ((n+1)! = (n+1)*n!).
- Applying the ratio test to series where it is inconclusive when a simpler test would work.
