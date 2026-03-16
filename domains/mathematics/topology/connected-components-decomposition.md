---
id: connected-components-decomposition
title: Connected Components
domain: mathematics
course: topology
prerequisites:
- id: connected-spaces-definition
  type: hard
tags:
- connected-components
- decomposition
stage: abstract-reasoning
status: draft
---

# Connected Components

## Core Idea
The connected component of a point x is the maximal connected subset containing x. Connected components partition X into connected pieces. A space is connected iff it has one component. Component spaces are topological invariants; they classify spaces into their 'pieces.' Connected components of the identity in topological groups are normal subgroups.

## Explainer

You already know what it means for a topological space to be connected: it cannot be written as a union of two disjoint nonempty open sets. Now the natural follow-up question is: what if the space *isn't* connected? How do we systematically decompose it into its connected "pieces"? That is exactly what connected components formalize.

The **connected component** of a point x is defined as the union of all connected subsets of X that contain x. This is always well-defined because the union of connected sets that share a common point is itself connected — so the union is still connected, and it is the largest such set. Every point belongs to exactly one component, so the components **partition** X: every point is in precisely one piece, and no two pieces overlap. If X is already connected, there is just one component — all of X. At the other extreme, if X carries the discrete topology (every subset is open), each singleton {x} is its own component, and the space has as many pieces as it has points.

A useful example: take ℝ and remove the rationals. The resulting space of irrationals is **totally disconnected** — every connected component is a single point. Between any two irrationals there is a rational, which has been removed, so no interval of irrationals can be connected (any two-point subset can be separated by choosing a rational between them). Compare this to ℝ itself, which is connected (one component), or to a figure-eight graph, which is connected, or to two disjoint circles, which has two components. Counting components is a rough but useful measure of a space's "connectivity."

Connected components are **topological invariants**: any homeomorphism between spaces must map components of one space bijectively onto components of the other. This makes the number of components a tool for distinguishing spaces — if two spaces have different numbers of components, no homeomorphism between them exists. In topological groups — structures that are simultaneously groups and topological spaces, with the group operations continuous — the connected component of the identity element is always a **normal subgroup**. This connects topological structure to algebraic structure and is a foundational fact in the theory of Lie groups, where the component of the identity is often the most important part of the group.
