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
stage: advanced
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

## Explainer

From your study of independence results, you know that set theory has models — the same axioms can be satisfied by different mathematical universes. Two models M and N (with M ⊆ N) may disagree about the truth of statements: a sentence true in M might be false in N. This is disturbing if you think of M and N as "the same sets" — but they are not the same universe, and each evaluates formulas in its own domain. **Absoluteness** is the study of which properties are immune to this model-dependence.

The cleanest example is **Δ₀ absoluteness**. A **Δ₀ formula** (also called bounded) is one where all quantifiers are restricted: instead of ∀x, you write ∀x ∈ y (for all x that are elements of y). Such formulas only quantify over elements of things already in scope, so their truth can be checked by looking "inside" the sets present in the model. If M is a transitive model (closed under membership: x ∈ y ∈ M → x ∈ M), then a Δ₀ formula φ(a) is absolute between M and V: φ(a) holds in M iff it holds in V. Properties like "x is an ordered pair," "f is a function with domain d," and "x is an ordinal" are all Δ₀ or Δ₁ (provably equivalent to both a Σ₁ and a Π₁ formula), hence absolute for transitive models.

By contrast, **"x is countable"** is the archetypal non-absolute notion. Countability means "there exists a bijection between x and ω." That bijection must exist *in the model*. An inner model M might be missing many bijections that exist in V — in fact, forcing constructions deliberately add new bijections to make previously "uncountable" sets become countable. So ℵ₁^M (what M thinks is the first uncountable cardinal) might be countable from V's perspective. The formula ∃f (f is a bijection from x to ω) is Σ₁, and Σ₁ formulas are upward absolute (if true in M, they remain true in any extension N ⊇ M) but not downward absolute. "x is uncountable" is Π₁, hence downward absolute but not upward — the exact mirror.

**Shoenfield's absoluteness theorem** dramatically extends these observations. It states that all **Σ¹₂** statements of second-order arithmetic — formulas of the form ∃f ∀g φ(f, g) where f, g range over real numbers and φ is arithmetic — are absolute between V and any inner model containing all the countable ordinals (in particular, between V and L, and between V and any forcing extension). This means that many of the central problems of descriptive set theory — the Borel and analytic sets — cannot be shown independent of ZFC by forcing. Forcing changes which reals exist, but it cannot change which Σ¹₂ statements hold, because those statements only depend on countable objects, and forcing extensions agree with V on all countable ordinals. Absoluteness thus draws a sharp line: below Σ¹₂ the set-theoretic universe is rigid; above it, independence results become possible.
