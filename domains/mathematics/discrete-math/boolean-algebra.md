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
status: draft
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
