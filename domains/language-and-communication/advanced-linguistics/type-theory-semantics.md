---
id: type-theory-semantics
title: Type Theory in Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: lambda-calculus-for-linguistics
  type: hard
- id: montague-semantics
  type: hard
builds-toward:
- de-re-de-dicto-distinction
tags:
- type-theory
- semantics
- formal
stage: advanced
status: draft
---

# Type Theory in Semantics

## Core Idea
Type theory assigns semantic types to linguistic expressions: individuals (type e), truth values (type t), and functions of various arities. Every word and phrase receives a type, and semantic composition respects type compatibility—functions apply only to arguments of the correct type. This system prevents semantic anomalies and explains category-level restrictions (e.g., why adjectives cannot be arguments of transitive verbs).

## How It's Best Learned
Assign types to words in a simple sentence and verify that composition respects type constraints. Explore type mismatches and how they account for semantic anomalies or coercion effects.

## Common Misconceptions
- Type theory does not prevent all anomalous expressions; pragmatic coercion can override type-theoretic restrictions.
- The type system is not arbitrary; types reflect interpretability at the phonological and semantic interfaces.

## Explainer

From lambda calculus and Montague semantics, you're already familiar with the idea that meanings are functions — that a verb phrase like "runs" denotes a function from individuals to truth values, and that semantic composition is function application. **Type theory** is the system that makes this function-based semantics disciplined: it assigns a formal **type** to every linguistic expression so that composition only proceeds when the types match up correctly, just as in a well-typed programming language where you can't pass a string to a function expecting an integer.

The two **basic types** are *e* (the type of individuals, or entities) and *t* (the type of truth values — propositions that are true or false). Everything else is built from these by function types. The notation ⟨α, β⟩ means "a function from things of type α to things of type β." So a common noun like "cat" has type ⟨e, t⟩ — it takes an individual and returns a truth value (true if that individual is a cat, false otherwise). A transitive verb like "likes" takes two individuals and returns a truth value, but since functions in this system are **curried** (they take one argument at a time), its type is ⟨e, ⟨e, t⟩⟩ — it takes an individual (the object) and returns a function of type ⟨e, t⟩ that then takes the subject and returns a truth value.

**Semantic composition** as type-driven function application works as follows. To combine "likes" ⟨e, ⟨e, t⟩⟩ with "Mary" (type *e*), you apply the function to the argument, yielding something of type ⟨e, t⟩ — the property of being someone who likes Mary. To then combine with "John" (type *e*), you apply again, yielding something of type *t* — a truth value. The full sentence "John likes Mary" successfully composes because the types are compatible at every step. The type system acts as a grammaticality filter on semantic composition: if you try to apply a function to an argument of the wrong type, the derivation is blocked. This is why "The table likes Mary" is semantically anomalous in a specific way — "the table" has type *e* just fine, but the problem arises elsewhere, or the anomaly is semantic rather than type-theoretic, which is itself informative.

**Generalized quantifiers** reveal the real explanatory power. "Every student" and "some student" cannot have type *e* — there is no individual they denote. Instead, they have type ⟨⟨e, t⟩, t⟩: they take a predicate (type ⟨e, t⟩) and return a truth value. "Every student runs" is computed by applying the generalized quantifier "every student" to the predicate "runs." This **type-lifting** of quantifiers from the seemingly simple to the functionally complex is one of Montague semantics' core contributions, and type theory is the tool that makes the lifting explicit and compositionally tractable. When you encounter apparent **type mismatches** in natural language — "The ham sandwich wants the check" (restaurant jargon where a food item refers to a person) — the interesting question is whether the anomaly triggers **coercion** (a pragmatic repair that reinterprets the type) or simply fails. Type theory thus provides not just a description of well-formed semantic composition but a precise diagnostic for where and how composition can go wrong.
