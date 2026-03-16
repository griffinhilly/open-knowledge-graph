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
builds-toward:
- lexical-functional-grammar
- head-driven-phrase-structure-grammar
tags:
- formalism
- agreement
- computation
stage: formal-systems
status: draft
---

# Unification and Feature Agreement

## Core Idea
Unification is a formal operation that merges two feature structures by resolving shared features. It provides a mathematical account of agreement: two constituents can combine only if their features unify without contradiction.

## Explainer

You already know how to represent linguistic information as **typed feature structures** — attribute-value matrices where grammatical properties like number, person, case, and gender are encoded as attribute-value pairs. Unification is the operation that determines whether two such structures are compatible, and if so, what the combined structure looks like. Think of it as checking whether two puzzle pieces can join: if neither contradicts the other, they merge; if they conflict on any shared attribute, they fail to unify, and no grammatical combination is possible.

The formal definition is straightforward. Two feature structures unify if, for every attribute they share, their values for that attribute are compatible. Compatibility means either both values are identical, or one value is underspecified (a variable that can take any value) and the other provides a specific value that fills it in. The result of unification is a new feature structure containing all attributes from both inputs, with shared attributes resolved to their specific values. Consider a subject noun phrase specified as [NUM: plural, PERS: 3rd] and a verb specified as [NUM: plural, PERS: 3rd, TENSE: past] — these unify successfully, yielding a combined structure with all five values. Now try a subject [NUM: singular] with a verb requiring [NUM: plural] — the NUM attribute conflicts, unification fails, and the grammar correctly predicts the sentence is ungrammatical ("*The cat were sleeping").

This mechanism elegantly handles the range of agreement phenomena you've studied. Subject-verb agreement in English, gender and case agreement between articles and nouns in German, person agreement in Spanish verbs — all can be modeled as unification constraints. The grammar specifies that to combine a subject and verb, their feature structures must unify on the relevant attributes. Where agreement is more complex — as in languages with multiple agreement targets — the feature structures simply carry more attributes, and unification handles the logic without special-case rules.

The computational appeal of unification is that it is both **declarative** and **general-purpose**. Rather than writing separate procedural rules for each type of agreement ("if the subject is singular, make the verb singular; if the subject is plural, make the verb plural..."), the grammar specifies feature constraints once, and unification applies them uniformly. This is why unification forms the backbone of constraint-based grammar formalisms like Lexical-Functional Grammar (LFG) and Head-Driven Phrase Structure Grammar (HPSG) — both of which you'll encounter as you build on this foundation. In those frameworks, every grammatical combination in the language is licensed by successful unification of feature structures, and every ungrammatical combination corresponds to a unification failure — a clean, falsifiable, formally explicit account of what it means for a sentence to be grammatical.
