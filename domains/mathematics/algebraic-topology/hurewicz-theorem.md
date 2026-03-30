---
id: hurewicz-theorem
title: The Hurewicz Theorem
domain: mathematics
course: algebraic-topology
prerequisites:
- id: higher-homotopy-groups
  type: hard
- id: singular-homology-groups
  type: hard
- id: homology-of-spheres
  type: soft
builds-toward:
- degree-theory-maps-spheres
tags: [algebraic-topology, hurewicz-theorem, homotopy-groups, homology]
stage: expert
status: validated
---
# The Hurewicz Theorem

## Core Idea
The Hurewicz theorem is the fundamental bridge between homotopy groups and homology groups. It states: if X is a path-connected space with pi_k(X) = 0 for all k < n (where n >= 2), then H_k(X) = 0 for k < n and the Hurewicz homomorphism h : pi_n(X) -> H_n(X) is an isomorphism. In the n = 1 case, h : pi_1(X) -> H_1(X) is abelianization. The theorem says that the "first nontrivial" homotopy group always equals the corresponding homology group, providing a computable entry point into the homotopy groups of a space.

## Questions

```yaml
- question: "A simply connected space X has π_2(X) ≅ Z^3. What does the Hurewicz theorem tell us about H_2(X)?"
  type: multiple-choice
  options:
    - "H_2(X) = 0 because X is simply connected"
    - "H_2(X) ≅ Z^3, since X is simply connected (π_1 = 0) and π_2 is the first nontrivial homotopy group"
    - "H_2(X) ≅ Z^3/(some torsion subgroup)"
    - "Nothing — the Hurewicz theorem only applies to spheres"
  answer: 1
  explanation: "X is path-connected (being simply connected) with π_1(X) = 0. The Hurewicz theorem (n = 2 case) says that if π_1(X) = 0, then h: π_2(X) → H_2(X) is an isomorphism. Since π_2(X) ≅ Z^3, we get H_2(X) ≅ Z^3. The theorem also tells us H_1(X) = 0 (the abelianization of the trivial group is trivial). This is the power of Hurewicz: it converts the first nontrivial homotopy group into a computable homology group."

- question: "The Hurewicz theorem for n = 1 says H_1(X) is the abelianization of π_1(X). This means H_1 of a space with non-abelian fundamental group carries less information than π_1."
  type: true-false
  answer: true
  explanation: "For n = 1, the Hurewicz homomorphism h: π_1(X) → H_1(X) is surjective with kernel equal to the commutator subgroup [π_1, π_1]. So H_1(X) = π_1(X)/[π_1(X), π_1(X)] — the abelianization. If π_1 is non-abelian (like the free group on two generators for the figure-eight), the abelianization loses the non-commutativity: F_2 has abelianization Z^2, which cannot distinguish it from Z × Z. This information loss is why the fundamental group is a finer invariant than H_1."

- question: "If a CW complex X satisfies H_k(X) = 0 for all k ≥ 1, what can you conclude about X?"
  type: multiple-choice
  options:
    - "X is contractible"
    - "X has the same homology as a point, but may not be contractible"
    - "π_n(X) = 0 for all n ≥ 1, so X is contractible (using Whitehead's theorem)"
    - "Both A and C, since they say the same thing"
  answer: 0
  explanation: "For a CW complex with trivial reduced homology: H_1(X) = 0 implies π_1(X) is a perfect group (equal to its own commutator subgroup). But actually, if X is simply connected AND has all homology vanishing, then by the Hurewicz theorem, π_n(X) = 0 for all n (by induction: each π_n is the first to be nontrivial, so it equals H_n = 0). Then Whitehead's theorem gives contractibility. If X is not simply connected, there exist acyclic spaces that are not contractible (like certain quotients of trees). So the full answer requires assuming simple connectivity or being more careful."

- question: "Apply the Hurewicz theorem to compute π_n(S^n) for n ≥ 2."
  type: short-answer
  answer: "S^n is (n-1)-connected: π_k(S^n) = 0 for k < n (by cellular approximation, since S^n has cells only in dimensions 0 and n). The Hurewicz theorem then says the Hurewicz homomorphism h: π_n(S^n) → H_n(S^n) is an isomorphism. Since H_n(S^n) ≅ Z, we get π_n(S^n) ≅ Z. The generator is the homotopy class of the identity map id: S^n → S^n."
  explanation: "This is one of the most important applications of the Hurewicz theorem. It confirms that the degree of a map S^n → S^n (defined homologically as the integer d with f_*[S^n] = d[S^n]) coincides with its homotopy class — degree completely classifies self-maps of S^n up to homotopy. The Hurewicz theorem thus provides the foundation for degree theory."

- question: "Does the Hurewicz theorem help compute π_3(S^2)?"
  type: short-answer
  answer: "No, not directly. The Hurewicz theorem says π_2(S^2) ≅ H_2(S^2) ≅ Z (the first nontrivial homotopy group matches the homology). But for π_3(S^2), we are above the first nontrivial dimension, and the Hurewicz map h: π_3(S^2) → H_3(S^2) = 0 is the zero map — it provides no information. Computing π_3(S^2) ≅ Z requires different tools, such as the long exact sequence of the Hopf fibration S^1 → S^3 → S^2."
  explanation: "This illustrates the limitation of the Hurewicz theorem: it gives an isomorphism only in the first nontrivial dimension and only a surjection one dimension higher (by the relative Hurewicz theorem). Beyond that, the relationship between homotopy and homology breaks down, and the two invariants diverge dramatically."
```

## Explainer

The **Hurewicz homomorphism** h : pi_n(X, x_0) -> H_n(X; Z) is defined by sending the homotopy class of a based map f : (S^n, s_0) -> (X, x_0) to the homology class f_*([S^n]) in H_n(X), where [S^n] in H_n(S^n) = Z is the fundamental class. Intuitively, h takes a "homotopy-theoretic n-sphere in X" and measures its "homological shadow." The Hurewicz theorem states that in the first nontrivial dimension, this shadow captures everything.

The **n = 1 case**: for any path-connected space X, h : pi_1(X) -> H_1(X) is surjective with kernel [pi_1, pi_1] (the commutator subgroup), so H_1(X) = pi_1(X)^{ab} (the abelianization). This is why H_1 of the figure-eight is Z^2 (the abelianization of the free group F_2), and H_1 of the torus is Z^2 (the abelianization of Z^2, which is already abelian). The abelianization perspective shows that H_1 captures the "abelian shadow" of the fundamental group, which is precisely the information encoded in the commutative group structure of homology.

The **n >= 2 case** (the main theorem): suppose X is (n-1)-connected, meaning path-connected with pi_k(X) = 0 for all 1 <= k <= n-1. Then H_k(X) = 0 for 1 <= k <= n-1, and h : pi_n(X) -> H_n(X) is an isomorphism. The condition "(n-1)-connected" means the space has no holes detectable by spheres of dimension less than n, so the first interesting homotopy group is pi_n. The theorem says that this first interesting homotopy group agrees with the corresponding homology group — the abelianization that normally makes homology a coarser invariant has no effect in the first nontrivial dimension (since pi_n is already abelian for n >= 2).

The most fundamental application is to spheres. S^n is (n-1)-connected (all homotopy groups below dimension n vanish, by cellular approximation or a direct argument). The Hurewicz theorem gives pi_n(S^n) = H_n(S^n) = Z, generated by the identity map. This is the rigorous foundation of **degree theory**: the homotopy class of a map f : S^n -> S^n is completely determined by the integer deg(f), which equals the induced map on the Z factor. The degree is simultaneously a homological quantity (how f_* acts on H_n) and a homotopical quantity (which class f represents in pi_n), and the Hurewicz theorem guarantees their agreement.

The theorem has a **relative version**: if (X, A) is an (n-1)-connected pair with A simply connected and n >= 2, then H_k(X, A) = 0 for k < n and h : pi_n(X, A) -> H_n(X, A) is an isomorphism. Combined with the long exact sequences of homotopy and homology, this provides tools for comparing the two theories systematically. However, the Hurewicz theorem gives information only at the "edge" — the first nontrivial dimension. Beyond that, homotopy groups and homology groups can diverge wildly. The computation of pi_3(S^2) = Z (while H_3(S^2) = 0) is the simplest example of this divergence, and it shows that homotopy groups encode qualitatively different information from homology in higher dimensions.
