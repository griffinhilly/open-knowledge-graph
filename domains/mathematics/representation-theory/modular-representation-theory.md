---
id: modular-representation-theory
title: Modular Representation Theory
domain: mathematics
course: representation-theory
prerequisites:
- id: maschkes-theorem
  type: hard
- id: semisimplicity-and-wedderburn
  type: hard
- id: character-theory
  type: soft
builds-toward: []
tags:
- modular-representation
- brauer-character
- blocks
- defect-group
- characteristic-p
stage: expert
status: validated
---

# Modular Representation Theory

## Core Idea
Modular representation theory studies representations of finite groups over fields whose characteristic p divides the group order |G|. In this setting, Maschke's theorem fails — the group algebra is no longer semisimple, and representations need not decompose into irreducible summands. Indecomposable representations (which cannot be written as direct sums) need not be irreducible, and the Jordan-Hölder composition factors of a module become the primary objects of study. Brauer characters replace ordinary characters, and the representation theory organizes into blocks determined by p-local structure.

## Questions

```yaml
- question: "Over a field of characteristic p dividing |G|, which fundamental theorem of ordinary representation theory fails?"
  type: multiple-choice
  options:
    - "Schur's lemma"
    - "Maschke's theorem (complete reducibility)"
    - "The existence of a character map"
    - "The fact that representations are group homomorphisms"
  answer: 1
  explanation: "Maschke's theorem requires dividing by |G|, which is impossible when char(k) divides |G| (since |G| = 0 in k). Without complete reducibility, the category of representations is no longer semisimple. Schur's lemma still holds (it uses only irreducibility and linear algebra). Characters still exist as traces, but they lose much of their power because non-isomorphic indecomposable modules can have the same composition factors."

- question: "In characteristic p, an indecomposable module is always irreducible."
  type: true-false
  answer: false
  explanation: "This is the key distinction in modular theory. A module is indecomposable if it cannot be written as M₁ ⊕ M₂ with both nonzero; it is irreducible if it has no proper nonzero submodules. In the semisimple case (Maschke), these coincide. In the modular case, there exist indecomposable modules with proper submodules that are not direct summands. For example, the 2-dimensional representation of ℤ/pℤ over 𝔽_p given by [[1,1],[0,1]] is indecomposable but not irreducible."

- question: "The number of irreducible representations of G over an algebraically closed field of characteristic p equals:"
  type: multiple-choice
  options:
    - "The number of conjugacy classes of G"
    - "The number of p-regular conjugacy classes (classes of elements whose order is not divisible by p)"
    - "The number of Sylow p-subgroups"
    - "|G|/p"
  answer: 1
  explanation: "In characteristic 0, the number of irreducibles equals the total number of conjugacy classes. In characteristic p, it equals the number of p-regular (also called p'-) conjugacy classes. An element g is p-regular if its order is coprime to p. This is because the Brauer characters, which replace ordinary characters in modular theory, are only defined on p-regular elements and satisfy orthogonality relations on this restricted set."

- question: "Brauer characters are defined only on p-regular elements of G. Why can't ordinary trace be used as a character in characteristic p?"
  type: short-answer
  answer: "The trace of a matrix over a field of characteristic p takes values in that field, where distinct eigenvalue configurations can give the same trace (e.g., a matrix with p identical eigenvalues λ has trace pλ = 0). Brauer's solution is to lift eigenvalues to characteristic 0 via a ring of p-adic integers and take the trace there, but this only works for elements whose eigenvalues are roots of unity of order coprime to p — the p-regular elements."
  explanation: "In characteristic 0, the trace determines the multiset of eigenvalues (via Newton's identities). In characteristic p, information is lost: tr([[1,1],[0,1]]) = 2 = tr(I₂) over 𝔽₂, even though these matrices are not similar. Brauer characters bypass this by lifting to characteristic 0, recovering enough information to classify irreducible modules. The resulting theory is powerful but more intricate than ordinary character theory."
```

## Explainer

In **ordinary** (characteristic 0) representation theory, Maschke's theorem guarantees complete reducibility: every representation splits into a direct sum of irreducibles. When the field has characteristic p dividing |G|, this fails catastrophically. The group algebra k[G] has a nonzero **Jacobson radical** J(k[G]) — a nilpotent ideal consisting of elements that act as zero on every simple module. The quotient k[G]/J(k[G]) is semisimple, but the radical introduces nontrivial extensions between simple modules, creating indecomposable modules that are not irreducible.

The simplest example is G = ℤ/pℤ over 𝔽_p. The group algebra 𝔽_p[ℤ/pℤ] ≅ 𝔽_p[x]/(x^p − 1) = 𝔽_p[x]/((x−1)^p) (since x^p − 1 = (x−1)^p in characteristic p). This is a local ring with unique maximal ideal (x−1). The only irreducible module is the trivial representation 𝔽_p, but there are p indecomposable modules of dimensions 1, 2, …, p, corresponding to Jordan blocks of size 1 through p for the element (x−1). The Krull-Schmidt theorem guarantees unique decomposition into indecomposables, which replaces the irreducible decomposition.

**Brauer characters** are the modular replacement for ordinary characters. For a p-regular element g (one whose order is coprime to p), the eigenvalues of ρ(g) are roots of unity of order coprime to p. These can be lifted uniquely to complex roots of unity via a fixed embedding of the multiplicative group of the algebraic closure into ℂ*. The Brauer character φ(g) is the sum of these lifted eigenvalues. Brauer characters satisfy orthogonality relations on p-regular classes, and the number of irreducible Brauer characters equals the number of p-regular conjugacy classes.

The representation theory organizes into **blocks** — indecomposable direct summands of the group algebra k[G] as a (k[G], k[G])-bimodule. Each block is controlled by a **defect group**, a p-subgroup of G that measures how far the block is from being semisimple. A block with trivial defect group is a full matrix algebra (semisimple), while a block with defect group of order p^d has p^d simple modules and a rich structure of indecomposable modules. Brauer's three main theorems relate the blocks of G to blocks of local subgroups (normalizers of p-subgroups), creating a deep connection between modular representation theory and the p-local structure of G.
