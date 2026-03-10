---
id: adjunction-unit-and-counit
title: Adjunction Unit and Counit
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- monads-in-category-theory
- equivalence-of-categories
tags:
- unit
- counit
- triangle identities
- adjunction
- monad
stage: advanced
status: draft
---

# Adjunction Unit and Counit

## Core Idea
An adjunction F ⊣ G can equivalently be given by two natural transformations: the unit η: Id_C ⇒ G∘F and the counit ε: F∘G ⇒ Id_D, satisfying the triangle identities (ε_F ∘ F(η) = id_F and G(ε) ∘ η_G = id_G). The unit η_A: A → GF(A) is the universal arrow from A to G—the 'most efficient' way to place A inside the G-structure. The triangle identities are the coherence conditions that ensure the hom-set bijection and the unit-counit formulation are equivalent.

## How It's Best Learned
For the free-forgetful adjunction between Set and Grp, identify the unit as the inclusion of a set S into the underlying set of its free group F(S), and the counit as the evaluation map F(U(G)) → G sending generators to their values. Verify both triangle identities by tracing elements.

## Common Misconceptions
- The triangle identities look like cancellation laws but are not trivially true; they encode the coherence between unit and counit.
- The unit need not be a monomorphism and the counit need not be an epimorphism in general, though they are in many familiar examples.
- Confusing the unit (going into GF) with the counit (coming out of FG) is a common source of errors.
