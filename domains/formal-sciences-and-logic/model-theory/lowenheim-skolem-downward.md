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
- id: lowenheim-skolem-upward
  type: soft
builds-toward:
- skolem-functions-and-witnesses
tags:
- downward LS
- countable model
- countable theory
stage: expert
status: validated
---
# Downward Löwenheim-Skolem Theorem

## Core Idea
The Downward Löwenheim-Skolem Theorem states: if a countable set of first-order sentences has an infinite model, then it has a countable model. This surprising result means no first-order axiomatization can force uncountability. Every countable first-order theory with an infinite model has a countable model, revealing a fundamental limitation of first-order expressiveness.

## Questions

```yaml
- question: "ZFC set theory proves that uncountable sets exist. By the Downward Löwenheim-Skolem theorem, ZFC has a countable model. A student says this is a contradiction: 'a countable model cannot contain uncountable sets.' What is the correct resolution?"
  type: multiple-choice
  options:
    - "ZFC cannot actually prove uncountable sets exist within a countable model"
    - "The countable model contains a set that appears uncountable from inside the model because no bijection to ω exists within the model itself"
    - "The theorem only applies if ZFC is consistent, and ZFC might be inconsistent"
    - "The model is only 'countable' in an informal sense; technically it contains uncountably many elements"
  answer: 1
  explanation: "This is Skolem's paradox, resolved by recognizing that 'uncountable' is model-relative. The model is countable when viewed from outside (an external bijection to ω exists), but the model cannot see that bijection — it does not exist as an element or function within the model. Inside the model, the real numbers appear uncountable because no internal bijection witnesses their equinumerosity with ω. 'Uncountable' always means 'no bijection to ω exists in this universe,' and the relevant universe depends on your vantage point."

- question: "A logician wants to write a countable set of first-order axioms whose models are all and only uncountable structures. Can this be done?"
  type: multiple-choice
  options:
    - "Yes — just add the axiom 'there exist uncountably many elements' in first-order syntax"
    - "Yes — Cantor's diagonal argument can be transcribed into a finite set of first-order axioms"
    - "No — the Downward Löwenheim-Skolem theorem guarantees any such theory with an infinite model also has a countable model"
    - "No — but only because first-order logic has no quantifiers that range over sets"
  answer: 2
  explanation: "First-order logic cannot express 'there are uncountably many elements' as a first-order sentence — cardinality conditions of this kind lie beyond first-order expressibility. Downward LS makes this precise: any countable first-order theory that has any infinite model must also have a countable model. So you cannot rule out countable models using first-order axioms alone. This is a fundamental limitation of first-order logic: it cannot control the cardinality of its models from above."

- question: "The Downward Löwenheim-Skolem theorem states that nearly every first-order theory has a countable model."
  type: true-false
  answer: false
  explanation: "The theorem requires two conditions: the theory must be countable (finitely or countably many sentences), and it must have at least one infinite model. A theory satisfied only by finite structures need not have a countable infinite model. Also, an inconsistent theory has no models at all. The correct statement is: if a countable first-order theory has an infinite model, then it has a countable model. Finite models and theories with only finite models are not covered."

- question: "The proof of Downward Löwenheim-Skolem constructs a countable elementary substructure by closing a countable seed set under Skolem functions — and the closure of a countable set under countably many functions is countable."
  type: true-false
  answer: true
  explanation: "This is the core construction. For each existential formula φ(x, a₁,...,aₙ), a Skolem function picks a specific witnessing element. Starting from any countable seed (even a single element), closing under countably many Skolem functions adds at most countably many elements per step. A countable union of countable sets is countable. The result is an elementary substructure — it satisfies exactly the same first-order sentences as the original model — and it is provably countable."

- question: "What does Skolem's paradox reveal about the nature of 'uncountability,' and how is the apparent contradiction resolved?"
  type: short-answer
  answer: "Skolem's paradox reveals that uncountability is not an absolute property but is relative to a model. A set can be 'uncountable' within a model (no internal bijection to ω exists) yet be countable when viewed from outside (an external bijection exists). The contradiction dissolves because 'uncountable' means 'no bijection to ω in this universe,' and the relevant universe differs depending on whether you are inside or outside the model."
  explanation: "ZFC proves ℝ is uncountable, meaning the model satisfies the sentence 'there is no bijection from ℝ to ω.' In the countable model, this sentence is still true — the model contains no such bijection as an internal object. But externally, the entire domain of the model is countable, so a bijection exists outside the model. This shows that cardinality claims are always relative to a background set-theoretic universe, not absolute facts. The same lesson applies to power sets, measurability, and many other set-theoretic notions."
```

## Explainer

You already know that cardinality is a genuine distinction between infinite sets — the natural numbers are countable while the real numbers are not, and no bijection exists between them. The Downward Löwenheim-Skolem Theorem says something that initially sounds impossible: if you write down any countable set of first-order axioms that has an infinite model, it also has a countable model. The axioms cannot force the models to be uncountable, no matter what you say.

The proof is constructive and illuminating. Starting from any model M, you use **Skolem functions** — for each existential statement "there exists x such that φ(x, a₁, ..., aₙ)," pick a specific witnessing element. The closure of any countable set of elements under all Skolem functions is countable, and it forms an **elementary substructure** — a submodel that satisfies exactly the same first-order sentences as M. If you start with a countable set of elements and close under countably many functions, the result is countable. That countable elementary substructure is the promised countable model.

The philosophical punchline is **Skolem's paradox**. Zermelo-Fraenkel set theory (ZFC) proves the existence of uncountable sets — the theorem is right there in the axioms. But by Downward Löwenheim-Skolem, if ZFC is consistent, it has a countable model. How can a model of ZFC be countable if ZFC proves uncountable sets exist? The resolution is that "uncountable" is relative: inside the countable model, the set of real numbers appears uncountable because there is no bijection to the naturals *within the model*. The bijection exists in the real world (the set is only countably infinite when viewed from outside), but the model cannot see it. Uncountability is not an absolute property — it is always relative to a universe of sets.

The deeper lesson is about the **expressive limitations of first-order logic**. No matter how many axioms you write, you cannot use first-order sentences alone to guarantee that your models are large. Any property that fails in some countable structure cannot be expressed by a first-order theory with only infinite models. This is why mathematicians working with uncountable structures — measure theory, analysis, higher set theory — cannot fully capture their intended meanings in first-order terms. The theorem pairs with the Compactness Theorem to delineate exactly what first-order logic can and cannot say about size.
