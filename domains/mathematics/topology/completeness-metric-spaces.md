---
id: completeness-metric-spaces
title: Completeness in Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: metric-topology
  type: hard
- id: cauchy-sequences-and-completeness
  type: hard
builds-toward:
- contraction-mapping-theorem
- baire-category-theorem
tags:
- completeness
- cauchy-sequences
- metric-spaces
stage: advanced
status: draft
---

# Completeness in Metric Spaces

## Core Idea
A metric space is complete if every Cauchy sequence converges. Completeness is a metric property (not purely topological) that guarantees existence of limits. Many important spaces are complete: ℝⁿ, closed subsets of complete spaces, and function spaces with appropriate metrics. Completeness enables powerful existence theorems in analysis.

## Explainer

From your study of Cauchy sequences, you know that a sequence is **Cauchy** if its terms become arbitrarily close to each other — without referencing any particular limit. A **complete metric space** is one in which every Cauchy sequence converges to a point that is actually *in* the space. The definition separates two things that can come apart: the internal coherence of a sequence (are its terms bunching together?) and the existence of a target (is there a point in the space for them to reach?).

The canonical example of incompleteness is the rationals ℚ with the usual metric. The sequence 1, 1.4, 1.41, 1.414, ... is Cauchy — successive terms differ by less than 10⁻ⁿ — yet it converges to √2, which is not rational. The sequence is perfectly well-behaved internally, but ℚ has a "hole" at √2. The reals ℝ are exactly the completion of ℚ: every such hole is filled. From your metric topology background, you know that a metric defines an ambient space; completeness asks whether that space has any missing points that Cauchy sequences can "fall into."

Not every topological property is preserved by completeness, and vice versa. Completeness is a **metric** property, not a purely topological one. Two homeomorphic spaces can differ in completeness: (0, 1) and ℝ are homeomorphic as topological spaces (there is a continuous bijection with continuous inverse between them), but (0, 1) with the usual metric is incomplete — the sequence 1/n is Cauchy but converges to 0, which is outside (0, 1). The real line ℝ is complete. This example shows that completeness can be broken by removing points or by choosing the "wrong" metric for a space.

The power of completeness lies in the existence theorems it enables. The **Contraction Mapping Theorem** (Banach Fixed-Point Theorem) guarantees that any contraction map on a complete metric space has a unique fixed point — a statement used in differential equations, numerical analysis, and computer science to prove iterative algorithms converge. The **Baire Category Theorem** tells you that complete metric spaces cannot be written as a countable union of nowhere-dense closed sets. Both results are impossible to state without completeness. The pattern is consistent: completeness is the hypothesis you need whenever you want to show that something you have constructed "inside" the space actually lives there. It is the guarantee that your space has no gaps for limiting objects to fall through.
