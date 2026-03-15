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
