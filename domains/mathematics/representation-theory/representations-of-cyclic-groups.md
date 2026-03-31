---
id: representations-of-cyclic-groups
title: Representations of Cyclic Groups
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: reducibility-and-irreducibility
  type: hard
- id: cyclic-groups
  type: soft
builds-toward:
- representations-of-abelian-groups
- character-tables
tags:
- cyclic-group
- roots-of-unity
- one-dimensional
- classification
stage: expert
status: validated
---

# Representations of Cyclic Groups

## Core Idea
Every irreducible complex representation of a cyclic group ℤ/nℤ is one-dimensional, given by sending a generator g to an nth root of unity ζ = e^{2πik/n} for k = 0, 1, …, n−1. This gives exactly n irreducible representations, matching the n conjugacy classes (each element is its own conjugacy class since the group is abelian). The character table is the DFT matrix (1/√n)(ζʲᵏ), and the representation theory of cyclic groups is equivalent to the discrete Fourier transform — a fact that connects algebra to signal processing.

## Questions

```yaml
- question: "How many non-isomorphic irreducible complex representations does ℤ/6ℤ have, and what are their dimensions?"
  type: short-answer
  answer: "Exactly 6 irreducible representations, all of dimension 1."
  explanation: "A cyclic group of order n has n conjugacy classes (each element is its own class, since the group is abelian). The number of irreducible representations equals the number of conjugacy classes, so there are n = 6 irreducibles. Since the group is abelian, Schur's lemma forces all irreducibles to be 1-dimensional. The sum-of-squares check confirms: 1² × 6 = 6 = |G|."

- question: "The representation ρ_k: ℤ/nℤ → GL₁(ℂ) defined by ρ_k(g) = e^{2πik/n} for a generator g is irreducible for all k = 0, …, n−1."
  type: true-false
  answer: true
  explanation: "Each ρ_k is a group homomorphism from ℤ/nℤ to ℂ* (since (e^{2πik/n})ⁿ = 1). These are 1-dimensional, hence automatically irreducible (no proper nonzero subspaces exist). They are pairwise non-isomorphic because ρ_k(g) ≠ ρ_ℓ(g) when k ≠ ℓ (mod n). Since there are exactly n of them and n = |G| = Σ dᵢ² requires n summands of 1², this is the complete list."

- question: "What is the character table of ℤ/3ℤ?"
  type: multiple-choice
  options:
    - "A 3×3 identity matrix"
    - "A 3×3 matrix with all entries equal to 1"
    - "The 3×3 DFT matrix with entries ω^{jk} where ω = e^{2πi/3}"
    - "A 3×3 matrix with entries ±1"
  answer: 2
  explanation: "The character table has rows indexed by irreducible representations ρ₀, ρ₁, ρ₂ and columns by group elements e, g, g². The entry χ_k(gʲ) = ω^{jk} where ω = e^{2πi/3}. This gives the matrix [[1,1,1],[1,ω,ω²],[1,ω²,ω]], which is precisely the 3×3 discrete Fourier transform matrix. The orthogonality relations for characters correspond to the unitarity of the DFT matrix (after scaling by 1/√3)."

- question: "Over ℝ (rather than ℂ), the cyclic group ℤ/4ℤ has an irreducible representation of dimension 2."
  type: true-false
  answer: true
  explanation: "Over ℂ, the four irreducibles of ℤ/4ℤ send the generator to 1, i, −1, −i. Over ℝ, the representations sending g to 1 and −1 remain irreducible (they are real). But the representations sending g to i and −i cannot be realized in dimension 1 over ℝ. They combine into a single 2-dimensional real irreducible representation where g acts as the rotation matrix [[0,−1],[1,0]]. This is the real 90° rotation representation."
```

## Explainer

The cyclic group ℤ/nℤ = ⟨g | gⁿ = e⟩ has the simplest representation theory of any group family. Since the group is abelian, Schur's lemma implies that every irreducible complex representation is one-dimensional. A 1-dimensional representation is just a group homomorphism ρ: ℤ/nℤ → ℂ*, which is determined by ρ(g) since g generates the group. The constraint ρ(g)ⁿ = ρ(gⁿ) = ρ(e) = 1 means ρ(g) must be an nth root of unity. There are exactly n choices: ρ_k(g) = e^{2πik/n} for k = 0, 1, …, n−1. These n representations are pairwise non-isomorphic and exhaust all irreducibles.

The **character table** of ℤ/nℤ is the n×n matrix with entry (j,k) equal to ω^{jk}, where ω = e^{2πi/n}. This is exactly the **discrete Fourier transform (DFT) matrix**. The orthogonality relations for characters — Σ_{g∈G} χᵢ(g)·conjugate(χⱼ(g)) = |G|·δᵢⱼ — become the statement that the DFT matrix (scaled by 1/√n) is unitary. This is not a coincidence: the DFT decomposes functions on ℤ/nℤ into irreducible components, and the Fourier inversion formula is the character orthogonality relation. Representation theory of cyclic groups **is** Fourier analysis on finite cyclic groups.

Over the **real numbers**, the picture changes. The representations ρ_k and ρ_{n−k} are complex conjugates, and when k ≠ 0, n/2, they cannot be individually realized over ℝ. Instead, they combine into a 2-dimensional real irreducible representation where g acts as the rotation matrix [[cos(2πk/n), −sin(2πk/n)], [sin(2πk/n), cos(2πk/n)]]. So the real irreducible representations of ℤ/nℤ consist of some 1-dimensional ones (corresponding to real roots of unity: ±1 when they exist) and some 2-dimensional ones (corresponding to conjugate pairs of complex roots).

The group algebra ℂ[ℤ/nℤ] ≅ ℂ[x]/(xⁿ − 1) ≅ ℂ ⊕ ℂ ⊕ ··· ⊕ ℂ (n copies), where the isomorphism uses the Chinese Remainder Theorem and the factorization xⁿ − 1 = ∏(x − ω^k). Each factor ℂ corresponds to one irreducible representation. This is the simplest instance of the Artin-Wedderburn decomposition. For cyclic groups, the representation ring R(ℤ/nℤ) ≅ ℤ[x]/(xⁿ − 1), with the tensor product of representations corresponding to multiplication of characters (pointwise product of roots of unity).
