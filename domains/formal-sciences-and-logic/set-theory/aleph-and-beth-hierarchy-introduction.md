---
id: aleph-and-beth-hierarchy-introduction
title: The Aleph and Beth Hierarchies of Infinities
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: uncountable-sets-and-the-reals
  type: hard
- id: cardinal-comparison-and-schroeder-bernstein
  type: hard
builds-toward:
- aleph-numbers
- beth-numbers
- continuum-hypothesis
- infinite-cardinal-numbers
tags:
- hierarchy
- infinite-cardinals
- power-sets
stage: formal-systems
status: draft
---

# The Aleph and Beth Hierarchies of Infinities

## Core Idea
The aleph numbers ℵ₀, ℵ₁, ℵ₂, ... enumerate infinite cardinalities in increasing order; ℵ₀ is countable infinity, ℵ₁ the next larger cardinal. The beth numbers ℶ₀, ℶ₁, ℶ₂, ... are defined by iterating power sets: ℶ₀ = ℵ₀, ℶ_{n+1} = 2^{ℶ_n}. The continuum hypothesis asks whether ℶ₁ = ℵ₁.
