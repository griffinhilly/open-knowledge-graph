---
id: binary-relations
title: Binary Relations
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cartesian-product
  type: hard
- id: partial-orders-relations
  type: soft
builds-toward:
- equivalence-relations
- partial-orders
tags:
- relations
- binary
stage: formal-systems
status: validated
---
# Binary Relations

## Core Idea
A binary relation R on sets A and B is a subset of A × B, expressing relationships between elements. Relations have properties: reflexive (relates to itself), symmetric (mutual), transitive (chaining). These properties characterize equivalence and ordering relations.

## Questions

```yaml
- question: "Let R be the relation on the integers defined by 'a R b iff a ≤ b.' Which properties does R have?"
  type: multiple-choice
  options: ["Reflexive and symmetric only", "Symmetric and transitive only", "Reflexive and transitive only", "Reflexive, symmetric, and transitive"]
  answer: 2
  explanation: "≤ is reflexive (a ≤ a), transitive (if a ≤ b and b ≤ c then a ≤ c), but NOT symmetric (2 ≤ 3 does not imply 3 ≤ 2). A relation that is reflexive and transitive but not symmetric is a preorder (or partial order if also antisymmetric)."

- question: "Every subset of A × A qualifies as a binary relation on A."
  type: true-false
  answer: true
  explanation: "By definition, a binary relation on A is simply any subset of A × A. There is no requirement that the subset satisfy reflexivity, symmetry, or any other property — those are additional properties a relation may or may not have. The empty set and the full Cartesian product are both valid (if extreme) relations."

- question: "Give an example of a relation that is symmetric and transitive but NOT reflexive, or explain why no such relation can exist on a non-empty set."
  type: short-answer
  answer: "The empty relation on any non-empty set A is symmetric and transitive (vacuously) but not reflexive. Among non-empty relations, consider R = {(1,2),(2,1),(1,1),(2,2)} on {1,2,3} — it is symmetric and transitive on the elements it relates, but not reflexive because (3,3) is absent."
  explanation: "It is a common misconception that a symmetric + transitive relation must be reflexive. The reasoning 'if a R b and b R a, then a R a by transitivity' only works if every element appears in some pair. Elements that appear in no pair are never forced to be self-related, so reflexivity can fail."
```

## Explainer

When you studied the Cartesian product A × B, you saw how to form ordered pairs from two sets. A binary relation is simply a *selection* from those pairs: it picks out which pairs are related. For example, the relation "is a factor of" on the integers selects pairs like (2, 6) and (3, 12) but not (4, 7), because 2 divides 6 but 4 does not divide 7. Formally, R ⊆ A × A (or A × B for a relation between two different sets).

Relations become interesting when we ask about their structural properties. **Reflexivity** means every element is related to itself — (a, a) ∈ R for all a in A. Equality is reflexive; "is strictly less than" is not. **Symmetry** means the relation goes both ways: if (a, b) ∈ R then (b, a) ∈ R. "Is a sibling of" is symmetric; "is a parent of" is not. **Transitivity** means the relation chains: if a R b and b R c, then a R c. "Is an ancestor of" is transitive; "is a friend of" often is not in practice.

These three properties combine in important ways. A relation that is reflexive, symmetric, and transitive is called an **equivalence relation** — it partitions a set into groups of mutually related elements (equivalence classes). You will study this formally next. A relation that is reflexive, antisymmetric, and transitive is a **partial order** — like ≤ or "is a subset of" — which captures the idea of ranking or containment without requiring every pair to be comparable.

One subtlety worth watching: the empty relation (no pairs at all) is both symmetric and transitive *vacuously* — there are simply no pairs to violate those conditions. But it is not reflexive on any non-empty set because no element is self-related. This shows that symmetry + transitivity does not automatically give you reflexivity, contrary to a common intuition.
