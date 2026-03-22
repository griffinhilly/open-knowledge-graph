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

## Explainer

The **interior** of a set A in a topological space (X, τ), denoted int(A) or A°, is the largest open set contained in A. Equivalently, it is the union of all open sets that are subsets of A. Since any union of open sets is open, this union is itself open and is contained in A, making it the unique largest open subset. A point x belongs to int(A) if and only if A is a **neighborhood** of x — that is, there exists an open set U with x ∈ U ⊆ A. This gives two equivalent perspectives: globally, int(A) is the largest open set inside A; locally, it is the set of points that have an open "cushion" entirely within A.

In ℝ with the standard topology, the interior of [0, 1] is (0, 1). The endpoints 0 and 1 are not interior points because every open interval around them extends outside [0, 1]. The interior of (0, 1] is also (0, 1) — the endpoint 1 fails the interior test for the same reason. The interior of a single point {x} in ℝ is empty, since no open interval fits inside a singleton. The interior of ℚ (the rationals) in ℝ is also empty: every open interval contains irrationals, so no open set is contained in ℚ. These examples show that the interior operator strips away the "boundary" of a set, leaving only the portion where the set has room to breathe.

The interior operator satisfies four characteristic properties, known as the **Kuratowski interior axioms**: (1) int(X) = X, (2) int(A) ⊆ A for every A, (3) int(int(A)) = int(A) (idempotence), and (4) int(A ∩ B) = int(A) ∩ int(B). Property (3) follows from the fact that int(A) is already open, and the interior of an open set is itself. Property (4) states that the interior distributes over finite intersections. However, the analogous identity for unions fails: int(A ∪ B) is not necessarily equal to int(A) ∪ int(B). For example, in ℝ, int([0, 1] ∪ [1, 2]) = int([0, 2]) = (0, 2), but int([0, 1]) ∪ int([1, 2]) = (0, 1) ∪ (1, 2), which misses the point 1.

The interior operator is dual to the **closure** operator: int(A) = X \ cl(X \ A), and cl(A) = X \ int(X \ A). Taking the interior of A is the same as taking the complement, then the closure, then the complement again. This duality means that every theorem about interiors has a dual theorem about closures, and vice versa. A set is open if and only if it equals its own interior (A = int(A)), just as a set is closed if and only if it equals its own closure. The interior and closure operators, together with the boundary operator ∂A = cl(A) \ int(A), provide a complete toolkit for analyzing the fine structure of sets in a topological space.

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
