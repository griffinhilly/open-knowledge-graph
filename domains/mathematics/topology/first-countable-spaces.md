---
id: first-countable-spaces
title: First Countable Spaces
domain: mathematics
course: topology
prerequisites:
- id: neighborhood-basis-topology
  type: hard
builds-toward:
- metrization-theorems
- sequential-compactness
tags:
- countability
- first-countable
stage: formal-systems
status: draft
---

# First Countable Spaces

## Core Idea
A space is first countable if every point has a countable neighborhood basis. Metric spaces are first countable. First countability makes topology characterizable by sequences.

## How It's Best Learned
Verify that metric spaces are first countable (use balls of rational radius). Find a non-first-countable space: the cocountable topology on an uncountable set. Check which topological properties are preserved under first countability.

## Common Misconceptions
- Confusing first countable with second countable (having a countable basis for the whole topology, not just at each point).
- Assuming first countability is trivial; many natural spaces like function spaces with the product topology fail it.
- Thinking sequences always characterize topology; they do in first-countable spaces, but not in general.

## Explainer

From your work on neighborhood bases, you know that a **neighborhood basis** at a point x is a collection of neighborhoods of x such that every neighborhood of x contains at least one member of the collection. The basis provides a "reference library" of neighborhoods you can use to check any topological property involving x — instead of quantifying over all neighborhoods, you only need to check the basis elements. A space is **first countable** if every point has a neighborhood basis that is *countable*, meaning you can index the basis elements as B₁, B₂, B₃, ….

The canonical example is any metric space. At a point x in a metric space, the open balls {y : d(x, y) < 1/n} for n = 1, 2, 3, … form a countable neighborhood basis. Any open set containing x must contain one of these balls (since open sets contain an open ball around each of their points), so this countable collection is sufficient. This is why all of real analysis — which happens in ℝⁿ, a metric space — can be carried out entirely with sequences. Whenever you want to verify that a point is a limit or that a function is continuous at x, you can test with sequential neighborhoods of shrinking radius.

The payoff of first countability is that **sequences suffice to detect topology**. In a general topological space, sequences are too coarse — a point can be in the closure of a set without any sequence from that set converging to it. But in first-countable spaces, closure is exactly characterized by sequential limits: x ∈ cl(A) if and only if some sequence in A converges to x. Similarly, a function f : X → Y between first-countable spaces is continuous at x if and only if for every sequence xₙ → x in X, f(xₙ) → f(x) in Y. These sequential characterizations are what make metric-space analysis feel intuitive — they're the first-countability axiom doing work.

Without first countability, sequences can mislead. The function space ℝ^ℝ with the product topology is not first countable at any point, and there are sets whose closures cannot be detected by sequences alone — you need **nets** or **filters**, which are more general convergence notions. First countability marks the boundary between the sequential world of metric spaces and the more exotic behavior of general topology. Spaces built from uncountable products, certain quotient constructions, or the cocountable topology often fail it, and when they do, sequential intuition breaks down.

