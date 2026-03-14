---
id: root-test
title: Root Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-convergence
    type: hard
  - id: ratio-test
    type: soft
builds-toward:
  - radius-and-interval-of-convergence
tags: [series, convergence-tests, root-test]
stage: formal-systems
status: validated
---

# Root Test

## Core Idea
The Root Test examines L = lim(n->infinity) |a_n|^(1/n). If L < 1, the series converges absolutely. If L > 1, it diverges. If L = 1, inconclusive. The root test is most useful when a_n involves an nth power, such as (expression)^n, where the nth root simplifies cleanly. It is equivalent in power to the ratio test but sometimes easier to apply.

## How It's Best Learned
Apply to series of the form (f(n))^n. Compare with the ratio test on the same series to see which is more convenient. Practice computing nth roots using properties of limits and logarithms.

## Common Misconceptions
- Trying to use the root test on series with factorials (the ratio test is usually better for those).
- Confusing |a_n|^(1/n) with |a_n^(1/n)| (they are the same, but the computation can be confusing).
- Drawing a conclusion when L = 1.
