---
id: singular-homology-groups
title: Singular Homology Groups
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-simplices-singular-chains
  type: hard
- id: simplicial-homology-groups
  type: soft
- id: group-homomorphisms
  type: soft
builds-toward:
- homology-of-spheres
- relative-homology-long-exact-sequence
- homology-with-coefficients
- cochain-complexes-cohomology
tags: [algebraic-topology, singular-homology, homotopy-invariance, functoriality]
stage: expert
status: validated
---
# Singular Homology Groups

## Core Idea
The singular homology groups H_n(X) = ker(d_n)/im(d_{n+1}) of the singular chain complex are the fundamental topological invariants of algebraic topology. They are defined for any topological space, are invariant under homotopy equivalence (not just homeomorphism), and are functorial — continuous maps induce homomorphisms on homology. For spaces admitting triangulations, singular homology agrees with simplicial homology, but singular homology's true power lies in the theoretical tools (long exact sequences, excision, Mayer-Vietoris) that make it computable without ever writing down the enormous chain groups explicitly.

## Questions

```yaml
- question: "Two spaces X and Y are homotopy equivalent (there exist maps f: X -> Y and g: Y -> X with g∘f ≃ id_X and f∘g ≃ id_Y). What can you conclude about their singular homology groups?"
  type: multiple-choice
  options:
    - "H_n(X) and H_n(Y) are isomorphic for all n"
    - "H_n(X) and H_n(Y) have the same rank but may differ in torsion"
    - "H_0(X) ≅ H_0(Y) but higher homology groups may differ"
    - "Nothing — homotopy equivalence does not constrain homology"
  answer: 0
  explanation: "Homotopy invariance is a fundamental property of singular homology: homotopic maps induce identical homomorphisms on homology. If f and g are homotopy inverses, then f_* and g_* are inverse isomorphisms on H_n for every n. This is stronger than topological invariance (homeomorphism invariance) and has powerful consequences: for example, any contractible space has the homology of a point (H_0 ≅ Z, H_n = 0 for n > 0), because contractible means homotopy equivalent to a point."

- question: "The singular homology of a point is H_0 ≅ Z and H_n = 0 for all n > 0."
  type: true-false
  answer: true
  explanation: "A point has exactly one singular 0-simplex (the unique map from Delta^0 to the point), and for each n > 0, it has exactly one singular n-simplex (the unique constant map from Delta^n to the point). The chain complex is Z -> Z -> Z -> ... with alternating boundary maps that are either zero or the identity. Working out the kernels and images: ker(d_0) = Z, im(d_1) = 0, so H_0 = Z. For n > 0, the cycles and boundaries cancel to give H_n = 0. Since any contractible space is homotopy equivalent to a point, this also gives the homology of R^n, D^n, and any convex subset of Euclidean space."

- question: "A continuous map f: X -> Y always induces a surjective homomorphism f_*: H_n(X) -> H_n(Y)."
  type: true-false
  answer: false
  explanation: "Functoriality guarantees that f induces a homomorphism f_* on homology, but this homomorphism need not be surjective (or injective). For example, the inclusion of a point into S^1 induces the zero map on H_1, which is not surjective. The constant map from any space to a point induces the zero map on all H_n with n > 0. Only special maps (like homotopy equivalences, or maps with degree +/- 1 on spheres) induce surjections. The power of functoriality is that f_* exists and respects composition, not that it preserves all algebraic structure."

- question: "Explain intuitively why homotopy equivalent spaces must have isomorphic homology groups, using the fact that homology counts 'holes.'"
  type: short-answer
  answer: "Homotopy equivalence means two spaces can be continuously deformed into each other (in a looser sense than homeomorphism — dimensions can collapse as long as they can be re-inflated). If X deforms to Y, every hole in X deforms to a corresponding hole in Y, and vice versa. Since homology counts holes (by dimension: H_0 counts components, H_1 counts tunnels, H_2 counts cavities), the counts must match. Formally, the induced maps f_* and g_* on homology are mutual inverses, giving isomorphisms H_n(X) ≅ H_n(Y) for all n."
  explanation: "The formal proof uses the chain homotopy concept: homotopic maps f ≃ g induce chain-homotopic chain maps, which induce identical maps on homology. The key technical lemma (the prism operator) constructs an explicit chain homotopy from a homotopy between maps. This is one of the deepest results in algebraic topology, because it shows that homology depends only on the 'shape' of a space up to continuous deformation, not on metric, dimension, or other geometric details."

- question: "For a path-connected space X, H_0(X) ≅ Z. What is the geometric meaning of the isomorphism?"
  type: short-answer
  answer: "The isomorphism sends the homology class of any singular 0-simplex (point) to 1 ∈ Z. This is called the augmentation map. Since X is path-connected, any two points p and q are connected by a path gamma, and d_1(gamma) = q - p, so p and q differ by a boundary and represent the same class in H_0. Thus H_0(X) has a single generator [p] for any point p, and is isomorphic to Z. The generator corresponds to the 'connected component' that is the entire space."
  explanation: "For a space with k path components, H_0 ≅ Z^k, with one generator per component. Two 0-cycles are homologous if and only if they assign the same total 'count' to each component. This is the simplest instance of homology detecting topological structure, and it illustrates the general pattern: homology measures the failure of cycles to be boundaries."
```

## Explainer

Having defined the singular chain complex C_*(X) with its boundary operators d_n, the **singular homology groups** H_n(X) = ker(d_n)/im(d_{n+1}) are the central objects of algebraic topology. Every topological space has singular homology groups, and these groups are computable (for reasonable spaces) despite the apparently intractable size of the chain groups. The key properties that make singular homology powerful are **homotopy invariance**, **functoriality**, and a suite of computational tools (long exact sequences, excision, Mayer-Vietoris) that allow indirect computation.

**Functoriality** means that a continuous map f : X -> Y induces group homomorphisms f_* : H_n(X) -> H_n(Y) for all n, defined by f_*([\alpha]) = [f compose alpha] on chains. This respects composition: (g compose f)_* = g_* compose f_*, and id_* = id. In categorical language, H_n is a functor from the category of topological spaces to the category of abelian groups. The practical consequence is that any topological relationship between spaces (inclusion, retraction, covering map, quotient map) translates into an algebraic relationship between their homology groups. This is the fundamental strategy of algebraic topology: convert topological questions into algebraic ones, which are often easier.

**Homotopy invariance** is the theorem that homotopic maps f, g : X -> Y induce the same homomorphism on homology: f_* = g_*. The proof constructs a **chain homotopy** — a sequence of homomorphisms P_n : C_n(X) -> C_{n+1}(Y) satisfying f_# - g_# = d compose P + P compose d — using the prism operator, which triangulates the product Delta^n x [0,1] and maps it into Y using the homotopy. The chain homotopy equation implies that f_# and g_# induce identical maps on homology (their difference sends every cycle to a boundary). As an immediate corollary, homotopy equivalent spaces have isomorphic homology: if f : X -> Y is a homotopy equivalence with homotopy inverse g, then f_* and g_* are mutually inverse isomorphisms.

For basic spaces: a point has H_0 = Z and H_n = 0 for n > 0. Any contractible space (R^n, D^n, star-shaped regions) has the same homology, by homotopy invariance. The circle S^1 has H_0 = Z, H_1 = Z, and H_n = 0 for n >= 2. More generally, the n-sphere S^n has H_0 = Z, H_n = Z, and all other homology zero. The torus T^2 has H_0 = Z, H_1 = Z^2, H_2 = Z. These basic computations, which we will establish using the tools developed in subsequent topics, serve as the building blocks from which the homology of more complex spaces is assembled via exact sequences and excision.

The agreement between singular and simplicial homology (for triangulable spaces) is a nontrivial theorem. The proof proceeds by showing that the inclusion of the simplicial chain complex into the singular chain complex induces isomorphisms on homology. This justifies the simplicial approach to computation: for a space with a known triangulation, compute with the small simplicial chain groups and obtain the same answer as the enormous singular chain complex would give. But singular homology's universality and homotopy invariance make it the correct theoretical framework: it is singular homology that satisfies the Eilenberg-Steenrod axioms that characterize homology theories, and all the major theorems (Mayer-Vietoris, excision, universal coefficients, Poincare duality) are most naturally stated and proved for singular homology.
