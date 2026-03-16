---
id: quotient-maps-and-identification
title: Quotient Maps and Identification Spaces
domain: mathematics
course: topology
prerequisites:
- id: quotient-topology
  type: hard
- id: open-and-closed-maps
  type: soft
builds-toward:
- van-kampen-theorem
- classification-compact-surfaces
tags:
- quotient-maps
- identification-spaces
- gluing
stage: advanced
status: draft
---

# Quotient Maps and Identification Spaces

## Core Idea
A quotient map q: X → Y is a surjective function where Y carries the quotient topology relative to q—a set is open iff its preimage is open. Quotient maps formalize the process of identifying points or gluing spaces together. Understanding when quotient maps are homeomorphisms and when they preserve properties like compactness is essential for constructing new spaces.

## Explainer

From quotient topology you know how to build a new space X/~ by declaring an equivalence relation ~ on X and giving the resulting set of equivalence classes the finest topology making the canonical projection q: X → X/~ continuous. A **quotient map** is a generalization of this projection: any surjective map q: X → Y where Y carries exactly the topology induced by q — meaning a subset V ⊆ Y is open if and only if q⁻¹(V) is open in X. The quotient topology is the finest topology on Y making q continuous, and quotient maps are precisely the continuous surjections that realize this fine topology.

The geometric intuition is *identification* or *gluing*. Start with a square [0,1] × [0,1]. Identify the left and right edges by declaring (0, y) ~ (1, y) for all y. The quotient space is a cylinder. Now additionally identify the top and bottom edges: (x, 0) ~ (x, 1). The quotient is a torus. Quotient maps make these constructions rigorous — the resulting topology on the cylinder or torus is exactly what "feels right" geometrically, because a set is open in the quotient precisely when its preimage (a tube around the identified edge, say) is open in the square. The same pattern builds the Möbius band, projective plane, and Klein bottle by choosing which edges to identify and in which orientation.

Not every surjective continuous map is a quotient map. A continuous bijection that is *not* a homeomorphism provides a counterexample: the map is continuous but its inverse is not, so the topology on the codomain is coarser than the quotient topology. Quotient maps are exactly the surjections that "push forward" the full open structure of X to Y. Crucially, any surjective continuous map from a **compact** space to a **Hausdorff** space is automatically a quotient map — and a homeomorphism if it is also injective. This theorem is why so many constructions in topology work: when you have compactness on the domain and Hausdorff separation on the codomain, continuous surjections are automatically well-behaved.

The central challenge with quotient maps is that they can fail to preserve useful properties. Quotients of Hausdorff spaces need not be Hausdorff (collapsing a closed subspace can create "stuck-together" points). Quotients of compact spaces are compact (continuous images of compact sets are compact). These preservation and failure results govern which spaces can be built by identification. Understanding quotient maps is the prerequisite for Van Kampen's theorem (computing fundamental groups of spaces built by gluing) and the classification of compact surfaces — both of which construct complicated spaces as quotients of simple ones, then analyze the result using the topology of the quotient.
