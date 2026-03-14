---
id: counterexample-and-refutation
title: Counterexamples and Refutation
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: satisfaction-relation-fol
  type: hard
- id: ground-instances-and-instantiation
  type: soft
tags:
- first-order-logic
- proof-methods
- refutation
stage: formal-systems
status: draft
---

# Counterexamples and Refutation

## Core Idea
A counterexample to the claim that Γ ⊨ φ is an interpretation where all formulas in Γ are true but φ is false. Finding a counterexample is equivalent to finding a satisfying assignment for Γ ∧ ¬φ, making the connection between semantic consequence and satisfiability concrete and computationally relevant.
