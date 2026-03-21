---
id: quotient-maps-definition
title: Quotient Maps and Quotient Topologies
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-definition
  type: hard
- id: quotient-topology
  type: soft
tags:
- quotient-maps
- identification
stage: advanced
status: draft
---

# Quotient Maps and Quotient Topologies

## Core Idea
A surjection q: X → Y is a quotient map if U ⊆ Y is open iff q⁻¹(U) is open. The quotient topology on Y is the finest making q continuous. Quotient maps formalize identification and gluing: the torus is ℝ² with 'opposite edges identified,' projective space ℝP^n is S^n with antipodal points identified.

## Questions

```yaml
- question: "A surjection q: X → Y is continuous. A student concludes that Y therefore has the quotient topology. What is wrong?"
  type: multiple-choice
  options:
    - "Continuous surjections cannot be used to define a topology on Y"
    - "Continuity only requires that preimages of open sets are open — many topologies on Y can make q continuous, and the quotient topology is specifically the finest (largest) such topology"
    - "The student is correct: any topology making q continuous is by definition the quotient topology"
    - "The quotient topology requires q to be injective as well as surjective"
  answer: 1
  explanation: "Continuity is a one-directional condition: U open implies q⁻¹(U) open. The quotient topology is defined by the biconditional: U is open if AND ONLY IF q⁻¹(U) is open. Many topologies on Y (including the indiscrete topology) make q continuous; the quotient topology is the finest one — it admits as many open sets as the map allows. Confusing 'a topology making q continuous' with 'the quotient topology' is the core error."

- question: "If q: X → Y is a quotient map, what is the most efficient way to verify that a function f: Y → Z is continuous?"
  type: multiple-choice
  options:
    - "Show that f maps closed sets to closed sets in Z"
    - "Show that f is injective and the preimage of every open set is saturated"
    - "Show that the composition f ∘ q: X → Z is continuous — the universal property of quotient maps lets you work upstairs in X"
    - "Show that f preserves the equivalence relation used to construct Y"
  answer: 2
  explanation: "This is the universal property of quotient maps: f: Y → Z is continuous if and only if f ∘ q: X → Z is continuous. Since X is often a simpler, better-understood space, this lets you verify continuity of maps out of quotient spaces without working directly with the quotient topology — you lift the problem up to X where standard tools apply."

- question: "The quotient topology on Y is the coarsest (fewest open sets) topology making q continuous."
  type: true-false
  answer: false
  explanation: "The quotient topology is the FINEST topology making q continuous — it contains as many open sets as possible (every set whose preimage under q is open). A coarser topology would discard some of these open sets, losing topological information that q's structure allows. The indiscrete topology {∅, Y} is the coarsest making q continuous, but it contains almost no information about the space."

- question: "When a torus is constructed as a quotient of the unit square [0,1]², the topology on the torus is completely determined by which subsets of the square are open — no embedding in ℝ³ is needed."
  type: true-false
  answer: true
  explanation: "This is the power of the quotient construction. The quotient map q sends each point of the square to its equivalence class under the edge identifications. The quotient topology on the torus declares U open iff q⁻¹(U) is open in [0,1]². This gives a rigorous, intrinsic definition of the torus's topology without any reference to geometry or embedding in three-dimensional space."

- question: "Explain in your own words why the biconditional in the definition of a quotient map — 'U is open if and only if q⁻¹(U) is open' — is stronger than mere continuity, and why this matters for the resulting topology on Y."
  type: short-answer
  answer: "Continuity is one direction: q continuous means q⁻¹(U) open whenever U is open. The quotient map adds the converse: if q⁻¹(U) is open, then U must be open. This biconditional means the topology of Y is entirely determined by q — Y has exactly the open sets that q 'lets through,' making it the finest possible topology consistent with q. A weaker topology would discard topological information; a stronger one would require q to be an open map, which quotient maps need not be."
  explanation: "The biconditional ensures the quotient topology captures the full topological content of the identification. Any coarser topology would declare some set U closed even though q⁻¹(U) is open, destroying information about the space. The finest topology condition is what makes quotient spaces well-defined and gives them the universal property: maps out of Y are continuous iff their composition with q is continuous."
```

## Explainer

From continuity of topological spaces, you know that a map f: X → Y is continuous when preimages of open sets are open: U open in Y implies f⁻¹(U) open in X. This is the "weak" condition — continuity only flows one way. A **quotient map** q: X → Y strengthens this to a biconditional: U ⊆ Y is open *if and only if* q⁻¹(U) is open in X. The topology on Y is completely determined by q — Y has exactly the open sets that q "lets through." This makes q the most topologically faithful type of surjection: the topology of Y is not just compatible with q but is entirely defined by it.

The canonical motivation is gluing. Take a square [0,1] × [0,1] and identify the left and right edges: declare that (0, t) and (1, t) are "the same point" for every t ∈ [0, 1]. The result is a cylinder. Then identify top and bottom edges of the cylinder: (s, 0) and (s, 1) become the same. The result is a torus. The quotient map q sends each point of the square to its equivalence class under these identifications, and the quotient topology on the torus is precisely: a set U in the torus is open iff its preimage in the square is open. This construction is completely precise — you do not need to embed the torus in ℝ³ or describe its geometry. The topology is entirely determined by the identification rule and the continuity condition.

The **quotient topology** on Y is the finest (largest) topology making q continuous. "Finest" means as many open sets as possible: since q is continuous iff preimages of opens are open, we put in every set whose preimage is open. Any coarser topology would declare some set U closed even though q⁻¹(U) is open — discarding topological information. The quotient topology keeps everything the map allows. A useful consequence: a map f: Y → Z out of a quotient space Y is continuous iff the composition f ∘ q: X → Z is continuous. This is the **universal property** of quotient maps, and it means you can check continuity of maps *out of* quotient spaces by working upstairs in X, where life is often simpler.

The power of quotient maps in practice is that they generate all the important non-trivial topological spaces from simple ones. The projective plane ℝP² is S² with antipodal points identified — q: S² → ℝP² collapses each pair {x, −x} to a single point. The Möbius band is a rectangle with one pair of opposite edges identified with a flip. These are not merely metaphors or embeddings in 3-space: they are precisely defined topological spaces, and their topology (which sets are open) is given by the quotient map definition. Whenever you see a description like "X with these points identified" or "X modulo the equivalence relation ∼," you are seeing a quotient space, and the quotient map is the projection sending each point to its equivalence class. The biconditional in the definition — not just preimages of opens are open, but conversely — is what ensures the quotient space captures the full topological content of the identification.
