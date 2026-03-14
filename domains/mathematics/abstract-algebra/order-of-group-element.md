---
id: order-of-group-element
title: Order of a Group Element
domain: mathematics
course: abstract-algebra
prerequisites:
- id: cyclic-groups
  type: hard
builds-toward:
- cosets-and-lagrange-theorem
- sylow-theorems
tags:
- order
- elements
- properties
stage: advanced
status: draft
---

# Order of a Group Element

## Core Idea
The order of element a is the smallest positive integer n with a^n = e. Infinite order elements exist in infinite groups. The order divides |G| for finite groups; elements of order n generate cyclic subgroups of order n.

## How It's Best Learned
Compute orders in Z/nZ and symmetric groups. Verify that the set {e, a, a^2, ..., a^{n-1}} forms a cyclic subgroup of order n.

## Common Misconceptions
- Confusing the order of an element with the order of the group containing it.
- Assuming the order is always positive; we define it only for finite orders.
