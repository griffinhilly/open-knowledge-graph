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

## Explainer

From your study of primitive recursive functions, you know that every primitive recursive function is built up from zero, successor, and projection using composition and primitive recursion — a scheme where the recursion on n is bounded in advance by a fixed number of steps. Addition is defined by recursing on the second argument for n steps; multiplication by recursing on addition n times; exponentiation by recursing on multiplication n times. Each new operation uses the previous one as a primitive, forming a layered hierarchy. The key limitation: each primitive recursive definition only reaches one level higher than what it builds on.

The **Ackermann function** A(m, n) escapes this hierarchy by using *double recursion* — recursing simultaneously on both m and n. The base cases are simple: A(0, n) = n+1 is just the successor function. A(1, n) = n+2 is essentially repeated successor (addition). A(2, n) = 2n+3 corresponds to multiplication. A(3, n) = 2^(n+3) − 3 corresponds to exponentiation. So the first argument m selects a "level" of the arithmetic hierarchy: successor, addition, multiplication, exponentiation, tetration (tower of exponents), and beyond. Each new level is not just faster than the previous — it is a qualitatively new kind of growth.

Here is why A(4, 2) becomes incomprehensibly large: A(4, 2) = A(3, A(4, 1)) = A(3, A(3, A(4, 0))) = A(3, A(3, A(3, 1))). Each A(3, k) produces a tower of 2s of height k+3. So A(3, 1) = 2^4 − 3 = 13, A(3, 13) = 2^16 − 3 = 65533, A(3, 65533) is a tower of 65536 twos — and we are not done yet. The final result exceeds 10^19,000. The double recursion means that even computing A(m, 0) for large m requires unwinding a cascade of recursive calls that span all previous levels.

The significance for computability theory is precise: for every primitive recursive function f, there exists an N such that A(n, n) > f(n) for all n > N. This means A is not bounded by any fixed level of the primitive recursive hierarchy. No matter how many times you nest the primitive recursion scheme, Ackermann's growth escapes it. Yet A is still computable — a Turing machine can evaluate it using a stack to track the recursive calls. This separates two concepts you might have conflated: "having a nice closed-form recursion scheme" and "being computable at all." The Ackermann function lives in the gap between primitive recursive and the full class of total computable functions, proving that gap is nonempty.
