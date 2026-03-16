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

## Explainer

You already know that a natural transformation η: F → G assigns a morphism η_c: F(c) → G(c) to each object c, subject to a naturality square: for every f: c → d, the square η_d ∘ F(f) = G(f) ∘ η_c commutes. Natural transformations treat the functor argument as a *covariant* slot. Ends and coends generalize this to functors T: C^op × C → D with *two* arguments — one contravariant and one covariant. The challenge is that you need something like naturality in both slots simultaneously, but they are in opposite variance. A **dinatural transformation** resolves this: for each f: c → d, the hexagon T(d, c) → T(d, d) → T(d, e) and T(d, c) → T(c, c) → T(c, e) both commute (formally, the two routes through T(f, id) and T(id, f) are equal). A **wedge** is a dinatural family that factors through a common object.

An **end** ∫_c T(c, c) is the universal wedge: an object e in D with a dinatural family π_c: e → T(c, c) such that every other wedge factors uniquely through e. Think of it as the most general "simultaneously natural in both slots" extraction of T's diagonal. The canonical example is the set of natural transformations: **Nat(F, G) = ∫_c Hom(F(c), G(c))**. An element of this end is a family of functions α_c: F(c) → G(c) — one per object — that satisfies the naturality condition, exactly because the wedge condition for Hom(F(−), G(−)): C^op × C → Set is precisely naturality. The end packages the naturality requirement into a single universal object.

A **coend** ∫^c T(c, c) is the dual: a universal cowedge. Where an end is a limit-like construction (requiring something to be equal for all objects simultaneously), a coend is a colimit-like construction (identifying things across the diagonal). The **ninja Yoneda lemma** F(a) ≅ ∫^c Hom(a, c) × F(c) says that any functor value F(a) can be recovered as a coend against the representable functor Hom(a, −). Intuitively: you can reconstruct F(a) by taking one copy of F(c) for each morphism a → c and then identifying (via the coend relation) all the copies that are related by precomposition. It is a "change-of-basis" formula for functors, making the Yoneda embedding the canonical basis.

The integral notation — subscript for ends, superscript for coends — is designed to mirror the analogy with integration: an end is like a product over the variable c (you need consistency at every c), a coend is like a sum or integral over c (you identify contributions from different c). Day convolution, weighted limits, and the pointwise formula for Kan extensions all reduce to ends and coends once you know the machinery. When you see ∫_c or ∫^c in a categorical formula, the first step is always to identify the functor T: C^op × C → D, verify what the wedge condition requires, and check whether the universal property gives you the object you want.
