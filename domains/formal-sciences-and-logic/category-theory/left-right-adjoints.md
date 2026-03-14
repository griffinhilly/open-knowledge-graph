---
id: left-right-adjoints
title: Left and Right Adjoints
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: universal-properties
  type: hard
builds-toward:
- kan-extensions
- topos-theory-intro
tags:
- adjoint
- universal-property
- left
- right
stage: advanced
status: draft
---

# Left and Right Adjoints

## Core Idea
For functors F: C → D and G: D → C, F is left adjoint to G (written F ⊣ G) if there exists a natural isomorphism Hom_D(F(−), −) ≅ Hom_C(−, G(−)). This relationship encodes a deep structural property: F and G preserve the monoidal and functorial properties of their source and target categories. Adjoint pairs unify free constructions, tensor products, and many universal properties across algebra and topology.

## How It's Best Learned
Start with concrete adjoint pairs: free-forgetful adjunctions between Set and algebraic categories, tensor product and hom adjunctions between module categories, and homology-cohomology pairings. Verify the adjunction by computing natural isomorphisms of hom-sets explicitly.

## Common Misconceptions
Adjoint functors are not inverses or quasi-inverses; they are distinct functors with a specific structural relationship. Left and right refer to the position in the hom-functor isomorphism, not to group-theoretic inverses. An adjoint pair exists only when the universal property can be satisfied in a natural, categorical way.
