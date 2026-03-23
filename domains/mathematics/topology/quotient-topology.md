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
status: validated
---

# Quotient Topology

## Core Idea
The quotient topology is defined on the set of equivalence classes of a topological space under an equivalence relation. A set is open in the quotient if its preimage under the quotient map is open, making the quotient map continuous and the finest topology with this property. This is the natural topology for identifying points or gluing spaces together.

## Questions

```yaml
- question: "A subset U ⊆ X/~ is declared open in the quotient topology when which condition holds?"
  type: multiple-choice
  options:
    - "q(V) = U for some open set V ⊆ X"
    - "q⁻¹(U) is open in X"
    - "U is an open ball of equivalence classes under some metric"
    - "U is contained in the image of an open set of X"
  answer: 1
  explanation: "The quotient topology is defined by declaring U ⊆ X/~ open if and only if its PREIMAGE q⁻¹(U) is open in X. This is exactly what forces the quotient map q to be continuous. Option A is the most tempting wrong answer: it uses images rather than preimages, but q is not generally an open map — the image of an open set need not be open in the quotient. Preimages are the right tool because continuity is defined via preimages."

- question: "A student claims: 'The quotient topology is the coarsest topology on X/~ that makes q continuous.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — this is a correct characterization of the quotient topology"
    - "It is the finest (largest) topology making q continuous, not the coarsest"
    - "The quotient map is never continuous, so no such topology exists"
    - "Coarseness and fineness are not defined for quotient spaces"
  answer: 1
  explanation: "The quotient topology is the FINEST (largest) topology on X/~ making q continuous — it declares as many sets open as possible while still maintaining continuity of q. A coarser topology (fewer open sets) would also make q continuous, since fewer open sets means fewer preimage conditions to check. The indiscrete topology is the coarsest that makes q continuous, but it is trivial and loses all structure. The quotient topology is the natural maximum — the richest topology consistent with continuity of q."

- question: "In the quotient topology, the open sets of X/~ are exactly the images q(U) of open sets U in X."
  type: true-false
  answer: false
  explanation: "This reverses the direction: open sets in X/~ are determined by PREIMAGES, not images. A set V ⊆ X/~ is open iff q⁻¹(V) is open in X. The map q is not generally an open map — it does not need to send open sets to open sets. A concrete example: when [0,1] is collapsed by identifying 0 ~ 1 to form S¹, there are open sets in [0,1] whose images under q are not open in the quotient."

- question: "When building the torus by identifying opposite edges of the unit square, the quotient topology is well-defined even though the resulting space is not a subset of any Euclidean space used in the construction."
  type: true-false
  answer: true
  explanation: "The quotient topology is defined purely in terms of the equivalence relation and the topology on the original space — it does not require the quotient space to be embedded in any ambient Euclidean space. The torus, projective plane, Klein bottle, and many other spaces are naturally constructed as quotients, and their topology is fully determined by the quotient construction. This is precisely the power of the framework: it defines a topology on X/~ intrinsically, not by reference to an embedding."

- question: "Why is the quotient topology defined using preimages of the quotient map q rather than images?"
  type: short-answer
  answer: "Because continuity of q requires that preimages of open sets are open. Defining open sets in X/~ via preimages of q is exactly what forces q to be continuous — and the quotient topology is the finest topology with this property. Images of open sets under q need not be open because q is not generally an open map."
  explanation: "This connects to the fundamental definition of continuity in topology: f is continuous iff the preimage of every open set is open. By defining the quotient topology so that U ⊆ X/~ is open iff q⁻¹(U) is open, we are effectively building continuity of q into the definition of open sets. This also gives the quotient topology its universal property: a function f: X/~ → Y is continuous iff f ∘ q: X → Y is continuous, which is what makes the quotient the 'right' domain for maps that respect the equivalence relation."
```

## Explainer

You already know what equivalence relations are: a relation ~ on a set X that is reflexive, symmetric, and transitive. The **quotient set** X/~ is the set of equivalence classes [x] = {y ∈ X : y ~ x}. The question is: when X is a topological space, how do we put a topology on X/~? The answer is the **quotient topology**, and it is driven by one requirement — the natural map q: X → X/~ defined by q(x) = [x] should be continuous.

Requiring q to be continuous means: for every open set U ⊆ X/~, the preimage q⁻¹(U) must be open in X. The quotient topology takes this as its definition of "open": declare U ⊆ X/~ to be open if and only if q⁻¹(U) is open in X. This is the **finest** (largest) topology on X/~ that makes q continuous — any coarser topology would declare fewer sets open, which is still consistent with continuity, but the quotient topology is the natural maximum.

The canonical example is building a circle from an interval. Take X = [0,1] and define the equivalence relation that identifies the two endpoints: 0 ~ 1, and x ~ x for all other x. The quotient X/~ consists of a single equivalence class {0,1} and all the singletons {x} for x ∈ (0,1). Geometrically, you are gluing the left end of the interval to the right end — folding the interval into a loop. The quotient space is homeomorphic to the circle S¹. The quotient topology is what makes this precise: open sets in the quotient correspond exactly to open arcs in the circle.

A richer example is the **torus**. Start with the unit square [0,1] × [0,1] and identify opposite edges: (0, y) ~ (1, y) for all y (gluing left and right edges) and (x, 0) ~ (x, 1) for all x (gluing top and bottom edges). The result is a torus — the surface of a donut — constructed purely by gluing. The **projective plane** ℝP² is built similarly by identifying antipodal points on a sphere or, equivalently, gluing opposite edges of a square with a twist. These constructions would be impossible to describe cleanly without the quotient topology. The power of the quotient construction is that it lets you build new spaces from familiar ones by declaring which points count as "the same," with the topology inherited automatically through the quotient map.
