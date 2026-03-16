---
id: formulas-and-well-formed-expressions
title: Formulas and Well-Formed Expressions
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: terms-and-atomic-formulas
  type: hard
builds-toward:
- structures-and-interpretations
- first-order-logic-syntax
tags:
- syntax
- first-order-logic
stage: formal-systems
status: draft
---

# Formulas and Well-Formed Expressions

## Core Idea
Well-formed formulas are recursively defined: every atomic formula is a wff; if φ and ψ are wffs, then so are ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), ∀x φ, and ∃x φ. This syntax is the foundation for assigning meanings via interpretations in structures.

## Explainer

You already know how to construct **terms** (expressions that name objects) and **atomic formulas** (the simplest sentences, like R(t₁, t₂) or t₁ = t₂). A **well-formed formula** (wff) is a syntactic expression that has a definite grammatical structure — it is a legitimate sentence of the logical language, as opposed to a random string of symbols. The definition is **recursive**: start from atomic formulas, then close under the logical connectives and quantifiers. Every atomic formula is a wff. If φ is a wff, then so is ¬φ. If φ and ψ are wffs, then so are (φ ∧ ψ), (φ ∨ ψ), and (φ → ψ). If φ is a wff and x is a variable, then ∀x φ and ∃x φ are wffs. Nothing else is a wff.

This recursive definition is not just an arbitrary grammar rule — it is what makes logical syntax compositional. The meaning of a compound formula is determined entirely by the meanings of its parts and the connective that joins them. Without a precise grammar, we could not define semantics at all: "what does this expression mean?" presupposes that the expression is grammatically legitimate. The wff definition is the contract between syntax and semantics — it specifies exactly which strings the semantics is obligated to interpret.

The recursive structure also enables **structural induction**, the primary proof technique for results about formulas. To prove a property holds for all wffs, prove it for all atomic formulas (base case), then show that if it holds for φ and ψ, it holds for ¬φ, (φ ∧ ψ), ∀x φ, and so on (inductive step). Almost every result in logic — soundness, completeness, compactness — is proved by structural induction on the formula. When you encounter a metatheorem like "every valid formula is provable," you should expect to prove it by induction on the complexity of the formula.

A key distinction the wff definition enables is between **free** and **bound** occurrences of variables. In ∀x (P(x) → Q(x, y)), the variable x is bound (governed by ∀x) while y is free (no quantifier governs it). The wff definition makes this distinction precise: a variable occurrence is bound if it falls within the scope of a quantifier for that variable, which the recursive structure tracks exactly. Free variables are the "parameters" of a formula — the formula expresses a property of them. Bound variables are internal bookkeeping. This distinction is foundational for substitution, semantics, and the correct statement of every theorem about first-order logic.
