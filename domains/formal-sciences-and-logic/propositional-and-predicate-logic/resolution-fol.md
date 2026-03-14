---
id: resolution-fol
title: First-Order Resolution
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-soundness-completeness
  type: hard
- id: substitution-and-unification
  type: hard
builds-toward:
- decidability-of-theories
tags:
- resolution
- Skolemization
- Herbrand-theorem
- refutation-completeness
- automated-theorem-proving
stage: formal-systems
status: draft
---

# First-Order Resolution

## Core Idea
First-order resolution extends propositional resolution to predicate logic by combining clause resolution with unification. To refute a set of first-order sentences: negate the conjecture, Skolemize (replace existential quantifiers with Skolem functions), convert to clause form, then resolve pairs of clauses by unifying complementary literals and applying the most general unifier to the resolvent. Herbrand's theorem guarantees that an unsatisfiable set of first-order clauses has a finite propositional refutation over its Herbrand universe, providing the theoretical basis for refutation completeness. First-order resolution is the foundation of automated theorem provers like Prover9 and the Prolog execution model.

## How It's Best Learned
Skolemize a simple first-order argument (e.g., "all humans are mortal, Socrates is human, therefore Socrates is mortal"), convert to clauses, and carry out resolution with unification by hand. Compare the result to the same argument proved by natural deduction to see the tradeoffs.

## Common Misconceptions
- Skolemization does not preserve logical equivalence — it preserves satisfiability, which is sufficient for refutation proofs but means you cannot simply substitute Skolem terms back.
- First-order resolution is refutation-complete but undecidable — the procedure may run forever on satisfiable inputs because first-order validity is only semidecidable.
- The Herbrand universe can be infinite, so Herbrand's theorem guarantees a finite refutation exists but says nothing about finding it efficiently.
