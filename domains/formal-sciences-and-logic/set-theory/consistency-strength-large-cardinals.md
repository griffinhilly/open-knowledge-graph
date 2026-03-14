---
id: consistency-strength-large-cardinals
title: Consistency Strength and the Large-Cardinal Hierarchy
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: large-cardinals-intro
  type: hard
- id: measurable-cardinals-ultra-filters
  type: soft
builds-toward:
- inner-models-relative-consistency
tags:
- consistency-strength
- large-cardinals
- hierarchy
- provability
stage: formal-systems
status: draft
---

# Consistency Strength and the Large-Cardinal Hierarchy

## Core Idea
Large cardinals are ordered by consistency strength: the existence of an inaccessible is consistent with ZFC but strictly stronger than ZFC; the existence of a measurable is strictly stronger than inaccessible; supercompacts are stronger still. This hierarchy is studied via inner models and reflection principles. Consistency strength provides a refined notion of 'how much you add' when extending ZFC.

## How It's Best Learned
Introduce the Veblen hierarchy of inaccessible, measurable, supercompact, and extendible cardinals. Show consistency of large-cardinal axioms is unprovable in ZFC by Gödel's incompleteness. Use inner-model theory (L, HOD, V) to compare consistency strengths.

## Common Misconceptions
- Assuming all large cardinals are 'equally large' (the consistency hierarchy reveals subtle differences).
- Conflating the cardinal itself being large with its consistency-strength; a weakly compact cardinal has lower consistency strength than many 'smaller' cardinals by ordinal comparison.
