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
- id: tautology-satisfiability-validity
  type: soft
builds-toward:
- resolution-fol
tags:
- first-order-logic
- skolemization
- satisfiability
- normal-forms
stage: advanced
status: validated
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

## Questions

```yaml
- question: "A logician Skolemizes the formula ∀x ∃y P(x, y) to obtain ∀x P(x, f(x)). What is the correct relationship between the original and the Skolemized formula?"
  type: multiple-choice
  options:
    - "They are logically equivalent — every model of one is a model of the other"
    - "They are equisatisfiable — a model for one exists if and only if a model for the other exists — but the Skolemized version is logically stronger"
    - "The Skolemized version implies the original, but not vice versa — Skolemization weakens the formula"
    - "They are neither equivalent nor equisatisfiable — Skolemization changes the meaning of the formula"
  answer: 1
  explanation: "Equisatisfiability, not logical equivalence, is the correct relationship. Any model M of ∀x ∃y P(x,y) can be extended to a model of ∀x P(x,f(x)) by interpreting f as a choice function that picks a witness y for each x. Conversely, any model of ∀x P(x,f(x)) satisfies ∀x ∃y P(x,y) by existential introduction (let y = f(x)). So they are satisfiable in the same circumstances. However, ∀x P(x,f(x)) is logically stronger: it requires a *uniform* function f witnessing all instances simultaneously, while ∀x ∃y P(x,y) only requires that for each x some witness exists, possibly varying with the model. There are models of the original that cannot interpret f in the required way for the Skolemized version."

- question: "When Skolemizing ∃y ∀x P(x, y) — where the existential quantifier is outermost — the correct Skolemized form is:"
  type: multiple-choice
  options:
    - "∀x P(x, f(x)), with a Skolem function f taking x as argument"
    - "∀x P(x, c), with a Skolem constant c (a 0-ary function symbol)"
    - "P(x, y) with both quantifiers dropped and variables left free"
    - "∀x ∃y P(x, y), since the existential is moved inward"
  answer: 1
  explanation: "The rule for Skolemization is: when eliminating ∃y, introduce a fresh function symbol whose arguments are all universally quantified variables in scope *before* y in the prenex prefix. When ∃y is the outermost quantifier, there are no preceding ∀ quantifiers, so the Skolem term is a constant c (a 0-ary function) — the witness doesn't depend on anything. The formula becomes ∀x P(x, c). If the formula were instead ∀x ∃y P(x,y), then y's witness could depend on x, so we'd use f(x). The key is tracking the ordering of quantifiers in the prefix."

- question: "Skolemization preserves logical equivalence: a formula φ and its Skolemization φ_S are true in exactly the same models."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about Skolemization. Skolemization preserves *satisfiability* (they have models in the same circumstances), not logical equivalence (they are not true in exactly the same models). The Skolemized formula φ_S is logically stronger: it asserts the existence of a specific function symbol (Skolem function) that uniformly witnesses all instances of the existential quantifier. In models where witnesses exist but no uniform function works, φ is true but φ_S is false. This is why Skolemization cannot be reversed and why it is called equisatisfiability, not equivalence."

- question: "Equisatisfiability is exactly the right property for automated theorem proving because resolution works on clause sets that require all existential quantifiers to be eliminated first."
  type: true-false
  answer: true
  explanation: "Resolution works on Horn clauses and general clause sets — quantifier-free formulas where all variables are implicitly universally quantified. To apply resolution to a first-order formula with existential quantifiers, you must first convert to prenex normal form and then Skolemize to eliminate the existentials. The result is a universally quantified formula that, after dropping the universal quantifiers (since variables are implicitly universal in clause form), can be converted to CNF clauses. Equisatisfiability is sufficient: if the original formula is unsatisfiable, so is its Skolemization, and resolution can detect this by deriving the empty clause. Logical equivalence is not needed and in fact cannot be preserved by the quantifier-elimination step."

- question: "Why does Skolemization preserve satisfiability but not logical equivalence, and why is satisfiability-preservation sufficient for automated theorem proving via resolution?"
  type: short-answer
  answer: "Satisfiability is preserved because: if φ has a model, that model's existential witnesses can be used to define Skolem functions, extending the model to satisfy φ_S; conversely, any model of φ_S satisfies φ by existential introduction. Logical equivalence fails because φ_S is stronger: it commits to a specific choice function for all instances, while φ only requires that some witness exists in each model independently. For automated theorem proving, satisfiability-preservation suffices because resolution proves unsatisfiability: to prove a theorem T, you negate it, Skolemize, convert to clauses, and run resolution. If the original negation was unsatisfiable, the Skolemized version is too (by equisatisfiability), and resolution will find a refutation. No stronger property is needed."
  explanation: "The critical point is what resolution is *doing*: it is searching for a refutation (proof that a set of clauses is unsatisfiable). For this purpose, you only need to know that satisfiability is the same before and after Skolemization. If you needed to reconstruct models or reason about truth in specific interpretations, logical equivalence would matter. But since refutation only cares about whether a model exists at all, equisatisfiability is precisely the right property — no stronger, no weaker."
```

## Explainer

You've studied prenex normal form: any first-order formula can be rewritten so all quantifiers appear at the front, producing a prefix of quantifiers followed by a quantifier-free matrix. A formula in prenex form looks like Q₁x₁ Q₂x₂ ... Qₙxₙ M(x₁,...,xₙ), where each Qᵢ is either ∀ or ∃. **Skolemization** is the process of eliminating all existential quantifiers from this prefix by replacing them with **Skolem functions** — fresh function symbols not appearing anywhere else in the formula.

The rule is: when you encounter an existential quantifier ∃y in the prefix, and the universally quantified variables introduced before it are x₁, ..., xₖ, replace every occurrence of y in the matrix with a fresh function term f(x₁,...,xₖ). This encodes the semantic content of ∃y: "there exists a witness for y, and that witness may depend on the universally quantified variables that have already been fixed." If there are no preceding ∀ quantifiers (∃y is the outermost quantifier), replace y with a fresh **Skolem constant** c — a 0-ary function. For example, ∀x ∃y P(x, y) Skolemizes to ∀x P(x, f(x)), and ∃y ∀x P(x, y) Skolemizes to ∀x P(x, c). After all existential quantifiers are eliminated, the prefix contains only ∀ quantifiers, which can be dropped — all remaining variables are understood to be universally quantified.

The critical property of Skolemization is **equisatisfiability**, not logical equivalence. The original formula φ and its Skolemized version φ_S have the same satisfiability: φ is satisfiable if and only if φ_S is satisfiable. To see why in one direction: if M ⊨ φ, then for each x the existential ∃y P(x, y) is witnessed by some element; define f(x) to be any such witness. Then M extended with this interpretation of f satisfies φ_S. In the other direction, any model of φ_S already satisfies φ by existential introduction — just say "let the witness be f(x)." However, φ and φ_S are *not* logically equivalent: φ_S is typically logically stronger (it asserts a uniform choice function, not merely the existence of witnesses), so Skolemization can never be reversed without changing meaning.

Equisatisfiability is exactly what automated theorem provers need. Resolution works on clause sets — quantifier-free, universally-quantified first-order clauses. By converting to prenex normal form and then Skolemizing, you reduce any first-order satisfiability question to a purely universal one, and then to a set of clauses via CNF conversion. The Skolem functions in the clauses act as terms: resolution's **unification** algorithm matches these terms against each other, effectively performing instantiation. Skolemization is thus the bridge between the expressive language of first-order logic with mixed quantifiers and the tractable, purely universal language that resolution can manipulate algorithmically.
