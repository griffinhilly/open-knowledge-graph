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
stage: abstract-reasoning
status: draft
---

# Quotient Maps and Quotient Topologies

## Core Idea
A surjection q: X → Y is a quotient map if U ⊆ Y is open iff q⁻¹(U) is open. The quotient topology on Y is the finest making q continuous. Quotient maps formalize identification and gluing: the torus is ℝ² with 'opposite edges identified,' projective space ℝP^n is S^n with antipodal points identified.

## Explainer

From continuity of topological spaces, you know that a map f: X → Y is continuous when preimages of open sets are open: U open in Y implies f⁻¹(U) open in X. This is the "weak" condition — continuity only flows one way. A **quotient map** q: X → Y strengthens this to a biconditional: U ⊆ Y is open *if and only if* q⁻¹(U) is open in X. The topology on Y is completely determined by q — Y has exactly the open sets that q "lets through." This makes q the most topologically faithful type of surjection: the topology of Y is not just compatible with q but is entirely defined by it.

The canonical motivation is gluing. Take a square [0,1] × [0,1] and identify the left and right edges: declare that (0, t) and (1, t) are "the same point" for every t ∈ [0, 1]. The result is a cylinder. Then identify top and bottom edges of the cylinder: (s, 0) and (s, 1) become the same. The result is a torus. The quotient map q sends each point of the square to its equivalence class under these identifications, and the quotient topology on the torus is precisely: a set U in the torus is open iff its preimage in the square is open. This construction is completely precise — you do not need to embed the torus in ℝ³ or describe its geometry. The topology is entirely determined by the identification rule and the continuity condition.

The **quotient topology** on Y is the finest (largest) topology making q continuous. "Finest" means as many open sets as possible: since q is continuous iff preimages of opens are open, we put in every set whose preimage is open. Any coarser topology would declare some set U closed even though q⁻¹(U) is open — discarding topological information. The quotient topology keeps everything the map allows. A useful consequence: a map f: Y → Z out of a quotient space Y is continuous iff the composition f ∘ q: X → Z is continuous. This is the **universal property** of quotient maps, and it means you can check continuity of maps *out of* quotient spaces by working upstairs in X, where life is often simpler.

The power of quotient maps in practice is that they generate all the important non-trivial topological spaces from simple ones. The projective plane ℝP² is S² with antipodal points identified — q: S² → ℝP² collapses each pair {x, −x} to a single point. The Möbius band is a rectangle with one pair of opposite edges identified with a flip. These are not merely metaphors or embeddings in 3-space: they are precisely defined topological spaces, and their topology (which sets are open) is given by the quotient map definition. Whenever you see a description like "X with these points identified" or "X modulo the equivalence relation ∼," you are seeing a quotient space, and the quotient map is the projection sending each point to its equivalence class. The biconditional in the definition — not just preimages of opens are open, but conversely — is what ensures the quotient space captures the full topological content of the identification.
