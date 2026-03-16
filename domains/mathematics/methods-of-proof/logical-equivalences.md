---
id: logical-equivalences
title: Logical Equivalences
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables
  type: hard
builds-toward:
- de-morgans-laws
- proof-structure-and-terminology
tags:
- equivalence
- transformation
- logic
stage: formal-systems
status: draft
---

# Logical Equivalences

## Core Idea
Two statements are logically equivalent if they have identical truth values in all cases. Key equivalences like p → q ≡ ¬p ∨ q allow rewriting statements in different forms, essential for proof construction.

## Explainer

From your work with truth tables, you know how to determine whether a compound statement is true or false for any specific combination of truth values. Logical equivalence takes that one step further: two statements are **logically equivalent** if their truth tables are identical column by column — they match in every single row, not just some. When P ≡ Q, you can replace one with the other anywhere in a proof without changing whether the proof is valid.

The most important equivalence in proof writing is the **contrapositive**: the statement "if p then q" (p → q) is logically equivalent to "if not q then not p" (¬q → ¬p). You can verify this with a truth table — both are false only when p is true and q is false, and true in every other case. Why does this matter? Because sometimes "if p then q" is hard to prove directly, while "if not q then not p" has a clear attack. Proving the contrapositive is not a trick or an approximation — it is exactly the same claim, just phrased differently.

A second critical equivalence rewrites implication as disjunction: p → q ≡ ¬p ∨ q. Reading it aloud: "if p then q" says the same thing as "either p is false, or q is true." This equivalence shows up constantly when manipulating logical expressions and when converting between different proof strategies. For example, to prove p → q, it suffices to assume p is true and show q follows — because if p is false, the disjunction ¬p ∨ q is already true. The equivalence explains why proof by assuming the hypothesis is valid: you're simply exploiting this rewriting.

A third family of equivalences is **De Morgan's laws**: ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q. These tell you how negation distributes over "and" and "or" — and the distribution flips the connective. Negating "it's raining and it's cold" yields "it's not raining or it's not cold," not "it's not raining and it's not cold." Fluency with these transformations is what allows you to negate complex mathematical statements correctly — an essential skill for proof by contradiction and proof by contrapositive that you'll use throughout mathematics.
