---
id: cumulative-hierarchy-and-ranks
title: The Cumulative Hierarchy and Set Ranks
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: natural-numbers-as-iterative-construction
  type: hard
- id: indexed-families-of-sets
  type: soft
builds-toward:
- axiom-of-regularity
- axiom-of-foundation
- constructible-universe
tags:
- hierarchy
- ranks
- foundation
stage: formal-systems
status: draft
---

# The Cumulative Hierarchy and Set Ranks

## Core Idea
The cumulative hierarchy V is defined iteratively: V₀ = ∅, V_{α+1} = 𝒫(V_α), and V_λ = ⋃_{α<λ} V_α for limit ordinals λ. Every set has a rank—the smallest ordinal α such that the set is in V_{α+1}. This formalization captures the intuition that sets are built successively from the empty set, with no circular dependencies.

## Explainer

You know from the iterative construction of natural numbers that ∅ can serve as the "starting point" from which all mathematical objects are built. The **cumulative hierarchy** V generalizes this insight to all of set theory: every set is a collection built from previously existing sets, which are themselves built from earlier sets, all the way back to ∅. The hierarchy makes this informal picture precise using ordinals as the index of construction.

The construction proceeds in stages indexed by ordinals α:
- **V₀ = ∅** — at stage 0, nothing exists yet.
- **V₁ = 𝒫(V₀) = {∅}** — at stage 1, you can form the one subset of ∅, which is ∅ itself.
- **V₂ = 𝒫(V₁) = {∅, {∅}}** — at stage 2, you have two elements and can form 4 subsets: ∅, {∅}, {{∅}}, and {∅, {∅}}.
- **V_{n+1} = 𝒫(Vₙ)** — each finite stage doubles in a structured way.
- **Vω = ⋃_{n<ω} Vₙ** — at the first limit ordinal ω, you take the union of all finite stages. This is the smallest infinite set in the hierarchy.
- **V_{ω+1} = 𝒫(Vω)** — now you can form all subsets of Vω, which has cardinality ℵ₀, giving a stage of size 2^ℵ₀.

The **rank** of a set x is the smallest ordinal α such that x ∈ V_{α+1}. Equivalently, rank(x) = sup{rank(y) + 1 : y ∈ x}. The rank of ∅ is 0, of {∅} is 1, of {∅, {∅}} is 2, and so on. The natural number n (in the von Neumann encoding 0 = ∅, 1 = {0}, 2 = {0,1}, …) has rank n. The set ω of natural numbers has rank ω, and its power set 𝒫(ω) has rank ω+1.

The philosophical payoff is the **well-foundedness** of set membership. The axiom of regularity (or foundation) asserts exactly that every set has a rank — equivalently, there are no infinite descending ∈-chains x₁ ∋ x₂ ∋ x₃ ∋ … and no set is a member of itself. The cumulative hierarchy gives a *model* of this axiom: since ranks are ordinals and ordinals are well-ordered, the membership relation on sets in V is well-founded by construction. Any claim about sets can be made by transfinite induction on rank: prove it for rank-0 sets (just ∅), assume it for all sets of rank < α, and prove it for rank-α sets. This is the set-theoretic analogue of mathematical induction, and it underlies the standard technique for proving results about all sets in ZFC. The hierarchy V = ⋃_α V_α is not just a convenient picture — it is the universe within which all ZFC mathematics takes place.

