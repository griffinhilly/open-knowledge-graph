---
id: conditional-and-biconditional
title: Conditional and Biconditional Statements
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- logical-equivalences
- contrapositive-converse-and-inverse
tags:
- implication
- if-then
- logic
stage: formal-systems
status: draft
---

# Conditional and Biconditional Statements

## Core Idea
The conditional 'if p then q' (p → q) is false only when p is true and q is false; in all other cases it is true. The biconditional 'p if and only if q' (p ↔ q) is true when both have the same truth value.

## How It's Best Learned
Relate conditionals to everyday reasoning: 'If it rains, the ground is wet' is false only if it rains but the ground stays dry.

## Common Misconceptions
- Assuming p → q is true whenever q is true, regardless of p.
- Confusing 'if' with 'if and only if'.

## Explainer

From your work with logical connectives, you know that AND, OR, and NOT have truth tables that match ordinary language fairly closely. The **conditional** p → q (read "if p then q") is the connective that tends to trip people up, because its truth table diverges from everyday intuition in one row. Let's build it from scratch. If p is true and q is true — it rained and the ground is wet — then "if it rains, the ground is wet" looks true. If p is true and q is false — it rained but the ground is dry — then the conditional is clearly *false*; the promised relationship failed. Those two cases are uncontroversial.

The confusing cases are when p is false. If it didn't rain, can "if it rains, the ground is wet" be false? Consider the speaker's commitment: they promised that *whenever* it rains, the ground gets wet. If it never rains today, the promise is never tested — you can't accuse them of lying. The standard convention in classical logic is to call a conditional **true** whenever its hypothesis is false, regardless of whether the conclusion is true or false. This is called **vacuous truth**. It allows universal statements like "all prime numbers greater than 2 are odd" to be true even though we never verify the claim for each prime individually — we just confirm the pattern holds whenever the hypothesis applies.

The truth table is therefore: p → q is false in exactly one row (T, F), and true in all three others. A useful reading is "p → q says p is sufficient for q, or equivalently q is necessary for p." If you know it rained (p), you're guaranteed the ground is wet (q); if you know the ground is dry (not q), you're guaranteed it didn't rain (not p). This second statement — not q → not p — is the **contrapositive**, and it is logically equivalent to the original. Proofs by contrapositive exploit this equivalence: rather than assuming p and proving q, you assume not q and prove not p.

The **biconditional** p ↔ q (read "p if and only if q") is simply the conjunction of both conditionals at once: (p → q) AND (q → p). It is true precisely when p and q have the same truth value — both true or both false. In mathematics, "if and only if" (often abbreviated "iff") signals a claim of equivalence: the two conditions are interchangeable. When a definition says "a number is even if and only if it is divisible by 2," it means divisibility by 2 is not merely a consequence of being even — it is the *exact same property*, just phrased differently. Learning to recognize which direction (or both directions) a proof requires is one of the most practical skills in rigorous mathematics.
