---
id: mayer-vietoris-sequence
title: The Mayer-Vietoris Sequence
domain: mathematics
course: algebraic-topology
prerequisites:
- id: relative-homology-long-exact-sequence
  type: hard
- id: excision-theorem
  type: hard
- id: exact-sequences-homological-algebra
  type: soft
builds-toward:
- homology-of-spheres
- kunneth-formula
tags: [algebraic-topology, mayer-vietoris, computation, exact-sequences]
stage: expert
status: validated
---
# The Mayer-Vietoris Sequence

## Core Idea
The Mayer-Vietoris sequence is the homological analogue of the inclusion-exclusion principle: it computes the homology of a union X = A union B from the homology groups of A, B, and their intersection A intersect B. The long exact sequence ... -> H_n(A intersect B) -> H_n(A) + H_n(B) -> H_n(X) -> H_{n-1}(A intersect B) -> ... systematically relates these groups, and the connecting homomorphism captures how the topology of the intersection constrains the topology of the whole. It is the primary computational tool for singular homology.

## Questions

```yaml
- question: "In the Mayer-Vietoris sequence for X = A ∪ B, the map H_n(A ∩ B) → H_n(A) ⊕ H_n(B) sends [c] to (i_*[c], j_*[c]) where i, j are the inclusions. What does it mean when this map is injective?"
  type: multiple-choice
  options:
    - "Every cycle in A ∩ B that becomes trivial in A also becomes trivial in B"
    - "Every cycle in A ∩ B that becomes trivial in both A and B separately is already trivial in A ∩ B"
    - "A ∩ B is a deformation retract of A"
    - "H_n(X) ≅ H_n(A) ⊕ H_n(B)"
  answer: 1
  explanation: "Injectivity of the map (i_*, -j_*) means: if a cycle c in A ∩ B becomes a boundary both in A and in B, then c was already a boundary in A ∩ B. Equivalently: no nontrivial cycle of A ∩ B is 'killed' by passing to A and B simultaneously. By exactness, injectivity of this map forces the connecting homomorphism H_n(X) → H_{n-1}(A ∩ B) to be zero, which means the sequence splits into short exact sequences 0 → coker → H_n(X) → ker → 0, simplifying the computation."

- question: "Using Mayer-Vietoris with A and B as open hemispheres of S^n, the connecting homomorphism H_n(S^n) → H_{n-1}(S^{n-1}) is an isomorphism for n ≥ 2."
  type: true-false
  answer: true
  explanation: "Both hemispheres are contractible, so H_k(A) = H_k(B) = 0 for k > 0. The Mayer-Vietoris sequence gives: 0 → H_n(S^n) → H_{n-1}(S^{n-1}) → 0 for n ≥ 2, since the terms H_n(A) ⊕ H_n(B) and H_{n-1}(A) ⊕ H_{n-1}(B) vanish. By exactness, the connecting homomorphism is an isomorphism. This is the key step in the inductive computation of H_*(S^n)."

- question: "Compute H_1 of the torus T^2 using Mayer-Vietoris, decomposing T^2 as the union of two open cylinders."
  type: short-answer
  answer: "Let A and B be open neighborhoods of the two half-tori, each homotopy equivalent to S^1 (deformation retracting to a circle). Their intersection A ∩ B is two disjoint open annuli, each homotopy equivalent to S^1, so H_1(A ∩ B) ≅ Z ⊕ Z and H_0(A ∩ B) ≅ Z ⊕ Z. The Mayer-Vietoris sequence gives: H_1(A ∩ B) → H_1(A) ⊕ H_1(B) → H_1(T^2) → H_0(A ∩ B) → H_0(A) ⊕ H_0(B). This is Z^2 → Z^2 → H_1(T^2) → Z^2 → Z^2. Working out the maps: the first map is [1,1; 1,1] (both circles in A ∩ B include to the same generator in each piece), which has kernel Z. Chasing through gives H_1(T^2) ≅ Z^2."
  explanation: "The Mayer-Vietoris computation for the torus is a standard exercise. The key subtlety is tracking the inclusion maps carefully — each component of A ∩ B maps to A and B, and the relationship between these maps determines the kernel and cokernel that produce H_1(T^2). This computation is much more tractable than working directly with singular chains, demonstrating the power of the Mayer-Vietoris sequence."

- question: "The Mayer-Vietoris sequence is the homological analogue of which principle from combinatorics?"
  type: multiple-choice
  options:
    - "The pigeonhole principle"
    - "Inclusion-exclusion: |A ∪ B| = |A| + |B| - |A ∩ B|"
    - "The binomial theorem"
    - "Burnside's lemma"
  answer: 1
  explanation: "Inclusion-exclusion for cardinalities says |A ∪ B| = |A| + |B| - |A ∩ B|. The Mayer-Vietoris sequence is the homological upgrade: it relates H_*(A ∪ B) to H_*(A), H_*(B), and H_*(A ∩ B). The Euler characteristic satisfies the exact analogue: χ(A ∪ B) = χ(A) + χ(B) - χ(A ∩ B), which follows from the Mayer-Vietoris sequence. But the full long exact sequence carries more information than just the alternating sum — it encodes how cycles in the pieces interact."
```

## Explainer

The **Mayer-Vietoris sequence** is the most frequently used computational tool in homology. Suppose X = A union B, where A and B are open subsets (or more generally, the interiors of A and B cover X). Then there is a long exact sequence: ... -> H_n(A intersect B) -(i_*,-j_*)-> H_n(A) direct sum H_n(B) -(k_*+l_*)-> H_n(X) -partial-> H_{n-1}(A intersect B) -> ... The first map sends a class [c] in H_n(A intersect B) to the pair (i_*[c], -j_*[c]) of its images in A and B (with a sign chosen for exactness). The second map adds the images of classes in A and B to produce a class in X. The connecting homomorphism partial links the homology of X in one dimension to the homology of the intersection in one dimension lower.

The derivation of Mayer-Vietoris from excision and the long exact sequence of a pair is instructive. Start with the pair (X, A). Its long exact sequence involves H_n(X, A). Excision (with Z = X \ B, noting cl(X \ B) subset int(A) when {int(A), int(B)} covers X) gives H_n(X, A) = H_n(B, A intersect B). Now the long exact sequence of the pair (B, A intersect B) involves H_n(A intersect B) and H_n(B). Splicing these two long exact sequences together and rearranging yields the Mayer-Vietoris sequence. Understanding this derivation shows that Mayer-Vietoris is not a separate axiom but a consequence of the more fundamental excision property.

The Mayer-Vietoris sequence is most powerful when A, B, or A intersect B have simple homology. The classic example is the computation of H_*(S^n) by covering the sphere with two contractible hemispheres whose intersection is S^{n-1}. Since contractible spaces have trivial higher homology, the Mayer-Vietoris sequence collapses to isomorphisms H_k(S^n) = H_{k-1}(S^{n-1}) for k >= 2, giving the homology of all spheres by induction. For surfaces, one typically decomposes into pieces that retract to graphs or circles, and the Mayer-Vietoris sequence assembles the answer from these simple building blocks.

The Mayer-Vietoris sequence also exists for cohomology (with arrows reversed) and for reduced homology (which simplifies the low-dimensional terms). There are relative versions for pairs and versions for arbitrary coverings (the Mayer-Vietoris spectral sequence). The Euler characteristic satisfies the clean formula chi(A union B) = chi(A) + chi(B) - chi(A intersect B), which follows immediately from the exactness of the Mayer-Vietoris sequence and the additivity of the Euler characteristic on exact sequences. This "inclusion-exclusion for topology" is one of the most elegant consequences of the sequence and reinforces its role as the homological upgrade of a familiar combinatorial principle.
