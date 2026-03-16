---
id: derivation-vs-generation
title: Derivation Versus Generation in Formal Grammar
domain: language-and-communication
course: linguistics
prerequisites:
- id: constituent-trees-and-notation
  type: hard
- id: phrase-structure-rules
  type: soft
builds-toward:
- constraint-based-phonology-formal
tags:
- formalism
- grammar
- computation
stage: formal-systems
status: draft
---

# Derivation Versus Generation in Formal Grammar

## Core Idea
Generative approaches show how rules progressively build structures from base elements (derivation). Constraint-based approaches specify well-formedness conditions that structures must satisfy (generation). Both can model the same phenomena but differ in how they organize formal knowledge.

## Explainer

From your work with **constituent trees** and **phrase structure rules**, you know that a grammar can be written as a set of rules like S → NP VP, NP → Det N, and so on. These rules work by expansion: start with the symbol S, pick a rule that rewrites it, apply more rules to the resulting symbols, and continue until you have a string of words. The sequence of steps — each rule application transforming one symbolic expression into another — is a **derivation**. The final tree records the history of those steps. Derivational thinking asks: what is the *procedure* that built this structure?

**Constraint-based** frameworks invert the question. Instead of asking how a structure is built step by step, they ask: what conditions must any well-formed structure satisfy? A constraint-based grammar specifies a set of constraints — requirements about word order, case, agreement, argument structure — and a structure is grammatical if and only if it satisfies all of them simultaneously. There is no ordered sequence of rule applications; all constraints evaluate the candidate structure at once. Lexical-Functional Grammar (LFG), Head-Driven Phrase Structure Grammar (HPSG), and Optimality Theory (OT) all work in this mode.

The conceptual difference matters because it changes what "explanation" looks like. In a derivational account, explaining why a structure is ill-formed means showing that no valid derivation produces it — some rule was violated or failed to apply. In a constraint-based account, an ill-formed structure violates one or more constraints, and explaining it means identifying which constraints are at stake. In practice, both frameworks can capture the same empirical facts; the debate is partly about which organization better reflects the mental grammar humans actually use and which scales more gracefully to complex phenomena like long-distance dependencies, ellipsis, or cross-linguistic variation.

The distinction also maps onto a broader division in formal systems: **procedural** versus **declarative** representations. A derivational grammar is procedural — it describes a process. A constraint-based grammar is declarative — it describes a state of affairs that must hold. This same split appears in programming languages (imperative vs. declarative), logic (proof-theoretic vs. model-theoretic), and machine learning (generative models vs. discriminative models). Recognizing this isomorphism helps you transfer intuitions across fields: whenever you see a system that generates outputs via sequential rule application versus one that filters candidates against constraints, you are encountering the derivation/constraint distinction in another domain.
