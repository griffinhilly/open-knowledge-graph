---
id: cochain-complexes-cohomology
title: Cochain Complexes and Cohomology
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-homology-groups
  type: hard
- id: chain-complexes-boundary-operator
  type: hard
- id: group-homomorphisms
  type: hard
builds-toward:
- singular-cohomology
- universal-coefficient-theorem
tags: [algebraic-topology, cohomology, cochain-complexes, duality]
stage: expert
status: validated
---
# Cochain Complexes and Cohomology

## Core Idea
A cochain complex is obtained by dualizing a chain complex: replacing each chain group C_n with the dual group Hom(C_n, G) (typically G = Z) and reversing the direction of the maps. The coboundary operator d^n goes "upward" from C^n to C^{n+1}, and cohomology H^n = ker(d^n)/im(d^{n-1}) measures the failure of cocycles to be coboundaries. While cohomology carries the same information as homology for spaces over a field, over the integers it carries strictly more information due to the universal coefficient theorem, and the cup product gives cohomology a ring structure that homology lacks.

## Questions

```yaml
- question: "If C_n is a chain complex with boundary d_n, the coboundary map d^n: C^n → C^{n+1} is defined by d^n(f) = f ∘ d_{n+1} (precomposition with the boundary). Why does d^{n+1} ∘ d^n = 0?"
  type: multiple-choice
  options:
    - "Because cohomology is always trivial"
    - "Because d^{n+1}(d^n(f)) = f ∘ d_{n+1} ∘ d_{n+2} = f ∘ 0 = 0, since d ∘ d = 0 in the chain complex"
    - "Because Hom(−, G) is an exact functor"
    - "Because f is a homomorphism"
  answer: 1
  explanation: "The coboundary of d^n(f) is d^{n+1}(f ∘ d_{n+1}) = (f ∘ d_{n+1}) ∘ d_{n+2} = f ∘ (d_{n+1} ∘ d_{n+2}) = f ∘ 0 = 0. The vanishing of the composed coboundary follows directly from d ∘ d = 0 in the original chain complex. This is the dual of the fundamental property of chain complexes, and it guarantees that cohomology is well-defined. Note that Hom(−, G) is NOT exact in general (it is only left exact), which is why cohomology and homology can differ."

- question: "A cochain f ∈ C^n(X; Z) = Hom(C_n(X), Z) is a cocycle if d^n(f) = 0, meaning f ∘ d_{n+1} = 0. What does this mean geometrically?"
  type: multiple-choice
  options:
    - "f assigns zero to every n-simplex"
    - "f assigns the same integer to homologous n-cycles"
    - "f vanishes on all boundaries — f(d_{n+1}(c)) = 0 for every (n+1)-chain c"
    - "f is a constant function on simplices"
  answer: 2
  explanation: "The cocycle condition d^n(f) = 0 means f ∘ d_{n+1} = 0, i.e., f(d_{n+1}(c)) = 0 for all (n+1)-chains c. In other words, f vanishes on all n-boundaries. This means f 'sees' only the homology: its value on an n-cycle depends only on the homology class, not the specific representative. Cocycles are the linear functionals on chains that respect the boundary structure, and their cohomology classes are well-defined pairings with homology classes."

- question: "Cohomology with coefficients in a field k (e.g., Q or Z/pZ) is isomorphic to the linear dual of homology: H^n(X; k) ≅ Hom_k(H_n(X; k), k)."
  type: true-false
  answer: true
  explanation: "When the coefficient group is a field k, the Hom functor is exact, and the universal coefficient theorem simplifies to H^n(X; k) ≅ Hom(H_n(X; k), k). This is the vector space dual. Over a field, cohomology and homology are dual vector spaces of the same dimension, so they carry equivalent information. Over the integers, the situation is more subtle: H^n(X; Z) ≅ Free(H_n(X; Z)) ⊕ Torsion(H_{n-1}(X; Z)), mixing information from adjacent homology groups."

- question: "Why does algebraic topology study both homology and cohomology, rather than just one?"
  type: short-answer
  answer: "Cohomology has a natural ring structure via the cup product, which homology lacks. The cup product H^p(X) × H^q(X) → H^{p+q}(X) encodes how cohomology classes interact multiplicatively, and this ring structure is a strictly finer invariant than the additive group structure alone — spaces with isomorphic homology groups can have non-isomorphic cohomology rings. Additionally, cohomology is the natural setting for duality theorems (Poincare duality), characteristic classes, and obstruction theory."
  explanation: "The multiplicative structure is the key advantage. For example, CP^2 and S^2 ∨ S^4 have isomorphic homology groups in every dimension, but their cohomology rings differ: CP^2 has a generator α ∈ H^2 with α^2 ≠ 0 in H^4, while in S^2 ∨ S^4 all cup products of positive-degree classes vanish. Cohomology detects this difference; homology cannot."
```

## Explainer

**Cohomology** is the dual theory to homology, obtained by applying the Hom functor to the chain complex. Given a chain complex C_* with boundary operators d_n : C_n -> C_{n-1}, and a coefficient group G (typically Z, Q, or Z/pZ), the **cochain group** C^n(X; G) = Hom(C_n(X), G) consists of all group homomorphisms from the n-th chain group to G. A cochain f in C^n assigns an element of G to each singular n-simplex — it "evaluates" chains rather than being a chain itself. The **coboundary operator** d^n : C^n -> C^{n+1} is defined by d^n(f) = f compose d_{n+1}: it precomposes a cochain with the boundary map, pulling it up one dimension.

The fundamental property d^{n+1} compose d^n = 0 follows immediately from d compose d = 0 in the chain complex. This makes (C^*, d^*) a **cochain complex** — a sequence of abelian groups with maps going "upward" in dimension whose composition is zero. The n-th **cohomology group** is H^n(X; G) = ker(d^n) / im(d^{n-1}). Elements of ker(d^n) are called **cocycles** — cochains that vanish on boundaries. Elements of im(d^{n-1}) are called **coboundaries** — cochains that are the coboundary of a lower-dimensional cochain. Two cocycles represent the same cohomology class when they differ by a coboundary.

The relationship between homology and cohomology is governed by the **universal coefficient theorem**, which states (for integer coefficients) that H^n(X; Z) fits into a short exact sequence 0 -> Ext(H_{n-1}(X), Z) -> H^n(X; Z) -> Hom(H_n(X), Z) -> 0. When the homology groups are free abelian (no torsion), the Ext term vanishes and H^n(X; Z) = Hom(H_n(X), Z), the usual algebraic dual. Torsion in homology produces additional torsion in cohomology, shifted by one degree — this is the "extra information" that cohomology carries over the integers.

The deepest reason to study cohomology alongside homology is the **cup product**, which gives H^*(X; R) = direct sum H^n(X; R) the structure of a graded ring (when R is a commutative ring). This multiplicative structure is invisible from the homology side and provides a strictly finer topological invariant. Poincare duality — the statement that H^k(M) = H_{n-k}(M) for a closed oriented n-manifold M — is most naturally expressed in cohomological terms. Characteristic classes (Stiefel-Whitney, Chern, Pontryagin), which classify vector bundles, live in cohomology. Obstruction theory, which determines when maps with certain properties exist, is formulated cohomologically. Cohomology is not merely the "dual of homology" but a richer and more structured invariant in its own right.
