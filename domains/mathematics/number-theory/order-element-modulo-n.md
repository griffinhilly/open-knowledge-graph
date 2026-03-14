---
id: order-element-modulo-n
title: Order of an Element Modulo n
domain: mathematics
course: number-theory
prerequisites:
- id: fermats-little-theorem
  type: hard
- id: congruence-properties
  type: hard
builds-toward:
- primitive-roots-cyclic-groups-mod-p
- discrete-logarithms
tags:
- order
- multiplicative-group
- exponents
stage: advanced
status: draft
---

# Order of an Element Modulo n

## Core Idea
The order of a mod n (with gcd(a,n) = 1) is the smallest positive k such that a^k ≡ 1 (mod n). The order divides φ(n) by Lagrange's theorem, and equals φ(n) precisely when a is a primitive root.
