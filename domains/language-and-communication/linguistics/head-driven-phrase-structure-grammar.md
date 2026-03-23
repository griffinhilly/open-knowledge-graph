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
stage: advanced
status: validated
---

# Head-Driven Phrase Structure Grammar

## Core Idea
Head-Driven Phrase Structure Grammar (HPSG) builds on typed feature structures to represent phrases. The head of a phrase determines key properties; constituents are gathered in valence lists that track which arguments are satisfied. Structure-sharing encodes agreement and long-distance dependencies.

## Questions

```yaml
- question: "In HPSG, how is the dependency between 'which book' and the gap after 'read' in 'Which book did she read?' maintained without moving the wh-word from the gap site?"
  type: multiple-choice
  options:
    - "A transformation moves the wh-word to sentence-initial position at the level of logical form, as in Minimalism"
    - "The grammar generates two independent copies of the wh-phrase and checks their agreement at the end of the derivation"
    - "A SLASH feature propagates up the tree from the gap site, using structure-sharing so the gap and the filler refer to the same object in the feature structure"
    - "A deletion rule removes the gap and leaves the fronted wh-word bearing all properties of the missing element"
  answer: 2
  explanation: "HPSG is explicitly non-derivational — there is no movement, no transformation, no derivation at all. Instead, a SLASH feature is introduced at the gap site and propagated up the tree through structure-sharing until it is discharged at the point where the filler appears. Because structure-sharing means the gap and filler refer to the same data object (not copies that must be kept in sync), their phonological, syntactic, and semantic properties are automatically identical. This is the formal payoff of the unification framework."

- question: "A transitive verb 'devours' starts with a non-empty COMPS list. After combining with its noun phrase object, what is the state of the resulting verb phrase's COMPS list?"
  type: multiple-choice
  options:
    - "Unchanged — the verb phrase inherits all feature values from the head verb, including its COMPS list"
    - "The object's features are appended to the COMPS list of the verb phrase"
    - "The object is consumed off the COMPS list, leaving the verb phrase with an empty COMPS list"
    - "The COMPS list is replaced by an SPR list, which will be satisfied by the subject"
  answer: 2
  explanation: "In HPSG, valence lists track which arguments a head still needs to combine with. When a complement combines with the head, the Valence Principle ensures the complement is 'consumed' — removed from the COMPS list of the resulting phrase. A well-formed sentence is one where all valence requirements have been discharged: every COMPS and SPR list is empty at the root. This is how HPSG encodes subcategorization without movement or phrase structure rules."

- question: "In HPSG, the Head Feature Principle ensures that certain features of the head word are literally shared with the mother node — not merely copied to it."
  type: true-false
  answer: true
  explanation: "Structure-sharing in HPSG means that head features and mother features refer to the same location in the data structure, not independent slots that happen to hold the same value. A change to the head's feature is therefore automatically reflected in the mother's feature — they are the same object. This is what makes HPSG a constraint-based rather than rule-based system: constraints apply simultaneously to a single feature structure, not sequentially to a derivation."

- question: "HPSG uses movement transformations, like Minimalism's Internal Merge, to handle long-distance dependencies such as wh-questions and relative clauses."
  type: true-false
  answer: false
  explanation: "HPSG is explicitly constraint-based and non-derivational — there are no movement operations, no derivational history, and no levels of representation that transformations operate between. Long-distance dependencies are handled by the SLASH mechanism: a feature introduced at the gap site propagates up the tree through structure-sharing until it is bound off by the filler. The grammar states constraints that a feature structure must simultaneously satisfy; it does not build structures through ordered operations."

- question: "What is structure-sharing in HPSG, and why is it more powerful than simply copying feature values between parts of a structure?"
  type: short-answer
  answer: "Structure-sharing means that two positions in a feature structure refer to the same data object — they are co-indexed to literally the same value, not independent copies that happen to match. Copying creates two separate slots that must be kept in sync by explicit checking mechanisms; structure-sharing makes identity automatic. If the shared value changes for any reason, the change is immediately reflected everywhere the value is shared. For long-distance dependencies, structure-sharing ensures that a gap and its filler have identical properties not because the grammar checks them against each other, but because they are the same thing in the data structure. This is why HPSG can handle agreement, head-feature inheritance, and wh-dependencies without stipulating separate enforcement mechanisms — identity constraints arise naturally from the architecture."
  explanation: "This distinction is the formal reason HPSG's unification-based architecture is particularly elegant for linguistic analysis: properties that in other frameworks require explicit rules or operations to maintain emerge automatically from the data structure itself."
```

## Explainer

**Head-Driven Phrase Structure Grammar (HPSG)** is a constraint-based syntactic framework built on the typed feature structures you studied in unification. Where transformational approaches derive sentences by moving elements around, HPSG instead states a set of constraints that any well-formed structure must simultaneously satisfy. No derivations, no movement — only feature structures that either unify or fail to unify.

The central organizing concept is the **head**. Every grammatical phrase has a head — the word that determines the phrase's core syntactic and semantic properties. In a noun phrase, the head noun determines whether the phrase is singular or plural, count or mass. In a verb phrase, the head verb determines what arguments are required. The head's feature structure propagates to the phrase as a whole through the **Head Feature Principle**: certain features of the head (like part-of-speech category) are shared with the mother node by structure-sharing, meaning they literally refer to the same value in the feature structure, not just a copy of it. If you change the head's feature, the phrase's feature changes automatically.

Arguments and complements are tracked through **valence lists** — specifically, the COMPS (complements) and SPR (specifier) lists. A transitive verb like "devours" begins with a non-empty COMPS list requiring a noun phrase object. When it combines with its object, the complement is consumed off the list: the resulting verb phrase has an empty COMPS list. This is the grammar's way of encoding subcategorization. A well-formed sentence is one where all valence requirements have been satisfied — every list is empty at the top of the tree.

**Structure-sharing** — the use of co-indexed values across different parts of a feature structure — is what makes long-distance dependencies tractable without movement. In a sentence like "Which book did she read?", the gap inside the relative clause is linked to the fronted wh-word not by moving anything but by propagating a SLASH feature up the tree from the gap site to the point where it is discharged. Structure-sharing ensures the phonological, syntactic, and semantic properties of the filler and the gap are kept identical — they are the same object in the data structure, not two copies that need to be kept in sync. This is the formal payoff of the unification mechanism: identity constraints are natural and automatic rather than imposed by stipulation.
