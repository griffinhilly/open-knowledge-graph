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
stage: expert
status: validated
---

# Model Completeness and the Model Completeness Test

## Core Idea
A theory T is model-complete if every formula is equivalent to a universal formula, equivalently, if every embedding of one model of T into another model of T is an elementary embedding. Model completeness implies that models embed elementarily into larger models. The model completeness test (Tarski's criterion) provides a decidable way to verify this property.

## How It's Best Learned
Study the MCT and work through examples: algebraically closed fields, real closed fields, and divisible abelian groups. Compare model completeness with completeness and saturation.

## Common Misconceptions
Model completeness is not the same as completeness. A model-complete theory need not be complete. Also, model-completeness does not imply all models are isomorphic.

## Questions

```yaml
- question: "A theory T is model-complete. What can you directly conclude?"
  type: multiple-choice
  options:
    - "Every model of T satisfies exactly the same sentences — T decides every sentence"
    - "Every embedding of one model of T into another is an elementary embedding"
    - "All models of T are isomorphic to each other"
    - "T is complete and has quantifier elimination"
  answer: 1
  explanation: "Model completeness means precisely that every embedding between models of T is elementary — the submodel and the extending model agree on all first-order sentences with parameters from the submodel. Option A describes completeness (a different property). Option C would follow only if T were also categorical. Option D conflates model completeness with the stronger property of quantifier elimination, which implies model completeness but is not equivalent to it."

- question: "You are trying to determine whether a theory T is model-complete. You verify that for every pair of models M ⊆ N of T, every existential sentence with parameters from M that is true in N is already true in M. What have you established?"
  type: multiple-choice
  options:
    - "T is complete — it decides every sentence"
    - "T is model-complete by Robinson's test"
    - "T admits quantifier elimination"
    - "All models of T are elementarily equivalent"
  answer: 1
  explanation: "This is Robinson's model completeness test: T is model-complete if and only if for every M ⊆ N ⊨ T, every existential sentence true in N with parameters from M is already true in M. The test checks whether extending a model can 'create' new witnesses for existential claims about old elements — if not, embeddings are elementary. This does not establish completeness (option A), which requires T to decide every sentence outright, nor quantifier elimination (option C), which is a stronger property."

- question: "A model-complete theory must be complete — if every embedding between its models is elementary, then all its models satisfy the same sentences."
  type: true-false
  answer: false
  explanation: "Model completeness and completeness are independent properties. Model completeness governs how models extend each other (embeddings are elementary), while completeness means the theory decides every sentence (T ⊨ φ or T ⊨ ¬φ for all φ). Algebraically closed fields of different transcendence degrees are models of ACF (fixed characteristic) that are not isomorphic, and ACF is model-complete. However, without fixing the characteristic, ACF has models of different characteristics satisfying different sentences — so the theory without a fixed characteristic is model-complete but not complete."

- question: "If T is model-complete, then every formula is equivalent modulo T to a universal formula (one using only universal quantifiers over a quantifier-free matrix)."
  type: true-false
  answer: true
  explanation: "This is one of the central equivalent characterizations of model completeness. Universal formulas are preserved under passing to substructures, and if every formula is universally equivalent, then embeddings automatically preserve all formulas in both directions — exactly the condition for being elementary. This equivalence is what makes model completeness analyzable at the formula level: you do not need to check all embeddings directly if you can show every definable property is universally expressible."

- question: "What is the key distinction between a theory being 'model-complete' and being 'complete,' and why does the example of algebraically closed fields illustrate the difference?"
  type: short-answer
  answer: "A complete theory decides every sentence (for every φ, either T ⊨ φ or T ⊨ ¬φ), while a model-complete theory only guarantees that embeddings between its models are elementary. ACF without a specified characteristic is model-complete — any embedding of one algebraically closed field into another is elementary — but it is not complete, because models of characteristic 0 (like ℂ) and characteristic p satisfy different sentences. Fixing the characteristic (ACF_p) makes it both complete and model-complete."
  explanation: "The confusion arises because both properties use the word 'complete,' but they describe different structural features. Completeness is a property of the theory's deductive power over sentences; model completeness is a property of how models relate under embedding. A theory can have either, both, or neither. ACF_p (fixed characteristic) has both; Presburger arithmetic is complete but not model-complete; some theories are model-complete but have multiple incompatible completions."
```

## Explainer

From your prerequisite work, you know that a theory T is **complete** if every sentence is decided — T ⊨ φ or T ⊨ ¬φ for every sentence φ. **Model completeness** is a different, structural property about how models embed into each other. A theory T is model-complete if, whenever M ⊆ N are both models of T (M is a substructure of N), the inclusion is automatically an **elementary embedding** — every first-order sentence with parameters from M has the same truth value in M and in N. Intuitively, extending a model of T never introduces new "first-order facts" about the old elements.

The most important equivalent characterization is the formula-level one: T is model-complete if and only if every formula is equivalent (modulo T) to a **universal formula** — a formula of the form ∀x₁…∀xₙ φ where φ is quantifier-free. The force of this is that existential quantifiers can always be eliminated or replaced. If you can describe any definable property using only "for all," then embedding a model into a larger one cannot "create" new witnesses that change the truth of old statements.

The paradigm examples are **algebraically closed fields** (ACF) and **real closed fields** (RCF). In ACF (the theory of fields like ℂ where every polynomial has a root), if you extend one algebraically closed field to another of the same characteristic, the smaller field is an elementary substructure. The theory ACF is model-complete and, with a fixed characteristic, also complete — so ACF is the cleaner example. RCF (the theory of ordered fields like ℝ where every positive element has a square root and every odd-degree polynomial has a root) is model-complete via Tarski's theorem: every formula in the language of ordered fields is equivalent to a quantifier-free formula, which is an even stronger property called **quantifier elimination**. Quantifier elimination implies model completeness, since quantifier-free formulas are preserved under both extensions and restrictions.

The distinction from completeness is crucial. A model-complete theory can have multiple non-isomorphic models satisfying different sentences: for example, two algebraically closed fields of different transcendence degrees are models of ACF and are not isomorphic, even though the embedding between them is elementary. Model completeness controls the extension relationship between models; completeness controls which sentences the theory decides. These are orthogonal concerns. A theory can be complete but not model-complete (e.g., Presburger arithmetic), model-complete but not complete (some theories with multiple characteristic classes), or both (ACF with fixed characteristic). The **model completeness test** (Robinson's test) gives a practical decision procedure: T is model-complete if and only if for every M ⊆ N ⊨ T, every existential sentence true in N with parameters from M is already true in M. Verifying this for RCF is the key step in Tarski's proof that the first-order theory of the reals is decidable.

