---
id: limit-points-convergence-topology
title: Limit Points and Convergence
domain: mathematics
course: topology
prerequisites:
- id: neighborhoods-in-topology
  type: hard
builds-toward:
- hausdorff-spaces
- sequential-compactness
tags:
- limit-points
- convergence
- accumulation-points
stage: advanced
status: draft
---

# Limit Points and Convergence

## Core Idea
A point x is a limit point of a set A if every neighborhood of x contains points of A other than x itself. Convergence generalizes the real-line notion: a sequence converges to x if for every neighborhood of x, all but finitely many terms lie in that neighborhood. In general topological spaces, limits may not be unique, which is addressed by separation axioms.

## Explainer

You know what a neighborhood is in a topological space: an open set containing a point. Now we use neighborhoods to generalize two fundamental concepts from real analysis — limit points and sequence convergence — to arbitrary topological spaces. The key move is replacing "within ε of x" with "in every neighborhood of x," which works in any topological space, not just metric ones.

A point x is a **limit point** (also called an accumulation point) of a set A if every neighborhood of x contains at least one point of A *other than x itself*. The "other than x" clause is essential: it excludes isolated points that happen to be in A. Consider A = {0} ∪ (1, 2) in ℝ. The point 0 is isolated in A — the neighborhood (−0.5, 0.5) contains no other point of A — so 0 is not a limit point of A. But every point in the closed interval [1, 2] is a limit point of A: any neighborhood of such a point intersects (1, 2) in a nonempty open interval containing infinitely many points. The **closure** of A is then A together with all its limit points; a set is closed if and only if it contains all of its limit points. This gives a purely neighborhood-based way to compute closures without invoking distances.

**Convergence** in a topological space takes the same neighborhood approach: a sequence (xₙ) converges to x if for every open neighborhood U of x, there exists N such that xₙ ∈ U for all n > N. In a metric space, this reduces exactly to the standard ε definition (let U = B(x, ε)). But in a general topological space, a striking pathology can occur: limits need not be unique. In the **indiscrete topology** (where the only open sets are ∅ and X itself), every sequence converges to every point simultaneously, because the only neighborhood of any point is all of X, which trivially contains every term. This seems absurd, and it is — which is why **Hausdorff spaces** (T₂ spaces) are so important: a space is Hausdorff if any two distinct points have disjoint open neighborhoods, and in a Hausdorff space limits are always unique. The progression from general spaces to Hausdorff spaces mirrors the progression from pathological to well-behaved, and most spaces arising in practice are Hausdorff.
