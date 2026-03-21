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

## Questions

```yaml
- question: "Why is a recursive definition of well-formed formulas (wffs) necessary, rather than simply providing a comprehensive list of valid formulas?"
  type: multiple-choice
  options:
    - "Listing all valid formulas is possible in principle but the list would be very long, so recursion is used for convenience"
    - "The recursive definition enables structural induction and makes semantics compositional — the meaning of any compound formula is determined by the meanings of its parts and their connective"
    - "A recursive definition allows logic to handle self-referential formulas and circular definitions"
    - "Listing all valid formulas would produce ambiguous parsings, whereas recursion avoids this"
  answer: 1
  explanation: "There are infinitely many wffs, so enumeration is impossible. But more fundamentally, the recursive definition does two things no list can: it enables structural induction (proofs about all wffs reduce to base cases and inductive steps), and it makes semantics compositional — the truth conditions of (φ ∧ ψ) are determined by the truth conditions of φ and ψ and the meaning of ∧. Without compositional structure, semantics cannot be defined for formulas not yet seen. The recursion is the bridge between syntax and semantics."

- question: "In the formula ∀x (P(x) → Q(x, y)), which correctly describes the variable occurrences?"
  type: multiple-choice
  options:
    - "Both x and y are bound, since the entire formula is governed by ∀x"
    - "x is bound (governed by ∀x throughout its scope) and y is free (no quantifier governs y)"
    - "x is free in the antecedent P(x) and bound in the consequent Q(x, y)"
    - "y is bound because it appears within the scope of ∀x, which governs the whole subformula"
  answer: 1
  explanation: "The scope of ∀x is the entire formula (P(x) → Q(x, y)). All occurrences of x fall within this scope, so x is bound everywhere it appears. The variable y has no governing quantifier anywhere in the formula — no ∃y or ∀y appears — so every occurrence of y is free. Binding requires a *matching* quantifier: ∀x only binds x, not y. Free variables are the 'parameters' of the formula — this formula expresses a property of y. The wff definition tracks this distinction precisely through its recursive scope rules."

- question: "Every theorem about all well-formed formulas can in principle be proved by structural induction, because the recursive definition of wffs specifies exactly the construction cases that must be handled."
  type: true-false
  answer: true
  explanation: "Structural induction mirrors the recursive structure of wffs directly. To prove property P holds for all wffs: prove P for all atomic formulas (base case), then show that if P holds for wffs φ and ψ, it holds for ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), ∀x φ, and ∃x φ (inductive steps). Since these cases exhaust all possible wffs by the recursive definition, the proof covers everything. The soundness theorem, completeness theorem, and compactness theorem for first-order logic are all proved by structural induction on the formula."

- question: "In the formula ∀x (P(x) → Q(x, y)), both x and y are bound variables, since x appears under the quantifier ∀x which governs the entire formula."
  type: true-false
  answer: false
  explanation: "Only x is bound; y is free. The quantifier ∀x binds x throughout the formula's scope — every occurrence of x is bound by it. But binding is variable-specific: ∀x only binds x, not any other variable. Since no ∀y or ∃y appears anywhere, y has no governing quantifier and every occurrence of y is free. The rule is precise: a variable occurrence is bound if and only if it falls within the scope of a quantifier *for that specific variable*. Free variables are the parameters of the formula — it expresses a property about them, not about bound placeholders."

- question: "Explain why the recursive definition of wffs is described as 'the contract between syntax and semantics.' What would be lost without a recursive definition?"
  type: short-answer
  answer: "The wff definition specifies exactly which expressions the semantics is obligated to interpret, and it provides the compositional structure needed to define truth conditions. The semantics can define the meaning of (φ ∧ ψ) in terms of the meanings of φ and ψ because the recursive definition guarantees φ and ψ are themselves wffs with their own meanings. Without recursion, we could only assign meanings to explicitly listed formulas, leaving infinitely many others undefined. We also lose structural induction as a proof technique."
  explanation: "The 'contract' metaphor captures a mutual commitment: the wff definition commits the semanticist to interpret every formula the grammar generates (no new formulas that the semantics hasn't handled), and the grammar commits to generating only formulas with the compositional structure the semantics requires. Without recursion, proofs about all formulas would be impossible — you'd have no way to enumerate the cases. Nearly every major result in logic (soundness, completeness, compactness) would have no proof technique available. The recursive definition is the architectural foundation the rest of the subject rests on."
```

## Explainer

You already know how to construct **terms** (expressions that name objects) and **atomic formulas** (the simplest sentences, like R(t₁, t₂) or t₁ = t₂). A **well-formed formula** (wff) is a syntactic expression that has a definite grammatical structure — it is a legitimate sentence of the logical language, as opposed to a random string of symbols. The definition is **recursive**: start from atomic formulas, then close under the logical connectives and quantifiers. Every atomic formula is a wff. If φ is a wff, then so is ¬φ. If φ and ψ are wffs, then so are (φ ∧ ψ), (φ ∨ ψ), and (φ → ψ). If φ is a wff and x is a variable, then ∀x φ and ∃x φ are wffs. Nothing else is a wff.

This recursive definition is not just an arbitrary grammar rule — it is what makes logical syntax compositional. The meaning of a compound formula is determined entirely by the meanings of its parts and the connective that joins them. Without a precise grammar, we could not define semantics at all: "what does this expression mean?" presupposes that the expression is grammatically legitimate. The wff definition is the contract between syntax and semantics — it specifies exactly which strings the semantics is obligated to interpret.

The recursive structure also enables **structural induction**, the primary proof technique for results about formulas. To prove a property holds for all wffs, prove it for all atomic formulas (base case), then show that if it holds for φ and ψ, it holds for ¬φ, (φ ∧ ψ), ∀x φ, and so on (inductive step). Almost every result in logic — soundness, completeness, compactness — is proved by structural induction on the formula. When you encounter a metatheorem like "every valid formula is provable," you should expect to prove it by induction on the complexity of the formula.

A key distinction the wff definition enables is between **free** and **bound** occurrences of variables. In ∀x (P(x) → Q(x, y)), the variable x is bound (governed by ∀x) while y is free (no quantifier governs it). The wff definition makes this distinction precise: a variable occurrence is bound if it falls within the scope of a quantifier for that variable, which the recursive structure tracks exactly. Free variables are the "parameters" of a formula — the formula expresses a property of them. Bound variables are internal bookkeeping. This distinction is foundational for substitution, semantics, and the correct statement of every theorem about first-order logic.
