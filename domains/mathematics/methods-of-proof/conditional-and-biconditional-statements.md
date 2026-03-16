---
id: conditional-and-biconditional-statements
title: Conditional and Biconditional Statements
domain: mathematics
course: methods-of-proof
prerequisites:
- id: logical-equivalences-intro
  type: hard
builds-toward:
- proof-by-contrapositive
- proof-by-contradiction
tags:
- logic
- if-then
- conditionals
- biconditionals
stage: formal-systems
status: draft
---

# Conditional and Biconditional Statements

## Core Idea
A conditional statement 'If P, then Q' (P → Q) is false only when P is true and Q is false; otherwise it is true. A biconditional 'P if and only if Q' (P ↔ Q) is true when both statements have the same truth value. Understanding the contrapositive—'If not Q then not P'—is crucial: it is logically equivalent to the original conditional.

## Explainer

The **conditional statement** "If P, then Q" is the sentence structure of almost every mathematical theorem. "If n is even, then n² is even." "If a function is differentiable, then it is continuous." Learning to handle these statements precisely is not just symbol-pushing — it's the grammar of mathematical argument. From your work with logical equivalences, you know how truth tables work. The key fact about P → Q is its truth table: it is false in exactly one case, when P is true and Q is false. Every other combination is true, including the case where P is false — a conditional with a false hypothesis is **vacuously true**.

Vacuous truth trips up beginners but makes logical sense. The statement "If the moon is made of cheese, then 2 + 2 = 5" is true, because the hypothesis is false. No promise is broken. A conditional only makes a commitment when P holds; if P never fires, no violation can occur. In mathematics this matters when you say "for every x in this set, if P(x) then Q(x)" — if the set is empty or P(x) is never satisfied, the statement is vacuously true.

The **contrapositive** of P → Q is ¬Q → ¬P, and these two statements are logically equivalent — they have the same truth value in all cases. This equivalence is one of the most useful tools in proof-writing. When proving "if n² is even, then n is even" is difficult directly, the contrapositive "if n is odd, then n² is odd" is often easier to verify. Recognizing that switching to the contrapositive is not a trick but a logical equivalence is the key insight. Contrast the contrapositive with the **converse** (Q → P) and the **inverse** (¬P → ¬Q): these are related but neither is equivalent to the original conditional in general.

The **biconditional** P ↔ Q means "P if and only if Q" — often abbreviated "P iff Q." It is true when P and Q have the same truth value: both true or both false. In mathematical proofs, establishing a biconditional requires showing two directions: P → Q and Q → P. When a theorem says "A is equivalent to B," it means A ↔ B. Learning to decompose biconditionals into two conditionals and prove each direction separately is a fundamental proof strategy you will use constantly in courses like real analysis and abstract algebra.
