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
status: validated
---

# Models and Interpretations in First-Order Logic

## Core Idea
In first-order logic, a model (or interpretation) is a structure consisting of a non-empty domain and an assignment of denotations to each constant symbol, function symbol, and predicate symbol in the language. Models make precise the intuitive notion that a formula can be true or false depending on what world we are describing.

## How It's Best Learned
Start with simple structures like the natural numbers with addition, or small finite domains with basic relations. Verify that the same formula can be true in one model and false in another.

## Common Misconceptions
- Thinking a model must be 'the' intended model rather than one of many possible interpretations.
- Confusing the domain (objects) with the interpretation function (what predicates mean).

## Questions

```yaml
- question: "The sentence ∃x ∀y (x ≤ y) is evaluated in two models: M1 has domain ℕ with standard ≤, and M2 has domain ℤ with standard ≤. What is true?"
  type: multiple-choice
  options:
    - "The sentence is true in both models — 0 is the smallest element in both ℕ and ℤ"
    - "The sentence is false in both models — no integer is smaller than all others"
    - "The sentence is true in M1 but false in M2 — ℕ has a minimum (0), but ℤ has no smallest integer"
    - "The sentence is false in M1 but true in M2 — integers allow for a universal lower bound that natural numbers don't"
  answer: 2
  explanation: "In M1 (domain ℕ), the sentence is true: the witness is 0, since 0 ≤ y for every natural number y. In M2 (domain ℤ), the sentence is false: for any integer x, x − 1 is also an integer with x − 1 < x, so no element satisfies ∀y (x ≤ y). This example demonstrates the key insight: the same sentence, with the same symbol ≤ interpreted identically (as the standard ordering), can have opposite truth values depending solely on the domain of quantification."

- question: "You want to construct a model in which the sentence ∀x P(x) is false. Which approach is guaranteed to work?"
  type: multiple-choice
  options:
    - "Choose a domain containing infinitely many objects — ∀x is harder to satisfy over infinite domains"
    - "Interpret P as an empty relation — then no object satisfies P, making ∀x P(x) false"
    - "Use the empty domain, so there are no objects to test the universal claim against"
    - "Choose any domain where the interpretation of P has at least one object not in its extension"
  answer: 3
  explanation: "∀x P(x) is false if and only if at least one object in the domain fails to satisfy P. Option D correctly identifies this: any domain where some object d has P(d) = false makes the universal false. Option B works too (no objects satisfy P), but option D is the minimal sufficient condition and more revealing. Option C is wrong — the standard semantics of first-order logic requires non-empty domains, and in an empty domain ∀x P(x) would vacuously be true. Option A is a misconception — domain size doesn't directly determine truth of a universal."

- question: "A formula in first-order logic has a definite truth value that does not depend on which model is used to interpret it."
  type: true-false
  answer: false
  explanation: "This is the central misconception the model-theoretic framework is designed to correct. Truth in first-order logic is always relative to a model: the same formula can be true in one model and false in another. Only logical validities (formulas true in every model) and contradictions (false in every model) have model-independent truth values. Most interesting formulas are contingent — true in some models, false in others. This is why formal semantics requires explicitly specifying a model before asking whether a sentence is true."

- question: "A valid model in standard first-order logic must have a non-empty domain — interpretations over the empty set are not permitted."
  type: true-false
  answer: true
  explanation: "Standard first-order logic requires the domain to be non-empty (at least one object must exist). This is a foundational stipulation, not an arbitrary convention: many inference rules (like existential instantiation and universal instantiation) break down over empty domains. The non-emptiness requirement also ensures that ∃x (x = x) is logically valid — a sentence saying 'something exists' is true in every valid model. Some non-classical systems (free logic) relax this constraint, but classical first-order logic assumes non-empty domains throughout."

- question: "What are the two distinct components of a model in first-order logic, and how can varying each independently change the truth of a sentence?"
  type: short-answer
  answer: "A model has two components: (1) a domain — the set of objects that exist in the model, and (2) an interpretation function — which assigns specific objects, functions, or relations to each constant, function symbol, and predicate symbol in the language. Varying the domain while keeping interpretation fixed can change truth: 'there is a smallest element (∃x ∀y x ≤ y)' is true in ℕ but false in ℤ with the same ≤ interpretation. Varying the interpretation while keeping the domain fixed also changes truth: over domain ℕ, interpreting binary predicate R as '<' vs. 'divides' gives a different model in which different sentences hold."
  explanation: "The two-component structure is essential because it separates existence questions (what objects are there?) from meaning questions (what do the symbols refer to?). A sentence can fail to be true either because the domain lacks the needed objects (existential statements) or because the predicates don't have the right extension given the domain. This distinction underlies model theory, the study of which theories have which kinds of models — and it is the foundation for soundness and completeness results in logic."
```

## Explainer

You have studied how first-order logic sentences are built from symbols — predicates, constants, variables, quantifiers, and connectives — according to rigorous syntactic rules. But a formula by itself carries no truth value. The sentence ∀x P(x) is neither true nor false in isolation: it depends entirely on what "P" means and what objects "x" ranges over. A **model** (also called an **interpretation** or **structure**) is the mathematical object that supplies these meanings, making semantic evaluation precise.

A model M for a first-order language L consists of two components. First, a non-empty set called the **domain** (or universe) — the set of objects under discussion. Second, an **interpretation function** that assigns: a specific element of the domain to each constant symbol, a function on the domain to each function symbol (respecting its arity), and a relation on the domain to each predicate symbol. For example, a model for the language of arithmetic might have domain ℕ, with "0" interpreted as zero, "S" as the successor function, and "<" as the standard less-than ordering. Another model might have domain ℤ with the same symbols interpreted differently — and the same sentence can be true in one model and false in the other.

This relativity of truth to models is the defining feature of semantics. The sentence ∃x ∀y (x ≤ y) — "there is a smallest element" — is true in ℕ (0 is the witness) and false in ℤ (no integer is smallest). Neither model is more "correct" than the other; they are simply different structures. The formula is contingent: true in some models, false in others. A formula that is true in *every* model is a **validity**; one true in *no* model is a **contradiction**. Understanding this spectrum is the core of first-order semantics.

The distinction between domain and interpretation function is subtle but essential. The domain supplies the raw material — the objects that exist. The interpretation function determines what the predicates and functions *mean* on those objects. You can hold the domain fixed (say, ℕ) and vary the interpretation: interpreting the binary predicate "R" as "less than" gives one model; interpreting it as "divides" gives another, with different sentences true in each. Conversely, you can hold the interpretation fixed (predicates mean the same thing) and vary the domain. These two dimensions of variation — what exists and what the symbols mean — together constitute what it means to interpret a formal language, and mastering this two-part structure is the foundation for everything else in model theory.
