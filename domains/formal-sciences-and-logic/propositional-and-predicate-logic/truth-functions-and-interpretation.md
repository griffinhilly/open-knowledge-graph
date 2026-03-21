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

## Questions

```yaml
- question: "A student claims: 'The formula (P → Q) is false.' What is the correct response?"
  type: multiple-choice
  options:
    - "The student is right — (P → Q) is always false because it depends on unknown variables"
    - "The formula (P → Q) has no inherent truth value; it is true or false only relative to a specific interpretation that assigns values to P and Q"
    - "The student is wrong because (P → Q) is a tautology — it is always true"
    - "The claim is acceptable shorthand for 'P → Q seems false given what we know'"
  answer: 1
  explanation: "Formulas do not have inherent truth values — they are evaluated relative to interpretations. Under the interpretation P=T, Q=F, the formula (P → Q) evaluates to F. Under P=T, Q=T, it evaluates to T. Under P=F, Q=anything, it evaluates to T. Without specifying an interpretation, 'the formula is true/false' is a category error. Only tautologies (true under all interpretations) and contradictions (false under all interpretations) have truth values independent of interpretation."

- question: "Under the interpretation A = F, B = T, what is the truth value of ¬(A ∧ ¬B)?"
  type: multiple-choice
  options:
    - "False — because A is false, the conjunction fails"
    - "True — computed step by step: ¬B = F, A ∧ F = F, ¬F = T"
    - "True — because ¬B = F and negating a false conjunction gives true"
    - "Indeterminate — without knowing what A and B mean, we cannot evaluate"
  answer: 1
  explanation: "Apply truth functions bottom-up through the parse tree. Step 1: ¬B = ¬T = F. Step 2: A ∧ ¬B = F ∧ F = F. Step 3: ¬(A ∧ ¬B) = ¬F = T. The result is T. The key skill here is mechanical application of truth functions — no interpretation of 'what A means' is required or useful. Option D (indeterminate) represents the misconception that formulas need semantic content to evaluate; they only need an interpretation assigning T/F to each atom."

- question: "Two formulas are logically equivalent if and only if they produce the same truth value under every possible interpretation."
  type: true-false
  answer: true
  explanation: "True — this is the definition of logical equivalence (φ ≡ ψ). Two formulas define the same truth function if and only if they agree on every row of the truth table. For example, (P → Q) ≡ (¬P ∨ Q) because both evaluate to F only when P=T and Q=F, and T otherwise. Logical equivalence is verified exhaustively over all 2^n interpretations for n atoms. This makes propositional logic decidable: you can always determine equivalence by truth table."

- question: "The formula (A ∨ ¬A) is true because every proposition A refers to something that is either true or false in the real world."
  type: true-false
  answer: false
  explanation: "False — and this gets the explanation backwards. (A ∨ ¬A) is a tautology because of its logical structure: under any interpretation, either A = T (making A ∨ ¬A = T ∨ F = T) or A = F (making A ∨ ¬A = F ∨ T = T). The formula's tautologous status follows purely from how the truth functions for ∨ and ¬ interact — no facts about the real world are needed. The claim in the question reverses the logic: the tautology is not true because of empirical facts; it would remain a tautology even in a world where nothing is true or false in any meaningful sense."

- question: "Why do formulas in propositional logic have no inherent truth value, and what determines their truth value instead?"
  type: short-answer
  answer: "A formula is a syntactic object — a string of symbols. It has no inherent truth value because its atomic propositions (P, Q, A, etc.) are uninterpreted variables, not statements about a fixed state of affairs. What determines a formula's truth value is an interpretation: a function that assigns T or F to each atomic proposition. Given an interpretation, the truth value of the whole formula is computed mechanically by applying truth functions bottom-up through the formula's structure. The same formula evaluates differently under different interpretations unless it is a tautology (always T) or contradiction (always F)."
  explanation: "This separation between syntax (the formula) and semantics (its truth value under an interpretation) is foundational to logic. It means we can study the logical relationships between formulas — entailment, equivalence, satisfiability — without committing to what the variables 'really mean.' It also makes logic computationally tractable: to check whether a formula is a tautology, enumerate all 2^n interpretations and verify T on each. This would be impossible if formulas had meaning-dependent truth values that couldn't be enumerated."
```

## Explainer

You already know the connectives AND (∧), OR (∨), NOT (¬), and IMPLIES (→) from propositional logic, and you know that propositions have truth values. A **truth function** makes this precise: it is a function from tuples of truth values to a truth value. Conjunction (∧) is a function f: {T, F} × {T, F} → {T, F} that maps (T,T) to T and everything else to F. This is not just a definition-by-name — it is a genuine mathematical function, and everything about the semantics of propositional logic flows from these functions.

An **interpretation** (also called a **valuation**) assigns a truth value — T or F — to each atomic proposition. There are only two choices per atom, so for n atoms there are exactly 2^n distinct interpretations. Given an interpretation, the truth value of any complex formula is computed mechanically by applying truth functions bottom-up through the formula's parse tree. For example, under the interpretation where A = T and B = F: (A ∧ B) applies the conjunction function to (T, F), returning F; (A → B) applies the material conditional function to (T, F), returning F; and ¬(A ∧ ¬B) requires evaluating ¬B = T, then A ∧ T = T, then ¬T = F. No intuition about meaning is needed — only the functions.

The fundamental lesson from your propositional semantics background is that formulas do not have truth values in themselves — they only have truth values **relative to interpretations**. The formula (A ∨ ¬A) is a **tautology**: it evaluates to T under every possible interpretation, because regardless of what A is, either A is T or ¬A is T. The formula (A ∧ ¬A) is a **contradiction**: it evaluates to F under every interpretation. Most formulas are **contingent**: true under some interpretations and false under others. A truth table exhausts all 2^n interpretations, making this classification systematic.

The deeper point is what truth functions reveal about logical equivalence. Two formulas φ and ψ are **logically equivalent** (written φ ≡ ψ) exactly when they agree under every interpretation — they define the same truth function. This gives you a decision procedure for propositional logic: build truth tables for both formulas and compare column by column. The connectives →, ↔, and ⊕ (exclusive or) are all just specific truth functions, and any boolean function can be expressed using ∧, ∨, and ¬ alone (completeness of connectives). This connection between truth functions and logic is what makes propositional logic computationally tractable — and it sets the stage for understanding why predicate logic, which introduces quantifiers, is fundamentally harder.

