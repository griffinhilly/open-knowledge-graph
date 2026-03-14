---
id: skolemization-and-equisatisfiability
title: Skolemization and Equisatisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: prenex-normal-form
  type: hard
- id: existential-formulas-embeddings
  type: hard
builds-toward:
- resolution-fol
tags:
- first-order-logic
- skolemization
- satisfiability
- normal-forms
stage: formal-systems
status: draft
---

# Skolemization and Equisatisfiability

## Core Idea
Skolemization is a process that transforms a formula into an equisatisfiable formula (same satisfiability) by replacing existential quantifiers with Skolem functions. For example, ∀x ∃y P(x, y) becomes ∀x P(x, f(x)), where f is a fresh function symbol (Skolem function). The resulting formula has no existential quantifiers. Crucially, the original and Skolemized formulas have the same satisfiability: a model for one exists iff a model for the other exists. This is essential for resolution and automated reasoning methods.

## How It's Best Learned
Start with simple formulas in prenex form and apply Skolemization step-by-step. Understand that Skolem functions encode the witness for the existential quantifier. Verify equisatisfiability on small examples. Relate to how resolution uses Skolemization to reduce first-order problems to propositional ones.

## Common Misconceptions
- Thinking Skolemization preserves logical equivalence (it preserves satisfiability, not equivalence — the Skolemized formula may be stronger).
- Confusing Skolem functions with arbitrary functions (Skolem functions are introduced specifically to witness the existential quantifier).
- Assuming free variables in the input require Skolemization (Skolemization targets existential quantifiers; free variables require different handling).
