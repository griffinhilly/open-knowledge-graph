---
id: signature-and-vocabulary-model-theory
title: Signature and Formal Vocabulary
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: structures-and-formal-languages
  type: hard
builds-toward:
- model-instantiation-structures
- embedding-and-preservation-properties
tags:
- signature
- vocabulary
- language
- formalization
stage: abstract-reasoning
status: draft
---

# Signature and Formal Vocabulary

## Core Idea
A signature consists of a set of constant symbols, function symbols, and relation symbols with specified arities. The signature defines the vocabulary through which we can express properties of structures. Every first-order theory is formulated in a particular signature, and different signatures can express different classes of mathematical objects.

## How It's Best Learned
Study signatures for familiar mathematical structures: the signature for groups (one binary operation, identity), fields (addition, multiplication), and ordered sets (a binary relation). Compare how the same underlying structure can be described in different signatures.

## Common Misconceptions
Signature is not the same as a theory—a signature is the vocabulary, while a theory makes statements in that vocabulary. The choice of signature can dramatically affect what is expressible.

## Explainer

You already know that first-order logic has syntax (formulas built from variables, logical connectives, and quantifiers) and semantics (interpretations that assign meaning). A **signature** — also called a **vocabulary** or **language** — is the bridge between them: it specifies *what kind of things* your formulas can talk about, before you commit to any particular interpretation. A signature σ is simply a list: a collection of constant symbols (like `0`, `1`, `e`), function symbols each with an **arity** (like `+` with arity 2, or `succ` with arity 1), and relation symbols each with an arity (like `<` with arity 2, or `Prime` with arity 1). Nothing more — no rules about what these symbols mean, just their names and arities.

The same underlying mathematical object can be described by different signatures, and the choice matters enormously. The integers ℤ can be presented with signature {+, ·, 0, 1} (the ring signature), or with {+, ·, 0, 1, <} (adding the order), or with {+, ·, 0, 1, |} where `|` is divisibility. Each enrichment allows you to express more properties. In the ring signature, you can define even numbers (∃y, x = y + y) but not primeness without a richer vocabulary. In the signature with `<`, you can express order properties. The key lesson is that **what is definable depends entirely on the signature**: change the vocabulary, change what can be said.

A **structure** for a signature σ is a universe (a set of elements) together with interpretations for each symbol in σ: each constant gets assigned an element, each function symbol gets a function of the right arity, and each relation symbol gets a subset of the appropriate Cartesian product. When you say "the group (ℤ, +, 0)" you are specifying a structure for the signature {+, 0}: the universe is ℤ, `+` is interpreted as integer addition, `0` is the integer zero. Two structures for the same signature can be compared (are they isomorphic? does one embed in the other?), but structures for different signatures are not directly comparable — they speak different languages.

**Expansion** and **reduct** are the two operations on signatures. If you add new symbols to σ to get σ', a σ-structure M can be expanded to a σ'-structure M' by interpreting the new symbols. Conversely, the σ-reduct of M' forgets the extra interpretations. This is routine but conceptually important: adding a constant for a specific element (as in the diagram construction) is an expansion. The ability to freely expand and then take reducts is what lets model theory study structures through their enriched cousins, then strip away the extra vocabulary when done.

