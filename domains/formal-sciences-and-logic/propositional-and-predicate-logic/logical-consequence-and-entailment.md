---
id: logical-consequence-and-entailment
title: Logical Consequence and Entailment
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-equivalence-formulas
  type: hard
builds-toward:
- satisfiability-and-unsatisfiability
- deduction-theorem-propositional
- compactness-propositional-logic
tags:
- propositional-logic
- consequence
- inference
stage: formal-systems
status: draft
---

# Logical Consequence and Entailment

## Core Idea
A set of formulas Γ entails a formula φ (written Γ ⊨ φ) if every interpretation that makes all formulas in Γ true also makes φ true. This semantic notion of consequence is central to understanding what it means for one set of premises to logically justify a conclusion.

## How It's Best Learned
Distinguish between entailment (semantic, truth-based) and derivability (syntactic, proof-based). Work with small concrete examples showing when entailment holds and when counterexamples exist.

## Common Misconceptions
- Confusing entailment with the material conditional (→): A ⊨ B means every model of A is a model of B, not that A → B is true.
- Thinking that A ⊨ B means A and B must have similar structure.
