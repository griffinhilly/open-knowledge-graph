---
id: model-completeness-theorems
title: Model Completeness and the Model Completeness Test
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-theory-basics
  type: hard
- id: first-order-semantics
  type: hard
- id: complete-first-order-theories
  type: hard
builds-toward:
- quantifier-elimination-decidability
- decidable-theories
tags:
- model-completeness
- universal-formulas
- decidability
stage: advanced
status: draft
---

# Model Completeness and the Model Completeness Test

## Core Idea
A theory T is model-complete if every formula is equivalent to a universal formula, equivalently, if every embedding of one model of T into another model of T is an elementary embedding. Model completeness implies that models embed elementarily into larger models. The model completeness test (Tarski's criterion) provides a decidable way to verify this property.

## How It's Best Learned
Study the MCT and work through examples: algebraically closed fields, real closed fields, and divisible abelian groups. Compare model completeness with completeness and saturation.

## Common Misconceptions
Model completeness is not the same as completeness. A model-complete theory need not be complete. Also, model-completeness does not imply all models are isomorphic.

## Explainer

From your prerequisite work, you know that a theory T is **complete** if every sentence is decided — T ⊨ φ or T ⊨ ¬φ for every sentence φ. **Model completeness** is a different, structural property about how models embed into each other. A theory T is model-complete if, whenever M ⊆ N are both models of T (M is a substructure of N), the inclusion is automatically an **elementary embedding** — every first-order sentence with parameters from M has the same truth value in M and in N. Intuitively, extending a model of T never introduces new "first-order facts" about the old elements.

The most important equivalent characterization is the formula-level one: T is model-complete if and only if every formula is equivalent (modulo T) to a **universal formula** — a formula of the form ∀x₁…∀xₙ φ where φ is quantifier-free. The force of this is that existential quantifiers can always be eliminated or replaced. If you can describe any definable property using only "for all," then embedding a model into a larger one cannot "create" new witnesses that change the truth of old statements.

The paradigm examples are **algebraically closed fields** (ACF) and **real closed fields** (RCF). In ACF (the theory of fields like ℂ where every polynomial has a root), if you extend one algebraically closed field to another of the same characteristic, the smaller field is an elementary substructure. The theory ACF is model-complete and, with a fixed characteristic, also complete — so ACF is the cleaner example. RCF (the theory of ordered fields like ℝ where every positive element has a square root and every odd-degree polynomial has a root) is model-complete via Tarski's theorem: every formula in the language of ordered fields is equivalent to a quantifier-free formula, which is an even stronger property called **quantifier elimination**. Quantifier elimination implies model completeness, since quantifier-free formulas are preserved under both extensions and restrictions.

The distinction from completeness is crucial. A model-complete theory can have multiple non-isomorphic models satisfying different sentences: for example, two algebraically closed fields of different transcendence degrees are models of ACF and are not isomorphic, even though the embedding between them is elementary. Model completeness controls the extension relationship between models; completeness controls which sentences the theory decides. These are orthogonal concerns. A theory can be complete but not model-complete (e.g., Presburger arithmetic), model-complete but not complete (some theories with multiple characteristic classes), or both (ACF with fixed characteristic). The **model completeness test** (Robinson's test) gives a practical decision procedure: T is model-complete if and only if for every M ⊆ N ⊨ T, every existential sentence true in N with parameters from M is already true in M. Verifying this for RCF is the key step in Tarski's proof that the first-order theory of the reals is decidable.

