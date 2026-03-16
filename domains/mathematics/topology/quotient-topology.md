---
id: quotient-topology
title: Quotient Topology
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
- id: equivalence-relations
  type: hard
builds-toward:
- quotient-maps-and-identification
- classification-compact-surfaces
tags:
- quotient-topology
- identification-spaces
- equivalence-classes
stage: advanced
status: draft
---

# Quotient Topology

## Core Idea
The quotient topology is defined on the set of equivalence classes of a topological space under an equivalence relation. A set is open in the quotient if its preimage under the quotient map is open, making the quotient map continuous and the finest topology with this property. This is the natural topology for identifying points or gluing spaces together.

## Explainer

You already know what equivalence relations are: a relation ~ on a set X that is reflexive, symmetric, and transitive. The **quotient set** X/~ is the set of equivalence classes [x] = {y ∈ X : y ~ x}. The question is: when X is a topological space, how do we put a topology on X/~? The answer is the **quotient topology**, and it is driven by one requirement — the natural map q: X → X/~ defined by q(x) = [x] should be continuous.

Requiring q to be continuous means: for every open set U ⊆ X/~, the preimage q⁻¹(U) must be open in X. The quotient topology takes this as its definition of "open": declare U ⊆ X/~ to be open if and only if q⁻¹(U) is open in X. This is the **finest** (largest) topology on X/~ that makes q continuous — any coarser topology would declare fewer sets open, which is still consistent with continuity, but the quotient topology is the natural maximum.

The canonical example is building a circle from an interval. Take X = [0,1] and define the equivalence relation that identifies the two endpoints: 0 ~ 1, and x ~ x for all other x. The quotient X/~ consists of a single equivalence class {0,1} and all the singletons {x} for x ∈ (0,1). Geometrically, you are gluing the left end of the interval to the right end — folding the interval into a loop. The quotient space is homeomorphic to the circle S¹. The quotient topology is what makes this precise: open sets in the quotient correspond exactly to open arcs in the circle.

A richer example is the **torus**. Start with the unit square [0,1] × [0,1] and identify opposite edges: (0, y) ~ (1, y) for all y (gluing left and right edges) and (x, 0) ~ (x, 1) for all x (gluing top and bottom edges). The result is a torus — the surface of a donut — constructed purely by gluing. The **projective plane** ℝP² is built similarly by identifying antipodal points on a sphere or, equivalently, gluing opposite edges of a square with a twist. These constructions would be impossible to describe cleanly without the quotient topology. The power of the quotient construction is that it lets you build new spaces from familiar ones by declaring which points count as "the same," with the topology inherited automatically through the quotient map.
