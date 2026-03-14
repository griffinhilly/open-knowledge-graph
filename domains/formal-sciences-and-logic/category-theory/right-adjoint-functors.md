---
id: right-adjoint-functors
title: Right Adjoint Functors
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
- limits-and-colimits
tags:
- adjunction
- functor-pairs
- universal-properties
stage: advanced
status: draft
---

# Right Adjoint Functors

## Core Idea
A functor R: D → C is a right adjoint if there exists L: C → D such that morphisms Lc → d in D correspond bijectively to morphisms c → Rd in C, naturally in both variables. Right adjoints preserve limits and characterize objects as 'universal targets' for maps from given sources. They are dual to left adjoints via opposite categories.
