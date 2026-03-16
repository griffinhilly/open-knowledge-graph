---
id: predicates-and-quantifiers-intro
title: Predicates and Quantifiers
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- negation-of-quantified-statements
- set-fundamentals
tags:
- logic
- predicates
- quantifiers
stage: formal-systems
status: draft
---

# Predicates and Quantifiers

## Core Idea
A predicate is a statement involving a variable that becomes true or false based on the variable's value. The universal quantifier 'for all' (∀) and existential quantifier 'there exists' (∃) specify how claims about predicates apply to sets of objects. These tools formalize statements about entire domains precisely and are indispensable for mathematical discourse.

## Explainer

In propositional logic — your prerequisite — every statement has a fixed truth value. "It is raining" is either true or false as a whole. But most interesting mathematical statements aren't like that: "n is even," "x² > 0," and "f is continuous" are neither true nor false on their own. They are **predicates**: statements whose truth depends on the value of one or more variables. Write P(n) for "n is even"; then P(2) is true and P(3) is false. A predicate is like a function from a domain of objects to {true, false}.

Predicates become full propositions — statements with definite truth values — when you **bind the variables** using quantifiers. The **universal quantifier** ∀ asserts that a predicate is true for every element in the domain: ∀n ∈ ℤ, (n is even or n is odd) is a true proposition. The **existential quantifier** ∃ asserts that at least one element satisfies the predicate: ∃n ∈ ℤ, n² = 4 is also true (take n = 2 or n = −2). Notice that neither quantifier tells you *which* element witnesses the existential — just that one exists. To prove ∀x P(x) you must show P holds for an arbitrary x; to prove ∃x P(x) you typically exhibit a specific x.

A single predicate can carry multiple variables, and **nested quantifiers** apply them one at a time. ∀x ∃y, y > x says "for every x, there is some y larger than it" — true over the integers (take y = x + 1). But ∃y ∀x, y > x says "there is some y larger than every x" — false over the integers (no largest integer exists). Swapping ∀ and ∃ can change a true statement to a false one. The order of unlike quantifiers is crucial and is one of the most common sources of logical error in beginning proof-writing.

Negating quantified statements follows precise rules that are the logical analog of De Morgan's laws. The negation of ∀x P(x) is ∃x ¬P(x): "not all x satisfy P" means "there is some x that does not." The negation of ∃x P(x) is ∀x ¬P(x): "there is no x satisfying P" means "all x fail P." These rules nest: negating ∀x ∃y P(x, y) gives ∃x ∀y ¬P(x, y). Every quantifier flips, every connective follows De Morgan, and all the variable bindings stay in place. Mastering negation of quantified statements is essential — every proof by contradiction and every counterexample argument starts by correctly negating the claim you're trying to disprove.
