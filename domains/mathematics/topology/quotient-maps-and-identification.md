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

## Questions

```yaml
- question: "You have a surjective continuous map f from [0,1] (compact) to a Hausdorff space Y. Without checking preimages of every open set, can you conclude f is a quotient map?"
  type: multiple-choice
  options:
    - "No — compactness and Hausdorff are irrelevant; you must verify the open-set condition directly"
    - "Yes — any surjective continuous map is automatically a quotient map"
    - "Yes — a surjective continuous map from a compact space to a Hausdorff space is automatically a quotient map"
    - "Only if f is also injective, making it a homeomorphism"
  answer: 2
  explanation: "The key theorem states: any surjective continuous map from a compact space to a Hausdorff space is a quotient map. The proof uses the fact that in this setting, closed sets in X map to closed sets in Y (a continuous map from compact to Hausdorff is a closed map), which implies the quotient topology condition. This theorem is enormously useful in practice — it lets you verify quotient maps without checking every open set, as long as you can establish compactness and Hausdorff separation."

- question: "Both endpoints of [0,1] are identified: 0 ~ 1, while all other points are equivalent only to themselves. What is the resulting quotient space?"
  type: multiple-choice
  options:
    - "A closed interval [0,1] — identifying two points does not change the topology significantly"
    - "A circle — identifying the endpoints bends the interval and glues them into a single point"
    - "Two separate components — the identified endpoints form one piece, the interior another"
    - "An open interval (0,1) — the identified point at the boundary is removed from the space"
  answer: 1
  explanation: "Identifying the endpoints of [0,1] produces a space homeomorphic to S¹ (the circle). Intuitively, the interval is 'bent' so its two ends meet at a single point, forming a loop. The quotient topology makes this rigorous: an open set in the quotient must have a preimage that is open in [0,1], and the neighborhoods of the identified endpoint must include open sets from both ends of the interval simultaneously — exactly the behavior of a neighborhood of a point on a circle."

- question: "Every surjective continuous map from one topological space to another is a quotient map."
  type: true-false
  answer: false
  explanation: "A continuous bijection that is not a homeomorphism provides a counterexample: the map f: [0,1) → S¹ given by f(t) = e^{2πit} is a continuous bijection, but its inverse is not continuous (the circle topology is 'finer' in the relevant sense). So f is surjective and continuous but not a quotient map — there are open sets in S¹ whose preimages are not open in [0,1). A quotient map requires the stronger condition: V is open in Y if AND ONLY IF f⁻¹(V) is open in X."

- question: "If q: X → Y is a quotient map and X is compact, then Y is compact."
  type: true-false
  answer: true
  explanation: "Continuous images of compact spaces are compact — this is a standard theorem in topology. Since a quotient map is in particular a continuous surjection, Y = q(X) is a continuous image of the compact space X, hence compact. This is one of the few 'nice' properties that quotient maps reliably preserve; Hausdorff separation, for instance, can be lost under quotient maps."

- question: "What property defines a quotient map, and why does this definition give the codomain 'exactly the right topology'?"
  type: short-answer
  answer: "A quotient map q: X → Y is a surjection where V ⊆ Y is open if and only if q⁻¹(V) is open in X. This gives Y the finest topology making q continuous: if you made the topology coarser (fewer open sets), you would lose open sets whose preimages are open; if you made it finer (more open sets), some open set in Y would have a non-open preimage, making q discontinuous. The 'exactly right topology' captures precisely the open structure of X that is visible through the identification — open sets in Y correspond exactly to saturated open sets in X."
  explanation: "The 'if and only if' is crucial. The 'if' direction (open preimage implies open in Y) says the topology is fine enough to include all opens arising from X. The 'only if' direction (open in Y implies open preimage) says the topology is not finer than necessary — every open set in Y must be 'witnessed' by an open set in X. Together, these conditions uniquely characterize the quotient topology as the finest topology making q continuous."
```

## Explainer

From quotient topology you know how to build a new space X/~ by declaring an equivalence relation ~ on X and giving the resulting set of equivalence classes the finest topology making the canonical projection q: X → X/~ continuous. A **quotient map** is a generalization of this projection: any surjective map q: X → Y where Y carries exactly the topology induced by q — meaning a subset V ⊆ Y is open if and only if q⁻¹(V) is open in X. The quotient topology is the finest topology on Y making q continuous, and quotient maps are precisely the continuous surjections that realize this fine topology.

The geometric intuition is *identification* or *gluing*. Start with a square [0,1] × [0,1]. Identify the left and right edges by declaring (0, y) ~ (1, y) for all y. The quotient space is a cylinder. Now additionally identify the top and bottom edges: (x, 0) ~ (x, 1). The quotient is a torus. Quotient maps make these constructions rigorous — the resulting topology on the cylinder or torus is exactly what "feels right" geometrically, because a set is open in the quotient precisely when its preimage (a tube around the identified edge, say) is open in the square. The same pattern builds the Möbius band, projective plane, and Klein bottle by choosing which edges to identify and in which orientation.

Not every surjective continuous map is a quotient map. A continuous bijection that is *not* a homeomorphism provides a counterexample: the map is continuous but its inverse is not, so the topology on the codomain is coarser than the quotient topology. Quotient maps are exactly the surjections that "push forward" the full open structure of X to Y. Crucially, any surjective continuous map from a **compact** space to a **Hausdorff** space is automatically a quotient map — and a homeomorphism if it is also injective. This theorem is why so many constructions in topology work: when you have compactness on the domain and Hausdorff separation on the codomain, continuous surjections are automatically well-behaved.

The central challenge with quotient maps is that they can fail to preserve useful properties. Quotients of Hausdorff spaces need not be Hausdorff (collapsing a closed subspace can create "stuck-together" points). Quotients of compact spaces are compact (continuous images of compact sets are compact). These preservation and failure results govern which spaces can be built by identification. Understanding quotient maps is the prerequisite for Van Kampen's theorem (computing fundamental groups of spaces built by gluing) and the classification of compact surfaces — both of which construct complicated spaces as quotients of simple ones, then analyze the result using the topology of the quotient.
