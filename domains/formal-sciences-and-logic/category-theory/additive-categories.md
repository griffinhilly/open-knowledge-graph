---
id: additive-categories
title: Additive Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: initial-and-terminal-objects
  type: hard
- id: products-and-coproducts
  type: hard
builds-toward:
- abelian-categories
- biproducts-in-categories
tags:
- additive-structure
- abelian-groups
- hom-sets
stage: abstract-reasoning
status: draft
---

# Additive Categories

## Core Idea
An additive category is a category enriched in abelian groups where hom-sets admit addition operations compatible with morphism composition, and where finite products coincide with finite coproducts (called biproducts). Additive categories generalize the structure of modules and provide the algebraic foundation for homological algebra.

## How It's Best Learned
Begin with the category of abelian groups and modules over a ring. Verify that morphism sets form abelian groups under pointwise addition and that biproducts exist. Then examine more abstract additive categories and their universal properties.

## Common Misconceptions
Additivity does not require the category to have zero objects, though it ensures their existence. Another misconception: not every category enriched over abelian groups is additive without additional structure.
