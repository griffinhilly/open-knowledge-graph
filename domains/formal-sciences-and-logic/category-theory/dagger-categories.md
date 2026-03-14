---
id: dagger-categories
title: Dagger Categories and Involutions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- compact-closed-categories
tags:
- dagger
- involution
- adjoint
- unitary
- self-adjoint
stage: advanced
status: draft
---

# Dagger Categories and Involutions

## Core Idea
A dagger category (†-category) is a category with an involutive functor †: C → C^op such that objects are fixed and f† = (g∘f)† = f† ∘ g†, with (f†)† = f. This structure models categories where morphisms have 'adjoints' or conjugates, as in Hilbert spaces with adjoint operators. Dagger categories provide a categorical framework for self-adjoint and unitary morphisms, and are foundational in categorical quantum mechanics.

## How It's Best Learned
Study the category of finite-dimensional Hilbert spaces with dagger-structure given by adjoint operators. Examine finite sets with involution and verify dagger properties. Define and work with unitary, self-adjoint, and isometric morphisms using the dagger involution.

## Common Misconceptions
The dagger is not a contravariant endofunctor; it is an involution swapping morphism directions while fixing objects. Self-adjoint morphisms (f = f†) behave like Hermitian operators but require careful interpretation in general dagger categories. The dagger structure is additional data and cannot be recovered from the category alone.
