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
stage: expert
status: validated
---

# Type Theory in Semantics

## Core Idea
Type theory assigns semantic types to linguistic expressions: individuals (type e), truth values (type t), and functions of various arities. Every word and phrase receives a type, and semantic composition respects type compatibility—functions apply only to arguments of the correct type. This system prevents semantic anomalies and explains category-level restrictions (e.g., why adjectives cannot be arguments of transitive verbs).

## How It's Best Learned
Assign types to words in a simple sentence and verify that composition respects type constraints. Explore type mismatches and how they account for semantic anomalies or coercion effects.

## Common Misconceptions
- Type theory does not prevent all anomalous expressions; pragmatic coercion can override type-theoretic restrictions.
- The type system is not arbitrary; types reflect interpretability at the phonological and semantic interfaces.

## Questions

```yaml
- question: "What is the semantic type of the noun phrase 'every student' in formal semantics?"
  type: multiple-choice
  options:
    - "e — it denotes the individual that is every student"
    - "⟨e, t⟩ — it denotes a predicate that applies to individuals"
    - "⟨⟨e, t⟩, t⟩ — it takes a predicate and returns a truth value"
    - "t — it directly expresses a truth value"
  answer: 2
  explanation: "'Every student' is a generalized quantifier, not an individual. There is no single entity it names, so type e is impossible. Instead, it combines with a predicate like 'passed' (type ⟨e, t⟩) and returns a truth value — true if every student is in the extension of 'passed.' This gives it type ⟨⟨e, t⟩, t⟩. The common misconception is treating quantifier phrases as referring expressions (type e) by analogy with names like 'John.' The type-lifting from apparent noun-phrase simplicity to quantifier complexity is one of Montague semantics' central contributions."

- question: "The transitive verb 'admires' has type ⟨e, ⟨e, t⟩⟩. When it combines with its object 'Bach' (type e), what type does the resulting expression have?"
  type: multiple-choice
  options:
    - "t — the combination produces a complete sentence"
    - "e — Bach remains an individual in the resulting expression"
    - "⟨e, t⟩ — the result is a predicate waiting for a subject"
    - "⟨⟨e, t⟩, t⟩ — the result must be a generalized quantifier"
  answer: 2
  explanation: "Semantic composition here is function application: applying 'admires' (type ⟨e, ⟨e, t⟩⟩) to 'Bach' (type e) consumes the first argument and returns ⟨e, t⟩ — a predicate meaning 'is someone who admires Bach.' This predicate then waits for the subject (e.g., 'John', type e) to yield a full truth value (type t). This illustrates currying: functions take one argument at a time, and the intermediate type ⟨e, t⟩ is not yet a complete sentence but a well-formed semantic object awaiting further composition."

- question: "According to type theory, the expression 'The ham sandwich wants the check' is semantically impossible to compose because the types are incompatible."
  type: true-false
  answer: false
  explanation: "'The ham sandwich' has type e (it denotes an individual, at least syntactically), and 'wants' has a type that can take type-e arguments, so the types actually do compose. The anomaly is not a type-level failure — it is a pragmatic one, resolved through coercion: in restaurant contexts, 'the ham sandwich' is reinterpreted as referring to the person who ordered it. Type theory identifies where and why composition can go wrong, but pragmatic coercion can override or repair apparent mismatches without blocking derivation entirely."

- question: "In a well-typed semantic derivation, a complete declarative sentence like 'John runs' denotes a value of type t."
  type: true-false
  answer: true
  explanation: "'John' has type e (an individual). 'Runs' has type ⟨e, t⟩ (a function from individuals to truth values). Applying 'runs' to 'John' yields type t — a truth value representing whether it is true that John runs. This is the foundational compositionality claim: sentences denote truth conditions, and the type system ensures that grammatical sentences reduce to type t when fully composed. Non-sentential expressions like 'John' or 'runs' have sub-propositional types that only reach t through complete composition."

- question: "Why can't noun phrases like 'every student' or 'some professor' have semantic type e, and what type must they have instead?"
  type: short-answer
  answer: "Type e is reserved for expressions that denote specific individuals — names like 'John' or 'Mary.' Quantifier phrases like 'every student' do not pick out a single individual; they express a relationship between two sets (e.g., the set of students and the set of things that passed). They must have type ⟨⟨e, t⟩, t⟩: they take a predicate (type ⟨e, t⟩) and return a truth value indicating whether the quantificational condition is satisfied."
  explanation: "This type-lifting is not merely formal machinery — it reflects a deep semantic difference between reference (picking out an entity) and quantification (asserting something about the relationship between sets). Treating 'every student' as type e would mean it names some particular individual, which fails for universal and existential quantifiers that range over sets. Montague's insight was that natural language noun phrases uniformly have the higher type ⟨⟨e, t⟩, t⟩, with proper names 'lifted' to that type for uniformity, rather than a heterogeneous system mixing e and quantifier types."
```

## Explainer

From lambda calculus and Montague semantics, you're already familiar with the idea that meanings are functions — that a verb phrase like "runs" denotes a function from individuals to truth values, and that semantic composition is function application. **Type theory** is the system that makes this function-based semantics disciplined: it assigns a formal **type** to every linguistic expression so that composition only proceeds when the types match up correctly, just as in a well-typed programming language where you can't pass a string to a function expecting an integer.

The two **basic types** are *e* (the type of individuals, or entities) and *t* (the type of truth values — propositions that are true or false). Everything else is built from these by function types. The notation ⟨α, β⟩ means "a function from things of type α to things of type β." So a common noun like "cat" has type ⟨e, t⟩ — it takes an individual and returns a truth value (true if that individual is a cat, false otherwise). A transitive verb like "likes" takes two individuals and returns a truth value, but since functions in this system are **curried** (they take one argument at a time), its type is ⟨e, ⟨e, t⟩⟩ — it takes an individual (the object) and returns a function of type ⟨e, t⟩ that then takes the subject and returns a truth value.

**Semantic composition** as type-driven function application works as follows. To combine "likes" ⟨e, ⟨e, t⟩⟩ with "Mary" (type *e*), you apply the function to the argument, yielding something of type ⟨e, t⟩ — the property of being someone who likes Mary. To then combine with "John" (type *e*), you apply again, yielding something of type *t* — a truth value. The full sentence "John likes Mary" successfully composes because the types are compatible at every step. The type system acts as a grammaticality filter on semantic composition: if you try to apply a function to an argument of the wrong type, the derivation is blocked. This is why "The table likes Mary" is semantically anomalous in a specific way — "the table" has type *e* just fine, but the problem arises elsewhere, or the anomaly is semantic rather than type-theoretic, which is itself informative.

**Generalized quantifiers** reveal the real explanatory power. "Every student" and "some student" cannot have type *e* — there is no individual they denote. Instead, they have type ⟨⟨e, t⟩, t⟩: they take a predicate (type ⟨e, t⟩) and return a truth value. "Every student runs" is computed by applying the generalized quantifier "every student" to the predicate "runs." This **type-lifting** of quantifiers from the seemingly simple to the functionally complex is one of Montague semantics' core contributions, and type theory is the tool that makes the lifting explicit and compositionally tractable. When you encounter apparent **type mismatches** in natural language — "The ham sandwich wants the check" (restaurant jargon where a food item refers to a person) — the interesting question is whether the anomaly triggers **coercion** (a pragmatic repair that reinterprets the type) or simply fails. Type theory thus provides not just a description of well-formed semantic composition but a precise diagnostic for where and how composition can go wrong.
