---
id: cartesian-closed-categories
title: Cartesian Closed Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: products-and-coproducts
  type: hard
- id: initial-and-terminal-objects
  type: hard
builds-toward:
- topos-theory-intro
tags:
- cartesian
- closed
- exponential
- internal-hom
- lambda-calculus
stage: advanced
status: draft
---

# Cartesian Closed Categories

## Core Idea
A cartesian closed category has finite products with a terminal object and an exponential object B^A for each pair of objects, satisfying the adjunction Hom(A × B, C) ≅ Hom(A, C^B). Cartesian closed categories are the categorical semantics for typed lambda calculus and higher-order logic. The exponential object represents the set of all morphisms from A to B, generalizing function spaces.

## How It's Best Learned
Study Set (exponential = function space), Top (topological exponential objects and the compact-open topology), and Grp (where exponentials do not always exist). Verify the adjunction explicitly in these examples and practice translating lambda calculus into cartesian closed category language.

## Common Misconceptions
Not every category with finite products is cartesian closed; the exponential object must exist and satisfy the adjunction. In Top, the naive exponential (all continuous functions with pointwise operations) may fail to be in the category unless carefully chosen. Cartesian closed structure depends on the underlying monoidal structure.
