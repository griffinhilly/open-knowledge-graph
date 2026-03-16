---
id: models-and-interpretation-basic
title: Models and Interpretations in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: first-order-semantics
  type: hard
builds-toward:
- domain-and-structure-fol
tags:
- first-order-logic
- models
- semantics
stage: formal-systems
status: draft
---

# Models and Interpretations in First-Order Logic

## Core Idea
In first-order logic, a model (or interpretation) is a structure consisting of a non-empty domain and an assignment of denotations to each constant symbol, function symbol, and predicate symbol in the language. Models make precise the intuitive notion that a formula can be true or false depending on what world we are describing.

## How It's Best Learned
Start with simple structures like the natural numbers with addition, or small finite domains with basic relations. Verify that the same formula can be true in one model and false in another.

## Common Misconceptions
- Thinking a model must be 'the' intended model rather than one of many possible interpretations.
- Confusing the domain (objects) with the interpretation function (what predicates mean).

## Explainer

You have studied how first-order logic sentences are built from symbols — predicates, constants, variables, quantifiers, and connectives — according to rigorous syntactic rules. But a formula by itself carries no truth value. The sentence ∀x P(x) is neither true nor false in isolation: it depends entirely on what "P" means and what objects "x" ranges over. A **model** (also called an **interpretation** or **structure**) is the mathematical object that supplies these meanings, making semantic evaluation precise.

A model M for a first-order language L consists of two components. First, a non-empty set called the **domain** (or universe) — the set of objects under discussion. Second, an **interpretation function** that assigns: a specific element of the domain to each constant symbol, a function on the domain to each function symbol (respecting its arity), and a relation on the domain to each predicate symbol. For example, a model for the language of arithmetic might have domain ℕ, with "0" interpreted as zero, "S" as the successor function, and "<" as the standard less-than ordering. Another model might have domain ℤ with the same symbols interpreted differently — and the same sentence can be true in one model and false in the other.

This relativity of truth to models is the defining feature of semantics. The sentence ∃x ∀y (x ≤ y) — "there is a smallest element" — is true in ℕ (0 is the witness) and false in ℤ (no integer is smallest). Neither model is more "correct" than the other; they are simply different structures. The formula is contingent: true in some models, false in others. A formula that is true in *every* model is a **validity**; one true in *no* model is a **contradiction**. Understanding this spectrum is the core of first-order semantics.

The distinction between domain and interpretation function is subtle but essential. The domain supplies the raw material — the objects that exist. The interpretation function determines what the predicates and functions *mean* on those objects. You can hold the domain fixed (say, ℕ) and vary the interpretation: interpreting the binary predicate "R" as "less than" gives one model; interpreting it as "divides" gives another, with different sentences true in each. Conversely, you can hold the interpretation fixed (predicates mean the same thing) and vary the domain. These two dimensions of variation — what exists and what the symbols mean — together constitute what it means to interpret a formal language, and mastering this two-part structure is the foundation for everything else in model theory.
