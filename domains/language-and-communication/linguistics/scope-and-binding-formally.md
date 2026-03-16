---
id: scope-and-binding-formally
title: 'Quantifier Scope and Binding: Formal Treatment'
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
- id: quantifier-scope-and-binding
  type: soft
tags:
- semantics
- scope
- binding
stage: formal-systems
status: draft
---

# Quantifier Scope and Binding: Formal Treatment

## Core Idea
In formal semantics, quantifiers denote generalized quantifiers (functions from properties to truth values). Scope is determined by logical form; variable binding is formalized via lambda abstraction, which allows pronouns to be bound to quantified antecedents.

## Explainer

From your work on semantic types and composition, you know that sentences are built by functional application: expressions combine when their types match, and the output inherits the result type. From your study of quantifier scope and binding, you know that sentences with multiple quantifiers — like "Everyone loves someone" — are systematically ambiguous, and that how quantifiers interact depends on which takes scope over the other. Formal semantics gives you the tools to represent these interpretations precisely and derive them compositionally.

A **generalized quantifier** is a function from properties to truth values. "Every student" doesn't denote a particular student — it denotes a function that takes a property (like "passed the test") and returns true if every student has that property. In type notation, quantified noun phrases have type ⟨⟨e,t⟩, t⟩: they take a property (⟨e,t⟩) and return a truth value (t). This is a **higher-order** object — a function over functions, not a function over individuals. "Every student passed" is true if and only if the property "passed" holds of every individual in the student domain.

Scope becomes the critical question when two quantifiers interact. "Every professor assigned some paper" has two readings: (1) there is a single paper that every professor assigned (wide scope for "some paper"); (2) each professor may have assigned a different paper (narrow scope for "some paper"). **Logical form** (LF) is the level of syntactic representation at which scope is resolved. On reading (1), "some paper" takes scope over "every professor"; on reading (2), it falls inside the scope of "every professor." The truth conditions of the two interpretations are genuinely different — the sentence can be true on one reading and false on the other — and LF is the formal site where this difference is represented.

**Lambda abstraction** provides the formal mechanism for variable binding. When a pronoun like "he" is bound to a quantified antecedent in "every student thinks he will pass," the pronoun functions as a variable ranging over the values introduced by the quantifier. The formal representation uses lambda notation: the predicate containing the pronoun is abstracted over the variable, creating a property of type ⟨e,t⟩, which the quantifier then takes as its argument. "Every student [λx [x thinks x will pass]]" makes explicit that the "x" inside the clause is bound by "every student." Lambda abstraction is the bridge between surface sentences with pronouns and their underlying variable-binding structure — and it allows the same compositional machinery that handles ordinary predication to handle anaphora without requiring separate mechanisms.
