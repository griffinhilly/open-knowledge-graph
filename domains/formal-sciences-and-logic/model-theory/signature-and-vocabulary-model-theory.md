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
stage: advanced
status: draft
---

# Signature and Formal Vocabulary

## Core Idea
A signature consists of a set of constant symbols, function symbols, and relation symbols with specified arities. The signature defines the vocabulary through which we can express properties of structures. Every first-order theory is formulated in a particular signature, and different signatures can express different classes of mathematical objects.

## How It's Best Learned
Study signatures for familiar mathematical structures: the signature for groups (one binary operation, identity), fields (addition, multiplication), and ordered sets (a binary relation). Compare how the same underlying structure can be described in different signatures.

## Common Misconceptions
Signature is not the same as a theory—a signature is the vocabulary, while a theory makes statements in that vocabulary. The choice of signature can dramatically affect what is expressible.

## Questions

```yaml
- question: "A logician describes the integers ℤ with two different signatures: σ₁ = {+, 0, 1} and σ₂ = {+, ·, 0, 1}. Which statement about these two presentations is correct?"
  type: multiple-choice
  options:
    - "Both presentations are equivalent — ℤ is the same object, so both signatures express the same properties"
    - "σ₂ is strictly more expressive — properties involving multiplication (like divisibility) can be expressed in σ₂ but not directly in σ₁"
    - "The choice of signature is a notational convenience with no effect on what can be proven"
    - "σ₁ is more fundamental because addition is the basic operation of ℤ"
  answer: 1
  explanation: "Signature determines what properties can be expressed in formulas. In σ₁ = {+, 0, 1}, multiplication is not part of the vocabulary, so properties essentially involving multiplication — like 'x divides y' or 'x is a perfect square' — cannot be expressed directly. Adding · to get σ₂ opens up an entire class of new expressible properties. The underlying mathematical object is the same ℤ, but two structures for different signatures speak different formal languages. Changing the vocabulary changes what can be said, what theories can be formulated, and what structures can be distinguished."

- question: "A student says: 'I've written down signature σ = {e, ·, inv} with a constant, a binary function, and a unary function. This signature defines the theory of groups.' What is the error?"
  type: multiple-choice
  options:
    - "Group signatures cannot include a constant — identity must be a relation"
    - "A signature specifies only the vocabulary — symbol names and arities. It defines no theory; axioms (associativity, identity, inverses) are separate statements in that vocabulary"
    - "The signature is correct and fully defines the theory of groups"
    - "Signatures cannot mix constants, function symbols, and relation symbols"
  answer: 1
  explanation: "This is the core distinction: signature ≠ theory. A signature is purely syntactic: it lists symbol names and arities (e is a constant, · is binary, inv is unary) with no constraints on interpretation. Any set with any function interpreting · and any function interpreting inv is a σ-structure, even if it fails associativity or lacks inverses. The theory of groups requires additional axioms: associativity (∀xyz, x·(y·z)=(x·y)·z), identity (∀x, x·e=x=e·x), inverses (∀x, x·inv(x)=e). The signature σ is the vocabulary for groups; the axioms are what restrict σ-structures to groups specifically."

- question: "Two structures that interpret different signatures cannot be directly compared for properties like isomorphism, because they speak different formal languages."
  type: true-false
  answer: true
  explanation: "Isomorphism (and other structural comparisons like embedding or elementary equivalence) are defined between structures for the *same* signature. A σ₁-structure M and a σ₂-structure N interpret different symbols, so there is no natural way to compare them unless one signature extends the other. For instance, asking whether a group (interpreted in {·, e, inv}) is isomorphic to an ordered set (interpreted in {<}) is not a well-formed model-theoretic question. Comparing requires a shared vocabulary, which is why expansions and reducts — moving between related signatures — are important operations."

- question: "The same set can serve as the universe for multiple distinct structures, all for the same signature, by interpreting the signature's symbols differently."
  type: true-false
  answer: true
  explanation: "A structure for signature σ = {·, e} consists of a universe (a set) plus an interpretation: · gets assigned some binary function on the set, e gets assigned some element. The set ℤ can be a σ-structure with · as multiplication and e as 1 (giving a monoid), or with · as addition and e as 0 (giving a different monoid), or with · as the 'always return the left argument' function — all different σ-structures on the same universe. The structure is the combination of universe plus interpretation, not the universe alone."

- question: "What does it mean to 'expand' a structure to a larger signature, and why is this operation useful in model theory?"
  type: short-answer
  answer: "To expand a σ-structure M to a σ'-structure M' (where σ' adds new symbols to σ) means interpreting the new symbols in the same universe M already has. The existing interpretations of σ symbols are unchanged; the new σ'-symbols are given fresh interpretations. The operation is useful because it lets model theorists add 'named constants' or auxiliary functions to a structure to make certain elements or properties explicitly accessible — for example, adding constants for each element of M (the diagram construction) to study what sentences M satisfies, then taking the σ-reduct afterward to strip away the auxiliary machinery."
  explanation: "Expansion and reduct are the two basic signature operations. An expansion adds new vocabulary without changing the underlying universe or the interpretations of existing symbols. The reduct is the inverse: given a σ'-structure, forget the interpretations of symbols not in σ to get a σ-structure. These operations are used throughout model theory — for example, in the compactness theorem applications where you expand the language to include constant witnesses, prove something about the expanded structure, and then reduce back. Controlling which vocabulary is present at each step is essential to the method."
```

## Explainer

You already know that first-order logic has syntax (formulas built from variables, logical connectives, and quantifiers) and semantics (interpretations that assign meaning). A **signature** — also called a **vocabulary** or **language** — is the bridge between them: it specifies *what kind of things* your formulas can talk about, before you commit to any particular interpretation. A signature σ is simply a list: a collection of constant symbols (like `0`, `1`, `e`), function symbols each with an **arity** (like `+` with arity 2, or `succ` with arity 1), and relation symbols each with an arity (like `<` with arity 2, or `Prime` with arity 1). Nothing more — no rules about what these symbols mean, just their names and arities.

The same underlying mathematical object can be described by different signatures, and the choice matters enormously. The integers ℤ can be presented with signature {+, ·, 0, 1} (the ring signature), or with {+, ·, 0, 1, <} (adding the order), or with {+, ·, 0, 1, |} where `|` is divisibility. Each enrichment allows you to express more properties. In the ring signature, you can define even numbers (∃y, x = y + y) but not primeness without a richer vocabulary. In the signature with `<`, you can express order properties. The key lesson is that **what is definable depends entirely on the signature**: change the vocabulary, change what can be said.

A **structure** for a signature σ is a universe (a set of elements) together with interpretations for each symbol in σ: each constant gets assigned an element, each function symbol gets a function of the right arity, and each relation symbol gets a subset of the appropriate Cartesian product. When you say "the group (ℤ, +, 0)" you are specifying a structure for the signature {+, 0}: the universe is ℤ, `+` is interpreted as integer addition, `0` is the integer zero. Two structures for the same signature can be compared (are they isomorphic? does one embed in the other?), but structures for different signatures are not directly comparable — they speak different languages.

**Expansion** and **reduct** are the two operations on signatures. If you add new symbols to σ to get σ', a σ-structure M can be expanded to a σ'-structure M' by interpreting the new symbols. Conversely, the σ-reduct of M' forgets the extra interpretations. This is routine but conceptually important: adding a constant for a specific element (as in the diagram construction) is an expansion. The ability to freely expand and then take reducts is what lets model theory study structures through their enriched cousins, then strip away the extra vocabulary when done.

