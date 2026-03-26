---
id: unification-mechanism
title: Unification and Feature Agreement
domain: language-and-communication
course: linguistics
prerequisites:
- id: typed-feature-structures
  type: hard
- id: agreement-comprehensive-overview
  type: soft
- id: derivation-vs-generation
  type: soft
- id: computational-pragmatics
  type: soft
- id: inflectional-morphology-formal
  type: soft
- id: internal-reconstruction
  type: soft
- id: word-order-typology
  type: soft
builds-toward:
- lexical-functional-grammar
- head-driven-phrase-structure-grammar
tags:
- formalism
- agreement
- computation
stage: advanced
status: validated
---
# Unification and Feature Agreement

## Core Idea
Unification is a formal operation that merges two feature structures by resolving shared features. It provides a mathematical account of agreement: two constituents can combine only if their features unify without contradiction.

## Questions

```yaml
- question: "A grammar specifies that to form a grammatical sentence, the subject and verb feature structures must unify. The subject is specified as [NUM: singular, PERS: 3rd] and the verb requires [NUM: plural, PERS: 3rd, TENSE: past]. What is the result?"
  type: multiple-choice
  options:
    - "Unification succeeds because person features match, and the NUM conflict is resolved in favor of the verb"
    - "Unification fails because the NUM values conflict, correctly predicting the sentence is ungrammatical"
    - "Unification partially succeeds, yielding a combined structure that marks the sentence as pragmatically unusual"
    - "Unification succeeds because the verb's specification is more complete and overrides the subject"
  answer: 1
  explanation: "Unification requires that ALL shared attributes be compatible. The NUM attribute has conflicting values (singular vs. plural) — this is a contradiction that cannot be resolved. Unification fails, and the grammar correctly predicts the sentence is ungrammatical. This is precisely the elegance of the mechanism: there is no special rule for number agreement, no procedure checking subject against verb — the general unification operation handles it automatically, and failure equals ungrammaticality."

- question: "What is the primary advantage of modeling agreement through unification rather than writing separate procedural rules for each agreement type (e.g., 'if subject is singular, make verb singular')?'"
  type: multiple-choice
  options:
    - "Unification is faster to compute and requires less memory than rule-based approaches"
    - "Unification applies only to syntactic features, so semantic interpretation can proceed independently"
    - "A single declarative unification constraint handles all agreement phenomena uniformly — the grammar specifies what must match, and unification applies the logic without special-casing each agreement type"
    - "Unification eliminates the need for feature structures by encoding agreement in word order"
  answer: 2
  explanation: "The power of unification is that it is both declarative (stating what must be true) and general (applicable to any combination of feature structures). Instead of writing separate rules for number agreement, gender agreement, case agreement, person agreement, etc. — each with their own procedural logic — you specify features once and let unification do the checking. Adding a new agreement dimension (say, animacy in a language that distinguishes animate/inanimate agreement) just means adding a new feature attribute; the unification mechanism itself does not change."

- question: "Unification can succeed even when two feature structures have conflicting values for a shared attribute, provided the conflict is on a minor or optional feature."
  type: true-false
  answer: false
  explanation: "Unification is all-or-nothing: it succeeds if and only if ALL shared attributes are compatible. There is no concept of 'minor' or 'optional' conflicts in the formal operation — any conflict on any shared attribute causes unification to fail. This strictness is what gives the mechanism its predictive power: grammaticality is a binary outcome (unification succeeds or fails), not a matter of degree. If a grammar needs to allow some flexibility, it must do so by leaving certain features underspecified (variables), not by tolerating conflicts."

- question: "An underspecified feature — one represented as a variable that has not yet been assigned a specific value — can unify with any specific value, allowing grammatical specifications to be completed through combination with other elements."
  type: true-false
  answer: true
  explanation: "Underspecification is the mechanism that allows unification to handle partial information. A feature structure representing an English verb that can appear with either singular or plural subjects might leave NUM underspecified. When this verb combines with a singular subject [NUM: singular], unification fills in the variable with 'singular,' yielding a fully specified combined structure. This is how agreement propagates through a sentence: underspecified elements receive values from elements they combine with, and conflicts emerge only when two structures try to assign different specific values to the same attribute."

- question: "How does unification provide a declarative account of grammaticality? Explain why a unification failure corresponds to an ungrammatical sentence."
  type: short-answer
  answer: "In a unification-based grammar, every grammatical combination is licensed by a successful unification of the feature structures of the combining elements. The grammar does not contain explicit lists of grammatical sentences or procedural rules that generate them — it contains feature constraints, and unification checks whether those constraints are mutually satisfiable. When a combination violates a constraint (e.g., subject and verb disagree in number), the feature structures conflict and unification fails. The grammar predicts the sentence is ungrammatical as a logical consequence of this failure, not because a rule explicitly bans it. Grammaticality is thus reduced to a question of constraint satisfaction."
  explanation: "The declarative/procedural distinction is central here. A procedural grammar says: 'follow these steps to generate a sentence.' A declarative grammar says: 'a sentence is grammatical if and only if these constraints are satisfied.' Unification implements the checking half of the declarative approach. The result is a grammar that is both formally explicit (every prediction follows from the feature specifications) and easy to extend (new phenomena add new features, not new procedures)."
```

## Explainer

You already know how to represent linguistic information as **typed feature structures** — attribute-value matrices where grammatical properties like number, person, case, and gender are encoded as attribute-value pairs. Unification is the operation that determines whether two such structures are compatible, and if so, what the combined structure looks like. Think of it as checking whether two puzzle pieces can join: if neither contradicts the other, they merge; if they conflict on any shared attribute, they fail to unify, and no grammatical combination is possible.

The formal definition is straightforward. Two feature structures unify if, for every attribute they share, their values for that attribute are compatible. Compatibility means either both values are identical, or one value is underspecified (a variable that can take any value) and the other provides a specific value that fills it in. The result of unification is a new feature structure containing all attributes from both inputs, with shared attributes resolved to their specific values. Consider a subject noun phrase specified as [NUM: plural, PERS: 3rd] and a verb specified as [NUM: plural, PERS: 3rd, TENSE: past] — these unify successfully, yielding a combined structure with all five values. Now try a subject [NUM: singular] with a verb requiring [NUM: plural] — the NUM attribute conflicts, unification fails, and the grammar correctly predicts the sentence is ungrammatical ("*The cat were sleeping").

This mechanism elegantly handles the range of agreement phenomena you've studied. Subject-verb agreement in English, gender and case agreement between articles and nouns in German, person agreement in Spanish verbs — all can be modeled as unification constraints. The grammar specifies that to combine a subject and verb, their feature structures must unify on the relevant attributes. Where agreement is more complex — as in languages with multiple agreement targets — the feature structures simply carry more attributes, and unification handles the logic without special-case rules.

The computational appeal of unification is that it is both **declarative** and **general-purpose**. Rather than writing separate procedural rules for each type of agreement ("if the subject is singular, make the verb singular; if the subject is plural, make the verb plural..."), the grammar specifies feature constraints once, and unification applies them uniformly. This is why unification forms the backbone of constraint-based grammar formalisms like Lexical-Functional Grammar (LFG) and Head-Driven Phrase Structure Grammar (HPSG) — both of which you'll encounter as you build on this foundation. In those frameworks, every grammatical combination in the language is licensed by successful unification of feature structures, and every ungrammatical combination corresponds to a unification failure — a clean, falsifiable, formally explicit account of what it means for a sentence to be grammatical.
