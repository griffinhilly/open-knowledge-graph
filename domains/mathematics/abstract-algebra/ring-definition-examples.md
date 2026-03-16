---
id: ring-definition-examples
title: Ring Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-definition-examples
  type: hard
builds-toward:
- ring-homomorphisms
- subrings-ideals
tags:
- ring
- distributivity
- commutativity
- unity
stage: advanced
status: draft
---

# Ring Definition and Examples

## Core Idea
A ring R is an abelian group under addition with a second binary operation (multiplication) that is associative and distributive over addition. A commutative ring has commutative multiplication; a ring with unity has a multiplicative identity. Rings generalize the arithmetic of integers and polynomials.

## Explainer

You already know what a group is: a set with one binary operation satisfying closure, associativity, an identity element, and inverses. A **ring** adds a second operation — multiplication — to an abelian group. Specifically, R is a ring if (R, +) is an abelian group, multiplication is associative, and multiplication distributes over addition: a(b + c) = ab + ac and (a + b)c = ac + bc. That's it. Notice what's missing: multiplication does not need to be commutative, and nonzero elements do not need multiplicative inverses. Rings are weaker than fields, which is exactly why there are so many more of them.

The integers Z are the canonical example. They form an abelian group under addition, multiplication is associative and distributes, and yet 2 has no multiplicative inverse in Z (1/2 is not an integer). So Z is a ring but not a field. The **ring with unity** condition simply asks for a multiplicative identity element, usually written 1. Z has this. The **commutative ring** condition asks that ab = ba for all a, b — again, Z satisfies this. Polynomial rings like Z[x] and R[x] are also commutative rings with unity, and they are the algebraic objects that formalize the familiar arithmetic of polynomials you've used for years.

Not all rings are commutative. The set of n×n matrices with real entries under matrix addition and multiplication is a ring, but multiplication is not commutative once n ≥ 2. Matrix rings are important examples of **noncommutative rings** and explain why the definition does not require commutativity. Another family: the integers modulo n, written Z/nZ, are commutative rings with unity. When n is prime, Z/nZ is actually a field — every nonzero element has an inverse. When n is composite, some nonzero elements lack inverses (for example, 2 has no inverse mod 4), so Z/4Z is a ring but not a field.

The **distributive law** is the structural spine of a ring — it is what makes the two operations talk to each other. Without distributivity, you just have two unrelated groups. With it, you get an algebra where familiar rules like (a + b)² = a² + 2ab + b² hold, ring homomorphisms preserve both operations simultaneously, and concepts like ideals (the analogue of normal subgroups) become well-defined. Every field is a ring, but most rings are not fields. The ring framework is broad enough to encompass integers, polynomials, matrices, and modular arithmetic all under a single set of axioms.
