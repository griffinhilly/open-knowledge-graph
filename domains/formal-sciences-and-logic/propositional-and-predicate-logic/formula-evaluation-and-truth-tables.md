---
id: formula-evaluation-and-truth-tables
title: Formula Evaluation and Truth Tables
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-functions-and-interpretation
  type: hard
- id: propositional-syntax
  type: hard
- id: truth-tables-and-evaluation
  type: soft
- id: boolean-functions
  type: soft
builds-toward:
- logical-equivalence-formulas
tags:
- propositional-logic
- truth-tables
- semantic-analysis
stage: formal-systems
status: draft
---

# Formula Evaluation and Truth Tables

## Core Idea
A truth table systematically lists all possible truth assignments to atomic formulas and computes the resulting truth value of a complex formula. This mechanical method makes it easy to determine whether a formula is always true (tautology), sometimes true (contingent), or never true (contradiction).

## How It's Best Learned
Build truth tables by hand for increasingly complex formulas, working column by column. Use software tools to verify your work and explore patterns in larger formulas.

## Common Misconceptions
- Errors in operator precedence when building truth tables—always clarify parentheses.
- Thinking a truth table proves something rather than just computing truth values for all cases.

## Explainer

You already know from propositional syntax how to read a formula's structure: connectives (¬, ∧, ∨, →, ↔) combine atomic propositions according to a grammar. You know from truth functions and interpretation that each connective is a function from truth values to truth values — ¬ flips T to F, ∧ outputs T only when both inputs are T, and so on. **Formula evaluation** is just the process of applying these functions layer by layer to compute the overall truth value of a complex formula under a specific assignment.

A **truth table** is the systematic method for doing this across *all possible* assignments at once. If a formula contains n distinct atomic propositions, there are 2ⁿ possible rows — one for each assignment of T or F to every atom. The table has columns for each atom, columns for each intermediate subformula, and a final column for the whole formula. You fill it in left to right, bottom up through the formula's parse tree, because each subformula's value depends only on its children's values.

The payoff is a complete classification of the formula. If the final column is all T, the formula is a **tautology** — it is true under every interpretation, regardless of what the atoms mean. The formula (P → P) is a tautology: whether P is true or false, the implication holds. If the final column is all F, the formula is a **contradiction** — unsatisfiable. If the column has both T and F entries, the formula is **contingent**: sometimes true, sometimes false, depending on how you interpret the atoms.

The key skill to build is working column by column through subformulas before reaching the main connective. For a formula like ¬(P ∧ Q) → (¬P ∨ ¬Q), you first compute P ∧ Q, then ¬(P ∧ Q), then ¬P, then ¬Q, then ¬P ∨ ¬Q, then the full implication. Skipping steps and trying to evaluate the whole formula at once is where errors enter. The mechanical discipline of the column-by-column approach is not busywork — it mirrors the recursive structure of the formula's syntax tree and makes correctness checkable.

Truth tables are finite, complete, and decision-procedure: for any propositional formula, the table always terminates and definitively answers whether it is a tautology, contradiction, or contingency. This is the semantic approach to logic. Later, you will meet proof-theoretic methods (derivations, sequent calculi) that establish the same results by symbol manipulation rather than exhaustive enumeration. The equivalence of these two methods — that semantic tautology coincides with provability — is what soundness and completeness theorems establish.
