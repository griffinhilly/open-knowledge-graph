---
id: the-snake-lemma
title: The Snake Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
- id: commutative-diagrams-and-composition
  type: hard
builds-toward:
- the-five-lemma
- diagram-chasing-lemmas
tags:
- homological-algebra
- diagram-chasing
- connecting-morphism
stage: abstract-reasoning
status: draft
---

# The Snake Lemma

## Core Idea
The snake lemma is a fundamental result in homological algebra stating that given a commutative diagram of short exact sequences in an abelian category, there exists a natural connecting morphism (the 'snake') from the kernel of one morphism to the cokernel of another, and the resulting six-term sequence is exact. It is a premier tool for deriving long exact sequences from short ones.

## How It's Best Learned
Draw the full commutative diagram and carefully trace through the construction of the connecting morphism using diagram chasing. Apply it to derive long exact sequences in homology and cohomology. Work through its proof in a concrete category first (abelian groups or modules).

## Common Misconceptions
The connecting morphism is not arbitrary; its construction involves careful diagram chasing and depends on exactness. Students sometimes apply the snake lemma without verifying that the input diagram genuinely consists of short exact sequences.
