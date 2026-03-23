---
id: local-compactness
title: Local Compactness
domain: mathematics
course: topology
prerequisites:
- id: compact-spaces-open-covers
  type: hard
builds-toward:
- topological-manifolds-introduction
tags:
- local-compactness
- compact-neighborhoods
stage: advanced
status: validated
---

# Local Compactness

## Core Idea
A space is locally compact if every point has a compact neighborhood. Local compactness allows one-point compactification and enables many results from classical analysis to extend. Manifolds are locally compact, and the concept bridges finite-dimensional compactness with infinite-dimensional topology.

## Questions

```yaml
- question: "Which of the following spaces is locally compact?"
  type: multiple-choice
  options:
    - "ℚ (the rational numbers) with the subspace topology from ℝ"
    - "An infinite-dimensional Hilbert space with the norm topology"
    - "ℝ with its standard topology"
    - "No non-compact space can be locally compact, by definition"
  answer: 2
  explanation: "ℝ is locally compact because every point x has the compact neighborhood [x−1, x+1] (compact by Heine-Borel). ℚ is not locally compact — compact subsets of ℚ have empty interior, so no compact set can contain an open neighborhood of any rational point. Infinite-dimensional Hilbert spaces are not locally compact because the closed unit ball is not compact. Option D is false — local compactness is strictly weaker than compactness; ℝ itself is the canonical example."

- question: "Why is local compactness the exactly right hypothesis needed to construct the one-point (Alexandroff) compactification of a Hausdorff space?"
  type: multiple-choice
  options:
    - "It guarantees the space is metrizable, which the compactification requires"
    - "It ensures there are enough compact sets to define neighborhoods of the added point ∞ in a way that makes the resulting space Hausdorff"
    - "It is needed so that every continuous function on the original space extends continuously to the compactification"
    - "It guarantees the original space is already compact, making the construction trivial"
  answer: 1
  explanation: "In the one-point compactification, neighborhoods of ∞ are defined as sets whose complement in X is compact. For the resulting space X* to be Hausdorff, every point x in X must have a compact neighborhood disjoint from a neighborhood of ∞ — which is exactly the definition of local compactness. Without local compactness, the construction fails to produce a Hausdorff space because there aren't enough compact sets to separate x from ∞."

- question: "Every compact topological space is also locally compact."
  type: true-false
  answer: true
  explanation: "If X is compact, then X itself is a compact neighborhood of every point — the whole space is open in itself and is compact by assumption. So every point trivially has a compact neighborhood. Local compactness is thus a strictly weaker condition than compactness: every compact space is locally compact, but not vice versa (ℝ is locally compact but not compact)."

- question: "The real numbers ℝ fail to be locally compact because no bounded subset of ℝ is compact."
  type: true-false
  answer: false
  explanation: "This gets it backwards: ℝ *is* locally compact. Moreover, closed and bounded subsets of ℝ *are* compact (by Heine-Borel), which is exactly why ℝ is locally compact — every point x has the compact neighborhood [x−1, x+1]. What ℝ lacks is *global* compactness: the whole space has no finite subcover for the cover {(−n, n)}, so ℝ is not compact. Local compactness asks only for compact neighborhoods at each point, not for the whole space to be compact."

- question: "Why is ℚ (the rationals with the subspace topology from ℝ) not locally compact, even though ℝ is? What is the structural reason?"
  type: short-answer
  answer: "A locally compact space requires compact neighborhoods around every point. In ℚ, any open set around a rational number q contains an interval (a, b) ∩ ℚ. But compact subsets of ℚ have empty interior — no compact subset of ℚ can contain an open interval of rationals. The reason is that any interval in ℚ contains Cauchy sequences converging to irrationals, so the interval cannot be compact (a compact metric space must be complete, but ℚ is not). There is therefore no compact set in ℚ that contains an open neighborhood of any point."
  explanation: "The key structural fact is that every compact subset of ℚ is nowhere dense in ℚ. This means no open set in ℚ is contained in a compact set — the condition for local compactness fails at every point. The difference from ℝ is that ℝ is complete: closed bounded sets are compact, so [x−1, x+1] works as a compact neighborhood. ℚ's incompleteness destroys this."
```

## Explainer

From your study of compact spaces and open covers, you know that compactness is a global condition: every open cover of the entire space has a finite subcover. **Local compactness** replaces this global demand with a pointwise one. A space X is **locally compact at a point x** if there exists a compact neighborhood of x — a compact set K containing an open set containing x. The space is **locally compact** if it is locally compact at every point.

The canonical example is ℝⁿ. The real line ℝ is not compact (the cover {(−n, n) : n ∈ ℕ} has no finite subcover), but every point x ∈ ℝ has a compact neighborhood: [x−1, x+1] is compact by the Heine-Borel theorem. So ℝ is locally compact but not compact. More generally, any open subset of ℝⁿ is locally compact, and any compact space is trivially locally compact (the whole space is a compact neighborhood of each point). An example that is neither: ℚ with the subspace topology from ℝ — it is not locally compact because no compact neighborhood of a rational number exists (compact subsets of ℚ have empty interior).

The most powerful consequence of local compactness in a Hausdorff space is the **one-point compactification** (Alexandroff compactification). Given a locally compact Hausdorff space X, adjoin a single extra point ∞ to form X* = X ∪ {∞}. Declare the topology on X* by keeping all the original open sets of X, and declaring a neighborhood of ∞ to be any set whose complement in X is compact. The result is compact: every open cover of X* either omits ∞ (covered by X's topology) or includes a neighborhood of ∞ whose complement is compact, reducing to a finite subcover. This construction turns ℝ into the circle S¹ and ℝ² into the 2-sphere S². Local compactness is exactly the hypothesis that ensures there are enough compact sets to build the topology around ∞ coherently — without it, the construction fails to produce a Hausdorff space.

Local compactness is also a cornerstone of integration theory beyond ℝⁿ. **Haar measure** — the canonical translation-invariant measure on locally compact groups — requires local compactness as an essential hypothesis; without compact neighborhoods, the averaging procedure used to construct the measure breaks down. For topological manifolds, local compactness is part of the definition: it ensures every point has a neighborhood homeomorphic to an open ball in ℝⁿ, connecting abstract topology to the finite-dimensional geometry you understand from calculus. Local compactness is the minimal condition under which the intuitions of classical analysis — that you can work locally in a small, controlled, "finite-feeling" region — remain valid in a general topological setting.
