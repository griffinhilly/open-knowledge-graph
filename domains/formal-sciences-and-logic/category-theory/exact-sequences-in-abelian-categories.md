---
id: exact-sequences-in-abelian-categories
title: Exact Sequences in Abelian Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: chain-complexes-exact-sequences
  type: hard
builds-toward:
- the-snake-lemma
- the-five-lemma
- long-exact-sequences
tags:
- exactness
- kernels
- images
- homology
stage: abstract-reasoning
status: draft
---

# Exact Sequences in Abelian Categories

## Core Idea
In an abelian category, a sequence of morphisms is exact at an object if the image of one morphism equals the kernel of the next, generalizing the notion of exactness from module categories. Exactness is the central concept of homological algebra and allows systematic study of how information flows through categorical constructions.

## How It's Best Learned
Start with short exact sequences in the category of abelian groups, then extend to modules and general abelian categories. Verify exactness by computing images and kernels. Construct examples of exact and non-exact sequences.

## Common Misconceptions
Exactness at an object depends on both the morphism going in and going out, not either alone. Students sometimes forget that exactness is a local condition—it must hold at every object in the sequence.
