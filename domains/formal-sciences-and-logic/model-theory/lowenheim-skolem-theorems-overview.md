---
id: lowenheim-skolem-theorems-overview
title: 'Löwenheim-Skolem Theorems: Overview and Unification'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: lowenheim-skolem-theorem
  type: hard
- id: infinite-cardinal-numbers
  type: soft
- id: cardinality-and-countability
  type: soft
- id: countable-sets-and-enumeration
  type: soft
builds-toward:
- lowenheim-skolem-downward
- lowenheim-skolem-upward
tags:
- Löwenheim-Skolem
- cardinality
- spectrum
- model size
stage: advanced
status: draft
---

# Löwenheim-Skolem Theorems: Overview and Unification

## Core Idea
The Löwenheim-Skolem theorems describe the spectrum of model sizes: (1) downward: if there is an infinite model, there is a countable model; (2) upward: if there is an infinite model, there are models of every larger cardinality. Together, these results show first-order logic cannot distinguish between infinite cardinalities, constraining its expressive power.

## Explainer

You know from your work on cardinality that infinite sets come in genuinely different sizes—ℕ is countable while ℝ is uncountable, and Cantor's theorem generates an endless tower of strictly larger infinities. The Löwenheim-Skolem theorems reveal that first-order logic is powerless to enforce these distinctions: no matter what first-order theory you write, if it has any infinite model it has models of *every* infinite cardinality. First-order logic cannot pin down the size of its intended structures.

The **downward Löwenheim-Skolem theorem** states: if a theory T has an infinite model M, it has a countable elementary submodel M′ satisfying exactly the same first-order sentences as M. The construction works by closing under witnesses: for every existential formula ∃y φ(a,y) that holds in M with parameters from a chosen countable set, add one witness to the set. This closure process is iterated, and the resulting countable set carries an elementarily equivalent structure. The key word is *elementary*: M′ is not just a substructure but an **elementary substructure**, meaning every first-order sentence with parameters from M′ has the same truth value in M′ as in M.

The **upward Löwenheim-Skolem theorem** states: if T has an infinite model, it has models of every infinite cardinality κ ≥ |T|. The proof adds κ many new constants to the language, asserts they are pairwise distinct, and applies compactness: any finite subset of these assertions is satisfiable (the existing infinite model has enough elements), so the whole enlarged theory is satisfiable. The resulting model has cardinality at least κ, and the downward theorem can trim it to exactly κ.

Together these theorems produce **Skolem's paradox**. ZFC, the standard foundation of mathematics, is a first-order theory. If ZFC has any model at all, it has a *countable* model—yet ZFC proves that uncountable sets exist. How can a countable model contain an "uncountable set"? The resolution: uncountability is not absolute. A set S is uncountable when no bijection between ℕ and S exists *within the model*. In the countable model of ZFC, there is no internal bijection from ℕ to the set that the model calls "ℝ," but a bijection *does* exist outside the model. The model is countable from outside but "correctly" contains an uncountable set from its own perspective. This teaches the deepest lesson of model theory: first-order properties are always model-relative, and expressive power has hard limits that cannot be overcome within the language.
