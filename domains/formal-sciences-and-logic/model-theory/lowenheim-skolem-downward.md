---
id: lowenheim-skolem-downward
title: Downward Löwenheim-Skolem Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: lowenheim-skolem-theorems-overview
  type: hard
- id: compactness-theorem-model-theory
  type: hard
- id: cardinality-and-countability
  type: soft
builds-toward:
- skolem-functions-and-witnesses
tags:
- downward LS
- countable model
- countable theory
stage: advanced
status: draft
---

# Downward Löwenheim-Skolem Theorem

## Core Idea
The Downward Löwenheim-Skolem Theorem states: if a countable set of first-order sentences has an infinite model, then it has a countable model. This surprising result means no first-order axiomatization can force uncountability. Every countable first-order theory with an infinite model has a countable model, revealing a fundamental limitation of first-order expressiveness.

## Explainer

You already know that cardinality is a genuine distinction between infinite sets — the natural numbers are countable while the real numbers are not, and no bijection exists between them. The Downward Löwenheim-Skolem Theorem says something that initially sounds impossible: if you write down any countable set of first-order axioms that has an infinite model, it also has a countable model. The axioms cannot force the models to be uncountable, no matter what you say.

The proof is constructive and illuminating. Starting from any model M, you use **Skolem functions** — for each existential statement "there exists x such that φ(x, a₁, ..., aₙ)," pick a specific witnessing element. The closure of any countable set of elements under all Skolem functions is countable, and it forms an **elementary substructure** — a submodel that satisfies exactly the same first-order sentences as M. If you start with a countable set of elements and close under countably many functions, the result is countable. That countable elementary substructure is the promised countable model.

The philosophical punchline is **Skolem's paradox**. Zermelo-Fraenkel set theory (ZFC) proves the existence of uncountable sets — the theorem is right there in the axioms. But by Downward Löwenheim-Skolem, if ZFC is consistent, it has a countable model. How can a model of ZFC be countable if ZFC proves uncountable sets exist? The resolution is that "uncountable" is relative: inside the countable model, the set of real numbers appears uncountable because there is no bijection to the naturals *within the model*. The bijection exists in the real world (the set is only countably infinite when viewed from outside), but the model cannot see it. Uncountability is not an absolute property — it is always relative to a universe of sets.

The deeper lesson is about the **expressive limitations of first-order logic**. No matter how many axioms you write, you cannot use first-order sentences alone to guarantee that your models are large. Any property that fails in some countable structure cannot be expressed by a first-order theory with only infinite models. This is why mathematicians working with uncountable structures — measure theory, analysis, higher set theory — cannot fully capture their intended meanings in first-order terms. The theorem pairs with the Compactness Theorem to delineate exactly what first-order logic can and cannot say about size.
