---
id: semantic-types-and-composition
title: Semantic Types and Compositional Meaning
domain: language-and-communication
course: linguistics
prerequisites:
- id: typed-feature-structures
  type: soft
- id: compositional-semantics
  type: hard
builds-toward:
- formal-semantics-of-tense
- formal-semantics-of-modality
- scope-and-binding-formally
tags:
- semantics
- type-theory
- composition
stage: advanced
status: draft
---

# Semantic Types and Compositional Meaning

## Core Idea
In type theory, linguistic expressions are assigned types (e.g., t for truth values, e for individuals, ⟨e,t⟩ for properties). Meaning is computed by applying typed functions systematically, ensuring only well-typed combinations are possible.

## Questions

```yaml
- question: "A common noun like 'runs' denotes a property — a function that takes an individual and returns a truth value. What semantic type does 'runs' have?"
  type: multiple-choice
  options: ["t", "e", "⟨e,t⟩", "⟨t,t⟩"]
  answer: 2
  explanation: "⟨e,t⟩ is the type of a function from individuals (type e) to truth values (type t). 'Runs' takes an entity — say, Maria — and returns true or false depending on whether that entity runs. This is the canonical type for one-place predicates."

- question: "A quantifier phrase like 'every student' has the same semantic type as a simple predicate like 'runs', namely ⟨e,t⟩."
  type: true-false
  answer: false
  explanation: "Quantifiers are higher-order: they take a property (type ⟨e,t⟩) and return a truth value (type t), giving them type ⟨⟨e,t⟩,t⟩. 'Every student runs' composes by applying the quantifier to the predicate, not by applying a predicate to an entity. Treating quantifiers as type ⟨e,t⟩ would collapse the distinction between predicates and determiners."

- question: "What role does the type system play in compositional semantics — why does assigning types to expressions matter for computing sentence meanings?"
  type: short-answer
  answer: "Types constrain which expressions can combine: a function of type ⟨σ,τ⟩ can only apply to an argument of type σ, yielding a value of type τ. This prevents meaningless combinations and specifies exactly how meanings compose step by step, making the derivation of sentence meaning fully explicit and mechanically verifiable."
  explanation: "Without types, we could try to combine any two expressions, but many such combinations would be semantically ill-formed (e.g., applying a truth value to another truth value). Types make compositionality precise: each application step is licensed by a type-matching rule, so the system can compute complex meanings — including quantifier scope — in a principled way."
```

## Explainer

If you have studied compositional semantics, you already know the core principle: the meaning of a complex expression is built from the meanings of its parts plus the rules for combining them. Semantic type theory is the formal scaffolding that makes this precise. Every expression in the language is assigned a type, and types determine what can combine with what — just as type systems in programming languages prevent you from multiplying a string by a boolean.

The basic types are just two: **e** (entities — individuals in the domain of discourse, like people, places, or objects) and **t** (truth values — true or false). Everything else is a function type built from these. A one-place predicate like "runs" has type ⟨e,t⟩: give it an entity and you get a truth value. The sentence "Maria runs" composes by applying the ⟨e,t⟩ function to the entity Maria (type e), returning a truth value — which is exactly what a sentence denotes.

Quantifier phrases reveal why higher-order types are necessary. "Every student" does not denote an individual; it denotes a relation between sets. Formally, it has type ⟨⟨e,t⟩,t⟩ — a function that takes a property (type ⟨e,t⟩) and returns a truth value. "Every student runs" is parsed as applying the ⟨⟨e,t⟩,t⟩ quantifier to the ⟨e,t⟩ predicate. The type-matching rule licenses this combination and predicts the output type (t), confirming that the result is a truth-evaluable sentence. This is the key insight you would miss if you treated quantifiers as ordinary noun phrases.

Composition proceeds by function application: wherever you have a function of type ⟨σ,τ⟩ adjacent to an argument of type σ, apply the function to the argument and obtain something of type τ. The type system is what lets you track this mechanically across an arbitrarily complex sentence. If a combination fails type-checking — say, you try to apply a truth value to a predicate — that is a formal signal that the expressions do not compose in the intended way, which may indicate a scope ambiguity or a syntactic mismatch.

Building from compositional semantics, the type-theoretic framework extends naturally to tense, modality, and quantifier scope — topics you will encounter next. In each case, the strategy is the same: assign types carefully to new expression classes, specify the composition rules, and let the machinery derive sentence meanings bottom-up from lexical entries. The power of the approach lies in its generativity: a small set of types and rules can produce meanings for an unlimited range of sentences.
