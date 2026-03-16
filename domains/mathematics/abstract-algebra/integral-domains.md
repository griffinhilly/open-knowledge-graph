---
id: integral-domains
title: Integral Domains
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-rings
  type: hard
builds-toward:
- principal-ideal-domains
- unique-factorization-domains
tags:
- integral-domain
- no-zero-divisors
- cancellation
stage: advanced
status: draft
---

# Integral Domains

## Core Idea
An integral domain is a commutative ring with unity in which there are no zero divisors: ab = 0 implies a = 0 or b = 0. Integral domains are the natural setting for factorization and divisibility.

## Explainer

From your work with the first isomorphism theorem for rings, you know that rings are algebraic structures with addition and multiplication satisfying specific axioms — but multiplication need not be commutative, need not have an identity, and products of nonzero elements can equal zero. An integral domain imposes three clarifying conditions: the ring is commutative, it has a multiplicative identity (unity), and it has **no zero divisors**.

A **zero divisor** is a nonzero element a such that ab = 0 for some nonzero b. The integers ℤ have no zero divisors — a fact so familiar it seems obvious. But consider ℤ/6ℤ (integers mod 6): here 2 × 3 = 6 ≡ 0, yet both 2 and 3 are nonzero elements of ℤ/6ℤ. So ℤ/6ℤ is *not* an integral domain. The problem is that 6 is composite; in contrast, ℤ/pℤ for any prime p has no zero divisors and is actually a field.

The no-zero-divisors condition is equivalent to the **cancellation law**: if ac = bc and c ≠ 0, then a = b. Proof: ac = bc means ac − bc = 0, i.e., (a − b)c = 0. Since c ≠ 0 and there are no zero divisors, a − b = 0, so a = b. This cancellation is what makes divisibility arguments work correctly — you can cancel common factors without ambiguity. In ℤ/6ℤ, the cancellation law fails: 2·1 ≡ 2·4 (mod 6), but 1 ≠ 4.

The hierarchy of ring types is worth fixing in your mind: every **field** is an integral domain (nonzero elements have inverses, preventing zero divisors), but not every integral domain is a field (ℤ is the canonical non-field domain). Integral domains sit between general commutative rings and fields, and they are precisely the setting where factorization, divisibility, GCDs, and primality all behave the way you expect from the integers. The concepts of "prime element" and "irreducible element" — which coincide in ℤ but can diverge in other rings — are both defined within integral domains, and studying when they agree leads directly to unique factorization domains.
