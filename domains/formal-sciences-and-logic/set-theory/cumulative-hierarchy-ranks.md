---
id: cumulative-hierarchy-ranks
title: The Cumulative Hierarchy and Ranks
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: von-neumann-ordinals
  type: hard
- id: axiom-of-regularity
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- constructible-universe
- absolute-formulas-models
tags:
- cumulative-hierarchy
- ranks
- von-neumann
- foundation
stage: formal-systems
status: draft
---

# The Cumulative Hierarchy and Ranks

## Core Idea
The cumulative hierarchy V is a stratification of all sets by rank. V₀ = ∅, V_{α+1} = P(V_α), and V_λ = ⋃_{α < λ} V_α for limit λ. Every set has a rank, the least ordinal α such that the set belongs to V_α. The union V = ⋃_α V_α is the universe of all sets in standard set theory, and foundation ensures every set is in some V_α.

## How It's Best Learned
Construct V₀, V₁, V₂, ... and describe which sets appear at each level. Show hereditarily finite sets occur in V_ω. Verify that rank(x) is well-defined by transfinite induction. Discuss absoluteness: the notion of rank is absolute across models of ZFC.

## Common Misconceptions
- Confusing rank with cardinality; rank is an ordinal measuring depth, not size.
- Forgetting that V itself is a proper class, not a set, due to the Burali-Forti paradox.

## Explainer

From your study of von Neumann ordinals, you know that ordinals are defined so that each ordinal α is the set of all smaller ordinals: 0 = ∅, 1 = {0}, 2 = {0, 1}, ω = {0, 1, 2, ...}, and so on. The **cumulative hierarchy** uses ordinals as indices to stratify the entire universe of sets into a well-ordered tower, where each level is built from the previous by taking the power set.

The construction proceeds by transfinite recursion. Define: V₀ = ∅, V_{α+1} = P(V_α) (the power set of the previous level), and V_λ = ⋃_{α < λ} V_α for limit ordinals λ (the union of all earlier levels). The first few levels already produce many familiar objects: V₁ = {∅} (one set), V₂ = {∅, {∅}} (two sets), V₃ has 4 elements, V₄ has 16, and so on. By V_ω — the union of all finite levels — we have all the **hereditarily finite sets**: sets whose members, members of members, and so on, are all finite. The von Neumann natural numbers 0, 1, 2, ... are all in V_ω, and V_ω itself is a model of ZFC minus the axiom of infinity.

Every set x has a **rank**: the least ordinal α such that x ∈ V_{α+1}, equivalently, one more than the supremum of the ranks of x's elements. Rank measures **depth of membership nesting**, not size or cardinality. The set {ω} has rank ω + 1, even though it contains only one element, because that element ω has rank ω. A set of rank 3 contains only sets of rank ≤ 2, which contain only sets of rank ≤ 1, which contain only ∅. Rank is an ordinal-valued measure of how deeply a set's construction is nested, analogous to the depth of a tree.

The **axiom of regularity** (foundation) is what makes the cumulative hierarchy a description of *all* sets: it rules out membership cycles (x ∈ x, or x ∈ y ∈ x) and non-well-founded sets. Under regularity, every set is well-founded — its membership relation terminates — which means every set appears at some finite or transfinite level V_α. The universe V = ⋃_α V_α is thus the totality of all well-founded sets. The hierarchy is not just a picture of the universe; it *is* the universe, stratified by rank. This stratification is crucial for **relative consistency proofs** and for the concept of **absoluteness**: a formula is absolute if its truth in some V_α is the same as its truth in the full universe V, regardless of what new sets exist at higher ranks. Rank provides the tool that makes these arguments precise.
