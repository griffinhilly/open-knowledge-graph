---
id: presheaves-and-sheaves
title: Presheaves and Sheaves on Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: presheaves
  type: hard
- id: yoneda-embedding-full-faithful
  type: soft
builds-toward:
- topos-theory-intro
tags:
- presheaf
- sheaf
- grothendieck-topology
- topos
- gluing
stage: advanced
status: draft
---

# Presheaves and Sheaves on Categories

## Core Idea
A presheaf on a category C is a contravariant functor C^op → Set. The presheaf category [C^op, Set] is a Grothendieck topos: cartesian closed, complete, cocomplete, and satisfying the internal axiom of choice. Sheaves are presheaves satisfying a gluing condition with respect to a Grothendieck topology, forming a reflective subcategory. Presheaves and sheaves provide the fundamental examples of topoi and model intuitionistic logic.

## How It's Best Learned
Study simplicial sets [∆^op, Set] as the canonical presheaf example. Verify that [C^op, Set] is cartesian closed and complete. Define sheafification and verify that sheaves form a reflective subcategory. Compute limits and colimits of presheaves and sheaves explicitly.

## Common Misconceptions
Presheaves are not sheaves; sheafification requires imposing a Grothendieck topology. Not every presheaf is representable; non-representable presheaves are essential to the theory. Topos logic is intuitionistic; classical logic requires additional axioms (like axiom of choice), and not all topoi satisfy them.
