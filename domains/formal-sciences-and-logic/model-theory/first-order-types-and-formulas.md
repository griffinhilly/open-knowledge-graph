---
id: first-order-types-and-formulas
title: First-Order Types and Partial Descriptions
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: complete-first-order-theories
  type: hard
- id: set-membership-and-notation
  type: soft
builds-toward:
- type-spaces-and-stone-topology
- type-realization-and-omission
tags:
- type
- partial type
- n-type
- consistency
- formula set
stage: advanced
status: draft
---

# First-Order Types and Partial Descriptions

## Core Idea
An n-type p(x₁,...,xₙ) over a theory T is a set of formulas in n free variables consistent with T. Types formalize 'partial descriptions' of elements: they capture which formulas are satisfied by those elements. Realized types correspond to actual n-tuples in models; omitted types correspond to 'gaps' where the described n-tuple does not exist.

## Explainer

From your work on complete first-order theories, you know that a theory T is the set of all sentences true in some class of structures, and that a complete theory decides every sentence one way or the other. But sentences only describe *global* truths about a structure — they say nothing about specific elements. A **type** is the local analogue: it captures everything a theory can say about particular elements. An **n-type** p(x₁, ..., xₙ) over a theory T is a set of first-order formulas with n free variables, each formula consistent with T, that describes what n particular elements of a model might look like from the theory's perspective.

Think of a concrete example: let T be the complete theory of the real number field. The 1-type of a particular real number r is the collection of all formulas φ(x) that r satisfies — things like "x > 0," "x² < 2," "x ≠ 1/3," and infinitely many more. Two real numbers have the same type if and only if the theory cannot distinguish them using any formula. A **complete type** is a maximal consistent set: for every formula φ(x), either φ or ¬φ is in the type. Complete types are the finest possible descriptions — they pin down an element as precisely as the language of T allows. A **partial type** is any consistent subset of a complete type, a description that leaves some questions open.

The distinction between **realized** and **omitted** types is where the theory becomes interesting. A type p(x) is *realized* in a model M if some element a ∈ M satisfies every formula in p simultaneously. It is *omitted* if no such element exists in M, even though p is consistent with T. Some types are consistent with T yet omitted in every countable model — the **Omitting Types Theorem** precisely characterizes when this is possible. This shows that models of the same complete theory can differ structurally: they realize different types over T, giving rise to non-isomorphic models. Constructing models that omit certain types (or realize all types) is a fundamental model-theoretic technique.

All complete n-types consistent with T are collected into the **type space** Sₙ(T). This space carries a natural topology — the Stone topology — where basic open sets correspond to types containing a given formula. The size and complexity of Sₙ(T) directly measures how many distinct "possible behaviors" n-tuples of elements can exhibit according to T. Counting types turns out to be a deep invariant: if Sₙ(T) is small (at most countable over every countable parameter set), the theory is **stable**, with strong structural properties. If type spaces can be maximal, the theory is unstable and far more combinatorially complex. Types thus bridge the microscopic (what does this specific element look like?) and the macroscopic (how complex is this theory overall?) — making them the central currency of model-theoretic classification.
