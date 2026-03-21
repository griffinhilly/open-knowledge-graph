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

## Questions

```yaml
- question: "You discover that functor F: C → D is a right adjoint to some functor G: D → C. Without any further computation, what can you immediately conclude about F?"
  type: multiple-choice
  options:
    - "F preserves all colimits in C"
    - "F reflects all limits in D"
    - "F preserves all limits that exist in C — including products, equalizers, pullbacks, and terminal objects"
    - "F is full and faithful, so it both preserves and reflects all limits"
  answer: 2
  explanation: "The adjoint limit theorem states: right adjoints preserve all limits, left adjoints preserve all colimits. Knowing that F is a right adjoint immediately gives you preservation of every limit type — products, equalizers, pullbacks, terminal objects, and any others. This is one of the most powerful and frequently used results in category theory because it replaces case-by-case verification with a single structural property. Note the distinction: F preserves limits but need not reflect them; and being a right adjoint does not imply F is full or faithful."

- question: "A functor F: C → D reflects limits. A colleague shows you that F applied to a certain cone λ in C produces a limit cone in D. What can you conclude?"
  type: multiple-choice
  options:
    - "F also preserves limits, since reflecting implies preserving"
    - "The cone λ in C was already a limit cone before applying F"
    - "Every cone in C maps to a limit cone under F"
    - "F is a right adjoint, since reflection of limits is equivalent to being a right adjoint"
  answer: 1
  explanation: "Reflection of limits means: if F(λ) is a limit cone in D, then λ was a limit cone in C. This is the 'backward' direction — it lets you verify limits in C by checking their images in D. This is valuable when D has a more concrete or tractable structure (e.g., D = Set) where limits are easier to verify. Preservation (the forward direction) is independent: a functor can reflect without preserving, or preserve without reflecting. And reflection is not equivalent to being a right adjoint — right adjoints preserve limits, not necessarily reflect them."

- question: "The hom-functor Hom(A, −): C → Set preserves all limits that exist in C, as a consequence of the interaction between limits and universal properties."
  type: true-false
  answer: true
  explanation: "Hom(A, −) is a right adjoint (to the tensor product or co-product functor, depending on context), and right adjoints preserve all limits. More directly: a limit in C satisfies a universal property that interacts naturally with hom-sets. Formally, Hom(A, lim D) ≅ lim Hom(A, D(−)), meaning maps from A into a limit correspond to compatible families of maps from A into the diagram — exactly preserving the universal property. This fact is used constantly in homological algebra and sheaf theory."

- question: "A functor that preserves limits must also reflect them — preservation and reflection are equivalent properties."
  type: true-false
  answer: false
  explanation: "Preservation and reflection are logically independent. Preservation says: if λ is a limit cone in C, then F(λ) is a limit cone in D. Reflection says: if F(λ) is a limit cone in D, then λ was a limit cone in C. Neither implies the other. A functor can preserve without reflecting (e.g., a constant functor maps every cone to the same cone, which may happen to be a limit, but this tells you nothing about the original). A functor can reflect without preserving (certain faithful functors detect limits without creating them). The two properties are distinct tools serving different theoretical purposes."

- question: "State the fundamental adjoint limit theorem and explain why it is practically useful in category theory."
  type: short-answer
  answer: "Right adjoints preserve all limits; left adjoints preserve all colimits. This is practically useful because it replaces case-by-case verification with a single structural check: if you can show a functor is a right adjoint, you immediately know it preserves products, equalizers, pullbacks, terminal objects, and any other limits — without examining each limit type separately. Conversely, if you want a functor to preserve all colimits, you should make it a left adjoint. Adjoint pairs thus come with automatic limit/colimit guarantees, which is a major reason they are the central structural concept of category theory."
  explanation: "The theorem's utility is seen throughout mathematics. Forgetful functors from algebraic categories (groups, rings, modules) to Set are often right adjoints (to free functors), and this immediately explains why they preserve products and equalizers. Sheafification is a left adjoint, explaining why it preserves colimits. The base change functor in algebraic geometry is a right adjoint, and limit preservation is essential for its role in descent theory. Knowing the adjoint structure of a functor is often the fastest path to its limit-preservation properties."
```

## Explainer

You know that limits (products, equalizers, pullbacks, terminal objects) are defined by a universal property: a limit cone is the most efficient way to map into a diagram, characterized up to unique isomorphism. You also know that functors are structure-preserving maps between categories. The question of **preservation and reflection** asks: when you pass a construction through a functor, does the universal property survive?

A functor F: C → D **preserves a limit** if it maps limit cones to limit cones. Concretely: suppose D: J → C is a small diagram with a limit cone λ: Δ(L) ⇒ D in C (where L is the limit object and each λ_j: L → D(j) is a component of the cone). Then F preserves this limit if the cone F(λ): Δ(F(L)) ⇒ F∘D in D is also a limit cone — meaning F(L) with the maps F(λ_j) satisfies the same universal property in D. Preservation is a statement about what F does: it carries a particular universal construction to another universal construction. The classic example is that the **hom-functor** Hom(A, −): C → Set preserves all limits that exist in C — this is a consequence of limits and hom-sets interacting via the universal property, and it is one of the most-used facts in category theory.

A functor F **reflects a limit** if the converse holds: whenever F(λ) is a limit cone in D, the original λ was already a limit cone in C. Reflection is a statement about what you can deduce looking backward through F. If F reflects limits, you can verify that a construction in C is a limit by checking its image in D — a technique used when D has a more concrete or tractable structure. **Faithful** functors (those injective on hom-sets) often reflect limits, because they don't collapse the morphism information needed to detect universality.

The distinction between preservation and reflection matters for transferring theorems across categories. **Right adjoints preserve all limits** — this is the fundamental adjoint limit theorem and one of the most useful results in category theory. If F is a right adjoint, you can immediately conclude F preserves products, equalizers, pullbacks, and any other limits. Left adjoints dually preserve colimits. This is why adjoint functors are so powerful: they come with automatic limit-preservation guarantees, letting you compute limits in one category by passing to the other through the adjunction. Knowing whether a functor is an adjoint tells you, in one stroke, what kinds of constructions it respects — and preservation of limits is the primary currency of that respect.
