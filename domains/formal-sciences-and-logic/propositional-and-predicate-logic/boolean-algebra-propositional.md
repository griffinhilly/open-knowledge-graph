---
id: boolean-algebra-propositional
title: Boolean Algebra and Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: boolean-algebra
  type: soft
builds-toward:
- resolution-propositional
tags:
- boolean-algebra
- lattice
- De-Morgan
- duality
- algebraic-logic
stage: formal-systems
status: draft
---

# Boolean Algebra and Propositional Logic

## Core Idea
A Boolean algebra is an algebraic structure (B, ∧, ∨, ¬, 0, 1) satisfying commutativity, associativity, distributivity, identity, and complementation laws. The two-element Boolean algebra {0, 1} is isomorphic to propositional logic under the correspondence ∧ = AND, ∨ = OR, ¬ = NOT. De Morgan's laws (¬(a ∧ b) = ¬a ∨ ¬b and ¬(a ∨ b) = ¬a ∧ ¬b) and the duality principle — every theorem remains true when ∧ and ∨ are swapped and 0 and 1 are swapped — arise naturally from the lattice structure. Boolean algebra provides an algebraic toolkit for manipulating propositional formulas without truth tables.

## How It's Best Learned
Prove standard propositional equivalences (distribution, absorption, De Morgan) using only the Boolean algebra axioms, without appealing to truth tables. Draw the Hasse diagram for the power-set lattice of a small set to see the lattice structure concretely.

## Common Misconceptions
- Boolean algebra is not just another name for propositional logic — it is a broader algebraic theory with models beyond {0, 1}, including power-set algebras and interval algebras.
- De Morgan's laws are not ad hoc rules but consequences of the complementation and distributivity axioms.
- Duality is a metatheorem (about theorems), not an object-level equivalence between formulas.

## Questions

```yaml
- question: "Consider the Boolean theorem: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c). What does the duality principle tell us about this theorem?"
  type: multiple-choice
  options:
    - "The formula a ∧ (b ∨ c) is logically equivalent to its dual, a ∨ (b ∧ c)"
    - "The theorem's dual — a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) — is also a theorem of Boolean algebra"
    - "The two sides of the equation have the same truth table in every Boolean algebra"
    - "The theorem proves that ∧ and ∨ are interchangeable operations"
  answer: 1
  explanation: "The duality principle is a metatheorem: if you can prove a theorem from the Boolean algebra axioms, then swapping ∧ with ∨ and 0 with 1 throughout gives another theorem. So the distributivity of ∧ over ∨ (the original) and the distributivity of ∨ over ∧ (the dual) are both theorems — you get two for the price of one. Option A is the critical misconception: duality says the *dual theorem is provable*, not that a formula and its dual are logically equivalent. The formula a ∧ (b ∨ c) is generally NOT equivalent to a ∨ (b ∧ c)."

- question: "A student proves De Morgan's law ¬(a ∧ b) = ¬a ∨ ¬b from the Boolean algebra axioms alone, without a truth table. Why is this significant?"
  type: multiple-choice
  options:
    - "It shows De Morgan's law only holds in the two-element Boolean algebra {0, 1}, not in larger models"
    - "It proves the law holds in every Boolean algebra — power-set algebras, interval algebras, and all other models — because the proof used only axioms that all Boolean algebras share"
    - "It demonstrates that De Morgan's law is itself one of the axioms of Boolean algebra"
    - "It shows De Morgan's law is unique to propositional logic and does not extend to algebraic structures"
  answer: 1
  explanation: "A proof from axioms is universal: it holds in every structure satisfying those axioms. De Morgan's law, proved from Boolean algebra axioms, is therefore true in all Boolean algebras — not just {0, 1}, but also the power-set algebra of any set, interval algebras, and others. A truth-table proof, by contrast, only verifies the law for the two-element case. Option C is wrong — De Morgan's laws are theorems, not axioms; they are derived from the complementation and distributivity axioms."

- question: "The two-element Boolean algebra {0, 1} is just one model of Boolean algebra; the same equational laws proved from the axioms hold in power-set algebras and other Boolean algebra models as well."
  type: true-false
  answer: true
  explanation: "Boolean algebra is an equational theory with many models. Any structure satisfying the axioms — commutativity, associativity, distributivity, identity, and complementation — is a Boolean algebra, and every theorem proved from those axioms holds in all such models. The power-set of any set S, with ∩ for ∧, ∪ for ∨, and complement for ¬, is a classic example. Stone's representation theorem shows that every Boolean algebra is isomorphic to a field of sets, making the power-set case canonical."

- question: "The duality principle states that every propositional formula is logically equivalent to its dual — the formula obtained by swapping ∧ with ∨ and 0 with 1."
  type: true-false
  answer: false
  explanation: "This is the central misconception about duality. Duality is a metatheorem about theorems (provable equations), not a claim about individual formulas. It says: if an equation is a theorem of Boolean algebra, then its dual equation is also a theorem. It does NOT say a formula equals its dual. For example, a ∧ b and its dual a ∨ b have completely different truth tables — they are equivalent only in degenerate cases. Confusing the metatheorem with object-level equivalence is a common and consequential error."

- question: "Explain the difference between duality as a metatheorem and logical equivalence between a formula and its dual. Give an example showing they are not the same."
  type: short-answer
  answer: "Duality is a fact about the *theory*: if an equation E is provable from the Boolean algebra axioms, then swapping ∧↔∨ and 0↔1 throughout E gives another provable equation. It says nothing about whether a formula equals its dual. Logical equivalence is a claim about specific formulas: P ≡ Q means they have the same truth value under every assignment. These are different levels. Example: distributivity a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) is a theorem; by duality, so is a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c). But the formula a ∧ (b ∨ c) is NOT logically equivalent to its dual a ∨ (b ∧ c) — set a = 1, b = 0, c = 0: the first gives 0, the second gives 1."
  explanation: "The distinction matters because students often try to use duality to swap connectives inside a formula and claim equivalence, which is invalid. Duality lets you generate new *theorems* from old ones; it does not let you replace a formula with its dual inside a proof. Keeping the levels separate — theorems of the theory vs. equivalences between formulas — is essential for correct algebraic reasoning."
```

## Explainer

You already know from propositional semantics that propositional logic assigns truth values — true or false — to formulas built from connectives. Boolean algebra takes the same idea and lifts it to an algebraic setting: instead of truth tables, you work with **equational laws** that hold in any Boolean algebra, not just the two-element one. A **Boolean algebra** is a set B with two binary operations (∧ and ∨), a unary operation (¬), and two constants (0 and 1) satisfying a specific list of axioms: commutativity and associativity of both operations, two distributivity laws (each operation distributes over the other), identity laws (a ∧ 1 = a and a ∨ 0 = a), and complementation laws (a ∧ ¬a = 0 and a ∨ ¬a = 1). The two-element set {0, 1} with the usual AND, OR, and NOT is a Boolean algebra — the one propositional logic lives in — but it is not the only one.

The connection to propositional semantics is precise: propositional formulas, identified up to logical equivalence, form a Boolean algebra. The operations correspond directly (AND = ∧, OR = ∨, NOT = ¬), and tautologies correspond to the top element 1 while contradictions correspond to 0. This means every equational identity provable in Boolean algebra is a propositional tautology, and vice versa. The algebraic viewpoint lets you prove equivalences like ¬(a ∧ b) = ¬a ∨ ¬b (**De Morgan's first law**) and ¬(a ∨ b) = ¬a ∧ ¬b (**De Morgan's second law**) by algebraic manipulation from the axioms, without constructing a truth table. Once you have the axioms, the laws follow by pure symbol manipulation.

The **duality principle** is the most elegant feature of Boolean algebra. Every Boolean algebra axiom comes in a dual pair: swap ∧ with ∨ and swap 0 with 1, and you get another axiom. This means that if you prove a theorem from the axioms, its dual — obtained by making the same swaps throughout — is also a theorem. De Morgan's two laws are dual to each other; the identity laws for ∧ and ∨ are dual; the distributivity of ∧ over ∨ and of ∨ over ∧ are dual. Duality is a *metatheorem*: it says you get two theorems for the price of one, because the axiom set is self-dual. It does not say a formula and its dual are logically equivalent — they are generally not. The distinction is between a theorem about the *theory* and a claim about specific *formulas* inside the theory.

Beyond {0, 1}, Boolean algebras arise naturally as power-set algebras: the collection of all subsets of a set S, with ∩ for ∧, ∪ for ∨, complement for ¬, ∅ for 0, and S for 1. This is the simplest non-trivial family of Boolean algebras and is why Boolean algebra is relevant to set theory, circuit design, and database query optimization. Deeper results in the theory — Stone's representation theorem — say that every Boolean algebra is isomorphic to a field of sets, making the power-set example canonical rather than incidental.
