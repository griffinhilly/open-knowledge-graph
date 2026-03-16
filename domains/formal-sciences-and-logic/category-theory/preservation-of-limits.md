---
id: preservation-of-limits
title: Preservation and Reflection of Limits
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- adjoint-functors
- kan-extensions
tags:
- functor-properties
- limits
- universal-properties
stage: advanced
status: draft
---

# Preservation and Reflection of Limits

## Core Idea
A functor F: C → D preserves limits if whenever a diagram in C has a limit cone, F maps it to a limit cone in D. A functor reflects limits if F's image of a cone is a limit in D only when the original cone was a limit in C. Preservation relates to the idea that F respects 'universal' constructions.

## Explainer

You know that limits (products, equalizers, pullbacks, terminal objects) are defined by a universal property: a limit cone is the most efficient way to map into a diagram, characterized up to unique isomorphism. You also know that functors are structure-preserving maps between categories. The question of **preservation and reflection** asks: when you pass a construction through a functor, does the universal property survive?

A functor F: C → D **preserves a limit** if it maps limit cones to limit cones. Concretely: suppose D: J → C is a small diagram with a limit cone λ: Δ(L) ⇒ D in C (where L is the limit object and each λ_j: L → D(j) is a component of the cone). Then F preserves this limit if the cone F(λ): Δ(F(L)) ⇒ F∘D in D is also a limit cone — meaning F(L) with the maps F(λ_j) satisfies the same universal property in D. Preservation is a statement about what F does: it carries a particular universal construction to another universal construction. The classic example is that the **hom-functor** Hom(A, −): C → Set preserves all limits that exist in C — this is a consequence of limits and hom-sets interacting via the universal property, and it is one of the most-used facts in category theory.

A functor F **reflects a limit** if the converse holds: whenever F(λ) is a limit cone in D, the original λ was already a limit cone in C. Reflection is a statement about what you can deduce looking backward through F. If F reflects limits, you can verify that a construction in C is a limit by checking its image in D — a technique used when D has a more concrete or tractable structure. **Faithful** functors (those injective on hom-sets) often reflect limits, because they don't collapse the morphism information needed to detect universality.

The distinction between preservation and reflection matters for transferring theorems across categories. **Right adjoints preserve all limits** — this is the fundamental adjoint limit theorem and one of the most useful results in category theory. If F is a right adjoint, you can immediately conclude F preserves products, equalizers, pullbacks, and any other limits. Left adjoints dually preserve colimits. This is why adjoint functors are so powerful: they come with automatic limit-preservation guarantees, letting you compute limits in one category by passing to the other through the adjunction. Knowing whether a functor is an adjoint tells you, in one stroke, what kinds of constructions it respects — and preservation of limits is the primary currency of that respect.
