---
id: schurs-lemma
title: Schur's Lemma
domain: mathematics
course: representation-theory
prerequisites:
- id: reducibility-and-irreducibility
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- character-theory
- orthogonality-relations
- artin-wedderburn-theorem
tags:
- schur
- intertwining-operator
- irreducible
stage: expert
status: validated
---

# Schur's Lemma

## Core Idea
Schur's lemma states that any intertwining operator between irreducible representations is either zero or an isomorphism. Over an algebraically closed field, any self-intertwining operator of an irreducible representation is a scalar multiple of the identity. This seemingly simple result has enormous consequences: it constrains the structure of Hom_G spaces, underpins the orthogonality relations for characters, and is the single most-used tool in representation theory.

## Questions

```yaml
- question: "Let T: V → W be a G-map between irreducible representations. Schur's lemma says T must be either zero or an isomorphism. Why can't T be a non-zero, non-invertible map?"
  type: short-answer
  answer: "The kernel ker(T) is a G-invariant subspace of V, and the image im(T) is a G-invariant subspace of W. Since V is irreducible, ker(T) is either {0} or V. If T ≠ 0, then ker(T) ≠ V, so ker(T) = {0} (T is injective). Since W is irreducible, im(T) is either {0} or W. Since T ≠ 0, im(T) = W (T is surjective). So T is bijective."
  explanation: "This proof is a model of how irreducibility arguments work: G-invariance of kernels and images (which follows from the intertwining condition) constrains them to be trivial or the whole space, leaving no middle ground. The proof uses nothing beyond the definition of irreducibility and basic linear algebra."

- question: "Over ℂ, if ρ: G → GL(V) is irreducible and T: V → V is a G-map, then T = λI for some scalar λ. Why does this fail over ℝ?"
  type: multiple-choice
  options:
    - "The real numbers are not a field"
    - "T may have no real eigenvalues, so the argument 'T − λI has nontrivial kernel' cannot be started"
    - "Schur's lemma does not apply over ℝ"
    - "Real matrices cannot be scalar multiples of the identity"
  answer: 1
  explanation: "Over ℂ (algebraically closed), every linear operator has at least one eigenvalue λ. Then T − λI is a G-map with nontrivial kernel, so by Schur's lemma it must be zero, giving T = λI. Over ℝ, a linear operator need not have real eigenvalues (e.g., a rotation by 90° on ℝ²), so the argument breaks down at the first step. Schur's lemma (first part) still holds over ℝ — it is only the scalar conclusion that requires algebraic closure."

- question: "Schur's lemma implies that irreducible representations of abelian groups over ℂ are one-dimensional."
  type: true-false
  answer: true
  explanation: "For an abelian group, every ρ(g) commutes with every ρ(h). So each ρ(g) is a G-map from the representation to itself. By Schur's lemma over ℂ, each ρ(g) = λ_g · I. But then every subspace is G-invariant (since scalar matrices preserve all subspaces). For the representation to be irreducible, V must have no proper nontrivial subspaces, which forces dim(V) = 1. This is a powerful structural result derived from a few lines of reasoning."

- question: "If V and W are non-isomorphic irreducible representations, then Hom_G(V, W) = {0}."
  type: true-false
  answer: true
  explanation: "By Schur's lemma, any G-map T: V → W is either zero or an isomorphism. If V and W are not isomorphic, the isomorphism case is excluded, so every G-map must be zero. This means Hom_G(V, W) contains only the zero map. Combined with the scalar result for Hom_G(V, V) ≅ ℂ (over algebraically closed fields), this completely determines the structure of Hom spaces between irreducibles."
```

## Explainer

Schur's lemma is the workhorse of representation theory. It comes in two parts. **Part 1**: If ρ: G → GL(V) and σ: G → GL(W) are irreducible representations and T: V → W is a G-equivariant linear map (meaning Tρ(g) = σ(g)T for all g), then T is either the zero map or an isomorphism. **Part 2** (over an algebraically closed field like ℂ): If T: V → V is a G-equivariant endomorphism of an irreducible representation, then T = λI for some scalar λ.

The proof of Part 1 is elegant and short. The key observation is that ker(T) ⊆ V and im(T) ⊆ W are both G-invariant subspaces. For the kernel: if v ∈ ker(T), then T(ρ(g)v) = σ(g)(Tv) = σ(g)(0) = 0, so ρ(g)v ∈ ker(T). Similarly, the image is invariant. Since V is irreducible, ker(T) is either {0} or V; since W is irreducible, im(T) is either {0} or W. If T ≠ 0, the kernel must be {0} (T is injective) and the image must be W (T is surjective), so T is an isomorphism. There is no room for anything in between.

Part 2 uses algebraic closure. Over ℂ, the operator T: V → V has at least one eigenvalue λ. The map T − λI is still G-equivariant (since λI commutes with everything), and it has a nontrivial kernel (the λ-eigenspace). By Part 1, T − λI must be zero, so T = λI. Over ℝ, this argument fails because real operators need not have real eigenvalues — for instance, a 90° rotation has eigenvalues ±i.

The consequences are far-reaching. For abelian groups over ℂ, every ρ(g) commutes with the entire representation and is therefore scalar by Part 2. This forces all irreducible representations to be one-dimensional — a complete classification in one stroke. For non-abelian groups, Schur's lemma constrains the algebra of intertwining operators (the endomorphism ring of an irreducible is a division algebra), and this constraint underpins the orthogonality relations that make character theory work. Nearly every structural result in finite-group representation theory traces back to Schur's lemma.
