---
id: combinations-selections-discrete
title: Combinations and Selections
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-arrangements-discrete
  type: hard
- id: combinations
  type: hard
builds-toward:
- binomial-theorem-discrete
- inclusion-exclusion-advanced
tags:
- combinations
- selections
- C(n,r)
- unordered
stage: formal-systems
status: draft
---

# Combinations and Selections

## Core Idea
A combination is an unordered selection of objects. The number of r-combinations of n objects is C(n, r) = n!/(r!(n−r)!). When order doesn't matter—choosing committee members or lottery numbers—combinations apply.

## How It's Best Learned
Derive C(n, r) = P(n, r)/r! by recognizing that r! orderings of the same r objects must be divided out. Use the identity C(n, r) = C(n, n−r) to simplify.

## Common Misconceptions
Combinations count unordered sets; {A, B} and {B, A} are the same. Confusing combinations with permutations is the most common error in counting problems.
