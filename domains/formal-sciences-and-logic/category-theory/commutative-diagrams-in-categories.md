---
id: commutative-diagrams-in-categories
title: Commutative Diagrams in Category Theory
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- natural-transformations
- adjoint-functors
tags:
- diagrams
- commutative
- morphisms
- composition
stage: advanced
status: draft
---

# Commutative Diagrams in Category Theory

## Core Idea
A commutative diagram is a visual representation of morphism compositions where different paths between objects yield identical morphisms. Commutative diagrams serve as both rigorous notation and pedagogical tools for expressing categorical properties and proofs. They are essential for verifying the consistency of constructions involving multiple objects and morphisms, especially when proving universal properties and naturality conditions.

## How It's Best Learned
Begin with simple two or three-object diagrams, computing compositions along different paths to verify commutativity. Practice translating categorical statements (adjunctions, natural transformations) into diagram form, then verifying each required commutativity directly.

## Common Misconceptions
Commutativity requires paths to compose identically, not merely to yield isomorphic objects. Not every diagram should commute—commutativity must be explicitly required or proven. A diagram being drawable does not imply the relationships depicted are satisfied.

## Explainer

From your study of categories and morphisms, you know that a category consists of objects and arrows (morphisms), with composition defined when arrows connect sequentially. Commutative diagrams are the natural language for expressing that two different sequences of compositions produce the same result — and they are to category theory what equations are to algebra: a way to assert an equality visually.

The simplest commutative diagram is a **triangle**: objects A, B, C and morphisms f: A → B, g: B → C, and h: A → C. The diagram commutes if g ∘ f = h — following the two-step path via B gives the same morphism as taking the direct path h. You can verify this by checking the equation, but drawing it as a diagram makes the structure immediately visible and scales gracefully as the number of objects grows. A **square** with corners A, B, C, D and arrows f: A → B, g: B → D, h: A → C, k: C → D commutes when g ∘ f = k ∘ h — both paths from A to D agree.

The real power emerges with functors. A functor F: C → D must send every commutative diagram in C to a commutative diagram in D — this is the precise meaning of "F preserves composition." A **natural transformation** η: F ⇒ G between functors is exactly the data that makes a family of squares commute: for every morphism f: A → B in C, the square with corners F(A), F(B), G(A), G(B) and edges F(f), G(f), η_A, η_B must commute. The condition η_B ∘ F(f) = G(f) ∘ η_A is the **naturality square**. Without commutative diagram notation, this condition would require several lines of prose to state clearly.

Commutative diagrams also encode **universal properties**. The product A × B in a category is defined by: there exists a unique morphism from any object C into A × B making a certain triangle commute. The pushout of two morphisms is the object making a certain square commute universally. Recognizing these patterns — which diagram shape corresponds to which universal property — is what lets you transfer theorems between algebra, topology, and logic. Once you prove that a result holds for any category containing a commuting triangle of a particular shape, it applies everywhere that shape appears.
