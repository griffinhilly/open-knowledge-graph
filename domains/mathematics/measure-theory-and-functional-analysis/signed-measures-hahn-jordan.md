---
id: signed-measures-hahn-jordan
title: Signed Measures and Hahn-Jordan Decomposition
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: radon-nikodym-theorem
  type: hard
tags:
- measure-theory
stage: advanced
status: draft
---

# Signed Measures and Hahn-Jordan Decomposition

## Core Idea
A signed measure ν: F → ℝ is countably additive but can take negative values. Every signed measure decomposes uniquely as ν = ν⁺ - ν⁻ (Hahn-Jordan), where ν⁺, ν⁻ are mutually singular positive measures.

## Explainer

Standard measures assign nonnegative sizes to sets. A **signed measure** relaxes this: sets can have negative measure, representing a net quantity that allows cancellation. The motivating example is a difference of two ordinary measures: if μ and ν are both positive measures, then ν - μ is a signed measure. The Hahn-Jordan decomposition theorem says this is essentially the only structure — every signed measure is the difference of two positive measures, and the decomposition is unique under the constraint of mutual singularity.

The **Hahn decomposition** partitions the underlying space X into a positive set P (where ν assigns nonneg­ative values to all subsets) and a negative set N = Pᶜ (where ν assigns nonpositive values to all subsets). Think of it as dividing X into a net-positive region and a net-negative region. This partition is essentially unique up to null sets — the decomposition reflects an intrinsic property of ν rather than an arbitrary choice.

From the Hahn decomposition, the **Jordan decomposition** follows immediately: define ν⁺(E) = ν(E ∩ P) and ν⁻(E) = −ν(E ∩ N). Both ν⁺ and ν⁻ are positive measures, they are **mutually singular** (ν⁺ concentrates on P, ν⁻ on N, which are disjoint), and ν = ν⁺ − ν⁻. The **total variation** |ν| = ν⁺ + ν⁻ is the signed-measure analogue of the absolute value — it measures total mass, positive and negative combined.

Your prerequisite, the Radon-Nikodym theorem, tells you when a measure is absolutely continuous with respect to another, producing a density function dν/dμ. Signed measures extend this naturally: the Radon-Nikodym derivative dν/dμ can itself be a real-valued function that takes negative values on some sets. The Jordan decomposition then corresponds to decomposing dν/dμ into its positive and negative parts as a function. This bridge between signed measures and signed densities is what makes the decomposition analytically useful — it reduces measure-theoretic questions to real-variable ones.
