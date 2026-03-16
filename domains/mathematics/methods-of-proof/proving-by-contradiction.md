---
id: proving-by-contradiction
title: Proving by Contradiction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proving-by-direct-method
  type: hard
- id: tautologies-and-contradictions-classification
  type: soft
- id: negating-quantifiers
  type: soft
builds-toward:
- proving-by-cases
tags:
- proof
- contradiction
- reductio ad absurdum
- indirect
stage: formal-systems
status: draft
---

# Proving by Contradiction

## Core Idea
To prove P, assume ¬P and derive a contradiction. If ¬P leads to a contradiction (a statement that is always false), then ¬P must be false, so P must be true. Contradiction proofs are powerful for establishing results that are hard to derive directly.

## How It's Best Learned
Start with simple contradiction proofs (e.g., proving √2 is irrational). Identify the contradiction clearly and verify it is genuine.

## Common Misconceptions
- Confusing any false statement with a logical contradiction.
- Failing to clearly state what is assumed and what is derived.
- Using the conclusion indirectly in the proof.

## Explainer

You already know from direct proof that a mathematical argument establishes P by starting from known truths and reasoning forward to P. Proof by contradiction takes a different entry point: instead of trying to build a path to P, you ask what would happen if P were false. The logical engine is the **law of excluded middle** — every proposition is either true or false, with no middle ground. If assuming ¬P leads to a logical impossibility (a statement that cannot be true), then ¬P must be false, so P must be true. The formal name for this technique is **reductio ad absurdum** — "reduction to the absurd."

The structure of every contradiction proof follows the same template: (1) clearly state that you are assuming ¬P; (2) derive consequences from ¬P, combined with whatever other facts are available; (3) arrive at a statement of the form "Q and ¬Q" — a statement that is simultaneously asserted true and false. The contradiction is genuine only when Q and ¬Q are exact logical negations of each other. This is where most errors enter: a conclusion can be merely false (given our other assumptions) without being a literal logical contradiction of the form Q ∧ ¬Q. The contradiction must come from the assumption of ¬P itself.

The most famous example — proving √2 is irrational — illustrates why contradiction is sometimes the only viable method. To prove a negative ("√2 is *not* rational") directly would require examining every rational number, which is impossible. Instead, assume √2 = p/q in lowest terms. Squaring both sides gives 2q² = p², so p² is even, so p is even (write p = 2k). Then 2q² = 4k², so q² = 2k², so q is even. But then p and q share a factor of 2, contradicting the assumption that p/q was in lowest terms. The contradiction is concrete and specific — the same fraction cannot simultaneously be in lowest terms and have both numerator and denominator even.

From your study of negating quantifiers and tautologies, you know that negating a statement carefully is essential. When the proposition P has the form "for all x, Q(x)," the negation ¬P is "there exists x such that ¬Q(x)" — not just "Q(x) is false somewhere." Getting the negation precisely right before beginning the proof prevents the error of assuming something weaker than ¬P and then being surprised when the contradiction does not materialize. Contradiction is especially powerful when P is an existence statement, an irrationality claim, or a non-constructive assertion — cases where direct proof would require exhibiting or constructing something that may be hard to find.
