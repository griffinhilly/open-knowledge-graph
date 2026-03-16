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

## Explainer

You already know two things that first-order resolution combines: unification (finding substitutions that make terms syntactically identical) and the soundness/completeness of first-order logic (valid arguments have proofs). Propositional resolution, which you may recall, derives new clauses by canceling complementary literals — if you have C₁ ∨ p and C₂ ∨ ¬p, you resolve them to get C₁ ∨ C₂. First-order resolution lifts this to predicate logic by using **unification** to make complementary literals identical before canceling them.

The overall procedure is a **proof by refutation**: to prove a conclusion from premises, negate the conclusion, add it to the premises, and try to derive the empty clause (contradiction). The steps are: (1) negate the goal and add it to the premise set; (2) **Skolemize** by replacing each existentially quantified variable with a Skolem function of the universally quantified variables in whose scope it appears; (3) convert to **clause normal form** (conjunctions of disjunctions of literals, with universal quantifiers implicit); (4) repeatedly resolve pairs of clauses by finding a **most general unifier** (MGU) for a complementary literal pair and applying it to both clauses before taking the disjunction of the rest. A refutation is found when the empty clause □ is derived.

The Socrates example is the clearest illustration. Premises: "All humans are mortal" → ∀x (Human(x) → Mortal(x)); "Socrates is human" → Human(Socrates). Goal: Mortal(Socrates). Negate the goal: ¬Mortal(Socrates). Clauses: {¬Human(x) ∨ Mortal(x)}, {Human(Socrates)}, {¬Mortal(Socrates)}. Resolve the first clause with {¬Mortal(Socrates)} using MGU {x ↦ Socrates}: derive ¬Human(Socrates). Now resolve with {Human(Socrates)}: derive □. Refutation complete; the original argument is valid.

**Herbrand's theorem** provides the theoretical guarantee: an unsatisfiable set of first-order clauses has a finite unsatisfiable set of ground instances, which has a propositional resolution refutation. First-order resolution is **refutation-complete** — if a refutation exists, the procedure will eventually find it. However, it is not a decision procedure: on a satisfiable input, the procedure may run forever, generating new ground instances without termination. This is unavoidable since first-order validity is only semidecidable. In practice, resolution powers automated theorem provers like Prover9 and underpins the operational semantics of Prolog (which uses a restricted form called SLD-resolution), making it one of the most consequential proof-search strategies in computer science and logic.
