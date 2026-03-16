---
id: galois-groups
title: Galois Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: finite-fields
  type: hard
- id: group-definition-examples
  type: hard
builds-toward:
- fundamental-theorem-galois-theory
tags:
- galois-group
- automorphism
- field-automorphism
stage: advanced
status: draft
---

# Galois Groups

## Core Idea
The Galois group Gal(K/F) of a field extension K/F is the group of field automorphisms of K that fix F element-wise. For separable extensions, the order of the Galois group equals the degree of the extension.

## Explainer

You already know what a group is — a set with an associative binary operation, identity, and inverses. You've also seen finite fields, where the structure of a field can be tightly controlled. A **Galois group** merges these two ideas: it captures the symmetry of a field extension by collecting all the ways you can permute the larger field while leaving the smaller one untouched.

Concretely, an **automorphism** of a field K is a bijective map φ: K → K that preserves addition and multiplication — φ(a+b) = φ(a)+φ(b) and φ(ab) = φ(a)φ(b). The condition "fixing F element-wise" means φ(f) = f for every f ∈ F. Think of F as a rigid backbone that every symmetry must respect, while the extension elements are free to permute among themselves. The group operation is function composition.

As a concrete example, consider the extension ℚ(√2)/ℚ. Any automorphism must fix every rational number and must send √2 to a root of x² − 2, which are ±√2. So there are exactly two automorphisms: the identity (√2 ↦ √2) and the conjugation map (√2 ↦ −√2). These form the group {id, σ} under composition, which is isomorphic to ℤ/2ℤ. The **degree** [ℚ(√2):ℚ] = 2, and indeed |Gal(ℚ(√2)/ℚ)| = 2, confirming the fundamental count: for Galois extensions, the group order equals the extension degree.

The real power emerges when you connect group structure to field structure. Subgroups of Gal(K/F) correspond precisely to intermediate fields between F and K — this is the content of the Fundamental Theorem of Galois Theory, which you'll see next. Solvability of polynomials by radicals (the original question Galois answered) translates into whether the Galois group has a special algebraic property called solvability. The abstract symmetry of the group encodes everything about how the roots of the polynomial relate to each other — an extraordinary compression of algebraic information into group theory.
