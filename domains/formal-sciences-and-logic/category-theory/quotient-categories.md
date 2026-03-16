---
id: quotient-categories
title: Quotient Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
builds-toward:
- localization-of-categories
tags:
- quotient-construction
- equivalence-relations
- morphism-identification
stage: abstract-reasoning
status: draft
---

# Quotient Categories

## Core Idea
A quotient category is formed by identifying morphisms in a category according to an equivalence relation that respects composition, resulting in a category where some formerly distinct morphisms are identical. Quotient categories generalize the notion of quotient structures in algebra and provide a framework for understanding how categorical information changes under identifications.

## How It's Best Learned
Start with simple examples: quotient of a discrete category by an equivalence relation on objects, and quotient of a category of complexes by homotopy equivalence. Verify that the quotient map is universal and that the quotient respects categorical structure.

## Common Misconceptions
Not every equivalence relation on morphisms descends to a valid quotient category; the relation must be compatible with composition. Additionally, the quotient category may collapse structure in surprising ways.

## Explainer

You know from categories and morphisms that a category consists of objects, morphisms between them, and a composition law. You know from functors that structure-preserving maps between categories must respect this composition. A **quotient category** is what you get when you decide that some formerly distinct morphisms should be considered equal — you "mod out" the morphism sets by an equivalence relation, just as you mod out a group or ring by a normal subgroup or ideal.

The construction is as follows. Start with a category **C**. For each pair of objects X, Y, you impose an equivalence relation ~ on the set Hom_C(X, Y). The critical constraint is that ~ must be a **congruence relation**: it must respect composition. That is, if f ~ f' (morphisms from X to Y) and g ~ g' (morphisms from Y to Z), then g ∘ f ~ g' ∘ f'. This is the categorical analog of a normal subgroup being closed under conjugation — it's precisely the condition that ensures composition in the quotient is well-defined. If you impose an arbitrary equivalence relation that doesn't satisfy congruence, the resulting structure fails to be a category because composition becomes ambiguous.

The **quotient category C/~** then has the same objects as C, but its morphism sets are the equivalence classes: Hom_{C/~}(X, Y) = Hom_C(X, Y)/~. Composition is defined by choosing representatives: [g] ∘ [f] = [g ∘ f], and the congruence condition guarantees this is independent of the choice. The identity morphisms descend immediately: [id_X] is the identity in C/~. The quotient functor Q: C → C/~ sends each morphism f to its class [f]; it is a functor by construction and is the universal functor that identifies all related morphisms — any functor out of C that makes ~ equivalent morphisms go to equal morphisms factors uniquely through C/~.

The most important example in practice is the **homotopy category of chain complexes**: two chain maps f, g: A• → B• are declared equivalent if they are chain-homotopic (there exists a degree-1 map h with f − g = dh + hd). This is a congruence relation, and the quotient category is denoted K(A). The homotopy category collapses an enormous amount of data — two chain maps related by a homotopy are "equivalent for homological purposes" — and is the first step toward the derived category, where one further inverts quasi-isomorphisms. Understanding quotient categories thus unlocks the conceptual foundation of homological algebra: derived categories, derived functors, and localization are all built on this basic machinery of identifying morphisms by categorical equivalence.
