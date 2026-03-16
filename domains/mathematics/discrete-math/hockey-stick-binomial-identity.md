---
id: hockey-stick-binomial-identity
title: Hockey Stick Identity
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
- id: double-counting-principle
  type: soft
tags:
- combinatorics
- binomial-coefficients
- identities
stage: formal-systems
status: draft
---

# Hockey Stick Identity

## Core Idea
The hockey stick identity (also called Pascal's identity summed) states Σ C(n+i, i) = C(n+r+1, r) for non-negative integers. It gets its name from the shape traced in Pascal's triangle and is proven using combinatorial arguments or induction.

## Explainer

From your work with **binomial coefficients**, you know that C(n, k) counts the number of ways to choose k items from n, and that Pascal's triangle encodes these values with each entry equal to the sum of the two above it. The **Hockey Stick Identity** reveals a different pattern: add up a diagonal of entries in Pascal's triangle, and you get the value just one step below the bottom of that diagonal. Specifically: C(r, r) + C(r+1, r) + C(r+2, r) + ⋯ + C(n, r) = C(n+1, r+1). If you trace these cells in Pascal's triangle, the summed entries form the straight shaft of a hockey stick, and the result is the curved blade at the bottom — hence the name.

The cleanest proof uses the **double-counting principle** from your prerequisites. Ask: how many ways can you choose r+1 items from the set {1, 2, 3, ..., n+1}? The answer is C(n+1, r+1). Now count the same thing a different way: condition on which element is the *largest* chosen. If the largest is r+1, the remaining r items come from {1, ..., r}, giving C(r, r) = 1 way. If the largest is r+2, the remaining r come from {1, ..., r+1}, giving C(r+1, r) ways. If the largest is r+k+1, you get C(r+k, r) ways. Summing over all possible largest elements from r+1 up to n+1 produces exactly the hockey stick sum — and both counts equal C(n+1, r+1). The identity follows.

Let's verify with r = 2: C(2,2) + C(3,2) + C(4,2) + C(5,2) = C(6,3). Computing: 1 + 3 + 6 + 10 = 20, and C(6,3) = 20. ✓ In Pascal's triangle these values — 1, 3, 6, 10 — appear along a diagonal moving down-right from the apex, and the answer 20 appears one step below and one step right of the last term, forming the blade. Marking these cells makes the hockey stick shape unmistakable.

The Hockey Stick Identity is a powerful shortcut whenever you need to sum a diagonal run of binomial coefficients — a computation that arises in probability distributions, combinatorial proofs, and algorithm analysis. More broadly, it exemplifies a central technique in combinatorics: identify the same quantity in two different ways, equate the counts, and the resulting equation is a non-trivial identity. Double counting doesn't just verify formulas — it reveals *why* they are true.
