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
status: validated
---

# Absoluteness

## Core Idea
A formula φ is absolute between two models M ⊆ N of set theory if φ holds in M exactly when it holds in N — the truth value does not depend on which model is evaluating it. Δ₁ formulas (those equivalent to both a Σ₁ and a Π₁ formula) are absolute for transitive models: properties like 'x is an ordinal', 'x is a natural number', and 'f is a function' cannot change their truth value when passing between a transitive model and the full universe. Shoenfield's absoluteness theorem extends this dramatically: all Σ¹₂ statements of second-order arithmetic are absolute between V and any inner model containing all countable ordinals. This means many analytic and coanalytic properties of reals are immune to forcing and cannot be shown independent by standard methods.

## How It's Best Learned
Start with concrete examples of absolute and non-absolute notions. 'x is an ordinal' is absolute; 'x is countable' is not (a set can be countable in V but uncountable in an inner model that lacks the witnessing bijection). Prove that bounded quantifier formulas (Δ₀) are absolute for transitive models, then extend to Σ₁ and Δ₁. Finally, state Shoenfield absoluteness and see why it limits what independence proofs can achieve: no Σ¹₂ statement of analysis can be shown independent of ZFC using forcing.

## Common Misconceptions
- Absoluteness does not mean the formula is true — it means its truth value is the same across models. A false absolute statement is still absolute.
- 'x is countable' is the classic non-absolute concept, but this does not mean countability is somehow ill-defined — it just means it depends on what bijections are available in the model.

## Questions

```yaml
- question: "In the universe V of all sets, set S is countable — there exists a bijection f: S → ω. Now consider a transitive inner model M ⊆ V that happens to not contain f. What is S's status in M?"
  type: multiple-choice
  options:
    - "S remains countable in M, because countability is an absolute property preserved in all transitive models"
    - "S may be uncountable in M, because M lacks the witnessing bijection and cannot verify countability"
    - "S does not exist in M, since sets with missing witnesses are removed from inner models"
    - "S is countable in M if and only if S is finite — infinite countable sets lose countability in inner models"
  answer: 1
  explanation: "Countability is not absolute. To say 'S is countable in M' means: there exists a bijection from S to ω *in M*. If M lacks the bijection f (even though it exists in V), M has no witness to S's countability and will declare S uncountable. This is the standard example of a non-absolute notion: 'x is countable' is Σ₁ (there exists a bijection), and Σ₁ statements are upward absolute (true in M implies true in V) but not downward absolute (true in V does not imply true in M). Forcing exploits this by deliberately adding or removing bijections to change what is 'countable.'"

- question: "Which of the following set-theoretic notions is ABSOLUTE for all transitive models of ZF?"
  type: multiple-choice
  options:
    - "x is a countable set"
    - "x is an ordinal"
    - "x has cardinality ℵ₁"
    - "x is a real number that codes a well-ordering of ω"
  answer: 1
  explanation: "'x is an ordinal' is Δ₁ (equivalent to both a Σ₁ and a Π₁ definition), hence absolute for all transitive models. An ordinal is a transitive set well-ordered by membership, and checking this only requires quantifying over elements of x — bounded quantification that transitive models can evaluate locally. 'x is countable' requires an existential quantifier ranging over bijections that may not exist in the model. 'Cardinality ℵ₁' depends on what bijections are available. 'Codes a well-ordering' is more complex and not straightforwardly absolute."

- question: "If a formula φ is absolute between transitive models M and N (with M ⊆ N), then φ is expected to be true in both M and N."
  type: true-false
  answer: false
  explanation: "This is one of the key misconceptions about absoluteness. Absolute means the truth value is the SAME in both models — φ holds in M iff it holds in N. A false formula can be absolute: 'x is an ordinal' is absolute, but a specific set x might fail to be an ordinal in both M and N equally. Absoluteness is about model-independence of truth evaluation, not about the truth value being 'true.' A statement like '0 = 1' is trivially absolute (false in all models) even though it is never true."

- question: "Shoenfield's absoluteness theorem implies that whether a real number has a certain Σ¹₂ property cannot be made to depend on which forcing extension of ZFC you work in."
  type: true-false
  answer: true
  explanation: "Shoenfield's theorem states that Σ¹₂ (and Π¹₂) statements of second-order arithmetic are absolute between the universe V and any inner model containing all countable ordinals — in particular, between V and any forcing extension. Since Σ¹₂ statements depend only on countable objects and countable ordinals, and forcing extensions agree with the ground model on all countable ordinals, the truth value of any Σ¹₂ statement is unchanged by forcing. This means no Σ¹₂ statement can be shown independent of ZFC using forcing — providing a firm boundary on what independence results are achievable by the main technique of modern set theory."

- question: "Why is 'x is countable' not absolute between a transitive inner model M and the full universe V, even though countability is a perfectly rigorous mathematical property?"
  type: short-answer
  answer: "Countability of x means: there exists a bijection f: x → ω. That bijection must exist *in the model being evaluated*. An inner model M ⊆ V may be 'missing' certain bijections that exist in V — especially after a forcing construction that adds new functions. If M lacks the witnessing bijection for x, M cannot verify x's countability and will declare x uncountable, even though V knows x is countable. The mathematical definition is rigorous, but its truth depends on which functions are available as witnesses, and different models have different function inventories."
  explanation: "This points to the heart of why set theory has genuine model-dependence. Statements with existential quantifiers ranging over all functions (not just functions of elements of x) are sensitive to the ambient universe. 'x is countable' is Σ₁ — one unbounded existential quantifier. Such statements are upward absolute: if M thinks x is countable, V does too (V has at least as many bijections as M). But they are not downward absolute. The classic slogan: 'An uncountable set in M might be countable from the outside' — meaning from V's perspective — is a precise theorem, not a paradox."
```

## Explainer

From your study of independence results, you know that set theory has models — the same axioms can be satisfied by different mathematical universes. Two models M and N (with M ⊆ N) may disagree about the truth of statements: a sentence true in M might be false in N. This is disturbing if you think of M and N as "the same sets" — but they are not the same universe, and each evaluates formulas in its own domain. **Absoluteness** is the study of which properties are immune to this model-dependence.

The cleanest example is **Δ₀ absoluteness**. A **Δ₀ formula** (also called bounded) is one where all quantifiers are restricted: instead of ∀x, you write ∀x ∈ y (for all x that are elements of y). Such formulas only quantify over elements of things already in scope, so their truth can be checked by looking "inside" the sets present in the model. If M is a transitive model (closed under membership: x ∈ y ∈ M → x ∈ M), then a Δ₀ formula φ(a) is absolute between M and V: φ(a) holds in M iff it holds in V. Properties like "x is an ordered pair," "f is a function with domain d," and "x is an ordinal" are all Δ₀ or Δ₁ (provably equivalent to both a Σ₁ and a Π₁ formula), hence absolute for transitive models.

By contrast, **"x is countable"** is the archetypal non-absolute notion. Countability means "there exists a bijection between x and ω." That bijection must exist *in the model*. An inner model M might be missing many bijections that exist in V — in fact, forcing constructions deliberately add new bijections to make previously "uncountable" sets become countable. So ℵ₁^M (what M thinks is the first uncountable cardinal) might be countable from V's perspective. The formula ∃f (f is a bijection from x to ω) is Σ₁, and Σ₁ formulas are upward absolute (if true in M, they remain true in any extension N ⊇ M) but not downward absolute. "x is uncountable" is Π₁, hence downward absolute but not upward — the exact mirror.

**Shoenfield's absoluteness theorem** dramatically extends these observations. It states that all **Σ¹₂** statements of second-order arithmetic — formulas of the form ∃f ∀g φ(f, g) where f, g range over real numbers and φ is arithmetic — are absolute between V and any inner model containing all the countable ordinals (in particular, between V and L, and between V and any forcing extension). This means that many of the central problems of descriptive set theory — the Borel and analytic sets — cannot be shown independent of ZFC by forcing. Forcing changes which reals exist, but it cannot change which Σ¹₂ statements hold, because those statements only depend on countable objects, and forcing extensions agree with V on all countable ordinals. Absoluteness thus draws a sharp line: below Σ¹₂ the set-theoretic universe is rigid; above it, independence results become possible.
