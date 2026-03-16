---
id: measure-spaces-definition
title: 'Measure Spaces: Definition and Examples'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measurable-sets-properties
  type: hard
builds-toward:
- outer-measure-definition
- null-sets-almost-everywhere
- product-measures-definition
tags:
- measure-theory
- measure-spaces
stage: abstract-reasoning
status: draft
---

# Measure Spaces: Definition and Examples

## Core Idea
A measure space is a triple (X, ℱ, μ) where X is a set, ℱ is a σ-algebra, and μ: ℱ → [0,∞] is countably additive with μ(∅) = 0. This unifies notions of length, area, volume, and probability in a single framework.

## How It's Best Learned
Examine (ℝ, Borel sets, Lebesgue measure), discrete spaces with counting measure, and probability spaces. Verify countable additivity in concrete examples.

## Common Misconceptions
Not all subsets are measurable in general spaces (though they are in Lebesgue's construction on ℝ). Countable additivity is stronger than finite additivity and requires care in proofs.

## Explainer

You already know what a σ-algebra is: a collection ℱ of subsets of X that is closed under complements and countable unions. The σ-algebra specifies *which* subsets of X are "measurable" — the sets we are allowed to assign sizes to. A **measure space** takes the next step: it equips the σ-algebra with an actual measuring function, so we can say not just "this set is measurable" but "this set has measure 3.7."

The triple **(X, ℱ, μ)** has three components. **X** is the underlying set (for example, the real line ℝ, a finite collection of outcomes, or an abstract topological space). **ℱ** is the σ-algebra of measurable subsets — the bookkeeping structure specifying which sets you are allowed to measure. **μ** is the **measure** itself: a function from ℱ to [0, ∞] that assigns each measurable set a non-negative size, possibly infinite. The two axioms are: μ(∅) = 0 (the empty set has zero size), and **countable additivity** — if A₁, A₂, … are pairwise disjoint measurable sets, then μ(⋃ Aᵢ) = Σ μ(Aᵢ).

Countable additivity is the key property that separates measure theory from a naive notion of "size." Finite additivity — the rule holding for finitely many disjoint sets — is weaker and admits pathological counterexamples. Countable additivity forces continuity properties: the measure of an increasing sequence of sets converges to the measure of their union, and the measure of a decreasing sequence of sets (when the first has finite measure) converges to the measure of their intersection. These limit theorems are what allow calculus-like reasoning about integration and convergence.

The power of the measure space axioms is their generality. The triple (ℝ, Borel sets, Lebesgue measure) encodes the ordinary notion of length. The triple (ℝ², Borel sets, 2D Lebesgue measure) encodes area. A **probability space** is simply a measure space (Ω, ℱ, P) where P(Ω) = 1 — the entire space has measure 1. Counting measure on a discrete set assigns each singleton measure 1 and each finite set its cardinality. All of these are the same abstract structure; any theorem proved once in the abstract applies to length, area, probability, and counting simultaneously.
