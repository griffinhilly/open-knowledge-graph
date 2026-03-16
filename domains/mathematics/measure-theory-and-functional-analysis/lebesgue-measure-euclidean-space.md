---
id: lebesgue-measure-euclidean-space
title: Lebesgue Measure on ℝⁿ
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-measure-real-line
  type: hard
builds-toward:
- product-measures-fubini-theorem
tags:
- lebesgue-measure
stage: advanced
status: draft
---

# Lebesgue Measure on ℝⁿ

## Core Idea
Lebesgue measure on ℝⁿ extends the one-dimensional measure via product measure, assigning volume to measurable sets. Lower-dimensional sets (lines, planes) have measure zero, reflecting that they are 'negligible' in the higher-dimensional space.

## Explainer

You already understand Lebesgue measure on ℝ — it assigns a "length" to subsets of the real line in a way that extends the intuitive notion of length for intervals while handling pathological sets. The key move in building Lebesgue measure on ℝⁿ is to apply that same idea dimensionally: start with **product measure**. In ℝ², the natural way to measure a rectangle [a, b] × [c, d] is as its width times its height: (b − a)(d − c). The Lebesgue measure on ℝ² is the unique measure that assigns exactly this value to rectangles and extends to all measurable sets via the product construction.

The formal mechanism is Carathéodory's extension theorem applied to the product σ-algebra. But the geometric intuition is accessible: just as you built the Lebesgue σ-algebra on ℝ by starting with intervals and closing under countable unions and complements, the Lebesgue σ-algebra on ℝⁿ starts with n-dimensional rectangles (products of intervals) and closes under the same operations. The measure λₙ(A) that results agrees with your intuitions — the unit cube [0,1]ⁿ has measure 1, a ball of radius r in ℝ³ has volume (4/3)πr³, and so on.

The most conceptually important feature of higher-dimensional Lebesgue measure is the **measure-zero phenomenon**: a set can be geometrically rich in one sense while being completely negligible from the standpoint of integration in a higher-dimensional space. A line in ℝ² has λ₂-measure zero. A plane in ℝ³ has λ₃-measure zero. More generally, any k-dimensional set (k < n), including smooth curves and surfaces, has **λₙ-measure zero**. The intuition: a lower-dimensional set has no "n-dimensional thickness," so it occupies no fraction of n-dimensional volume, no matter how it is oriented or how large it is.

This measure-zero fact is not merely aesthetic — it is operationally decisive. When you integrate over ℝⁿ, you can ignore what a function does on any set of measure zero without changing the integral. Changing the value of a function on a line, a surface, or even a countable dense set does not affect a Lebesgue integral. This is the precision behind the measure-theoretic notion of "almost everywhere," and it is what makes Lebesgue integration robust in ways that Riemann integration is not.
