---
id: left-adjoint-functors
title: Left Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- adjoint-functors
- adjunction-as-hom-bijection
- monads-in-category-theory
tags:
- adjunction
- functor-pairs
- universal-properties
stage: advanced
status: draft
---

# Left Adjoint Functors

## Core Idea
A functor L: C → D is a left adjoint if there exists R: D → C such that morphisms Lc → d in D correspond bijectively to morphisms c → Rd in C, naturally in both variables. Left adjoints preserve colimits and satisfy a universal property characterizing them as the 'best approximation' in a precise sense.
