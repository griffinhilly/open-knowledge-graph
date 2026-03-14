---
id: the-five-lemma
title: The Five Lemma and Related Results
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
builds-toward:
- diagram-chasing-lemmas
tags:
- homological-algebra
- isomorphism-criteria
- diagram-chasing
stage: abstract-reasoning
status: draft
---

# The Five Lemma and Related Results

## Core Idea
The five lemma states that if two rows of a commutative diagram are exact and four of the five vertical morphisms are isomorphisms, then so is the fifth—providing a powerful criterion for establishing isomorphisms without explicit computation. The short five lemma and related results like the four lemma are equally useful for showing injectivity and surjectivity.

## How It's Best Learned
Begin with the standard five lemma and verify its proof by diagram chasing. Apply it to prove that certain canonical morphisms are isomorphisms. Explore variants: the four lemma, the three lemma, and how they all follow from the same principles.

## Common Misconceptions
The five lemma requires exactness of both rows; without exactness, the conclusion fails. Also, the positioning of the morphisms matters—swapping the roles of exactness and commutativity breaks the result.
