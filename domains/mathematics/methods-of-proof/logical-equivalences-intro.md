---
id: logical-equivalences-intro
title: Logical Equivalences and Laws
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables-intro
  type: hard
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- conditional-and-biconditional-statements
- proof-by-contrapositive
tags:
- logic
- equivalence
- simplification
stage: formal-systems
status: draft
---

# Logical Equivalences and Laws

## Core Idea
Two statements are logically equivalent if they have identical truth values in all possible conditions. Key laws like De Morgan's laws, commutativity, and associativity allow us to transform and simplify logical statements while preserving their logical content. These transformations are essential tools for proof techniques.

## Explainer

From your work with truth tables, you know how to evaluate a compound statement row by row. **Logical equivalence** goes one step further: two statements P and Q are logically equivalent (written P ≡ Q) if their truth tables are identical — every possible assignment of truth values to the atomic components produces the same result for both P and Q. This is not just "they usually agree" — they must agree in every case, with no exceptions. The symbol ≡ means "is the same logical object as," just expressed differently.

Think of logical equivalences as algebraic identities for logic. Just as the algebraic identity a(b + c) = ab + ac lets you rewrite expressions without changing their value, logical laws let you rewrite compound statements into equivalent but simpler or more useful forms. The most important laws are **De Morgan's laws**: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q, and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q. In words: "not (A and B)" means "not A or not B"; "not (A or B)" means "not A and not B." These let you push negations inward through conjunctions and disjunctions, a maneuver you will use constantly in proofs.

Other essential equivalences include: commutativity (P ∧ Q ≡ Q ∧ P), associativity, distributivity, double negation (¬¬P ≡ P), and the **contrapositive** equivalence (P → Q) ≡ (¬Q → ¬P). The contrapositive equivalence is particularly powerful: it says that proving "if P then Q" is logically identical to proving "if not Q then not P." When the direct route (assume P, prove Q) is difficult, you can flip to the contrapositive form without changing what you're proving. This is proof by contrapositive — one of the core techniques your next topics cover.

Logical equivalences also give you a mechanical way to simplify premises and conclusions. If you have a complex hypothesis like ¬(P ∧ ¬Q), De Morgan's law turns it into ¬P ∨ Q, which by another equivalence is just P → Q. That simplification can make the structure of a proof much clearer. Mastering these transformations means you can fluidly rewrite any logical statement into whatever form is most convenient — direct, contrapositive, or proof by contradiction — without losing logical content.
