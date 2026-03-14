---
id: limit-comparison-test
title: Limit Comparison Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: comparison-test
    type: hard
builds-toward:
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, limit-comparison]
stage: formal-systems
status: validated
---

# Limit Comparison Test

## Core Idea
The Limit Comparison Test states: if a_n > 0 and b_n > 0, and lim(n->infinity) a_n/b_n = c where 0 < c < infinity, then sum of a_n and sum of b_n either both converge or both diverge. This test is more flexible than direct comparison because you only need to show the terms are proportional in the limit, not that one is always larger than the other.

## How It's Best Learned
Compare unfamiliar series with p-series or geometric series by computing the limit of their ratio. Practice identifying the dominant term in a_n to guess the right comparison series. Emphasize that the limit must be a positive finite number for the conclusion to hold.

## Common Misconceptions
- Drawing a conclusion when the limit is 0 or infinity (these cases require separate analysis).
- Choosing a comparison series b_n that does not match the growth rate of a_n.
- Confusing the limit comparison test with L'Hopital's rule (they serve different purposes, though L'Hopital's rule may be used within the limit comparison test).
