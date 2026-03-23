---
id: logical-equivalence-formulas
title: Logical Equivalence of Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formula-evaluation-and-truth-tables
  type: hard
builds-toward:
- logical-consequence-and-entailment
tags:
- propositional-logic
- equivalence
- transformation
stage: formal-systems
status: validated
---

# Logical Equivalence of Formulas

## Core Idea
Two formulas are logically equivalent if they have the same truth value under every possible interpretation. Logical equivalence is an equivalence relation on formulas and forms the basis for simplifying, transforming, and understanding the deep structure of logical formulas.

## Questions

```yaml
- question: "Which of the following correctly states one of De Morgan's laws?"
  type: multiple-choice
  options:
    - "¬(A ∧ B) ≡ (¬A ∧ ¬B)"
    - "¬(A ∨ B) ≡ (¬A ∨ ¬B)"
    - "¬(A ∧ B) ≡ (¬A ∨ ¬B)"
    - "¬(A → B) ≡ (A → ¬B)"
  answer: 2
  explanation: "De Morgan's law for conjunction states: ¬(A ∧ B) ≡ (¬A ∨ ¬B). Negating a conjunction distributes the negation to each component and flips 'and' to 'or.' The symmetric law is ¬(A ∨ B) ≡ (¬A ∧ ¬B) — negating a disjunction distributes and flips 'or' to 'and.' The critical pattern: the connective always flips. Options A and B distribute the negation correctly but fail to flip the connective — a common error. Option D is unrelated to De Morgan's laws."

- question: "A student wants to show ¬(P → Q) is equivalent to (P ∧ ¬Q). Applying the conditional equivalence A → B ≡ ¬A ∨ B followed by De Morgan's law, what is the correct derivation?"
  type: multiple-choice
  options:
    - "¬(P → Q) ≡ ¬(¬P ∧ Q) ≡ (P ∨ ¬Q) by distributing negation and applying De Morgan"
    - "¬(P → Q) ≡ ¬(¬P ∨ Q) ≡ (P ∧ ¬Q) by conditional equivalence then De Morgan then double negation"
    - "¬(P → Q) ≡ (¬P → ¬Q) by negating both the antecedent and consequent"
    - "¬(P → Q) ≡ (¬P ∧ ¬Q) by applying De Morgan directly to the implication"
  answer: 1
  explanation: "Step 1: Apply conditional equivalence: P → Q ≡ ¬P ∨ Q, so ¬(P → Q) ≡ ¬(¬P ∨ Q). Step 2: Apply De Morgan's law to ¬(¬P ∨ Q): distribute negation and flip ∨ to ∧, giving (¬¬P ∧ ¬Q). Step 3: Apply double negation: ¬¬P ≡ P. Result: P ∧ ¬Q — 'P is true and Q is false,' which is exactly when an implication fails. Option A makes an error in the first step. Option C applies a different (invalid) transformation. Option D skips the conditional equivalence step entirely."

- question: "If φ ≡ ψ, then replacing any occurrence of φ inside a larger compound formula with ψ preserves the larger formula's truth value under every interpretation."
  type: true-false
  answer: true
  explanation: "True. This is the substitution theorem, and it follows directly from what logical equivalence means. Since φ and ψ produce identical truth values under every possible variable assignment, any formula built using φ as a component must produce the same output whether φ or ψ appears there — the surrounding formula 'sees' the same truth value from the subformula. This licenses algebraic manipulation of logic: just as you can substitute equals for equals in arithmetic, you can substitute logically equivalent formulas in logic."

- question: "A → B and B → A are logically equivalent because they are both conditionals built from the same two variables."
  type: true-false
  answer: false
  explanation: "False. Sharing the same variables is not sufficient for logical equivalence — the truth tables must match on *every* row. When A = T and B = F: A → B is false (true antecedent, false consequent), but B → A is true (false antecedent makes the conditional vacuously true). The truth tables differ, so they are not equivalent. A → B (equivalent to ¬A ∨ B) and its converse B → A (equivalent to ¬B ∨ A) are distinct logical claims. Confusing a conditional with its converse is a fundamental logical error."

- question: "Explain in your own words what it means for two propositional formulas to be logically equivalent, and why the substitution theorem follows directly from this definition."
  type: short-answer
  answer: "Two formulas φ and ψ are logically equivalent (φ ≡ ψ) when they produce identical truth values under every possible assignment of true or false to their propositional variables — their truth tables are row-by-row identical. The substitution theorem says: if φ ≡ ψ, you can replace any occurrence of φ inside any larger formula with ψ without changing the larger formula's truth value under any interpretation. This follows directly from the definition: since φ and ψ behave identically in every context (same output for every input), substituting one for the other in any compound formula cannot change how the compound formula evaluates."
  explanation: "Logical equivalence partitions all formulas into classes of synonymous expressions that are interchangeable in any logical context. The substitution theorem is what gives this partition its practical utility: it licenses step-by-step algebraic manipulation of formulas. Just as knowing 2 + 2 = 4 lets you replace '2 + 2' with '4' anywhere in an arithmetic expression, knowing φ ≡ ψ lets you replace φ with ψ anywhere in a logical formula — enabling simplification, conversion to normal forms, and formal proof construction."
```

## Explainer

You know how to evaluate a propositional formula's truth value using **truth tables**: for each possible assignment of T/F to the variables, compute the formula's output. Two formulas are **logically equivalent** — written φ ≡ ψ — if they produce identical truth tables. Every row gives the same output. This means they express the same logical content; one can always replace the other in any context without changing the truth value of the compound formula containing them.

The most important logical equivalences form a small algebra of propositional logic. **De Morgan's laws** let you push negations inward: ¬(A ∧ B) ≡ (¬A ∨ ¬B), and ¬(A ∨ B) ≡ (¬A ∧ ¬B). Think of negating a conjunction as distributing the negation and flipping the connective from "and" to "or." **Double negation elimination** gives ¬¬A ≡ A. The **conditional equivalence** A → B ≡ ¬A ∨ B is crucial: it rewrites an implication purely in terms of disjunction and negation. **Distributive laws** mirror their algebraic counterparts: A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C). Verify any of these by drawing the full truth table for both sides — every row will match.

These equivalences are the engine for converting formulas into **normal forms** — canonical representations with standardized structure. Applying De Morgan's laws, double negation, and distribution systematically converts any formula into **Conjunctive Normal Form (CNF)**: a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals. CNF is the standard input format for SAT solvers, making these equivalences directly relevant to automated reasoning. Every formula is also reducible to **Disjunctive Normal Form (DNF)**: a disjunction of conjunctions. The existence of both normal forms proves that ∧, ∨, and ¬ together are **functionally complete** — sufficient to express any truth function.

Logical equivalence is an **equivalence relation** on formulas: every formula is equivalent to itself, equivalence is symmetric, and it is transitive (if φ ≡ ψ and ψ ≡ χ then φ ≡ χ). This partitions the space of all formulas into equivalence classes of "synonymous" expressions. The practical payoff is the **substitution theorem**: if φ ≡ ψ, then replacing any occurrence of φ inside a larger formula with ψ preserves the larger formula's truth value under every interpretation. This is what makes algebraic manipulation of logic possible — the same way you substitute equals for equals in arithmetic, you substitute logically equivalent formulas in logic, and the surrounding structure is unaffected.
