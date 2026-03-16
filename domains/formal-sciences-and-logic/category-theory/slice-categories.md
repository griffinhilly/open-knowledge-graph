---
id: slice-categories
title: Slice and Coslice Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- universal-properties
- kan-extensions
tags:
- slice
- coslice
- comma
- relative
- over
stage: advanced
status: draft
---

# Slice and Coslice Categories

## Core Idea
The slice category C/X has objects as morphisms f: Y → X and morphisms as commutative triangles. The coslice category X/C has objects as morphisms X → Y with the same commutative structure. Slice categories formalize 'relative' categorical properties and are essential for defining limits and colimits in a relative sense. They appear naturally in studying fibrations and in defining universal properties with a fixed reference object.

## How It's Best Learned
Study slice categories of Set over a set S (equivalent to S-indexed families of sets). Examine slice categories of a poset over an element, and verify that limits in the slice category correspond to special limits in the original category.

## Common Misconceptions
A slice category is not a full subcategory—morphisms in C/X are defined relative to X. Not every limit in C/X lifts to a limit in C. The universal properties in slice categories are weaker than absolute universal properties because they depend on the choice of X.

## Explainer

You already know that a category consists of objects and morphisms satisfying identity and composition laws. The slice construction takes a fixed object X in a category C and builds an entirely new category whose objects are **morphisms landing in X**. An object of the **slice category** C/X is a pair (Y, f) where f: Y → X is a morphism in C. Think of it as "everything that maps into X, organized as a category in its own right."

A morphism in C/X from (Y, f) to (Z, g) is a morphism h: Y → Z in C such that the triangle commutes: g ∘ h = f. In other words, h must be compatible with the maps to X — it doesn't just connect Y to Z, it connects Y to Z **in a way that respects both objects' relationship to X**. Composition is inherited from C (compose the underlying morphisms), and the commutativity condition is preserved under composition. Identity morphisms are the identity morphisms from C, which trivially satisfy the commutativity condition.

The concrete example worth internalizing is **Set/S**, the slice of **Set** over a set S. An object is a function f: A → S — equivalently, an S-indexed family of sets (the fiber over each s ∈ S is f⁻¹(s)). A morphism from f: A → S to g: B → S is a function h: A → B preserving fibers: g(h(a)) = f(a) for all a. This is precisely a morphism of S-indexed families of sets. So **Set/S** is equivalent to the category of S-indexed families — and this makes slice categories the correct setting for studying variable or parameterized structures.

The **coslice category** X/C reverses the arrows: its objects are morphisms X → Y (things that X maps **into**), and morphisms are commutative triangles pointing outward. Coslice categories capture "things equipped with a distinguished element or basepoint," since a morphism X → Y in Set is the same as a choice of element in Y (when X is a singleton). Both slice and coslice categories appear naturally in the theory of limits and colimits — a cone over a diagram D with apex X is exactly an object of the appropriate slice category built from D — and they are essential for expressing universal properties in a relative, contextual way. When the fixed object X changes, so does the entire categorical context for what "universal" means.
