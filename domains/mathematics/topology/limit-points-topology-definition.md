---
id: limit-points-topology-definition
title: Limit Points and Accumulation Points
domain: mathematics
course: topology
prerequisites:
- id: neighborhoods-topology-definition
  type: hard
builds-toward:
- dense-sets-topology-definition
tags:
- limit-points
- accumulation
stage: formal-systems
status: validated
---

# Limit Points and Accumulation Points

## Core Idea
A point x is a limit point of A if every neighborhood of x contains a point of A different from x. The derived set A' is the set of all limit points of A. Then cl(A) = A ∪ A'. A set is closed iff A = cl(A) iff A' ⊆ A. Limit points generalize the notion of convergence to arbitrary topologies.

## Explainer

A point x is a **limit point** (or accumulation point) of a set A in a topological space (X, τ) if every neighborhood of x contains at least one point of A that is different from x. Formally, for every open set U containing x, the intersection U ∩ (A \ {x}) is nonempty. The requirement that the point be different from x is essential: without it, every element of A would trivially be a limit point of A (since x ∈ U ∩ A whenever x ∈ A), and the concept would collapse. The "different from x" clause is what distinguishes genuine accumulation — being approached by other points of A — from mere membership.

The canonical example is the set A = {1/n : n = 1, 2, 3, ...} in ℝ. The point 0 is a limit point of A: every open interval around 0 contains 1/n for sufficiently large n. But 0 is not in A. Meanwhile, 1/2 ∈ A is not a limit point of A, because the interval (1/3, 2/3) contains 1/2 but no other element of A. A point of A that is not a limit point of A is called an **isolated point** — it sits alone with a neighborhood containing no other element of the set. In this example, every element of A is isolated, and the only limit point is 0.

The set of all limit points of A is called the **derived set**, denoted A'. The closure of A is then cl(A) = A ∪ A' — the original set together with all its limit points. This gives a characterization of closed sets: A is closed if and only if A' ⊆ A, meaning A contains all its limit points. If any limit point of A is missing from A, then A fails to be closed. This connects the abstract definition of closed (complement is open) to the intuitive notion of a set that "includes its boundary." The closure cl(A) is always closed, and it is the smallest closed set containing A.

In metric spaces and first-countable spaces, limit points can be detected by sequences: x is a limit point of A if and only if there exists a sequence of distinct points in A converging to x. But in general topological spaces, this sequential characterization can fail. A point can be a limit point of A without any sequence from A converging to it — the topology may have "too many" neighborhoods for sequences (indexed by ℕ) to probe. In such spaces, **nets** (generalized sequences indexed by directed sets) or **filters** are needed to capture all limit points. The definition via neighborhoods — every neighborhood of x meets A \ {x} — works universally, which is why it is the foundational one.

## Questions

```yaml
- question: "The set A = {1/n : n = 1, 2, 3, ...} ⊂ ℝ with the standard topology. Which point is a limit point of A?"
  type: multiple-choice
  options:
    - "1, because it equals 1/1 and is in A"
    - "0, because every open interval around 0 contains points of A other than 0"
    - "1/2, because it is in A"
    - "Every element of A is its own limit point"
  answer: 1
  explanation: "0 is not in A, but every neighborhood of 0 contains 1/n for sufficiently large n — infinitely many points of A distinct from 0. That satisfies the definition. The elements of A like 1/2 are isolated: the interval (1/3, 2/3) contains 1/2 but no other point of A, so 1/2 does NOT meet the definition of limit point."

- question: "Point x is a limit point of set A if and only if:"
  type: multiple-choice
  options:
    - "x ∈ A and some neighborhood of x contains another point of A"
    - "Every neighborhood of x contains at least one point of A (including possibly x itself)"
    - "Every neighborhood of x contains a point of A distinct from x"
    - "x is the limit of a convergent sequence of distinct points in A"
  answer: 2
  explanation: "The definition of limit point requires every neighborhood to contain a point of A DIFFERENT from x. Option B is too weak — it would make any point of A trivially a limit point of itself. Option D is too restrictive — sequences do not characterize limit points in all topological spaces, only in first-countable ones."

- question: "If x is a limit point of A, then x must be an element of A."
  type: true-false
  answer: false
  explanation: "Limit points need not belong to A. For example, 0 is a limit point of A = {1/n : n ∈ ℕ} but 0 ∉ A. The closure cl(A) = A ∪ A' explicitly includes limit points that lie outside A — that is precisely what closure adds."

- question: "A set is closed if and only if it contains all of its limit points."
  type: true-false
  answer: true
  explanation: "This is the characterization of closed sets via limit points: A is closed ⟺ A' ⊆ A ⟺ cl(A) = A. A closed set contains every point that is 'approached' by elements of the set. This connects the abstract definition of closed set to the intuition of a set that contains its boundary."

- question: "Why does the definition of limit point require every neighborhood to contain a point of A DIFFERENT FROM x? What goes wrong if you drop that clause?"
  type: short-answer
  answer: "Without the 'different from x' requirement, every point of A would trivially be a limit point of A, since every neighborhood of x ∈ A contains x itself. The notion would collapse: every set would contain all its 'limit points,' all sets would be closed by the new definition, and the distinction between isolated points and genuine accumulation points would disappear."
  explanation: "The clause is what distinguishes isolated points (in A but not approached by other elements of A) from genuine limit points. An isolated point has a neighborhood containing no other element of A; a limit point has OTHER elements of A in every neighborhood, no matter how small."
```
