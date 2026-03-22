---
id: type-realization-and-omission
title: Type Realization and Omission
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: type-spaces-and-stone-topology
  type: hard
builds-toward:
- omitting-types-theorem-countable
- saturated-models-and-realization
tags:
- realization
- omission
- realizes type
- completeness
stage: advanced
status: draft
---

# Type Realization and Omission

## Core Idea
A model M realizes a type p if there exists an n-tuple a in M such that every formula in p is satisfied by a; it omits p if no such n-tuple exists. Realizability measures how 'complete' a model is: saturated models realize many types. Omitting types allows construction of models with prescribed gaps. The tension between realization and omission drives the study of saturation.

## Questions

```yaml
- question: "Consider the type p(x) = {x > 0, x > 1, x > 2, x > 3, …} in Peano arithmetic — the type of an element larger than every standard natural number. Which claim is correct?"
  type: multiple-choice
  options:
    - "This type is inconsistent with PA, because the axioms imply no element can exceed every natural number"
    - "This type is consistent (every finite subset is satisfied in ℕ by some large standard number) but omitted by the standard model ℕ; a nonstandard model of PA realizes it"
    - "This type is realized in ℕ because infinity (ω) is an element of the standard model"
    - "This type is isolated by the formula 'x is infinite,' so the Omitting Types Theorem guarantees it cannot be omitted from any model"
  answer: 1
  explanation: "Every finite subset {x > 0, …, x > n} is satisfied in ℕ — just take any k > n. So the type is finitely satisfiable and hence consistent with PA. But ℕ has no element that simultaneously exceeds every natural number, so ℕ omits the type. Nonstandard models contain 'infinite' elements that do realize it. This illustrates the central gap: consistency (no finite contradiction) does not guarantee realization in every model."

- question: "A κ-saturated model is best characterized as:"
  type: multiple-choice
  options:
    - "A model with exactly κ elements satisfying every sentence of the theory"
    - "A model that realizes every type over every parameter set of cardinality less than κ that is consistent with the theory — making it maximally 'rich' in witnesses"
    - "A model in which every definable set has cardinality at most κ"
    - "A model with κ many automorphisms, reflecting internal symmetry"
  answer: 1
  explanation: "κ-saturation is a maximality condition on type realization: the model contains a witness for every consistent description of an element using fewer than κ parameters. Saturated models are 'rich' in the sense that nothing consistent is missing. This richness has structural consequences: any two saturated models of the same complete theory of the same cardinality are isomorphic, and automorphisms can be built by back-and-forth arguments extending finite partial maps."

- question: "A type can be consistent with a complete theory T and yet be omitted by some model of T — the same type may be realized in one model of T and absent from another model of T."
  type: true-false
  answer: true
  explanation: "This is the central insight of type realization and omission. Completeness of T means T decides every sentence — there is no sentence left undetermined. But it does not mean all models are isomorphic (that would be categoricity, a much stronger property). The standard model ℕ and a nonstandard model both satisfy the complete theory of PA, yet they realize different types. Two models of the same complete theory can differ profoundly in which types they contain."

- question: "If a theory T is complete, then all models of T realize exactly the same types, since completeness ensures all models are structurally identical."
  type: true-false
  answer: false
  explanation: "Completeness means T decides every sentence — for every sentence φ, either φ ∈ T or ¬φ ∈ T. It does not imply categoricity (all models isomorphic). The theory PA is complete (for first-order logic, with Gödel incompleteness aside) yet has both the standard model ℕ and many nonstandard models, which realize different types. Type realization is precisely what distinguishes models of the same complete theory from one another."

- question: "What is the significance of the distinction between a type being 'consistent' and a type being 'realized'? Use a concrete example to illustrate why the gap matters."
  type: short-answer
  answer: "A type p(x) is consistent if every finite subset of p is satisfiable — there is no logical contradiction in p. It is realized in M if there is a single element a ∈ M satisfying all formulas in p simultaneously. The gap between these notions is the gap between logical possibility and actual instantiation. Example: the type {x > n : n ∈ ℕ} in PA is consistent — for any finite subset {x > 0, …, x > k}, any standard number larger than k witnesses it. But the standard model ℕ omits this type: no single standard natural number exceeds every other. A nonstandard model realizes it with an 'infinite' element. This gap matters because it shows that models of the same theory can differ radically in their elements, and gives the Omitting Types Theorem its content: a non-isolated type can be deliberately excluded from a countable model, allowing precise construction of 'thin' models with prescribed absences."
  explanation: "The consistency-realization gap is one of model theory's most important distinctions. It underlies the entire study of saturation, omission, and the diversity of models of a fixed theory."
```

## Explainer

You know from studying **type spaces** that a **type** p(x) over a parameter set A is a maximal consistent set of formulas with free variable x and parameters from A — it describes a "possible element" of the theory that is logically coherent but may or may not actually exist in a given model. A model M **realizes** a type p if there is an actual element a ∈ M satisfying every formula in p simultaneously. The type is not merely consistent in the abstract; it is *instantiated* by a concrete element. If no such element exists in M, then M **omits** p — the type is consistent but absent from this particular model.

The intuition from arithmetic is vivid. In the standard model ℕ of Peano arithmetic, consider the type p(x) = {x > 0, x > 1, x > 2, x > 3, …} — the type of an element larger than every standard natural number. Each finite portion of p is consistent with ℕ (there's always a larger standard number), but ℕ omits p as a whole: there is no single element greater than every natural number. A **nonstandard model** of PA, however, *realizes* p — it contains infinite elements. The same consistent type is realized in some models and omitted in others, and this variance drives much of model theory.

**Saturated models** are models that realize as many types as possible. A model M is κ-saturated if it realizes every type over every parameter set A of cardinality less than κ that is consistent with the theory. Saturated models are the "richest" models — they contain witnesses for every consistent description. In a saturated real closed field, for instance, every consistent type about an element's ordering relationships with parameters is realized by some element of the field. Saturation gives enormous flexibility: automorphisms can be built from finite partial maps, and any two saturated models of the same complete theory and the same cardinality are isomorphic.

Omitting types is just as useful as realizing them — it lets you construct models with deliberate absences. The **Omitting Types Theorem** states that if a type p is not isolated (no single formula implies p), then there is a countable model of the theory that omits p entirely. This is the tool for building "small" or "thin" models that avoid particular elements. The construction uses a Henkin-style argument, arranging witnesses at each stage to avoid realizing the unwanted type. Together, realization and omission give a fine-grained vocabulary for classifying models: which types they contain is a primary axis along which models of the same theory differ.
