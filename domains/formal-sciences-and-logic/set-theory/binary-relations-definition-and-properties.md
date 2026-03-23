---
id: binary-relations-definition-and-properties
title: Binary Relations and Their Properties
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordered-pairs-and-tuples
  type: hard
- id: indexed-families-of-sets
  type: soft
builds-toward:
- equivalence-relations-and-equivalence-classes
- well-founded-relations-and-recursion
- functions-and-function-properties
tags:
- relations
- properties
- structures
stage: formal-systems
status: validated
---

# Binary Relations and Their Properties

## Core Idea
A binary relation R on a set S is a subset R ⊆ S × S. Relations exhibit properties including reflexivity (aRa for all a), symmetry (aRb ⟹ bRa), and transitivity (aRb ∧ bRc ⟹ aRc). Different combinations of these properties define important relation classes: equivalence relations, orderings, and more.

## Questions

```yaml
- question: "The relation R on the integers defined by 'aRb if a ≤ b' satisfies which combination of properties?"
  type: multiple-choice
  options:
    - "Reflexive, symmetric, and transitive — it is an equivalence relation"
    - "Reflexive, antisymmetric, and transitive — it is a partial (and total) order"
    - "Symmetric and transitive but not reflexive"
    - "Antisymmetric only — it fails both reflexivity and transitivity"
  answer: 1
  explanation: "The ≤ relation is reflexive (a ≤ a for all integers), antisymmetric (if a ≤ b and b ≤ a then a = b), and transitive (if a ≤ b and b ≤ c then a ≤ c). It is NOT symmetric: 3 ≤ 5 but 5 ≤ 3 is false. This combination — reflexivity, antisymmetry, transitivity — defines a partial order. Since every pair of integers is comparable (either a ≤ b or b ≤ a), it is additionally a total order."

- question: "Consider the 'is a sibling of' relation. A student claims it is transitive because if Alice is a sibling of Bob and Bob is a sibling of Carol, then Alice is a sibling of Carol. Is 'sibling of' an equivalence relation?"
  type: multiple-choice
  options:
    - "Yes — it is reflexive, symmetric, and transitive, satisfying all three requirements"
    - "No — sibling-of is symmetric and transitive but fails reflexivity (no one is their own sibling), so it is not an equivalence relation"
    - "No — sibling-of is not transitive, so the student's reasoning is flawed"
    - "Yes — any relation that is symmetric and transitive is automatically reflexive"
  answer: 1
  explanation: "The student's transitivity claim is correct for full siblings. And sibling-of is symmetric. But reflexivity fails: a person is not their own sibling, so for person a, aRa does not hold. An equivalence relation requires all three properties: reflexivity, symmetry, and transitivity. Failing any one disqualifies it. Note that option D is a common misconception: a relation can be symmetric and transitive without being reflexive (if no element is related to anything, it vacuously satisfies both while failing reflexivity)."

- question: "Every equivalence relation on a set S partitions S into disjoint subsets called equivalence classes, where every element in a subset is related to every other element in that subset."
  type: true-false
  answer: true
  explanation: "This is one of the most important theorems in basic set theory. An equivalence relation's three properties — reflexivity (every element is in some class), symmetry (membership is mutual), and transitivity (being related to the same element puts you in the same class) — together guarantee that the equivalence classes are disjoint and exhaustive. The integers modulo n provide a canonical example: congruence mod 3 partitions the integers into exactly three classes."

- question: "A symmetric relation and an antisymmetric relation are mutually exclusive — no relation can satisfy both properties simultaneously."
  type: true-false
  answer: false
  explanation: "False. The equality relation = on any set satisfies both. Symmetry requires: if aRb then bRa. Antisymmetry requires: if aRb and bRa then a = b. The equality relation satisfies symmetry (if a = b then b = a) and antisymmetry (if a = b and b = a then trivially a = b). There is no contradiction because antisymmetry's condition only triggers when both aRb and bRa hold — equality allows this only when a and b are the same element. The two properties conflict only when a relation has pairs (a,b) and (b,a) with a ≠ b."

- question: "Explain the difference between an equivalence relation and a partial order in terms of the properties they require. Why does swapping symmetry for antisymmetry change the mathematical structure so fundamentally?"
  type: short-answer
  answer: "Both equivalence relations and partial orders require reflexivity and transitivity. The difference is in the third property: equivalence relations add symmetry (if aRb then bRa), while partial orders add antisymmetry (if aRb and bRa then a = b). Symmetry means the relation is mutual — being related has no directionality, so all related elements form clusters of 'equal' elements. Antisymmetry means the relation has direction — when it runs both ways, the two elements must be identical. This turns clusters into a ranked structure where elements can be 'above' or 'below' each other. Equality becomes the only way to be related in both directions in an order, giving the structure its hierarchical character."
  explanation: "The three-property framework reveals how small changes in axioms produce radically different mathematical structures. Equivalence relations partition sets; partial orders impose hierarchy. The swap of one property — symmetry vs. antisymmetry — is the precise formal difference between 'same kind of thing' and 'at most as large as.' This is why identifying which properties a relation has is the first step to understanding what kind of mathematical structure it defines."
```

## Explainer

From your work with ordered pairs, you know that S × S is the set of all pairs (a, b) where a and b come from S. A **binary relation** R on S is simply a subset of this Cartesian product: a collection of pairs. When (a, b) ∈ R, we write aRb and say "a is related to b." This set-theoretic definition is completely general — any collection of pairs is a valid relation. The interesting structure comes from which properties that collection happens to satisfy.

Three properties appear most often. **Reflexivity** says every element is related to itself: for all a ∈ S, aRa. The equality relation on any set is reflexive; so is "less than or equal to" on the integers. **Symmetry** says the relation runs in both directions: if aRb then bRa. "Is a sibling of" is symmetric; "is a parent of" is not. **Transitivity** says the relation chains: if aRb and bRc then aRc. "Is an ancestor of" is transitive; "is a neighbor of" (in a graph) typically is not. A fourth property appears in orderings: **antisymmetry** says that if aRb and bRa, then a = b — the relation can go both ways only when the two elements are the same.

These properties combine to define the most important relation types in mathematics. **Equivalence relations** satisfy reflexivity, symmetry, and transitivity — they partition S into equivalence classes where all related elements are grouped together. "Has the same remainder when divided by 3" is an equivalence relation on the integers, grouping them into classes {0, 3, 6, ...}, {1, 4, 7, ...}, {2, 5, 8, ...}. **Partial orders** satisfy reflexivity, antisymmetry, and transitivity — they give a notion of "at most as large as" without requiring all elements to be comparable. The subset relation on a collection of sets is a partial order. **Total orders** add comparability: for any two elements, either aRb or bRa (or both, in which case a = b). The usual ≤ on the integers is a total order.

Learning to identify which properties a relation has — and which it lacks — is the first step toward classifying it. The strategy is to test each property directly with concrete examples and counterexamples. For a finite set, you can draw the relation as a directed graph (a → b whenever aRb) and read off reflexivity (every node has a self-loop), symmetry (every edge runs in both directions), and transitivity (if a → b → c then a → c). This visual representation builds intuition rapidly and makes the abstract definitions concrete.
