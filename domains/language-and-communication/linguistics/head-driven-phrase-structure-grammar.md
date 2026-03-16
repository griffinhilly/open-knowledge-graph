---
id: head-driven-phrase-structure-grammar
title: Head-Driven Phrase Structure Grammar
domain: language-and-communication
course: linguistics
prerequisites:
- id: unification-mechanism
  type: hard
- id: constituent-trees-and-notation
  type: soft
tags:
- syntax
- framework
- formalism
stage: formal-systems
status: draft
---

# Head-Driven Phrase Structure Grammar

## Core Idea
Head-Driven Phrase Structure Grammar (HPSG) builds on typed feature structures to represent phrases. The head of a phrase determines key properties; constituents are gathered in valence lists that track which arguments are satisfied. Structure-sharing encodes agreement and long-distance dependencies.

## Explainer

**Head-Driven Phrase Structure Grammar (HPSG)** is a constraint-based syntactic framework built on the typed feature structures you studied in unification. Where transformational approaches derive sentences by moving elements around, HPSG instead states a set of constraints that any well-formed structure must simultaneously satisfy. No derivations, no movement — only feature structures that either unify or fail to unify.

The central organizing concept is the **head**. Every grammatical phrase has a head — the word that determines the phrase's core syntactic and semantic properties. In a noun phrase, the head noun determines whether the phrase is singular or plural, count or mass. In a verb phrase, the head verb determines what arguments are required. The head's feature structure propagates to the phrase as a whole through the **Head Feature Principle**: certain features of the head (like part-of-speech category) are shared with the mother node by structure-sharing, meaning they literally refer to the same value in the feature structure, not just a copy of it. If you change the head's feature, the phrase's feature changes automatically.

Arguments and complements are tracked through **valence lists** — specifically, the COMPS (complements) and SPR (specifier) lists. A transitive verb like "devours" begins with a non-empty COMPS list requiring a noun phrase object. When it combines with its object, the complement is consumed off the list: the resulting verb phrase has an empty COMPS list. This is the grammar's way of encoding subcategorization. A well-formed sentence is one where all valence requirements have been satisfied — every list is empty at the top of the tree.

**Structure-sharing** — the use of co-indexed values across different parts of a feature structure — is what makes long-distance dependencies tractable without movement. In a sentence like "Which book did she read?", the gap inside the relative clause is linked to the fronted wh-word not by moving anything but by propagating a SLASH feature up the tree from the gap site to the point where it is discharged. Structure-sharing ensures the phonological, syntactic, and semantic properties of the filler and the gap are kept identical — they are the same object in the data structure, not two copies that need to be kept in sync. This is the formal payoff of the unification mechanism: identity constraints are natural and automatic rather than imposed by stipulation.
