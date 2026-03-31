---
id: representations-of-sl2
title: Representations of SL₂
domain: mathematics
course: representation-theory
prerequisites:
- id: lie-group-representations-intro
  type: hard
- id: reducibility-and-irreducibility
  type: hard
- id: linear-transformations
  type: soft
builds-toward: []
tags:
- sl2
- highest-weight
- casimir-element
- weight-space
- raising-lowering
stage: expert
status: validated
---

# Representations of SL₂

## Core Idea
The representation theory of SL₂(ℂ) (or equivalently its Lie algebra 𝔰𝔩₂(ℂ)) is the fundamental example in Lie theory. The Lie algebra 𝔰𝔩₂ is spanned by three elements e, f, h with [h,e] = 2e, [h,f] = −2f, [e,f] = h. The finite-dimensional irreducible representations are classified by a single non-negative integer n: for each n ≥ 0, there is a unique (n+1)-dimensional irreducible representation V(n) with highest weight n. The representation V(n) has a basis of weight vectors v_n, v_{n−2}, …, v_{−n} on which e raises weight by 2, f lowers weight by 2, and h acts by the weight.

## Questions

```yaml
- question: "How many finite-dimensional irreducible representations does 𝔰𝔩₂(ℂ) have?"
  type: multiple-choice
  options:
    - "Three (the trivial, standard, and adjoint)"
    - "Finitely many, one for each root of unity"
    - "Infinitely many — one for each non-negative integer n, of dimension n+1"
    - "Two — the standard and its dual"
  answer: 2
  explanation: "For each n = 0, 1, 2, 3, …, there is exactly one irreducible representation V(n) of dimension n+1. V(0) is the trivial representation. V(1) is the standard 2-dimensional representation. V(2) is the 3-dimensional adjoint representation (≅ 𝔰𝔩₂ acting on itself via the Lie bracket). V(3) is 4-dimensional, and so on. This is the complete classification: every finite-dimensional irreducible representation is isomorphic to exactly one V(n)."

- question: "In the irreducible representation V(n) of 𝔰𝔩₂, the element h acts diagonalizably with eigenvalues n, n−2, n−4, …, −n."
  type: true-false
  answer: true
  explanation: "V(n) has a basis {v_n, v_{n-2}, ..., v_{-n}} where h·v_m = m·v_m. The weights form the arithmetic sequence n, n−2, …, −n, decreasing by 2 at each step, giving n+1 weight spaces in total. Each weight space is 1-dimensional for irreducible representations of 𝔰𝔩₂. The element e maps v_m to a scalar multiple of v_{m+2} (raising operator) and f maps v_m to a scalar multiple of v_{m−2} (lowering operator)."

- question: "The Casimir element C = h² + 2ef + 2fe = h² + 2h + 4fe acts on the irreducible representation V(n) as a scalar. What scalar?"
  type: short-answer
  answer: "C acts on V(n) as multiplication by n(n+2), equivalently n² + 2n."
  explanation: "The Casimir element lies in the center of the universal enveloping algebra U(𝔰𝔩₂). By Schur's lemma, it acts as a scalar on each irreducible representation. Computing on the highest weight vector v_n: h²·v_n = n²v_n, and 2h·v_n = 2nv_n, and 4fe·v_n = 0 (since e·v_n = 0 for the highest weight vector). So C·v_n = (n² + 2n)v_n = n(n+2)v_n. This scalar distinguishes non-isomorphic irreducibles."

- question: "The standard representation V(1) of 𝔰𝔩₂ has dimension 2 with basis {v₁, v₋₁}. What is V(1) ⊗ V(1) as a direct sum of irreducibles?"
  type: multiple-choice
  options:
    - "V(2)"
    - "V(0) ⊕ V(2)"
    - "V(1) ⊕ V(1)"
    - "V(0) ⊕ V(1) ⊕ V(2)"
  answer: 1
  explanation: "V(1) ⊗ V(1) has dimension 4. The tensor product of representations with highest weights m and n decomposes by the Clebsch-Gordan formula: V(m) ⊗ V(n) ≅ V(m+n) ⊕ V(m+n−2) ⊕ ··· ⊕ V(|m−n|). For m = n = 1: V(1) ⊗ V(1) ≅ V(2) ⊕ V(0). Dimension check: 3 + 1 = 4. The V(2) component is the symmetric part (Sym²V(1)), and V(0) is the antisymmetric part (∧²V(1) ≅ det)."

- question: "Why is 𝔰𝔩₂ representation theory considered the 'template' for all semisimple Lie algebras?"
  type: short-answer
  answer: "Every semisimple Lie algebra contains copies of 𝔰𝔩₂ as subalgebras (one for each simple root), and the weight space decomposition of any representation restricts to an 𝔰𝔩₂-representation along each root direction. The entire highest weight classification for semisimple Lie algebras is built by combining these 𝔰𝔩₂ analyses across all root directions."
  explanation: "The root space decomposition of a semisimple Lie algebra 𝔤 identifies a triple {eα, fα, hα} ≅ 𝔰𝔩₂ for each root α. The representation theory of 𝔤 is analyzed by restricting to these 𝔰𝔩₂-triples: the integrality of weights, the finite-dimensionality criterion, and the Weyl character formula all ultimately rest on the 𝔰𝔩₂ classification. This is why every Lie theory textbook begins with 𝔰𝔩₂."
```

## Explainer

The Lie algebra **𝔰𝔩₂(ℂ)** consists of 2×2 traceless complex matrices. It is 3-dimensional with standard basis: e = [[0,1],[0,0]] (strictly upper triangular), f = [[0,0],[1,0]] (strictly lower triangular), and h = [[1,0],[0,−1]] (diagonal). The commutation relations are [h,e] = 2e, [h,f] = −2f, [e,f] = h. These relations, not the specific matrices, determine the representation theory. The element h generates a Cartan subalgebra, e is a raising operator, and f is a lowering operator.

A representation V of 𝔰𝔩₂ decomposes into **weight spaces** V = ⊕_λ V_λ, where V_λ = {v ∈ V : h·v = λv}. The commutation relations force e to raise weights by 2 (if v ∈ V_λ, then e·v ∈ V_{λ+2}) and f to lower weights by 2. In a finite-dimensional representation, there must be a **highest weight vector** v_λ with e·v_λ = 0 (since weights are bounded above). Starting from v_λ and applying f repeatedly generates v_λ, f·v_λ, f²·v_λ, … until reaching the lowest weight. If the highest weight is n, this chain has length n+1, producing an (n+1)-dimensional space with weights n, n−2, …, −n.

The **classification theorem** states: for each integer n ≥ 0, there is a unique irreducible representation V(n) of dimension n+1, and every finite-dimensional representation is a direct sum of these. The proof uses the **Casimir element** C = h² + 2h + 4fe ∈ U(𝔰𝔩₂), which lies in the center of the universal enveloping algebra and acts as the scalar n(n+2) on V(n). Since this scalar is distinct for each n, the Casimir separates irreducibles. Complete reducibility follows from the fact that SU(2) (the compact real form) is compact, so the analogue of Maschke's theorem applies.

The **Clebsch-Gordan formula** describes tensor products: V(m) ⊗ V(n) ≅ V(m+n) ⊕ V(m+n−2) ⊕ ··· ⊕ V(|m−n|), a multiplicity-free direct sum. This is the mathematical content of angular momentum addition in quantum mechanics (with V(n) corresponding to spin n/2). The formula can be proved by comparing characters or by explicitly constructing highest weight vectors in the tensor product. The entire structure — weight space decomposition, highest weight classification, Casimir element, Clebsch-Gordan decomposition — generalizes to all semisimple Lie algebras, with 𝔰𝔩₂ providing the blueprint for the general theory via the root system.
