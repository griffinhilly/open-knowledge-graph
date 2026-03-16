---
id: functions-and-mappings-formal
title: 'Functions and Mappings: Formal Definition'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: relations-as-set-subsets
  type: hard
builds-toward:
- injections-surjections-bijections-classification
tags:
- functions
- mappings
- domain-codomain-range
stage: formal-systems
status: draft
---

# Functions and Mappings: Formal Definition

## Core Idea
A function f: A → B is a relation from A to B where each element of A is paired with exactly one element of B. This definition generalizes functions beyond real arithmetic to arbitrary sets. The domain A and codomain B are essential parts of the definition; the range is the set of all actual outputs f(A).

## Explainer

You already know that a relation from A to B is a subset of the Cartesian product A × B — a collection of ordered pairs (a, b) where a ∈ A and b ∈ B. A **function** f: A → B is a relation with two additional constraints: it is **total** (every element of A appears as a first coordinate) and **single-valued** (no element of A appears as a first coordinate more than once). In other words, for every a ∈ A there exists *exactly one* b ∈ B such that (a, b) ∈ f. Writing "f(a) = b" is shorthand for "(a, b) ∈ f." This is the set-theoretic definition of function — a function *is* a set of ordered pairs satisfying these two conditions.

The distinction between **domain**, **codomain**, and **range** is essential and often confused. The domain A is the set of all inputs — every element of A must have an output. The codomain B is the declared "output type" — it is part of the specification of f and need not equal the set of actual outputs. The **range** (or image) f(A) = {f(a) : a ∈ A} is the set of values that f actually takes; it is a subset of B, but may be a proper subset. For example, the function f: ℝ → ℝ defined by f(x) = x² has domain ℝ, codomain ℝ, and range [0, ∞) ⊊ ℝ. Changing the codomain to [0, ∞) gives a *different function* — same rule, different specification — even though the rule and range are identical.

Why define functions as sets of pairs rather than as "rules"? The set-theoretic definition is required for rigor in contexts where "rule" is ambiguous or where functions are constructed by set operations. For instance, the axiom of choice constructs functions whose rule cannot be written down explicitly; the set-of-pairs definition handles these without awkwardness. It also makes function equality precise: two functions f and g from A to B are equal iff they have the same graph — the same set of pairs — regardless of how they are described. This extensional notion of equality is fundamental: f(x) = x + 1 − 1 and g(x) = x are the *same* function from ℤ to ℤ.

This formal definition generalizes immediately to arbitrary sets, not just number systems. Functions between finite sets (used in combinatorics and group theory), functions between sets of strings (formal language theory), and functions between structures (homomorphisms in algebra) all fall under the same definition. The building blocks — total, single-valued relations — extend naturally to **partial functions** (drop totality) and **multivalued functions** (drop single-valuedness), which arise in computability theory and analysis. Mastering the formal definition of function here is the foundation for all of these, and for the classification of functions as injective, surjective, or bijective that follows immediately from it.
