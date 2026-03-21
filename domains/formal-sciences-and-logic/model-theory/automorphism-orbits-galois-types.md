---
id: automorphism-orbits-galois-types
title: Automorphism Orbits and Galois Types
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: automorphism-groups-of-models
  type: hard
- id: type-spaces-and-stone-topology
  type: soft
tags:
- automorphism
- orbit
- Galois
- type
- symmetry
stage: advanced
status: draft
---

# Automorphism Orbits and Galois Types

## Core Idea
The automorphism group Aut(M) of a model M acts on its elements; orbits of this action are equivalence classes under symmetry. Galois types formalize this: two elements have the same Galois type over a set A if there is an automorphism of M fixing A pointwise that maps one to the other. In classical algebra (Galois theory), Galois types correspond to algebraic conjugacy; the model-theoretic notion generalizes this widely.

## How It's Best Learned
Study automorphisms of (C, +, ·) fixing Q: two algebraic numbers are conjugate iff they have the same Galois type over Q, connecting Galois theory to model-theoretic types.

## Questions

```yaml
- question: "In the field ℂ with automorphisms fixing ℚ, which pair of numbers shares a Galois type over ℚ, and why?"
  type: multiple-choice
  options:
    - "π and e, because both are transcendental and no algebraic formula can distinguish them over ℚ"
    - "√2 and −√2, because they are roots of the same irreducible polynomial x²−2 over ℚ, related by a ℚ-fixing automorphism"
    - "√2 and √3, because both are irrational square roots with the same degree over ℚ"
    - "i and −1, because they are both non-real complex numbers"
  answer: 1
  explanation: "√2 and −√2 are conjugate roots of x²−2, and the map √2 ↦ −√2 extends to a field automorphism of ℚ(√2) fixing ℚ pointwise — they share a Galois type over ℚ. While π and e are both transcendental, it is not known whether any ℚ-fixing automorphism of ℂ sends π to e; their orbit structure is far from obvious. √2 and √3 have different minimal polynomials (x²−2 vs x²−3) over ℚ, so no ℚ-fixing automorphism maps one to the other — different Galois types."

- question: "In the dense linear order (ℚ, <), what is the Galois type structure over the empty base set ∅?"
  type: multiple-choice
  options:
    - "Each rational number has its own unique Galois type, since different rationals occupy different positions"
    - "All rationals share a single Galois type over ∅, since any rational can be mapped to any other by an order-preserving automorphism"
    - "Rationals split into two Galois types: positive and negative"
    - "Galois types are undefined for linear orders because they are not algebraic structures"
  answer: 1
  explanation: "In (ℚ, <), for any two rationals a and b, the translation x ↦ x + (b−a) is an order-preserving bijection of ℚ to itself sending a to b. Since any element can be mapped to any other by an automorphism, the entire domain is a single orbit under Aut(ℚ, <) over ∅ — one Galois type. This makes (ℚ, <) ω-categorical: maximally symmetric, with no formula over ∅ that can distinguish any two elements by position alone."

- question: "Two elements having the same Galois type over A means there is no formula with parameters from A that is satisfied by one but not the other."
  type: true-false
  answer: true
  explanation: "If σ ∈ Aut(M/A) sends a to b, then for any formula φ(x) with parameters from A, M ⊨ φ(a) iff M ⊨ φ(σ(a)) = φ(b) — the automorphism preserves all relations and fixes every parameter. So a and b satisfy exactly the same formulas over A. They are genuinely indistinguishable by the language with A-parameters. This is the model-theoretic formalization of 'symmetric relative to A': the structure cannot, even in principle, tell them apart using A as a reference frame."

- question: "In every model, the Galois type of an element over A is the same as its syntactic type — the set of all A-parameter formulas the element satisfies."
  type: true-false
  answer: false
  explanation: "Galois types (orbit-based) and syntactic types (formula-based) agree in saturated and homogeneous models, but can diverge in arbitrary models. Same syntactic type means same set of formulas is satisfied — an outside-in, linguistic description. Same Galois type means an automorphism connects them — an inside-out, structural description. In a model lacking sufficient automorphisms (not saturated or homogeneous), two elements may satisfy exactly the same formulas but no automorphism sends one to the other. Stability theory largely studies when these notions coincide."

- question: "How does the model-theoretic notion of Galois type generalize the classical notion of algebraic conjugacy from Galois theory?"
  type: short-answer
  answer: "In classical Galois theory, two algebraic numbers are conjugate over ℚ iff they are roots of the same irreducible polynomial over ℚ — equivalently, iff a field automorphism of the algebraic closure fixing ℚ maps one to the other. The model-theoretic Galois type over A is the orbit of an element under Aut(M/A), the automorphisms of M fixing A pointwise. Substituting M = ℂ and A = ℚ recovers classical conjugacy exactly: same Galois type over ℚ iff conjugate algebraic numbers. The model-theoretic version applies this idea to any first-order structure and any base set, making 'indistinguishable by symmetry over A' meaningful universally."
  explanation: "The key abstraction is that conjugacy in classical Galois theory is really about orbits under a symmetry group fixing a base — a purely structural idea that model theory extracted and applied to all first-order structures. Stability theory then studies when this orbit-based indistinguishability agrees with formula-based indistinguishability."
```

## Explainer

You know from studying **automorphism groups of models** that an automorphism of a structure M is a bijection M → M that preserves all the relations and functions of M. When the automorphism group Aut(M) acts on the elements of M, it partitions those elements into **orbits**: two elements a and b are in the same orbit if some automorphism sends a to b. Elements in the same orbit are "indistinguishable by symmetry" — the model cannot tell them apart structurally. In a dense linear order without endpoints like (ℚ, <), any two elements are in the same orbit (any rational can be mapped to any other by an order-preserving bijection), so the entire domain is one orbit.

**Galois types** make this orbit notion relative to a base set. Fix a model M and a subset A ⊆ M. A **Galois type** of an element b over A is the orbit of b under the subgroup Aut(M/A) — the automorphisms of M that fix every element of A pointwise. Two elements have the same Galois type over A if and only if some A-fixing automorphism maps one to the other. This captures a precise notion of "structural indistinguishability over A": no formula with parameters from A can separate them.

The connection to classical Galois theory is the primary intuition. In the field ℂ of complex numbers, consider the automorphisms fixing ℚ pointwise. Two algebraic numbers α and β have the same Galois type over ℚ precisely when they are **conjugate** — roots of the same irreducible polynomial over ℚ. For instance, √2 and −√2 are conjugates and thus share a Galois type over ℚ, because the map √2 ↦ −√2 extends to a field automorphism of ℚ(√2) fixing ℚ. Transcendental numbers like π and e are both in the same orbit under Aut(ℂ/ℚ) — indistinguishable over ℚ by any algebraic formula — because no algebraic relation can pin down transcendentals.

Galois types should be compared with **syntactic types** from type-spaces-and-stone-topology. A syntactic type of b over A is the set of all formulas with parameters in A satisfied by b; it describes b from the outside via the language. A Galois type describes b from the inside via automorphisms. In **saturated and homogeneous models**, these notions agree: syntactic type equality implies orbit membership and vice versa. But in arbitrary models they can diverge, and the gap between them measures how far the model is from being well-behaved in the model-theoretic sense. Stability theory largely studies when syntactic and Galois types coincide.
