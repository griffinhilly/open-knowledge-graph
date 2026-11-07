---
id: character-theory
title: Character Theory
domain: mathematics
course: representation-theory
prerequisites:
- id: schurs-lemma
  type: hard
- id: maschkes-theorem
  type: hard
- id: matrix-representations
  type: hard
- id: equivalence-of-representations
  type: hard
builds-toward:
- orthogonality-relations
- character-tables
- regular-representation
- induced-representations
- burnsides-theorem
tags:
- character
- trace
- class-function
stage: expert
status: validated
---

# Character Theory

## Core Idea
The character of a representation ρ: G → GL(V) is the function χ_ρ: G → F defined by χ_ρ(g) = tr(ρ(g)). Characters are class functions (constant on conjugacy classes), are independent of the choice of basis, and — remarkably — determine the representation up to equivalence over ℂ. Character theory reduces the study of representations to the study of these numerical functions, making computation tractable.

## How It's Best Learned
Start with S₃ acting on ℂ³ by permuting coordinates. The trace of a permutation matrix counts fixed points, so the character is (3, 1, 0) on the classes of e, transpositions and 3-cycles. Subtract the trivial character (1, 1, 1) to get (2, 0, −1), the character of the two-dimensional piece. Then compute the decomposition multiplicities with the inner product and confirm they match.

## Common Misconceptions
- A character is a homomorphism from G to the nonzero complex numbers. (That holds for one-dimensional representations only. For the two-dimensional representation of S₃, χ((12))² = 0 but χ(e) = 2.)
- Two representations with the same dimension have the same character. (The dimension is the single value χ(e). The trivial and sign representations of S₃ both have dimension 1 but differ on transpositions.)
- Characters determine representations over every field. (This uses characteristic zero. Over a field of characteristic p, V and V ⊕ (p copies of the trivial representation) have the same character.)

## Questions

```yaml
- question: "Why is the character χ(g) = tr(ρ(g)) constant on conjugacy classes of G?"
  type: short-answer
  answer: "For any h ∈ G, χ(hgh⁻¹) = tr(ρ(hgh⁻¹)) = tr(ρ(h)ρ(g)ρ(h)⁻¹) = tr(ρ(g)) = χ(g), using the cyclic property of trace: tr(ABA⁻¹) = tr(A⁻¹AB) = tr(B)."
  explanation: "The trace's invariance under conjugation is a linear algebra fact that becomes profoundly useful here. It means characters carry no more information than one value per conjugacy class, which drastically reduces the amount of data needed. For S₃ with 3 conjugacy classes, a character is determined by just 3 numbers rather than 6."

- question: "Two non-isomorphic irreducible representations over ℂ can have the same character."
  type: true-false
  answer: false
  explanation: "Over an algebraically closed field of characteristic zero, characters completely determine irreducible representations up to equivalence. If χ_ρ = χ_σ as functions on G, then ρ ≅ σ. This is a consequence of the orthogonality relations: distinct irreducible characters are orthogonal in the class function inner product, so they cannot be equal unless they correspond to the same representation."

- question: "If ρ is a representation of degree n, what is χ_ρ(e), where e is the identity element?"
  type: multiple-choice
  options:
    - "0"
    - "1"
    - "n"
    - "|G|"
  answer: 2
  explanation: "Since ρ(e) = Iₙ (the n×n identity matrix), we have χ_ρ(e) = tr(Iₙ) = n. So the character evaluated at the identity gives the dimension of the representation. This is a useful quick check and means the first column of any character table lists the dimensions of the irreducible representations."

- question: "If V ≅ W₁ ⊕ W₂ as representations, how is χ_V related to χ_{W₁} and χ_{W₂}?"
  type: multiple-choice
  options:
    - "χ_V = χ_{W₁} · χ_{W₂}"
    - "χ_V = χ_{W₁} + χ_{W₂}"
    - "χ_V = χ_{W₁} − χ_{W₂}"
    - "There is no general relationship"
  answer: 1
  explanation: "The trace of a block-diagonal matrix is the sum of the traces of the blocks. If V = W₁ ⊕ W₂ and we choose a basis adapted to this decomposition, then ρ(g) is block-diagonal, and tr(ρ(g)) = tr(ρ₁(g)) + tr(ρ₂(g)). So characters are additive under direct sums: χ_{V⊕W} = χ_V + χ_W. This additivity is what makes characters so useful for decomposition — the multiplicities in V ≅ ⊕ nᵢVᵢ can be extracted from χ_V using inner products."
```

## Explainer

Character theory is the computational engine of representation theory for finite groups. The **character** of a representation ρ: G → GL(V) is the function χ_ρ: G → ℂ defined by χ_ρ(g) = tr(ρ(g)) — the trace of the matrix (in any basis) representing g. The trace is basis-independent (since tr(PAP⁻¹) = tr(A)) and satisfies tr(AB) = tr(BA), which makes characters constant on conjugacy classes: χ(hgh⁻¹) = tr(ρ(h)ρ(g)ρ(h)⁻¹) = tr(ρ(g)) = χ(g).

The first key property is **additivity**: if V = W₁ ⊕ W₂, then χ_V = χ_{W₁} + χ_{W₂}. This follows from the trace of a block-diagonal matrix being the sum of the block traces. The second key property, far deeper, is **faithfulness**: over ℂ, two representations with the same character are equivalent. This means the character — a simple numerical function — captures all the information in the representation up to isomorphism.

To decompose a representation V into irreducibles V₁, …, Vₖ with multiplicities n₁, …, nₖ, we have χ_V = n₁χ₁ + ··· + nₖχₖ. The orthogonality relations (the next topic) provide an inner product on class functions under which the irreducible characters form an orthonormal basis. The multiplicity nᵢ is then simply the inner product ⟨χ_V, χᵢ⟩ — a finite computation involving a sum over the group. This transforms the algebraic problem of decomposing a representation into a numerical calculation.

The number of distinct irreducible characters equals the number of conjugacy classes of G. For S₃, there are 3 conjugacy classes and 3 irreducible characters. For the symmetric group Sₙ, the number of conjugacy classes equals the number of partitions of n, connecting representation theory to combinatorics. The character table — a square matrix whose rows are irreducible characters and whose columns are conjugacy classes — encodes the entire representation theory of a finite group in a compact, computable form.
