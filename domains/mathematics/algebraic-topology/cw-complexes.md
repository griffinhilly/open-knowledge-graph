---
id: cw-complexes
title: CW Complexes
domain: mathematics
course: algebraic-topology
prerequisites:
- id: delta-complexes
  type: hard
- id: quotient-topology
  type: hard
- id: homotopy-definition
  type: soft
builds-toward:
- cellular-homology
- higher-homotopy-groups
- homotopy-exact-sequence-fibration
tags: [algebraic-topology, cw-complexes, cell-structures, homotopy-theory]
stage: expert
status: validated
---
# CW Complexes

## Core Idea
A CW complex is a topological space built inductively by attaching cells (disks) of increasing dimension via continuous maps on their boundaries. Starting from a discrete set of points (0-skeleton), we attach 1-cells (intervals) along their endpoints, then 2-cells (disks) along their boundary circles, and so on. CW complexes are the natural habitat of algebraic topology: they are general enough to model all reasonable topological spaces (every manifold, every polyhedron, every simplicial complex), yet structured enough that homology, cohomology, and homotopy groups can be computed efficiently via cellular methods.

## Questions

```yaml
- question: "The 2-sphere S^2 can be given a CW structure with one 0-cell, zero 1-cells, and one 2-cell. How is the 2-cell attached?"
  type: multiple-choice
  options:
    - "Its boundary circle is mapped homeomorphically to the 1-skeleton"
    - "Its boundary circle is mapped to the single 0-cell (the entire boundary is collapsed to a point)"
    - "Its boundary circle is divided into two arcs mapping to two 1-cells"
    - "This CW structure is impossible — S^2 needs at least one 1-cell"
  answer: 1
  explanation: "The 0-skeleton is a single point. There are no 1-cells, so the 1-skeleton equals the 0-skeleton (still just a point). To form S^2, we attach a 2-cell e^2 with attaching map φ: S^1 → X^1 = {point}. This collapses the entire boundary circle to the point, and the quotient D^2/S^1 is homeomorphic to S^2. This is a minimal CW structure: just one 0-cell and one 2-cell. Compare this to the minimal simplicial triangulation of S^2, which requires 4 vertices, 6 edges, and 4 triangles."

- question: "Every CW complex is a Hausdorff space."
  type: true-false
  answer: true
  explanation: "This is a theorem, not obvious from the definition. The proof uses the 'weak topology' property (the W in CW): a set is closed if and only if its intersection with every finite subcomplex is closed. Combined with the fact that cells are attached via continuous maps from compact Hausdorff spaces (closed disks), this implies the Hausdorff property. The C in CW stands for 'closure-finite' (each cell touches only finitely many other cells), and together these properties ensure CW complexes are well-behaved topological spaces."

- question: "Complex projective space CP^n has a CW structure with one cell in each even dimension: one 0-cell, one 2-cell, one 4-cell, ..., one 2n-cell, and no odd-dimensional cells."
  type: true-false
  answer: true
  explanation: "CP^n = {[z_0 : ... : z_n] | z_i ∈ C} has a natural CW decomposition using the standard affine coordinate charts. The cell e^{2k} consists of points [z_0 : ... : z_k : 0 : ... : 0] with z_k = 1, parametrized by (z_0, ..., z_{k-1}) ∈ C^k ≅ R^{2k}. The attaching map sends the boundary of the 2k-disk to CP^{k-1} via the Hopf-like map. The absence of odd-dimensional cells immediately gives H_{2k+1}(CP^n) = 0 and H_{2k}(CP^n) = Z for 0 ≤ k ≤ n by cellular homology."

- question: "Why are CW complexes preferred over simplicial complexes in modern algebraic topology?"
  type: short-answer
  answer: "CW complexes require far fewer cells than simplicial complexes require simplices to model the same space, because cells can be attached via arbitrary continuous maps (not just face-to-face gluings). S^2 needs 2 cells (CW) vs 14 triangles (simplicial). This economy translates directly to smaller chain complexes in cellular homology, making computations faster. Additionally, many natural constructions in homotopy theory (mapping cones, suspensions, loop spaces) produce CW complexes directly, not simplicial complexes."
  explanation: "The trade-off: simplicial complexes have more rigid combinatorial structure, which is better for computational algorithms (like persistent homology). CW complexes have more flexible attaching maps, which is better for theoretical work and hand computation. For homotopy theory specifically, CW complexes are essential: Whitehead's theorem (a weak homotopy equivalence between CW complexes is a homotopy equivalence) and the CW approximation theorem (every space is weakly equivalent to a CW complex) make CW complexes the canonical representatives of homotopy types."
```

## Explainer

A **CW complex** is built by an inductive process of cell attachment. Start with a discrete set X^0 of points (the **0-skeleton**). The **n-skeleton** X^n is obtained from X^{n-1} by attaching n-cells: for each n-cell e_alpha^n, take a copy of the closed n-disk D^n and glue it to X^{n-1} along a continuous **attaching map** phi_alpha : S^{n-1} = boundary(D^n) -> X^{n-1}. The resulting space is X^n = X^{n-1} union_{phi_alpha} D^n (a quotient of the disjoint union that identifies each point of S^{n-1} with its image under phi_alpha). The CW complex X is the union X = union X^n with the **weak topology**: a set is open in X if and only if its intersection with every X^n is open.

The key feature of CW complexes is the flexibility of the attaching maps. In a simplicial complex, simplices must be glued face-to-face with all vertices distinct. In a CW complex, the attaching map phi : S^{n-1} -> X^{n-1} can be any continuous map — it can collapse part of the boundary, wrap it around multiple times, or map it to a lower-dimensional skeleton. This flexibility allows extremely economical cell structures. The sphere S^n needs only two cells (one 0-cell and one n-cell), the torus needs one 0-cell, two 1-cells, and one 2-cell, and complex projective space CP^n needs just one cell in each even dimension up to 2n.

The **cellular chain complex** of a CW complex gives the most efficient route to computing homology. The n-th cellular chain group is the free abelian group on the n-cells: C_n^{CW}(X) = Z^{number of n-cells}. The cellular boundary operator d_n : C_n^{CW} -> C_{n-1}^{CW} is determined by the degrees of the attaching maps: the coefficient of e^{n-1}_beta in d_n(e^n_alpha) is the degree of the composite map S^{n-1} -> X^{n-1} -> X^{n-1}/X^{n-2} = wedge of (n-1)-spheres -> S^{n-1}_beta. The resulting homology H_n^{CW}(X) is isomorphic to the singular homology H_n(X). For CP^n, the cellular chain complex is 0 -> Z -> 0 -> Z -> 0 -> ... -> Z -> 0, and all boundary maps are zero (since there are no adjacent-dimension cells), immediately giving H_{2k}(CP^n) = Z.

Two fundamental theorems in homotopy theory demonstrate the centrality of CW complexes. **Whitehead's theorem** states that a continuous map between CW complexes that induces isomorphisms on all homotopy groups is a homotopy equivalence. This fails for general spaces but holds for CW complexes because of their inductive cell structure. The **CW approximation theorem** states that every topological space is weakly homotopy equivalent to a CW complex — meaning there exists a CW complex with the same homotopy groups, homology groups, and cohomology groups. Together, these theorems mean that for the purposes of algebraic topology, CW complexes are the canonical class of spaces: every "algebraic topology question" can be answered within the world of CW complexes.
