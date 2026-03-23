---
id: truth-tables-introduction
title: Introduction to Truth Tables
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: conditional-statements-formal
    type: hard
  - id: variables-in-logic
    type: hard
  - id: true-false-statements
    type: soft
builds-toward:
  - logical-equivalence-intro
  - truth-tables-intro
  - formula-evaluation-and-truth-tables
tags: [truth-tables, logic, connectives, evaluation]
stage: abstract-reasoning
status: draft
---

# Introduction to Truth Tables

## Core Idea
A truth table is a systematic way to list every possible combination of truth values for the variables in a logical expression and determine the resulting truth value. For a statement with two variables P and Q, there are four possible combinations (TT, TF, FT, FF). Truth tables let you see exactly when a compound statement is true and when it is false, removing all ambiguity. They are the foundation for checking validity, identifying logical equivalences, and understanding how logical connectives (AND, OR, NOT, IF-THEN) behave.

## How It's Best Learned
Start with NOT (one variable, two rows), then AND and OR (two variables, four rows). Build tables step by step, column by column. Then build the truth table for P → Q and confront the vacuous truth rows directly. Have students predict the output before computing each row. Compare AND vs. OR truth tables side by side to highlight the difference. Then use truth tables to verify that P → Q and ¬Q → ¬P (contrapositive) produce identical columns.

## Common Misconceptions
- Forgetting to include all combinations. With n variables, there are 2ⁿ rows — students sometimes skip the rows where both variables are false.
- Confusing OR with exclusive-or. Logical OR (P ∨ Q) is true when both P and Q are true; exclusive-or is not.
- Not breaking compound expressions into steps. For complex expressions, build intermediate columns before computing the final result.

## Questions

```yaml
- question: "How many rows does a truth table for an expression with three variables (P, Q, R) have?"
  type: multiple-choice
  options: ["3", "6", "8", "9"]
  answer: 2
  explanation: "Each variable can be true or false (2 values), and with 3 independent variables, the total number of combinations is 2³ = 8. In general, n variables require 2ⁿ rows. Two variables need 4 rows, three need 8, four need 16, and so on."

- question: "In a truth table for P → Q, the result is FALSE when P is true and Q is false."
  type: true-false
  answer: true
  explanation: "P → Q is false only in the single case where P is true and Q is false. In all other combinations (P true and Q true, P false and Q true, P false and Q false), P → Q is true. This is the defining property of the conditional — it can only be broken when the hypothesis holds but the conclusion does not."

- question: "Build the truth table for P AND (NOT Q) and identify in which row(s) the expression is true."
  type: short-answer
  answer: "P=T, Q=T → NOT Q=F → P AND F = F. P=T, Q=F → NOT Q=T → P AND T = T. P=F, Q=T → NOT Q=F → F AND F = F. P=F, Q=F → NOT Q=T → F AND T = F. The expression is true only when P is true and Q is false (row 2)."
  explanation: "Building the table step by step: first compute NOT Q for each row, then compute P AND (NOT Q). The expression P ∧ ¬Q is true exactly when P is true and Q is false. Interestingly, this is exactly the condition that makes P → Q false — so P ∧ ¬Q is the negation of P → Q."
```

## Explainer

A truth table is the brute-force method for understanding logical statements: list every possible scenario and check what happens in each one. It is not elegant, but it is thorough and it never lies. For any compound logical statement, a truth table tells you its truth value in every possible case — and once you have that, you know everything about it.

The simplest truth table is for NOT. The variable P has two possible values (true and false), so the table has two rows. When P is true, NOT P is false. When P is false, NOT P is true. That is the entire table, and it completely defines negation.

For two variables, you need four rows to cover every combination: both true, first true and second false, first false and second true, both false. The truth table for AND (P ∧ Q) shows it is true only when both P and Q are true — any other combination gives false. The truth table for OR (P ∨ Q) shows it is true when at least one of P or Q is true — the only false case is when both are false. Note that logical OR is inclusive: "P or Q" is true even when both are true, which differs from how "or" often works in everyday English.

The most important truth table to internalize is the one for the conditional P → Q. It has four rows: (T,T) → T, (T,F) → F, (F,T) → T, (F,F) → T. The conditional is false in exactly one case: when P is true and Q is false. The two rows where P is false both give true — this is the vacuous truth you learned about earlier, now visible as entries in a table.

Truth tables become genuinely powerful when you use them to compare statements. Build the truth table for P → Q and the truth table for ¬Q → ¬P (the contrapositive) side by side. You will find that the final columns are identical — same truth value in every row. This proves they are logically equivalent, not just for one example but for all possible truth values of P and Q. You have just verified a fundamental logical law using nothing but systematic case-checking. This technique will serve you throughout your study of logic and proofs.
