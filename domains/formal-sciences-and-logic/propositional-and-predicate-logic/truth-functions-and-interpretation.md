---
id: truth-functions-and-interpretation
title: Truth Functions and Interpretation
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-connectives
  type: hard
- id: propositional-semantics
  type: hard
builds-toward:
- formula-evaluation-and-truth-tables
tags:
- propositional-logic
- semantics
- truth-functions
stage: formal-systems
status: draft
---

# Truth Functions and Interpretation

## Core Idea
In propositional logic, each connective (AND, OR, NOT, IMPLIES) defines a truth function that determines the truth value of a complex formula based on the truth values of its parts. An interpretation assigns truth values to atomic propositions, and these combine via truth functions to determine the truth value of any formula.

## How It's Best Learned
Start with small formulas like (A ∧ B) and work through how their truth values depend on A and B. Visualize truth functions with simple diagrams before moving to complex nested formulas.

## Common Misconceptions
- Thinking truth functions are just names of connectives rather than actual functions mapping truth values to truth values.
- Confusing the truth value of a formula under one interpretation with the formula's inherent truth value.

## Explainer

You already know the connectives AND (∧), OR (∨), NOT (¬), and IMPLIES (→) from propositional logic, and you know that propositions have truth values. A **truth function** makes this precise: it is a function from tuples of truth values to a truth value. Conjunction (∧) is a function f: {T, F} × {T, F} → {T, F} that maps (T,T) to T and everything else to F. This is not just a definition-by-name — it is a genuine mathematical function, and everything about the semantics of propositional logic flows from these functions.

An **interpretation** (also called a **valuation**) assigns a truth value — T or F — to each atomic proposition. There are only two choices per atom, so for n atoms there are exactly 2^n distinct interpretations. Given an interpretation, the truth value of any complex formula is computed mechanically by applying truth functions bottom-up through the formula's parse tree. For example, under the interpretation where A = T and B = F: (A ∧ B) applies the conjunction function to (T, F), returning F; (A → B) applies the material conditional function to (T, F), returning F; and ¬(A ∧ ¬B) requires evaluating ¬B = T, then A ∧ T = T, then ¬T = F. No intuition about meaning is needed — only the functions.

The fundamental lesson from your propositional semantics background is that formulas do not have truth values in themselves — they only have truth values **relative to interpretations**. The formula (A ∨ ¬A) is a **tautology**: it evaluates to T under every possible interpretation, because regardless of what A is, either A is T or ¬A is T. The formula (A ∧ ¬A) is a **contradiction**: it evaluates to F under every interpretation. Most formulas are **contingent**: true under some interpretations and false under others. A truth table exhausts all 2^n interpretations, making this classification systematic.

The deeper point is what truth functions reveal about logical equivalence. Two formulas φ and ψ are **logically equivalent** (written φ ≡ ψ) exactly when they agree under every interpretation — they define the same truth function. This gives you a decision procedure for propositional logic: build truth tables for both formulas and compare column by column. The connectives →, ↔, and ⊕ (exclusive or) are all just specific truth functions, and any boolean function can be expressed using ∧, ∨, and ¬ alone (completeness of connectives). This connection between truth functions and logic is what makes propositional logic computationally tractable — and it sets the stage for understanding why predicate logic, which introduces quantifiers, is fundamentally harder.

