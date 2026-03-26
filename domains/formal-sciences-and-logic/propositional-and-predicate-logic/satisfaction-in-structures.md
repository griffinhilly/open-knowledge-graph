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
status: validated
---

# Satisfaction of Formulas in Structures

## Core Idea
A formula φ is satisfied in a structure M (M ⊨ φ) if it evaluates to true under M's interpretation. Satisfaction is defined recursively: atomic formulas based on the interpretation, compound formulas based on connective truth conditions, quantified formulas based on existence or universality of satisfying variable assignments.

## Questions

```yaml
- question: "The sentence ∀x∀y (x < y → ∃z (x < z ∧ z < y)) — 'between any two elements there is a third' — is true in (ℚ, <) but false in (ℤ, <). What does this demonstrate?"
  type: multiple-choice
  options:
    - "The sentence is logically invalid, since it fails in at least one structure"
    - "The sentence is logically valid, since it succeeds in at least one structure"
    - "The truth value of a first-order sentence is relative to the structure, not an intrinsic property of the formula alone"
    - "Quantifiers behave differently over rational numbers than over integers, making universal quantification unreliable"
  answer: 2
  explanation: "A sentence's truth is not absolute in first-order logic — it holds or fails relative to a specific structure's domain and interpretation. The sentence is true in (ℚ, <) because the rationals are dense (there is always a rational between any two rationals). It is false in (ℤ, <) because there is nothing between 3 and 4 in the integers. The same formula, different structure, different truth value. This is the foundational concept of model theory: M ⊨ φ is a relation, not a property of φ alone."

- question: "To evaluate whether M ⊨ ∃x P(x), which of the following must be true?"
  type: multiple-choice
  options:
    - "P(x) must hold for every element a in the domain |M|"
    - "There must exist at least one element a ∈ |M| such that M ⊨ P(x)[x↦a]"
    - "The variable x must already be assigned a value in the variable assignment s"
    - "P must be interpreted as a total function in the structure M"
  answer: 1
  explanation: "The existential quantifier ∃x φ is satisfied in M iff there is *some* element a in the domain |M| for which φ is satisfied when x is assigned to a. You only need one witness — if any single element makes the formula true, ∃x φ is satisfied. Option A describes universal quantification (∀). Option C is wrong because the quantifier itself binds x; no prior assignment is needed."

- question: "For a sentence φ (a formula with no free variables), the truth value M ⊨ φ does not depend on the variable assignment s."
  type: true-false
  answer: true
  explanation: "Variable assignments matter only for free variables — the open slots in a formula that must be assigned concrete domain elements before the formula has a truth value. A sentence has no free variables by definition; all variables are bound by quantifiers, which range over the domain themselves. So whether M ⊨ φ holds is determined entirely by the structure M and not by any particular assignment s. This is why sentences can be said to be simply 'true or false in M' without specifying s."

- question: "A formula that is satisfiable (true in some structure) is also valid (true in most structures)."
  type: true-false
  answer: false
  explanation: "Satisfiability and validity are distinct logical properties. A satisfiable formula is one that is true in *at least one* structure. A valid formula is true in *every* structure (a tautology). Most interesting formulas are satisfiable but not valid — the example ∀x∀y (x < y → ∃z (x < z ∧ z < y)) is true in (ℚ, <) but false in (ℤ, <), so it is satisfiable but not valid. Only logical tautologies like ∀x (P(x) → P(x)) are valid."

- question: "Explain why evaluating a first-order sentence requires specifying a structure M, rather than simply determining whether the sentence is 'true' on its own."
  type: short-answer
  answer: "First-order sentences contain predicate symbols, function symbols, and constants that have no meaning by themselves — they are just syntactic labels. A structure M assigns each symbol a concrete interpretation: predicates become sets of tuples, functions become actual functions, constants become domain elements. Without a structure, 'x < y' has no truth value because < has no meaning, and the domain for quantifiers to range over is undefined. Satisfaction M ⊨ φ is inherently a relation between a formula and a structure because the formula's truth depends entirely on what the symbols are interpreted to mean in a specific mathematical universe."
  explanation: "This is what distinguishes first-order logic from propositional logic, where truth values are directly assigned. In first-order logic, meaning is supplied by structures, making satisfaction a two-place relation. Model theory studies exactly this relationship — which formulas are true in which structures — and it underlies all of modern mathematics' foundations."
```

## Explainer

From your study of structures and interpretations, you know that a **structure** M for a first-order language L consists of a non-empty domain |M|, an interpretation of each constant symbol as an element of |M|, each function symbol as an actual function on |M|, and each predicate symbol as a subset of |M|ⁿ (a set of n-tuples). Satisfaction is the bridge between this semantic object and the syntactic formulas of L. It answers the question: is formula φ true in M?

The definition is **recursive** on formula structure. For **atomic formulas**, the base cases: a formula P(t₁, …, tₙ) is satisfied in M (under variable assignment s) if the tuple (t₁^(M,s), …, tₙ^(M,s)) — where each tᵢ^(M,s) evaluates the term under M and s — belongs to the interpretation of P. For example, if M = (ℕ, <) and φ is "x < y", then M ⊨ φ[s] if and only if s(x) < s(y) in the natural number ordering. The atomic case grounds everything in the concrete interpretation.

Compound formulas follow classical truth tables. M ⊨ ¬φ [s] iff M ⊭ φ[s]. M ⊨ φ ∧ ψ [s] iff both M ⊨ φ[s] and M ⊨ ψ[s]. Similarly for ∨ and →. Nothing surprising here — the connectives just propagate truth values computed by the recursive calls. The interesting case is **quantifiers**. M ⊨ ∃x φ [s] iff there exists some element a ∈ |M| such that M ⊨ φ[s(x↦a)] — that is, some assignment of x to a concrete domain element makes φ true. M ⊨ ∀x φ [s] iff for every a ∈ |M|, M ⊨ φ[s(x↦a)]. The notation s(x↦a) means the assignment that maps x to a and agrees with s on all other variables.

For a **sentence** (a formula with no free variables), the truth value does not depend on the variable assignment — the assignment only matters for the free variables, and sentences have none. So we write M ⊨ φ without an assignment. The sentence ∀x∀y (x < y → ∃z (x < z ∧ z < y)) says "between any two elements there is a third." It is true in (ℚ, <) and false in (ℤ, <) — in the integers, there is nothing between 3 and 4. This single example shows how satisfaction is sensitive to the structure's domain, not just its signature. The same formula, different structure, different truth value. The **satisfaction relation** ⊨ is thus a relation between structures and sentences, and understanding it is the entire foundation for model theory, logical consequence, and the notion of what a mathematical statement "means."

