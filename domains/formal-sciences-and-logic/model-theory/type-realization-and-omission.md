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

## Explainer

You know from studying **type spaces** that a **type** p(x) over a parameter set A is a maximal consistent set of formulas with free variable x and parameters from A — it describes a "possible element" of the theory that is logically coherent but may or may not actually exist in a given model. A model M **realizes** a type p if there is an actual element a ∈ M satisfying every formula in p simultaneously. The type is not merely consistent in the abstract; it is *instantiated* by a concrete element. If no such element exists in M, then M **omits** p — the type is consistent but absent from this particular model.

The intuition from arithmetic is vivid. In the standard model ℕ of Peano arithmetic, consider the type p(x) = {x > 0, x > 1, x > 2, x > 3, …} — the type of an element larger than every standard natural number. Each finite portion of p is consistent with ℕ (there's always a larger standard number), but ℕ omits p as a whole: there is no single element greater than every natural number. A **nonstandard model** of PA, however, *realizes* p — it contains infinite elements. The same consistent type is realized in some models and omitted in others, and this variance drives much of model theory.

**Saturated models** are models that realize as many types as possible. A model M is κ-saturated if it realizes every type over every parameter set A of cardinality less than κ that is consistent with the theory. Saturated models are the "richest" models — they contain witnesses for every consistent description. In a saturated real closed field, for instance, every consistent type about an element's ordering relationships with parameters is realized by some element of the field. Saturation gives enormous flexibility: automorphisms can be built from finite partial maps, and any two saturated models of the same complete theory and the same cardinality are isomorphic.

Omitting types is just as useful as realizing them — it lets you construct models with deliberate absences. The **Omitting Types Theorem** states that if a type p is not isolated (no single formula implies p), then there is a countable model of the theory that omits p entirely. This is the tool for building "small" or "thin" models that avoid particular elements. The construction uses a Henkin-style argument, arranging witnesses at each stage to avoid realizing the unwanted type. Together, realization and omission give a fine-grained vocabulary for classifying models: which types they contain is a primary axis along which models of the same theory differ.
