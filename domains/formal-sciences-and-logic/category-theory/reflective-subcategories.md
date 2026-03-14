---
id: reflective-subcategories
title: Reflective and Coreflective Subcategories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: universal-properties
  type: hard
builds-toward:
- localization-of-categories
tags:
- adjoint-pairs
- reflections
- coreflections
- universal-properties
stage: abstract-reasoning
status: draft
---

# Reflective and Coreflective Subcategories

## Core Idea
A subcategory is reflective if the inclusion functor has a left adjoint (the reflection), and coreflective if it has a right adjoint (the coreflection). These adjoints provide universal ways to map objects into or out of the subcategory, formalizing the idea that the subcategory 'captures' certain categorical properties. Reflective subcategories are ubiquitous in algebra, topology, and homological algebra.

## How It's Best Learned
Study the category of abelian groups as a reflective subcategory of groups, and the category of vector spaces as a reflective subcategory of modules. Understand the reflection functor and verify that the universal property holds. Compute reflections and coreflections in concrete examples.

## Common Misconceptions
A subcategory need not be reflective, even if the inclusion functor is fully faithful. Also, reflection and coreflection are distinct operations; a subcategory cannot be both reflective and coreflective unless it is the ambient category itself (in most cases).
