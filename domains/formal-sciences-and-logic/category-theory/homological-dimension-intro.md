---
id: homological-dimension-intro
title: Homological Dimension in Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-structure-properties
  type: hard
- id: projective-objects
  type: soft
- id: injective-objects
  type: soft
builds-toward:
- derived-functors
- homology-and-cohomology
tags:
- homological-algebra
- dimension
- resolutions
stage: advanced
status: draft
---

# Homological Dimension in Categories

## Core Idea
Homological dimension measures the 'length' of projective or injective resolutions. The projective dimension of an object is the shortest length of a projective resolution; global dimension is the supremum of projective dimensions of all objects. Low homological dimension implies strong homological properties, making it a fundamental invariant in ring theory and module categories.

## Explainer

From your study of abelian categories and projective objects, you know that projective objects are those with the lifting property — morphisms out of them lift through epimorphisms. A **projective resolution** of an object M is an exact sequence ··· → P₂ → P₁ → P₀ → M → 0 where each Pᵢ is projective. Every object in a sufficiently nice abelian category (like R-modules for a ring R) admits such a resolution: start with a surjection P₀ → M from a projective, take the kernel K₀, surject from a projective P₁ onto K₀, take that kernel, and continue. The resolution exists; what varies is how long it needs to be.

The **projective dimension** pd(M) is the length of the shortest projective resolution — the smallest n such that you can arrange 0 → Pₙ → ··· → P₀ → M → 0 exactly. If M is itself projective, pd(M) = 0: the trivial resolution 0 → M → M → 0 works. If M is not projective but admits a two-step resolution 0 → P₁ → P₀ → M → 0, then pd(M) = 1. Think of pd(M) as measuring how many "correction steps" are needed to build M from projective building blocks — the higher the dimension, the more non-projective obstruction M carries. This is analogous to measuring the distance from M to the class of projective objects.

The **global dimension** gl.dim(R) of a ring is the supremum of projective dimensions of all R-modules. It reads as: "how complicated, in the worst case, can a module over R be?" If gl.dim(R) = 0, every R-module is projective — this characterizes **semisimple rings** (like direct products of matrix algebras). If gl.dim(R) = 1, every submodule of a projective is projective — this characterizes **hereditary rings**, which include principal ideal domains like ℤ and polynomial rings in one variable over a field. The celebrated **Serre–Auslander–Buchsbaum theorem** shows that a Noetherian local ring R is **regular** (geometrically: its spectrum is a smooth variety) if and only if R has finite global dimension. Homological dimension is not bookkeeping — it is an algebraic encoding of geometric smoothness.

The dual concept, **injective dimension** id(M), measures the length of the shortest injective resolution. A module can have finite projective dimension but infinite injective dimension, or vice versa. Both invariants appear when you compute the derived functors Ext and Tor: Extⁿ(M, N) vanishes for n > pd(M) and for n > id(N). This means homological dimension governs precisely when long exact sequences of Ext groups truncate — a fact that makes it the key organizational principle for the derived functor machinery you will study next.
