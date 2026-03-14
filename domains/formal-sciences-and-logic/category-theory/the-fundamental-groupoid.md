---
id: the-fundamental-groupoid
title: The Fundamental Groupoid of a Space
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: groupoids-and-weak-inverses
  type: hard
builds-toward:
- enriched-categories
tags:
- fundamental-group
- paths
- homotopy
- topological-invariant
stage: abstract-reasoning
status: draft
---

# The Fundamental Groupoid of a Space

## Core Idea
The fundamental groupoid of a topological space has points as objects and homotopy classes of paths as morphisms, with composition given by path concatenation. Unlike the fundamental group (which depends on a basepoint choice), the fundamental groupoid is base-point-free and captures the full homotopy-theoretic information of the space. It provides a more natural and categorical framework for studying connectivity.

## How It's Best Learned
Compute the fundamental groupoid of familiar spaces: the circle, the plane, a figure-eight. Verify that morphisms are invertible and explore how groupoid structure reflects topological properties. Understand the relationship between the fundamental groupoid and fundamental groups at various basepoints.

## Common Misconceptions
The fundamental groupoid is not the same as the fundamental group; it encodes information at all points simultaneously. The automorphism group at a point is the fundamental group at that basepoint, but the groupoid structure includes much more.
