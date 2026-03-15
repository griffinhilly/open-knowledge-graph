---
id: permutations-arrangements-discrete
title: Permutations and Arrangements
domain: mathematics
course: discrete-math
prerequisites:
- id: counting-fundamentals-discrete
  type: hard
- id: factorial
  type: hard
builds-toward:
- combinations-selections-discrete
- binomial-theorem-discrete
tags:
- permutations
- arrangements
- ordering
- P(n,r)
stage: formal-systems
status: draft
---

# Permutations and Arrangements

## Core Idea
A permutation is an ordered arrangement of distinct objects. The number of r-permutations of n objects is P(n, r) = n!/(n−r)!. When order matters—choosing a president, vice-president, and treasurer—permutations apply.

## How It's Best Learned
Use the multiplication principle to derive P(n, r): first position has n choices, second has n−1, etc. Practice distinguishing permutations (order matters) from combinations (order doesn't).

## Common Misconceptions
Permutations require distinct objects; if objects repeat, the formula changes. The formula P(n, r) assumes choosing without replacement and that order distinguishes arrangements.
