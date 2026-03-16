---
id: bijections-establish-equinumerosity
title: Bijections and Cardinality Equivalence
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: naive-set-theory
  type: hard
builds-toward:
- cardinality-and-equinumerosity
- infinite-cardinal-numbers
tags:
- cardinality
- bijections
- functions
- equivalence
stage: formal-systems
status: draft
---

# Bijections and Cardinality Equivalence

## Core Idea
Two sets have the same cardinality if and only if there exists a bijection (one-to-one and onto function) between them. This formal definition replaces intuitive notions of 'same size' with a precise mathematical relation. Bijections establish an equivalence relation on sets, partitioning them into cardinality classes.

## How It's Best Learned
Start with finite examples: show bijections between sets of different sizes establish equality. Then apply to countably infinite sets, comparing ℕ with ℤ and ℚ via explicit bijections.

## Common Misconceptions
- Assuming infinite sets cannot be equinumerous with proper subsets (forgetting that Dedekind-infinite sets can be).
- Confusing bijections with other function types; bijections require both injection AND surjection.

## Explainer

From naive set theory, you know how to describe sets and functions. Now a natural question arises: when do two sets have "the same number of elements"? For finite sets you can just count. But Cantor's insight, which launched the mathematical study of infinity, was that the right definition in all cases — finite or infinite — is to use **bijections**. Two sets A and B have the same **cardinality** if there exists a bijection f: A → B: a function that is both **injective** (one-to-one: distinct inputs map to distinct outputs, so nothing in B is hit twice) and **surjective** (onto: every element of B is mapped to by at least one element of A). Together these guarantee a perfect pairing with nothing left over on either side.

For finite sets, this matches intuition precisely. A bijection between two finite sets is exactly a perfect pairing — like matching dancers to partners one-to-one with none left unpartnered. If such a pairing exists, the two sets must be the same size. The bijection replaces the need to count: rather than counting each set separately and comparing the numbers, you directly exhibit the correspondence. The key shift is moving from "count then compare" to "pair directly" — a shift that pays off enormously when dealing with infinite sets where counting breaks down.

The payoff is immediate and counterintuitive. Consider the even natural numbers E = {0, 2, 4, 6,...}. Intuitively, E seems "smaller" than ℕ = {0, 1, 2, 3,...} — it misses all the odd numbers. But the function f(n) = 2n is a bijection from ℕ to E: it is injective (different n's give different 2n's) and surjective (every even number 2k is the image of k). By Cantor's definition, ℕ and E have the same cardinality. This is **Dedekind-infinity**: a set is Dedekind-infinite if it can be put in bijection with a proper subset. For infinite sets, cardinality-as-bijection diverges from finite intuition — and that divergence is mathematically meaningful, not a flaw.

Cardinality defined via bijections is an **equivalence relation** on sets. Reflexivity: every set A bijects with itself via the identity function. Symmetry: if f: A → B is a bijection, then f⁻¹: B → A is also a bijection (bijections are invertible). Transitivity: if f: A → B and g: B → C are bijections, then g ∘ f: A → C is a bijection. This partitions all sets into cardinality classes. The finite sets divide into classes of size 0, 1, 2, 3,... Then comes the class of **countably infinite** sets (those bijecting with ℕ), and beyond that the uncountable sets. Your next step will be Cantor's theorem: no set bijects with its own power set, which shows that no matter how large a set is, its collection of subsets is strictly larger. The cardinality hierarchy is infinite — there is no largest infinity.
