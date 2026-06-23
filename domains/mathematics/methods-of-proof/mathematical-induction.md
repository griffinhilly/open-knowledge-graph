---
id: mathematical-induction
title: Mathematical Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-by-cases
  type: hard
- id: mathematical-induction-introduction
  type: hard
builds-toward:
- strong-induction
tags:
- induction
- proof
- recursion
stage: formal-systems
status: validated
---

# Mathematical Induction

## Core Idea
Mathematical induction proves statements about natural numbers by (1) proving the base case (n=1), and (2) proving that if true for n=k, then true for n=k+1. This establishes a logical chain covering all natural numbers.

## Questions

```yaml
- question: "In a proof by induction that a statement P(n) holds for all natural numbers, the inductive step proves:"
  type: multiple-choice
  options:
    - "P(n) is true for every specific value of n"
    - "If P(k) is true, then P(k+1) is true"
    - "P(1) and P(2) are true, so P(n) is true for all n"
    - "P(k+1) is directly true for all k"
  answer: 1
  explanation: "The inductive step proves the conditional: IF P(k) holds, THEN P(k+1) holds. It does not prove P(k+1) outright — it only establishes the implication. The base case then provides the starting truth (P(1) is true), and repeated application of the conditional propagates truth to every natural number."

- question: "A proof that checks P(1), P(2), P(3), ..., P(100) for a statement about natural numbers constitutes a valid proof that P(n) holds for most n."
  type: true-false
  answer: false
  explanation: "Checking finitely many cases — no matter how many — never proves a universal statement. There are infinitely many natural numbers, so any finite check leaves infinitely many cases unverified. Induction is powerful precisely because the inductive step is a general conditional that covers all k simultaneously, not a case-by-case check."

- question: "Why is the base case necessary in a proof by induction? What goes wrong if you skip it?"
  type: short-answer
  answer: "Without the base case, the inductive step gives you only a chain of conditionals with no starting truth. The argument would show P(1) → P(2) → P(3) → ... but never establish that P(1) is actually true, so the chain never 'fires.' A proof without a base case can appear to prove false statements."
  explanation: "A classic example of a broken induction is 'all horses are the same color' — the inductive step has a hidden flaw, but it illustrates that the structure of induction requires both parts. The base case is the seed; the inductive step is the propagation rule. Without the seed, no propagation occurs."
```

## Explainer

Mathematical induction is one of the most elegant proof techniques in mathematics because it lets you prove a statement about *infinitely many* cases with a finite argument. The idea is a logical domino effect: prove that the first domino falls (base case), and prove that each domino knocks over the next (inductive step). Together, these two facts guarantee that every domino in an infinite row will eventually fall.

More precisely, suppose you want to prove a statement P(n) for all natural numbers n ≥ 1. The proof has two parts. First, the *base case*: verify directly that P(1) is true. Second, the *inductive step*: assume P(k) is true for some arbitrary k (this assumption is called the *inductive hypothesis*), and then use that assumption to prove P(k+1) is true. If both parts succeed, you have proven P(n) for all n.

The inductive hypothesis is what makes induction feel different from ordinary proof. You are *assuming* the very thing you want to prove — but only for a single arbitrary case k, not for all n. You are not being circular; you are setting up a conditional. "IF P(k) is true THEN P(k+1) is true" is a perfectly valid implication to prove, and once you have it, you apply it starting from k=1: since P(1) is true, P(2) is true; since P(2) is true, P(3) is true; and so on forever.

A standard first example is the sum formula: 1 + 2 + 3 + ... + n = n(n+1)/2. Base case: n=1 gives 1 = 1(2)/2 = 1 ✓. Inductive step: assume 1+2+...+k = k(k+1)/2. Then 1+2+...+k+(k+1) = k(k+1)/2 + (k+1) = (k+1)(k/2 + 1) = (k+1)(k+2)/2, which is the formula with k+1 substituted. Both steps work, so the formula holds for all n ≥ 1. Notice how the inductive hypothesis was the essential tool in the algebra.

Because you have already studied proof by cases, you know that proving something for all cases requires covering every case. Induction is a way to cover infinitely many cases systematically. The connection to recursion is also worth noting: recursive algorithms often work precisely because they do a small amount of work and then call themselves on a smaller input — and induction is the proof technique that verifies such recursive reasoning is sound. You will use induction again when you study sequences, series, divisibility, and data structures.
