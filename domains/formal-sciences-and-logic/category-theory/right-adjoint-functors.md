---
id: right-adjoint-functors
title: Right Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- adjoint-functors
- adjunction-as-hom-bijection
- limits-and-colimits
tags:
- adjunction
- functor-pairs
- universal-properties
stage: advanced
status: draft
---

# Right Adjoint Functors

## Core Idea
A functor R: D → C is a right adjoint if there exists L: C → D such that morphisms Lc → d in D correspond bijectively to morphisms c → Rd in C, naturally in both variables. Right adjoints preserve limits and characterize objects as 'universal targets' for maps from given sources. They are dual to left adjoints via opposite categories.

## Explainer

To understand right adjoints, start from the adjunction hom-bijection you know: an adjunction L ⊣ R gives a natural bijection Hom_D(Lc, d) ≅ Hom_C(c, Rd) for all objects c in C and d in D. Both functors are defined by this bijection, and each one is right or left depending on which side of the hom-set it appears on. **R is the right adjoint** because it appears on the right side of Hom_C(c, Rd) — it maps into the hom-set's target. Dually, L is the left adjoint because it appears on the left side of Hom_D(Lc, d). Every adjoint pair has exactly one left adjoint and one right adjoint; neither role is more "fundamental" — they define each other.

The most important structural property of right adjoints is that they **preserve limits**. Limits are the categorical generalization of products, equalizers, terminal objects, and pullbacks — all constructions that satisfy a "universal cone" property. If D has limits of a particular shape and R: D → C is a right adjoint, then R sends those limits to limits in C. Concretely: the right adjoint functor sends a product d₁ × d₂ in D to R(d₁ × d₂) ≅ R(d₁) × R(d₂) in C. It sends terminal objects to terminal objects, and pullbacks to pullbacks. You can verify this in familiar examples: the forgetful functor from groups to sets (which is a right adjoint to the free group functor) preserves the underlying set of a product group, which is the product of the underlying sets.

A right adjoint R: D → C characterizes Rd as the **best approximation** of d within C — the "universal target" for morphisms arriving from the image of L. The unit morphism η_c: c → R(Lc) and the counit morphism ε_d: L(Rd) → d encode the adjunction's universal properties. For a right adjoint, it is the counit that is primary: ε_d: L(Rd) → d expresses that d is the "universal element" that the left adjoint maps to. Any morphism Lc → d in D factors through Lc → L(Rd) → d, with the first map determined by the unique morphism c → Rd in C. Right adjoints arise naturally when you want to "freely add structure" on the left and "remember structure" on the right.

Duality gives the cleanest way to reason about right adjoints: R is a right adjoint in category C if and only if R^op: D^op → C^op (the opposite functor) is a left adjoint. Since left adjoints preserve colimits, right adjoints preserve limits. This duality is not merely formal — it is a template for generating theorems. If you prove something about left adjoints (they preserve initial objects, they send colimits to colimits), you immediately get the dual statement about right adjoints for free, by passing to opposite categories. The most economical way to think about a specific right adjoint is to identify its left adjoint partner and read off the bijection: once you know what the left adjoint does, the right adjoint is characterized as the functor that makes the hom-bijection work.
