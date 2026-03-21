---
id: power-set-and-boolean-operations
title: Power Set and Boolean Algebra Operations
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: subset-proper-subset-relations
  type: hard
- id: axiom-of-power-set
  type: soft
builds-toward:
- cardinality-and-equinumerosity
tags:
- power-set
- boolean-algebra
- cantor-theorem
stage: formal-systems
status: draft
---

# Power Set and Boolean Algebra Operations

## Core Idea
The power set P(A) is the set of all subsets of A. For any set A with n elements, P(A) has 2ⁿ elements. The power set forms a Boolean algebra under union, intersection, and complementation. Cantor's theorem guarantees P(A) is strictly larger than A for any set.

## How It's Best Learned
Construct power sets for small finite sets: P({1}) = {∅, {1}}, P({1,2}) = {∅, {1}, {2}, {1,2}}. Verify the cardinality formula |P(A)| = 2^|A| by counting. Then consider infinite sets to build intuition about transfinite cardinals.

## Common Misconceptions
- Confusing P(A) with the union A ∪ {∅}. - Forgetting that both ∅ and A itself are always elements of P(A). - Thinking P(A) is infinite only when A is infinite (false; P(A) is infinite for any set A).

## Questions

```yaml
- question: "A set A has 10 elements. Someone estimates |P(A)| ≈ 20, reasoning: 'each element contributes two subsets — one containing it, one not.' What is the correct size of P(A) and what is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "P(A) has 20 elements — the reasoning is correct"
    - "P(A) has 100 elements — there are n² possible pairs"
    - "P(A) has 1,024 elements — the reasoning should count all combinations of n independent binary choices, giving 2^n"
    - "P(A) has 10 elements — P(A) and A have the same cardinality"
  answer: 2
  explanation: "The error treats each element's contribution in isolation rather than in combination. For each of the 10 elements, you make one binary choice: include or exclude. With 10 independent binary choices, there are 2^10 = 1,024 possible combinations. The '20 elements' reasoning implicitly assumes subsets contain at most one element, ignoring all the subsets with 2, 3, ..., 10 members. The counting argument (n independent yes/no decisions → 2^n outcomes) is the cleanest proof of |P(A)| = 2^n."

- question: "Cantor's theorem states that for any set A, |P(A)| > |A|. What does this imply for infinite sets?"
  type: multiple-choice
  options:
    - "It does not apply to infinite sets — all infinite sets have the same size"
    - "It implies there are infinitely many distinct infinite cardinalities, since each power-set operation creates a strictly larger infinity"
    - "It implies P(A) is infinite for any infinite A, but all infinite sets are the same size"
    - "It only means P(ℕ) is larger than ℕ; beyond that all infinite power sets collapse to the same size"
  answer: 1
  explanation: "Cantor's theorem has no exception for infinite sets — P(A) is strictly larger than A for any set whatsoever. Applying it repeatedly: ℕ < P(ℕ) < P(P(ℕ)) < ··· This generates a proper class of distinct infinite cardinalities. This was one of Cantor's most shocking results: not only are there different sizes of infinity, but there are infinitely many of them, with no largest one. Every infinite cardinal has a strictly larger power-set cardinal above it."

- question: "For any set A, both ∅ and A itself are always elements of P(A)."
  type: true-false
  answer: true
  explanation: "P(A) is the set of all subsets of A. The empty set ∅ is a subset of every set (vacuously: there is no element of ∅ that fails to be in A), so ∅ ∈ P(A) always. Every set is a subset of itself (A ⊆ A trivially), so A ∈ P(A) always. These are structural features of the power set, not edge cases. A common error is constructing P(A) while forgetting one or both — always check that your count includes ∅ and A."

- question: "For any infinite set A, P(A) and A have the same cardinality because both are infinite."
  type: true-false
  answer: false
  explanation: "This is exactly what Cantor's theorem disproves. 'Both are infinite' is true but irrelevant — there are different sizes of infinity. Cantor showed that no function from A to P(A) can be surjective, regardless of how large A is. For example, ℕ is countably infinite, but P(ℕ) has the same cardinality as the real numbers ℝ (uncountably infinite), which is strictly larger. The intuition that 'all infinities are equal' is one of the most consequential misconceptions in mathematics."

- question: "Explain Cantor's diagonal argument: why can no function f from A to P(A) be surjective, regardless of how large A is?"
  type: short-answer
  answer: "Suppose for contradiction that f: A → P(A) is any function. Define D = {x ∈ A : x ∉ f(x)} — the set of elements that are not members of their own image. D is a subset of A, so D ∈ P(A). But D cannot be in the range of f: if some element a mapped to D (i.e., f(a) = D), then asking 'is a ∈ D?' leads to a contradiction — a ∈ D iff a ∉ f(a) = D. So no element of A maps to D, meaning f is not surjective. Since f was arbitrary, no surjection from A to P(A) can exist."
  explanation: "The diagonal construction is the key technique: D is built specifically to differ from f(x) at the position x for every x in A. This 'diagonal' element D is outside the range of f by construction. The same technique appears in Cantor's original diagonal argument about ℝ, in Gödel's incompleteness theorem, and in the proof that the halting problem is undecidable — it is one of the most powerful proof patterns in all of mathematics."
```

## Explainer

You already know what a subset is: a set B is a subset of A if every element of B is also in A. The **power set** P(A) collects all of those subsets into a single set — it is the set of all subsets of A. For A = {1, 2}, the subsets are ∅, {1}, {2}, and {1, 2}, so P(A) = {∅, {1}, {2}, {1, 2}}. Notice two things immediately: the empty set ∅ is always an element of P(A) (it is a subset of everything), and A itself is always an element (every set is a subset of itself). These are not edge cases — they are structural guarantees.

The cardinality formula |P(A)| = 2^|A| is best understood through a counting argument. For each element of A, you make a binary choice: include it in the subset or exclude it. With n elements, you have n independent binary choices, giving 2^n possible combinations. For a three-element set, 2³ = 8 subsets; for a ten-element set, 2¹⁰ = 1,024 subsets. This exponential growth means power sets of even modest finite sets become unwieldy quickly.

The power set forms a **Boolean algebra** — a structure you can think of as the algebra of "on/off" decisions. The operations are union (∪), intersection (∩), and complementation (taking A minus a subset). These operations satisfy familiar laws: union and intersection distribute over each other, double complementation returns to the original set, and the empty set and A itself act as identity elements for union and intersection respectively. Boolean algebra is not merely abstract; it is the mathematical foundation of digital logic, where sets of variables and truth tables are isomorphic to subsets and power-set operations.

**Cantor's theorem** is the deepest result here: for any set A, the power set P(A) is strictly larger than A — there is no surjection from A onto P(A). The proof uses a clever diagonal argument. Suppose f maps A to P(A). Define D = {x ∈ A : x ∉ f(x)} — the set of elements that are not in their own image. D is in P(A), but no element of A maps to D under f (any candidate leads to a contradiction). Therefore f cannot be surjective, so |P(A)| > |A| always. For finite sets this is obvious (n < 2ⁿ for all n ≥ 1), but for infinite sets it reveals a stunning fact: there are infinitely many infinite cardinalities, each power set creating a strictly larger infinity. This is the gateway to the transfinite cardinal arithmetic you will encounter in cardinality and equinumerosity.
