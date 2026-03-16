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
builds-toward:
- ground-instances-and-instantiation
tags:
- first-order-logic
- normal-forms
- automated-reasoning
stage: formal-systems
status: draft
---

# Conversion to Clausal Form

## Core Idea
Any first-order formula can be converted to clausal form (a conjunction of disjunctions of literals), which is the canonical input format for resolution-based theorem provers. The conversion process involves converting to prenex normal form, Skolemization, and distribution of conjunction over disjunction—understanding this process is essential for using automated reasoning tools.

## Explainer

You know how to convert a propositional formula to **conjunctive normal form (CNF)** — a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals (atomic formulas or their negations). For propositional logic, CNF is the end state. For first-order logic, the analogous goal is **clausal form**: a set of clauses where each clause is a disjunction of first-order literals, with all variables implicitly universally quantified. Resolution-based theorem provers like Prolog's underlying engine and ATP systems (Vampire, E, SPASS) require their input in clausal form, so learning the conversion pipeline is essential for applying automated reasoning.

The pipeline has three stages. First, convert to **prenex normal form** (PNF): push all quantifiers to the front of the formula so that the quantifier block (the prefix) precedes a quantifier-free matrix. You know how to do this: push negations inward using De Morgan's laws and the rules ¬∀x φ ≡ ∃x ¬φ and ¬∃x φ ≡ ∀x ¬φ, then pull quantifiers outward using the rules for conjunction and disjunction. The result is a formula like ∀x ∃y ∀z M(x, y, z) where M is quantifier-free. Second, apply **Skolemization**: replace each existential quantifier with a Skolem function whose arguments are all universally quantified variables that have been introduced earlier. If ∃y appears after ∀x, replace every occurrence of y with a fresh function symbol f(x). After Skolemization you have a universally quantified formula — all quantifiers are ∀ — so you can drop the universal prefix entirely, since all remaining variables are understood to be universally quantified. The Skolemized formula is **equisatisfiable** with the original: it has a model if and only if the original does, though the two formulas are not logically equivalent.

Third, distribute the matrix into CNF. The Skolemized matrix is a quantifier-free first-order formula — you can apply the same propositional CNF conversion to it, treating atomic formulas as propositional atoms. Use distribution of ∨ over ∧ (or equivalently the TSEITIN transformation for efficiency) to produce a conjunction of clauses. Each clause becomes a member of the clause set. The entire process converts any first-order formula into a finite set of clauses that is equisatisfiable with the original. The clause set `{C₁, C₂, ..., Cₙ}` is treated as their conjunction, and each variable in each clause is universally quantified.

A worked example clarifies the pipeline. Start with ∀x (P(x) → ∃y Q(x,y)). Expand the implication: ∀x (¬P(x) ∨ ∃y Q(x,y)). Pull the existential quantifier outward: ∀x ∃y (¬P(x) ∨ Q(x,y)). Skolemize: replace y with f(x), giving ∀x (¬P(x) ∨ Q(x,f(x))). Drop the universal quantifier (variables implicitly ∀). The result is the single clause {¬P(x), Q(x,f(x))} — a clause set with one clause and one Skolem function. Resolution can now operate on this clause set directly, deriving consequences by combining and canceling complementary literals across clauses.
