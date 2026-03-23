---
id: heine-borel-compact-sets
title: Heine-Borel Theorem
domain: mathematics
course: topology
prerequisites:
- id: compact-sets-definition
  type: hard
- id: compact-sets-heine-borel
  type: soft
builds-toward:
- compactness-hausdorff-spaces
tags:
- compactness
- characterization
stage: advanced
status: validated
---

# Heine-Borel Theorem

## Core Idea
In ℝⁿ with standard topology, a set is compact iff it is closed and bounded. This theorem does not generalize to all metric spaces (e.g., [0,∞) is closed but not compact), showing that compactness is truly a topological concept, not merely about boundedness.

## Questions

```yaml
- question: "Consider the closed unit ball B = {f ∈ C([0,1]) : ‖f‖∞ ≤ 1} in the space of continuous functions with the supremum norm. Is B compact?"
  type: multiple-choice
  options:
    - "Yes — it is closed and bounded, so Heine-Borel applies"
    - "Yes — all closed and bounded sets in metric spaces are compact"
    - "No — Heine-Borel only applies to ℝⁿ, and B has no convergent subsequences for all sequences in it"
    - "No — B is not bounded in the sup norm"
  answer: 2
  explanation: "This is the central counterexample. C([0,1]) with the sup norm is an infinite-dimensional space, and Heine-Borel does NOT apply there. B is closed and bounded, yet it fails to be compact — one can construct sequences of continuous functions in B (e.g., fₙ(x) = sin(nπx)) with no uniformly convergent subsequence. Compactness is a topological property, not a geometric one, and 'closed and bounded' characterizes it only in finite-dimensional Euclidean space."

- question: "Which of the following subsets of ℝ is compact?"
  type: multiple-choice
  options:
    - "(0, 1) — bounded but not closed"
    - "[0, ∞) — closed but not bounded"
    - "ℤ — closed but not bounded"
    - "[−3, 7] — closed and bounded"
  answer: 3
  explanation: "By Heine-Borel, a subset of ℝ is compact iff it is both closed and bounded. [−3, 7] satisfies both conditions. (0,1) fails closure (limit point 0 is absent). [0,∞) fails boundedness. ℤ is closed but unbounded — every open cover {(n−0.1, n+0.1)} has no finite subcover. Only option D satisfies both required conditions."

- question: "Every closed and bounded subset of a metric space is compact."
  type: true-false
  answer: false
  explanation: "This is false in general metric spaces. Heine-Borel is a theorem specific to ℝⁿ with its standard topology. In infinite-dimensional normed spaces (like C([0,1])), or even in some metric spaces on countable sets, you can have closed and bounded sets that fail to be compact. The theorem's scope is a crucial part of its content — over-generalizing it is a common and consequential error."

- question: "The open interval (0, 1) in ℝ fails to be compact because it is not closed, even though it is bounded."
  type: true-false
  answer: true
  explanation: "Correct. (0,1) is bounded but not closed — it is missing its limit points 0 and 1. Concretely, the open cover {(1/n, 1) : n ≥ 2} has no finite subcover, because any finite subcollection leaves a neighborhood of 0 uncovered. Closedness is necessary for compactness in ℝⁿ because it ensures limit points (the 'endpoints' where sequences might escape) are included in the set."

- question: "Why does 'closed and bounded' guarantee compactness in ℝⁿ but not in general metric spaces? What property of ℝⁿ makes the theorem work?"
  type: short-answer
  answer: "In ℝⁿ, bounded sets can always be enclosed in a finite closed box (via the Bolzano-Weierstrass theorem, every bounded sequence has a convergent subsequence), and closed subsets of compact sets are compact. These properties hold because ℝⁿ is finite-dimensional. In infinite-dimensional spaces, boundedness no longer forces sequential compactness — you can have bounded sequences with no convergent subsequence — so the two geometric conditions are no longer sufficient for the topological property."
  explanation: "The key is finite-dimensionality. In ℝⁿ, Bolzano-Weierstrass guarantees that bounded sequences have convergent subsequences, tying sequential compactness to boundedness. Closedness then ensures the limit is in the set. In infinite dimensions, neither connection holds, so compactness must be verified directly from the open-cover definition or other topological criteria."
```

## Explainer

You already know the abstract definition of compactness: a space is compact if every open cover has a finite subcover. That definition is powerful but opaque — given an arbitrary set in ℝⁿ, checking every possible open cover is infeasible. The **Heine-Borel Theorem** replaces this with a concrete geometric test: in ℝⁿ with its standard topology, a set K is compact if and only if it is **closed** and **bounded**. Closed means K contains all its limit points. Bounded means K fits inside some ball of finite radius. Both conditions are straightforward to verify.

Why do both conditions matter? Bounded alone is insufficient: the open interval (0, 1) is bounded, but the open cover {(1/n, 1) : n ≥ 2} has no finite subcover — the left endpoint 0 is the problem, and it's a limit point missing from the set. Closed alone is also insufficient: the entire real line ℝ is closed, but cover it with open intervals (−n, n) for n = 1, 2, 3, …; no finite subcollection covers all of ℝ. The combination — closed and bounded — is what traps sequences and covers simultaneously: boundedness prevents escape to infinity, and closedness ensures limit points are included.

The proof strategy illustrates the deep connection to Bolzano-Weierstrass. One direction (compact → closed and bounded) is relatively easy: compactness implies sequential compactness, which forces the set to contain its limit points (hence closed) and prohibits sequences escaping to infinity (hence bounded). The other direction (closed and bounded → compact) proceeds by enclosing K in a large closed box, showing the box is compact via iterated bisection, and noting that K as a closed subset of a compact set is itself compact.

The theorem's scope is limited to ℝⁿ, and this is no accident. In the space C([0,1]) of continuous functions with the sup norm, the closed unit ball {f : ‖f‖∞ ≤ 1} is closed and bounded but not compact — you can construct sequences of continuous functions with no convergent subsequence. Compactness is a topological property, not a geometric one, and "closed and bounded" is a special feature of finite-dimensional Euclidean space. In higher-dimensional and infinite-dimensional settings, you must work directly from the cover definition or use sequential compactness, which is why the abstract definition was necessary to learn first.
