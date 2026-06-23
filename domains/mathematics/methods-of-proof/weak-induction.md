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
- id: mathematical-induction-introduction
  type: hard
builds-toward:
- strong-induction-and-wellordering
tags:
- proof
- induction
- mathematical induction
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A student wants to prove P(n) for all n ≥ 1. They show P(1) is true, then write an inductive step that appears to derive P(k+1) — but on close inspection, one algebraic step secretly assumes P(k+1) is true in order to simplify an expression. What is wrong with this proof?"
  type: multiple-choice
  options:
    - "Nothing — the algebra is internally consistent and the proof is valid"
    - "The base case should be verified for n=0 as well, not just n=1"
    - "The proof is circular: it uses P(k+1) to establish P(k+1), which proves nothing"
    - "The inductive hypothesis was not written out explicitly enough"
  answer: 2
  explanation: "The inductive step must derive P(k+1) using only P(k) (the inductive hypothesis) and valid logic or algebra. If P(k+1) is assumed anywhere during the derivation, the argument is circular — you've proven 'if P(k+1) then P(k+1),' which is a tautology. This error is common because students recognize what they want to arrive at and unconsciously use it to simplify. The fix is to start only from P(k) and valid algebraic moves, never touching P(k+1) until you've derived it."

- question: "A student verifies that the formula 1 + 2 + ⋯ + n = n(n+1)/2 holds for n = 1, 2, 3, …, 20. What has the student accomplished?"
  type: multiple-choice
  options:
    - "A proof valid for all positive integers, since 20 cases establishes the pattern"
    - "A proof by strong induction covering the first 20 cases"
    - "A verification of finitely many cases — not a proof that the formula holds for all n"
    - "A sufficient base case collection for a standard inductive proof"
  answer: 2
  explanation: "Verification of finitely many cases — even many cases — is not a proof for all natural numbers. Induction is powerful precisely because the inductive step is a universal claim: if P(k) then P(k+1) for *every* k. Combined with the base case, this chain reaches every natural number. Checking examples only establishes finitely many instances; no finite number of checks can rule out a counterexample at n = 1,000,000 or beyond."

- question: "In the inductive step of a weak induction proof, you may assume P(k) is true for an arbitrary fixed k — this assumption is what allows you to derive P(k+1)."
  type: true-false
  answer: true
  explanation: "Correct. The inductive hypothesis is the assumption that P(k) holds for some fixed (but arbitrary) k. 'Arbitrary' is crucial: we're not assuming it for a specific number, but for a generic k that could be any value in the domain. The derivation that follows must use this assumption to logically arrive at P(k+1). If the derivation does not actually use P(k), something is likely wrong — either the proof is trivial or the argument is circular."

- question: "A proof by weak induction is complete once you have verified the base case, because the inductive step just repeats the same calculation for the next value."
  type: true-false
  answer: false
  explanation: "The base case alone proves only P(1) — one specific instance. The inductive step is not a repeated calculation; it is a conditional proof that *for any* k, P(k) implies P(k+1). Only when both parts are in place does the chain reaction start: P(1) is true, so P(2) is true (by the inductive step with k=1); P(2) is true, so P(3) is true (with k=2); and so on through all natural numbers. Without the inductive step, you've proven nothing beyond the base case."

- question: "What makes mathematical induction a valid proof technique rather than just an extended pattern check? Why does proving P(1) and 'P(k) implies P(k+1)' actually establish P(n) for all n?"
  type: short-answer
  answer: "Induction is valid because the inductive step is a universal conditional — it holds for every k without exception. Once we know P(1) (domino 1 falls) and that any true P(k) forces P(k+1) to be true (any fallen domino knocks down the next), the entire infinite sequence is determined: P(1) is true, so P(2) must be true; P(2) is true, so P(3) must be true; and this chain extends indefinitely. There is no gap and no stopping point. By contrast, checking examples only covers finitely many cases and leaves infinitely many unchecked."
  explanation: "The key is that 'P(k) implies P(k+1)' is a statement about *all* k, not just specific ones. Combined with P(1), it creates an unbroken chain of logical consequences stretching across all natural numbers. This is fundamentally different from pattern recognition: patterns can fail at large n, but a valid inductive step cannot, because it applies universally."
```

## Explainer

Think of induction as a domino argument. You have infinitely many dominoes standing in a line, labeled 1, 2, 3, ... You want to show they all fall. The strategy: (1) knock down domino 1 (the **base case**), and (2) verify that whenever domino k has fallen, domino k+1 also falls (the **inductive step**). If both conditions hold, every domino falls — because domino 1 falls, which knocks down domino 2, which knocks down domino 3, and so on forever. Weak induction is just this argument made precise.

In formal terms, weak induction proves a predicate P(n) holds for all natural numbers n ≥ n₀. Your work with predicates and quantified statements prepared you for exactly this: P(n) is a predicate, and we want ∀n ≥ n₀, P(n). The proof has two parts. The **base case** establishes P(n₀) directly — usually by substitution and simple calculation. The **inductive step** assumes P(k) for an arbitrary fixed k (this is the **inductive hypothesis**) and then derives P(k+1). The derivation must actually use the assumption P(k); if it doesn't, something is wrong.

A classic example: prove that 1 + 2 + ... + n = n(n+1)/2. Base case: n=1 gives 1 = 1(2)/2 = 1. ✓. Inductive step: assume the formula holds for k, so 1 + 2 + ... + k = k(k+1)/2. Now consider the sum up to k+1: it equals k(k+1)/2 + (k+1) = (k+1)[k/2 + 1] = (k+1)(k+2)/2, which is the formula with n = k+1. ✓. The key move was taking the assumed result for k and building up to k+1 by adding the next term — the domino step.

The most common error is circular reasoning in the inductive step: students sometimes use P(k+1) to prove P(k+1), which proves nothing. The inductive hypothesis is P(k) — a statement about k — and you must derive P(k+1) from it using valid algebra or logic. A secondary pitfall is treating verification by examples as induction. Checking that the formula holds for n = 1, 2, 3, 4, 5 is not an inductive proof; it establishes only finitely many cases. Induction is powerful precisely because the inductive step is a universal claim — it works for *every* k — and combining it with the base case yields the result for all n at once.
