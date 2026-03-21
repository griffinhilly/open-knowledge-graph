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
status: draft
---

# Limit Points and Accumulation Points

## Core Idea
A point x is a limit point of A if every neighborhood of x contains a point of A different from x. The derived set A' is the set of all limit points of A. Then cl(A) = A ∪ A'. A set is closed iff A = cl(A) iff A' ⊆ A. Limit points generalize the notion of convergence to arbitrary topologies.

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
