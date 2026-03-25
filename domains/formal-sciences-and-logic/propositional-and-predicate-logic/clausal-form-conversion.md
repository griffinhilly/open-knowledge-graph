---
id: clausal-form-conversion
title: Conversion to Clausal Form
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: normal-forms-cnf-dnf
  type: hard
- id: prenex-normal-form
  type: hard
- id: skolemization-and-witnesses
  type: hard
- id: skolemization-and-equisatisfiability
  type: soft
- id: literals-and-clauses-cnf
  type: soft
builds-toward:
- ground-instances-and-instantiation
tags:
- first-order-logic
- normal-forms
- automated-reasoning
stage: advanced
status: validated
---
# Conversion to Clausal Form

## Core Idea
Any first-order formula can be converted to clausal form (a conjunction of disjunctions of literals), which is the canonical input format for resolution-based theorem provers. The conversion process involves converting to prenex normal form, Skolemization, and distribution of conjunction over disjunction—understanding this process is essential for using automated reasoning tools.

## Questions

```yaml
- question: "After applying the full clausal-form conversion pipeline to ∀x (P(x) → ∃y Q(x,y)), what is the result?"
  type: multiple-choice
  options:
    - "A logically equivalent formula ∀x (¬P(x) ∨ Q(x, f(x)))"
    - "An equisatisfiable clause {¬P(x), Q(x, f(x))} with f a Skolem function"
    - "The formula remains unchanged because it is already in prenex form"
    - "Two clauses: {¬P(x)} and {Q(x, f(x))}"
  answer: 1
  explanation: "The implication expands to ∀x (¬P(x) ∨ ∃y Q(x,y)), PNF pulls the quantifier out to ∀x ∃y (¬P(x) ∨ Q(x,y)), Skolemization replaces y with f(x) giving ∀x (¬P(x) ∨ Q(x,f(x))), and dropping the universal prefix yields the single clause {¬P(x), Q(x,f(x))}. Option A says 'logically equivalent' — this is the key error. Skolemization preserves satisfiability, not logical equivalence; the Skolemized formula has a richer signature (f is a new symbol) and is not equivalent to the original."

- question: "A student claims the clausal form of a first-order formula is 'just CNF with quantifiers added back.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — clausal form is exactly quantified CNF"
    - "Clausal form requires removing existential quantifiers via Skolemization, so no quantifiers appear in the final clause set"
    - "Clausal form only applies to propositional logic, not first-order logic"
    - "In clausal form, universal quantifiers are moved to the inside of each clause"
  answer: 1
  explanation: "The student's claim misses the Skolemization step. Clausal form eliminates all existential quantifiers by replacing them with Skolem functions. The resulting clause set has only universally quantified variables, and by convention those universal quantifiers are dropped — variables are understood to be universally quantified. This is not 'CNF with quantifiers added back'; it is a quantifier-free clause set that is equisatisfiable with, but not logically equivalent to, the original."

- question: "A first-order formula and its clausal form are logically equivalent."
  type: true-false
  answer: false
  explanation: "Clausal form conversion involves Skolemization, which preserves satisfiability but not logical equivalence. The Skolemized formula introduces new function symbols not in the original vocabulary, and the two formulas make claims about different signatures. They are equisatisfiable — one has a model iff the other does — but they are not equivalent. For example, ∃y Q(y) and Q(f) (where f is a Skolem constant) have different models in general."

- question: "After Skolemization of a prenex normal form formula, all remaining variables in the clause set are implicitly universally quantified."
  type: true-false
  answer: true
  explanation: "Skolemization replaces each existential quantifier ∃x with a Skolem function applied to all enclosing universal variables. Once every existential is eliminated, only universal quantifiers remain. By the convention of clausal form, these universal quantifiers are then dropped: in each clause, any variable symbol is understood to be universally quantified over all values in the domain. This is what makes the clause set directly usable by resolution-based theorem provers."

- question: "Why does Skolemization produce a formula that is equisatisfiable with the original rather than logically equivalent to it? What is lost in the transformation?"
  type: short-answer
  answer: "Skolemization replaces existential quantifiers with Skolem functions, which 'choose' witnesses in a vocabulary-dependent way. The Skolemized formula is satisfiable in exactly the same models as the original — if the original is satisfiable, a Skolem model can be constructed; if not, neither is the Skolemized version. But logical equivalence requires the same truth value in all interpretations over the same signature, and the Skolemized formula has extra function symbols the original lacks. It commits to a specific witnessing function, while the original merely asserts existence."
  explanation: "The distinction matters for theorem proving: resolution refutation only requires equisatisfiability (to prove unsatisfiability, we need the clause set to be unsatisfiable iff the original is). Skolemization enables this — it turns existential witnesses into explicit terms manipulable by unification, at the cost of logical equivalence."
```

## Explainer

You know how to convert a propositional formula to **conjunctive normal form (CNF)** — a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals (atomic formulas or their negations). For propositional logic, CNF is the end state. For first-order logic, the analogous goal is **clausal form**: a set of clauses where each clause is a disjunction of first-order literals, with all variables implicitly universally quantified. Resolution-based theorem provers like Prolog's underlying engine and ATP systems (Vampire, E, SPASS) require their input in clausal form, so learning the conversion pipeline is essential for applying automated reasoning.

The pipeline has three stages. First, convert to **prenex normal form** (PNF): push all quantifiers to the front of the formula so that the quantifier block (the prefix) precedes a quantifier-free matrix. You know how to do this: push negations inward using De Morgan's laws and the rules ¬∀x φ ≡ ∃x ¬φ and ¬∃x φ ≡ ∀x ¬φ, then pull quantifiers outward using the rules for conjunction and disjunction. The result is a formula like ∀x ∃y ∀z M(x, y, z) where M is quantifier-free. Second, apply **Skolemization**: replace each existential quantifier with a Skolem function whose arguments are all universally quantified variables that have been introduced earlier. If ∃y appears after ∀x, replace every occurrence of y with a fresh function symbol f(x). After Skolemization you have a universally quantified formula — all quantifiers are ∀ — so you can drop the universal prefix entirely, since all remaining variables are understood to be universally quantified. The Skolemized formula is **equisatisfiable** with the original: it has a model if and only if the original does, though the two formulas are not logically equivalent.

Third, distribute the matrix into CNF. The Skolemized matrix is a quantifier-free first-order formula — you can apply the same propositional CNF conversion to it, treating atomic formulas as propositional atoms. Use distribution of ∨ over ∧ (or equivalently the TSEITIN transformation for efficiency) to produce a conjunction of clauses. Each clause becomes a member of the clause set. The entire process converts any first-order formula into a finite set of clauses that is equisatisfiable with the original. The clause set `{C₁, C₂, ..., Cₙ}` is treated as their conjunction, and each variable in each clause is universally quantified.

A worked example clarifies the pipeline. Start with ∀x (P(x) → ∃y Q(x,y)). Expand the implication: ∀x (¬P(x) ∨ ∃y Q(x,y)). Pull the existential quantifier outward: ∀x ∃y (¬P(x) ∨ Q(x,y)). Skolemize: replace y with f(x), giving ∀x (¬P(x) ∨ Q(x,f(x))). Drop the universal quantifier (variables implicitly ∀). The result is the single clause {¬P(x), Q(x,f(x))} — a clause set with one clause and one Skolem function. Resolution can now operate on this clause set directly, deriving consequences by combining and canceling complementary literals across clauses.
