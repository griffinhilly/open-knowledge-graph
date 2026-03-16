---
id: statements-and-logical-connectives
title: Statements and Logical Connectives
domain: mathematics
course: methods-of-proof
prerequisites: []
builds-toward:
- truth-tables-intro
- logical-equivalences-intro
tags:
- logic
- foundations
- statements
stage: formal-systems
status: draft
---

# Statements and Logical Connectives

## Core Idea
A logical statement is a declarative sentence that is either true or false, never both. Logical connectives—AND, OR, NOT, IF-THEN—combine simple statements into compound statements, allowing us to express complex logical relationships precisely. Mastering these connectives is the foundation for all formal reasoning.

## Explainer

Mathematics is built on precise claims, and the first tool of precision is identifying what can be true or false. A **statement** (also called a **proposition**) is a declarative sentence with a definite truth value: "17 is prime" is true; "the square root of 4 is 3" is false. By contrast, "is 17 prime?" (a question) and "let x be a number" (a command) are not statements — they have no truth value. The discipline of logic begins by demanding that every sentence we reason about be a statement in this strict sense.

**Logical connectives** combine simple statements into compound ones. The **conjunction** "P AND Q" (written P ∧ Q) is true only when both P and Q are true simultaneously. The **disjunction** "P OR Q" (written P ∨ Q) is true when at least one is true — mathematical "or" is inclusive, unlike the everyday "either/or" which excludes the both-true case. The **negation** "NOT P" (written ¬P) flips the truth value: if P is "x > 5," then ¬P is "x ≤ 5." Each connective has a precise definition that a truth table captures exhaustively — listing every combination of truth values for the component statements and the resulting truth value of the compound.

The most important connective for mathematical reasoning is **implication**: "IF P THEN Q" (written P → Q). It asserts that whenever P is true, Q must also be true. Crucially, P → Q is false only when P is true but Q is false — a true hypothesis leading to a false conclusion is the only way to violate a conditional claim. When P is false, P → Q is **vacuously true** regardless of Q. This surprises newcomers: "If the moon is made of cheese, then 2 + 2 = 5" is logically true, because the hypothesis is false. The implication made a promise only about what happens when P holds — and P never holds.

These four connectives (AND, OR, NOT, IF-THEN) are enough to express any logical relationship precisely. Every mathematical theorem is ultimately a statement — often an implication — built from simpler components. The rules for manipulating these connectives (like the equivalence P → Q ≡ ¬P ∨ Q, or De Morgan's laws) let you transform statements while preserving truth, which is exactly what a mathematical proof does. Mastering the meaning of each connective, especially the surprising cases of vacuous truth and inclusive or, prevents the logical errors that invalidate proofs before they even begin.
