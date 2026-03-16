---
id: truth-tables-intro
title: Truth Tables and Truth Conditions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- logical-equivalences-intro
- conditional-and-biconditional-statements
tags:
- logic
- truth-values
- systematic-reasoning
stage: formal-systems
status: draft
---

# Truth Tables and Truth Conditions

## Core Idea
A truth table systematically lists all possible truth value assignments for a statement's components and shows the resulting truth value. Truth tables provide a mechanical, exhaustive method for determining when compound statements are true or false under all possible conditions, eliminating ambiguity from logical reasoning.

## Explainer

You know that logical connectives like AND (∧), OR (∨), NOT (¬), and the conditional (→) have meanings in ordinary language. But ordinary language is imprecise: "or" can mean "one or the other but not both" or "at least one of them," and "if…then" carries causal implications that formal logic strips away. A **truth table** makes these meanings completely precise by exhaustively listing every possible combination of truth values and specifying the output for each combination according to a fixed rule.

The construction is mechanical. A compound statement with n atomic components has 2ⁿ possible truth value assignments — two choices (true or false) per component. You write one row per assignment, then evaluate the compound statement in each row using the definitions of the connectives. For ¬P: flip the truth value. For P ∧ Q: true only when both are true. For P ∨ Q: true when at least one is true. For P → Q: false only when P is true and Q is false — the conditional "breaks its promise" only in that case. For P ↔ Q: true when both have the same truth value. Each connective has a fixed, completely mechanical rule with no room for interpretation.

The power of truth tables goes beyond evaluating a single statement. A **tautology** is a statement that is true in every row — it is logically necessary regardless of the truth values of its components. De Morgan's laws (¬(P ∧ Q) ≡ ¬P ∨ ¬Q) and the equivalence between P → Q and ¬P ∨ Q are tautologies you can verify by checking that no row makes them false. A **contradiction** is false in every row. Two statements are **logically equivalent** when their truth tables match column-for-column under identical inputs — this is a mechanical test for equivalence that requires no insight or intuition.

Truth tables also provide a formal criterion for **validity** of an argument. An argument is valid when every row that makes all the premises true also makes the conclusion true — there is no possible assignment of truth values that satisfies the premises but falsifies the conclusion. This is how you verify that modus ponens is valid and how you expose that affirming the consequent is invalid: there exist rows where P → Q and Q are both true but P is false, showing the argument can fail. Validity is a purely structural guarantee about the relationship between premises and conclusion, independent of whether the premises are actually true.
