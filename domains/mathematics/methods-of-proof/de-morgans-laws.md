---
id: de-morgans-laws
title: De Morgan's Laws
domain: mathematics
course: methods-of-proof
prerequisites:
- id: logical-equivalences
  type: hard
builds-toward:
- proof-structure-and-terminology
tags:
- equivalence
- negation
- logic
stage: formal-systems
status: draft
---

# De Morgan's Laws

## Core Idea
De Morgan's Laws state that ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q. These laws describe how negation distributes over AND and OR, essential for manipulating logical expressions.

## Explainer

From your study of logical equivalences, you know that two statements are equivalent when they have identical truth tables. De Morgan's Laws are perhaps the most useful equivalences in all of logic — they tell you exactly what happens when you push a negation sign inside a compound statement. The rule is: **negation flips AND to OR and OR to AND**. These two laws are simple to state but surprisingly powerful in practice.

The first law, ¬(p ∧ q) ≡ ¬p ∨ ¬q, says: "not (both p and q)" means "either not-p or not-q." Think of it concretely. Suppose a lock opens only when *both* a key and a code are correct. If the lock fails to open, then either the key was wrong *or* the code was wrong (or both). The failure of a conjunction is a disjunction of failures. The second law, ¬(p ∨ q) ≡ ¬p ∧ ¬q, says: "not (p or q)" means "not-p and not-q." If a door won't open when pushed *or* pulled, then it blocks both pushing *and* pulling. The negation of a disjunction is a conjunction of negations.

Both laws are easily verified with truth tables — a technique from your logical equivalences prerequisite. For any combination of truth values of p and q (TT, TF, FT, FF), the left and right sides of each law always match. But the laws are more useful as *algebraic tools* than as truth table exercises. When writing proofs, you often encounter complex negated statements and need to "expand" them into a usable form. De Morgan's Laws provide the algebra for doing so: ¬(A ∧ B ∧ C) = ¬A ∨ ¬B ∨ ¬C, and ¬(A ∨ B ∨ C) = ¬A ∧ ¬B ∧ ¬C by iterated application.

The laws extend naturally to sets: if A and B are subsets of a universal set U, then (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ and (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ. These are the set-theoretic De Morgan's Laws, and they follow directly from the logical versions by translating "x ∈ A" as a proposition. This connection between logical connectives and set operations (∧ ↔ ∩, ∨ ↔ ∪, ¬ ↔ complement) is one of the deepest unifying patterns in mathematics, and De Morgan's Laws sit at the center of it.
