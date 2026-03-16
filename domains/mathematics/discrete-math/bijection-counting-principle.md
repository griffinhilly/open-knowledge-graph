---
id: bijection-counting-principle
title: Bijection Principle in Counting
domain: mathematics
course: discrete-math
prerequisites:
- id: double-counting-principle
  type: hard
- id: injective-surjective-bijective
  type: hard
tags:
- combinatorics
- counting
- bijections
stage: formal-systems
status: draft
---

# Bijection Principle in Counting

## Core Idea
The bijection principle states that if a bijection exists between two sets, they have the same cardinality. In combinatorics, proving a bijection between two sets immediately proves they are equinumerous, often revealing why two counting expressions are equal.

## Explainer

You already know from injective-surjective-bijective that a bijection is a one-to-one, onto function between two sets — every element of one set pairs with exactly one element of the other, with no leftovers on either side. The bijection principle in counting takes this structural idea and turns it into a proof technique: if you can exhibit a bijection between two sets, you have proven they have the same size, without needing to count either one directly.

The key insight is that cardinality is preserved by bijections. Think of pairing socks: if every left sock has exactly one right-sock partner and no right sock is unpaired, you have the same number of left and right socks — without counting. The same logic applies to any two finite sets: a bijection is sufficient proof of equal size. This is exactly what your prerequisite on injective and surjective functions was building toward.

The technique becomes powerful when two counting formulas look different but should give the same number. Consider: why does C(n,k) = C(n, n−k)? You could prove this algebraically, but the bijection proof is more illuminating. Every k-element subset of {1,...,n} corresponds to exactly one (n−k)-element subset — its complement. This mapping is a bijection, so the two collections of subsets have the same size. No algebra needed. The bijection **reveals** why the identity holds, not just that it holds.

From double-counting, you know that counting one set two ways yields an algebraic identity. Bijection is a related but distinct technique: instead of counting one set two different ways, you define a correspondence between two *different* sets and prove they are equinumerous. The double-counting principle often produces equations between sums; the bijection principle often produces combinatorial identities. Both rest on the same underlying idea — you understand a set deeply when you understand its relationship to another, better-understood set. Over time, spotting "this set of objects is secretly in bijection with that simpler one" becomes one of the most elegant moves in combinatorics.
