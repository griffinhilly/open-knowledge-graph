---
id: symmetric-monoidal-categories
title: Symmetric Monoidal Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: braided-monoidal-categories
  type: hard
builds-toward:
- closed-categories-and-internal-homs
tags:
- symmetry
- commutativity
- coherence
- monoidal-category
stage: abstract-reasoning
status: draft
---

# Symmetric Monoidal Categories

## Core Idea
A symmetric monoidal category is a braided monoidal category where the braiding is a symmetry—it squares to the identity and satisfies the additional compatibility that swapping twice returns the original arrangement. Symmetric monoidal categories are the most well-behaved monoidal categories and are pervasive in algebra, topology, and logic, where they provide a categorical framework for commutative multiplication.

## How It's Best Learned
Study the category of finite-dimensional vector spaces with the standard tensor product, the category of abelian groups, and the category of sets with disjoint union and cartesian product. Verify the symmetry condition and explore how it simplifies coherence. Work with monoids and commutative monoids in symmetric monoidal categories.

## Common Misconceptions
Symmetry is a very restrictive condition; not all braided categories are symmetric. In symmetric monoidal categories, the distinction between left and right actions essentially disappears.
