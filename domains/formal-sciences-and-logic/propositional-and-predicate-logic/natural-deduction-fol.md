---
id: natural-deduction-fol
title: Natural Deduction for First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: natural-deduction-propositional
  type: hard
- id: first-order-logic-syntax
  type: hard
builds-toward:
- fol-soundness-completeness
tags:
- natural-deduction
- quantifier-rules
- universal
- existential
- FOL-proof
stage: formal-systems
status: draft
---

# Natural Deduction for First-Order Logic

## Core Idea
Natural deduction for FOL extends propositional natural deduction with four quantifier rules. Universal introduction (∀I) derives ∀x φ(x) from φ(a) where a is an arbitrary fresh constant not mentioned elsewhere. Universal elimination (∀E) instantiates ∀x φ(x) to φ(t) for any term t. Existential introduction (∃I) derives ∃x φ(x) from φ(t). Existential elimination (∃E) discharges an assumption φ(a) when proving a conclusion that does not mention the fresh constant a. The freshness conditions on ∀I and ∃E are critical: they formalize the logical principle that reasoning about 'an arbitrary object' must not smuggle in extra assumptions.

## How It's Best Learned
Prove simple theorems like ∀x P(x) → ∀x (P(x) ∨ Q(x)) in Fitch notation before attempting ∃-elimination. Pay close attention to which constants appear in the context when applying freshness conditions.

## Common Misconceptions
- The fresh constant in ∀I and ∃E is a proof artifact — it does not exist in the theorem statement.
- ∀E does not require a fresh constant; only ∀I and ∃E have freshness restrictions.
