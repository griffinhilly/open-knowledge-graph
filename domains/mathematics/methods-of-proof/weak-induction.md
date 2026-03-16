---
id: weak-induction
title: Weak Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: mathematical-induction
  type: hard
- id: predicates-and-quantified-statements
  type: soft
builds-toward:
- strong-induction-and-wellordering
tags:
- proof
- induction
- mathematical induction
stage: formal-systems
status: draft
---

# Weak Induction

## Core Idea
Weak induction (or standard induction) proves a statement P(n) for all natural numbers by: (1) proving the base case P(1) or P(0), and (2) proving that if P(k) is true, then P(k+1) is true. The inductive step assumes P(k) for one value k and derives P(k+1). Weak induction is sufficient for most inductive proofs.

## How It's Best Learned
Work through several inductive proofs with clear base cases and inductive steps. Practice formulating the inductive hypothesis clearly.

## Common Misconceptions
- Forgetting the base case.
- Assuming P(k) without explicitly stating the inductive hypothesis.
- Confusing induction with intuitive reasoning by examples.

## Explainer

Think of induction as a domino argument. You have infinitely many dominoes standing in a line, labeled 1, 2, 3, ... You want to show they all fall. The strategy: (1) knock down domino 1 (the **base case**), and (2) verify that whenever domino k has fallen, domino k+1 also falls (the **inductive step**). If both conditions hold, every domino falls — because domino 1 falls, which knocks down domino 2, which knocks down domino 3, and so on forever. Weak induction is just this argument made precise.

In formal terms, weak induction proves a predicate P(n) holds for all natural numbers n ≥ n₀. Your work with predicates and quantified statements prepared you for exactly this: P(n) is a predicate, and we want ∀n ≥ n₀, P(n). The proof has two parts. The **base case** establishes P(n₀) directly — usually by substitution and simple calculation. The **inductive step** assumes P(k) for an arbitrary fixed k (this is the **inductive hypothesis**) and then derives P(k+1). The derivation must actually use the assumption P(k); if it doesn't, something is wrong.

A classic example: prove that 1 + 2 + ... + n = n(n+1)/2. Base case: n=1 gives 1 = 1(2)/2 = 1. ✓. Inductive step: assume the formula holds for k, so 1 + 2 + ... + k = k(k+1)/2. Now consider the sum up to k+1: it equals k(k+1)/2 + (k+1) = (k+1)[k/2 + 1] = (k+1)(k+2)/2, which is the formula with n = k+1. ✓. The key move was taking the assumed result for k and building up to k+1 by adding the next term — the domino step.

The most common error is circular reasoning in the inductive step: students sometimes use P(k+1) to prove P(k+1), which proves nothing. The inductive hypothesis is P(k) — a statement about k — and you must derive P(k+1) from it using valid algebra or logic. A secondary pitfall is treating verification by examples as induction. Checking that the formula holds for n = 1, 2, 3, 4, 5 is not an inductive proof; it establishes only finitely many cases. Induction is powerful precisely because the inductive step is a universal claim — it works for *every* k — and combining it with the base case yields the result for all n at once.
