---
id: fibered-categories
title: Fibered Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: comma-categories
  type: hard
- id: functor-categories
  type: hard
- id: two-categories
  type: soft
- id: opposite-categories-and-duality
  type: soft
builds-toward:
- grothendieck-construction
tags:
- fibered category
- fibration
- cartesian morphism
- Grothendieck fibration
- descent
- cleavage
stage: advanced
status: draft
---
# Fibered Categories

## Core Idea
A fibered category (or Grothendieck fibration) over a base category B is a functor p: E → B such that for every morphism f: b → b' in B and object e' in E with p(e') = b', there exists a cartesian morphism (or cartesian lifting) φ: e → e' with p(φ) = f, satisfying a universal property. Intuitively, E is a "family of categories parametrized by B": the fiber E_b = p^{-1}(b) is the category sitting over each object b, and cartesian morphisms provide canonical ways to pull back along morphisms in B. Fibered categories formalize the notion of "varying algebraic/geometric structure over a base" and are central to descent theory, stacks, and the Grothendieck construction.

## How It's Best Learned
Consider the codomain fibration cod: Arr(C) → C sending each arrow f: A → B to its codomain B. The fiber over B is the slice category C/B. A cartesian morphism is a pullback square. Verify the universal property of cartesian liftings in this example. Then consider the category of vector bundles over a base space, where the fiber functor sends each bundle to its base space—pullback of bundles provides the cartesian liftings.

## Common Misconceptions
- A fibered category is not the same as a functor to Cat; the Grothendieck construction provides the precise correspondence, but a fibration is a single functor p: E → B, not a diagram of categories.
- Cartesian morphisms are not simply morphisms in the total category; they must satisfy a universal property relative to the projection functor.
- A cleavage (choice of cartesian liftings) is not unique; different cleavages give equivalent structures, and a split fibration is one where the cleavage is strictly functorial.
