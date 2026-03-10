---
id: vector-spaces
title: Vector Spaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
builds-toward:
- subspaces
- inner-product-spaces
- null-space
- column-space
- span-of-vectors
tags:
- vector space
- axioms
- abstract
- closure
- field
stage: formal-systems
status: draft
---

# Vector Spaces

## Core Idea
A vector space is a set V equipped with operations of addition and scalar multiplication that satisfy ten axioms, including closure, associativity, commutativity of addition, existence of a zero vector and additive inverses, and distributivity. The key examples are Rⁿ, the space of polynomials, spaces of continuous functions, and spaces of matrices. This abstraction unifies many mathematical objects under one framework: any result proved for abstract vector spaces applies to all these examples simultaneously. The axioms are not arbitrary — they capture exactly what is needed to do linear algebra.

## How It's Best Learned
Verify the axioms for concrete examples (R², polynomials of degree ≤ 2, 2×2 matrices) to internalize what each axiom means. Practice disqualifying non-examples: show that the set of polynomials with positive leading coefficient fails to be a vector space by exhibiting a closure failure.

## Common Misconceptions
- Students expect vectors to look like arrows; in abstract vector spaces, 'vectors' may be functions, matrices, or polynomials.
- Failing even one axiom disqualifies a set from being a vector space — all ten must hold.
- The zero vector is not always the number 0; it is the additive identity of the particular space.
