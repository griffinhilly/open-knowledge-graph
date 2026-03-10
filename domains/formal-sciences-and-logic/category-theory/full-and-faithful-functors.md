---
id: full-and-faithful-functors
title: Full and Faithful Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: injective-surjective-bijective
  type: soft
builds-toward:
- equivalence-of-categories
- representable-functors
- yoneda-lemma
tags:
- full functor
- faithful functor
- embedding
- subcategory
stage: advanced
status: draft
---

# Full and Faithful Functors

## Core Idea
A functor F: C → D is faithful if it is injective on each hom-set (F(f) = F(g) implies f = g), and full if it is surjective on each hom-set (every morphism between F(A) and F(B) in D arises as F(f) for some f in C). A fully faithful functor embeds C as a subcategory of D in a strong sense: it reflects isomorphisms and allows C to be identified with its image in D. Forgetful functors are typically faithful but not full; inclusion functors of full subcategories are fully faithful.

## How It's Best Learned
Check the forgetful functor from Ab (abelian groups) to Grp: it is faithful (group homomorphisms between abelian groups are the same in both categories) but not full (not every group homomorphism between two abelian groups is an abelian group homomorphism—actually it is, so check another example). Work out when the inclusion of a subcategory is full.

## Common Misconceptions
- A fully faithful functor need not be an isomorphism of categories; it can fail to be surjective on objects.
- Faithful does not mean injective on objects; a functor can be faithful yet send different objects to the same object.
