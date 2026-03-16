---
id: maximal-prime-ideals
title: Maximal and Prime Ideals
domain: mathematics
course: abstract-algebra
prerequisites:
- id: subrings-ideals
  type: hard
builds-toward:
- field-definition-examples
tags:
- maximal-ideal
- prime-ideal
- quotient-structure
stage: advanced
status: draft
---

# Maximal and Prime Ideals

## Core Idea
A maximal ideal M of a ring R is an ideal properly contained in R such that no ideal properly contains M. An ideal P is prime if ab ∈ P implies a ∈ P or b ∈ P. In a commutative ring with unity, R/M is a field iff M is maximal, and R/P is an integral domain iff P is prime.

## Explainer

You know about ideals from your prerequisite: an ideal I of a ring R is a subset closed under addition and under multiplication by any element of R. Ideals are the "normal subgroups" of rings — the right building blocks for forming quotient rings R/I, where elements are cosets a + I and arithmetic is done modulo I. The question this topic asks is: what algebraic structure does R/I inherit from R, and what does that structure tell you about I itself?

The answer comes in two levels. An ideal P is called **prime** if whenever a product ab lands in P, at least one of a or b must already be in P. This is a direct generalization of the prime number property: in ℤ, the ideal (p) is prime exactly when p is a prime number — if p divides ab, then p divides a or p divides b. The algebraic payoff is that P is prime if and only if the quotient ring R/P has no **zero divisors**: nonzero elements whose product is zero. A commutative ring with unity and no zero divisors is called an **integral domain**, and the correspondence reads: R/P is an integral domain ⟺ P is prime.

An ideal M is **maximal** if no ideal sits strictly between M and all of R: there is no ideal J with M ⊊ J ⊊ R. Geometrically, M is as "large" as an ideal can be while remaining proper. The quotient R/M then has no nontrivial ideals of its own — and a commutative ring with unity and no nontrivial ideals is exactly a **field**. So R/M is a field ⟺ M is maximal.

The logical relationship between these: every maximal ideal is prime (because every field is an integral domain), but not every prime ideal is maximal. In ℤ, (0) is prime but not maximal, because (0) ⊊ (2) ⊊ ℤ. In a field itself, (0) is both prime and maximal. This hierarchy — fields inside integral domains inside general rings, mirrored by maximal ideals inside prime ideals inside general ideals — becomes the backbone of commutative algebra and algebraic geometry, where ideals correspond to algebraic varieties and the prime/maximal distinction tracks which varieties are irreducible versus which are points.
