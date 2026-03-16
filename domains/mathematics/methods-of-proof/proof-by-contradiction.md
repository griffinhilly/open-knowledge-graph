---
id: proof-by-contradiction
title: Proof by Contradiction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: negation-of-quantified-statements
  type: hard
- id: proof-structure-terminology
  type: hard
builds-toward:
- proof-by-cases-exhaustion
tags:
- proof
- contradiction
- reductio-ad-absurdum
stage: formal-systems
status: draft
---

# Proof by Contradiction

## Core Idea
In a proof by contradiction, we assume the negation of our goal and derive a contradiction (a statement that is both true and false). Since the assumption leads to an absurdity, the original statement must be true. This technique works for any statement, not just conditionals, making it versatile for goals that resist direct proof.

## Explainer

Proof by contradiction is one of the most powerful proof strategies because it makes no assumption about what form the proof must take — only about what would follow if you were wrong. From your prerequisites on negation and proof structure, you know that every statement P has a negation ¬P, and that exactly one of them is true in classical logic. The contradiction strategy exploits this: assume ¬P is true, then derive a statement that is both provably true and provably false. Since a contradiction is impossible, the assumption ¬P must be what is wrong — so P must be true. This is **reductio ad absurdum**: reduction to absurdity.

The classic example is proving √2 is irrational. Assume the negation: √2 = p/q for integers p, q with no common factor (in lowest terms). Then p² = 2q², so p² is even, so p must be even (since odd² is always odd), so p = 2k for some integer k. Substituting: 4k² = 2q², so q² = 2k², so q is also even. But now both p and q are even — they share the factor 2 — contradicting the assumption that p/q is in lowest terms. The assumption led to a contradiction, so √2 cannot be rational. Notice that the proof constructs nothing; it works entirely by showing the alternative is impossible.

This non-constructive character is what distinguishes contradiction from direct proof. A **direct proof** builds the conclusion from the hypotheses step by step, producing a positive construction. A proof by contradiction establishes that the opposite is incompatible with what is already known. The technique is especially effective when the conclusion is a negation ("there is no largest prime"), when negating the conclusion gives you powerful structural information to work with (as "√2 is rational" gives you a fraction to manipulate), or when no direct route to the conclusion is visible.

Precise **logical hygiene** is essential. You must negate the entire goal, not a convenient subset of it. If the goal is "if A then B," the negation is "A and not-B" — not simply "not-B." After assuming the negation, you pursue any contradiction, anywhere it leads. The contradiction does not have to be an explicit P ∧ ¬P; it can be any statement already known to be false (like 0 = 1, or a previously proven theorem being violated). Once the contradiction is derived, the assumed negation is discharged and the original statement is established. The proof is complete.
