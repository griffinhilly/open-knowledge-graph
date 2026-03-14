---
id: adjunction-as-hom-bijection
title: Adjunctions as Natural Hom-set Bijections
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: left-adjoint-functors
  type: hard
- id: right-adjoint-functors
  type: hard
- id: adjoint-functors
  type: soft
builds-toward:
- monads-in-category-theory
- kan-extensions
tags:
- adjunction
- hom-sets
- natural-transformation
stage: advanced
status: draft
---

# Adjunctions as Natural Hom-set Bijections

## Core Idea
An adjunction L ⊣ R is a pair of functors with a natural isomorphism φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd) for all objects c and d. The unit η: id_C ⇒ RL and counit ε: LR ⇒ id_D encapsulate the adjunction. This framework unifies diverse constructions—free groups, tensor products, completions—as universal solutions.
