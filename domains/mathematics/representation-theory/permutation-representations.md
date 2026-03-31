---
id: permutation-representations
title: Permutation Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: group-actions
  type: hard
- id: character-theory
  type: soft
builds-toward:
- burnsides-theorem
- induced-representations
tags:
- permutation-representation
- permutation-module
- orbit-counting
- G-set
stage: expert
status: validated
---

# Permutation Representations

## Core Idea
A permutation representation arises from a group action on a finite set X: each element g ∈ G permutes the elements of X, giving a homomorphism G → S_X. Linearizing this action over a field k produces a representation on k^X (the free vector space with basis X), where g acts by permuting basis vectors. The character of a permutation representation evaluated at g counts the number of fixed points of g on X. Permutation representations are the most concrete class of representations and provide a bridge between combinatorial group actions and linear algebra.

## Questions

```yaml
- question: "S₃ acts on {1, 2, 3} by permutation. The resulting permutation representation has dimension 3. What is its decomposition into irreducible representations of S₃?"
  type: short-answer
  answer: "The permutation representation decomposes as the trivial representation ⊕ the standard 2-dimensional representation."
  explanation: "The character of the permutation representation is χ(e) = 3, χ((12)) = 1, χ((123)) = 0 (counting fixed points). The trivial representation has character (1,1,1) and the standard has (2,0,−1). Taking inner products: ⟨χ, χ_triv⟩ = (3+3+0)/6 = 1, ⟨χ, χ_sign⟩ = (3−3+0)/6 = 0, ⟨χ, χ_std⟩ = (6+0+0)/6 = 1. So χ = χ_triv + χ_std. The trivial summand is the span of e₁+e₂+e₃."

- question: "The character of a permutation representation counts fixed points: χ(g) = |Fix(g)| = |{x ∈ X : g·x = x}|."
  type: true-false
  answer: true
  explanation: "In the permutation representation, g sends basis vector eₓ to e_{g·x}. The trace of this permutation matrix counts the number of basis vectors fixed by g, which is exactly |{x ∈ X : g·x = x}|. This makes permutation characters easy to compute without constructing matrices — just count fixed points for each group element."

- question: "Every permutation representation on a set with |X| ≥ 2 contains the trivial representation as a subrepresentation."
  type: true-false
  answer: true
  explanation: "The vector v = Σ_{x∈X} eₓ (the sum of all basis vectors) is fixed by every group element, since g permutes the basis vectors. So span{v} is a 1-dimensional G-invariant subspace on which G acts trivially. By Maschke's theorem (over ℂ), this splits off as a direct summand. The complementary (|X|−1)-dimensional subspace {Σ aₓeₓ : Σ aₓ = 0} is also G-invariant and may or may not be irreducible."

- question: "Burnside's lemma states that the number of orbits of G acting on X equals:"
  type: multiple-choice
  options:
    - "The dimension of the permutation representation"
    - "(1/|G|) Σ_{g∈G} |Fix(g)|, the average number of fixed points"
    - "The number of irreducible representations of G"
    - "|X| / |G|"
  answer: 1
  explanation: "Burnside's lemma gives |X/G| = (1/|G|) Σ_{g∈G} |Fix(g)|. In representation-theoretic terms, this is ⟨χ_perm, χ_triv⟩ — the multiplicity of the trivial representation in the permutation representation. Since χ_triv = 1 everywhere, the inner product computes exactly the average number of fixed points. Each orbit contributes one copy of the trivial representation."

- question: "If G acts transitively on X with stabilizer H = Stab(x₀), the permutation representation on X is isomorphic to:"
  type: multiple-choice
  options:
    - "The regular representation of G"
    - "The induced representation Ind_H^G(trivial)"
    - "The trivial representation of dimension |X|"
    - "The sign representation tensored with itself"
  answer: 1
  explanation: "When G acts transitively on X, we can identify X with G/H (the coset space). The permutation representation is then G acting on the left cosets of H by left multiplication. This is precisely the induced representation of the trivial representation of H to G: Ind_H^G(1_H). This connection between transitive permutation representations and induced representations is fundamental. When H = {e}, G/H = G and we recover the regular representation."
```

## Explainer

A **permutation representation** starts with a group action G × X → X on a finite set X. Each g ∈ G defines a permutation σ_g: X → X, giving a homomorphism G → Sym(X). To get a linear representation, we **linearize**: form the free vector space k^X with basis {eₓ : x ∈ X} and define ρ(g)(eₓ) = e_{g·x}. The representing matrices are permutation matrices — exactly one 1 in each row and column — and the dimension is |X|. This is the most natural way to pass from combinatorial group theory to representation theory.

The character of a permutation representation has a beautiful combinatorial interpretation: **χ(g) = |Fix(g)|**, the number of elements of X fixed by g. This is because the trace of a permutation matrix counts the 1s on the diagonal, which correspond to basis vectors eₓ with g·x = x. This makes permutation characters far easier to compute than general characters — no eigenvalue calculations needed, just counting. Burnside's lemma, which counts orbits as the average number of fixed points, is a direct corollary: |X/G| = (1/|G|) Σ_{g∈G} χ(g) = ⟨χ, 1⟩, the inner product of the permutation character with the trivial character.

Every permutation representation contains the **trivial subrepresentation** spanned by Σ eₓ (since permutations preserve this sum). The **augmentation subspace** {Σ aₓeₓ : Σ aₓ = 0} is the complementary G-invariant subspace of codimension 1. For the natural action of Sₙ on {1, …, n}, this augmentation subspace is the **standard representation** of Sₙ, which is irreducible for n ≥ 2.

The connection to **induced representations** gives permutation representations their structural depth. If G acts transitively on X, then X ≅ G/H as a G-set, where H is the stabilizer of any point. The corresponding permutation representation is Ind_H^G(1_H), the induction of the trivial representation from H to G. This allows all tools of induced representations (Frobenius reciprocity, Mackey's formula) to be applied to permutation representations. Conversely, every induced representation of a 1-dimensional character is a generalized permutation representation, so the induction machinery is a direct generalization of the permutation construction.
