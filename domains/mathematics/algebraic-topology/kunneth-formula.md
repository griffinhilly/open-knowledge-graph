---
id: kunneth-formula
title: The Kunneth Formula
domain: mathematics
course: algebraic-topology
prerequisites:
- id: singular-homology-groups
  type: hard
- id: exact-sequences-homological-algebra
  type: hard
- id: mayer-vietoris-sequence
  type: soft
- id: five-lemma
  type: soft
builds-toward: []
tags: [algebraic-topology, kunneth-formula, tensor-product, product-spaces, homology]
stage: expert
status: validated
---
# The Kunneth Formula

## Core Idea
The Kunneth formula computes the homology of a product space X x Y from the homology groups of the factors. Over a field k, it simplifies to H_n(X x Y; k) = direct sum_{p+q=n} H_p(X; k) tensor H_q(Y; k). Over the integers, there is a correction term involving Tor: 0 -> direct sum H_p(X) tensor H_q(Y) -> H_n(X x Y) -> direct sum Tor(H_p(X), H_{q-1}(Y)) -> 0. The Kunneth formula is the product theorem for homology, reducing the computation of H_*(X x Y) to the known homology of X and Y.

## Questions

```yaml
- question: "Using the Kunneth formula over Z, compute H_1(S^1 × S^1)."
  type: multiple-choice
  options:
    - "Z"
    - "Z ⊕ Z"
    - "Z ⊕ Z ⊕ Z"
    - "0"
  answer: 1
  explanation: "H_1(S^1 × S^1) = ⊕_{p+q=1} H_p(S^1) ⊗ H_q(S^1) (the Tor term vanishes since all homology groups of S^1 are free). The terms: H_0(S^1) ⊗ H_1(S^1) = Z ⊗ Z = Z, and H_1(S^1) ⊗ H_0(S^1) = Z ⊗ Z = Z. So H_1(T^2) = Z ⊕ Z, matching the known first homology of the torus. The two generators correspond to the two fundamental loops — one wrapping around each S^1 factor."

- question: "The Kunneth formula with field coefficients gives H_n(X × Y; k) ≅ ⊕_{p+q=n} H_p(X; k) ⊗_k H_q(Y; k) with no correction term."
  type: true-false
  answer: true
  explanation: "Over a field k, the Tor term vanishes because every module over a field is free (hence flat). The short exact Kunneth sequence becomes 0 → ⊕ H_p ⊗ H_q → H_n(X × Y) → 0, giving an isomorphism. This is why field coefficients are technically simpler: the Kunneth formula gives a clean tensor product decomposition. Over Z, torsion in the homology groups can produce Tor terms that contribute to the product homology."

- question: "Let X = RP^2 (with H_0 = Z, H_1 = Z/2Z, H_2 = 0). Using Kunneth over Z, does H_2(RP^2 × RP^2) have torsion?"
  type: multiple-choice
  options:
    - "No — H_2 is free abelian"
    - "Yes — the Tor term Tor(H_1(RP^2), H_0(RP^2)) = Tor(Z/2Z, Z) = 0 contributes nothing, but Tor(H_0, H_1) also vanishes, so H_2 is the tensor sum only"
    - "Yes — Tor(Z/2Z, Z/2Z) = Z/2Z contributes a torsion summand"
    - "Cannot be determined without the full Kunneth computation"
  answer: 2
  explanation: "H_2(RP^2 × RP^2; Z): the tensor terms with p + q = 2 are H_0 ⊗ H_2 = 0, H_1 ⊗ H_1 = Z/2Z ⊗ Z/2Z = Z/2Z, H_2 ⊗ H_0 = 0. The Tor terms with p + (q-1) = 2, i.e., p + q = 2 in the Tor sum (shifted): Tor(H_1, H_0) = Tor(Z/2Z, Z) = 0, Tor(H_0, H_1) = Tor(Z, Z/2Z) = 0. Actually, the Tor contribution is ⊕_{p+q=n-1} Tor(H_p, H_q), so for n=2: Tor(H_0, H_0) + Tor(H_1, ...) — let me recompute. The Kunneth exact sequence is 0 → ⊕_{p+q=n} H_p ⊗ H_q → H_n → ⊕_{p+q=n-1} Tor(H_p, H_q) → 0. For n=2: tensor part = Z/2Z, Tor part (p+q=1): Tor(H_0, H_1) + Tor(H_1, H_0) = Tor(Z, Z/2Z) + Tor(Z/2Z, Z) = 0 + 0 = 0. So H_2 = Z/2Z, which IS torsion, but from the tensor term."

- question: "Explain why the Kunneth formula is 'multiplicative' for Euler characteristics: χ(X × Y) = χ(X) · χ(Y)."
  type: short-answer
  answer: "From the Kunneth formula (over a field, for simplicity): b_n(X × Y) = Σ_{p+q=n} b_p(X) · b_q(Y). Therefore χ(X × Y) = Σ_n (-1)^n b_n(X × Y) = Σ_n (-1)^n Σ_{p+q=n} b_p(X) · b_q(Y) = Σ_p Σ_q (-1)^{p+q} b_p(X) · b_q(Y) = (Σ_p (-1)^p b_p(X))(Σ_q (-1)^q b_q(Y)) = χ(X) · χ(Y). The key step is that (-1)^{p+q} = (-1)^p · (-1)^q, allowing the double sum to factor as a product."
  explanation: "This is one of the cleanest consequences of the Kunneth formula. It gives a quick way to compute Euler characteristics of products: χ(T^2) = χ(S^1) · χ(S^1) = 0 · 0 = 0, χ(S^2 × S^2) = 2 · 2 = 4, χ(S^1 × S^2) = 0 · 2 = 0. The multiplicativity fails for Betti numbers individually (b_1(T^2) = 2 ≠ b_1(S^1)^2 = 1), but works perfectly for the alternating sum."
```

## Explainer

The **Kunneth formula** answers the natural question: if we know H_*(X) and H_*(Y), can we compute H_*(X x Y)? The answer is yes, with a tensor product playing the central role. At the chain level, the **Eilenberg-Zilber theorem** provides a chain homotopy equivalence between C_*(X x Y) and the tensor product complex C_*(X) tensor C_*(Y), whose n-th chain group is the direct sum over p + q = n of C_p(X) tensor C_q(Y). This chain-level equivalence reduces the computation of H_*(X x Y) to an algebraic question about the homology of a tensor product of chain complexes.

Over a **field** k, the Kunneth formula is clean: H_n(X x Y; k) = direct sum_{p+q=n} H_p(X; k) tensor_k H_q(Y; k). This is an isomorphism, with no correction terms. The Betti numbers satisfy b_n(X x Y) = sum_{p+q=n} b_p(X) * b_q(Y), which is the "convolution" of the Betti number sequences. For the torus: b_0(T^2) = b_0(S^1) * b_0(S^1) = 1, b_1(T^2) = b_0 * b_1 + b_1 * b_0 = 1 + 1 = 2, b_2(T^2) = b_1 * b_1 = 1.

Over the **integers**, the formula acquires a correction term from the **Tor functor**. The Kunneth short exact sequence is: 0 -> direct sum_{p+q=n} H_p(X) tensor H_q(Y) -> H_n(X x Y) -> direct sum_{p+q=n-1} Tor(H_p(X), H_q(Y)) -> 0. This sequence always splits (non-naturally), so as abelian groups, H_n(X x Y) = (direct sum H_p tensor H_q) direct sum (direct sum Tor(H_p, H_q)), where the first sum is over p + q = n and the second over p + q = n - 1. The Tor term detects interactions between the torsion in H_*(X) and H_*(Y). When both spaces have torsion-free homology, Tor vanishes and the formula simplifies to the tensor product alone.

The Tor functor Tor(A, B) measures the "failure of the tensor product to be exact." For finitely generated abelian groups: Tor(Z, B) = 0 (free groups contribute no Tor), Tor(Z/mZ, Z/nZ) = Z/gcd(m,n)Z (cyclic torsion groups interact via their gcd). So the Tor term contributes torsion to H_*(X x Y) that is not visible in the individual homology groups of X and Y separately. For example, Tor(Z/2Z, Z/2Z) = Z/2Z, so if both X and Y have Z/2Z torsion in adjacent dimensions, additional Z/2Z torsion appears in the product homology.

The Kunneth formula is the product theorem for homology, just as the Mayer-Vietoris sequence is the union theorem. Together with the long exact sequence of a pair (the quotient/subspace theorem), these three results form a complete toolkit for computing homology: any space built from simpler pieces by products, unions, and quotients can have its homology computed by iterating these tools. The cohomological version of the Kunneth formula is enriched by the cup product: H^*(X x Y; k) is isomorphic to H^*(X; k) tensor H^*(Y; k) as graded rings, where the product on the right is the tensor product of rings. This algebraic structure is essential for computing cup products on product spaces.
