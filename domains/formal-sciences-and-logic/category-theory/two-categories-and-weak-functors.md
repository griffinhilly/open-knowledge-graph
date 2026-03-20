---
id: two-categories-and-weak-functors
title: 2-Categories and Weak Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- higher-category-theory-intro
tags:
- higher-categories
- two-categories
- weak-functors
- natural-transformations
stage: advanced
status: draft
---

# 2-Categories and Weak Functors

## Core Idea
A 2-category consists of objects, morphisms (1-cells) between objects, and 2-morphisms (2-cells) between morphisms, with composition operations at both levels. Weak (or lax) functors between 2-categories preserve the 2-categorical structure up to invertible 2-morphisms, generalizing both ordinary functors and natural transformations. This framework encompasses categories, functors, and natural transformations as a single 2-categorical structure.

## How It's Best Learned
Study the 2-category Cat of all categories, functors, and natural transformations. Understand how ordinary categories and functors sit inside this structure. Explore other 2-categories: 2-categories arising from partial orders, from rings, and from algebraic structures.

## Common Misconceptions
In a 2-category, 2-morphisms need not have inverses; strict equality of compositions is replaced by isomorphism. Weak functors are less restrictive than strict functors and are often more natural, but this requires care in applications.

## Explainer

You already know three layers of categorical structure: **objects** (things), **morphisms** (maps between things, satisfying composition and identity laws), and **natural transformations** (maps between functors, which are themselves maps between categories). A **2-category** takes these three layers and treats them as a unified structure. Objects are 0-cells, morphisms are 1-cells, and natural transformations — or their generalizations — are **2-cells**. The defining example is Cat itself: objects are categories, 1-cells are functors, and 2-cells are natural transformations. The strictness of Cat (composition of functors is strictly associative on the nose) makes it the prototypical **strict** 2-category.

The power of the 2-categorical framework is that it unifies phenomena that otherwise require separate language. The statement "a functor F is an equivalence of categories" becomes, in 2-categorical terms, "F is a 1-cell with a quasi-inverse": there exists G and 2-cell isomorphisms FG ≅ Id and GF ≅ Id. Adjunctions, too, are 2-categorical data: the unit η: Id → GF and counit ε: FG → Id are 2-cells satisfying the triangle identities, so an adjunction is a structured pair of 1-cells with specified 2-cells. Once you recognize that functors, natural transformations, and adjunctions are all just 0-, 1-, and 2-dimensional cells in Cat, you can lift these concepts to any 2-category and reason about them uniformly.

**Strict 2-functors** between 2-categories preserve all structure exactly: composition of 1-cells is preserved on the nose, and 2-cells are sent to 2-cells respecting all compositions. But in practice, many natural constructions only preserve composition up to coherent isomorphism, not up to strict equality. A **weak functor** (also called a **pseudofunctor** or **homomorphism** of 2-categories) preserves composition of 1-cells only up to specified invertible 2-cells, together with coherence conditions ensuring these comparison 2-cells are compatible with associativity and identity. The prototypical example is the functor that assigns to each ring its category of modules: the "tensor product of modules" construction gives a functor that is only associative up to natural isomorphism, not strictly.

The distinction between strict and weak is the first instance of a deep pattern in higher category theory: as dimension increases, equality of composites is progressively weakened to "equivalence up to a cell one dimension higher," with coherence conditions ensuring the cells behave consistently. A **strict** 2-functor sends F(g ∘ f) = F(g) ∘ F(f) exactly. A **weak** 2-functor sends F(g ∘ f) ≅ F(g) ∘ F(f) via an invertible 2-cell φ_{g,f}, and this family of 2-cells must satisfy a pentagon-like coherence condition when composing three 1-cells. These coherence diagrams are the 2-categorical analogues of the associativity and unit axioms for monoidal categories — they ensure all ways of re-bracketing composites using the comparison 2-cells give the same result.

The **builds-toward** topic of higher category theory extends this pattern further: in a 3-category, 3-cells are maps between 2-cells, and weak functors between 3-categories preserve composition only up to invertible 3-cells, and so on up through the n-categorical hierarchy. The 2-categorical layer is where the essential new phenomena first appear — the distinction between strict and weak, the need for coherence data, and the recognition that "equality" of higher-dimensional structure is too strong a demand. Understanding 2-categories and weak functors gives you the conceptual vocabulary to engage with ∞-categories, homotopy type theory, and modern algebraic topology, all of which are grounded in the same hierarchical logic of cells and coherence conditions at increasing dimensions.

