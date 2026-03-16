---
id: equivalence-relations
title: Equivalence Relations
domain: mathematics
course: methods-of-proof
prerequisites:
- id: binary-relations
  type: hard
tags:
- relations
- equivalence
- partitions
stage: formal-systems
status: draft
---

# Equivalence Relations

## Core Idea
An equivalence relation is reflexive, symmetric, and transitive. Every equivalence relation partitions its domain into equivalence classes of mutually related elements, formalizing the notion of 'sameness' for a given property.

## Questions

```yaml
- question: "The relation R on integers defined by 'a R b if and only if a − b is even' — which of the following correctly describes its properties?"
  type: multiple-choice
  options:
    - "Reflexive and symmetric, but not transitive"
    - "Reflexive and transitive, but not symmetric"
    - "Reflexive, symmetric, and transitive — it is an equivalence relation"
    - "Symmetric and transitive, but not reflexive"
  answer: 2
  explanation: "Reflexivity: a − a = 0, which is even. Symmetry: if a − b is even then b − a = −(a − b) is also even. Transitivity: if a − b and b − c are both even, their sum (a − c) = (a − b) + (b − c) is even. All three properties hold, making R an equivalence relation. Its two equivalence classes are the even integers and the odd integers."

- question: "The relation 'less than' (<) on the real numbers is an equivalence relation because it is transitive."
  type: true-false
  answer: false
  explanation: "Transitivity alone is not sufficient for an equivalence relation. 'Less than' fails reflexivity (no number satisfies a < a) and fails symmetry (a < b does not imply b < a). An equivalence relation requires all three properties: reflexive, symmetric, and transitive. Transitivity alone produces a strict partial order, not an equivalence relation."

- question: "What is an equivalence class, and how do equivalence classes relate to the partition of a set?"
  type: short-answer
  answer: "The equivalence class [a] is the set of all elements related to a. The equivalence classes of an equivalence relation partition the domain into non-overlapping, exhaustive subsets — every element belongs to exactly one class."
  explanation: "Reflexivity ensures a is always in its own class. Symmetry and transitivity together ensure two equivalence classes are either identical or completely disjoint — no element can belong to two different classes at once. So the classes tile the domain without gaps or overlaps, which is precisely the definition of a partition."
```

## Explainer

You already know what a binary relation is — a set of ordered pairs that records which elements are related to which. An equivalence relation is a special kind of binary relation that formalizes the intuitive idea of "sameness under some criterion." The three defining properties — reflexive, symmetric, and transitive — are precisely what any reasonable notion of sameness must satisfy.

Reflexivity says every element is related to itself (a ~ a). Symmetry says the relation works in both directions (if a ~ b, then b ~ a). Transitivity says the relation is consistent across chains (if a ~ b and b ~ c, then a ~ c). Intuitively: you're the same as yourself, sameness is mutual, and chains of sameness compose. Geometric congruence satisfies all three. Equality satisfies all three. "Has the same remainder when divided by 3" satisfies all three — and this last example is modular arithmetic in disguise, a sign of how pervasive equivalence relations are.

The most important consequence of these three properties together is the **partition theorem**: every equivalence relation on a set S partitions S into equivalence classes — non-overlapping groups where every element belongs to exactly one group. The equivalence class of a, written [a], is the set {x : x ~ a}. Two elements are in the same class if and only if they are related. This is why mathematicians use equivalence relations so extensively: when you want to treat "indistinguishable" things as the same object, you quotient by an equivalence relation and work with classes instead of individual elements. Rational numbers are defined this way (pairs of integers under the equivalence (a, b) ~ (c, d) iff ad = bc).

A common pitfall is assuming that any two of the three properties imply the third. They do not. The relation ≤ on real numbers is reflexive and transitive but not symmetric — it is a partial order, not an equivalence relation. Admiration between people may be symmetric but rarely reflexive or transitive. When verifying whether a relation is an equivalence relation, always check each property separately, either by proving it holds or constructing a counterexample to show it fails.
