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
- id: first-order-semantics
  type: soft
builds-toward:
- fol-soundness-completeness
tags:
- natural-deduction
- quantifier-rules
- universal
- existential
- FOL-proof
stage: formal-systems
status: validated
---
# Natural Deduction for First-Order Logic

## Core Idea
Natural deduction for FOL extends propositional natural deduction with four quantifier rules. Universal introduction (∀I) derives ∀x φ(x) from φ(a) where a is an arbitrary fresh constant not mentioned elsewhere. Universal elimination (∀E) instantiates ∀x φ(x) to φ(t) for any term t. Existential introduction (∃I) derives ∃x φ(x) from φ(t). Existential elimination (∃E) discharges an assumption φ(a) when proving a conclusion that does not mention the fresh constant a. The freshness conditions on ∀I and ∃E are critical: they formalize the logical principle that reasoning about 'an arbitrary object' must not smuggle in extra assumptions.

## How It's Best Learned
Prove simple theorems like ∀x P(x) → ∀x (P(x) ∨ Q(x)) in Fitch notation before attempting ∃-elimination. Pay close attention to which constants appear in the context when applying freshness conditions.

## Common Misconceptions
- The fresh constant in ∀I and ∃E is a proof artifact — it does not exist in the theorem statement.
- ∀E does not require a fresh constant; only ∀I and ∃E have freshness restrictions.

## Explainer

You already know natural deduction for propositional logic: every connective has an introduction rule (how to prove it) and an elimination rule (how to use it). FOL natural deduction extends this system by giving introduction and elimination rules for the two quantifiers ∀ and ∃. The rules look symmetric on the surface but have subtly different constraints that reflect a deep logical distinction: the difference between *an arbitrary object* and *a specific unknown object*.

**Universal elimination (∀E)** is the simple one: from ∀x φ(x), you can derive φ(t) for *any* term t you like. If everything has a property, then this specific thing has it. No freshness condition is needed — t can be anything, including terms that already appear in your proof. This is just instantiation. **Universal introduction (∀I)** is the inverse and is more constrained: to derive ∀x φ(x), you must have derived φ(a) where a is a **fresh constant** — one that doesn't appear in any undischarged assumption. The fresh constant represents a *generic* object: if you proved φ(a) without using any special property of a, then a stands for any object whatsoever, and you're entitled to universally generalize.

**Existential introduction (∃I)** is also unconstrained: from φ(t), derive ∃x φ(x). You have a witness, so something satisfies the property. **Existential elimination (∃E)** is the tricky rule. From ∃x φ(x) and a derivation of conclusion C from assumption φ(a) (where a is fresh), you may derive C. The idea: you don't know *which* object witnesses ∃x φ(x), so you name it a and reason from what you know about it (just that it satisfies φ). If you reach a conclusion C that doesn't mention a, then C holds regardless of which witness a actually is. The freshness condition on a is essential: if a appeared in your other assumptions or in C, your reasoning would smuggle in extra information about the witness, corrupting the inference.

A worked example cements the rules. Prove ∃x P(x) → ∃x (P(x) ∨ Q(x)). Assume ∃x P(x). Apply ∃E: assume P(a) for fresh a. By ∃I on P(a) ∨ Q(a) (derived via ∨I from P(a)), derive ∃x (P(x) ∨ Q(x)). This conclusion doesn't mention a, so ∃E discharges the assumption P(a) and gives ∃x (P(x) ∨ Q(x)) from ∃x P(x). The proof works because a serves as a stand-in for "whichever object witnesses the existential" — we don't need to know which one it is, only that it satisfies P. This four-rule extension of propositional natural deduction is complete for FOL: every valid first-order sentence has a natural deduction proof.

