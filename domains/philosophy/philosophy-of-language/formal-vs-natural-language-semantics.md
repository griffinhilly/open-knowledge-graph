---
id: formal-vs-natural-language-semantics
title: Formal Language and Natural Language Semantics
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: truth-conditions-and-meaning
  type: hard
- id: compositionality-principle
  type: soft
- id: first-order-semantics
  type: hard
- id: model-theory-basics
  type: soft
builds-toward:
- semantic-underdetermination-context
tags:
- formal-logic
- natural-language
- semantics
stage: advanced
status: draft
---

# Formal Language and Natural Language Semantics

## Core Idea
Natural language differs from formal logic in crucial ways: it is ambiguous, context-dependent, imprecise, and contains many non-truth-functional expressions. Formal semantic methods apply to natural language, but require adapting logical tools to preserve both accuracy and applicability.

## Explainer

You already know how formal languages work from your study of first-order logic: a **formal language** has a fixed syntax, an explicit semantics defined over models, and no ambiguity — every well-formed formula has exactly one meaning relative to an interpretation. When you learned model theory, you saw how a model assigns objects to constants, extensions to predicates, and truth conditions to sentences in a fully determined, mechanical way. Natural language — the English, French, or Swahili you grew up speaking — operates very differently, and the gap between the two is where most of the philosophical action in semantics lives.

The most immediate difference is **ambiguity**. In first-order logic, "bank" simply does not appear — you would introduce a predicate BANK and specify what it applies to. In English, "She went to the bank" is genuinely ambiguous between a financial institution and a riverside, and listeners resolve the ambiguity using context, prior discourse, and world knowledge. Formal systems eliminate ambiguity by design; natural language lives with it and relies on pragmatic inference to recover the intended meaning. This means that a naïve translation of natural language into logic — treating each English sentence as having a single logical form — would misrepresent the phenomenon.

A second gap is **context-dependence**. You know that truth conditions specify what would make a sentence true or false. But many natural language sentences cannot be assigned truth conditions without knowing the context of utterance. "I am tired" is true in some contexts and false in others — the word "I" shifts referent with each speaker. "It's raining" needs a location. "That is tall" requires a comparison class — tall for a building, a person, or a blade of grass? Formal semantics handles this through **indexicals** (expressions whose reference is fixed by context) and **context parameters** (a context providing speaker, time, location, etc.) that supplement the model. The compositional machinery you learned — how complex meanings are built from parts — must be extended to take these parameters into account.

The deeper challenge is that natural language contains constructions that resist direct translation into first-order logic. Ordinary conditionals ("If it rains, the game is canceled") seem to work differently from material conditionals. Attitude reports ("Mary believes the president is corrupt") create contexts where substituting co-referring names can change truth value — a phenomenon that violates the substitutivity you expect from standard logic. Tense, aspect, modality, generics ("Tigers are striped") and questions all require extensions of the basic first-order toolkit. The project of **formal semantics for natural language** — pursued through tools like type theory, possible-worlds semantics, and dynamic logic — is precisely to find a systematic, compositional treatment of these phenomena that preserves the precision of formal methods while respecting the actual behavior of the language. The lesson is not that formal tools fail but that applying them to natural language is an ongoing, fine-grained empirical and theoretical enterprise, not a simple translation.

