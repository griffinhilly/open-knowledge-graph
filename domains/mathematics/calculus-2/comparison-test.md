---
id: comparison-test
title: Comparison Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: geometric-series
    type: hard
  - id: p-series
    type: hard
builds-toward:
  - limit-comparison-test
tags: [series, convergence-tests, comparison]
stage: formal-systems
status: draft
---

# Comparison Test

## Core Idea
The Direct Comparison Test states: if 0 <= a_n <= b_n for all n, then if sum of b_n converges, sum of a_n converges (smaller than convergent = convergent); if sum of a_n diverges, sum of b_n diverges (bigger than divergent = divergent). The test requires finding a suitable comparison series, typically a geometric or p-series. It is the series analogue of the comparison test for improper integrals.

## How It's Best Learned
Build a library of benchmark series (geometric, p-series). Practice bounding series terms above by convergent benchmarks or below by divergent benchmarks. Emphasize that the comparison must go the right direction: you cannot conclude convergence by bounding above by a divergent series.

## Common Misconceptions
- Comparing in the wrong direction (bounding below by a convergent series proves nothing).
- Forgetting that both series must have non-negative terms.
- Choosing a comparison series that is not actually larger or smaller as needed.
