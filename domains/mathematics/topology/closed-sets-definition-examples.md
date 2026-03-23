---
id: closed-sets-definition-examples
title: Closed Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
builds-toward:
- closure-operator-topology
- boundary-set-topology
tags:
- closed-sets
stage: formal-systems
status: validated
---

# Closed Sets in Topological Spaces

## Core Idea
A set F is closed if its complement X\F is open. Closed sets form the dual picture to open sets: every set is either open, closed, both, or neither. Properties: arbitrary intersections of closed sets are closed, finite unions of closed sets are closed, ∅ and X are both open and closed.

## Explainer

A **closed set** in a topological space (X, τ) is defined as a set whose complement is open. That is, F ⊆ X is closed if and only if X \ F ∈ τ. This definition is purely set-theoretic and relies on the topology already telling us which sets are open. From your study of open sets, you know that the topology τ is the collection of open sets satisfying the three axioms (∅ and X are open, arbitrary unions are open, finite intersections are open). Closed sets are the "dual" notion obtained by taking complements of everything in τ.

The closed sets satisfy axioms that mirror those for open sets, but with unions and intersections swapped. The empty set ∅ and the whole space X are both closed (since their complements X and ∅ are both open). Arbitrary intersections of closed sets are closed — this follows from De Morgan's law, since the complement of an arbitrary intersection is an arbitrary union of open sets, which is open. Finite unions of closed sets are closed — again by De Morgan, the complement of a finite union is a finite intersection of open sets. Notice the asymmetry: arbitrary intersections of closed sets are closed, but only finite unions are guaranteed to be closed. As a counterexample to infinite unions, the sets [1/n, 1] for n = 1, 2, 3, ... are all closed in ℝ, but their union is (0, 1], which is not closed.

A common source of confusion is the relationship between "open" and "closed." These are not opposites. A set can be open, closed, both, or neither. The sets ∅ and X are always both open and closed (called **clopen**). In ℝ with the standard topology, the half-open interval [0, 1) is neither open nor closed: it is not open because no open interval around 0 fits inside it, and it is not closed because its complement (−∞, 0) ∪ [1, ∞) is not open (there is no open interval around 1 contained in the complement). The four categories — open only, closed only, both, neither — all genuinely occur and are not pathological edge cases.

In metric spaces, being closed is equivalent to containing all limit points: if a sequence in F converges to some point x, then x ∈ F. This is a theorem, not the definition. The definition — complement is open — is the foundational one that works in every topological space, including those with no metric. When you move beyond metric spaces, you lose the intuition of "a closed set contains its boundary points" and must fall back on the complement-based definition. This is why topology defines closed sets the way it does: the complement condition is universal, while the limit-point characterization is a consequence that holds only in sufficiently nice spaces.

## Questions

```yaml
- question: "In ℝ with the standard topology, the interval [0, 1] is closed. What is the correct reason, based on the definition of a closed set?"
  type: multiple-choice
  options:
    - "It contains both of its endpoints"
    - "Its complement (−∞, 0) ∪ (1, ∞) is an open set"
    - "It is bounded and therefore closed"
    - "It is compact, and compact sets are always closed"
  answer: 1
  explanation: "The definition of a closed set is: F is closed if X \\ F is open. The complement of [0,1] in ℝ is (−∞, 0) ∪ (1, ∞), which is a union of open intervals and therefore open. This is why [0,1] is closed — not because it contains its endpoints (that is a consequence, not a definition) and not because it is bounded or compact (which require additional theory)."

- question: "Consider an infinite collection of closed sets F₁, F₂, F₃, ... in ℝ. Let A = ∩ Fₙ (intersection of all) and B = ∪ Fₙ (union of all). Which is guaranteed to be closed?"
  type: multiple-choice
  options:
    - "A but not necessarily B"
    - "B but not necessarily A"
    - "Both A and B"
    - "Neither A nor B"
  answer: 0
  explanation: "Arbitrary intersections of closed sets are always closed (by De Morgan's law: the complement of an arbitrary intersection is an arbitrary union of open sets, which is open). Arbitrary unions of closed sets need not be closed. Counterexample: Fₙ = [1/n, 1] for n = 1, 2, 3, ... Each Fₙ is closed, but their union ∪ Fₙ = (0, 1], which is not closed because its complement (−∞, 0] ∪ (1, ∞) is not open."

- question: "The empty set ∅ is both open and closed in any topological space."
  type: true-false
  answer: true
  explanation: "The axioms of a topology require that ∅ and X are both open. Since ∅ is open, its complement X must also be open (X is required to be open by the axioms). Therefore ∅ = X \\ X has an open complement, making ∅ closed. Similarly X is both open and closed. Sets that are both open and closed are called 'clopen.'"

- question: "Every subset of a topological space is either open, closed, or both."
  type: true-false
  answer: false
  explanation: "A set can be neither open nor closed. In ℝ with the standard topology, the interval (0, 1] is an example: it is not open (the point 1 has no open ball around it contained in (0,1]) and not closed (its complement (−∞, 0] ∪ (1, ∞) is not open, since no open ball around 0 is contained in that set). The four possibilities — open only, closed only, both, neither — all genuinely occur."

- question: "Why is it incorrect to *define* a closed set as 'a set that contains all its boundary points,' even though this is sometimes stated as a characterization of closed sets in metric spaces?"
  type: short-answer
  answer: "The actual definition of a closed set is that its complement is open — this is what the axioms give us. In metric spaces, it can be proved that this is equivalent to containing all limit points (and hence all boundary points), but that equivalence is a theorem, not a definition. In a general topological space, 'boundary point' and 'limit point' are themselves defined in terms of open and closed sets, so using them to define closed sets would be circular. The complement-is-open definition is the foundational one."
  explanation: "This distinction matters when moving beyond metric spaces. In a general topology, intuitive notions like 'boundary' and 'limit point' don't automatically apply, so the clean set-theoretic definition (complement is open) is what remains universally valid."
```
