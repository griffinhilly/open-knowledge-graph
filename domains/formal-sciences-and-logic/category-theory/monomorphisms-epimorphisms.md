---
id: monomorphisms-epimorphisms
title: Monomorphisms and Epimorphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- additive-categories
- abelian-structure-properties
tags:
- morphisms
- universal-properties
- categorical-structure
stage: advanced
status: draft
---

# Monomorphisms and Epimorphisms

## Core Idea
Monomorphisms generalize injective functions to arbitrary categories: a morphism f: A → B is monic if whenever gf = hf, then g = h. Epimorphisms are the dual concept, generalizing surjections. In categories without a notion of elements, these abstract properties capture injectivity and surjectivity without requiring explicit set-theoretic membership.

## How It's Best Learned
Start in Set and Ring where monomorphisms are exactly injections and epimorphisms are exactly surjections. Then explore categories where these concepts diverge—for example, in rings the natural homomorphism R → R[x] is epic but not surjective.

## Common Misconceptions
Assuming monomorphisms are always injective (false in general). Thinking epimorphisms must be surjective (counterexample: R → R[x] in Ring). Assuming every morphism is either monic or epic.
