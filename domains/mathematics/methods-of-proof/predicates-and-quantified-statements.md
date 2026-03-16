---
id: predicates-and-quantified-statements
title: Predicates and Quantified Statements
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-values-and-statements
  type: hard
builds-toward:
- universal-quantifier-introduction
- existential-quantifier-introduction
tags:
- logic
- predicates
- quantifiers
- variables
stage: formal-systems
status: draft
---

# Predicates and Quantified Statements

## Core Idea
A predicate is a statement containing variables that becomes true or false when values are substituted for the variables (e.g., 'x > 5'). Quantifiers bind variables: the universal quantifier ∀ means 'for all', and the existential quantifier ∃ means 'there exists'. These are essential for expressing mathematical claims about sets.

## How It's Best Learned
Translate between verbal and symbolic forms. Practice with concrete examples showing how substituting values makes a predicate true or false. Understand that without quantifiers, predicates with free variables are neither true nor false.

## Common Misconceptions
- Treating a predicate with a free variable as a statement.
- Confusing the order of quantifiers (∀∃ vs. ∃∀ have different meanings).
- Thinking quantifiers distribute over all logical connectives (they don't always).

## Explainer

A **predicate** is a sentence with a variable hole in it. "x > 5" is a predicate: plug in x = 7 and you get a true statement; plug in x = 3 and you get a false one. With a free variable, the predicate itself is neither true nor false — it is a function waiting for input. This is the key distinction between a predicate and a statement. From your work with truth values and statements, you know that statements have definite truth values. Predicates only become statements when their variables are bound — either by substitution or by quantifiers.

**Quantifiers** do the binding. The **universal quantifier** ∀ means "for all." The sentence ∀x, P(x) claims that P(x) is true for every x in the domain. The **existential quantifier** ∃ means "there exists." The sentence ∃x, P(x) claims that at least one x in the domain makes P(x) true. Together, these two quantifiers are the basic vocabulary for expressing mathematical claims: "every even number has a square that is even" is ∀n, if n is even then n² is even; "some prime is even" is ∃p, p is prime and p is even.

The domain of discourse matters enormously. ∀x, x > 0 is true if the domain is the positive integers, false if the domain is all integers. Always ask: quantifying over what? In a proof, you must fix the domain clearly before interpreting a quantified statement. Negating a quantified statement flips the quantifier and negates the body: the negation of ∀x, P(x) is ∃x, ¬P(x), and the negation of ∃x, P(x) is ∀x, ¬P(x). This is one of the most important rules in proof-writing — to prove "not all x have property P," you just find one counterexample.

The order of quantifiers is critical when multiple quantifiers appear. ∀x ∃y, y > x (for every x, there exists a y larger than it) is a true statement about the integers — just take y = x + 1. But ∃y ∀x, y > x (there exists a y larger than all x) is false — no integer is larger than every integer. The order ∀∃ says "for each x you give me, I can find a y"; the order ∃∀ says "I can find one y that works for every x simultaneously." These are profoundly different claims, and swapping quantifiers changes the meaning in ways that will matter throughout real analysis, topology, and any subject that reasons about limits and convergence.
