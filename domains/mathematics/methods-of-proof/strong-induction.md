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

## Questions

```yaml
- question: "You want to prove that every amount of postage ≥ 12 cents can be made from 4-cent and 5-cent stamps. To show amount n+1 works, you argue: if n+1 ≥ 17, subtract a 4-cent stamp to get n−3, which must be achievable. But n−3 could be far less than n. Which proof technique is required?"
  type: multiple-choice
  options:
    - "Weak induction — you only need the previous case (n) to prove n+1."
    - "Strong induction — the step for n+1 may require cases far below n, not just n itself."
    - "Direct proof — the result can be verified without induction by a closed-form argument."
    - "Proof by contradiction — assume postage n+1 is impossible and derive a contradiction."
  answer: 1
  explanation: "Weak induction hands you only the hypothesis that n works. But when n+1 = 17, you need the hypothesis for 17 − 4 = 13, which could be far below n. Weak induction's single-step hypothesis doesn't reach back to 13. Strong induction's hypothesis — 'all values from the base case up through n work' — covers 13 directly, making the step go through. Whenever the inductive step looks back more than one case, strong induction is the natural tool."

- question: "Why does the proof that every integer n ≥ 2 has a prime factorization require strong induction rather than weak induction?"
  type: multiple-choice
  options:
    - "Because n+1 may not equal the 'next' integer in the context of factorization."
    - "Because if n+1 is composite, its factors a and b satisfy 2 ≤ a, b < n+1 — requiring the hypothesis for values other than n."
    - "Because the base case n = 2 is insufficient to start the induction."
    - "Because weak induction does not apply when the domain starts at 2 rather than 1."
  answer: 1
  explanation: "If n+1 is composite, it factors as a·b with 2 ≤ a, b < n+1. To argue both a and b have prime factorizations, you need the inductive hypothesis at a and b — which could be as small as 2. Weak induction gives you only the hypothesis at n, which is useless when a = 3 and n = 100. Strong induction's hypothesis 'all integers from 2 through n have prime factorizations' covers every possible factor pair, making the step work for all composite values of n+1."

- question: "Strong induction is logically more powerful than weak (ordinary) induction — there exist theorems that can be proved by strong induction but not by weak induction."
  type: true-false
  answer: false
  explanation: "Strong and weak induction are logically equivalent. Any proof by strong induction can be converted to a proof by weak induction by reformulating the predicate: instead of P(n), use Q(n) defined as 'P(k) holds for all k from the base case up to n.' Then weak induction on Q(n) simulates strong induction on P(n) exactly. The choice between them is purely pragmatic: strong induction produces cleaner proofs when the step naturally reaches back multiple cases, without any gain in logical strength."

- question: "When using strong induction on a property involving the Fibonacci recurrence Fₙ = Fₙ₋₁ + Fₙ₋₂, the base case must establish the property for both F₁ and F₂."
  type: true-false
  answer: true
  explanation: "The Fibonacci step for F₃ requires both F₂ and F₁. If only F₁ is verified as the base case, the strong inductive hypothesis for n = 2 has only one data point (F₁), and the step for F₃ cannot draw on F₂. You must establish all initial values needed by the recurrence before the strong hypothesis has enough coverage to carry the step. In general, for a recurrence looking back k steps, the base case must verify k starting values."

- question: "Explain why the inductive step in a strong induction proof can 'look back' multiple cases, and why weak induction's hypothesis is insufficient in those situations."
  type: short-answer
  answer: "Weak induction's hypothesis at step n+1 is only 'P(n) holds.' If the proof of P(n+1) requires P(k) for some k < n, that hypothesis simply does not cover it — the step fails. Strong induction's hypothesis is 'P(k) holds for all k from the base case through n,' which covers every value below n+1 no matter how far back the step reaches. The inductive step can freely cite P(2), P(7), or P(n−3) alike. The tradeoff is only notational: you must state the hypothesis carefully and ensure the base case covers all special cases at the bottom of the recurrence."
  explanation: "Logically, strong induction is no stronger — the two forms are equivalent. But strong induction makes the fuller hypothesis explicit and available at each step, producing proofs that mirror the structure of the argument (especially for recurrences, divisibility arguments, and combinatorial decompositions). The key diagnostic question when drafting an inductive proof is: does the step use only P(n), or does it need P(k) for some k < n? If the latter, use strong induction from the start."
```

## Explainer

From standard (weak) mathematical induction, you know the template: establish a base case, then prove that if the statement holds for n it holds for n+1. This works beautifully when the (n+1)th case depends only on the nth case. But many sequences and combinatorial arguments involve recurrences where the next step depends on several previous steps. **Strong induction** (also called complete induction) modifies the inductive hypothesis to assume the statement holds for *every* integer from the base case up through n — not just for n alone — and then uses that full assumption to prove the (n+1)th case.

Consider the classic example: every integer n ≥ 2 has a prime factorization. The base case n = 2 is trivial (2 is prime). In the inductive step, assume every integer from 2 through n has a prime factorization; prove n+1 does too. If n+1 is prime, it is its own factorization. If n+1 is composite, it factors as n+1 = a · b where 2 ≤ a, b ≤ n. By the strong inductive hypothesis, both a and b have prime factorizations — and multiplying them together gives one for n+1. This argument is impossible with weak induction: when n+1 = a·b is composite, you need the hypothesis for a and b, which could be far smaller than n, not just for the single previous case n.

Another illustrative example: the Fibonacci sequence Fₙ = Fₙ₋₁ + Fₙ₋₂. Any property of Fₙ₊₁ immediately requires knowing both Fₙ and Fₙ₋₁. A weak inductive step that only "inherits" from n cannot reach back to n−1. Strong induction's assumption that the statement holds for all k ≤ n gives you both Fₙ and Fₙ₋₁ simultaneously, making the step go through. The base case here requires establishing two starting values (F₁ and F₂) to cover the initial conditions of the recurrence.

Structurally, strong induction is no more powerful than weak induction — the two are logically equivalent proof principles, and either can simulate the other. The choice is pragmatic: strong induction produces cleaner, more natural proofs whenever the inductive step reaches back more than one step. When writing a strong induction proof, be explicit in the hypothesis ("assume the property holds for all integers k with base ≤ k ≤ n") and verify that the base case covers all special cases at the bottom of the recurrence. The well-ordering principle — that every non-empty set of positive integers has a least element — is closely related and leads to an equivalent proof strategy called minimal counterexample.
