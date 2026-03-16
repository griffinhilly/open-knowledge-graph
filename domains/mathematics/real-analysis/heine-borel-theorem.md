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

## Explainer

From your study of compact sets, you know the abstract definition: a set K is compact if every open cover of K has a finite subcover. This definition is powerful but hard to verify directly — you'd need to check infinitely many possible open covers. The **Heine-Borel theorem** gives you a completely checkable equivalent in ℝⁿ: a set is compact if and only if it is **closed** and **bounded**. Checking whether [0, 1] is compact just became checking two easy conditions.

To see why both conditions are necessary, consider what happens when you drop one. The open interval (0, 1) is bounded but not closed — the sequence 1/n converges to 0, which is outside the set, so the set fails to contain all its limit points. You can build an open cover of (0, 1) that has no finite subcover: take Uₙ = (1/n, 1) for n = 1, 2, 3, …. Every point in (0, 1) is eventually covered, but any finite subcollection only covers points above some positive lower bound, missing points near 0. Now consider ℤ (the integers): closed but not bounded. Take the cover of singletons {n−1, n+1} for each n ∈ ℤ — each integer is covered, but removing any element of the cover leaves one integer uncovered, so no finite subcover exists. Boundedness keeps the set from stretching to infinity; closedness keeps it from leaking through its boundary.

The proof of the theorem in ℝ uses two tools you've seen: the **Bolzano-Weierstrass theorem** (every bounded sequence has a convergent subsequence) and the fact that a closed set contains all its limit points. The key idea is that an open cover that resists finite reduction must be "wasting" its sets on limit points that are somehow escaping — and if the set is closed and bounded, there's nowhere to escape to. In metric spaces beyond ℝⁿ — infinite-dimensional function spaces, for instance — closed and bounded no longer implies compact. This is why the theorem is prized: it collapses an infinite verification into two geometric checks, but only because ℝⁿ has just the right structure.

The practical import of Heine-Borel is that you can now classify compact sets at a glance: closed intervals [a, b], closed rectangles, closed balls in ℝⁿ — all compact. Open intervals, ℝ itself, the rationals in [0,1] — all fail at least one condition, hence not compact. Every theorem that requires compactness (extreme value theorem, uniform continuity, Riemann integrability) can now be invoked simply by verifying closedness and boundedness.
