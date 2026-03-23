---
id: mathematical-induction-introduction
title: Introduction to Mathematical Induction
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: direct-proof-introduction
    type: hard
  - id: deductive-vs-inductive-reasoning
    type: hard
  - id: conjectures-and-testing
    type: soft
  - id: number-sequences-patterns
    type: soft
builds-toward:
  - when-is-something-proven
  - mathematical-induction-intro
  - mathematical-induction
  - weak-induction
tags: [induction, proof, natural-numbers, recursion]
stage: abstract-reasoning
status: draft
---

# Introduction to Mathematical Induction

## Core Idea
Mathematical induction is a proof technique for statements about all natural numbers (or all integers from some starting point). It works in two steps. The base case verifies the statement for the first value (usually n = 1 or n = 0). The inductive step proves that if the statement holds for any integer k, then it also holds for k + 1. Together, these two steps create a chain reaction: the base case triggers k = 1 → k = 2 → k = 3 → ... , covering every natural number. Despite its name, mathematical induction is a deductive proof technique — it proves the statement with certainty for all cases.

## How It's Best Learned
Use the domino analogy: if the first domino falls (base case) and each domino knocks down the next (inductive step), then all dominoes fall. Then work through a concrete proof: prove 1 + 2 + 3 + ... + n = n(n+1)/2. Base case: n = 1, 1 = 1(2)/2 = 1. Inductive step: assume the formula holds for k, then show it holds for k + 1 by adding (k+1) to both sides. Have students write the proof themselves before seeing the full version.

## Common Misconceptions
- Confusing mathematical induction (a deductive proof) with inductive reasoning (generalizing from examples). Despite sharing the word "induction," they are fundamentally different. Mathematical induction is rigorous and certain.
- Forgetting the base case. Without it, the inductive step has nothing to start from. The statement "if k works then k+1 works" is useless without a specific k that actually works.
- Assuming the inductive hypothesis is circular reasoning. It is not: you are not assuming the statement is true for all n. You are assuming it for one specific k and proving it for k + 1. The deductive chain then covers all n from the base case onward.

## Questions

```yaml
- question: "In a proof by induction of a statement P(n) for all n ≥ 1, the inductive step proves:"
  type: multiple-choice
  options:
    - "P(1) is true"
    - "P(n) is true for all n"
    - "If P(k) is true, then P(k+1) is true"
    - "P(k) is true for some specific k"
  answer: 2
  explanation: "The inductive step proves the conditional: IF the statement holds for an arbitrary k, THEN it holds for k+1. This is not the same as proving P(n) for all n directly (option B does that only in combination with the base case). Option A is the base case. Option D is the inductive hypothesis, which is assumed, not proven, within the inductive step."

- question: "A proof by induction can succeed without a base case."
  type: true-false
  answer: false
  explanation: "Without a base case, there is no starting point for the chain. Consider the false statement 'all natural numbers are greater than 1000.' The inductive step would say 'if k > 1000, then k+1 > 1000,' which is true — but P(1) is false. Without a verified base case, the dominos never start falling. The base case is what connects the inductive chain to a concrete truth."

- question: "Use induction to prove that 1 + 3 + 5 + ... + (2n-1) = n² for all n ≥ 1."
  type: short-answer
  answer: "Base case: n = 1. The left side is 1, the right side is 1² = 1. True. Inductive step: Assume 1 + 3 + ... + (2k-1) = k². Add (2(k+1)-1) = (2k+1) to both sides: k² + (2k+1) = (k+1)². The left side equals (k+1)², confirming the formula for k+1. By induction, the formula holds for all n ≥ 1."
  explanation: "The inductive step takes the assumed formula for k and extends it to k+1 by adding the next odd number (2k+1). The algebra k² + 2k + 1 = (k+1)² is the key calculation. Combined with the base case, induction covers every natural number."
```

## Explainer

Imagine an infinite line of dominoes. You know two things: the first domino falls, and every domino, when it falls, knocks down the one after it. From these two facts, you can conclude that every domino in the line will fall. Mathematical induction works exactly like this — it proves a statement for every natural number by establishing a base case (the first domino) and an inductive step (each domino triggers the next).

The base case is straightforward: verify that the statement is true for the starting value, usually n = 1. For example, if you want to prove that 1 + 2 + ... + n = n(n+1)/2 for all n ≥ 1, the base case checks n = 1: the left side is 1, the right side is 1(2)/2 = 1. They match, so the base case holds.

The inductive step is the heart of the proof. You assume the statement is true for some arbitrary integer k (this assumption is called the inductive hypothesis), and then you prove it must also be true for k + 1. For the sum formula: assume 1 + 2 + ... + k = k(k+1)/2. Now add (k+1) to both sides. The left side becomes 1 + 2 + ... + k + (k+1). The right side becomes k(k+1)/2 + (k+1) = k(k+1)/2 + 2(k+1)/2 = (k+1)(k+2)/2. This is exactly the formula with n = k + 1. The inductive step is complete.

Students often feel uneasy about the inductive hypothesis: "Aren't we assuming what we want to prove?" No — and this is crucial. You are not assuming the statement is true for all n. You are assuming it for one particular k and proving it for k + 1. The base case establishes truth at n = 1. The inductive step then extends it: since it is true for 1, it must be true for 2 (by the inductive step with k = 1). Since it is true for 2, it must be true for 3 (with k = 2). And so on, forever. The chain of implications is valid because each link is proven, and the chain starts from a proven base case.

One important note about naming: despite the word "induction," mathematical induction is a deductive proof technique. It proves a statement with absolute certainty for all natural numbers. This contrasts with inductive reasoning (observing 1 + 3 = 4, 1 + 3 + 5 = 9, 1 + 3 + 5 + 7 = 16 and guessing the pattern is n²), which provides evidence but not proof. Inductive reasoning helps you discover the conjecture; mathematical induction proves it.
