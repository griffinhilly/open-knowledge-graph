---
id: quantifier-notation-and-basics
title: Quantifier Notation and Basic Semantics
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: predicates-and-relations-fol
  type: hard
- id: set-fundamentals
  type: hard
- id: set-operations
  type: hard
- id: domain-and-range
  type: soft
- id: set-membership-and-notation
  type: soft
builds-toward:
- universal-quantifier-semantics
- existential-quantifier-semantics
- free-variables-and-bound-variables
tags:
- syntax
- semantics
- quantifiers
stage: formal-systems
status: draft
---

# Quantifier Notation and Basic Semantics

## Core Idea
The universal quantifier ∀ (for all) and existential quantifier ∃ (there exists) express generality and existence. ∀x P(x) means 'for every object x, P holds'; ∃x P(x) means 'there is at least one object x for which P holds'. Quantifiers bind variables and determine scope.

## How It's Best Learned
Translate between English phrases ('all dogs bark', 'some cats are black') and formal quantified formulas. Practice recognizing quantifier scope and how scope affects meaning.

## Explainer

You already know what a predicate is: a property P(x) that is either true or false for each object x in some domain. Predicates by themselves make claims about specific objects — P(alice) says Alice has property P. Quantifiers lift this to claims about *all* or *some* objects in the domain at once, without naming any of them.

The **universal quantifier** ∀ is a logical "for all." The formula ∀x P(x) means: pick any object x from the domain — P holds. It is equivalent to the conjunction of P over every element, but without having to enumerate them. If your domain is the integers, ∀x (x + 0 = x) says that adding zero is a right identity for every integer. The connection to sets you already know: ∀x P(x) is true in a domain D precisely when the extension of P — the set {x ∈ D : P(x)} — equals the entire domain D.

The **existential quantifier** ∃ is the logical "there exists." The formula ∃x P(x) means: at least one object in the domain satisfies P. It is the disjunction of P over every element. If your domain is the integers, ∃x (x² = 2) is false over the integers (no integer squares to 2) but true over the reals. Notice that the *same sentence* changes truth value when the domain changes — quantifiers always range over a specific **domain of discourse**, and specifying that domain is part of giving a formula a meaning.

**Scope** and **variable binding** are the subtlest aspects. In ∀x (P(x) → ∃y Q(x, y)), the variable x is bound by the universal quantifier and y is bound by the existential. A bound variable is just a placeholder: ∀x P(x) and ∀z P(z) say exactly the same thing. A **free variable** — one not bound by any quantifier — makes a formula act like a predicate: it is true or false depending on what value you assign to the free variable. The formula P(x) with free x is open; ∀x P(x) closes it. Quantifier order matters crucially for nested quantifiers: ∀x ∃y (y > x) says "for every number there is a larger one" (true of the integers), while ∃y ∀x (y > x) says "there is a number larger than all numbers" (false). The swap changes the claim entirely.
