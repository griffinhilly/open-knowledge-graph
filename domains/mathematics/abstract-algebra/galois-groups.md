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
- id: algebraic-and-transcendental-elements
  type: soft
builds-toward:
- fundamental-theorem-galois-theory
tags:
- galois-group
- automorphism
- field-automorphism
stage: expert
status: validated
---

# Galois Groups

## Core Idea
The Galois group Gal(K/F) of a field extension K/F is the group of field automorphisms of K that fix F element-wise. For separable extensions, the order of the Galois group equals the degree of the extension.

## Questions

```yaml
- question: "Consider the field extension ℚ(∛2)/ℚ. A student claims this extension has a Galois group of order 3 because ∛2 has three cube roots. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the Galois group of ℚ(∛2)/ℚ does have order 3"
    - "The Galois group has order 6, not 3, because you must count all permutations of the root"
    - "ℚ(∛2)/ℚ is not a Galois extension because the other cube roots of 2 are complex and not in ℚ(∛2); the automorphism group has order 1"
    - "The Galois group has order 2 because only real automorphisms are allowed"
  answer: 2
  explanation: "ℚ(∛2)/ℚ is not a Galois extension — it is not a normal extension because the minimal polynomial x³−2 has three roots (∛2, ∛2·ω, ∛2·ω²) but only one lies in ℚ(∛2). An automorphism of ℚ(∛2) fixing ℚ must send ∛2 to a root of x³−2 that lies in ℚ(∛2), and the only such root is ∛2 itself. So the only automorphism is the identity, giving |Gal(ℚ(∛2)/ℚ)| = 1, not [ℚ(∛2):ℚ] = 3. The Galois correspondence holds only for Galois (normal and separable) extensions."

- question: "What determines which elements an automorphism φ ∈ Gal(K/F) is allowed to send an extension element α to?"
  type: multiple-choice
  options:
    - "φ(α) can be any element of K, since automorphisms are bijections of K"
    - "φ(α) must equal α, since automorphisms preserve all algebraic relationships"
    - "φ(α) must be another root of the same minimal polynomial of α over F"
    - "φ(α) must be an element of F, since the automorphism fixes the base field"
  answer: 2
  explanation: "An automorphism φ fixes F and preserves field operations. If α satisfies an irreducible polynomial p(x) over F, then p(φ(α)) = φ(p(α)) = φ(0) = 0. So φ(α) must also be a root of the same minimal polynomial p(x). This constraint — that automorphisms permute roots of irreducible polynomials — is what limits the size of the Galois group and connects group structure to the root relationships. For ℚ(√2)/ℚ, √2 has minimal polynomial x²−2 with roots ±√2, so φ(√2) ∈ {√2, −√2} — exactly two choices, giving |Gal| = 2."

- question: "The Galois group Gal(K/F) can include automorphisms that move elements of the base field F."
  type: true-false
  answer: false
  explanation: "By definition, every element of Gal(K/F) fixes F element-wise: φ(f) = f for all f ∈ F. This constraint is the 'relative' part of the Galois group — it captures symmetries of the extension K that respect the structure of F as a rigid backbone. An automorphism of K that moved elements of F would not belong to Gal(K/F), even if it were a valid field automorphism of K in isolation."

- question: "For a Galois extension K/F of degree n, the Galois group Gal(K/F) has exactly n elements."
  type: true-false
  answer: true
  explanation: "This is the fundamental counting theorem of Galois theory: for separable (and hence Galois) extensions, |Gal(K/F)| = [K:F]. The example ℚ(√2)/ℚ illustrates this — the extension has degree 2 (a basis is {1, √2}), and the Galois group {identity, conjugation} has exactly 2 elements. This equality is non-trivial: there could in principle be fewer automorphisms (if the polynomial has repeated roots) or more (if we allow automorphisms not fixing F). Separability ensures neither pathology occurs."

- question: "Why must any automorphism φ in Gal(ℚ(√2)/ℚ) send √2 to either √2 or −√2, and not to some other value like √3 or 2?"
  type: short-answer
  answer: "The automorphism φ must fix ℚ (all rational numbers) and preserve field operations. Since (√2)² = 2 and 2 is rational (fixed by φ), we get φ(√2)² = φ((√2)²) = φ(2) = 2. So φ(√2) must be a square root of 2, which means φ(√2) ∈ {√2, −√2}. Both lie in ℚ(√2), so both give valid automorphisms. Neither √3 (which satisfies x²−3, not x²−2) nor 2 (which satisfies x²−2 only if 4=2, which is false) are roots of x²−2."
  explanation: "This reasoning generalizes: every Galois automorphism permutes the roots of each irreducible polynomial over F among themselves. The minimal polynomial of α over F encodes all the algebraic constraints on α, and any automorphism fixing F must respect those constraints. This is why computing Gal(K/F) reduces to counting how many ways the roots of the generating minimal polynomial can be permuted while remaining within K."
```

## Explainer

You already know what a group is — a set with an associative binary operation, identity, and inverses. You've also seen finite fields, where the structure of a field can be tightly controlled. A **Galois group** merges these two ideas: it captures the symmetry of a field extension by collecting all the ways you can permute the larger field while leaving the smaller one untouched.

Concretely, an **automorphism** of a field K is a bijective map φ: K → K that preserves addition and multiplication — φ(a+b) = φ(a)+φ(b) and φ(ab) = φ(a)φ(b). The condition "fixing F element-wise" means φ(f) = f for every f ∈ F. Think of F as a rigid backbone that every symmetry must respect, while the extension elements are free to permute among themselves. The group operation is function composition.

As a concrete example, consider the extension ℚ(√2)/ℚ. Any automorphism must fix every rational number and must send √2 to a root of x² − 2, which are ±√2. So there are exactly two automorphisms: the identity (√2 ↦ √2) and the conjugation map (√2 ↦ −√2). These form the group {id, σ} under composition, which is isomorphic to ℤ/2ℤ. The **degree** [ℚ(√2):ℚ] = 2, and indeed |Gal(ℚ(√2)/ℚ)| = 2, confirming the fundamental count: for Galois extensions, the group order equals the extension degree.

The real power emerges when you connect group structure to field structure. Subgroups of Gal(K/F) correspond precisely to intermediate fields between F and K — this is the content of the Fundamental Theorem of Galois Theory, which you'll see next. Solvability of polynomials by radicals (the original question Galois answered) translates into whether the Galois group has a special algebraic property called solvability. The abstract symmetry of the group encodes everything about how the roots of the polynomial relate to each other — an extraordinary compression of algebraic information into group theory.
