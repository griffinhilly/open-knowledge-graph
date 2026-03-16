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

## Explainer

You've studied prenex normal form: any first-order formula can be rewritten so all quantifiers appear at the front, producing a prefix of quantifiers followed by a quantifier-free matrix. A formula in prenex form looks like Q₁x₁ Q₂x₂ ... Qₙxₙ M(x₁,...,xₙ), where each Qᵢ is either ∀ or ∃. **Skolemization** is the process of eliminating all existential quantifiers from this prefix by replacing them with **Skolem functions** — fresh function symbols not appearing anywhere else in the formula.

The rule is: when you encounter an existential quantifier ∃y in the prefix, and the universally quantified variables introduced before it are x₁, ..., xₖ, replace every occurrence of y in the matrix with a fresh function term f(x₁,...,xₖ). This encodes the semantic content of ∃y: "there exists a witness for y, and that witness may depend on the universally quantified variables that have already been fixed." If there are no preceding ∀ quantifiers (∃y is the outermost quantifier), replace y with a fresh **Skolem constant** c — a 0-ary function. For example, ∀x ∃y P(x, y) Skolemizes to ∀x P(x, f(x)), and ∃y ∀x P(x, y) Skolemizes to ∀x P(x, c). After all existential quantifiers are eliminated, the prefix contains only ∀ quantifiers, which can be dropped — all remaining variables are understood to be universally quantified.

The critical property of Skolemization is **equisatisfiability**, not logical equivalence. The original formula φ and its Skolemized version φ_S have the same satisfiability: φ is satisfiable if and only if φ_S is satisfiable. To see why in one direction: if M ⊨ φ, then for each x the existential ∃y P(x, y) is witnessed by some element; define f(x) to be any such witness. Then M extended with this interpretation of f satisfies φ_S. In the other direction, any model of φ_S already satisfies φ by existential introduction — just say "let the witness be f(x)." However, φ and φ_S are *not* logically equivalent: φ_S is typically logically stronger (it asserts a uniform choice function, not merely the existence of witnesses), so Skolemization can never be reversed without changing meaning.

Equisatisfiability is exactly what automated theorem provers need. Resolution works on clause sets — quantifier-free, universally-quantified first-order clauses. By converting to prenex normal form and then Skolemizing, you reduce any first-order satisfiability question to a purely universal one, and then to a set of clauses via CNF conversion. The Skolem functions in the clauses act as terms: resolution's **unification** algorithm matches these terms against each other, effectively performing instantiation. Skolemization is thus the bridge between the expressive language of first-order logic with mixed quantifiers and the tractable, purely universal language that resolution can manipulate algorithmically.
