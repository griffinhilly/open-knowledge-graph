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

## Explainer

In first-order logic, every formula is built from smaller pieces, much like how sentences are built from words. You already know about **predicates and relations** — properties and relationships that can hold between objects. Terms and atomic formulas are the syntax layer that specifies *what objects* those predicates talk about and *how* to build the simplest meaningful statements.

A **term** is a syntactic expression that refers to an object in the domain. There are three kinds. A **variable** (like x, y, z) is a placeholder for an unspecified object — think of it as a pronoun. A **constant symbol** (like a, b, c, or 0, 1 in arithmetic) is a name for a specific object. A **complex term** is formed by applying a **function symbol** to other terms: if f is a unary function symbol and t is a term, then f(t) is also a term; similarly g(t₁, t₂) for a binary function symbol g. In arithmetic, the expression s(0) uses the successor function symbol s applied to the constant 0, denoting the number 1. Terms can nest: s(s(s(0))) denotes 3. Terms are the "noun phrases" of first-order logic.

An **atomic formula** takes a predicate symbol and applies it to a sequence of terms. If P is a unary predicate and t is a term, then P(t) is an atomic formula — the simplest possible claim, asserting that the object denoted by t has property P. If R is a binary predicate and t₁, t₂ are terms, then R(t₁, t₂) says the pair stands in relation R. In arithmetic, x < y and x = y+1 are atomic formulas. Equality is a special built-in binary predicate: t₁ = t₂ asserts the two terms denote the same object.

Atomic formulas are the **base cases** of the inductive definition of formulas. Every compound formula — negations, conjunctions, disjunctions, implications, quantified statements — is built by combining atomic formulas using logical connectives and quantifiers. This means when you evaluate a formula in a structure, you ultimately reduce everything to asking about atomic formulas: does this object satisfy this predicate? Does this pair stand in this relation? Getting the term/atomic formula distinction right is essential before you can study quantifiers, interpret formulas in models, or understand the difference between syntax (the formula itself) and semantics (what it means in a particular structure).
