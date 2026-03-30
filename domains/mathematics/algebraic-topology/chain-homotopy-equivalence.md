---
id: chain-homotopy-equivalence
title: Chain Homotopy and Chain Equivalence
domain: mathematics
course: algebraic-topology
prerequisites:
- id: chain-complexes-boundary-operator
  type: hard
- id: singular-homology-groups
  type: hard
- id: homotopy-definition
  type: soft
builds-toward:
- five-lemma
tags: [algebraic-topology, chain-homotopy, homological-algebra, homotopy-invariance]
stage: expert
status: validated
---
# Chain Homotopy and Chain Equivalence

## Core Idea
A chain homotopy between two chain maps f, g : C_* -> D_* is a sequence of homomorphisms P_n : C_n -> D_{n+1} satisfying f_n - g_n = d_{n+1} compose P_n + P_{n-1} compose d_n. Chain homotopic maps induce identical homomorphisms on homology: f_* = g_*. This algebraic notion mirrors topological homotopy — when two continuous maps are homotopic, the induced chain maps are chain homotopic. Chain homotopy equivalence is the correct notion of "sameness" for chain complexes, just as homotopy equivalence is for topological spaces.

## Questions

```yaml
- question: "If f and g are chain homotopic chain maps (f ~ g via chain homotopy P), why do they induce the same map on homology?"
  type: multiple-choice
  options:
    - "Because P is an isomorphism"
    - "Because for any cycle z (with dz = 0), f(z) - g(z) = dP(z) + Pd(z) = dP(z) + 0 = dP(z), which is a boundary — so [f(z)] = [g(z)] in homology"
    - "Because chain homotopic maps are equal"
    - "Because the chain groups are free abelian"
  answer: 1
  explanation: "The chain homotopy equation f - g = dP + Pd evaluated on a cycle z (with dz = 0) gives f(z) - g(z) = dP(z) + P(dz) = dP(z) + P(0) = dP(z). So f(z) and g(z) differ by a boundary dP(z), meaning they represent the same homology class. This is the chain-level version of 'homotopic maps induce the same map on homology.' The argument works for any chain homotopy, regardless of whether it comes from a topological homotopy."

- question: "Chain homotopy is an equivalence relation on chain maps from C_* to D_*."
  type: true-false
  answer: true
  explanation: "Reflexive: f ~ f via P = 0 (since f - f = 0 = d·0 + 0·d). Symmetric: if f ~ g via P (f - g = dP + Pd), then g - f = -(dP + Pd) = d(-P) + (-P)d, so g ~ f via -P. Transitive: if f ~ g via P and g ~ h via Q, then f - h = (f - g) + (g - h) = dP + Pd + dQ + Qd = d(P + Q) + (P + Q)d, so f ~ h via P + Q. These are straightforward algebraic verifications."

- question: "A chain map f: C_* → D_* is a chain homotopy equivalence if there exists a chain map g: D_* → C_* with g ∘ f ~ id_{C_*} and f ∘ g ~ id_{D_*}. Such maps always induce isomorphisms on homology."
  type: true-false
  answer: true
  explanation: "If g ∘ f ~ id, then (g ∘ f)_* = g_* ∘ f_* = id_* on homology. Similarly f_* ∘ g_* = id_*. So f_* and g_* are inverse isomorphisms. This means chain homotopy equivalent complexes have isomorphic homology. The converse is not generally true: two chain complexes with isomorphic homology need not be chain homotopy equivalent (just as two spaces with the same homology need not be homotopy equivalent)."

- question: "Explain how the chain homotopy for the proof that homotopic maps induce the same map on homology is constructed from a topological homotopy H: X × [0,1] → Y."
  type: short-answer
  answer: "The prism operator P_n: C_n(X) → C_{n+1}(Y) is defined using a triangulation of Δ^n × [0,1]. Each singular n-simplex σ: Δ^n → X is 'thickened' to a prism σ × id: Δ^n × [0,1] → X × [0,1], and composing with H gives a map to Y. Triangulating the prism Δ^n × [0,1] into (n+1)-simplices gives a chain in C_{n+1}(Y). The boundary of this prism chain, by geometry, equals f#(σ) - g#(σ) plus lower-dimensional prism terms, yielding the chain homotopy equation f# - g# = dP + Pd."
  explanation: "The prism operator is the algebraic distillation of the geometric fact that a homotopy sweeps out a prism. The triangulation of Δ^n × [0,1] into (n+1)-simplices is standard (using n+1 simplices), and the boundary formula for this triangulation directly gives the chain homotopy relation. This construction is the technical heart of the proof of homotopy invariance of singular homology."
```

## Explainer

**Chain homotopy** is the algebraic analog of topological homotopy. In topology, two maps f, g : X -> Y are homotopic if there is a continuous deformation between them. In homological algebra, two chain maps f, g : C_* -> D_* are chain homotopic if there exists a sequence of homomorphisms P_n : C_n -> D_{n+1} (called a **chain homotopy** or **homotopy operator**) satisfying f_n - g_n = d_{n+1} compose P_n + P_{n-1} compose d_n for all n. The chain homotopy P "connects" f and g at the chain level, just as a homotopy H connects two maps at the space level.

The crucial consequence of chain homotopy is that **chain homotopic maps induce identical maps on homology**. The proof is direct: for a cycle z in ker(d_n), we have f(z) - g(z) = dP(z) + Pd(z) = dP(z) (since d(z) = 0). So f(z) - g(z) is a boundary, meaning [f(z)] = [g(z)] in homology. This is the algebraic mechanism underlying the topological theorem that homotopic maps induce the same homomorphism on homology. The proof of homotopy invariance of singular homology constructs the chain homotopy P (the "prism operator") from the given topological homotopy H : X x [0,1] -> Y, and the rest follows from this algebraic lemma.

Two chain complexes C_* and D_* are **chain homotopy equivalent** if there exist chain maps f : C_* -> D_* and g : D_* -> C_* with g compose f chain homotopic to id_{C_*} and f compose g chain homotopic to id_{D_*}. Chain homotopy equivalent complexes have isomorphic homology in every degree. This is the chain-level analog of homotopy equivalence: just as homotopy equivalent spaces have the same homology, chain homotopy equivalent complexes have the same homology. The theory of derived categories formalizes this by treating chain homotopy equivalent complexes as "the same object."

The **prism operator** construction is worth understanding in detail. Given a homotopy H : X x [0,1] -> Y between f = H(-, 0) and g = H(-, 1), define P_n : C_n(X) -> C_{n+1}(Y) as follows. For a singular n-simplex sigma : Delta^n -> X, consider the prism Delta^n x [0,1]. Triangulate this prism into (n+1)-simplices (there is a standard triangulation using n+1 simplices, corresponding to the n+1 orderings of "when each vertex moves from the bottom to the top"). Compose with sigma x id : Delta^n x [0,1] -> X x [0,1] and then with H to get (n+1)-chains in Y. The alternating sum of these gives P_n(sigma). The boundary of the prism equals the top face minus the bottom face minus the lateral faces, which translates algebraically to dP + Pd = f_# - g_#.

Chain homotopy equivalence is strictly weaker than isomorphism of chain complexes but strictly stronger than isomorphism of homology. Two non-isomorphic chain complexes can be chain homotopy equivalent (just as non-homeomorphic spaces can be homotopy equivalent), and two chain complexes with isomorphic homology need not be chain homotopy equivalent (just as spaces with the same homology need not be homotopy equivalent — e.g., the lens spaces L(7,1) and L(7,2) have isomorphic homology but are not homotopy equivalent). Chain homotopy equivalence occupies the "Goldilocks zone" for algebraic topology: it is fine enough to capture meaningful topological distinctions but coarse enough to identify spaces and complexes that are "the same" from the perspective of homological invariants.
