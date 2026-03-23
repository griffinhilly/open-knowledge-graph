---
id: hausdorff-spaces
title: Hausdorff Spaces
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms-t0-t1-t2
  type: hard
builds-toward:
- compactness-hausdorff-spaces
- metrization-theorems
tags:
- hausdorff
- t2-axiom
- separated
stage: advanced
status: validated
---

# Hausdorff Spaces

## Core Idea
A Hausdorff space (T₂ space) requires any two distinct points to have disjoint open neighborhoods. This is the most commonly studied separation axiom and appears throughout analysis and topology. In Hausdorff spaces, sequences have unique limits, singleton sets are closed, and compact subsets are closed.

## Questions

```yaml
- question: "In a topological space X, a sequence (xₙ) converges to both x and y, where x ≠ y. Which conclusion must follow?"
  type: multiple-choice
  options:
    - "X must be disconnected, since x and y must lie in separate components"
    - "X is not compact, since compact spaces always have unique limits"
    - "X is not a Hausdorff space, since the Hausdorff condition guarantees uniqueness of sequential limits"
    - "X must be finite, since infinite spaces always separate distinct points"
  answer: 2
  explanation: "Uniqueness of sequential limits is a direct consequence of the Hausdorff condition. If X were Hausdorff and (xₙ) converged to both x and y with x ≠ y, take disjoint neighborhoods U of x and V of y. Convergence to x means xₙ ∈ U eventually; convergence to y means xₙ ∈ V eventually. But U ∩ V = ∅, a contradiction. So any space where a sequence converges to two distinct points cannot be Hausdorff. Compactness and connectedness are independent properties that do not alone guarantee unique limits."

- question: "Let K be a compact subset of a Hausdorff space X, and let y be a point not in K. Which of the following is guaranteed by the Hausdorff condition combined with compactness?"
  type: multiple-choice
  options:
    - "K and {y} are contained in disjoint open sets — so y has an open neighborhood entirely disjoint from K"
    - "y must be isolated, meaning {y} is an open set in X"
    - "The union K ∪ {y} is also compact in X"
    - "No sequence in K can have y as a cluster point"
  answer: 0
  explanation: "For each k ∈ K, the Hausdorff condition gives disjoint open sets Uₖ ∋ y and Vₖ ∋ k. The sets {Vₖ} cover K. By compactness, finitely many suffice: V_{k₁}, …, V_{kₙ} cover K. Then U = U_{k₁} ∩ … ∩ U_{kₙ} is an open neighborhood of y disjoint from V_{k₁} ∪ … ∪ V_{kₙ} ⊇ K. This proves that compact subsets of Hausdorff spaces are closed — every exterior point has a neighborhood missing K. This interplay between Hausdorff and compactness is one of the central theorems of topology."

- question: "Every metric space is a Hausdorff space, because distinct points at distance d > 0 can always be separated by open balls of radius d/2, which are disjoint by the triangle inequality."
  type: true-false
  answer: true
  explanation: "Given distinct points x and y with d(x,y) = d > 0, let U = B(x, d/2) and V = B(y, d/2). If any point z were in both, then d(x,y) ≤ d(x,z) + d(z,y) < d/2 + d/2 = d, contradicting d(x,y) = d. So U and V are disjoint open neighborhoods separating x and y, confirming the Hausdorff condition. This means all spaces studied in classical analysis — ℝⁿ, normed spaces, manifolds — are automatically Hausdorff."

- question: "In any T₁ topological space (where every singleton {x} is closed), sequences have unique limits."
  type: true-false
  answer: false
  explanation: "T₁ is strictly weaker than T₂ (Hausdorff), and T₁ alone does not guarantee unique limits. Counterexample: ℝ with the cofinite topology (open sets are ∅ and sets with finite complement) is T₁, since the complement of {x} is cofinite, hence open. But every sequence of distinct points converges to every point in ℝ: any open neighborhood of any point excludes only finitely many elements, so the sequence is eventually in every open set. Unique limits require the Hausdorff condition — the ability to separate two distinct limit points by disjoint open sets."

- question: "Explain, using the definition of a Hausdorff space, why a sequence in a Hausdorff space cannot converge to two distinct limits."
  type: short-answer
  answer: "Suppose (xₙ) in a Hausdorff space X converges to both x and y, with x ≠ y. By the Hausdorff condition, there exist disjoint open sets U and V with x ∈ U and y ∈ V. Since xₙ → x, all but finitely many terms lie in U. Since xₙ → y, all but finitely many terms lie in V. But U ∩ V = ∅, so no term can lie in both — a contradiction. Therefore x = y."
  explanation: "This proof uses the Hausdorff condition precisely: disjoint neighborhoods of x and y let both convergence assumptions fight each other into a contradiction. In a non-Hausdorff space, x and y cannot be separated, so their neighborhoods overlap and the sequence can 'converge' to both simultaneously. Unique limits are what make Hausdorff spaces behave like the real line and other spaces in classical analysis — this is why Hausdorff is the default assumption in most of topology and geometry."
```

## Explainer

From your study of separation axioms, you know there is a hierarchy of ways a topological space can "separate" its points: T₀ asks that for any two distinct points, at least one has a neighborhood not containing the other; T₁ asks that each point can be separated from every other point by some open set; T₂ — the **Hausdorff condition** — asks for something stronger: any two distinct points have *disjoint* open neighborhoods. This is the condition that makes topology behave like the geometry you already know from analysis on ℝ.

The Hausdorff condition can be stated visually: if x ≠ y, you can "separate" them with open sets — find U ∋ x and V ∋ y such that U ∩ V = ∅. Every metric space is Hausdorff: given distinct points x and y at distance d > 0, take open balls of radius d/2 around each. These balls are disjoint by the triangle inequality. So all of the spaces from analysis — ℝⁿ, function spaces with norms, manifolds — are automatically Hausdorff. The Hausdorff condition is interesting precisely for spaces that might fail it, such as certain spaces in algebraic geometry or the quotient topologies that arise when you identify points together carelessly.

The most important consequence of the Hausdorff condition in analysis is **uniqueness of limits**. In a non-Hausdorff space, a sequence can converge to two different points simultaneously — because there is no way to isolate the two limit points from each other. In a Hausdorff space, this cannot happen: if x_n → x and x_n → y, then x = y. The proof uses the Hausdorff condition directly: if x ≠ y, take disjoint neighborhoods U of x and V of y; eventually the sequence must lie entirely in U (by convergence to x) and eventually entirely in V (by convergence to y), but U ∩ V = ∅, a contradiction. From this it follows that singletons {x} are closed in any T₁ space, and in particular in any Hausdorff space.

A crucial theorem linking Hausdorff spaces to compactness is: **in a Hausdorff space, every compact subset is closed**. The proof constructs, for any point y outside a compact set K, a neighborhood of y disjoint from K — using the Hausdorff condition to separate y from each point of K, then using compactness to extract a finite subcover. This interplay between Hausdorff and compactness is one of the central engines of topology: it explains why compact Hausdorff spaces have such clean and complete theory, and it sets up the study of compactification and metrization theorems you will encounter next.
