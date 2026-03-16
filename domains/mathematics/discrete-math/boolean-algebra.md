---
id: boolean-algebra
title: Boolean Algebra
domain: mathematics
course: discrete-math
prerequisites:
- id: logical-equivalences
  type: hard
- id: truth-tables
  type: hard
- id: set-operations
  type: soft
builds-toward:
- logic-gates-and-circuits
tags:
- boolean-algebra
- boolean-functions
- de-morgan
- dnf
- cnf
- simplification
stage: formal-systems
status: validated
---

# Boolean Algebra

## Core Idea
Boolean algebra is an algebraic structure with elements {0, 1} and operations AND (∧), OR (∨), and NOT (¬), satisfying axioms including commutativity, associativity, distributivity (each operation over the other), identity, and complementation. It is formally isomorphic to both propositional logic and set algebra. Every Boolean function can be expressed in disjunctive normal form (sum of minterms) or conjunctive normal form (product of maxterms). Simplification using De Morgan's laws, absorption, and idempotence reduces circuit complexity.

## How It's Best Learned
Build truth tables for compound Boolean expressions, then simplify algebraically and verify the simplified form has the same table. Connect each algebraic law to its logical and set-theoretic counterpart. Use Karnaugh maps as a visual simplification tool for 2-to-4 variable functions.

## Common Misconceptions
- Applying distributivity incorrectly: in Boolean algebra, AND distributes over OR and OR distributes over AND — unlike ordinary arithmetic.
- Confusing De Morgan's laws — both the operation (AND↔OR) and all complements flip simultaneously.
- Thinking Boolean algebra is 'just logic with 0 and 1' without recognizing its complete axiomatic algebraic structure.

## Questions

```yaml
- question: "Which of the following correctly applies De Morgan's law to ¬(A ∧ B)?"
  type: multiple-choice
  options: ["¬A ∧ ¬B", "¬A ∨ B", "¬A ∨ ¬B", "A ∨ B"]
  answer: 2
  explanation: "De Morgan's law states ¬(A ∧ B) = ¬A ∨ ¬B. Both things change simultaneously: the connective flips (AND → OR) AND complements are added to each variable. A common error is flipping only the complements but not the connective (leaving ¬A ∧ ¬B), or flipping only the connective without adding complements."

- question: "In Boolean algebra, AND distributes over OR but OR does not distribute over AND — just like in ordinary arithmetic where multiplication distributes over addition but not vice versa."
  type: true-false
  answer: false
  explanation: "In Boolean algebra, BOTH operations distribute over each other: A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C), and also A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C). This symmetric distributivity (the principle of duality) is one of the key structural differences from ordinary arithmetic, where only multiplication distributes over addition."

- question: "What does it mean for a Boolean expression to be in Disjunctive Normal Form (DNF), and why is it useful?"
  type: short-answer
  answer: "A Boolean expression is in DNF when it is written as an OR of AND-terms (minterms), where each AND-term contains only literals (variables or their complements). Every Boolean function has a DNF representation, making it a canonical form useful for verifying equivalences and constructing circuits directly from truth tables."
  explanation: "DNF corresponds directly to a truth table: each minterm covers exactly one row where the function outputs 1. This makes it easy to build any function from its truth table mechanically — one AND-term per true row — and provides a normal form for comparing whether two expressions are equivalent."
```

## Explainer

You already know propositional logic from truth tables and logical equivalences. Boolean algebra takes those logical operations and treats them algebraically — like algebra over {0, 1} instead of the real numbers. The payoff is that you can simplify complex logical expressions the way you simplify polynomial expressions, reducing circuit complexity without ever building a full truth table.

The elements are {0, 1} (false and true) with three operations: AND (∧), OR (∨), and NOT (¬). The algebraic laws are richer than they first appear. Commutativity, associativity, and identity laws work as expected. The surprise is double distributivity: AND distributes over OR, but so does OR over AND. In ordinary arithmetic, multiplication distributes over addition but not the reverse. In Boolean algebra, both directions work. This symmetry — called the principle of duality — means every valid law has a dual obtained by swapping AND and OR (and swapping 0 and 1). Idempotence (A ∧ A = A) and complementation (A ∧ ¬A = 0) have no ordinary arithmetic analogues at all.

De Morgan's laws are the most important tools for simplification and the most frequently misapplied. ¬(A ∧ B) = ¬A ∨ ¬B, and ¬(A ∨ B) = ¬A ∧ ¬B. The critical pattern: when you push a NOT through a parenthesis, two things change simultaneously — the connective (AND becomes OR or vice versa) AND complements are added to each variable. Students who change only one thing get wrong answers. A reliable mnemonic: "break the bar, change the operation." Verify any application by checking a truth table with a small example.

Every Boolean function has a canonical form. Disjunctive Normal Form (DNF) writes the function as an OR of AND-terms — one term for each row of the truth table where the output is 1. Conjunctive Normal Form (CNF) is the dual: AND of OR-terms. From your study of set operations, you already have intuition here: DNF corresponds to a union of intersections, CNF to an intersection of unions. These normal forms let you convert any truth table into an algebraic expression mechanically and provide a reference for checking equivalence between expressions.

The direct application of all this is digital circuit design. Each AND and OR gate in a circuit corresponds to a Boolean operation; each NOT gate applies complementation. Simplifying a Boolean expression using absorption (A ∧ (A ∨ B) = A), idempotence, and De Morgan reduces the gate count in hardware — translating to cheaper, faster chips. For functions with 2–4 variables, Karnaugh maps provide a visual tool for spotting these simplifications by grouping adjacent 1s in a grid. The historical note: Boolean algebra was invented by George Boole in 1847 as pure logic, but found its defining application a century later when Claude Shannon showed in 1937 that electrical relay circuits obey exactly these axioms.
