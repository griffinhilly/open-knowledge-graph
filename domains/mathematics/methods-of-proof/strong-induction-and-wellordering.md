---
id: strong-induction-and-wellordering
title: Strong Induction and Well-Ordering Principle
domain: mathematics
course: methods-of-proof
prerequisites:
- id: weak-induction
  type: hard
tags:
- proof
- strong induction
- well-ordering
stage: formal-systems
status: draft
---

# Strong Induction and Well-Ordering Principle

## Core Idea
Strong induction assumes all values from the base case up to k (not just P(k)) to prove P(k+1). This is logically equivalent to weak induction but sometimes more convenient. The well-ordering principle states that every non-empty set of positive integers has a smallest element; it is logically equivalent to induction. Strong induction is useful for recursive proofs.

## How It's Best Learned
Identify problems where assuming multiple previous cases simplifies the proof. Compare weak and strong induction on the same problem to see when strong induction helps.

## Common Misconceptions
- Thinking strong induction is stronger or easier than weak induction (they are equivalent).
- Forgetting that the well-ordering principle applies to subsets of positive integers.
- Using strong induction when weak induction suffices.
