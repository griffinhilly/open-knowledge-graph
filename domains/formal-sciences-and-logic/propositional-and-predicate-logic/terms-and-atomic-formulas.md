---
id: terms-and-atomic-formulas
title: Terms and Atomic Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: predicates-and-relations-fol
  type: hard
builds-toward:
- formulas-and-well-formed-expressions
tags:
- syntax
- first-order-logic
stage: formal-systems
status: draft
---

# Terms and Atomic Formulas

## Core Idea
A term is a syntactic expression denoting an object: a variable, constant, or complex term formed by applying function symbols (e.g., f(a), g(x, y)). An atomic formula applies a predicate to a sequence of terms: P(t₁, …, tₙ). Atomic formulas are the foundation of all first-order formulas.

## Questions

```yaml
- question: "In first-order logic, which of the following is a term but NOT an atomic formula?"
  type: multiple-choice
  options:
    - "P(x), where P is a unary predicate and x is a variable"
    - "f(a, b), where f is a binary function symbol and a, b are constants"
    - "x = y, where x and y are variables"
    - "∀x P(x), where P is a unary predicate"
  answer: 1
  explanation: "f(a, b) is a complex term: a function symbol applied to two term arguments. It refers to an object in the domain — it denotes something but makes no claim that could be true or false. P(x) is an atomic formula (predicate applied to a term). x = y is also an atomic formula (the built-in equality predicate applied to two terms). ∀x P(x) is a quantified formula. The key distinction is that terms denote objects while formulas make claims."

- question: "Consider g(f(x), c), where g is a binary function symbol, f is a unary function symbol, x is a variable, and c is a constant. What is this expression?"
  type: multiple-choice
  options:
    - "An atomic formula, because it contains predicate-like symbols applied to terms"
    - "A complex term, because it is built from function symbols applied to other terms"
    - "A quantified formula, because it contains a variable"
    - "An atomic formula when g is interpreted as a predicate in a specific structure"
  answer: 1
  explanation: "g(f(x), c) is a complex term built inductively: x is a variable (term), c is a constant (term), f(x) is a complex term, and g(f(x), c) is a complex term (binary function applied to two terms). No predicate symbol appears here. Function symbols build terms (noun phrases referring to objects); predicate symbols build atomic formulas (sentences making claims). The presence of a variable does not make something a quantified formula — quantification requires explicit ∀ or ∃."

- question: "An atomic formula is the simplest kind of expression in first-order logic that can be evaluated as true or false."
  type: true-false
  answer: true
  explanation: "Terms (variables, constants, complex terms) refer to objects but cannot be evaluated as true or false — they denote, they do not claim. Atomic formulas are the base case of the formula definition: P(t₁,...,tₙ) applies a predicate to terms, making the simplest possible claim. All compound formulas (conjunctions, negations, quantified statements) are built from atomic formulas by applying connectives and quantifiers. Atomic formulas are where truth values first enter."

- question: "A variable in first-order logic is a type of atomic formula."
  type: true-false
  answer: false
  explanation: "A variable is a term, not a formula. Terms and formulas are distinct syntactic categories. Terms refer to objects (noun phrases); formulas make claims that can be true or false (sentences). A variable like x denotes whatever object is assigned to it in an interpretation — it does not assert anything and cannot be evaluated as true or false. Confusing terms with formulas is a fundamental syntax error in first-order logic."

- question: "What is the difference between a term and an atomic formula, and why does this distinction matter for interpreting first-order logic?"
  type: short-answer
  answer: "A term is a syntactic expression that denotes an object: a variable, constant, or function symbol applied to terms. An atomic formula is a predicate symbol applied to a sequence of terms, making the simplest possible claim that can be true or false. Terms answer 'which object?' while atomic formulas answer 'what is true of that object?' The distinction matters because truth values only apply to formulas — you cannot negate or quantify a term, only a formula."
  explanation: "This separation between the naming layer (terms) and the claiming layer (formulas) is fundamental to how first-order logic is interpreted in structures. When evaluating a formula in a model, terms are mapped to domain elements, then the predicate is checked on those elements. Understanding that f(x) is a term (object reference) while P(f(x)) is a formula (claim) clarifies what can be negated, quantified over, or combined with logical connectives — all operations that apply to formulas, not terms."
```

## Explainer

In first-order logic, every formula is built from smaller pieces, much like how sentences are built from words. You already know about **predicates and relations** — properties and relationships that can hold between objects. Terms and atomic formulas are the syntax layer that specifies *what objects* those predicates talk about and *how* to build the simplest meaningful statements.

A **term** is a syntactic expression that refers to an object in the domain. There are three kinds. A **variable** (like x, y, z) is a placeholder for an unspecified object — think of it as a pronoun. A **constant symbol** (like a, b, c, or 0, 1 in arithmetic) is a name for a specific object. A **complex term** is formed by applying a **function symbol** to other terms: if f is a unary function symbol and t is a term, then f(t) is also a term; similarly g(t₁, t₂) for a binary function symbol g. In arithmetic, the expression s(0) uses the successor function symbol s applied to the constant 0, denoting the number 1. Terms can nest: s(s(s(0))) denotes 3. Terms are the "noun phrases" of first-order logic.

An **atomic formula** takes a predicate symbol and applies it to a sequence of terms. If P is a unary predicate and t is a term, then P(t) is an atomic formula — the simplest possible claim, asserting that the object denoted by t has property P. If R is a binary predicate and t₁, t₂ are terms, then R(t₁, t₂) says the pair stands in relation R. In arithmetic, x < y and x = y+1 are atomic formulas. Equality is a special built-in binary predicate: t₁ = t₂ asserts the two terms denote the same object.

Atomic formulas are the **base cases** of the inductive definition of formulas. Every compound formula — negations, conjunctions, disjunctions, implications, quantified statements — is built by combining atomic formulas using logical connectives and quantifiers. This means when you evaluate a formula in a structure, you ultimately reduce everything to asking about atomic formulas: does this object satisfy this predicate? Does this pair stand in this relation? Getting the term/atomic formula distinction right is essential before you can study quantifiers, interpret formulas in models, or understand the difference between syntax (the formula itself) and semantics (what it means in a particular structure).
