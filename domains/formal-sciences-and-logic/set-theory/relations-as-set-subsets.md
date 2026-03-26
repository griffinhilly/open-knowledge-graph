---
id: relations-as-set-subsets
title: Relations as Subsets of Cartesian Products
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cartesian-product-and-ordered-pairs
  type: hard
builds-toward:
- functions-and-mappings-formal
tags:
- relations
- binary-relations
- formal-definition
stage: formal-systems
status: validated
---

# Relations as Subsets of Cartesian Products

## Core Idea
A relation R from A to B is any subset of the Cartesian product A × B. This formalization treats all relational structures—ordering relations, equivalence relations, correspondence—as mathematical objects. Key properties include reflexivity, symmetry, transitivity, and totality, which characterize important relation types.

## Questions

```yaml
- question: "Consider the 'divides' relation on positive integers: a R b if a divides b evenly. Is this relation reflexive? Is it symmetric?"
  type: multiple-choice
  options:
    - "Reflexive only — every number divides itself, but 2 divides 4 while 4 does not divide 2"
    - "Both reflexive and symmetric — every number divides itself, and if a divides b then b divides a"
    - "Neither — integers cannot divide themselves, and divisibility does not go both directions"
    - "Symmetric only — if a divides b then b divides a, but no number divides itself"
  answer: 0
  explanation: "Every positive integer divides itself (n/n = 1), so the pair (n, n) is in the relation for all n — reflexive. But divisibility is not symmetric: 2 divides 4, yet 4 does not divide 2. So (2, 4) ∈ R but (4, 2) ∉ R, which means the relation is not symmetric. Option B's claim that divisibility is symmetric is false for most pairs."

- question: "You want to define a function f: {1, 2, 3} → {a, b, c} as a relation R ⊆ {1,2,3} × {a,b,c}. Which set of pairs qualifies as a function?"
  type: multiple-choice
  options:
    - "{(1, a), (1, b), (2, c), (3, a)} — having two outputs for input 1 is permitted in a general relation"
    - "{(1, a), (2, b)} — not every input has an output, but partial definitions are valid functions"
    - "{(1, b), (2, a), (3, c)} — every domain element appears exactly once as a left coordinate"
    - "{} — the empty relation qualifies since no pair violates the uniqueness condition"
  answer: 2
  explanation: "A function requires every element of the domain to appear as a left coordinate exactly once. Option C satisfies this: 1 maps to b, 2 to a, 3 to c — total coverage and uniqueness. Option A fails uniqueness (1 has two images). Option B fails totality (3 is missing). Option D fails totality (no element has any image). The empty set is a relation but not a total function on this domain."

- question: "A relation R ⊆ A × A is symmetric if and mainly if it contains no ordered pair (a, b) where a ≠ b."
  type: true-false
  answer: false
  explanation: "Symmetry requires that for every (a, b) ∈ R, the reverse (b, a) is also in R. It does not require the absence of pairs with a ≠ b — it requires such pairs to come in matching pairs. For example, {(1,2), (2,1), (3,3)} is symmetric despite containing pairs with distinct elements. The only relation containing no pair (a, b) with a ≠ b is a subset of the diagonal — that's a different property, not symmetry."

- question: "A function from A to B is a special case of a relation from A to B, subject to the constraint that every element of A appears as a left coordinate exactly once."
  type: true-false
  answer: true
  explanation: "This is the formal definition. A relation R ⊆ A × B becomes a total function when it satisfies two additional constraints: existence (every a ∈ A appears in at least one pair — every input has an output) and uniqueness (no a ∈ A appears in more than one pair — every input has exactly one output). A general relation satisfies neither condition; adding both gives a function. Functions are not a separate concept from relations — they are a constrained subtype."

- question: "What does it mean to define a relation 'extensionally,' and why does this approach matter for formal reasoning?"
  type: short-answer
  answer: "An extensional definition specifies a relation by listing exactly which pairs it contains — not by stating a rule or formula that generates them. Two relations defined by different rules but containing the same pairs are identical under the extensional definition, because identity is determined purely by membership. This matters because it allows set-theoretic operations (union, intersection, complement, composition) to apply directly to relations, and enables formal proofs about relational structure without depending on how the relation was described."
  explanation: "The extensional view is what allows you to treat 'less than on integers,' 'is a parent of,' and 'has the same remainder mod 3 as' as objects of the same type — subsets of Cartesian products — even though they arise from completely different contexts. Formal reasoning requires this uniformity: you can't apply the machinery of set theory to a vague 'rule' the way you can to an explicit set of pairs."
```

## Explainer

You already know that the **Cartesian product** A × B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. A relation is simply a selection from that pool — a subset R ⊆ A × B that picks exactly the pairs you want to declare "related." Writing (a, b) ∈ R is equivalent to saying "a is related to b under R," often written aRb. The key insight is that this definition requires nothing more than set membership: a relation is not a rule or a formula, just a collection of ordered pairs.

Consider the "less than" relation on the integers. Instead of defining it as a rule, we can think of it as the infinite set {(1,2), (1,3), (2,3), (1,4), (2,4), ...} — every pair (m, n) where m is less than n. Similarly, a family tree "is a parent of" relation is the set of ordered pairs (person, child) for every parent-child connection in the family. By reducing relations to sets of pairs, we can reason about them using the tools of set theory: union, intersection, complement, and composition.

Properties of relations are properties of these subsets relative to the underlying sets. **Reflexivity** means (a, a) ∈ R for every a in the domain — the relation includes all "self-pairs." **Symmetry** means if (a, b) ∈ R then (b, a) ∈ R — the relation looks the same in both directions. **Transitivity** means if (a, b) ∈ R and (b, c) ∈ R then (a, c) ∈ R — the relation chains through intermediate elements. An **equivalence relation** satisfies all three; it carves the set into disjoint classes of mutually related elements (called equivalence classes). A **partial order** is reflexive, antisymmetric, and transitive — it captures the structure of "no larger than" without requiring every pair to be comparable.

The payoff of this formalism is uniformity: functions, orderings, equivalences, and graphs are all special cases of the same structure. A **function** from A to B is a relation where every element of A appears as a left coordinate exactly once — adding a uniqueness constraint to the general relation definition. This builds directly toward the formal treatment of functions you will encounter next. Seeing functions as a subtype of relations, rather than a separate concept, lets you apply everything you know about sets to understand when functions exist, when they can be inverted, and how composition of relations generalizes function composition.

Mastering this definition means training yourself to think set-theoretically about structure. Whenever you encounter a relationship between objects — "divides," "is a subset of," "has the same remainder as" — the formal move is to ask: what are the two sets involved, what is A × B, and which ordered pairs belong to the relation? That translation from intuitive relationship to explicit subset is the foundation of all subsequent work in logic, algebra, and theoretical computer science.
