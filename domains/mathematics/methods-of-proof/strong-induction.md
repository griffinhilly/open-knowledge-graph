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
- induction
- proof
- complete
stage: formal-systems
status: draft
---

# Strong Induction

## Core Idea
Strong induction assumes the statement holds for all values up to n when proving it for n+1, rather than just for n. This stronger hypothesis is necessary when the inductive step depends on multiple previous cases.

## Explainer

From standard (weak) mathematical induction, you know the template: establish a base case, then prove that if the statement holds for n it holds for n+1. This works beautifully when the (n+1)th case depends only on the nth case. But many sequences and combinatorial arguments involve recurrences where the next step depends on several previous steps. **Strong induction** (also called complete induction) modifies the inductive hypothesis to assume the statement holds for *every* integer from the base case up through n — not just for n alone — and then uses that full assumption to prove the (n+1)th case.

Consider the classic example: every integer n ≥ 2 has a prime factorization. The base case n = 2 is trivial (2 is prime). In the inductive step, assume every integer from 2 through n has a prime factorization; prove n+1 does too. If n+1 is prime, it is its own factorization. If n+1 is composite, it factors as n+1 = a · b where 2 ≤ a, b ≤ n. By the strong inductive hypothesis, both a and b have prime factorizations — and multiplying them together gives one for n+1. This argument is impossible with weak induction: when n+1 = a·b is composite, you need the hypothesis for a and b, which could be far smaller than n, not just for the single previous case n.

Another illustrative example: the Fibonacci sequence Fₙ = Fₙ₋₁ + Fₙ₋₂. Any property of Fₙ₊₁ immediately requires knowing both Fₙ and Fₙ₋₁. A weak inductive step that only "inherits" from n cannot reach back to n−1. Strong induction's assumption that the statement holds for all k ≤ n gives you both Fₙ and Fₙ₋₁ simultaneously, making the step go through. The base case here requires establishing two starting values (F₁ and F₂) to cover the initial conditions of the recurrence.

Structurally, strong induction is no more powerful than weak induction — the two are logically equivalent proof principles, and either can simulate the other. The choice is pragmatic: strong induction produces cleaner, more natural proofs whenever the inductive step reaches back more than one step. When writing a strong induction proof, be explicit in the hypothesis ("assume the property holds for all integers k with base ≤ k ≤ n") and verify that the base case covers all special cases at the bottom of the recurrence. The well-ordering principle — that every non-empty set of positive integers has a least element — is closely related and leads to an equivalent proof strategy called minimal counterexample.
