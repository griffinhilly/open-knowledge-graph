---
id: proof-by-contrapositive
title: Proof by Contrapositive
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-and-biconditional-statements
  type: hard
- id: proof-structure-terminology
  type: hard
tags:
- proof
- contrapositive
stage: formal-systems
status: draft
---

# Proof by Contrapositive

## Core Idea
To prove 'If P then Q', we can instead prove the contrapositive: 'If not Q then not P'. Since a conditional and its contrapositive are logically equivalent, proving one proves the other. This technique is powerful when the contrapositive is easier to establish than the original statement or when assuming the negation of the conclusion leads naturally to the negation of the hypothesis.

## Explainer

You already know from your work with conditional statements that "If P then Q" (P → Q) is equivalent to its **contrapositive** "If ¬Q then ¬P" (¬Q → ¬P). This equivalence is not a trick — it is a straightforward fact from truth tables: P → Q is false only when P is true and Q is false, which is exactly when ¬Q is true and ¬P is false. The two statements have identical truth tables in every case. Proof by contrapositive simply exploits this: instead of assuming P and deriving Q, you assume ¬Q and derive ¬P.

The strategic question is: when should you choose the contrapositive over a direct proof? The signal is almost always in the *form* of the conclusion. If Q is a positive statement ("x is rational," "n is divisible by 4"), its negation ¬Q may open useful algebraic handles ("x is irrational," "n is not divisible by 4"). Consider proving: "If n² is odd, then n is odd." Going directly, you must somehow derive a property of n from a property of n². Going via the contrapositive — "If n is even, then n² is even" — is immediate: if n = 2k, then n² = 4k², which is even. The contrapositive flows naturally; the direct proof would require working backwards.

The mechanics are straightforward. Write down the contrapositive: ¬Q → ¬P. State "We prove the contrapositive." Assume ¬Q. Derive ¬P using whatever tools apply. Conclude that ¬Q → ¬P, and therefore P → Q. That final logical step — invoking the equivalence — closes the proof. This is not "assuming the conclusion"; you are proving a *different but equivalent* statement directly, then transferring the result.

It helps to contrast contrapositive with **proof by contradiction**, which students often conflate. Contrapositive: assume ¬Q, prove ¬P — you reach a positive conclusion. Contradiction: assume both P and ¬Q, derive any falsehood — you reach an impossibility. Both methods involve negating the conclusion, but they differ in structure and what they produce. Contrapositive is the cleaner tool when ¬Q is a productive assumption in its own right; contradiction is better when the only path forward is showing that something impossible follows from all assumptions taken together.
