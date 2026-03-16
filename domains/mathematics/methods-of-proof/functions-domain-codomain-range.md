---
id: functions-domain-codomain-range
title: 'Functions: Domain, Codomain, and Range'
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cartesian-products-relations
  type: hard
builds-toward:
- injective-surjective-bijective-functions
- function-composition-and-inverses
tags:
- functions
- domain
- codomain
- range
stage: formal-systems
status: draft
---

# Functions: Domain, Codomain, and Range

## Core Idea
A function f: A → B is a relation where each element of A (the domain) maps to exactly one element of B (the codomain). The range is the set of all elements in B that are actually outputs of f. Distinguishing codomain from range is critical: the codomain is fixed by definition, while the range is determined by which outputs are attained.

## Explainer

You already know that a Cartesian product A × B consists of ordered pairs (a, b), and that a relation is a subset of A × B. A **function** f: A → B is a special kind of relation: one where every element of A appears as the first coordinate of exactly one pair. In other words, every input has exactly one output. What distinguishes a function from a general relation is this uniqueness requirement — no input maps to two different outputs, and no input is left without an output.

The three terms **domain**, **codomain**, and **range** capture different aspects of a function's scope. The domain is the set A of all permitted inputs — the function must be defined on every element of A. The codomain is the set B declared as the target — it is a promise about where outputs land, chosen as part of the function's definition. The range (also called image) is {f(a) : a ∈ A} ⊆ B — the collection of outputs actually produced. The range is always a subset of the codomain, but can be strictly smaller.

The distinction between codomain and range is subtle but critical. Consider f: ℝ → ℝ defined by f(x) = x². The codomain is ℝ (all real numbers), but the range is [0, ∞) — no output is negative. You could alternatively write f: ℝ → [0, ∞), declaring the codomain to be just the nonneg­atives. These are technically different functions even though the formula is identical, because the codomain is part of the function's specification. This matters enormously for **surjectivity**: f is surjective (onto) if and only if every element of the codomain is achieved as an output — i.e., range = codomain. Whether f(x) = x² is surjective depends entirely on the declared codomain.

This framework also clarifies well-definedness. When you define a function by a formula or rule, you must verify: (1) the formula applies to every element of the domain, and (2) each domain element maps to a unique output. In abstract algebra, functions are often defined on equivalence classes, and checking well-definedness — verifying the output doesn't depend on which representative you chose — is a required proof step. The domain-codomain-range framework makes that checklist precise.
