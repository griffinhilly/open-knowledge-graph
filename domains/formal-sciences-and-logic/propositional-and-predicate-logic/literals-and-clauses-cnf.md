---
id: literals-and-clauses-cnf
title: Literals and Clauses in Conjunctive Normal Form
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: atomic-versus-complex-formulas
  type: hard
- id: normal-forms-cnf-dnf
  type: hard
builds-toward:
- resolution-propositional
- resolution-fol
tags:
- cnf
- literals
- clauses
- normal-forms
- resolution
stage: formal-systems
status: draft
---

# Literals and Clauses in Conjunctive Normal Form

## Core Idea
A literal is an atomic formula or its negation (e.g., P or ¬P). A clause is a disjunction of literals (e.g., P ∨ ¬Q ∨ R). Conjunctive normal form (CNF) is a formula that is a conjunction of clauses. CNF is important for automated reasoning: the resolution rule operates on clauses, and converting any formula to CNF enables the application of resolution. Every propositional formula can be converted to an equivalent CNF (possibly with an exponential blowup), and CNF is the standard input for SAT solvers.

## How It's Best Learned
Start with propositional formulas and convert them to CNF step-by-step using distributive laws. Understand clauses as OR-of-ANDs. Practice recognizing when a formula is already in CNF. Extend to first-order logic by treating ground atoms as propositional variables.

## Common Misconceptions
- Thinking CNF is unique (multiple CNF forms exist for the same formula).
- Confusing CNF with DNF (CNF is AND of ORs; DNF is OR of ANDs).
- Assuming CNF conversion is efficient in practice (it can lead to exponential growth; better methods use SAT solver techniques).
