---
id: reflective-subcategories
title: Reflective and Coreflective Subcategories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: functors
  type: hard
builds-toward:
- topos-theory-intro
tags:
- reflective
- coreflective
- localization
- adjoint
- inclusion
stage: advanced
status: draft
---

# Reflective and Coreflective Subcategories

## Core Idea
A full subcategory D ⊆ C is reflective if the inclusion functor i: D ↪ C has a left adjoint, called the reflector. The reflector provides a universal way to 'project' objects of C into D while preserving structure. Coreflective subcategories are defined dually, with the inclusion having a right adjoint. Reflective subcategories arise in completion, localization, and in constructing quotient structures.

## How It's Best Learned
Study the reflection of finite sets into all sets (not reflective), abelian groups into groups via abelianization (reflective), and divisible groups as a reflective subcategory of abelian groups. For each example, identify the reflector explicitly and verify the adjunction.

## Common Misconceptions
Not every full subcategory is reflective; reflectivity requires an adjoint to exist and satisfy naturality. The reflector is not surjective on objects—the image of the reflector covers only some objects of C. A full subcategory being reflective does not mean it is closed under limits or colimits in the original category.
