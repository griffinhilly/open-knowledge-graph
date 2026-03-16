---
id: outer-measure
title: Outer Measure and Carathéodory's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: sigma-algebras-formal-construction
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- lebesgue-measure-real-line
tags:
- measure-theory
- construction
stage: advanced
status: draft
---

# Outer Measure and Carathéodory's Theorem

## Core Idea
An outer measure is a countably subadditive function μ*: P(X) → [0,∞]. Carathéodory's theorem constructs a measure from an outer measure by restricting to Carathéodory-measurable sets, which satisfy the splitting property. This is the key tool for building Lebesgue measure.

## How It's Best Learned
First verify that any outer measure satisfying the countability axiom induces a σ-algebra. Apply to concrete examples like length on intervals to see how outer measure becomes Lebesgue measure.

## Common Misconceptions
- Thinking outer measure is already a measure (it's not countably additive on all sets). - Missing why the splitting property defines measurability (it's the precise condition Carathéodory needed). - Confusing inner and outer measure (only outer measure is used in the theorem).

## Explainer

You know from σ-algebras that a measure is defined on a carefully chosen collection of "measurable" sets, not on every subset of X. But where does that σ-algebra come from in the first place? The construction begins with a more primitive object: an **outer measure** μ*: P(X) → [0,∞], defined on *all* subsets of X, not just the nice ones. The cost of this generality is that μ* is only **countably subadditive** — μ*(⋃Aₙ) ≤ Σμ*(Aₙ) — rather than countably additive. You give up equality in exchange for universality.

The standard way to build an outer measure is from below: for any set E, define μ*(E) = inf{Σμ(Aₙ) : E ⊆ ⋃Aₙ}, where the Aₙ come from some generating collection (like open intervals) with known lengths. The **infimum** of all covering costs is precisely the "outer approximation" of the size of E — which connects to your prerequisite on suprema and infima. For a single interval (a,b), covering it by itself gives μ*(a,b) ≤ b−a, and any cover cannot do better, so μ*(a,b) = b−a. This is the intuition: outer measure recovers the right answer on simple sets.

**Carathéodory's theorem** solves the key problem: which sets can be assigned a *genuine* measure (one that is actually additive, not just subadditive)? Carathéodory's criterion says E is **measurable** if for every test set T, we have μ*(T) = μ*(T ∩ E) + μ*(T ∩ Eᶜ). This is the **splitting property**: a set E is measurable precisely when it splits every test set T additively. Geometrically, E has a "sharp enough" boundary that it doesn't create measurement ambiguity. The remarkable fact is that the collection of all measurable sets automatically forms a σ-algebra, and the restriction of μ* to this σ-algebra is countably additive — a genuine measure.

Why does this matter? Because it gives a complete construction of **Lebesgue measure** without assuming from the outset what the measurable sets are. Start with interval lengths, build the outer measure via coverings, and let Carathéodory's criterion identify which sets are measurable. The resulting σ-algebra turns out to contain all open and closed sets, all countable unions and intersections of these, and far more — essentially everything you would want to measure. The non-measurable sets (like the Vitali set) are exactly those that fail the splitting property, and their existence is precisely why we cannot naively assign a size to every subset of ℝ.
