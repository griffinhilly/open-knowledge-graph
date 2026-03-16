---
id: predicate-logic-semantics
title: Predicate Logic for Linguistic Semantics
domain: language-and-communication
course: linguistics
prerequisites:
- id: compositional-semantics
  type: hard
builds-toward:
- model-theoretic-semantics
- formal-pragmatics-computation
tags:
- semantics
- formal-logic
- logical-form
- quantification
stage: formal-systems
status: draft
---

# Predicate Logic for Linguistic Semantics

## Core Idea
Predicate logic provides formal notation for linguistic meaning. Predicates represent properties and relations; quantifiers bind variables. Natural language expressions are translated into logical forms: "Every dog barks" becomes ∀x(dog(x) → barks(x)). Logical form captures entailments and scope ambiguities that English surface structure leaves implicit.

## How It's Best Learned
Translate English sentences into predicate logic, focusing on quantifier scope. Compare logical forms for ambiguous sentences.

## Common Misconceptions
- Assuming logical form directly matches surface word order. - Confusing scope ambiguity with grammatical ambiguity; both manifest in natural language. - Thinking existential and universal quantifiers are interchangeable; their scope dramatically affects truth conditions.

## Explainer

Compositional semantics gave you the principle that the meaning of a sentence is built from the meanings of its parts and the rules that combine them. Predicate logic provides a formal language in which to write those meanings explicitly, with precise enough notation that entailments and ambiguities can be computed rather than intuited. The key insight is that natural language sentences have a **logical form** — a structured semantic representation — that may differ considerably from their surface word order.

The basic vocabulary of predicate logic for semantics is small. A **predicate** names a property or relation: *barks(x)* says that x has the property of barking; *loves(x, y)* says that x stands in the loving-relation to y. Constants (*a*, *b*) name specific individuals; variables (*x*, *y*, *z*) are placeholders that quantifiers bind. **Quantifiers** specify how many individuals satisfy a predicate. The **universal quantifier** ∀x reads "for every x"; the **existential quantifier** ∃x reads "there exists at least one x such that." "Every dog barks" becomes ∀x(dog(x) → barks(x)) — for every x, if x is a dog, then x barks. "Some dog barks" becomes ∃x(dog(x) ∧ barks(x)) — there exists an x such that x is a dog and x barks. Notice the connectives differ: the universal uses the conditional (→), the existential uses conjunction (∧). Using ∀x(dog(x) ∧ barks(x)) would claim that everything in the domain is a dog that barks — a much stronger claim.

**Scope ambiguity** is one of the most powerful things predicate logic reveals. "Every student read a book" has two logical forms. Reading 1: ∀x(student(x) → ∃y(book(y) ∧ read(x,y))) — for every student, there is (possibly a different) book they read. Reading 2: ∃y(book(y) ∧ ∀x(student(x) → read(x,y))) — there is one particular book that every student read. The English sentence is genuinely ambiguous between these readings; the logical form makes the ambiguity precise by specifying which quantifier takes wider scope. This is a real contribution of formal semantics: surface syntax often underdetermines meaning in ways that only become visible through formal representation.

Building from your prerequisite in compositional semantics, you can see predicate logic as the target representation that compositionality aims at. Lexical items denote predicates and constants; syntactic combination rules map to logical conjunction, function application, or λ-abstraction. The logical form of a sentence is what the compositional computation delivers, and it is what licenses **entailments** — truth-preserving inferences. "Every dog barks" entails "If Fido is a dog, Fido barks." Predicate logic makes this inference formal: from ∀x(dog(x) → barks(x)) and dog(fido), the conclusion barks(fido) follows by universal instantiation. The connection between formal logic and natural language meaning is not merely analogical — it is the foundation of model-theoretic semantics, which assigns truth conditions to logical forms relative to models of the world.
