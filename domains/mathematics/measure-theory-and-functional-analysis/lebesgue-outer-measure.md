---
id: lebesgue-outer-measure
title: Lebesgue Outer Measure on ℝⁿ
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: caratheodory-extension-theorem
  type: hard
builds-toward:
- lebesgue-measure-real-line
tags:
- measure-theory
- lebesgue-measure
stage: expert
status: validated
---

# Lebesgue Outer Measure on ℝⁿ

## Core Idea
Lebesgue outer measure on ℝⁿ is defined as λ*(A) = inf{Σᵢ vol(Iᵢ) : A ⊆ ∪ᵢ Iᵢ}, where the infimum is over countable covers by open intervals. Applying Carathéodory's theorem yields the Lebesgue measure.

## Questions

```yaml
- question: "The Lebesgue outer measure λ* is defined for every subset of ℝⁿ, yet it is not a 'measure' in the technical sense. The reason is:"
  type: multiple-choice
  options:
    - "It fails to assign finite values to bounded sets"
    - "It is not countably additive — for pathological disjoint sets A and B, λ*(A ∪ B) < λ*(A) + λ*(B) can occur"
    - "It violates countable subadditivity — λ*(∪ᵢ Aᵢ) can exceed Σᵢ λ*(Aᵢ)"
    - "It does not assign zero measure to the empty set"
  answer: 1
  explanation: "Outer measure satisfies countable subadditivity (λ*(∪ᵢ Aᵢ) ≤ Σᵢ λ*(Aᵢ)) but not countable additivity. For carefully constructed pathological sets — the kind Banach-Tarski-type constructions use — disjoint sets can fail to have λ*(A ∪ B) = λ*(A) + λ*(B). This failure of additivity is why outer measure alone is not a measure; the Carathéodory condition identifies the subclass of sets on which additivity holds."

- question: "A student argues: 'Lebesgue outer measure and Lebesgue measure are the same thing — both defined on all subsets of ℝⁿ.' What is the key error?"
  type: multiple-choice
  options:
    - "The student is correct; they are defined identically on all subsets"
    - "Outer measure is defined on all subsets but lacks additivity; Lebesgue measure is its restriction to the Carathéodory-measurable sets, where countable additivity holds — these are different objects with different domains"
    - "Lebesgue measure is defined only on intervals, not all subsets"
    - "Outer measure is strictly larger than Lebesgue measure on every set"
  answer: 1
  explanation: "This conflation is the central misconception. Outer measure λ* is defined universally (on all subsets) as the infimum of box covers — this universality is necessary for the Carathéodory criterion to function. But λ* is not additive on all subsets. Lebesgue measure is the restriction of λ* to the σ-algebra of Carathéodory-measurable sets, where additivity is guaranteed. The two are defined on different collections and have different properties."

- question: "The Lebesgue outer measure of a countable dense set (such as the rational numbers in [0,1]) is positive, because it contains infinitely many points spread throughout the interval."
  type: true-false
  answer: false
  explanation: "A countable set has outer measure zero. Each point can be enclosed in an open interval of length ε/2ⁿ; the total cover has volume at most ε × Σ(1/2ⁿ) = ε, which can be made arbitrarily small. Countability, not density, is what matters: no matter how densely packed the points are, a countable collection can always be covered by open intervals with total length approaching zero. This is one of the most counterintuitive consequences of the definition."

- question: "A set E is Carathéodory-measurable if for every test set A, λ*(A) = λ*(A ∩ E) + λ*(A ∩ Eᶜ) — that is, E correctly splits every set into non-interacting pieces."
  type: true-false
  answer: true
  explanation: "This is exactly the Carathéodory criterion. Intuitively, E is measurable if it acts like a clean partition boundary for every possible test set A — with no 'leakage' between E and its complement. When this holds, outer measure on the pieces adds correctly, and E is in the σ-algebra on which λ* is a genuine (countably additive) measure. The condition is stated for all A — including non-measurable sets — which is why outer measure must be defined universally first."

- question: "Why must Lebesgue outer measure be defined on all subsets of ℝⁿ before the Carathéodory criterion is applied, rather than defining it only on the measurable sets from the start?"
  type: short-answer
  answer: "Because the Carathéodory criterion tests whether a set E correctly splits every test set A — and A must range over all subsets, including non-measurable ones. If outer measure were only defined on the measurable sets, you couldn't evaluate the condition λ*(A) = λ*(A ∩ E) + λ*(A ∩ Eᶜ) for arbitrary A. The outer measure must exist everywhere as a preliminary construction; then Carathéodory selects the subcollection of sets on which it behaves as a genuine measure."
  explanation: "This logical ordering is non-negotiable: universality first, selection second. The outer measure is a pre-measure that sacrifices additivity for universality; the Carathéodory theorem restores additivity by restricting the domain. Understanding this order also explains why outer measure is defined via an infimum (approximation from outside) rather than some other construction — it must be computable from arbitrary sets, not just nice ones."
```

## Explainer

The motivating problem is deceptively simple: how do you assign a "size" to an arbitrary subset of ℝⁿ? For intervals and rectangles this is obvious — length, area, volume. But what about a dense countable set like the rationals? Or a Cantor set? The naive approach of summing lengths breaks down quickly on exotic sets, and Banach-Tarski-type paradoxes show that no measure can consistently assign a size to every subset of ℝⁿ. The Lebesgue outer measure is the response: define a notion of size for all sets, accepting that it will only be a true "measure" on a restricted class of well-behaved sets.

The definition of **Lebesgue outer measure** is: λ*(A) is the infimum of the total volume of all countable collections of open boxes that cover A. Think of it as approximating A from the outside — you are asking, "what is the least total volume I need if I'm allowed to cover A with as many (possibly overlapping) open boxes as I like?" The infimum ensures you are finding the tightest such approximation. For an interval [a, b], this gives b − a exactly, matching your intuition. For a single point, every cover can be made arbitrarily small, so the outer measure is 0. For a countable set of points, the same argument shows outer measure 0, even though such a set can be dense.

This construction is defined for every subset of ℝⁿ — it never fails to produce a value. But outer measure is not additive in general: λ*(A ∪ B) ≤ λ*(A) + λ*(B) (subadditivity holds), but equality for disjoint sets can fail for pathological A and B. This is where your prerequisite, the **Carathéodory extension theorem**, becomes essential. Carathéodory's criterion identifies exactly which sets E are "measurable" — those for which λ*(A) = λ*(A ∩ E) + λ*(A ∩ Eᶜ) for every test set A. Measurable sets split any test set into two non-interacting pieces, guaranteeing genuine additivity.

The **Lebesgue measure** is the restriction of λ* to the class of Carathéodory-measurable sets. By applying the Carathéodory extension theorem to λ*, you inherit all the good properties: countable additivity, completeness (subsets of null sets are measurable), and agreement with volume on rectangles. The outer measure plays the role of a pre-measure defined on all sets; the Carathéodory condition is the selection mechanism that picks out the σ-algebra on which it behaves properly. This is why the two ideas are sequential: you need the outer measure to exist everywhere before Carathéodory can select the measurable subcollection.
