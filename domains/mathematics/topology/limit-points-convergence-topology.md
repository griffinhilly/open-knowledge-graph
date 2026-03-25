---
id: limit-points-convergence-topology
title: Limit Points and Convergence
domain: mathematics
course: topology
prerequisites:
- id: neighborhoods-in-topology
  type: hard
- id: limit-points-topology-definition
  type: soft
- id: convergence-in-topology
  type: soft
builds-toward:
- hausdorff-spaces
- sequential-compactness
tags:
- limit-points
- convergence
- accumulation-points
stage: advanced
status: validated
---
# Limit Points and Convergence

## Core Idea
A point x is a limit point of a set A if every neighborhood of x contains points of A other than x itself. Convergence generalizes the real-line notion: a sequence converges to x if for every neighborhood of x, all but finitely many terms lie in that neighborhood. In general topological spaces, limits may not be unique, which is addressed by separation axioms.

## Questions

```yaml
- question: "In the indiscrete topology on X = {1, 2, 3} — where the only open sets are ∅ and X — the constant sequence (1, 1, 1, ...) converges to:"
  type: multiple-choice
  options:
    - "Only the point 1, since all terms equal 1"
    - "All three points 1, 2, and 3 simultaneously — the only neighborhood of any point is all of X, which every term trivially belongs to"
    - "No point — the sequence is eventually constant and does not truly approach a limit"
    - "Points 1 and 2 but not 3, since 3 is furthest from the terms"
  answer: 1
  explanation: "In the indiscrete topology, the only open set containing any point is X itself. The convergence definition requires that for every open neighborhood U of x, all but finitely many terms lie in U. Since the only neighborhood of every point is X, every term of every sequence trivially lies in it — so every sequence converges to every point simultaneously. This is the canonical example of why limits are not unique in general topological spaces, and why Hausdorff spaces (where any two distinct points have disjoint open neighborhoods) are needed to restore uniqueness."

- question: "Let A = {1/n : n ∈ ℕ} = {1, 1/2, 1/3, 1/4, ...} with the standard topology on ℝ. Which correctly identifies the limit points of A?"
  type: multiple-choice
  options:
    - "All elements of A are limit points, since they belong to the set"
    - "Only 0 is a limit point — every neighborhood of 0 contains infinitely many points of A other than 0, while each 1/n is isolated in A"
    - "The set has no limit points because A is countable"
    - "Every real number is a limit point of A since A is an infinite set"
  answer: 1
  explanation: "Being in a set and being a limit point are different things. Each point 1/n is isolated in A: the open interval (1/n − ε, 1/n + ε) for small enough ε contains no other point of A (since consecutive terms 1/n and 1/(n+1) have positive separation). So no element of A is a limit point of A. The point 0 is not in A but is a limit point: any neighborhood of 0, however small, contains 1/n for all sufficiently large n — infinitely many points of A. The closure of A is A ∪ {0}."

- question: "In any topological space, if a sequence converges to x and also to y, then x = y."
  type: true-false
  answer: false
  explanation: "This holds in Hausdorff spaces but fails in general. In a non-Hausdorff space — such as the indiscrete topology on any set with more than one point — limits are severely non-unique: every sequence converges to every point simultaneously. The Hausdorff condition precisely ensures that distinct points have disjoint open neighborhoods, which forces any convergent sequence to eventually stay in one neighborhood and out of the other, preventing it from converging to both points at once. Limit uniqueness is not a logical necessity — it is a topological property that must be imposed."

- question: "A set S in a topological space is closed if and only if it contains all of its limit points."
  type: true-false
  answer: true
  explanation: "This is one of the equivalent characterizations of closed sets in a topological space, and it provides a neighborhood-based definition of closedness that works without distances. A set is closed iff its complement is open. If S contains all its limit points, any point outside S has a neighborhood disjoint from S (otherwise it would be a limit point), so the complement is open — S is closed. Conversely, if S is closed and x is a limit point of S, any neighborhood of x meets S, so x cannot be in the open complement — x must be in S. The closure of S is then precisely S together with all its limit points."

- question: "Why does the definition of a limit point of a set A require that every neighborhood of x contains a point of A *other than x itself*, and what goes wrong if we drop this condition?"
  type: short-answer
  answer: "Without the 'other than x' clause, every point of A would automatically qualify as a limit point of A — just because the neighborhood contains x itself. This would collapse the distinction between a point being isolated in A (belonging to A but having a neighborhood that misses all other points of A) and being a genuine accumulation point (having every neighborhood intersect A in other points). With the condition, isolated points — like the element 0 in A = {0} ∪ (1, 2) — are correctly excluded from the limit points, allowing the concept to capture genuine accumulation behavior."
  explanation: "The 'other than x' clause ensures that being a limit point is a property about the *surrounding* elements of A, not just x's own membership. It separates isolated points (which belong to A but are surrounded by a gap) from limit points (which A's elements approach from outside). This distinction is essential for computing closures, characterizing closed sets, and analyzing convergence — for example, in proving that a set is closed iff its complement is open, the argument depends critically on limit points being genuinely accumulating, not just present."
```

## Explainer

You know what a neighborhood is in a topological space: an open set containing a point. Now we use neighborhoods to generalize two fundamental concepts from real analysis — limit points and sequence convergence — to arbitrary topological spaces. The key move is replacing "within ε of x" with "in every neighborhood of x," which works in any topological space, not just metric ones.

A point x is a **limit point** (also called an accumulation point) of a set A if every neighborhood of x contains at least one point of A *other than x itself*. The "other than x" clause is essential: it excludes isolated points that happen to be in A. Consider A = {0} ∪ (1, 2) in ℝ. The point 0 is isolated in A — the neighborhood (−0.5, 0.5) contains no other point of A — so 0 is not a limit point of A. But every point in the closed interval [1, 2] is a limit point of A: any neighborhood of such a point intersects (1, 2) in a nonempty open interval containing infinitely many points. The **closure** of A is then A together with all its limit points; a set is closed if and only if it contains all of its limit points. This gives a purely neighborhood-based way to compute closures without invoking distances.

**Convergence** in a topological space takes the same neighborhood approach: a sequence (xₙ) converges to x if for every open neighborhood U of x, there exists N such that xₙ ∈ U for all n > N. In a metric space, this reduces exactly to the standard ε definition (let U = B(x, ε)). But in a general topological space, a striking pathology can occur: limits need not be unique. In the **indiscrete topology** (where the only open sets are ∅ and X itself), every sequence converges to every point simultaneously, because the only neighborhood of any point is all of X, which trivially contains every term. This seems absurd, and it is — which is why **Hausdorff spaces** (T₂ spaces) are so important: a space is Hausdorff if any two distinct points have disjoint open neighborhoods, and in a Hausdorff space limits are always unique. The progression from general spaces to Hausdorff spaces mirrors the progression from pathological to well-behaved, and most spaces arising in practice are Hausdorff.
