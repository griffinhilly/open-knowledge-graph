---
id: quantifier-instantiation-rules
title: Quantifier Instantiation Rules in First-Order Proof Systems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: natural-deduction-fol
  type: hard
builds-toward:
- proof-strategies-natural-deduction
tags:
- first-order-logic
- natural-deduction
- quantifiers
- proof-rules
stage: formal-systems
status: draft
---

# Quantifier Instantiation Rules in First-Order Proof Systems

## Core Idea
Quantifier instantiation rules are the inference rules for introducing and eliminating quantifiers in first-order logic proof systems. Universal instantiation (UI) allows deriving φ[t/x] from ∀x φ (instantiate the universal quantifier with a term t). Existential generalization (EG) allows deriving ∃x φ from φ[t/x] (generalize a specific instance to an existential claim). These rules connect the syntactic manipulation of quantifiers to their semantic meaning and are essential for constructing proofs in first-order logic.

## How It's Best Learned
Use natural deduction proofs as examples. Distinguish between free and bound variables carefully. Understand that UI can instantiate with any term (constant or complex), while EG introduces a witness. Work through proofs that use these rules, paying attention to variable capture issues.

## Common Misconceptions
- Applying UI with a variable that is already bound in the context (causes variable capture).
- Thinking that ∃x φ can be derived from φ alone (need a specific instantiation).
- Confusing the direction of the rules (UI removes the universal quantifier, EG adds an existential quantifier).
