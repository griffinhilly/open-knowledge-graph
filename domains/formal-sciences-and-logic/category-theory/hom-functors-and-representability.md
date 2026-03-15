---
id: hom-functors-and-representability
title: Hom-Functors and Representability
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: representable-functors
  type: hard
- id: yoneda-lemma
  type: hard
- id: functions-and-function-properties
  type: soft
builds-toward:
- yoneda-embedding-full-faithful
- topos-theory-intro
tags:
- hom
- representable
- universal-element
- natural-isomorphism
stage: advanced
status: draft
---

# Hom-Functors and Representability

## Core Idea
For an object A in a category C, the contravariant hom-functor Hom(−, A): C^op → Set is a fundamental example of a set-valued functor. A functor F: C → Set is representable if it is naturally isomorphic to Hom(−, A) for some object A. Representability is equivalent to the existence of a universal element, and the Yoneda lemma characterizes all natural transformations from representable functors as evaluations at elements of the representing object.

## How It's Best Learned
Study representable functors in Set (where Hom(1, −) ≅ identity), Group (where Hom(Z, −) ≅ identity), and Vec_k. Use the Yoneda lemma to show that any natural transformation between representable functors corresponds uniquely to an element of the representing object.

## Common Misconceptions
Not every set-valued functor is representable—representability is a strong condition requiring a universal element. A functor can be 'almost' representable but fail on a single object or natural transformation. Representability depends on the target category (Set vs other categories give different notions).
