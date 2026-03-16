---
id: satisfaction-in-structures
title: Satisfaction of Formulas in Structures
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: structures-and-interpretations
  type: hard
builds-toward:
- logical-consequence-and-validity
tags:
- semantics
- models
- first-order-logic
stage: formal-systems
status: draft
---

# Satisfaction of Formulas in Structures

## Core Idea
A formula φ is satisfied in a structure M (M ⊨ φ) if it evaluates to true under M's interpretation. Satisfaction is defined recursively: atomic formulas based on the interpretation, compound formulas based on connective truth conditions, quantified formulas based on existence or universality of satisfying variable assignments.

## Explainer

From your study of structures and interpretations, you know that a **structure** M for a first-order language L consists of a non-empty domain |M|, an interpretation of each constant symbol as an element of |M|, each function symbol as an actual function on |M|, and each predicate symbol as a subset of |M|ⁿ (a set of n-tuples). Satisfaction is the bridge between this semantic object and the syntactic formulas of L. It answers the question: is formula φ true in M?

The definition is **recursive** on formula structure. For **atomic formulas**, the base cases: a formula P(t₁, …, tₙ) is satisfied in M (under variable assignment s) if the tuple (t₁^(M,s), …, tₙ^(M,s)) — where each tᵢ^(M,s) evaluates the term under M and s — belongs to the interpretation of P. For example, if M = (ℕ, <) and φ is "x < y", then M ⊨ φ[s] if and only if s(x) < s(y) in the natural number ordering. The atomic case grounds everything in the concrete interpretation.

Compound formulas follow classical truth tables. M ⊨ ¬φ [s] iff M ⊭ φ[s]. M ⊨ φ ∧ ψ [s] iff both M ⊨ φ[s] and M ⊨ ψ[s]. Similarly for ∨ and →. Nothing surprising here — the connectives just propagate truth values computed by the recursive calls. The interesting case is **quantifiers**. M ⊨ ∃x φ [s] iff there exists some element a ∈ |M| such that M ⊨ φ[s(x↦a)] — that is, some assignment of x to a concrete domain element makes φ true. M ⊨ ∀x φ [s] iff for every a ∈ |M|, M ⊨ φ[s(x↦a)]. The notation s(x↦a) means the assignment that maps x to a and agrees with s on all other variables.

For a **sentence** (a formula with no free variables), the truth value does not depend on the variable assignment — the assignment only matters for the free variables, and sentences have none. So we write M ⊨ φ without an assignment. The sentence ∀x∀y (x < y → ∃z (x < z ∧ z < y)) says "between any two elements there is a third." It is true in (ℚ, <) and false in (ℤ, <) — in the integers, there is nothing between 3 and 4. This single example shows how satisfaction is sensitive to the structure's domain, not just its signature. The same formula, different structure, different truth value. The **satisfaction relation** ⊨ is thus a relation between structures and sentences, and understanding it is the entire foundation for model theory, logical consequence, and the notion of what a mathematical statement "means."

