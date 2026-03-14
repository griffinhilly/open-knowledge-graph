---
id: functor-categories
title: Functor Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functors
  type: hard
builds-toward:
- yoneda-lemma
- representable-functors
- limits-and-colimits
tags:
- functor category
- 2-category
- presheaf
- diagram
stage: advanced
status: validated
---

# Functor Categories

## Core Idea
Given categories C and D, the functor category [C, D] (also written D^C) has functors F: C → D as objects and natural transformations as morphisms. Composition of natural transformations is defined component-wise and satisfies all category axioms, making functors and natural transformations into a genuine category. Presheaf categories [C^op, Set] are particularly important in mathematics and logic, providing models for sheaf theory, topos theory, and Kripke semantics for intuitionistic logic.

## How It's Best Learned
Verify that vertical composition of natural transformations (composing η: F ⇒ G and ε: G ⇒ H component-wise) is associative and has identity natural transformations. Then recognize that a diagram of shape J in a category C is simply a functor J → C, making limits and colimits into functors on functor categories.

## Common Misconceptions
- The functor category [C, D] may be large (a proper class) even when C and D are small; size issues matter in foundations.
- Horizontal composition and vertical composition of natural transformations are different operations; both are needed for the full 2-categorical structure.
