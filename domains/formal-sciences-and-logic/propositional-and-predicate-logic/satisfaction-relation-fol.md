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

