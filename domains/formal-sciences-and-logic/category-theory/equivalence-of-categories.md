---
id: equivalence-of-categories
title: Equivalence of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: full-and-faithful-functors
  type: hard
- id: natural-transformations
  type: hard
- id: isomorphisms-in-categories
  type: soft
- id: adjunction-unit-and-counit
  type: soft
- id: equivalence-relations
  type: soft
- id: yoneda-lemma
  type: soft
tags:
- equivalence of categories
- essentially surjective
- skeleton
- categorical equivalence
stage: advanced
status: validated
---
# Equivalence of Categories

## Core Idea
Two categories C and D are equivalent if there exist functors F: C → D and G: D → C with natural isomorphisms GF ≅ Id_C and FG ≅ Id_D. Equivalence is weaker than isomorphism (which requires GF = Id_C exactly) but is the correct notion of 'sameness' for categories, since categorical properties are invariant under equivalence. A functor F: C → D is an equivalence if and only if it is full, faithful, and essentially surjective (every object of D is isomorphic to some F(C)). Skeleta, opposite categories of finite sets, and many duality theorems (Stone duality, Pontryagin duality) are equivalences.

## How It's Best Learned
Verify that the inclusion of the full subcategory of finite sets {∅, {1}, {1,2}, {1,2,3}, ...} into FinSet is an equivalence, even though it is not an isomorphism. Check full faithfulness and essential surjectivity explicitly. Then compare with the non-equivalence of Set and Grp to understand why all three conditions are necessary.

## Common Misconceptions
- Equivalent categories can look very different set-theoretically; equivalence ignores the choice of specific objects in favor of isomorphism classes.
- An equivalence does not require the functors F and G to be inverses on objects; GF(A) need only be isomorphic to A, not equal.
- Essential surjectivity alone is far from sufficient; faithfulness ensures F reflects structural distinctions and fullness ensures no morphisms are missed.
