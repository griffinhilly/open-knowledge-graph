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
builds-toward:
- unification-mechanism
- lexical-functional-grammar
tags:
- formalism
- representation
- features
stage: formal-systems
status: draft
---

# Typed Feature Structures

## Core Idea
Feature structures are formal objects (attribute-value pairs organized hierarchically) used to represent linguistic constituents. Types define what features are allowed and their constraints, enabling systematic representation of agreement, subcategorization, and other phenomena.

## Explainer

You already know from symbolic representation in linguistics that formal grammars use structured objects rather than raw strings to represent linguistic information. You also know from feature agreement checking that agreement phenomena — like a verb matching its subject in number and person — can be encoded in terms of features that must unify across constituents. **Typed feature structures** provide the formal scaffolding that makes this precise and generative: they specify not just the features a linguistic object has, but the *type* of object it is, and what features objects of that type are *required* to have.

A **feature structure** is a set of attribute-value pairs organized hierarchically. Imagine a noun phrase like "the tall woman" represented not as a string but as a record: [CAT: NP, NUM: sg, GEND: fem, HEAD: woman, ...]. Each attribute names a grammatical dimension; each value either fills it directly (with a simple value like "sg") or fills it with a nested feature structure (allowing recursive description). This is richer than simple category labels because it bundles together multiple dimensions of grammatical information into a single coherent object. The constituent's type, category, number, gender, and subcategorization requirements are all accessible in one place.

**Types** add a layer of organization above individual structures. A type hierarchy constrains which features are grammatically meaningful for which kinds of objects. The type "noun-phrase" might require the features CAT, NUM, and CASE; the type "verb" might require TENSE, ASPECT, and subcategorization information. Types are arranged in a hierarchy: "transitive-verb" is a subtype of "verb," inheriting all verb features and adding an object requirement. This inheritance relationship means information only needs to be stated once at the appropriate level — all verbs share certain properties, and transitive verbs additionally share others.

The key operation on feature structures is **unification**: combining two structures into one by merging their information. If one structure specifies [NUM: sg] and another specifies [NUM: sg, GEND: fem], unification produces [NUM: sg, GEND: fem] — consistent information is merged. If one specifies [NUM: sg] and another specifies [NUM: pl], unification fails — the structures are inconsistent and the grammatical operation that combined them is blocked. This failure mechanism is how typed feature structures enforce agreement: a subject with [NUM: pl] cannot unify with a verb requiring [NUM: sg], so that combination is ruled out as ungrammatical. The formalism turns agreement checking from an ad hoc rule into a consequence of a general constraint-satisfaction mechanism that applies uniformly across all grammatical phenomena.
