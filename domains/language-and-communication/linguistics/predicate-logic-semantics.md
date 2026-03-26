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
status: validated
---

# Predicate Logic for Linguistic Semantics

## Core Idea
Predicate logic provides formal notation for linguistic meaning. Predicates represent properties and relations; quantifiers bind variables. Natural language expressions are translated into logical forms: "Every dog barks" becomes ∀x(dog(x) → barks(x)). Logical form captures entailments and scope ambiguities that English surface structure leaves implicit.

## How It's Best Learned
Translate English sentences into predicate logic, focusing on quantifier scope. Compare logical forms for ambiguous sentences.

## Common Misconceptions
- Assuming logical form directly matches surface word order. - Confusing scope ambiguity with grammatical ambiguity; both manifest in natural language. - Thinking existential and universal quantifiers are interchangeable; their scope dramatically affects truth conditions.

## Questions

```yaml
- question: "How is the sentence 'Every student passed the exam' correctly translated into predicate logic?"
  type: multiple-choice
  options:
    - "∀x(student(x) ∧ passed(x))"
    - "∀x(student(x) → passed(x))"
    - "∃x(student(x) → passed(x))"
    - "∃x(student(x) ∧ passed(x))"
  answer: 1
  explanation: "The universal quantifier uses the conditional (→): 'for every x, if x is a student, then x passed.' This restricts the claim to students without asserting anything about non-students. Option A (∀x(student(x) ∧ passed(x))) claims that everything in the domain is both a student and passed — far stronger than the original sentence. Option D correctly uses ∃ with ∧ but translates 'some student passed,' not 'every student passed.'"

- question: "A student translates 'Every dog barks' as ∀x(dog(x) ∧ barks(x)). What is wrong with this translation?"
  type: multiple-choice
  options:
    - "The universal quantifier should be replaced with an existential quantifier"
    - "The conjunction (∧) claims everything in the domain is a barking dog, not just dogs that bark"
    - "The predicate arguments are in the wrong order"
    - "Nothing is wrong — this is valid predicate logic notation for the sentence"
  answer: 1
  explanation: "∀x(dog(x) ∧ barks(x)) says: take any object x — it must be both a dog AND barking. If your domain includes cats, chairs, or people, the formula is immediately false because they are not dogs. The correct translation ∀x(dog(x) → barks(x)) restricts the claim: only if x is a dog does the barking requirement apply. The choice of connective (→ vs. ∧) with the universal quantifier is one of the most common and consequential errors in predicate logic translation."

- question: "The sentence 'Every student read a book' is genuinely ambiguous — it has two different logical forms that differ in which quantifier takes wider scope."
  type: true-false
  answer: true
  explanation: "Reading 1 (∀ wide scope): ∀x(student(x) → ∃y(book(y) ∧ read(x,y))) — each student read some (possibly different) book. Reading 2 (∃ wide scope): ∃y(book(y) ∧ ∀x(student(x) → read(x,y))) — there is one specific book that every student read. The English surface form is identical for both readings. Predicate logic makes the ambiguity precise by requiring an explicit choice of scope, which is exactly its contribution to linguistic semantics."

- question: "The logical form of a sentence in predicate logic typically directly mirrors the word order of the original English sentence."
  type: true-false
  answer: false
  explanation: "Natural language surface order and logical form routinely diverge. English often places quantifiers, negations, and modifiers in positions that do not directly correspond to their logical scope. For example, 'A book was read by every student' has the same two logical forms as 'Every student read a book' — the English word order changes but the underlying ambiguity is identical. Predicate logic reveals structure hidden beneath the surface, which is precisely why it is useful for semantics."

- question: "Why does the universal quantifier use a conditional (→) rather than conjunction (∧) in statements like 'Every dog barks,' and what goes wrong if you use ∧ instead?"
  type: short-answer
  answer: "The universal quantifier ranges over the entire domain, not just dogs. ∀x(dog(x) → barks(x)) correctly restricts the barking requirement: it only applies to objects that satisfy dog(x). Non-dogs satisfy the formula trivially (false → anything is true). Using ∧ instead gives ∀x(dog(x) ∧ barks(x)), which asserts that every object in the domain is simultaneously a dog and barks — including chairs, numbers, and people. This makes the formula almost certainly false in any realistic domain, far overstating the original sentence."
  explanation: "The conditional-vs-conjunction distinction is the heart of how universal quantification works in natural language. Linguists describe this as the universal quantifier introducing a restriction (dog) and a nuclear scope (barks): the restriction is always connected conditionally, not conjunctively. The existential quantifier works differently: ∃x(dog(x) ∧ barks(x)) correctly uses ∧ because you only need to find one x satisfying both conditions simultaneously."
```

## Explainer

Compositional semantics gave you the principle that the meaning of a sentence is built from the meanings of its parts and the rules that combine them. Predicate logic provides a formal language in which to write those meanings explicitly, with precise enough notation that entailments and ambiguities can be computed rather than intuited. The key insight is that natural language sentences have a **logical form** — a structured semantic representation — that may differ considerably from their surface word order.

The basic vocabulary of predicate logic for semantics is small. A **predicate** names a property or relation: *barks(x)* says that x has the property of barking; *loves(x, y)* says that x stands in the loving-relation to y. Constants (*a*, *b*) name specific individuals; variables (*x*, *y*, *z*) are placeholders that quantifiers bind. **Quantifiers** specify how many individuals satisfy a predicate. The **universal quantifier** ∀x reads "for every x"; the **existential quantifier** ∃x reads "there exists at least one x such that." "Every dog barks" becomes ∀x(dog(x) → barks(x)) — for every x, if x is a dog, then x barks. "Some dog barks" becomes ∃x(dog(x) ∧ barks(x)) — there exists an x such that x is a dog and x barks. Notice the connectives differ: the universal uses the conditional (→), the existential uses conjunction (∧). Using ∀x(dog(x) ∧ barks(x)) would claim that everything in the domain is a dog that barks — a much stronger claim.

**Scope ambiguity** is one of the most powerful things predicate logic reveals. "Every student read a book" has two logical forms. Reading 1: ∀x(student(x) → ∃y(book(y) ∧ read(x,y))) — for every student, there is (possibly a different) book they read. Reading 2: ∃y(book(y) ∧ ∀x(student(x) → read(x,y))) — there is one particular book that every student read. The English sentence is genuinely ambiguous between these readings; the logical form makes the ambiguity precise by specifying which quantifier takes wider scope. This is a real contribution of formal semantics: surface syntax often underdetermines meaning in ways that only become visible through formal representation.

Building from your prerequisite in compositional semantics, you can see predicate logic as the target representation that compositionality aims at. Lexical items denote predicates and constants; syntactic combination rules map to logical conjunction, function application, or λ-abstraction. The logical form of a sentence is what the compositional computation delivers, and it is what licenses **entailments** — truth-preserving inferences. "Every dog barks" entails "If Fido is a dog, Fido barks." Predicate logic makes this inference formal: from ∀x(dog(x) → barks(x)) and dog(fido), the conclusion barks(fido) follows by universal instantiation. The connection between formal logic and natural language meaning is not merely analogical — it is the foundation of model-theoretic semantics, which assigns truth conditions to logical forms relative to models of the world.
