---
id: lebesgue-measure-real-line
title: Lebesgue Measure on ℝ and ℝⁿ
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-outer-measure
  type: hard
- id: borel-sigma-algebra
  type: soft
builds-toward:
- lebesgue-integral-simple-functions
- riemann-vs-lebesgue-integrals
tags:
- measure-theory
- lebesgue-measure
stage: abstract-reasoning
status: draft
---

# Lebesgue Measure on ℝ and ℝⁿ

## Core Idea
The Lebesgue measure on ℝ is the unique measure on the Borel σ-algebra satisfying μ([a,b]) = b - a. The Carathéodory measurable sets form a σ-algebra strictly larger than Borel sets (including all null sets). Lebesgue measure is translation-invariant and extends naturally to ℝⁿ.

## Explainer

In your study of Lebesgue outer measure, you built a function μ* that assigns a non-negative real number (or ∞) to every subset of ℝ by covering the set with countable unions of open intervals and taking the infimum of the total length. The outer measure works for every set, but it doesn't behave well enough for integration: it fails to be countably additive on arbitrary collections of sets. **Lebesgue measure** fixes this by restricting attention to the sets where outer measure does behave well — the **Carathéodory measurable sets**.

A set E is Carathéodory measurable if it splits every other set A "cleanly": μ*(A) = μ*(A ∩ E) + μ*(A ∩ E^c) for all A. This condition says E acts as a perfect partition tool — it neither loses nor double-counts measure when used to split anything. The collection of all such sets forms a **σ-algebra** (closed under countable unions and complements), and the restriction of μ* to this σ-algebra is **Lebesgue measure** μ. This σ-algebra is strictly larger than the Borel σ-algebra you've studied: it includes all subsets of null sets (sets with measure zero), making Lebesgue measure **complete** in the technical sense.

The key properties to internalize are: (1) μ([a,b]) = b − a for any closed interval, consistent with ordinary length; (2) countable additivity — if E₁, E₂, ... are disjoint measurable sets, then μ(∪Eₙ) = Σμ(Eₙ); and (3) **translation invariance** — shifting a set E by a constant doesn't change its measure, μ(E + t) = μ(E). These properties uniquely characterize Lebesgue measure on the Borel sets: it is the only Borel measure on ℝ that assigns b − a to every interval [a, b] and is translation-invariant.

In ℝⁿ the construction extends naturally: open boxes (products of open intervals) serve as the covering sets, and their "volume" is the product of the edge lengths. The Lebesgue measure in ℝ² assigns area, in ℝ³ assigns volume, and so on. Null sets — sets of measure zero — are sets that can be covered by countable unions of intervals with total length less than any ε > 0. The rationals ℚ are a null set in ℝ despite being dense everywhere, a fact that sharply separates Lebesgue theory from Riemann integration and motivates the next step: integrating functions that are only well-behaved "almost everywhere."
