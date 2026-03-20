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
stage: advanced
status: draft
---

# Lebesgue Outer Measure on ℝⁿ

## Core Idea
Lebesgue outer measure on ℝⁿ is defined as λ*(A) = inf{Σᵢ vol(Iᵢ) : A ⊆ ∪ᵢ Iᵢ}, where the infimum is over countable covers by open intervals. Applying Carathéodory's theorem yields the Lebesgue measure.

## Explainer

The motivating problem is deceptively simple: how do you assign a "size" to an arbitrary subset of ℝⁿ? For intervals and rectangles this is obvious — length, area, volume. But what about a dense countable set like the rationals? Or a Cantor set? The naive approach of summing lengths breaks down quickly on exotic sets, and Banach-Tarski-type paradoxes show that no measure can consistently assign a size to every subset of ℝⁿ. The Lebesgue outer measure is the response: define a notion of size for all sets, accepting that it will only be a true "measure" on a restricted class of well-behaved sets.

The definition of **Lebesgue outer measure** is: λ*(A) is the infimum of the total volume of all countable collections of open boxes that cover A. Think of it as approximating A from the outside — you are asking, "what is the least total volume I need if I'm allowed to cover A with as many (possibly overlapping) open boxes as I like?" The infimum ensures you are finding the tightest such approximation. For an interval [a, b], this gives b − a exactly, matching your intuition. For a single point, every cover can be made arbitrarily small, so the outer measure is 0. For a countable set of points, the same argument shows outer measure 0, even though such a set can be dense.

This construction is defined for every subset of ℝⁿ — it never fails to produce a value. But outer measure is not additive in general: λ*(A ∪ B) ≤ λ*(A) + λ*(B) (subadditivity holds), but equality for disjoint sets can fail for pathological A and B. This is where your prerequisite, the **Carathéodory extension theorem**, becomes essential. Carathéodory's criterion identifies exactly which sets E are "measurable" — those for which λ*(A) = λ*(A ∩ E) + λ*(A ∩ Eᶜ) for every test set A. Measurable sets split any test set into two non-interacting pieces, guaranteeing genuine additivity.

The **Lebesgue measure** is the restriction of λ* to the class of Carathéodory-measurable sets. By applying the Carathéodory extension theorem to λ*, you inherit all the good properties: countable additivity, completeness (subsets of null sets are measurable), and agreement with volume on rectangles. The outer measure plays the role of a pre-measure defined on all sets; the Carathéodory condition is the selection mechanism that picks out the σ-algebra on which it behaves properly. This is why the two ideas are sequential: you need the outer measure to exist everywhere before Carathéodory can select the measurable subcollection.
