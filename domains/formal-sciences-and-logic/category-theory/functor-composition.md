---
id: functor-composition
title: Composition of Functors and Functor Equations
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
builds-toward:
- functor-categories
- natural-transformations
tags:
- functors
- categorical-structure
- composition
stage: advanced
status: draft
---

# Composition of Functors and Functor Equations

## Core Idea
Functors compose: given F: A → B and G: B → C, their composition GF: A → C is defined pointwise on objects and morphisms. Functor composition is associative with identity functors as units. This makes categories into a 2-category where objects are categories, 1-morphisms are functors, and 2-morphisms are natural transformations.
