---
id: atomic-versus-complex-formulas
title: Atomic and Complex Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: term-and-atom-fol
  type: hard
builds-toward:
- literals-and-clauses-cnf
- normal-forms-cnf-dnf
tags:
- syntax
- atomic
- complex
- propositional
- first-order
stage: formal-systems
status: draft
---

# Atomic and Complex Formulas

## Core Idea
An atomic formula is a formula with no logical connectives: in propositional logic, atomic formulas are propositional variables; in first-order logic, they are of the form P(t₁, …, tₙ) where P is a predicate and tᵢ are terms. Complex (or molecular) formulas are built from atomic formulas using logical connectives (¬, ∧, ∨, →, ↔) and/or quantifiers (∀, ∃). This distinction is fundamental: the truth value of a complex formula is determined compositionally from the truth values of its atomic constituents and the semantics of the connectives and quantifiers.

## How It's Best Learned
Use parse trees to visualize formula structure, showing atoms at the leaves and connectives/quantifiers at internal nodes. Practice identifying atoms in formulas of varying complexity. Relate atomicity to recursive definitions of formulas.

## Common Misconceptions
- Thinking a formula with one occurrence of a connective is atomic (it's not — any use of ¬, ∧, ∨, →, ↔, ∀, or ∃ makes it complex).
- Confusing atomic formulas with ground formulas (an atom like P(x) is atomic but not ground).
- Assuming all propositional variables are atoms (they are, but so are first-order predicate applications).

## Explainer

Every formula in a logical language is either an atom or built from atoms using connectives and quantifiers. This is not merely a classification — it is the foundation of how meaning is assigned to formulas. From your work on propositional syntax, you know that a formula is defined recursively: base cases and construction rules. The **atomic formulas** are precisely the base cases: the formulas that cannot be further decomposed. In propositional logic, every propositional variable (p, q, r, ...) is an atom. In first-order logic, atoms look like P(t₁, t₂, ..., tₙ) where P is a predicate symbol and each tᵢ is a term — for example, Loves(x, mary) or x = y.

The critical structural point is that atoms are the only formulas whose truth values are assigned directly by an interpretation. An interpretation specifies, for each predicate P and each tuple of elements from the domain, whether P holds of that tuple. Every other formula's truth value is derived from atoms through the semantics of connectives: ¬φ is true iff φ is false, φ ∧ ψ is true iff both are true, and so on. This **compositionality** — truth built bottom-up from atoms — is what makes logical semantics tractable.

A **parse tree** makes this structure visible. Build the tree of a formula like ¬(P(x) ∧ Q(y)) → R(z): the root is →, its left child is ¬, under which sits ∧, under which sit P(x) and Q(y); the right child of → is R(z). The *leaves* of the parse tree are exactly the atomic subformulas. Every **complex formula** corresponds to an internal node — a connective or quantifier applied to simpler subformulas. This is why atomic formulas are sometimes called "leaves" informally: they are the formulas that have no logical subformulas.

Understanding this distinction is prerequisite to everything that follows: normal forms (CNF, DNF) reorganize complex formulas while keeping atoms intact; resolution and tableaux methods work by decomposing formulas toward atoms; and the definition of logical consequence is stated in terms of truth-value assignments to atoms. When you later encounter clausal normal form, you will be converting arbitrary formulas into flat structures of atoms and their negations — recognizing atoms is what makes that conversion possible.
