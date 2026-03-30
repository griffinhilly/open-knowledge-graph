---
id: universal-coefficient-theorem
title: The Universal Coefficient Theorem
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-cohomology
  type: hard
- id: homology-with-coefficients
  type: hard
- id: exact-sequences-homological-algebra
  type: hard
builds-toward:
- poincare-duality
- kunneth-formula
tags: [algebraic-topology, universal-coefficients, ext-functor, homological-algebra]
stage: expert
status: validated
---
# The Universal Coefficient Theorem

## Core Idea
The universal coefficient theorem relates cohomology with coefficients in G to homology with integer coefficients, via a short exact sequence: 0 -> Ext^1(H_{n-1}(X; Z), G) -> H^n(X; G) -> Hom(H_n(X; Z), G) -> 0. This sequence always splits (non-naturally), so H^n(X; G) = Hom(H_n(X), G) + Ext(H_{n-1}(X), G) as abelian groups. The theorem says cohomology is "almost" dual to homology — the Hom term gives the expected duality, while the Ext term is a correction for torsion that shifts information from dimension n-1 to dimension n.

## Questions

```yaml
- question: "If H_1(X; Z) ≅ Z/6Z and H_0(X; Z) ≅ Z, what is H^1(X; Z)?"
  type: multiple-choice
  options:
    - "Z/6Z"
    - "Z"
    - "Z/6Z ⊕ Z"
    - "0"
  answer: 3
  explanation: "By the universal coefficient theorem: H^1(X; Z) ≅ Hom(H_1(X; Z), Z) ⊕ Ext^1(H_0(X; Z), Z). Now Hom(Z/6Z, Z) = 0 (the only homomorphism from a finite group to Z is zero), and Ext^1(Z, Z) = 0 (Z is free, so Ext vanishes for free groups). Therefore H^1(X; Z) = 0. The torsion Z/6Z in H_1 does NOT appear in H^1 — it appears in H^2 via the Ext term. This shift is a key feature of the universal coefficient theorem: torsion in H_{n-1} contributes to H^n."

- question: "For a space with free (torsion-free) homology groups, the universal coefficient theorem simplifies to H^n(X; Z) ≅ Hom(H_n(X; Z), Z)."
  type: true-false
  answer: true
  explanation: "When all homology groups are free abelian, Ext^1(H_{n-1}, Z) = 0 for all n (since Ext vanishes for free groups). The short exact sequence collapses to H^n(X; Z) ≅ Hom(H_n(X; Z), Z), which is the ordinary algebraic dual. In this case, cohomology and homology carry exactly the same information as abelian groups. Spaces with free homology include all spheres, complex projective spaces, and products of spheres."

- question: "The splitting in the universal coefficient theorem is natural (functorial with respect to continuous maps)."
  type: true-false
  answer: false
  explanation: "The universal coefficient theorem guarantees that the short exact sequence splits, but the splitting is NOT natural — there is no functorial way to choose the splitting. This means H^n(X; G) ≅ Hom(H_n, G) ⊕ Ext(H_{n-1}, G) as abstract groups, but the isomorphism is not compatible with maps between spaces. A continuous map f: X → Y induces compatible maps on the short exact sequences, but the splitting cannot be chosen to commute with f*. The non-naturality is a genuine subtlety, not a mere technicality."

- question: "Compute H^2(RP^2; Z) using the universal coefficient theorem, given that H_0(RP^2) = Z, H_1(RP^2) = Z/2Z, H_2(RP^2) = 0."
  type: short-answer
  answer: "H^2(RP^2; Z) ≅ Hom(H_2(RP^2), Z) ⊕ Ext^1(H_1(RP^2), Z) = Hom(0, Z) ⊕ Ext^1(Z/2Z, Z) = 0 ⊕ Z/2Z = Z/2Z. The torsion Z/2Z in H_1 reappears in H^2 via the Ext term. This is a manifestation of the general principle: torsion in homology dimension n-1 contributes torsion to cohomology dimension n."
  explanation: "Computing Ext^1(Z/2Z, Z): take a free resolution 0 → Z →^2 Z → Z/2Z → 0, apply Hom(−, Z) to get 0 → Hom(Z, Z) →^2 Hom(Z, Z) → 0, which is 0 → Z →^2 Z → 0. The cokernel is Z/2Z, so Ext^1(Z/2Z, Z) = Z/2Z. This computation exemplifies the general formula Ext^1(Z/nZ, Z) = Z/nZ."
```

## Explainer

The **universal coefficient theorem** (UCT) connects homology and cohomology through the algebraic functors Hom and Ext. There are two versions: one for cohomology (relating H^n to H_n) and one for homology with coefficients (relating H_n(X; G) to H_n(X; Z)). The cohomological version, which is the more commonly used, states: for any space X and abelian group G, there is a short exact sequence 0 -> Ext^1(H_{n-1}(X; Z), G) -> H^n(X; G) -> Hom(H_n(X; Z), G) -> 0, and this sequence splits (though not naturally).

The Hom term Hom(H_n(X), G) is the "expected" contribution — it says cohomology is dual to homology. If all homology groups were free abelian, this term would give the complete answer: H^n(X; G) = Hom(H_n(X), G). The Ext term Ext^1(H_{n-1}(X), G) is the correction for torsion. Ext^1(A, G) measures the "non-split extensions" of G by A and is computed from a free resolution of A. For the key cases: Ext^1(Z, G) = 0 (free groups contribute nothing), Ext^1(Z/nZ, G) = G/nG (cyclic torsion produces a quotient). So if H_{n-1}(X) has a Z/nZ summand, it contributes a G/nG summand to H^n(X; G). When G = Z, this gives Ext^1(Z/nZ, Z) = Z/nZ: torsion in H_{n-1} reappears as torsion in H^n, shifted up by one degree.

The **splitting** of the short exact sequence means that H^n(X; G) = Hom(H_n(X), G) direct sum Ext^1(H_{n-1}(X), G) as abstract abelian groups. However, this splitting is not natural — there is no way to choose the splitting compatibly with continuous maps. This non-naturality means the "decomposition" into Hom and Ext summands is not functorial, and one should not think of cohomology as literally being the direct sum of these two terms in any canonical way. The short exact sequence itself IS natural, and that is the correct functorial statement.

The UCT has a dual version for **homology with coefficients**: 0 -> H_n(X; Z) tensor G -> H_n(X; G) -> Tor_1(H_{n-1}(X; Z), G) -> 0. Here the Tor term plays the role of Ext, detecting how torsion in H_{n-1} interacts with the coefficient group G under the tensor product. When G is a field, both Tor and Ext vanish (or become trivial), and the theorem simplifies dramatically: H_n(X; k) = H_n(X; Z) tensor k, and H^n(X; k) = Hom_k(H_n(X; k), k). This is why field coefficients are technically simpler and why rational or mod-p homology is often computed first.

The universal coefficient theorem explains several phenomena. It clarifies why real projective spaces have torsion in cohomology (shifted from their torsion in homology). It explains why cohomology over a field contains the same information as homology (both Ext and Tor vanish). And it provides the theoretical basis for the Kronecker pairing between cohomology and homology: the surjection H^n(X; G) -> Hom(H_n(X), G) is the map that evaluates cocycles on cycles, and its kernel (the Ext term) consists of the "phantom" classes that pair trivially with all cycles. The UCT is one of the workhorses of algebraic topology, providing the algebraic machinery to move between homological and cohomological computations.
