---
id: simplicial-homology-groups
title: Simplicial Homology Groups
domain: mathematics
course: algebraic-topology
prerequisites:
- id: chain-complexes-boundary-operator
  type: hard
- id: quotient-groups
  type: hard
builds-toward:
- euler-characteristic-homology
- singular-homology-groups
- homology-with-coefficients
tags: [algebraic-topology, simplicial-homology, homology-groups, cycles, boundaries]
stage: expert
status: validated
---
# Simplicial Homology Groups

## Core Idea
The n-th simplicial homology group H_n(K) = ker(d_n)/im(d_{n+1}) measures the n-dimensional "holes" in a simplicial complex K. Elements of H_n are equivalence classes of n-cycles (chains with zero boundary) modulo n-boundaries (chains that bound (n+1)-dimensional regions). H_0 counts connected components, H_1 detects loops that do not bound surfaces, and H_2 detects enclosed cavities. Homology groups are computable topological invariants — different triangulations of the same space yield isomorphic groups.

## Questions

```yaml
- question: "A simplicial complex K has H_0(K) ≅ Z ⊕ Z. What does this tell you about K?"
  type: multiple-choice
  options:
    - "K has exactly two 1-dimensional holes"
    - "K has exactly two connected components"
    - "K is the 2-sphere"
    - "K has two independent 0-cycles that do not bound any 1-chain"
  answer: 1
  explanation: "H_0 measures path-connectivity: its rank equals the number of connected components. Each connected component contributes one copy of Z to H_0. With H_0 ≅ Z ⊕ Z, K has exactly two connected components. Option D is technically true (it restates the algebra) but B is the geometric interpretation. The 0-cycles are formal sums of vertices, and two vertices are homologous (differ by a boundary) if and only if they are connected by a path of edges."

- question: "For the triangulated torus T², the homology groups are H_0 ≅ Z, H_1 ≅ Z ⊕ Z, and H_2 ≅ Z. What does the generator of H_2 represent?"
  type: multiple-choice
  options:
    - "A single triangle on the surface of the torus"
    - "The fundamental cycle — the sum of all oriented 2-simplices forming the closed surface, which encloses a cavity but does not bound any 3-chain in the complex"
    - "The product of the two generating loops of H_1"
    - "The Euler characteristic of the torus"
  answer: 1
  explanation: "The generator of H_2(T²) is the fundamental cycle: the sum of all 2-simplices of the triangulation, oriented consistently. This 2-cycle has zero boundary (the surface is closed — every edge is shared by exactly two triangles with compatible orientations), but it is not the boundary of any 3-chain (there is no 3-dimensional 'filling' in the complex). This generator detects the cavity enclosed by the torus. The single copy of Z reflects that the torus is a connected, orientable, closed surface."

- question: "Two different triangulations of the same topological space always yield isomorphic simplicial homology groups."
  type: true-false
  answer: true
  explanation: "This is a deep theorem: simplicial homology is a topological invariant, not dependent on the choice of triangulation. The proof proceeds by showing that simplicial homology agrees with singular homology (which is defined without reference to any triangulation). Alternatively, one can show directly that subdivisions and simplicial approximations relate different triangulations without changing homology. This invariance is what makes homology useful — it extracts topological information that does not depend on the combinatorial presentation."

- question: "A simplicial complex K has H_1(K) ≅ Z ⊕ Z/2Z. Describe what the Z and Z/2Z summands represent geometrically."
  type: short-answer
  answer: "The Z summand corresponds to a 1-cycle (loop) that is not a boundary and has infinite order — going around it any number of times never becomes a boundary. The Z/2Z summand corresponds to a 1-cycle that is not itself a boundary, but going around it twice IS a boundary. This torsion element reflects a non-orientability phenomenon: the complex contains something like a Mobius band where traversing the core circle twice produces a boundary."
  explanation: "Torsion in homology detects subtle topological features beyond simple holes. The real projective plane RP² has H_1 ≅ Z/2Z because its core loop, traversed once, does not bound a 2-chain, but traversed twice it does (the loop 'unwraps' on the double cover S²). Spaces with both free and torsion summands in homology combine 'hole-like' and 'non-orientability-like' features."

- question: "Explain why im(d_{n+1}) is always a subgroup of ker(d_n), and why this inclusion is what makes the quotient H_n = ker(d_n)/im(d_{n+1}) well-defined."
  type: short-answer
  answer: "The property d_n ∘ d_{n+1} = 0 means that for any (n+1)-chain c, d_n(d_{n+1}(c)) = 0. So d_{n+1}(c) is in ker(d_n) for every c, which means im(d_{n+1}) ⊆ ker(d_n). Since im(d_{n+1}) is a subgroup of the abelian group ker(d_n), the quotient ker(d_n)/im(d_{n+1}) is a well-defined abelian group. This quotient identifies two cycles as 'the same' precisely when they differ by a boundary, which is the fundamental equivalence relation of homology."
  explanation: "If im(d_{n+1}) were not contained in ker(d_n), the quotient would be undefined. The condition d ∘ d = 0 is not just a technical convenience but the core structural property that makes homology theory possible. Every construction in homological algebra — singular homology, cellular homology, de Rham cohomology — rests on this same foundational property of chain complexes."
```

## Explainer

Given a simplicial complex K with its chain complex ... -> C_2(K) -d_2-> C_1(K) -d_1-> C_0(K) -> 0, the **n-th simplicial homology group** is the quotient H_n(K) = ker(d_n) / im(d_{n+1}). The kernel ker(d_n), called the group of **n-cycles** and denoted Z_n, consists of all n-chains whose boundary is zero. The image im(d_{n+1}), called the group of **n-boundaries** and denoted B_n, consists of all n-chains that are boundaries of (n+1)-chains. Since d_n compose d_{n+1} = 0, every boundary is a cycle (B_n is a subgroup of Z_n), and the homology group H_n = Z_n / B_n measures how much larger the cycle group is than the boundary group — cycles that are not boundaries represent genuine "holes."

The **zeroth homology** H_0(K) counts connected components. A 0-chain is a formal sum of vertices, and its boundary is zero (there is no d_{-1}), so every 0-chain is a cycle. A 0-boundary is d_1 of some 1-chain — for an edge [a,b], d_1([a,b]) = b - a. Two vertices are homologous (represent the same element of H_0) if and only if they are connected by a path of edges. Thus H_0(K) is a free abelian group with one generator per connected component. For a connected complex, H_0 is simply Z.

**First homology** H_1(K) detects 1-dimensional holes — loops that cannot be filled. A 1-cycle is a chain of edges forming a closed loop (every vertex appears as many times as a head as it does as a tail). A 1-boundary is the boundary of a 2-chain — a sum of triangles whose boundary edges form the loop. If the loop bounds a filled region, it is a boundary and represents zero in H_1. If the loop surrounds a hole (a missing interior), it is a cycle but not a boundary, representing a nontrivial homology class. For example, the triangulated torus has H_1 isomorphic to Z direct sum Z, with generators being the two fundamental loops (around the hole and through the tube) — neither loop can be filled by triangles in the torus.

**Higher homology** works analogously. H_2(K) detects 2-dimensional "cavities" — closed surfaces that do not bound solid regions. The triangulated 2-sphere has H_2 isomorphic to Z: the entire sphere is a 2-cycle (a closed surface with no boundary edges), but it does not bound any 3-chain (there is no solid ball in the complex). The Betti numbers b_n = rank(H_n) count the number of independent n-dimensional holes: b_0 is the number of components, b_1 the number of independent tunnels or loops, b_2 the number of enclosed cavities. Torsion elements (elements of finite order) in H_n detect more subtle phenomena related to non-orientability: the real projective plane has H_1 isomorphic to Z/2Z because its central loop, traversed twice, bounds a disk in the projective plane.

The remarkable fact about simplicial homology — and what makes it a central tool in topology — is its **topological invariance**: homeomorphic spaces have isomorphic homology groups, regardless of how they are triangulated. This means homology genuinely measures the shape of a space, not an artifact of its combinatorial presentation. Computing simplicial homology reduces to linear algebra: write down the boundary matrices, compute their kernels and images (via row reduction over Z), and take the quotient. This algorithmic computability, combined with topological invariance, makes simplicial homology one of the most powerful and practical invariants in all of topology.
