---
id: outer-measure-definition
title: 'Outer Measure: Definition and Properties'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measure-spaces-definition
  type: hard
builds-toward:
- caratheodory-extension-theorem
tags:
- measure-theory
- outer-measure
stage: abstract-reasoning
status: draft
---

# Outer Measure: Definition and Properties

## Core Idea
An outer measure μ*: 𝒫(X) → [0,∞] is monotone, countably subadditive, and satisfies μ*(∅) = 0. Outer measures are defined on all subsets, unlike measures. They serve as a tool for constructing measures via Carathéodory's theorem.

## Explainer

From your work on measure spaces, you know that a measure μ assigns sizes to sets in a σ-algebra in a countably additive way: μ(⋃ Eᵢ) = Σ μ(Eᵢ) for disjoint measurable sets. But this raises a bootstrapping problem: which sets should count as measurable in the first place? If you try to make every subset measurable and assign it a consistent, countably additive size, you run into paradoxes — the Vitali construction shows no such assignment can exist on all subsets of the real line. An **outer measure** is the technical device that navigates this problem by working with all subsets first, then identifying the well-behaved ones.

An outer measure μ*: 𝒫(X) → [0,∞] is defined on *all* subsets of X — not just the measurable ones. It satisfies three properties: μ*(∅) = 0, **monotonicity** (A ⊆ B implies μ*(A) ≤ μ*(B)), and **countable subadditivity** (μ*(⋃ Aᵢ) ≤ Σ μ*(Aᵢ)). The key contrast with a measure is in the last property: subadditivity is an inequality, not an equality. An outer measure may "overcount" when sets overlap, because it asks only for a consistent upper bound, not exact accounting.

The canonical example is the **Lebesgue outer measure** on ℝ: define μ*(A) = inf{Σ |Iₙ|: A ⊆ ⋃ Iₙ} where the infimum is over all countable covers of A by open intervals. This assigns a candidate "length" to every subset of ℝ, no matter how bizarre. Monotonicity holds because more sets can cover a smaller set; subadditivity holds because you can combine covers. But countable additivity fails on non-measurable sets — overlapping covers cannot be separated.

This is precisely the gap that **Carathéodory's theorem** closes. A set E is called **μ*-measurable** if it "splits" every test set A cleanly: μ*(A) = μ*(A ∩ E) + μ*(A ∩ Eᶜ). This condition says E does not cause overcounting — the outer measure of A is exactly the sum of the parts on each side of E. Carathéodory showed that the collection of all μ*-measurable sets forms a σ-algebra, and μ* restricted to this σ-algebra is a genuine measure. The outer measure is scaffolding: it builds candidate sizes for all sets, then the measurability condition filters out the pathological ones, leaving a clean measure space.
