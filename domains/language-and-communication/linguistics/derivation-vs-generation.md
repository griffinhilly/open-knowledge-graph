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
- id: acquisition-of-formal-systems
  type: soft
- id: computational-pragmatics
  type: soft
builds-toward:
- constraint-based-phonology-formal
tags:
- formalism
- grammar
- computation
stage: advanced
status: validated
---
# Derivation Versus Generation in Formal Grammar

## Core Idea
Generative approaches show how rules progressively build structures from base elements (derivation). Constraint-based approaches specify well-formedness conditions that structures must satisfy (generation). Both can model the same phenomena but differ in how they organize formal knowledge.

## Questions

```yaml
- question: "A linguist using a derivational grammar (like early Transformational-Generative grammar) and a linguist using a constraint-based grammar (like HPSG) both analyze the same ungrammatical sentence. How does each explain why the sentence is ill-formed?"
  type: multiple-choice
  options:
    - "The derivational linguist identifies violated constraints; the constraint-based linguist traces the failed derivation step"
    - "The derivational linguist shows no valid derivation produces the structure; the constraint-based linguist identifies which constraints the structure fails to satisfy"
    - "Both approaches explain ill-formedness identically — derivation and constraint are interchangeable formal tools"
    - "Only derivational grammars can explain ill-formedness; constraint-based grammars only describe well-formed sentences"
  answer: 1
  explanation: "The key difference is in what 'explanation' means in each framework. Derivational explanation is procedural: a sentence is ill-formed because no valid sequence of rule applications can produce it — some step in the derivation fails or cannot apply. Constraint-based explanation is declarative: a sentence is ill-formed because it violates one or more well-formedness conditions that all grammatical structures must simultaneously satisfy. The same empirical fact (the sentence is bad) receives different theoretical explanations that reflect the framework's fundamental commitments about what grammar is — a procedure or a set of conditions."

- question: "Constraint-based frameworks like HPSG and LFG represent a fundamentally different conception of grammatical knowledge than derivational frameworks. Which of the following best captures the nature of that difference?"
  type: multiple-choice
  options:
    - "Constraint-based grammars are more powerful because they can describe sentences that derivational grammars cannot"
    - "Derivational grammars describe a process; constraint-based grammars describe a state — one is procedural, the other is declarative"
    - "Derivational grammars apply rules in parallel; constraint-based grammars apply them sequentially"
    - "Constraint-based grammars replace phrase structure rules entirely; derivational grammars retain them"
  answer: 1
  explanation: "The fundamental distinction is procedural versus declarative. A derivational grammar specifies a procedure: start with a symbol, apply rules in sequence to expand it, until a string of words is produced. The derivation is the grammar's knowledge representation. A constraint-based grammar specifies conditions: here is a set of requirements that any well-formed structure must simultaneously satisfy. There is no ordered procedure — constraints evaluate candidate structures in parallel. This same procedural/declarative split appears in programming (imperative vs. declarative languages), logic (proof-theoretic vs. model-theoretic), and elsewhere. The two approaches can often describe the same data, making the debate partly about which better represents human linguistic competence."

- question: "In a derivational grammar, the sequence of rule applications that builds a syntactic structure from an initial symbol down to a string of words is called a derivation."
  type: true-false
  answer: true
  explanation: "True. In derivational frameworks (such as early Transformational Grammar), grammar is represented as a set of rewrite rules: S → NP VP, NP → Det N, and so on. Beginning with the start symbol S, rules are applied in sequence to expand non-terminal symbols into further symbols or into words. The ordered sequence of these steps is the derivation, and the resulting tree records its history. This sequential, procedural character is the defining feature that distinguishes derivational from constraint-based frameworks."

- question: "Constraint-based grammars are empirically more powerful than derivational grammars — they can describe a strictly larger set of grammatical phenomena."
  type: true-false
  answer: false
  explanation: "False. The debate between derivational and constraint-based frameworks is not primarily about expressive power or empirical coverage — both types of formalism are capable of modeling the same linguistic phenomena. The differences lie in how knowledge is organized (procedural vs. declarative), how explanation is structured (failed derivation steps vs. violated constraints), and which architecture is claimed to better reflect actual mental grammar. Choosing a framework is a theoretical commitment about the nature of linguistic knowledge, not a claim that one framework can describe phenomena the other cannot. Particular formalisms may differ in computational properties, but the general dichotomy is not a power hierarchy."

- question: "How does the distinction between derivation and constraint-based grammar parallel the distinction between procedural and declarative representations in computer science? What does this isomorphism reveal?"
  type: short-answer
  answer: "A derivational grammar is procedural: it specifies a step-by-step process that produces grammatical structures from initial symbols. A constraint-based grammar is declarative: it specifies conditions that any well-formed structure must satisfy, without specifying how that structure is constructed. This mirrors the programming distinction between imperative languages (which specify operations to perform in sequence) and declarative languages like Prolog or SQL (which specify what must be true of the output). The isomorphism reveals that the derivation/constraint split is a general tension in formal systems — not unique to linguistics — between building-by-procedure and filtering-by-condition. Recognizing it lets intuitions transfer across domains."
  explanation: "The same split appears in logic (proof-theoretic vs. model-theoretic semantics), machine learning (generative vs. discriminative models), and database querying (procedural vs. set-based retrieval). In each case the procedural approach emphasizes how an output is constructed; the declarative approach emphasizes what conditions the output must satisfy. The grammar debate is a specific instance of this fundamental choice in formal knowledge representation."
```

## Explainer

From your work with **constituent trees** and **phrase structure rules**, you know that a grammar can be written as a set of rules like S → NP VP, NP → Det N, and so on. These rules work by expansion: start with the symbol S, pick a rule that rewrites it, apply more rules to the resulting symbols, and continue until you have a string of words. The sequence of steps — each rule application transforming one symbolic expression into another — is a **derivation**. The final tree records the history of those steps. Derivational thinking asks: what is the *procedure* that built this structure?

**Constraint-based** frameworks invert the question. Instead of asking how a structure is built step by step, they ask: what conditions must any well-formed structure satisfy? A constraint-based grammar specifies a set of constraints — requirements about word order, case, agreement, argument structure — and a structure is grammatical if and only if it satisfies all of them simultaneously. There is no ordered sequence of rule applications; all constraints evaluate the candidate structure at once. Lexical-Functional Grammar (LFG), Head-Driven Phrase Structure Grammar (HPSG), and Optimality Theory (OT) all work in this mode.

The conceptual difference matters because it changes what "explanation" looks like. In a derivational account, explaining why a structure is ill-formed means showing that no valid derivation produces it — some rule was violated or failed to apply. In a constraint-based account, an ill-formed structure violates one or more constraints, and explaining it means identifying which constraints are at stake. In practice, both frameworks can capture the same empirical facts; the debate is partly about which organization better reflects the mental grammar humans actually use and which scales more gracefully to complex phenomena like long-distance dependencies, ellipsis, or cross-linguistic variation.

The distinction also maps onto a broader division in formal systems: **procedural** versus **declarative** representations. A derivational grammar is procedural — it describes a process. A constraint-based grammar is declarative — it describes a state of affairs that must hold. This same split appears in programming languages (imperative vs. declarative), logic (proof-theoretic vs. model-theoretic), and machine learning (generative models vs. discriminative models). Recognizing this isomorphism helps you transfer intuitions across fields: whenever you see a system that generates outputs via sequential rule application versus one that filters candidates against constraints, you are encountering the derivation/constraint distinction in another domain.
