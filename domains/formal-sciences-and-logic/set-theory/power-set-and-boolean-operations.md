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
