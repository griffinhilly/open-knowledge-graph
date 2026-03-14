---
id: coends-and-ends
title: Coends and Ends
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: limits-and-colimits
  type: hard
- id: functor-categories
  type: soft
- id: opposite-categories-and-duality
  type: soft
tags:
- end
- coend
- dinatural transformation
- ninja Yoneda lemma
- weighted limit
- integral notation
stage: advanced
status: draft
---
# Coends and Ends

## Core Idea
An end of a functor T: C^op × C → D is an object ∫_c T(c,c) equipped with a universal dinatural transformation from ∫_c T(c,c) to T, satisfying a wedge condition that generalizes the notion of a limit. Dually, a coend ∫^c T(c,c) is a universal cowedge, generalizing colimits. Ends and coends provide compact formulas throughout category theory: the set of natural transformations Nat(F, G) can be written as the end ∫_c Hom(F(c), G(c)), and the tensor product of functors is a coend. The "ninja Yoneda lemma" states F(a) ≅ ∫^c Hom(a, c) × F(c), expressing any functor value as a coend against the Yoneda embedding. Ends and coends are essential for weighted limits, Kan extensions, and Day convolution.

## How It's Best Learned
Compute the end ∫_c Hom(F(c), G(c)) for two specific functors F, G: C → Set on a small category C with two or three objects. Verify that the result is the set of natural transformations Nat(F, G) by checking the wedge condition against the naturality squares. Then compute a coend: ∫^c Hom(a, c) × F(c) for a representable presheaf and verify the ninja Yoneda result.

## Common Misconceptions
- Ends and coends are not simply limits and colimits of the diagonal; they involve dinatural transformations and wedge conditions that are genuinely different from ordinary cones.
- The integral notation (∫_c and ∫^c) is standard but can be confused with analysis; the subscript indicates an end (analogous to a product/limit) and the superscript indicates a coend (analogous to a coproduct/colimit).
- Dinaturality is weaker than naturality; a dinatural transformation between bifunctors C^op × C → D does not compose in general, which is why ends and coends require the wedge universality rather than ordinary naturality.
