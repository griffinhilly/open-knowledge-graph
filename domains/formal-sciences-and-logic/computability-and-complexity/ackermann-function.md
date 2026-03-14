---
id: ackermann-function
title: Ackermann Function
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: primitive-recursive-functions
  type: hard
builds-toward:
- mu-recursive-functions
tags:
- computability
- recursive-functions
- fast-growing-hierarchy
stage: formal-systems
status: draft
---

# Ackermann Function

## Core Idea
The Ackermann function is a total computable function that grows faster than any primitive recursive function, proving that the primitive recursive functions do not exhaust all total computable functions. It is defined by double recursion: A(0, n) = n+1, A(m+1, 0) = A(m, 1), and A(m+1, n+1) = A(m, A(m+1, n)). Even small inputs produce astronomically large outputs — A(4, 2) exceeds 10^19,000. The function demonstrates that the primitive recursive hierarchy, despite containing all common arithmetic operations and bounded loops, is strictly contained within the total computable functions.

## How It's Best Learned
Compute A(m, n) by hand for small values (m = 0, 1, 2, 3 and small n) and recognize the pattern: A(1, n) = n+2, A(2, n) = 2n+3, A(3, n) = 2^(n+3) - 3. Then understand why A(4, n) involves towers of exponents. This concretely demonstrates growth beyond any fixed level of the primitive recursive hierarchy.

## Common Misconceptions
- The Ackermann function IS computable (a Turing machine can compute it) — it is just not primitive recursive. Being non-primitive-recursive does not mean uncomputable.
- There are multiple variants of the Ackermann function in the literature (Ackermann's original three-argument version, the two-argument Robinson/Peter version); the two-argument version is standard in computability courses.
