---
id: typed-feature-structures
title: Typed Feature Structures
domain: language-and-communication
course: linguistics
prerequisites:
- id: symbolic-representation-linguistics
  type: hard
- id: feature-agreement-checking
  type: soft
- id: inflectional-morphology-formal
  type: soft
builds-toward:
- unification-mechanism
- lexical-functional-grammar
tags:
- formalism
- representation
- features
stage: advanced
status: validated
---
# Typed Feature Structures

## Core Idea
Feature structures are formal objects (attribute-value pairs organized hierarchically) used to represent linguistic constituents. Types define what features are allowed and their constraints, enabling systematic representation of agreement, subcategorization, and other phenomena.

## Questions

```yaml
- question: "A parser encounters the sentence 'The dogs runs.' The subject DP has the feature [NUM: pl] and the verb has the subcategorization constraint [NUM: sg]. In a typed feature structure grammar, how is the ungrammaticality detected?"
  type: multiple-choice
  options:
    - "A separate post-parse agreement checker scans the sentence and flags the number mismatch as a violation"
    - "Unification of the subject's feature structure with the verb's requirements fails because [NUM: pl] and [NUM: sg] are incompatible values, blocking the parse"
    - "The type hierarchy classifies 'dogs' and 'runs' as incompatible types before features are consulted"
    - "The grammar's phrase structure rules explicitly list permitted subject-verb combinations, and this pair is absent"
  answer: 1
  explanation: "Unification failure is the mechanism by which typed feature structures enforce agreement constraints. When the grammar attempts to combine the subject and verb into a sentence, it unifies their feature structures. The subject carries [NUM: pl]; the verb's licensing constraint requires [NUM: sg]. These values clash: unification produces no result and the grammatical operation is blocked. There is no separate agreement module — the constraint falls out of the general unification operation applied uniformly across all grammatical phenomena. This is the elegant power of the formalism."

- question: "In a typed feature structure grammar, the type 'ditransitive-verb' is a subtype of 'transitive-verb,' which is a subtype of 'verb.' When assigning the feature structure to a ditransitive verb like 'give,' what does the type hierarchy contribute?"
  type: multiple-choice
  options:
    - "Nothing — each verb type must list all its required features independently, since types cannot share information"
    - "The feature structure of 'give' automatically inherits all features required of 'verb' and 'transitive-verb,' and adds only the features specific to ditransitive verbs"
    - "The hierarchy reclassifies 'give' as a basic verb type to simplify the representation"
    - "The type hierarchy is used only for semantic classification, not for constraining feature structures"
  answer: 1
  explanation: "Type hierarchies encode linguistic generalizations through inheritance. All verbs share certain features (TENSE, agreement requirements); this is stated once at the 'verb' type. Transitive verbs additionally require an object subcategorization frame; this is stated at 'transitive-verb.' Ditransitive verbs inherit both and add a second object slot. 'Give' acquires all these features automatically by virtue of its type — without redeclaring verb-hood. This prevents redundancy and ensures generalizations about verbs are enforced uniformly across all subtypes."

- question: "Unification of two feature structures usually succeeds as long as both structures are well-typed — that is, consistent with the constraints of the type hierarchy."
  type: true-false
  answer: false
  explanation: "Well-typedness is necessary but not sufficient for unification to succeed. Two well-typed structures can still fail to unify if they specify incompatible values for the same feature — [NUM: sg] and [NUM: pl] are both perfectly well-typed values, but they cannot unify. Unification requires that every shared feature have compatible values. Unification failure, not type violation, is the primary mechanism ruling out ungrammatical constructions like number disagreement: both the subject and verb are well-typed, but their feature structures are incompatible."

- question: "A typed feature structure can simultaneously encode the syntactic category of a linguistic element and detailed grammatical properties (number, case, subcategorization requirements) in a single unified object."
  type: true-false
  answer: true
  explanation: "This integration is a core motivation for feature structures. Instead of encoding 'noun phrase' as a flat category label and separately tracking number and case, a typed feature structure bundles all grammatically relevant dimensions — [CAT: NP, NUM: sg, CASE: nom, HEAD: woman, ...] — into one hierarchically organized object. This allows unification to simultaneously check compatibility across all dimensions in a single operation, and allows subcategorization frames to be encoded as nested feature structures rather than lists of rules. The formalism's expressive power comes precisely from this integration."

- question: "What is unification in the context of typed feature structures, and how does unification failure serve as the mechanism for ruling out ungrammatical constructions?"
  type: short-answer
  answer: "Unification is the operation of combining two feature structures into one by merging their attribute-value pairs. For shared attributes, the values must themselves be unifiable (compatible); compatible information is merged into a single richer structure. If any attribute has conflicting values in the two structures (e.g., [NUM: sg] vs [NUM: pl]), unification fails — no merged structure is produced. In a grammar, combining constituents works by unifying their feature structures; if unification fails, the combination is blocked and the sentence is ruled out as ungrammatical. Agreement, subcategorization, and case licensing all fall out of this one mechanism rather than requiring separate rules."
  explanation: "The elegance of the approach is that a single general operation — unification — replaces a proliferation of specific agreement rules. The grammar encodes constraints in feature structures and lets unification failure enforce them automatically and uniformly. This captures the linguistic insight that agreement phenomena share a common underlying logic across different grammatical dimensions."
```

## Explainer

You already know from symbolic representation in linguistics that formal grammars use structured objects rather than raw strings to represent linguistic information. You also know from feature agreement checking that agreement phenomena — like a verb matching its subject in number and person — can be encoded in terms of features that must unify across constituents. **Typed feature structures** provide the formal scaffolding that makes this precise and generative: they specify not just the features a linguistic object has, but the *type* of object it is, and what features objects of that type are *required* to have.

A **feature structure** is a set of attribute-value pairs organized hierarchically. Imagine a noun phrase like "the tall woman" represented not as a string but as a record: [CAT: NP, NUM: sg, GEND: fem, HEAD: woman, ...]. Each attribute names a grammatical dimension; each value either fills it directly (with a simple value like "sg") or fills it with a nested feature structure (allowing recursive description). This is richer than simple category labels because it bundles together multiple dimensions of grammatical information into a single coherent object. The constituent's type, category, number, gender, and subcategorization requirements are all accessible in one place.

**Types** add a layer of organization above individual structures. A type hierarchy constrains which features are grammatically meaningful for which kinds of objects. The type "noun-phrase" might require the features CAT, NUM, and CASE; the type "verb" might require TENSE, ASPECT, and subcategorization information. Types are arranged in a hierarchy: "transitive-verb" is a subtype of "verb," inheriting all verb features and adding an object requirement. This inheritance relationship means information only needs to be stated once at the appropriate level — all verbs share certain properties, and transitive verbs additionally share others.

The key operation on feature structures is **unification**: combining two structures into one by merging their information. If one structure specifies [NUM: sg] and another specifies [NUM: sg, GEND: fem], unification produces [NUM: sg, GEND: fem] — consistent information is merged. If one specifies [NUM: sg] and another specifies [NUM: pl], unification fails — the structures are inconsistent and the grammatical operation that combined them is blocked. This failure mechanism is how typed feature structures enforce agreement: a subject with [NUM: pl] cannot unify with a verb requiring [NUM: sg], so that combination is ruled out as ungrammatical. The formalism turns agreement checking from an ad hoc rule into a consequence of a general constraint-satisfaction mechanism that applies uniformly across all grammatical phenomena.
