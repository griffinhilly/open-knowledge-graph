---
id: imaginary-elements-extension
title: Imaginary Elements and Quotient Sorts
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: definability-and-algebraic-applications
  type: soft
builds-toward:
- strongly-minimal-and-geometry
- o-minimality-and-tame-geometry
tags:
- imaginaries
- quotient-structures
- extensions
stage: advanced
status: draft
---

# Imaginary Elements and Quotient Sorts

## Core Idea
Imaginary elements are equivalence classes of tuples under definable equivalence relations. The imaginary extension M^eq of a model M adds all such quotient objects as new sorts, creating a richer structure. Imaginary elements capture definable structure that real elements cannot represent and are essential for category-theoretic properties of model theory.

## Explainer

From your study of structures and formal languages, you know that a model M is a domain of elements together with interpretations of the signature. A **definable set** is a subset of M^n picked out by a first-order formula — it is part of the structure's "visible" geometry. Now consider a definable equivalence relation E on M^n: a formula E(x⃗, y⃗) such that every model satisfies reflexivity, symmetry, and transitivity. The equivalence classes [a⃗]_E are natural mathematical objects — think of the cosets of a definable subgroup, or the orbits under a definable group action. The problem is that these equivalence classes are not elements of M; they are *sets* of elements. This gap between what the structure can define and what it can name is the motivation for imaginary elements.

An **imaginary element** is an equivalence class [a⃗]_E where E is a definable equivalence relation. The **imaginary extension** M^{eq} of M is a richer multi-sorted structure that adds, for each definable equivalence relation E on each Cartesian power M^n, a new sort whose elements are the E-classes of n-tuples. The original elements of M are called **real elements** and form one of the sorts of M^{eq}. There is also a canonical surjection from each sort of n-tuples onto the corresponding quotient sort, which is itself definable in M^{eq}.

Why bother? In many situations, the most natural "points" are not elements of the base structure but quotient objects. In the theory of algebraically closed fields, the coset space G/H (where H is a definable subgroup of a definable group G) is a natural object of study, but its elements are cosets, not field elements. By passing to M^{eq}, these cosets become genuine elements and can be directly quantified over, named by parameters, and handled by the model-theoretic machinery (types, definability, independence). Without imaginaries, one must constantly work around this gap with awkward coding tricks.

The central technical result is that well-behaved theories (specifically, those that **eliminate imaginaries**) have the property that every imaginary element is interdefinable with a real tuple — the new sorts add no genuinely new information, and the quotient structure is already "visible" in the original model. Strongly minimal theories and algebraically closed fields eliminate imaginaries, which is a key reason these theories have such clean geometric structure (the subject of strongly minimal sets and their geometries). Theories that fail to eliminate imaginaries have definable structure that cannot be reduced to real elements, indicating a richer and more complex geometry of types.

