---
id: homotopy-exact-sequence-fibration
title: Homotopy Exact Sequence of a Fibration
domain: mathematics
course: algebraic-topology
prerequisites:
- id: higher-homotopy-groups
  type: hard
- id: covering-spaces
  type: soft
- id: cw-complexes
  type: soft
builds-toward:
- borsuk-ulam-theorem
tags: [algebraic-topology, fibrations, fiber-bundles, long-exact-sequence, homotopy]
stage: expert
status: validated
---
# Homotopy Exact Sequence of a Fibration

## Core Idea
A fibration p : E -> B with fiber F gives rise to a long exact sequence of homotopy groups: ... -> pi_n(F) -> pi_n(E) -> pi_n(B) -> pi_{n-1}(F) -> ... -> pi_1(B) -> pi_0(F) -> pi_0(E). This sequence relates the homotopy groups of the total space, base, and fiber, and is the primary computational tool for homotopy groups. It generalizes the long exact sequence of a covering space (where the fiber is discrete) and is analogous to the long exact sequence of a pair in homology.

## Questions

```yaml
- question: "The Hopf fibration S^1 → S^3 → S^2 has fiber S^1, total space S^3, and base S^2. Using the long exact sequence, what is π_2(S^2)?"
  type: multiple-choice
  options:
    - "0"
    - "Z"
    - "Z/2Z"
    - "Z ⊕ Z"
  answer: 1
  explanation: "The long exact sequence gives: ... → π_2(S^3) → π_2(S^2) →^∂ π_1(S^1) → π_1(S^3) → ... Now π_2(S^3) = 0 and π_1(S^3) = 0 (S^3 is 2-connected). By exactness, the connecting homomorphism ∂: π_2(S^2) → π_1(S^1) is an isomorphism. Since π_1(S^1) ≅ Z, we get π_2(S^2) ≅ Z. This recovers the known result via a completely different method from Hurewicz or Mayer-Vietoris."

- question: "For a covering space p: E → B with fiber F (a discrete set of n points), the long exact sequence of the fibration gives π_k(E) ≅ π_k(B) for all k ≥ 2."
  type: true-false
  answer: true
  explanation: "If F is discrete, then π_k(F) = 0 for all k ≥ 1 (discrete spaces have trivial higher homotopy groups). The long exact sequence gives: ... → π_k(F) → π_k(E) → π_k(B) → π_{k-1}(F) → ... For k ≥ 2, both π_k(F) = 0 and π_{k-1}(F) = 0, so by exactness, π_k(E) → π_k(B) is an isomorphism. This is a well-known property of covering spaces: they share all higher homotopy groups with the base. Only π_1 can differ, and the exact sequence relates π_1(E) to π_1(B) via the fundamental group of the fiber."

- question: "A fibration p: E → B with contractible total space E has π_n(B) ≅ π_{n-1}(F) for all n ≥ 1."
  type: true-false
  answer: true
  explanation: "If E is contractible, then π_n(E) = 0 for all n ≥ 1. The long exact sequence gives: ... → 0 → π_n(B) →^∂ π_{n-1}(F) → 0 → ... By exactness, the connecting homomorphism ∂ is an isomorphism for all n ≥ 1. This is the key computation for path spaces and loop spaces: the path space PB → B has contractible total space and fiber ΩB (the loop space), giving π_n(B) ≅ π_{n-1}(ΩB). This relationship between a space and its loop space is fundamental to homotopy theory."

- question: "Explain the difference between a fibration and a fiber bundle, and why the long exact sequence applies to fibrations."
  type: short-answer
  answer: "A fiber bundle has local trivializations: every point of the base has a neighborhood U such that p^{-1}(U) ≅ U × F. A fibration is more general: it only requires the homotopy lifting property (any homotopy in the base can be lifted to the total space). Every fiber bundle over a paracompact base is a fibration, but not every fibration is a fiber bundle. The long exact sequence requires only the homotopy lifting property, not local triviality, so it applies to all fibrations. This generality is important because many natural constructions (path spaces, mapping spaces) produce fibrations that are not fiber bundles."
  explanation: "The homotopy lifting property is the key: it allows any map from a sphere into the base to be lifted to the total space (up to homotopy), which is exactly what's needed to relate the homotopy groups. The proof of the long exact sequence constructs the connecting homomorphism ∂ using the lifting property: a map S^n → B lifts to a map D^{n+1} → E whose boundary (a map S^n → F) gives the image under ∂."
```

## Explainer

A **fibration** is a continuous map p : E -> B satisfying the **homotopy lifting property** (HLP): given any homotopy h : X x [0,1] -> B and a lift h_0 : X -> E of the starting map (p compose h_0 = h(-, 0)), there exists a homotopy H : X x [0,1] -> E lifting the entire homotopy (p compose H = h). Intuitively, any continuous deformation in the base can be "tracked" in the total space. The **fiber** F = p^{-1}(b_0) over a basepoint b_0 is the preimage, and under mild conditions (B path-connected), all fibers are homotopy equivalent.

The **long exact sequence of a fibration** is the analog of the long exact sequence of a pair for homotopy groups. For a fibration F -> E -> B with connected base B, there is an exact sequence: ... -> pi_n(F) -i_*-> pi_n(E) -p_*-> pi_n(B) -partial-> pi_{n-1}(F) -> ... -> pi_1(E) -p_*-> pi_1(B) -partial-> pi_0(F) -> pi_0(E). The maps i_* and p_* are induced by the inclusion F hookrightarrow E and the projection p : E -> B. The connecting homomorphism partial : pi_n(B) -> pi_{n-1}(F) is constructed using the homotopy lifting property: given a based map f : S^n -> B representing a class in pi_n(B), lift the induced map D^n -> B to a map D^n -> E. The restriction of this lift to the boundary S^{n-1} = boundary(D^n) lands in the fiber F, giving a class in pi_{n-1}(F).

The most celebrated application is to the **Hopf fibration** S^1 -> S^3 -> S^2. The long exact sequence reads: ... -> pi_n(S^1) -> pi_n(S^3) -> pi_n(S^2) -> pi_{n-1}(S^1) -> ... Since pi_k(S^1) = 0 for k >= 2 (the universal cover R is contractible), the sequence gives isomorphisms pi_n(S^3) = pi_n(S^2) for n >= 3. In particular, pi_3(S^2) = pi_3(S^3) = Z. This is how the nontrivial pi_3(S^2) is computed: not by direct construction, but by recognizing S^2 as the base of the Hopf fibration and using the exact sequence to transfer the computation to the simpler space S^3.

Covering spaces are a special case: a covering p : E -> B is a fibration with discrete fiber F. Since discrete spaces have trivial higher homotopy groups (pi_n(F) = 0 for n >= 1), the long exact sequence gives isomorphisms pi_n(E) = pi_n(B) for n >= 2 and a short exact sequence 1 -> pi_1(E) -> pi_1(B) -> pi_0(F) for n = 1. This recovers the classical theory: a covering space has the same higher homotopy groups as the base, and its fundamental group is a subgroup of pi_1(B) with index equal to the number of sheets.

The **path-loop fibration** is another fundamental example: for any pointed space (B, b_0), the path space PB = {paths in B starting at b_0} is contractible, and the endpoint evaluation map PB -> B is a fibration with fiber Omega B = {loops in B based at b_0} (the loop space). Since PB is contractible, the long exact sequence gives isomorphisms pi_n(B) = pi_{n-1}(Omega B) for all n >= 1. This "looping" operation shifts homotopy groups down by one dimension and is one of the most important structural results in homotopy theory. It underpins the theory of iterated loop spaces, spectra, and stable homotopy theory — the modern framework for understanding the deep structure of homotopy groups.
