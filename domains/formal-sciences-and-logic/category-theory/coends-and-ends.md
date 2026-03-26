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
stage: expert
status: validated
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

## Questions

```yaml
- question: "The set of natural transformations Nat(F, G) between functors F, G: C → Set can be expressed categorically as which of the following?"
  type: multiple-choice
  options:
    - "The limit of the functor c ↦ Hom(F(c), G(c)) over the category C"
    - "The colimit of the functor c ↦ Hom(F(c), G(c)) over the category C"
    - "The end ∫_c Hom(F(c), G(c)), the universal wedge of the Hom bifunctor"
    - "The coend ∫^c Hom(F(c), G(c)), the universal cowedge of the Hom bifunctor"
  answer: 2
  explanation: "Nat(F, G) = ∫_c Hom(F(c), G(c)) is the canonical example of an end. An element of this end is a family of functions α_c: F(c) → G(c) satisfying the wedge condition — which turns out to be exactly the naturality condition. The end is correct (not a limit or colimit) because Hom(F(−), G(−)): C^op × C → Set has mixed variance, requiring dinatural transformations rather than ordinary natural transformations. A limit of the diagonal functor c ↦ T(c,c) is a different, weaker construction that misses the off-diagonal naturality conditions."

- question: "A student says: 'Computing Nat(F, G) as an end is just computing the limit of the diagonal functor c ↦ Hom(F(c), G(c)) — ends are limits applied to different notation.' What is the key error?"
  type: multiple-choice
  options:
    - "There is no error — ends of the form ∫_c T(c,c) are always equal to limits of the diagonal functor c ↦ T(c,c)"
    - "The limit of the diagonal only uses morphisms T(f,f) along the diagonal, but the end's wedge condition also imposes consistency through the off-diagonal T(f, id) and T(id, f) routes"
    - "The error is minor — ends and limits of the diagonal agree for Set-valued functors but diverge for other target categories"
    - "The error is about variance — limits apply to covariant functors, but T(c,c) is contravariant in c"
  answer: 1
  explanation: "The limit of the diagonal functor uses only T(f,f): T(d,d) → T(c,c) (applying f in both slots simultaneously). The end's wedge condition is stronger: for every morphism f: c → d, the two paths T(d,c) → T(d,d) → end and T(d,c) → T(c,c) → end must agree. This off-diagonal condition captures simultaneous naturality in both variance slots and is genuinely different from an ordinary limit. For Nat(F,G), it captures exactly the naturality squares that the limit-of-diagonal construction would miss."

- question: "In the integral notation for ends and coends, ∫_c (subscript) denotes an end — analogous to a limit, requiring consistency at every c — while ∫^c (superscript) denotes a coend, analogous to a colimit, identifying contributions from different c."
  type: true-false
  answer: true
  explanation: "This is the standard convention and intended analogy. An end ∫_c T(c,c) selects elements consistent with the wedge condition across all objects — like a product or limit, it requires something to hold everywhere simultaneously. A coend ∫^c T(c,c) identifies elements related by the coaction of morphisms — like a coproduct or colimit, it takes a sum and quotients by equivalence. The notation mirrors integration: subscript = integrate over all c simultaneously (limit flavor); superscript = sum over c with identifications (colimit flavor)."

- question: "Dinatural transformations between bifunctors C^op × C → D can generally be composed to form a new dinatural transformation, just as natural transformations between functors C → D compose."
  type: true-false
  answer: false
  explanation: "This is a key difference between dinaturals and naturals. Given dinatural transformations α: S → T and β: T → U where S, T, U: C^op × C → D, the naive composite β_c ∘ α_c is generally NOT dinatural — the hexagon condition for dinaturality fails at the composite. This failure is precisely why ends and coends are defined using wedge universality rather than ordinary naturality: wedges are a restricted class of dinatural families (from/to a constant functor) for which universal properties can be stated cleanly without requiring general dinaturality composition."

- question: "State the ninja Yoneda lemma and explain intuitively why the functor value F(a) can be recovered as the coend ∫^c Hom(a, c) × F(c)."
  type: short-answer
  answer: "The ninja Yoneda lemma states: F(a) ≅ ∫^c Hom(a, c) × F(c). For each morphism f: a → c and each element x ∈ F(c), the coend takes pairs (f, x) and identifies (f, x) ~ (g, F(h)(x)) whenever h ∘ f = g for morphisms h: c → c'. Since every morphism f: a → c can be factored through a → a via identity, every pair (f: a → c, x ∈ F(c)) gets identified with (id_a, F(f)(x) ∈ F(a)). After all identifications, the only data that survives is an element of F(a) itself."
  explanation: "The coend is a 'change-of-basis' formula: it expresses F as a weighted colimit of representable functors Hom(a, −), with the Yoneda embedding as the canonical basis. For each c, you take one copy of F(c) for each morphism a → c, then quotient by the natural action of morphisms. The quotient collapses everything to F(a) because F is functorial — any element x ∈ F(c) reachable from a via f: a → c is identified with F(f)(x) ∈ F(a). This is the coend version of the Yoneda lemma, generalizing cleanly to weighted limits and enriched categories."
```

## Explainer

You already know that a natural transformation η: F → G assigns a morphism η_c: F(c) → G(c) to each object c, subject to a naturality square: for every f: c → d, the square η_d ∘ F(f) = G(f) ∘ η_c commutes. Natural transformations treat the functor argument as a *covariant* slot. Ends and coends generalize this to functors T: C^op × C → D with *two* arguments — one contravariant and one covariant. The challenge is that you need something like naturality in both slots simultaneously, but they are in opposite variance. A **dinatural transformation** resolves this: for each f: c → d, the hexagon T(d, c) → T(d, d) → T(d, e) and T(d, c) → T(c, c) → T(c, e) both commute (formally, the two routes through T(f, id) and T(id, f) are equal). A **wedge** is a dinatural family that factors through a common object.

An **end** ∫_c T(c, c) is the universal wedge: an object e in D with a dinatural family π_c: e → T(c, c) such that every other wedge factors uniquely through e. Think of it as the most general "simultaneously natural in both slots" extraction of T's diagonal. The canonical example is the set of natural transformations: **Nat(F, G) = ∫_c Hom(F(c), G(c))**. An element of this end is a family of functions α_c: F(c) → G(c) — one per object — that satisfies the naturality condition, exactly because the wedge condition for Hom(F(−), G(−)): C^op × C → Set is precisely naturality. The end packages the naturality requirement into a single universal object.

A **coend** ∫^c T(c, c) is the dual: a universal cowedge. Where an end is a limit-like construction (requiring something to be equal for all objects simultaneously), a coend is a colimit-like construction (identifying things across the diagonal). The **ninja Yoneda lemma** F(a) ≅ ∫^c Hom(a, c) × F(c) says that any functor value F(a) can be recovered as a coend against the representable functor Hom(a, −). Intuitively: you can reconstruct F(a) by taking one copy of F(c) for each morphism a → c and then identifying (via the coend relation) all the copies that are related by precomposition. It is a "change-of-basis" formula for functors, making the Yoneda embedding the canonical basis.

The integral notation — subscript for ends, superscript for coends — is designed to mirror the analogy with integration: an end is like a product over the variable c (you need consistency at every c), a coend is like a sum or integral over c (you identify contributions from different c). Day convolution, weighted limits, and the pointwise formula for Kan extensions all reduce to ends and coends once you know the machinery. When you see ∫_c or ∫^c in a categorical formula, the first step is always to identify the functor T: C^op × C → D, verify what the wedge condition requires, and check whether the universal property gives you the object you want.
