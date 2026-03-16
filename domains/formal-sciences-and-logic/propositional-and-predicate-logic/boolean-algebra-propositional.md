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

## Explainer

You already know from propositional semantics that propositional logic assigns truth values — true or false — to formulas built from connectives. Boolean algebra takes the same idea and lifts it to an algebraic setting: instead of truth tables, you work with **equational laws** that hold in any Boolean algebra, not just the two-element one. A **Boolean algebra** is a set B with two binary operations (∧ and ∨), a unary operation (¬), and two constants (0 and 1) satisfying a specific list of axioms: commutativity and associativity of both operations, two distributivity laws (each operation distributes over the other), identity laws (a ∧ 1 = a and a ∨ 0 = a), and complementation laws (a ∧ ¬a = 0 and a ∨ ¬a = 1). The two-element set {0, 1} with the usual AND, OR, and NOT is a Boolean algebra — the one propositional logic lives in — but it is not the only one.

The connection to propositional semantics is precise: propositional formulas, identified up to logical equivalence, form a Boolean algebra. The operations correspond directly (AND = ∧, OR = ∨, NOT = ¬), and tautologies correspond to the top element 1 while contradictions correspond to 0. This means every equational identity provable in Boolean algebra is a propositional tautology, and vice versa. The algebraic viewpoint lets you prove equivalences like ¬(a ∧ b) = ¬a ∨ ¬b (**De Morgan's first law**) and ¬(a ∨ b) = ¬a ∧ ¬b (**De Morgan's second law**) by algebraic manipulation from the axioms, without constructing a truth table. Once you have the axioms, the laws follow by pure symbol manipulation.

The **duality principle** is the most elegant feature of Boolean algebra. Every Boolean algebra axiom comes in a dual pair: swap ∧ with ∨ and swap 0 with 1, and you get another axiom. This means that if you prove a theorem from the axioms, its dual — obtained by making the same swaps throughout — is also a theorem. De Morgan's two laws are dual to each other; the identity laws for ∧ and ∨ are dual; the distributivity of ∧ over ∨ and of ∨ over ∧ are dual. Duality is a *metatheorem*: it says you get two theorems for the price of one, because the axiom set is self-dual. It does not say a formula and its dual are logically equivalent — they are generally not. The distinction is between a theorem about the *theory* and a claim about specific *formulas* inside the theory.

Beyond {0, 1}, Boolean algebras arise naturally as power-set algebras: the collection of all subsets of a set S, with ∩ for ∧, ∪ for ∨, complement for ¬, ∅ for 0, and S for 1. This is the simplest non-trivial family of Boolean algebras and is why Boolean algebra is relevant to set theory, circuit design, and database query optimization. Deeper results in the theory — Stone's representation theorem — say that every Boolean algebra is isomorphic to a field of sets, making the power-set example canonical rather than incidental.
