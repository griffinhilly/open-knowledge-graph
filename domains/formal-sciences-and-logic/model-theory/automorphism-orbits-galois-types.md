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
stage: abstract-reasoning
status: draft
---

# Automorphism Orbits and Galois Types

## Core Idea
The automorphism group Aut(M) of a model M acts on its elements; orbits of this action are equivalence classes under symmetry. Galois types formalize this: two elements have the same Galois type over a set A if there is an automorphism of M fixing A pointwise that maps one to the other. In classical algebra (Galois theory), Galois types correspond to algebraic conjugacy; the model-theoretic notion generalizes this widely.

## How It's Best Learned
Study automorphisms of (C, +, ·) fixing Q: two algebraic numbers are conjugate iff they have the same Galois type over Q, connecting Galois theory to model-theoretic types.

## Explainer

You know from studying **automorphism groups of models** that an automorphism of a structure M is a bijection M → M that preserves all the relations and functions of M. When the automorphism group Aut(M) acts on the elements of M, it partitions those elements into **orbits**: two elements a and b are in the same orbit if some automorphism sends a to b. Elements in the same orbit are "indistinguishable by symmetry" — the model cannot tell them apart structurally. In a dense linear order without endpoints like (ℚ, <), any two elements are in the same orbit (any rational can be mapped to any other by an order-preserving bijection), so the entire domain is one orbit.

**Galois types** make this orbit notion relative to a base set. Fix a model M and a subset A ⊆ M. A **Galois type** of an element b over A is the orbit of b under the subgroup Aut(M/A) — the automorphisms of M that fix every element of A pointwise. Two elements have the same Galois type over A if and only if some A-fixing automorphism maps one to the other. This captures a precise notion of "structural indistinguishability over A": no formula with parameters from A can separate them.

The connection to classical Galois theory is the primary intuition. In the field ℂ of complex numbers, consider the automorphisms fixing ℚ pointwise. Two algebraic numbers α and β have the same Galois type over ℚ precisely when they are **conjugate** — roots of the same irreducible polynomial over ℚ. For instance, √2 and −√2 are conjugates and thus share a Galois type over ℚ, because the map √2 ↦ −√2 extends to a field automorphism of ℚ(√2) fixing ℚ. Transcendental numbers like π and e are both in the same orbit under Aut(ℂ/ℚ) — indistinguishable over ℚ by any algebraic formula — because no algebraic relation can pin down transcendentals.

Galois types should be compared with **syntactic types** from type-spaces-and-stone-topology. A syntactic type of b over A is the set of all formulas with parameters in A satisfied by b; it describes b from the outside via the language. A Galois type describes b from the inside via automorphisms. In **saturated and homogeneous models**, these notions agree: syntactic type equality implies orbit membership and vice versa. But in arbitrary models they can diverge, and the gap between them measures how far the model is from being well-behaved in the model-theoretic sense. Stability theory largely studies when syntactic and Galois types coincide.
