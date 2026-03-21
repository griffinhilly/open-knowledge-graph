---
id: limit-points-and-accumulation
title: Limit Points and Accumulation Points
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
  - sequences-convergence-topology
tags:
- limit-points
- convergence
stage: formal-systems
status: draft
---
# Limit Points and Accumulation Points

## Core Idea
A point x is a limit point of a set A if every open set containing x contains a point of A other than x itself. The closure of A equals A union its limit points. This characterizes closed sets.

## Questions

```yaml
- question: "Is 0 a limit point of the set A = {1, 1/2, 1/3, 1/4, …} ⊂ ℝ (with the usual topology)?"
  type: multiple-choice
  options:
    - "No — 0 is not in A, so it cannot be a limit point of A"
    - "No — the sequence 1/n approaches 0 but never equals 0, so the definition fails"
    - "Yes — every open interval around 0 contains infinitely many points of A different from 0"
    - "Yes — 0 is the greatest lower bound of A, which automatically makes it a limit point"
  answer: 2
  explanation: "The definition of limit point requires every open set containing x to contain a point of A other than x itself. For x = 0: any interval (−ε, ε) contains 1/n for all sufficiently large n, and none of these equal 0. So 0 is a limit point. Option A is the classic error — membership in A is irrelevant to limit-point status. A limit point does not need to belong to the set."

- question: "A set A is closed if and only if which condition holds?"
  type: multiple-choice
  options:
    - "Every point of A is a limit point of A"
    - "A contains no isolated points"
    - "Every limit point of A belongs to A"
    - "A equals its own interior"
  answer: 2
  explanation: "A set is closed iff it contains all its limit points — equivalently, A = Ā. Option A is wrong: closed sets can contain isolated points (points that are not limit points), such as a finite set like {1, 2, 3}. Option B is also wrong for the same reason. The key is whether limit points that A 'accumulates toward' are captured inside A."

- question: "Every point in a set A is a limit point of A."
  type: true-false
  answer: false
  explanation: "Isolated points are members of A that are NOT limit points: they have some open neighborhood containing no other point of A. For example, in A = {0} ∪ (1, 2), the point 0 belongs to A but every small open interval around it contains no other element of A, so 0 is isolated — not a limit point."

- question: "A limit point of a set A may lie outside of A."
  type: true-false
  answer: true
  explanation: "The definition requires every neighborhood of x to contain a point of A different from x — x itself need not be in A at all. For instance, 0 is a limit point of the open interval (0, 1) even though 0 ∉ (0, 1). This is precisely why the closure Ā = A ∪ A′ may be strictly larger than A: it must add the limit points that A 'approaches' but does not yet contain."

- question: "Why does the definition of limit point require the nearby point of A to be 'different from x itself'? What would go wrong without this requirement?"
  type: short-answer
  answer: "Without the 'different from x' clause, every point in A would trivially satisfy the definition: just take any neighborhood and find x ∈ A as the required element. The requirement forces x to be genuinely approached by other points of A — a real accumulation point. Without it, the distinction between isolated points (in A but surrounded by gaps) and true limit points (surrounded by other elements of A) would collapse."
  explanation: "The clause does real work: it rules out isolated points from being called limit points. An isolated point is in A but has a neighborhood containing no other element of A — with the 'different from x' requirement, it fails the limit-point test. This distinction matters for the closure operation and for characterizing closed sets."
```

## Explainer

You already know what **open sets** are in a topological space: sets that are "open" in the sense that every point has a neighborhood entirely contained within them. With that in hand, you can make precise what it means for a set to have "nearby" points accumulating around a given location. A point x is a **limit point** (also called an **accumulation point**) of a set A if every open set containing x also contains at least one point of A that is different from x itself.

Notice the phrasing carefully: *different from x itself*. This rules out the trivial case where x is isolated in A — a point that has some open neighborhood containing no other point of A. An isolated point is in A, but A doesn't "pile up" around it. A limit point may or may not belong to A; what matters is that A approaches x arbitrarily closely. In ℝ with the usual topology, every point of the interval (0, 1) is a limit point, and so are the endpoints 0 and 1 — even though 0 and 1 are not in the open interval itself. The sequence 1/n approaches 0, so every open set around 0 contains infinitely many points of the set {1, 1/2, 1/3, ...}, making 0 a limit point of that set.

The **closure** of a set A is defined as A together with all its limit points: A̅ = A ∪ A'. This is the smallest closed set containing A — adding the limit points fills in the "edges" that A is approaching. A set is **closed** if and only if it contains all its limit points, equivalently, if A = A̅. This is why [0, 1] is closed but (0, 1) is not: the open interval is missing its limit points 0 and 1. A closed set has "captured" everything that accumulates inside it.

Limit points let you connect the topology's open-set language to the analyst's intuition about limits of sequences. In a metric space, x is a limit point of A if and only if there exists a sequence of distinct points in A converging to x. In general topological spaces — where sequences may not capture all convergence behavior — the open-set definition of limit point is the correct generalization. This distinction matters when you move to spaces where first-countability fails and sequences must be replaced by nets or filters. But for the metric-space contexts you will encounter most often, the intuition is exactly right: a limit point is a point that A gets arbitrarily close to, a target that sequences in A can converge toward.
