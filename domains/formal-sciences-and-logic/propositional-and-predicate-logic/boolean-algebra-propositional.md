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
