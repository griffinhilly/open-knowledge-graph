---
id: interior-operator-topology
title: Interior of Sets
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
builds-toward:
- boundary-set-topology
- closure-operator-topology
tags:
- interior
- operators
stage: formal-systems
status: draft
---

# Interior of Sets

## Core Idea
The interior of A, denoted int(A) or A°, is the union of all open sets contained in A (the largest open subset of A). A point x ∈ int(A) iff A is a neighborhood of x. Properties: int(∅) = ∅, int(X) = X, int(int(A)) = int(A), int(A ∩ B) = int(A) ∩ int(B).

## Questions

```yaml
- question: "In ℝ with the standard topology, what is the interior of the set A = (0, 1]?"
  type: multiple-choice
  options:
    - "(0, 1], because A already contains its boundary point"
    - "(0, 1), because 1 is not in the interior — no open set containing 1 is fully contained in A"
    - "[0, 1], because the interior includes the closure"
    - "∅, because A is half-open and therefore has no interior"
  answer: 1
  explanation: "The interior of A consists of all points x such that some open set containing x is entirely contained in A. For any x ∈ (0, 1), we can find a small open interval (x−ε, x+ε) ⊂ A, so these are interior points. The endpoint 1 is not interior: every open interval around 1 contains points greater than 1, which are outside A. The endpoint 0 is also not interior for the same reason — open intervals around 0 extend into negative numbers."

- question: "Which statement correctly characterizes what it means for x to be in the interior of A?"
  type: multiple-choice
  options:
    - "x ∈ A and x is not on the boundary of A"
    - "Every open set containing x is a subset of A"
    - "There exists an open set U with x ∈ U ⊆ A"
    - "x belongs to all open sets contained in A"
  answer: 2
  explanation: "x ∈ int(A) if and only if A is a neighborhood of x — meaning there exists an open set U with x ∈ U ⊆ A. This is the point-level characterization of interior. Option A is intuitive but imprecise (boundary is defined using interior). Option B is too strong — we need existence of one such open set, not that every open set around x is contained in A. Option D is wrong because we need U ⊆ A, not x ∈ all such sets."

- question: "For any set A in a topological space, int(int(A)) = int(A)."
  type: true-false
  answer: true
  explanation: "The interior operator is idempotent: taking the interior twice gives the same result as taking it once. This follows from the fact that int(A) is already an open set (it is the union of open sets, hence open), and the interior of an open set is the set itself — every point of an open set has the set itself as an open neighborhood containing it. So int(int(A)) = int(A)."

- question: "The interior of a union satisfies int(A ∪ B) = int(A) ∪ int(B) for all sets A and B."
  type: true-false
  answer: false
  explanation: "This is false in general. int(A) ∪ int(B) ⊆ int(A ∪ B) always holds, but equality can fail. A simple counterexample in ℝ: let A = [0, 1] and B = [1, 2]. Then int(A) = (0,1), int(B) = (1,2), so int(A) ∪ int(B) = (0,1) ∪ (1,2), which omits the point 1. But int(A ∪ B) = int([0,2]) = (0,2), which includes 1. The correct identity is for intersections: int(A ∩ B) = int(A) ∩ int(B)."

- question: "What does it mean for a set A to be a 'neighborhood' of a point x in topology, and how does this relate to x being an interior point of A?"
  type: short-answer
  answer: "A set A is a neighborhood of x if there exists an open set U with x ∈ U ⊆ A — A contains an open set around x. This is exactly the condition for x to be an interior point of A. The interior of A is precisely the set of all points for which A is a neighborhood. This characterization shifts perspective from the global (int(A) as the largest open subset of A) to the local (which individual points have an open 'cushion' inside A)."
  explanation: "Both characterizations — int(A) as the largest open subset, and int(A) as the set of points for which A is a neighborhood — define the same set. The neighborhood characterization is useful for checking point membership; the 'largest open subset' characterization is useful for proving properties like int(int(A)) = int(A) and int(A ∩ B) = int(A) ∩ int(B)."
```
