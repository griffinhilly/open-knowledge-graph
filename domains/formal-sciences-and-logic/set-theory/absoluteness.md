---
id: absoluteness
title: Absoluteness
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: independence-results-set-theory
  type: hard
- id: constructible-universe
  type: soft
builds-toward:
- forcing-intro
tags:
- absoluteness
- Δ₁ formulas
- Shoenfield absoluteness
- transitive models
- inner models
stage: formal-systems
status: draft
---

# Absoluteness

## Core Idea
A formula φ is absolute between two models M ⊆ N of set theory if φ holds in M exactly when it holds in N — the truth value does not depend on which model is evaluating it. Δ₁ formulas (those equivalent to both a Σ₁ and a Π₁ formula) are absolute for transitive models: properties like 'x is an ordinal', 'x is a natural number', and 'f is a function' cannot change their truth value when passing between a transitive model and the full universe. Shoenfield's absoluteness theorem extends this dramatically: all Σ¹₂ statements of second-order arithmetic are absolute between V and any inner model containing all countable ordinals. This means many analytic and coanalytic properties of reals are immune to forcing and cannot be shown independent by standard methods.

## How It's Best Learned
Start with concrete examples of absolute and non-absolute notions. 'x is an ordinal' is absolute; 'x is countable' is not (a set can be countable in V but uncountable in an inner model that lacks the witnessing bijection). Prove that bounded quantifier formulas (Δ₀) are absolute for transitive models, then extend to Σ₁ and Δ₁. Finally, state Shoenfield absoluteness and see why it limits what independence proofs can achieve: no Σ¹₂ statement of analysis can be shown independent of ZFC using forcing.

## Common Misconceptions
- Absoluteness does not mean the formula is true — it means its truth value is the same across models. A false absolute statement is still absolute.
- 'x is countable' is the classic non-absolute concept, but this does not mean countability is somehow ill-defined — it just means it depends on what bijections are available in the model.
