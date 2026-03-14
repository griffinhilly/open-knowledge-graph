---
id: strong-induction
title: Strong Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: mathematical-induction
  type: hard
builds-toward:
- well-ordering-principle
tags:
- strong-induction
- complete-induction
- induction
- Fibonacci
- prime-factorization
stage: formal-systems
status: validated
---

# Strong Induction

## Core Idea
Strong induction (also called complete induction) modifies the inductive step: instead of assuming only P(k), you assume P(n₀), P(n₀+1), ..., P(k) are all true and then prove P(k+1). This is useful when proving P(k+1) requires not just the immediately preceding case but potentially any earlier one. Strong and weak induction are logically equivalent — each can simulate the other — but strong induction is often more natural for recursive algorithms and number-theoretic arguments.

## How It's Best Learned
Prove that every integer greater than 1 has a prime factorization using strong induction: for k+1, either it is prime (done) or it factors into two integers both less than k+1, each of which has a prime factorization by the strong inductive hypothesis. The Fibonacci sequence also yields natural examples.

## Common Misconceptions
- Thinking strong induction is a 'stronger' or 'more valid' proof than weak induction — they prove the same class of statements.
- Applying strong induction where only weak induction is needed (needless complexity).
- Forgetting to verify all relevant base cases when the inductive step uses several previous cases.
