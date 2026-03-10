---
id: well-ordering-principle
title: Well-Ordering Principle
domain: mathematics
course: methods-of-proof
prerequisites:
- id: mathematical-induction
  type: soft
- id: strong-induction
  type: soft
- id: set-theory-basics
  type: soft
builds-toward:
- partial-orders
tags:
- well-ordering
- least-element
- natural-numbers
- minimum
- induction-equivalence
stage: formal-systems
status: draft
---

# Well-Ordering Principle

## Core Idea
The well-ordering principle states that every non-empty set of natural numbers contains a least element. This seemingly simple fact is equivalent in power to mathematical induction — each can be derived from the other. It is used directly in proofs where you assume a non-empty set of counterexamples exists and then derive a contradiction by considering the minimal one. The well-ordering principle also underlies the Euclidean algorithm and the division algorithm.

## How It's Best Learned
Use the proof that √2 is irrational via well-ordering as an alternative to the standard contradiction proof. Also apply it to prove the division algorithm. Compare the three equivalent approaches: weak induction, strong induction, and well-ordering.

## Common Misconceptions
- Thinking well-ordering applies to all sets of real numbers — ℝ is not well-ordered (no least element in (0,1)).
- Confusing 'least element' with 'greatest lower bound' — the well-ordering principle is about actual minimum elements.
- Not seeing the connection to induction and treating well-ordering as an isolated fact.
