---
id: closed-sets-topology
title: Closed Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition
  type: hard
- id: open-sets-topology
  type: hard
builds-toward:
- closure-interior-boundary
- limit-points-and-accumulation
tags:
- closed-sets
- complements
stage: formal-systems
status: validated
---

# Closed Sets in Topological Spaces

## Core Idea
A set F in a topological space is closed if its complement X \ F is open. Closed sets satisfy the dual property to open sets: they are closed under arbitrary intersections and finite unions.

## Questions

```yaml
- question: "In ℝ with the standard topology, what kind of set is [0, 1)?"
  type: multiple-choice
  options:
    - "Open but not closed"
    - "Closed but not open"
    - "Both open and closed (clopen)"
    - "Neither open nor closed"
  answer: 3
  explanation: "[0, 1) is not open because the point 0 has no open interval entirely within [0, 1) — any neighborhood of 0 includes negative numbers. It is not closed because its complement (−∞, 0) ∪ [1, ∞) is not open — the point 1 has no open neighborhood contained in that complement. So [0, 1) is neither open nor closed. This shows that 'not open' does not mean 'closed'; the two properties are independent."

- question: "Which statement correctly captures the dual closure properties of open and closed sets in a topology?"
  type: multiple-choice
  options:
    - "Open sets are closed under arbitrary intersections; closed sets are closed under arbitrary unions"
    - "Open sets are closed under arbitrary unions; closed sets are closed under arbitrary intersections"
    - "Both are closed under arbitrary unions and arbitrary intersections"
    - "Both are closed under only finite operations"
  answer: 1
  explanation: "Open sets: arbitrary unions are open, but only *finite* intersections are guaranteed open (an infinite intersection of open sets can fail to be open — e.g., ⋂ₙ (−1/n, 1/n) = {0}, which is closed). Closed sets are exactly dual: arbitrary intersections of closed sets are closed, but only *finite* unions are guaranteed closed. This asymmetry between 'arbitrary' and 'finite' is fundamental in topology and is proved via De Morgan's laws applied to the open-set axioms."

- question: "In a topological space, a set cannot be both open and closed simultaneously."
  type: true-false
  answer: false
  explanation: "This is false. Sets that are both open and closed are called 'clopen.' In any topological space, the empty set ∅ and the whole space X are always clopen — they satisfy the open-set axioms directly. In some spaces (like a two-component disconnected space), other clopen sets exist. 'Closed' is not the negation of 'open'; a set can be open, closed, both, or neither."

- question: "Every closed set in a topological space is, by definition, the complement of some open set."
  type: true-false
  answer: true
  explanation: "Yes — this is exactly the definition of a closed set. A set F is closed if and only if X \\ F is open. Closed sets are not defined by any intrinsic property of their own; they are defined relationally, through their complements and the topology's open sets. This makes the topology's open-set structure the primary object, with closed sets derived from it by complementation."

- question: "Why is it possible for a set to be both open and closed in a topological space? Explain what 'clopen' means and give an example."
  type: short-answer
  answer: "A set is open if its complement is closed, and closed if its complement is open. A clopen set satisfies both: it is open, and its complement is also open (hence it is also closed). In any topological space, ∅ and X are always clopen: ∅ is open by axiom, and its complement X is also open by axiom — so ∅ is closed. The same reasoning applies to X."
  explanation: "The confusion arises from assuming 'open' and 'closed' are opposite properties, like a door being open or closed. In topology they are not opposites but independent conditions, each defined by its own criterion. The empty set and whole space always satisfy both because the topology axioms require them to be open, and since each is the complement of the other, each is also closed. In disconnected spaces, larger clopen sets exist and their presence is intimately tied to the notion of connectedness."
```

## Explainer

From your study of topological spaces, you know that a topology on a set X is a collection of **open sets** satisfying three axioms: ∅ and X are open, arbitrary unions of open sets are open, and finite intersections of open sets are open. **Closed sets** are defined purely in terms of open sets — a set F is closed when its complement X \ F is open. This is not a separate structure layered on top of the topology; it is the same topology viewed through complementation.

The relationship between open and closed becomes intuitive with examples. In ℝ with the standard topology, the open interval (0, 1) is open — every point has a small open neighborhood contained in the interval. Its complement (−∞, 0] ∪ [1, ∞) is closed. The closed interval [0, 1] is closed — its complement (−∞, 0) ∪ (1, ∞) is open. A single point {0.5} is closed — its complement is the union of two open rays. Notice that "closed" does not mean "not open": the empty set ∅ and the whole space X are both open and closed simultaneously (called **clopen** sets), and in general a set can be open, closed, both, or neither.

The closure properties of closed sets follow immediately from De Morgan's laws applied to the open set axioms. Arbitrary intersections of closed sets are closed: if each Fα is closed, then its complement is open, and ⋃(X \ Fα) = X \ (⋂Fα) is an arbitrary union of open sets — hence open — so ⋂Fα is closed. Finite unions of closed sets are closed by the dual argument. This is the exact mirror image of open sets, with the quantifiers swapped: open sets support arbitrary unions but only finite intersections; closed sets support arbitrary intersections but only finite unions. The asymmetry between "arbitrary" and "finite" is fundamental to topology and recurs throughout the subject.

Understanding closed sets well is essential for what comes next. The **closure** of a set A is the smallest closed set containing A — equivalently, the intersection of all closed sets containing A. The **interior** of A is the largest open set contained in A. The **boundary** of A sits between them. These notions give you the vocabulary to talk about limits, accumulation points, and continuity in purely topological terms, without any reference to distance or ε-δ arguments — a level of generality that becomes powerful when you move to spaces with no natural metric.
