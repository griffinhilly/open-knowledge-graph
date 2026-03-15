---
id: limits-and-colimits
title: Limits and Colimits
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: products-and-coproducts
  type: hard
- id: equalizers-and-coequalizers
  type: hard
- id: functor-categories
  type: soft
- id: natural-transformations
  type: soft
- id: comma-categories
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: soft
builds-toward:
- pullbacks-and-pushouts
- adjoint-functors
- yoneda-lemma
tags:
- limit
- colimit
- cone
- cocone
- diagram
- completeness
stage: advanced
status: validated
---
# Limits and Colimits

## Core Idea
A limit of a diagram (functor) D: J → C is a terminal cone over D: an object L with morphisms to each D(j) compatible with the diagram, such that any other cone factors uniquely through L. Colimits are dual: initial cocones. Limits generalize products, equalizers, and pullbacks; colimits generalize coproducts, coequalizers, and pushouts. A category is complete if it has all small limits, and cocomplete if it has all small colimits; most categories arising in practice (Set, Grp, Top, Ab) are both complete and cocomplete.

## How It's Best Learned
Unify previously studied constructions: verify that products are limits over a discrete two-object diagram, equalizers are limits over a diagram with two parallel arrows, and terminal objects are limits over the empty diagram. Dually identify coproducts, coequalizers, and initial objects as colimits.

## Common Misconceptions
- Limits are not the same as limits of sequences in analysis, though filtered colimits capture directed limits of sequences in suitable categories.
- A limit is not just 'the smallest' object fitting a diagram; the universal property (unique factorization) is essential.
- Limits and colimits may fail to exist in a given category, and completeness must be verified, not assumed.
