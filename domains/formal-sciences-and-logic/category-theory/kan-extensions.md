---
id: kan-extensions
title: Kan Extensions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: limits-and-colimits
  type: hard
- id: adjoint-functors
  type: soft
- id: functor-categories
  type: soft
- id: functions-and-function-properties
  type: soft
- id: function-composition
  type: soft
- id: set-operations
  type: soft
- id: function-composition-and-inverses
  type: soft
tags:
- Kan extension
- left Kan extension
- right Kan extension
- pointwise Kan extension
- colimit formula
- universal construction
stage: advanced
status: draft
---
# Kan Extensions

## Core Idea
Given functors K: C → D and F: C → E, the left Kan extension Lan_K F: D → E is the universal functor extending F along K, satisfying a universal property: Nat(Lan_K F, G) ≅ Nat(F, G ∘ K) for all G: D → E. Dually, the right Kan extension Ran_K F satisfies Nat(G, Ran_K F) ≅ Nat(G ∘ K, F). When E is cocomplete, left Kan extensions can be computed pointwise as colimits: (Lan_K F)(d) = colim_{(c, K(c)→d)} F(c) over the comma category (K ↓ d). Saunders Mac Lane famously wrote that "all concepts are Kan extensions," since limits, colimits, adjunctions, and even the Yoneda embedding can be expressed as Kan extensions.

## How It's Best Learned
Start with the simplest case: K is the inclusion of a subcategory and F assigns values on that subcategory. Compute the left Kan extension as a colimit over the relevant comma category for a concrete example (e.g., extending a functor defined on a discrete category to a larger one). Then verify that adjoint functors are a special case: the left adjoint of G is the left Kan extension of the identity along G.

## Common Misconceptions
- Kan extensions need not exist in general; existence requires sufficient (co)completeness conditions or specific properties of the functors involved.
- Pointwise Kan extensions (computed as (co)limits) are stronger than abstract Kan extensions defined solely by the universal property; the pointwise version implies the abstract one but not conversely.
- The phrase "all concepts are Kan extensions" is a conceptual statement about the universality of the construction, not a claim that every theorem in category theory literally reduces to a Kan extension computation.

## Explainer

The motivating question is simple: given a functor F: C → E and a functor K: C → D that "embeds" or "changes" the indexing, can you extend F to all of D in the most economical way? Concretely, imagine F is defined on a small subcategory C but you need a functor defined on all of D — the left Kan extension Lan_K F is the "best approximation from the left" to this problem. The universal property says: natural transformations from Lan_K F to any G: D → E are in natural bijection with natural transformations from F to G ∘ K. This is the same pattern you know from adjunctions: Lan_K F is left adjoint to the precomposition functor (− ∘ K) between functor categories. When you see Nat(Lan_K F, G) ≅ Nat(F, G ∘ K), read it as "the extension sees everything the original functor saw, and nothing more."

When E is cocomplete, you can compute the left Kan extension **pointwise** as a colimit. For each object d ∈ D, the comma category (K ↓ d) consists of all pairs (c ∈ C, K(c) → d) — the objects of C that map into d via K, together with those maps. The colimit of F over this comma category gives (Lan_K F)(d) = colim_{(K ↓ d)} F. Intuitively, to define the extension at d, you look at all the "ways d can be reached from C via K," take the values of F at those sources, and glue them together in the most general way — a colimit. The right Kan extension is the dual, using limits over the comma category (d ↓ K) instead. Pointwise Kan extensions are particularly well-behaved: they are preserved by representable functors and interact cleanly with composition.

Adjunctions are among the most important special cases. If you take K = G: D → C (a functor you want a left adjoint for) and set F = Id_C, then Lan_G Id_C: C → D is exactly the left adjoint of G — if it exists. The universal property of the Kan extension precisely recovers the adjoint bijection Hom_C(c, G(d)) ≅ Hom_D(Fd, d). This is why Mac Lane's dictum "all concepts are Kan extensions" carries weight: limits (right Kan extensions along the diagonal), colimits (left Kan extensions along the diagonal), the Yoneda embedding (the right Kan extension of the identity along itself), and adjoints all fall out of the one construction. Understanding Kan extensions is essentially understanding the universal properties that hold all of category theory together.

A practical technique worth mastering is computing Kan extensions via the **coend formula** for functor categories: (Lan_K F)(d) = ∫^{c ∈ C} Hom_D(K(c), d) ⊗ F(c), a "weighted colimit" that generalizes the pointwise formula. This expression makes it transparent that the extension at d is built by "gluing copies of F(c) weighted by how many ways K(c) maps to d." For discrete categories, it collapses to a coproduct; for enriched categories, it becomes a tensor product. Once you see this formula, constructions like Day convolution (the monoidal structure on functor categories) and nerve-realization adjunctions appear as instances of the same underlying Kan extension machinery.
