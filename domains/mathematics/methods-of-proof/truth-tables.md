---
id: truth-tables
title: Truth Tables
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- logical-equivalences
- tautologies-and-contradictions
tags:
- logic
- truth-values
- systematic
stage: formal-systems
status: draft
---

# Truth Tables

## Core Idea
Truth tables systematically enumerate all possible truth value assignments and show the resulting truth of compound statements. They are the primary tool for analyzing logical operations and verifying equivalences.

## How It's Best Learned
Build small tables for single connectives, then combine them step-by-step for complex statements.

## Common Misconceptions
- Missing rows when there are more than two variables (2^n rows for n variables).
- Incorrectly evaluating complex formulas by working left-to-right instead of respecting operator precedence.

## Explainer

From statements and logical connectives, you know the basic building blocks: atomic propositions (P, Q, R, …) that are either true or false, and connectives (¬, ∧, ∨, →, ↔) that combine them into compound statements. The truth value of a compound statement depends entirely on the truth values of its components. A **truth table** makes this dependence explicit by listing every possible combination of truth values for the atomic variables and computing the resulting truth value for the compound statement in each case.

For n atomic variables, there are 2ⁿ possible combinations of truth values — 2 choices (T or F) per variable, n variables. For two variables P and Q, there are 2² = 4 rows; for three variables, 8 rows; for four, 16. Each row represents one scenario or **interpretation**. The standard layout assigns truth values in a pattern that cycles through all combinations: the rightmost variable alternates T, F, T, F, …; the next variable cycles in pairs T, T, F, F, …; and so on. This systematic cycling guarantees you cover every case exactly once. Missing even one row is a logical error — the table would no longer be complete, and any conclusion drawn from it would be unwarranted.

To evaluate a compound statement, build the table **column by column**, following operator precedence: negation (¬) binds most tightly, then conjunction (∧), then disjunction (∨), then conditional (→), then biconditional (↔). For example, to evaluate ¬P ∨ (Q ∧ R), first compute ¬P, then Q ∧ R, then combine with ∨. Working left-to-right without respecting precedence is the most common computational error. Adding intermediate columns for each subexpression — rather than trying to evaluate the whole formula at once — keeps the work organized and checkable.

Truth tables are the primary tool for two important tasks. First, **checking logical equivalence**: two statements are logically equivalent (written A ≡ B) if and only if they have identical truth values in every row. This is how you verify that P → Q is equivalent to ¬P ∨ Q, or that De Morgan's laws hold. Second, **identifying tautologies and contradictions**: a statement is a **tautology** if it is true in every row (like P ∨ ¬P), and a **contradiction** if it is false in every row (like P ∧ ¬P). For larger formulas with many variables, truth tables grow exponentially and become impractical — at that point, algebraic methods (logical equivalences) become essential. But for small formulas, a truth table is definitive: it leaves no case unchecked.
