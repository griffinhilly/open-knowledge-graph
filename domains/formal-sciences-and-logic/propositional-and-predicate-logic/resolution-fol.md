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
status: validated
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

## Questions

```yaml
- question: "In first-order resolution, why do we negate the conclusion and add it to the premises before attempting to derive the empty clause?"
  type: multiple-choice
  options:
    - "To convert the formula into clause normal form, which is required before Skolemization can proceed"
    - "Because resolution works by refutation: if the premises plus the negated conclusion lead to contradiction, then the conclusion must logically follow from the premises"
    - "To allow unification to match complementary literals in the goal with literals in the premises"
    - "Because resolution cannot handle positive literals — only negated literals can be resolved"
  answer: 1
  explanation: "First-order resolution is a proof by contradiction. If a conclusion C follows from premises P, then P ∧ ¬C is unsatisfiable — there is no model that satisfies all premises while also falsifying the conclusion. By adding ¬C to the clause set and trying to derive □ (the empty clause, representing contradiction), we are proving that no such model exists. If we succeed, C must be true in every model of P. This refutation strategy is what makes resolution a complete proof procedure for first-order logic."

- question: "A student runs a first-order resolution prover on a satisfiable set of first-order clauses (no logical contradiction exists). After an hour, the prover has not terminated. The student concludes the prover has a bug. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — any correct theorem prover must terminate in polynomial time on finite inputs"
    - "No — first-order resolution is refutation-complete but not a decision procedure; on satisfiable inputs where no contradiction exists, the prover may run forever because first-order validity is only semidecidable"
    - "Yes — the prover is in an infinite loop caused by incorrect unification"
    - "No — but only because the input must actually be unsatisfiable, and the prover will eventually find the refutation"
  answer: 1
  explanation: "There is no general algorithm that can decide, for arbitrary first-order formulas, whether a proof exists. If an input is unsatisfiable, refutation-completeness guarantees the prover will eventually find the empty clause. But if the input is satisfiable, the prover may generate new resolvents indefinitely — it has no way to know that no contradiction will ever appear. This is a fundamental theoretical limit (undecidability of first-order validity), not a bug. Decidable fragments exist (propositional logic, some restricted first-order fragments), but general first-order resolution cannot avoid this."

- question: "Skolemization preserves logical equivalence: the Skolemized version of a formula is true in exactly the same models as the original."
  type: true-false
  answer: false
  explanation: "Skolemization preserves satisfiability, not logical equivalence. The Skolemized formula is equisatisfiable — it is satisfiable if and only if the original is — but the models of the two formulas are generally different. Skolem functions introduce new function symbols that don't appear in the original language, so they can't be models of the original formula. This is sufficient for refutation proofs (we only need to know whether the clause set is unsatisfiable), but it means you cannot interpret Skolem terms as actual witnesses in the original formula's semantics."

- question: "If a set of first-order clauses is unsatisfiable, first-order resolution is guaranteed to find a refutation (derive the empty clause) in finite time."
  type: true-false
  answer: true
  explanation: "This is what 'refutation-complete' means. Herbrand's theorem provides the theoretical basis: an unsatisfiable set of first-order clauses has a finite unsatisfiable set of ground instances, which has a propositional resolution refutation. The resolution procedure, by systematically generating ground instances and resolving them, will eventually find this finite refutation. The key asymmetry is that completeness is guaranteed only for the unsatisfiable case — the satisfiable case may not terminate."

- question: "Explain why first-order resolution is described as 'refutation-complete but undecidable,' and what this means in practice when running an automated theorem prover."
  type: short-answer
  answer: "Refutation-complete means: if a conclusion follows from premises (the negated conclusion plus premises is unsatisfiable), the resolution procedure will eventually derive the empty clause and confirm the proof. No valid proof will be missed. Undecidable means: if the input is satisfiable (no contradiction exists), there is no guaranteed termination — the prover may generate resolvents indefinitely without being able to conclude 'no proof exists.' In practice, provers use search strategies (ordering heuristics, clause deletion, depth limits) to handle non-termination, but they cannot solve the fundamental problem: an incomplete run doesn't tell you whether a proof would eventually appear or simply doesn't exist. Prover9 and Prolog (via SLD-resolution) are both built on this foundation, so they share the same theoretical limitation."
  explanation: "The contrast with propositional resolution is instructive: propositional logic is decidable because the clause set is finite and no new distinct clauses can be generated indefinitely. First-order resolution can generate infinitely many ground instances via Herbrand expansion, so the search space is infinite in the satisfiable case."
```

## Explainer

You already know two things that first-order resolution combines: unification (finding substitutions that make terms syntactically identical) and the soundness/completeness of first-order logic (valid arguments have proofs). Propositional resolution, which you may recall, derives new clauses by canceling complementary literals — if you have C₁ ∨ p and C₂ ∨ ¬p, you resolve them to get C₁ ∨ C₂. First-order resolution lifts this to predicate logic by using **unification** to make complementary literals identical before canceling them.

The overall procedure is a **proof by refutation**: to prove a conclusion from premises, negate the conclusion, add it to the premises, and try to derive the empty clause (contradiction). The steps are: (1) negate the goal and add it to the premise set; (2) **Skolemize** by replacing each existentially quantified variable with a Skolem function of the universally quantified variables in whose scope it appears; (3) convert to **clause normal form** (conjunctions of disjunctions of literals, with universal quantifiers implicit); (4) repeatedly resolve pairs of clauses by finding a **most general unifier** (MGU) for a complementary literal pair and applying it to both clauses before taking the disjunction of the rest. A refutation is found when the empty clause □ is derived.

The Socrates example is the clearest illustration. Premises: "All humans are mortal" → ∀x (Human(x) → Mortal(x)); "Socrates is human" → Human(Socrates). Goal: Mortal(Socrates). Negate the goal: ¬Mortal(Socrates). Clauses: {¬Human(x) ∨ Mortal(x)}, {Human(Socrates)}, {¬Mortal(Socrates)}. Resolve the first clause with {¬Mortal(Socrates)} using MGU {x ↦ Socrates}: derive ¬Human(Socrates). Now resolve with {Human(Socrates)}: derive □. Refutation complete; the original argument is valid.

**Herbrand's theorem** provides the theoretical guarantee: an unsatisfiable set of first-order clauses has a finite unsatisfiable set of ground instances, which has a propositional resolution refutation. First-order resolution is **refutation-complete** — if a refutation exists, the procedure will eventually find it. However, it is not a decision procedure: on a satisfiable input, the procedure may run forever, generating new ground instances without termination. This is unavoidable since first-order validity is only semidecidable. In practice, resolution powers automated theorem provers like Prover9 and underpins the operational semantics of Prolog (which uses a restricted form called SLD-resolution), making it one of the most consequential proof-search strategies in computer science and logic.
