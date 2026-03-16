---
id: group-isomorphisms
title: Group Isomorphisms
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-homomorphisms
  type: hard
builds-toward:
- cosets-lagrange-theorem
- first-isomorphism-theorem-groups
tags:
- isomorphisms
- bijective
- structure-preserving
- equivalent-groups
stage: advanced
status: draft
---

# Group Isomorphisms

## Core Idea
A group isomorphism is a bijective homomorphism. Two groups are isomorphic if there exists an isomorphism between them, meaning they have identical algebraic structure. Isomorphic groups differ only in notation.

## Explainer

You've already studied **homomorphisms** — maps φ: G → H that preserve the group operation, meaning φ(ab) = φ(a)φ(b). A homomorphism is the group-theoretic notion of "structure-preserving map." An **isomorphism** is a homomorphism with one additional requirement: bijectivity. The map must be one-to-one (injective) and onto (surjective). When such a map exists, we write G ≅ H and say the groups are *isomorphic*.

The intuition is that isomorphic groups are the same group wearing different clothes. Consider the group of integers under addition modulo 4 ({0,1,2,3} with operation +₄) and the group of rotations of a square ({0°, 90°, 180°, 270°} with operation "followed by"). Both have order 4, both have a generator that cycles through all elements, and the structure of their Cayley tables is identical. The map φ(k) = rotation by 90k degrees is a bijective homomorphism — an isomorphism. In abstract algebra, these two groups are indistinguishable; any theorem proved for one holds for the other.

Not all groups of the same order are isomorphic. Consider two groups of order 4: **ℤ₄** (cyclic, with a single generator of order 4) and the **Klein four-group V₄** (where every non-identity element has order 2, i.e., a² = e for all a). These have the same size but different algebraic structure: ℤ₄ has an element of order 4, V₄ does not. No bijection between them can preserve the group operation, so V₄ ≇ ℤ₄. To prove two groups are *not* isomorphic, you find a structural invariant — a property preserved by any isomorphism, like the order of elements, the number of elements of each order, or commutativity — that differs between the two groups.

Isomorphisms are the equivalence relation of group theory: they tell you when two groups are "the same" at the level of abstract structure. The **First Isomorphism Theorem**, which you'll study next, makes this even more powerful by connecting isomorphisms to quotient groups — showing that every homomorphism "factors through" an isomorphism in a canonical way.
