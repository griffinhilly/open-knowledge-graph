---
id: closed-sets-real-line
title: Closed Sets on the Real Line
domain: mathematics
course: real-analysis
prerequisites:
- id: open-sets-real-line
  type: hard
builds-toward:
- compact-sets
- connected-sets
tags:
- closed-sets
- topology
- complements
stage: advanced
status: validated
---

# Closed Sets on the Real Line

## Core Idea
A set F ⊆ ℝ is closed if its complement ℝ ∖ F is open, equivalently, if it contains all its limit points (a ∈ F whenever some sequence from F converges to a). Closed sets are dual to open sets: finite unions of closed sets are closed, and arbitrary intersections of closed sets are closed.

## Questions

```yaml
- question: "Consider the set S = {1/n : n ∈ ℕ} = {1, 1/2, 1/3, 1/4, …}. Is S a closed subset of ℝ?"
  type: multiple-choice
  options:
    - "Yes, because all elements of S are positive, so S is bounded away from negative numbers"
    - "Yes, because S is bounded above by 1 and below by 0, satisfying the definition of a closed set"
    - "No, because the sequence 1/n converges to 0, which is a limit point of S not contained in S"
    - "No, because S contains infinitely many points, and infinite sets cannot be closed"
  answer: 2
  explanation: "A closed set must contain all its limit points. The sequence 1, 1/2, 1/3, … converges to 0, making 0 a limit point of S. But 0 ∉ S, so S fails the closed set criterion. Adding 0 — forming {0} ∪ {1/n : n ≥ 1} — makes the set closed. Options A and B describe properties (positivity, boundedness) that are irrelevant to the definition of closedness."

- question: "Which statement correctly describes the duality between open and closed sets with respect to unions and intersections?"
  type: multiple-choice
  options:
    - "Arbitrary unions of closed sets are closed; only finite intersections of open sets are open"
    - "Only finite unions of closed sets are guaranteed to be closed; arbitrary intersections of closed sets are closed"
    - "Both open sets and closed sets are closed under arbitrary unions"
    - "Closed sets are closed under countable unions but not arbitrary ones"
  answer: 1
  explanation: "The exact dual of the open-set rule (arbitrary unions open; finite intersections open) is: arbitrary intersections closed; finite unions closed. Classic counterexample for infinite unions of closed sets: each singleton {1/n} is closed (finite sets are closed), but ⋃{1/n} = {1, 1/2, 1/3, …} is not closed, as shown above."

- question: "The interval [0, 1) is a closed set because it contains the boundary point 0."
  type: true-false
  answer: false
  explanation: "[0, 1) is neither open nor closed. The sequence of points 1 − 1/n = {0, 1/2, 2/3, 3/4, …} lies entirely inside [0, 1) and converges to 1. But 1 ∉ [0, 1), so 1 is a limit point not in the set — [0, 1) fails the limit-point criterion. The fact that 0 is included does not make the set closed; what matters is whether *all* limit points are included."

- question: "A set that is not open should be closed."
  type: true-false
  answer: false
  explanation: "This is a very common misconception. 'Open' and 'closed' are independent properties — they are not logical opposites. A set can be: open but not closed (e.g., (0,1)); closed but not open (e.g., [0,1]); both open and closed (e.g., ℝ itself, or ∅); or neither open nor closed (e.g., [0,1)). The interval [0,1) is not open (0 has no neighborhood entirely inside it) and not closed (1 is a limit point not in the set)."

- question: "What does it mean for a set to 'contain all its limit points,' and why does this property capture the intuition of being 'closed'?"
  type: short-answer
  answer: "A limit point of F is any point x such that every neighborhood of x contains a point of F other than x — sequences from F can get arbitrarily close to x. F is closed if every such limit point belongs to F. This captures 'closedness' because it means F is stable under the most basic operation of analysis: taking limits. You cannot escape F by taking limits of sequences from F. An open set like (0,1) fails because sequences approaching 0 or 1 from inside converge to points outside the set."
  explanation: "The limit-point criterion makes closed sets the natural setting for analysis: whenever you have a sequence from a closed set and it converges, the limit is guaranteed to stay in the set. This is why closed and bounded (compact) sets are so powerful — you can extract convergent subsequences without worrying about limits escaping."
```

## Explainer

From your study of open sets, you know that open sets are "inward-looking" — every point in an open set has a neighborhood that stays inside the set, so no point of an open set is on its boundary. Closed sets are defined as the complements of open sets, which immediately gives them a dual structure. Every theorem about open sets has a mirror image for closed sets, with unions and intersections swapped, and finite and arbitrary swapped.

The most important characterization of closed sets is the **limit point criterion**: a set F is closed if and only if it contains all of its limit points. A **limit point** of F is any point x (possibly in F, possibly not) such that every open interval around x contains a point of F other than x itself — in other words, points of F can get arbitrarily close to x. The closed interval [a, b] contains all its limit points because sequences from [a, b] converge to values in [a, b]; the open interval (a, b) fails this because sequences approaching a or b from the inside converge to points not in the set. The set {1/n : n ∈ ℕ} is not closed: the sequence 1, 1/2, 1/3, … converges to 0, but 0 is not in the set. Adding 0 to form {0} ∪ {1/n : n ≥ 1} makes it closed.

The intersection/union rules are the exact dual of what you know for open sets. Arbitrary intersections of closed sets are closed (the intersection of any collection of closed sets, even infinitely many, is closed), but only finite unions of closed sets are guaranteed to be closed. The classic counterexample for infinite unions: each singleton {1/n} is closed (any finite set is closed), but their union {1/n : n ≥ 1} is not closed, as shown above. This asymmetry mirrors the fact that open sets are closed under arbitrary unions but only finite intersections.

These duality rules have real consequences for analysis. When you need a set that is automatically closed — for instance, to take a limit of a sequence and know the limit stays inside — closed sets are the right setting. The interplay between open and closed sets is the foundation for compactness (every open cover has a finite subcover), which you will study next. A crucial distinction: despite the names, "not open" does not mean "closed," and "not closed" does not mean "open." The interval [0, 1) is neither open nor closed, and ℝ itself is both open and closed in the standard topology.
