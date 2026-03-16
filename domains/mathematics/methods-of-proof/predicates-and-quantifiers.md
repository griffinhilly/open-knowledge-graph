---
id: predicates-and-quantifiers
title: Predicates and Quantifiers
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- negation-of-quantifiers
- direct-proof
tags:
- quantifiers
- predicates
- first-order-logic
stage: formal-systems
status: draft
---

# Predicates and Quantifiers

## Core Idea
A predicate is a statement with variables whose truth depends on variable values. Quantifiers specify scope: ∀ (universal) means all values satisfy the predicate; ∃ (existential) means at least one does. These express mathematical theorems precisely.

## Explainer

The propositional logic you've learned so far deals with statements that have fixed truth values — "Paris is in France" is true, "2 + 2 = 5" is false. But mathematics rarely works with fixed facts alone. Most mathematical claims involve *variables*: "x is even," "n² > 0," "the function f is continuous." These are **predicates** — statement-templates that become true or false only once you substitute a value for the variable. P(x) = "x is even" is neither true nor false until you specify x; P(4) is true, P(7) is false.

To turn a predicate into a definite statement, you need a **quantifier** that says which values of x you mean. The **universal quantifier** ∀ ("for all") produces a claim that holds for every element of the domain: ∀x P(x) asserts that P(x) is true for every x you could substitute. To *prove* a universal claim, you must give an argument that works for an arbitrary x. To *disprove* it, you need only exhibit a single **counterexample** — one value of x for which P(x) is false.

The **existential quantifier** ∃ ("there exists") makes the weaker claim that at least one value works: ∃x P(x) asserts that some specific x makes P(x) true. To *prove* an existential claim, you exhibit a concrete witness. To *disprove* it, you must show P(x) fails for every x — a much harder task. The asymmetry between proving and disproving is opposite for the two quantifiers, and keeping this straight is essential for constructing correct proofs.

Order of quantifiers is critical when multiple quantifiers are nested. Consider "for every ε > 0, there exists δ > 0 such that if |x − a| < δ then |f(x) − L| < ε" — the definition of a limit. The ∀ε ∃δ order means δ is allowed to depend on ε (you choose δ after seeing ε). Reversing to ∃δ ∀ε would mean a single δ works for all ε simultaneously — a far stronger, usually false claim. Reading a statement with nested quantifiers is a skill in itself: track the order, note which variables depend on which, and the logical structure of theorems becomes precise and unambiguous.
