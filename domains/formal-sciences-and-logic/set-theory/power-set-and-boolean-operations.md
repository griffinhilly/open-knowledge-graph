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

## Explainer

You already know what a subset is: a set B is a subset of A if every element of B is also in A. The **power set** P(A) collects all of those subsets into a single set — it is the set of all subsets of A. For A = {1, 2}, the subsets are ∅, {1}, {2}, and {1, 2}, so P(A) = {∅, {1}, {2}, {1, 2}}. Notice two things immediately: the empty set ∅ is always an element of P(A) (it is a subset of everything), and A itself is always an element (every set is a subset of itself). These are not edge cases — they are structural guarantees.

The cardinality formula |P(A)| = 2^|A| is best understood through a counting argument. For each element of A, you make a binary choice: include it in the subset or exclude it. With n elements, you have n independent binary choices, giving 2^n possible combinations. For a three-element set, 2³ = 8 subsets; for a ten-element set, 2¹⁰ = 1,024 subsets. This exponential growth means power sets of even modest finite sets become unwieldy quickly.

The power set forms a **Boolean algebra** — a structure you can think of as the algebra of "on/off" decisions. The operations are union (∪), intersection (∩), and complementation (taking A minus a subset). These operations satisfy familiar laws: union and intersection distribute over each other, double complementation returns to the original set, and the empty set and A itself act as identity elements for union and intersection respectively. Boolean algebra is not merely abstract; it is the mathematical foundation of digital logic, where sets of variables and truth tables are isomorphic to subsets and power-set operations.

**Cantor's theorem** is the deepest result here: for any set A, the power set P(A) is strictly larger than A — there is no surjection from A onto P(A). The proof uses a clever diagonal argument. Suppose f maps A to P(A). Define D = {x ∈ A : x ∉ f(x)} — the set of elements that are not in their own image. D is in P(A), but no element of A maps to D under f (any candidate leads to a contradiction). Therefore f cannot be surjective, so |P(A)| > |A| always. For finite sets this is obvious (n < 2ⁿ for all n ≥ 1), but for infinite sets it reveals a stunning fact: there are infinitely many infinite cardinalities, each power set creating a strictly larger infinity. This is the gateway to the transfinite cardinal arithmetic you will encounter in cardinality and equinumerosity.
