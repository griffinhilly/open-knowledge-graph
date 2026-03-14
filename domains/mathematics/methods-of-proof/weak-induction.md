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
