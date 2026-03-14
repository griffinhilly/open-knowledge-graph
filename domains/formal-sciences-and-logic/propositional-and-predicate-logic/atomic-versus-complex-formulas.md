---
id: atomic-versus-complex-formulas
title: Atomic and Complex Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: term-and-atom-fol
  type: hard
builds-toward:
- literals-and-clauses-cnf
- normal-forms-cnf-dnf
tags:
- syntax
- atomic
- complex
- propositional
- first-order
stage: formal-systems
status: draft
---

# Atomic and Complex Formulas

## Core Idea
An atomic formula is a formula with no logical connectives: in propositional logic, atomic formulas are propositional variables; in first-order logic, they are of the form P(t₁, …, tₙ) where P is a predicate and tᵢ are terms. Complex (or molecular) formulas are built from atomic formulas using logical connectives (¬, ∧, ∨, →, ↔) and/or quantifiers (∀, ∃). This distinction is fundamental: the truth value of a complex formula is determined compositionally from the truth values of its atomic constituents and the semantics of the connectives and quantifiers.

## How It's Best Learned
Use parse trees to visualize formula structure, showing atoms at the leaves and connectives/quantifiers at internal nodes. Practice identifying atoms in formulas of varying complexity. Relate atomicity to recursive definitions of formulas.

## Common Misconceptions
- Thinking a formula with one occurrence of a connective is atomic (it's not — any use of ¬, ∧, ∨, →, ↔, ∀, or ∃ makes it complex).
- Confusing atomic formulas with ground formulas (an atom like P(x) is atomic but not ground).
- Assuming all propositional variables are atoms (they are, but so are first-order predicate applications).
