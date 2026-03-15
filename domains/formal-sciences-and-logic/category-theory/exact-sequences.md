---
id: exact-sequences
title: Exact Sequences in Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
- id: vector-spaces
  type: soft
builds-toward:
- snake-lemma
- abelian-structure-properties
- homology-and-cohomology
tags:
- sequences
- homological-algebra
- kernels-cokernels
stage: advanced
status: draft
---

# Exact Sequences in Categories

## Core Idea
An exact sequence is a sequence of morphisms f: A → B → C where the image of one equals the kernel of the next. Exactness encodes compatibility conditions between maps. Short exact sequences (0 → A → B → C → 0) characterize extensions and are central to homological algebra, capturing how one object fits inside another with a given quotient.
