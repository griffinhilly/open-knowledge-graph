---
id: homeomorphisms-topological-equivalence
title: Homeomorphisms and Topological Equivalence
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-spaces
  type: hard
builds-toward:
- topological-invariants
- classification-compact-surfaces
tags:
- homeomorphisms
- topological-equivalence
- isomorphisms
stage: advanced
status: draft
---

# Homeomorphisms and Topological Equivalence

## Core Idea
A homeomorphism is a continuous bijection with continuous inverse; two spaces are topologically equivalent if a homeomorphism exists between them. Homeomorphisms preserve all topological properties—they capture the intuition that two spaces have the same shape if one can be continuously deformed into the other without tearing or gluing.

## Explainer

In algebra, an isomorphism is a structure-preserving bijection — a map that respects all the operations and whose inverse does too. Topology has the same concept: a **homeomorphism** is the topological version of an isomorphism, a bijection that preserves the open-set structure in both directions. Formally, f: X → Y is a homeomorphism if f is bijective, f is continuous (preimages of open sets are open), and f⁻¹ is also continuous. That third condition is not automatic. A continuous bijection can fail to have a continuous inverse: map [0, 1) onto the circle S¹ by f(t) = (cos 2πt, sin 2πt). This is a continuous bijection, but f⁻¹ is not continuous at the point (1, 0) — a small open arc on the circle maps back to a set that is not open in [0, 1). The two spaces are not homeomorphic.

The power of homeomorphisms is that they make two spaces completely interchangeable for any topological purpose. The open interval (0, 1) and the entire real line ℝ are homeomorphic: the map f(x) = tan(π(x − 1/2)) is a homeomorphism from (0, 1) to ℝ. They "look different" — one is bounded, the other infinite — but boundedness is not a topological concept (it depends on a metric, not just open sets). Both spaces have the same connected components, the same number of holes, the same "local" structure at every point. Topologically they are identical.

To prove two spaces are homeomorphic you must construct an explicit homeomorphism. To prove they are **not** homeomorphic you must find a **topological invariant** — a property preserved by all homeomorphisms — that differs between them. The closed interval [0, 1] and the open interval (0, 1) are not homeomorphic: [0, 1] is compact (every open cover has a finite subcover) and (0, 1) is not. Since compactness is a topological invariant, no homeomorphism can exist. Similarly, a circle (S¹) and a figure-eight (S¹ ∨ S¹) are not homeomorphic: removing one point from S¹ leaves a connected space, but removing the central crossing point of the figure-eight leaves two disconnected arcs.

The topological invariants you will study next — compactness, connectedness, and the fundamental group — are the vocabulary for distinguishing spaces up to homeomorphism. Each invariant is a theorem of the form "if f: X → Y is a homeomorphism, then X and Y have the same [invariant]." The classification program of topology is exactly this: identify all topological spaces up to homeomorphism, and compile enough invariants to tell them apart. For compact surfaces (the sphere, torus, Klein bottle, etc.), this classification is complete — the genus and orientability determine the homeomorphism type.
