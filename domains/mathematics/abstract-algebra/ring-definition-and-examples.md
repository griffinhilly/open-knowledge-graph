---
id: ring-definition-and-examples
title: Ring Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: binary-operations-and-algebraic-structures
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- ring-homomorphisms
- subrings-and-ideals
- polynomial-rings
tags:
- rings
- definitions
- examples
stage: advanced
status: draft
---

# Ring Definition and Examples

## Core Idea
A ring has two operations (addition and multiplication) where (R, +) is an abelian group and multiplication is associative with distributivity over addition. Rings can be commutative or not, with or without unity. Examples: integers, polynomials, matrices, Gaussian integers.

## Explainer

You already understand **binary operations** and the **group axioms** — closure, associativity, identity, inverses. A ring extends this by adding a second operation and requiring the two operations to interact. Think of a ring as a structure where you can add, subtract (since additive inverses exist), and multiply — but division is not guaranteed. This makes rings a natural abstraction of the integers, where you can certainly add and multiply but dividing two integers rarely gives another integer.

Formally, a **ring** (R, +, ·) requires three things. First, (R, +) is an abelian group: addition is commutative and associative, there is an additive identity 0, and every element has an additive inverse. Second, multiplication is associative: (ab)c = a(bc) for all a, b, c. Third, multiplication distributes over addition from both sides: a(b+c) = ab + ac and (a+b)c = ac + bc. That's all. Multiplication does not need to be commutative, and there need not be a multiplicative identity (a "unity" or "1"). When commutativity holds we call it a **commutative ring**; when a unity exists we call it a **ring with unity** or **unital ring**.

The examples reveal the range of this definition. The integers Z are a commutative ring with unity — the prototypical example. Polynomials with real coefficients R[x] form another commutative ring with unity, where the unity is the constant polynomial 1. The set of 2×2 real matrices M₂(R) is a ring with unity (the identity matrix), but it is *not* commutative — matrix multiplication order matters. The **Gaussian integers** Z[i] = {a + bi : a, b ∈ Z} form a commutative ring with unity inside the complex numbers, which is useful for number theory. The set of even integers 2Z is a commutative ring *without* unity — there is no even number that acts as a multiplicative identity.

One subtlety: in a ring, 0·a = 0 for all a. This follows purely from the axioms without extra assumptions — it is a theorem, not an axiom. Proof: 0·a = (0+0)·a = 0·a + 0·a, and subtracting 0·a from both sides gives 0 = 0·a. This means the additive identity always "kills" multiplication, which distinguishes it from the multiplicative identity. A **zero divisor** is a nonzero element a where ab = 0 for some nonzero b — a phenomenon impossible in the integers but present in Z/6Z (where 2·3 = 0 mod 6). Rings without zero divisors are called **integral domains**, and they sit between general rings and fields in the hierarchy of algebraic structures you will study next.
