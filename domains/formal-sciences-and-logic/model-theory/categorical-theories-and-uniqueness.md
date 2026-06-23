---
id: categorical-theories-and-uniqueness
title: Categorical Theories and Uniqueness of Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: elementary-equivalence-indistinguishability
  type: hard
- id: infinite-cardinal-numbers
  type: soft
- id: cardinality-and-countability
  type: soft
- id: lowenheim-skolem-upward
  type: hard
builds-toward:
- morleys-uncountable-categoricity
tags:
- κ-categorical
- categoricity spectrum
- uniqueness
- rigid theory
stage: expert
status: validated
---

# Categorical Theories and Uniqueness of Models

## Core Idea
A complete theory T is κ-categorical if it has exactly one model of cardinality κ up to isomorphism. Categoricity captures that T completely determines model structure at a specific size. The spectrum of cardinalities where a theory is categorical is highly constrained: Morley proved surprising rigidity—if T is categorical in some uncountable κ, it is categorical in all uncountable cardinalities.

## Questions

```yaml
- question: "A student argues: 'DLO is ℵ₀-categorical, so by Morley's theorem it must be categorical in all uncountable cardinalities too.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "DLO is not a complete theory, so Morley's theorem doesn't apply"
    - "Morley's theorem runs in the other direction: categoricity in some uncountable cardinal implies categoricity in all uncountable cardinals — it says nothing about ℵ₀-categoricity"
    - "DLO actually is categorical in all uncountable cardinalities; the student is correct"
    - "Morley's theorem only applies to theories with finite models"
  answer: 1
  explanation: "Morley's theorem states: if T is categorical in some *uncountable* cardinality, it is categorical in all uncountable cardinalities. It does not run from ℵ₀ upward. DLO is ℵ₀-categorical (the back-and-forth argument works at ω), but uncountable dense linear orders can differ in cofinality and Dedekind completeness, so DLO has many non-isomorphic uncountable models. Morley's theorem simply does not apply here."

- question: "A complete theory T in a countable language is known to be categorical in ℵ₃. Which of the following must be true?"
  type: multiple-choice
  options:
    - "T is also ℵ₀-categorical"
    - "T is categorical in every uncountable cardinality"
    - "T has exactly one model of every infinite cardinality"
    - "T is categorical in ℵ₂ but not necessarily ℵ₄"
  answer: 1
  explanation: "By Morley's theorem, categoricity in any uncountable cardinal propagates to all uncountable cardinals. So knowing T is categorical in ℵ₃ immediately gives categoricity in ℵ₁, ℵ₂, ℵ₄, and every other uncountable cardinal. However, this says nothing about ℵ₀: a theory can be categorical in all uncountable cardinals while still having multiple countable models (or none, or one). The theory of algebraically closed fields of fixed characteristic exemplifies this."

- question: "A κ-categorical theory can have two non-isomorphic models of cardinality κ, provided they satisfy the same sentences."
  type: true-false
  answer: false
  explanation: "This directly contradicts the definition. κ-categoricity means there is exactly *one* model of cardinality κ up to isomorphism — any two models of that cardinality must be isomorphic. Elementary equivalence (satisfying the same sentences) is weaker than isomorphism. Categoricity is precisely the condition that collapses the distinction: at cardinality κ, elementary equivalence implies isomorphism."

- question: "The theory of algebraically closed fields of characteristic 0 (ACF₀) is categorical in every uncountable cardinality."
  type: true-false
  answer: true
  explanation: "ACF₀ is the canonical example of a Morley-categorical theory. Any two algebraically closed fields of characteristic 0 with the same uncountable cardinality are isomorphic — the cardinality alone determines the transcendence degree over ℚ, and transcendence degree characterizes the field up to isomorphism. This also illustrates Morley's theorem: ACF₀ is categorical in ℵ₁, ℵ₂, and every larger cardinal simultaneously."

- question: "What does the back-and-forth argument prove about DLO (the theory of dense linear orders without endpoints), and why does it fail at uncountable cardinalities?"
  type: short-answer
  answer: "The back-and-forth argument proves DLO is ℵ₀-categorical: any two countable dense linear orders without endpoints are isomorphic to each other (and to ℚ). At each step, you extend a partial isomorphism by one element, using density and the absence of endpoints to guarantee a matching element exists in the other structure. At uncountable cardinalities, the argument breaks down because uncountable dense linear orders can differ in cofinality (whether they have a cofinal ω-sequence) and whether they are Dedekind complete — structural properties that density and no-endpoints alone do not pin down, producing genuinely non-isomorphic uncountable models."
  explanation: "The key is that the back-and-forth argument is constructive and countable: it builds an isomorphism in countably many steps, matching one element at a time. This works perfectly at ω because density always supplies a matching point. At uncountable cardinalities, however, there are uncountable many points to match and the local density property is no longer enough to control global structure. Cofinality and completeness become independent degrees of freedom, allowing genuinely distinct models."
```

## Explainer

From your study of elementary equivalence, you know that two structures can satisfy exactly the same first-order sentences without being isomorphic—think of (ℕ, <) and a non-standard model of arithmetic that agrees with ℕ on every first-order sentence yet contains infinite elements. **κ-categoricity** asks whether there is a cardinality κ at which the theory rules out any such structural variation: if T is κ-categorical, any two models of T with cardinality κ are isomorphic. The theory determines the model uniquely at that size.

The canonical example is **DLO**, the theory of dense linear orders without endpoints—the first-order theory of (ℚ, <). This theory is ℵ₀-categorical: every countable dense linear order without endpoints is isomorphic to ℚ. The proof uses a **back-and-forth argument**, building an isomorphism incrementally by alternately extending it to cover one new element from each structure. Density and the absence of endpoints ensure you can always find an appropriate match. However, DLO is not κ-categorical for any uncountable κ: uncountable dense linear orders can differ in cofinality and whether they are Dedekind complete, producing genuinely non-isomorphic models of the same size.

**Morley's theorem** (1965) reveals a striking rigidity for uncountable categoricity: if a complete theory T in a countable language is categorical in *any* uncountable cardinality, it is categorical in *all* uncountable cardinalities. This was unexpected because uncountable cardinals are wildly diverse in size. The explanation lies in structural properties the theory must possess: it must be **totally transcendental**, must have a well-behaved notion of algebraic independence (generalizing linear independence in vector spaces), and models must be characterized entirely by a single "dimension." The theory of algebraically closed fields of fixed characteristic illustrates this: it is categorical in every uncountable cardinality (and also ℵ₁-categorical, since the algebraic closure of ℚ is countable while uncountable algebraically closed fields of characteristic 0 all look alike at each uncountable size).

Categoricity is ultimately a measure of how tightly a theory pins down structure. A κ-categorical theory leaves no freedom at cardinality κ—it is, in a precise sense, complete about models of that size. Non-categorical theories have multiple non-isomorphic models of the same infinite size, meaning the theory is "weaker" and cannot distinguish between structurally different possibilities. The spectrum of theories ranging from categorical to maximally non-categorical is a central organizing theme of modern model theory, and Morley's theorem is the founding result of that classification program.
