---
id: field-definition-examples
title: Field Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: maximal-prime-ideals
  type: hard
builds-toward:
- field-extensions
- finite-fields
tags:
- field
- inverse
- division-ring
- characteristic
stage: advanced
status: draft
---

# Field Definition and Examples

## Core Idea
A field is a commutative ring with unity in which every nonzero element has a multiplicative inverse. Fields include the rationals Q, reals R, complexes C, and finite fields Z/pZ for prime p.

## Explainer

You already know from rings that addition and multiplication interact through the distributive law, and from groups that a single operation can have inverses. A **field** is what you get when both operations are as well-behaved as possible simultaneously: addition makes the elements an abelian group, and multiplication makes the *nonzero* elements an abelian group too. That second condition — every nonzero element has a multiplicative inverse — is the key upgrade from rings to fields, because it allows division.

Think about what you lose when you drop that condition. The integers Z form a ring, but 2 has no multiplicative inverse in Z (there is no integer n such that 2n = 1). This is why you cannot divide 1 by 2 and stay in Z. The rationals Q fix this: for every nonzero integer p/q, the inverse is q/p, which is also rational. The rationals are the smallest field containing the integers. The reals R and complexes C extend this further, adding geometric completeness and algebraic closure respectively.

Your prerequisite — **maximal and prime ideals** — connects directly. A commutative ring R is a field if and only if it has no proper nonzero ideals at all. This is because if every nonzero element is invertible, any ideal containing a nonzero element must contain 1 and therefore all of R. The quotient construction makes this operational: R/M is a field if and only if M is a maximal ideal. The example Z/pZ (integers mod a prime p) illustrates this: the ideal pZ is maximal because p is prime, so Z/pZ is a field — its elements {0, 1, 2, ..., p−1} all have multiplicative inverses mod p.

The **characteristic** of a field is the smallest positive integer n such that adding 1 to itself n times gives 0, or 0 if no such n exists. Fields like Q, R, and C have characteristic 0 — you can add 1 to itself forever without reaching 0. Finite fields Z/pZ have characteristic p, a prime. A key theorem: the characteristic of any field is either 0 or a prime. This follows immediately from the field axioms — if characteristic were composite, say n = ab, then (a·1)(b·1) = n·1 = 0, but in a field a product is zero only if a factor is zero, forcing a·1 = 0 or b·1 = 0, contradicting the minimality of n. The characteristic constraint shapes everything in the theory of field extensions that follows.
