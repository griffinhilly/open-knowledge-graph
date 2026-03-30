---
id: homology-of-spheres
title: Homology of Spheres
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-homology-groups
  type: hard
- id: mayer-vietoris-sequence
  type: hard
builds-toward:
- degree-theory-maps-spheres
- brouwer-fixed-point-theorem-homological
- higher-homotopy-groups
- hurewicz-theorem
tags: [algebraic-topology, spheres, homology-computation, suspension]
stage: expert
status: validated
---
# Homology of Spheres

## Core Idea
The n-sphere S^n has singular homology H_k(S^n) = Z for k = 0 and k = n, and H_k(S^n) = 0 otherwise. This computation, established via the Mayer-Vietoris sequence or the long exact sequence of the pair (D^n, S^{n-1}), is one of the most important results in algebraic topology. It provides the foundation for degree theory, the Brouwer fixed point theorem, and the classification of maps between spheres, and it reveals that each sphere has exactly one nontrivial "hole" in its own dimension.

## Questions

```yaml
- question: "What are the homology groups of S^3 (the 3-sphere)?"
  type: multiple-choice
  options:
    - "H_0 = Z, H_1 = Z, H_2 = Z, H_3 = Z"
    - "H_0 = Z, H_3 = Z, all others zero"
    - "H_0 = Z, H_1 = Z^3, all others zero"
    - "H_k = Z for all k ≥ 0"
  answer: 1
  explanation: "The homology of S^n is concentrated in dimensions 0 and n: H_0(S^n) ≅ Z (connected), H_n(S^n) ≅ Z (fundamental class detecting the n-dimensional 'hole'), and H_k(S^n) = 0 for all other k. For S^3: H_0 = Z, H_3 = Z, and H_1 = H_2 = 0. The vanishing of H_1 means S^3 is simply connected (which also follows from the fundamental group being trivial), and the vanishing of H_2 means there are no 2-dimensional holes."

- question: "The homology of S^n can be computed inductively using the Mayer-Vietoris sequence by decomposing S^n into two hemispheres whose intersection is S^{n-1}."
  type: true-false
  answer: true
  explanation: "Decompose S^n as U ∪ V where U and V are open hemispheres (slightly overlapping at the equator). Both U and V are contractible (each deformation retracts to a point), so H_k(U) = H_k(V) = 0 for k > 0. The intersection U ∩ V deformation retracts to the equatorial S^{n-1}. The Mayer-Vietoris sequence then gives: ... → H_k(U) ⊕ H_k(V) → H_k(S^n) → H_{k-1}(S^{n-1}) → H_{k-1}(U) ⊕ H_{k-1}(V) → ... Since H_k(U) = H_k(V) = 0 for k > 0, this yields isomorphisms H_k(S^n) ≅ H_{k-1}(S^{n-1}) for k ≥ 2, which inductively computes the homology starting from H_*(S^0) = Z ⊕ Z (two points)."

- question: "S^2 has trivial fundamental group (π_1 = 0) but nontrivial H_2 ≅ Z. This shows that homology detects topological features invisible to the fundamental group."
  type: true-false
  answer: true
  explanation: "The fundamental group detects 1-dimensional holes (non-contractible loops). The 2-sphere has no non-contractible loops — every loop on S^2 can be shrunk to a point — so π_1(S^2) = 0. But S^2 encloses a 2-dimensional cavity, detected by H_2(S^2) ≅ Z. This is precisely the kind of higher-dimensional information that homology captures and the fundamental group misses. More generally, the n-sphere (n ≥ 2) has trivial fundamental group but nontrivial H_n, showing that higher homology groups are genuinely new invariants."

- question: "Explain the geometric meaning of the generator of H_n(S^n) ≅ Z."
  type: short-answer
  answer: "The generator of H_n(S^n), called the fundamental class [S^n], is represented by a singular n-cycle that 'wraps once around' the sphere. For any triangulation, this is the sum of all n-simplices with consistent orientations. The integer k ∈ Z = H_n(S^n) represents a cycle that wraps around S^n exactly k times (with sign indicating orientation). The fact that this group is Z (not Z/mZ) means the fundamental cycle has infinite order: wrapping around the sphere k times is never homologous to zero for any k ≠ 0."
  explanation: "The fundamental class is the homological version of the orientation of the sphere. For an oriented sphere, there is a canonical choice of generator (the fundamental class compatible with the orientation). This fundamental class is essential for degree theory: a map f : S^n → S^n sends [S^n] to some multiple d·[S^n], and this integer d is the degree of f, which determines f up to homotopy."

- question: "Using the Mayer-Vietoris induction, what is H_1(S^2)?"
  type: short-answer
  answer: "H_1(S^2) = 0. The Mayer-Vietoris sequence with contractible hemispheres gives H_1(S^2) ≅ H_0(S^1)/im(H_0(U) ⊕ H_0(V) → H_0(S^1)). Since S^1 is connected and both hemispheres are connected, the map Z ⊕ Z → Z is surjective (both hemispheres include into the connected equator), so the connecting homomorphism H_1(S^2) → H_0(S^1) lands in the kernel of Z → Z ⊕ Z, giving H_1(S^2) ≅ H_0(S^1)/image ≅ 0 after working through the exact sequence carefully."
  explanation: "More directly: S^2 is simply connected, so H_1(S^2) = π_1(S^2)^{ab} = 0 by the Hurewicz theorem. The Mayer-Vietoris computation confirms this by the algebraic machinery. The vanishing of H_1 for S^n with n ≥ 2 is a general pattern reflecting the simple-connectivity of higher-dimensional spheres."
```

## Explainer

The computation of the homology of spheres is a cornerstone of algebraic topology: nearly every major theorem and application refers back to H_*(S^n). The result is clean and beautiful: H_k(S^n) is Z when k = 0 or k = n, and zero otherwise. The 0-dimensional homology H_0(S^n) = Z reflects that S^n is connected (for n >= 1; S^0 consists of two points, giving H_0(S^0) = Z^2). The n-dimensional homology H_n(S^n) = Z detects the single "n-dimensional hole" — the cavity enclosed by the sphere. All intermediate homology vanishes: S^n has no holes of any dimension other than 0 and n.

The **Mayer-Vietoris induction** is the most elegant computation method. Decompose S^n into two open hemispheres U and V, each contractible (they deformation retract to a point). Their intersection U intersect V deformation retracts to the equatorial (n-1)-sphere S^{n-1}. The Mayer-Vietoris long exact sequence reads: ... -> H_k(U) direct sum H_k(V) -> H_k(S^n) -> H_{k-1}(S^{n-1}) -> H_{k-1}(U) direct sum H_{k-1}(V) -> ... Since U and V are contractible, H_k(U) = H_k(V) = 0 for k > 0, and the sequence collapses to isomorphisms H_k(S^n) = H_{k-1}(S^{n-1}) for k >= 2. Starting from S^0 (two points with H_0 = Z^2, all higher homology zero), we get: H_1(S^1) = H_0(S^0)/corrections = Z, H_2(S^2) = H_1(S^1) = Z, and inductively H_n(S^n) = Z.

An alternative approach uses the **long exact sequence of the pair** (D^n, S^{n-1}). Since the disk D^n is contractible, H_k(D^n) = 0 for k > 0. The long exact sequence ... -> H_k(D^n) -> H_k(D^n, S^{n-1}) -> H_{k-1}(S^{n-1}) -> H_{k-1}(D^n) -> ... gives isomorphisms H_k(D^n, S^{n-1}) = H_{k-1}(S^{n-1}) for k >= 2. The relative homology H_k(D^n, S^{n-1}) is isomorphic to the reduced homology of the quotient D^n/S^{n-1} = S^n (by excision-type arguments), giving the same inductive formula. Both methods reduce to the same recursion and yield the same answer.

The **fundamental class** [S^n], the generator of H_n(S^n), is the homological incarnation of the sphere's orientation. For any triangulation of S^n, the fundamental class is represented by the sum of all n-simplices with orientations consistent with the global orientation. The fact that H_n(S^n) = Z means that every n-cycle on S^n is a multiple of the fundamental class — it wraps around the sphere some integer number of times. This integer is the foundation of **degree theory**: for a continuous map f : S^n -> S^n, the induced map f_* : H_n(S^n) -> H_n(S^n) is multiplication by an integer deg(f), the degree of f. The degree is the single most important homotopy invariant of such maps and connects to winding numbers, Brouwer's theorem, and the Borsuk-Ulam theorem.

The homology of spheres also reveals a key limitation of the fundamental group and motivates the study of higher-dimensional invariants. The sphere S^n for n >= 2 has trivial fundamental group (every loop can be contracted to a point), yet its homology is nontrivial in dimension n. The fundamental group is blind to these higher-dimensional holes. This is precisely why homology (and later, higher homotopy groups and cohomology) are essential: they detect topological features that no single algebraic invariant can capture alone. The spheres, as the simplest spaces with holes of each dimension, serve as the calibration targets for all these invariants.
