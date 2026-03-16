---
id: introduction-lebesgue-measure
title: Introduction to Lebesgue Measure
domain: mathematics
course: real-analysis
prerequisites:
- id: compact-sets
  type: hard
- id: open-sets-real-line
  type: hard
builds-toward:
- introduction-lebesgue-integral
tags:
- lebesgue-measure
- measure-theory
- advanced
stage: advanced
status: draft
---

# Introduction to Lebesgue Measure

## Core Idea
Lebesgue measure extends the notion of length to more general sets than intervals. It assigns a non-negative measure to sets in σ-algebra on ℝ, generalizing length of intervals. Lebesgue measure has better properties than Riemann integrability: it handles arbitrary unions of open sets, and a set has measure zero if it can be covered by countably many intervals of arbitrarily small total length. This foundation enables the Lebesgue integral to integrate a much wider class of functions.

## Explainer

You already know that open sets on the real line are unions of open intervals, and that compact sets are closed and bounded subsets of ℝ. Now the question becomes: can we consistently assign a "length" to *any* set, not just intervals or simple combinations of them? The Riemann integral works by partitioning the *domain* into intervals, and for most functions this is enough. But there are natural sets — like the rational numbers in [0,1] — that are dense everywhere yet contain "almost nothing." The **Lebesgue measure** is the tool that makes this intuition precise.

The construction begins with a simple idea: a set E ⊆ ℝ has **outer measure** m*(E) equal to the infimum of the total length of all countable collections of open intervals that cover E. For an interval, this recovers ordinary length. For a single point or any countable set, it gives zero — because you can cover a countable collection of points with intervals of total length ε for any ε > 0. A set has **measure zero** when this infimum is 0, meaning the set is "negligibly small" in a size sense even if it is infinitely dense, like ℚ. This is the key concept that unlocks integration theory: events or sets of measure zero don't affect integration.

Not every subset of ℝ is **Lebesgue measurable** — there exist (assuming the axiom of choice) bizarre sets with no sensible length. The measurable sets form a **σ-algebra**: a collection closed under countable unions, countable intersections, and complements. Every open set, every closed set, and in particular every compact set you studied is measurable. Within this σ-algebra, Lebesgue measure satisfies **countable additivity**: the measure of a countable disjoint union is the sum of the individual measures. This property, which the Riemann approach cannot provide in full generality, is what makes modern analysis work.

The practical punchline is the notion of "almost everywhere." A property holds **almost everywhere** (a.e.) if it fails only on a set of measure zero. Two functions that differ on a set of measure zero behave identically for integration purposes. This is why the Lebesgue integral can handle the indicator function of the rationals — which is nowhere Riemann integrable — with ease: the rationals have measure zero, so the function is zero almost everywhere, and its integral is zero. This foundation, built on open sets and compact sets you already know, will enable a far more powerful and flexible theory of integration.


