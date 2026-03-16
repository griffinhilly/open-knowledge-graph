---
id: well-formed-formulas-logic
title: Well-Formed Formulas (WFF) in Propositional and First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-connectives
  type: hard
- id: propositional-syntax
  type: hard
builds-toward:
- atomic-versus-complex-formulas
- logical-consequence-and-entailment
- open-and-closed-formulas-fol
tags:
- syntax
- propositional-logic
- first-order-logic
- wff
stage: formal-systems
status: draft
---

# Well-Formed Formulas (WFF) in Propositional and First-Order Logic

## Core Idea
A well-formed formula (WFF) is a syntactically valid string following the grammar rules of propositional or first-order logic. In propositional logic, WFFs are built from atomic propositions and connectives (¬, ∧, ∨, →, ↔). In first-order logic, WFFs also include terms, predicates, and quantifiers (∀, ∃), with strict rules about variable binding and scope. Understanding what counts as a valid formula is foundational to defining logical consequence, proof systems, and semantics.

## How It's Best Learned
Start with propositional WFFs using simple examples and counterexamples (e.g., 'P ∧ Q' is WFF, but '∧ P' is not). Progress to first-order by adding terms and quantifiers with exercises on spotting syntactic errors. Use recursive grammar definitions and parse trees to visualize structure.

## Common Misconceptions
- Thinking that any string of symbols with logical connectives is a WFF (no — syntax matters).
- Forgetting that quantifiers must bind variables correctly (∀x P(y) is WFF but leaves y free).
- Assuming parentheses don't matter (they do — they determine scope and precedence).

## Explainer

You already know the propositional connectives — ¬, ∧, ∨, →, ↔ — and the basic syntax of propositional logic. A **well-formed formula (WFF)** is the precise definition of what counts as a grammatically legal string in a logical language. The point is that not every sequence of symbols is meaningful: "∧ P Q ¬" is not a formula any more than "the cat sat the" is a sentence. WFFs are defined by an inductive grammar that tells you exactly which strings are legal.

For **propositional logic**, the grammar is simple. Every atomic proposition (P, Q, R, …) is a WFF. If φ is a WFF, then ¬φ is a WFF. If φ and ψ are WFFs, then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), and (φ ↔ ψ) are WFFs. That's it — nothing else is a WFF. This inductive definition is powerful because it gives every formula a unique **parse tree**: a tree whose leaves are atomic propositions and whose internal nodes are connectives. The parse tree makes the meaning of a formula unambiguous and is the structure used when evaluating formulas with truth tables.

**First-order logic** extends this with three new ingredients: **terms** (built from variables, constants, and function symbols), **predicates** (applied to terms to make atomic formulas), and **quantifiers** (∀x and ∃x, which bind the variable x). An atomic formula in FOL is something like P(f(x), c) — a predicate applied to terms. Complex FOL formulas are then built by applying connectives and quantifiers: ∀x ∃y (R(x,y) ∧ ¬P(y)) is a WFF; ∀P(x) is not (you cannot quantify over predicates in first-order logic).

The subtlest new concept in FOL WFFs is **variable binding and scope**. In ∀x (P(x) → Q(x)), both occurrences of x are *bound* by the universal quantifier — they are not free variables, just formal placeholders. In ∀x P(x) ∧ Q(y), the variable y is *free* — it is not bound by any quantifier and acts like an unspecified parameter. A formula with no free variables is called a **sentence** (or **closed formula**); it is either true or false in a given structure. A formula with free variables has a truth value only once the free variables are assigned specific elements from the domain. This distinction matters enormously: sentences express propositions about a structure, while open formulas express properties of elements.

Understanding WFFs is foundational because every subsequent concept in logic — truth, satisfaction, proof, consequence — is defined by induction on the structure of WFFs. When you evaluate a formula's truth value, you recurse through its parse tree. When you define what a proof is, you build it up from WFFs step by step. The grammar of WFFs is the backbone on which all of logic hangs.
