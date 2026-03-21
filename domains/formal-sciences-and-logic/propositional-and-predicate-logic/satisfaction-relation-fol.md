---
id: satisfaction-relation-fol
title: Satisfaction Relation in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: domain-and-structure-fol
  type: hard
- id: first-order-semantics
  type: hard
builds-toward:
- counterexample-and-refutation
tags:
- first-order-logic
- satisfaction
- semantics
stage: formal-systems
status: draft
---

# Satisfaction Relation in First-Order Logic

## Core Idea
A formula φ is satisfied by a structure M under a variable assignment σ (written M ⊨ φ[σ]) if the formula is true when variables are interpreted according to σ and structure M. The satisfaction relation extends the notion of truth from propositional logic to first-order logic, allowing quantified formulas to be interpreted as ranging over elements of the domain.

## Questions

```yaml
- question: "In structure M = (ℤ, <), consider the formula φ: 'x < y'. Which statement correctly evaluates M ⊨ φ[σ]?"
  type: multiple-choice
  options:
    - "It is true in M, because in ℤ there always exist integers x and y with x < y"
    - "It depends on the variable assignment σ — it is true when σ(x) < σ(y) and false otherwise"
    - "It is false because x and y are not bound by quantifiers"
    - "It cannot be evaluated until the domain of σ is specified separately from M"
  answer: 1
  explanation: "A formula with free variables does not have a fixed truth value in a structure alone — its truth depends on what the free variables are assigned. With σ(x) = 3 and σ(y) = 5, the formula is true; with σ(x) = 7 and σ(y) = 2, it is false — same structure, same formula, different variable assignments, different truth values. Option A is the classic confusion: existential quantification (∃x ∃y x < y) is true in ℤ, but the unquantified formula 'x < y' with free variables is a different claim entirely."

- question: "Which of the following is a sentence — a formula that can be evaluated in a structure without any variable assignment?"
  type: multiple-choice
  options:
    - "x < y + 1"
    - "∃x (x < y)"
    - "∀x ∀y (x < y ∨ y < x ∨ x = y)"
    - "P(x) ∧ Q(y)"
  answer: 2
  explanation: "A sentence has no free variables — all variables are bound by quantifiers. Option C, ∀x ∀y (x < y ∨ y ≤ x), has every variable bound by ∀. Options A and D have free variables x and y with no quantifier. Option B has ∃x binding x, but y remains free — so it is not a sentence. Only option C can be evaluated as simply true or false in a structure without specifying what any variable refers to."

- question: "A formula with free variables has a definite truth value in a structure M, regardless of which variable assignment is used."
  type: true-false
  answer: false
  explanation: "Free variables are like parameters: their values are supplied by the variable assignment σ, not by the structure alone. The same formula 'x > 0' is true in (ℤ, >) under σ(x) = 5 and false under σ(x) = −2. Only sentences — formulas with no free variables — have truth values in a structure independent of any assignment."

- question: "The formula ∀x ψ is satisfied under assignment σ if there exists at least one element a in the domain such that ψ is satisfied when x is mapped to a."
  type: true-false
  answer: false
  explanation: "This describes the existential quantifier ∃x ψ, not the universal. For ∀x ψ to be satisfied, every element a of the domain must satisfy ψ when x is mapped to a. A single counterexample — one element a for which ψ fails — is enough to falsify ∀x ψ. The satisfaction clauses for ∃ and ∀ are duals: ∃ requires at least one witness; ∀ requires no exceptions."

- question: "Explain the difference between a formula and a sentence in first-order logic, and why the satisfaction relation requires a variable assignment for formulas but not for sentences."
  type: short-answer
  answer: "A sentence has no free variables — every variable is bound by a quantifier. A formula may have free variables whose values are not determined by the formula itself. Free variables act as parameters: the satisfaction relation M ⊨ φ[σ] tracks the assignment σ to supply values for them. When φ is a sentence, truth depends only on the structure M and is written M ⊨ φ without σ, because no variables need external assignment."
  explanation: "This distinction is foundational for model theory. Sentences express properties of structures (e.g., 'this group is abelian'). Formulas with free variables express properties of elements relative to a structure (e.g., 'this element has a multiplicative inverse'). A theory — a set of sentences — is satisfiable if some structure makes all of them true; this notion depends on having sentences, not formulas."
```

## Explainer

In propositional logic, satisfaction was simple: a formula is true or false in a valuation, and valuations just assign true/false to each propositional variable. First-order logic is more complex because formulas contain **variables** that range over elements of a domain, **quantifiers** that bind those variables, and **terms** that denote specific domain elements. The satisfaction relation M ⊨ φ[σ] is the rigorous definition of what it means for φ to be "true in M when variables are interpreted by σ."

A **variable assignment** σ is a function from variables to elements of the domain M. If φ has free variable x, then σ(x) is the specific element of M that x refers to. For example, if M = (ℤ, <) and φ is the formula x < y, then M ⊨ φ[σ] holds iff σ(x) < σ(y) in ℤ. With σ(x) = 3 and σ(y) = 5, this is true; with σ(x) = 7 and σ(y) = 2, this is false. The same formula has different truth values under different variable assignments in the same structure.

The satisfaction relation is defined **recursively** on the structure of φ:
- For an atomic formula R(t₁,…,tₙ): evaluate each term tᵢ in M under σ to get elements aᵢ, then check whether (a₁,…,aₙ) ∈ R^M.
- For ¬ψ: M ⊨ ¬ψ[σ] iff M does not satisfy ψ[σ].
- For ψ₁ ∧ ψ₂: M ⊨ (ψ₁ ∧ ψ₂)[σ] iff both M ⊨ ψ₁[σ] and M ⊨ ψ₂[σ].
- For ∃x ψ: M ⊨ ∃x ψ[σ] iff there exists some element a ∈ M such that M ⊨ ψ[σ[x↦a]], where σ[x↦a] is σ modified to send x to a.
- For ∀x ψ: M ⊨ ∀x ψ[σ] iff for *every* element a ∈ M, M ⊨ ψ[σ[x↦a]].

The quantifier cases are the key innovation over propositional logic. **∃x ψ** is satisfied if at least one element of the domain witnesses it; **∀x ψ** is satisfied if every element does. When φ is a **sentence** (no free variables), the truth value does not depend on σ at all — we simply write M ⊨ φ. This is why sentences express properties of structures themselves, while formulas with free variables express properties of *elements* relative to a structure. The satisfaction relation is the semantic foundation for all of model theory: two structures are **elementarily equivalent** if they satisfy exactly the same sentences, and a theory is **satisfiable** if some structure satisfies all of its sentences.

