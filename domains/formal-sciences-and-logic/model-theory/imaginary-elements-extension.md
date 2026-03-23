---
id: imaginary-elements-extension
title: Imaginary Elements and Quotient Sorts
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: definability-and-algebraic-applications
  type: soft
builds-toward:
- strongly-minimal-and-geometry
- o-minimality-and-tame-geometry
tags:
- imaginaries
- quotient-structures
- extensions
stage: expert
status: validated
---

# Imaginary Elements and Quotient Sorts

## Core Idea
Imaginary elements are equivalence classes of tuples under definable equivalence relations. The imaginary extension M^eq of a model M adds all such quotient objects as new sorts, creating a richer structure. Imaginary elements capture definable structure that real elements cannot represent and are essential for category-theoretic properties of model theory.

## Questions

```yaml
- question: "What is an 'imaginary element' in the sense of model theory?"
  type: multiple-choice
  options:
    - "An element that satisfies the axioms of the theory in some models but not others"
    - "An equivalence class of real tuples under a definable equivalence relation, treated as a named element in the imaginary extension M^eq"
    - "A complex number that encodes relational data in an arithmetic structure"
    - "A non-standard element introduced by ultraproduct constructions that violates the standard axioms"
  answer: 1
  explanation: "An imaginary element is [ā]_E — the equivalence class of a tuple ā under a definable equivalence relation E. It is 'imaginary' because it lives naturally in the mathematical setting (quotient structure) but is not itself an element of the base model M. The imaginary extension M^eq adds a new sort for each such quotient, making these classes into genuine named objects that can be quantified over and used as parameters."

- question: "In the theory of algebraically closed fields, a definable subgroup H of a definable group G produces cosets that are natural objects of study. Without imaginary elements, a model theorist faces which difficulty?"
  type: multiple-choice
  options:
    - "No difficulty — cosets are already elements of the field in any algebraically closed field"
    - "Awkward coding tricks to represent cosets using field elements, since cosets are sets of elements rather than individual elements of the model"
    - "A restriction to studying only finite groups H, where cosets can be enumerated"
    - "An inability to write first-order formulas defining H or G within the field language"
  answer: 1
  explanation: "A coset gH is a set of field elements — a subset of the domain, not a single element. Without M^eq, to work with cosets one must encode them indirectly using field elements, often choosing representatives and tracking equivalence by hand. This is cumbersome and breaks the clean model-theoretic machinery (types, definability, independence) that requires objects to be elements. M^eq resolves this by making each coset a genuine element in a new sort."

- question: "A theory 'eliminates imaginaries' if every imaginary element is interdefinable with a real tuple — meaning the structure M^eq adds no genuinely new objects beyond those already nameable in M."
  type: true-false
  answer: true
  explanation: "Elimination of imaginaries says: for every definable equivalence relation E on M^n, there is a definable function f: M^n → M^k such that E(ā, b̄) iff f(ā) = f(b̄). In other words, every equivalence class is coded by a real tuple, so no new sort is needed. Algebraically closed fields and strongly minimal theories eliminate imaginaries, which is part of why they have such clean geometric structure — all the definable quotients are already visible within the original model."

- question: "Adding imaginary elements to a model always makes the theory more complex and harder to work with, which is why most model theorists avoid M^eq when possible."
  type: true-false
  answer: false
  explanation: "The opposite is true: M^eq typically makes theories easier to analyze by promoting natural quotient objects to first-class elements. Once cosets, orbits, and other definable quotients are named elements, the full model-theoretic toolkit — types, definability, forking independence — applies directly without coding work-arounds. Theories that eliminate imaginaries (where M and M^eq are essentially equivalent) are considered the cleanest and best-behaved, not because M^eq is avoided, but because it adds nothing genuinely new."

- question: "Why do model theorists construct M^eq, the imaginary extension of M? What problem does it solve that cannot be resolved within M itself?"
  type: short-answer
  answer: "M^eq solves the problem that definable equivalence relations produce natural quotient objects — equivalence classes — that are sets of elements rather than elements of M. A structure can define the relation E(x, y) (saying x and y are equivalent) without being able to name the equivalence classes themselves. This gap means the model-theoretic machinery (quantifying over types, using objects as parameters, studying definability and independence) cannot be applied to these quotient objects directly. M^eq adds a new sort for each definable quotient, making these classes into genuine elements. Now the full toolkit applies, and structural properties like stability, forking, and geometric rank can be analyzed over all definable objects, not just real elements."
  explanation: "The need for M^eq reflects a general phenomenon in logic: a theory can define relations on its domain without being able to name all the sets those relations carve out. Imaginaries fill the gap between 'definable relation' and 'nameable object.'"
```

## Explainer

From your study of structures and formal languages, you know that a model M is a domain of elements together with interpretations of the signature. A **definable set** is a subset of M^n picked out by a first-order formula — it is part of the structure's "visible" geometry. Now consider a definable equivalence relation E on M^n: a formula E(x⃗, y⃗) such that every model satisfies reflexivity, symmetry, and transitivity. The equivalence classes [a⃗]_E are natural mathematical objects — think of the cosets of a definable subgroup, or the orbits under a definable group action. The problem is that these equivalence classes are not elements of M; they are *sets* of elements. This gap between what the structure can define and what it can name is the motivation for imaginary elements.

An **imaginary element** is an equivalence class [a⃗]_E where E is a definable equivalence relation. The **imaginary extension** M^{eq} of M is a richer multi-sorted structure that adds, for each definable equivalence relation E on each Cartesian power M^n, a new sort whose elements are the E-classes of n-tuples. The original elements of M are called **real elements** and form one of the sorts of M^{eq}. There is also a canonical surjection from each sort of n-tuples onto the corresponding quotient sort, which is itself definable in M^{eq}.

Why bother? In many situations, the most natural "points" are not elements of the base structure but quotient objects. In the theory of algebraically closed fields, the coset space G/H (where H is a definable subgroup of a definable group G) is a natural object of study, but its elements are cosets, not field elements. By passing to M^{eq}, these cosets become genuine elements and can be directly quantified over, named by parameters, and handled by the model-theoretic machinery (types, definability, independence). Without imaginaries, one must constantly work around this gap with awkward coding tricks.

The central technical result is that well-behaved theories (specifically, those that **eliminate imaginaries**) have the property that every imaginary element is interdefinable with a real tuple — the new sorts add no genuinely new information, and the quotient structure is already "visible" in the original model. Strongly minimal theories and algebraically closed fields eliminate imaginaries, which is a key reason these theories have such clean geometric structure (the subject of strongly minimal sets and their geometries). Theories that fail to eliminate imaginaries have definable structure that cannot be reduced to real elements, indicating a richer and more complex geometry of types.

