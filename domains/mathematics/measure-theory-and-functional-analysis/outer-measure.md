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
stage: expert
status: validated
---

# Outer Measure and Carathéodory's Theorem

## Core Idea
An outer measure is a countably subadditive function μ*: P(X) → [0,∞]. Carathéodory's theorem constructs a measure from an outer measure by restricting to Carathéodory-measurable sets, which satisfy the splitting property. This is the key tool for building Lebesgue measure.

## How It's Best Learned
First verify that any outer measure satisfying the countability axiom induces a σ-algebra. Apply to concrete examples like length on intervals to see how outer measure becomes Lebesgue measure.

## Common Misconceptions
- Thinking outer measure is already a measure (it's not countably additive on all sets). - Missing why the splitting property defines measurability (it's the precise condition Carathéodory needed). - Confusing inner and outer measure (only outer measure is used in the theorem).

## Questions

```yaml
- question: "An outer measure μ* assigns values to all subsets of ℝ. Which property distinguishes it from a genuine measure?"
  type: multiple-choice
  options:
    - "It assigns ∞ to all unbounded sets"
    - "It is only countably subadditive, not countably additive"
    - "It is not monotone — larger sets can get smaller values"
    - "It fails to assign 0 to the empty set"
  answer: 1
  explanation: "A genuine measure requires countable additivity: μ(⋃Aₙ) = Σμ(Aₙ) for disjoint measurable sets. An outer measure only satisfies countable SUBadditivity: μ*(⋃Aₙ) ≤ Σμ*(Aₙ). This weaker condition is exactly what allows μ* to be defined on all subsets of X — true countable additivity on all subsets of ℝ leads to contradiction (via Vitali's construction of a non-measurable set under the axiom of choice)."

- question: "A set E has the property that for every test set T ⊆ X, μ*(T) = μ*(T ∩ E) + μ*(T ∩ Eᶜ). What does Carathéodory's theorem conclude?"
  type: multiple-choice
  options:
    - "E must be an open set, since only open sets split test sets cleanly"
    - "E is Carathéodory-measurable, and the collection of all such sets forms a σ-algebra on which μ* is countably additive"
    - "μ* is countably additive everywhere on X"
    - "The infimum-of-coverings definition of μ*(E) agrees with its geometric length"
  answer: 1
  explanation: "The splitting property — μ*(T) = μ*(T ∩ E) + μ*(T ∩ Eᶜ) for every test set T — is Carathéodory's precise criterion for measurability. It captures the idea that E has a sharp enough boundary to partition any test set without loss. Remarkably, the collection of all sets satisfying this criterion automatically forms a σ-algebra, and restricting μ* to it yields a genuine countably additive measure — not just a subadditive function."

- question: "The Carathéodory splitting property is motivated by the idea that a measurable set should not create ambiguity when used to partition any test set."
  type: true-false
  answer: true
  explanation: "This is exactly the geometric intuition. If E is 'nicely shaped,' splitting any test set T into T ∩ E and T ∩ Eᶜ should not lose any measure — the pieces should add up exactly to μ*(T). Sets that fail this property have boundaries so irregular that they create measurement ambiguity. The splitting criterion is the precise algebraic encoding of this geometric idea."

- question: "An outer measure is already a measure on all subsets of X, since it satisfies monotonicity, assigns 0 to the empty set, and is countably subadditive."
  type: true-false
  answer: false
  explanation: "Outer measure satisfies three of the four measure axioms (non-negativity, μ*(∅) = 0, monotonicity), but it is only countably SUBadditive — not countably additive. Countable additivity is what distinguishes a genuine measure from an outer measure. Carathéodory's theorem solves exactly this problem: by restricting to measurable sets via the splitting property, the outer measure becomes a genuine measure on the resulting σ-algebra."

- question: "Why can't we simply define Lebesgue measure on all subsets of ℝ, and how does Carathéodory's approach avoid this problem?"
  type: short-answer
  answer: "Vitali's theorem shows that under the axiom of choice, there exist non-measurable subsets of ℝ that cannot be assigned a consistent countably additive measure. Carathéodory's approach sidesteps this by starting with an outer measure defined on all subsets (using only subadditivity), then using the splitting property to identify the measurable sets — those whose boundaries are sharp enough not to create measurement inconsistency. The resulting σ-algebra is vast (containing all open sets, closed sets, and their countable unions and intersections), but deliberately excludes pathological sets like the Vitali set."
  explanation: "The key insight is that Carathéodory doesn't assume which sets are measurable — the splitting property discovers them. This is why the construction works: you don't need to know in advance what the measurable sets are. The non-measurable sets are precisely those that fail the splitting property, and their existence is why naive measure-of-everything is impossible."
```

## Explainer

You know from σ-algebras that a measure is defined on a carefully chosen collection of "measurable" sets, not on every subset of X. But where does that σ-algebra come from in the first place? The construction begins with a more primitive object: an **outer measure** μ*: P(X) → [0,∞], defined on *all* subsets of X, not just the nice ones. The cost of this generality is that μ* is only **countably subadditive** — μ*(⋃Aₙ) ≤ Σμ*(Aₙ) — rather than countably additive. You give up equality in exchange for universality.

The standard way to build an outer measure is from below: for any set E, define μ*(E) = inf{Σμ(Aₙ) : E ⊆ ⋃Aₙ}, where the Aₙ come from some generating collection (like open intervals) with known lengths. The **infimum** of all covering costs is precisely the "outer approximation" of the size of E — which connects to your prerequisite on suprema and infima. For a single interval (a,b), covering it by itself gives μ*(a,b) ≤ b−a, and any cover cannot do better, so μ*(a,b) = b−a. This is the intuition: outer measure recovers the right answer on simple sets.

**Carathéodory's theorem** solves the key problem: which sets can be assigned a *genuine* measure (one that is actually additive, not just subadditive)? Carathéodory's criterion says E is **measurable** if for every test set T, we have μ*(T) = μ*(T ∩ E) + μ*(T ∩ Eᶜ). This is the **splitting property**: a set E is measurable precisely when it splits every test set T additively. Geometrically, E has a "sharp enough" boundary that it doesn't create measurement ambiguity. The remarkable fact is that the collection of all measurable sets automatically forms a σ-algebra, and the restriction of μ* to this σ-algebra is countably additive — a genuine measure.

Why does this matter? Because it gives a complete construction of **Lebesgue measure** without assuming from the outset what the measurable sets are. Start with interval lengths, build the outer measure via coverings, and let Carathéodory's criterion identify which sets are measurable. The resulting σ-algebra turns out to contain all open and closed sets, all countable unions and intersections of these, and far more — essentially everything you would want to measure. The non-measurable sets (like the Vitali set) are exactly those that fail the splitting property, and their existence is precisely why we cannot naively assign a size to every subset of ℝ.
