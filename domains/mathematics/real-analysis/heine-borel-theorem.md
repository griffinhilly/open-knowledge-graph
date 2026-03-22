---
id: heine-borel-theorem
title: Heine-Borel Theorem
domain: mathematics
course: real-analysis
prerequisites:
- id: compact-sets
  type: hard
- id: open-sets-real-line
  type: hard
builds-toward:
- uniform-continuity-compact-sets
- extreme-value-theorem-rigorous
tags:
- heine-borel
- compactness
- closed-bounded
stage: advanced
status: draft
---

# Heine-Borel Theorem

## Core Idea
In ℝ, a set is compact if and only if it is closed and bounded. This theorem ties the abstract definition of compactness (open cover property) to the concrete notion of being contained in some bounded interval. It is specific to Euclidean space and does not hold in all metric spaces.

## Questions

```yaml
- question: "Which of the following subsets of ℝ is compact according to the Heine-Borel theorem?"
  type: multiple-choice
  options:
    - "The open interval (0, 1)"
    - "The integers ℤ"
    - "The closed interval [0, 1]"
    - "The real line ℝ"
  answer: 2
  explanation: "[0, 1] is both closed (contains all its limit points) and bounded (contained in [−2, 2]), so Heine-Borel guarantees it is compact. (0, 1) is bounded but not closed — it fails to contain the limit point 0. ℤ is closed but unbounded. ℝ is neither bounded. Both conditions are required."

- question: "In an infinite-dimensional function space such as L²([0,1]), is every closed and bounded set compact?"
  type: multiple-choice
  options:
    - "Yes — Heine-Borel applies to any complete metric space"
    - "Yes — closed and bounded always implies compact regardless of the space"
    - "No — Heine-Borel is specific to ℝⁿ and fails in infinite-dimensional spaces"
    - "No — but only because function spaces are not metric spaces"
  answer: 2
  explanation: "The Heine-Borel theorem is a special feature of ℝⁿ, not a universal truth. In infinite-dimensional normed spaces such as L², the closed unit ball is closed and bounded but not compact — it contains sequences with no convergent subsequence. The theorem's power is precisely that it collapses an infinite verification into two geometric checks, but only because ℝⁿ has just the right structure."

- question: "A closed subset of ℝ is always compact."
  type: true-false
  answer: false
  explanation: "Closedness alone is not sufficient — the set must also be bounded. The integers ℤ form a closed set (they contain all their limit points, since they have none outside the set), yet ℤ is unbounded. Any cover by open intervals of width 1 centered at each integer has no finite subcover. Both conditions — closed AND bounded — are required by Heine-Borel."

- question: "The Heine-Borel theorem fails in general metric spaces: a closed and bounded set need not be compact outside of ℝⁿ."
  type: true-false
  answer: true
  explanation: "This is a crucial limitation of the theorem. In infinite-dimensional Banach spaces, or even in unusual metric spaces, closed and bounded does not imply compact. For example, in the metric space of rationals ℚ with the standard metric, the set {q ∈ ℚ : 0 ≤ q ≤ 1} is closed and bounded in ℚ but not compact (the sequence of rational approximations to √2/2 has no rational limit in the set). Heine-Borel is a theorem about ℝⁿ specifically."

- question: "Why are both closedness and boundedness necessary for a subset of ℝ to be compact? Give a counterexample for each condition failing."
  type: short-answer
  answer: "Boundedness keeps the set from stretching to infinity; without it, you can construct an open cover that cannot be reduced to finitely many sets (e.g., cover ℤ with intervals (n−0.5, n+0.5) — no finite subcollection covers all integers). Closedness keeps the set from leaking through its boundary; without it, a sequence of points can converge to a limit outside the set, and you can cover the set with intervals that each avoid that limit (e.g., cover (0,1) with (1/n, 1) — any finite subcollection misses points near 0)."
  explanation: "Each condition blocks a different failure mode. Boundedness prevents the 'escape to infinity' failure (ℤ example). Closedness prevents the 'converging sequence escapes' failure ((0,1) example). The Heine-Borel theorem says these are the only two ways compactness can fail in ℝⁿ."
```

## Explainer

From your study of compact sets, you know the abstract definition: a set K is compact if every open cover of K has a finite subcover. This definition is powerful but hard to verify directly — you'd need to check infinitely many possible open covers. The **Heine-Borel theorem** gives you a completely checkable equivalent in ℝⁿ: a set is compact if and only if it is **closed** and **bounded**. Checking whether [0, 1] is compact just became checking two easy conditions.

To see why both conditions are necessary, consider what happens when you drop one. The open interval (0, 1) is bounded but not closed — the sequence 1/n converges to 0, which is outside the set, so the set fails to contain all its limit points. You can build an open cover of (0, 1) that has no finite subcover: take Uₙ = (1/n, 1) for n = 1, 2, 3, …. Every point in (0, 1) is eventually covered, but any finite subcollection only covers points above some positive lower bound, missing points near 0. Now consider ℤ (the integers): closed but not bounded. Take the cover of singletons {n−1, n+1} for each n ∈ ℤ — each integer is covered, but removing any element of the cover leaves one integer uncovered, so no finite subcover exists. Boundedness keeps the set from stretching to infinity; closedness keeps it from leaking through its boundary.

The proof of the theorem in ℝ uses two tools you've seen: the **Bolzano-Weierstrass theorem** (every bounded sequence has a convergent subsequence) and the fact that a closed set contains all its limit points. The key idea is that an open cover that resists finite reduction must be "wasting" its sets on limit points that are somehow escaping — and if the set is closed and bounded, there's nowhere to escape to. In metric spaces beyond ℝⁿ — infinite-dimensional function spaces, for instance — closed and bounded no longer implies compact. This is why the theorem is prized: it collapses an infinite verification into two geometric checks, but only because ℝⁿ has just the right structure.

The practical import of Heine-Borel is that you can now classify compact sets at a glance: closed intervals [a, b], closed rectangles, closed balls in ℝⁿ — all compact. Open intervals, ℝ itself, the rationals in [0,1] — all fail at least one condition, hence not compact. Every theorem that requires compactness (extreme value theorem, uniform continuity, Riemann integrability) can now be invoked simply by verifying closedness and boundedness.
