---
id: absolute-convergence-rearrangement
title: Absolute Convergence and Rearrangement
domain: mathematics
course: real-analysis
prerequisites:
- id: series-convergence-rigorous
  type: hard
tags:
- absolute-convergence
- rearrangement
- conditional-convergence
stage: advanced
status: draft
---

# Absolute Convergence and Rearrangement

## Core Idea
A series ∑aₙ converges absolutely if ∑|aₙ| converges. Absolute convergence implies convergence, but not vice versa (∑(-1)ⁿ/n converges conditionally but not absolutely). A key theorem: absolutely convergent series remain convergent after any rearrangement (to the same sum), while conditionally convergent series can be rearranged to converge to any value or diverge entirely.

## How It's Best Learned
Compare 1 - 1/2 + 1/3 - 1/4 + ... (converges conditionally to ln 2) with its rearrangement 1 + 1/3 - 1/2 + 1/5 + 1/7 - 1/4 + ... (converges to 3ln 2/2). Show why ∑1/n converges absolutely only after grouping.

## Common Misconceptions
- Thinking conditional convergence means the series barely converges; ∑(-1)ⁿ/n is robustly conditionally convergent.
- Confusing rearrangement with reindexing; we're permuting terms, not reordering indices.
- Assuming rearrangement can only change the sum slightly; it can change it arbitrarily or destroy convergence.
