---
id: enriched-categories
title: Enriched Categories and Enrichment
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: monoidal-categories
  type: hard
- id: closed-categories-and-internal-homs
  type: soft
- id: vector-spaces-definition
  type: soft
builds-toward:
- enriched-functors
tags:
- enriched-categories
- enrichment
- hom-objects
- monoidal-category
stage: abstract-reasoning
status: draft
---

# Enriched Categories and Enrichment

## Core Idea
An enriched category over a monoidal category V is a category where hom-sets are replaced by hom-objects in V, with composition and identity axioms formulated internal to V. Enriched categories generalize ordinary categories to settings where morphisms have additional structure—they may be topological spaces, abelian groups, metric spaces, or objects in any monoidal category, unifying many categories of structured objects.

## How It's Best Learned
Study categories enriched over the monoidal category of abelian groups (additive categories), over topological spaces (topological categories), and over a complete lattice (ordered categories). Understand how composition is defined using the monoidal product. Explore how many naturally occurring categories are enriched.

## Common Misconceptions
Enriched categories are not just categories with extra structure on objects; the hom-sets themselves are objects in V. Composition must be expressed in terms of the monoidal structure, which requires care when V is non-cartesian.
