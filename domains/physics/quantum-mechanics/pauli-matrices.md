---
id: pauli-matrices
title: Pauli Matrices
domain: physics
course: quantum-mechanics
prerequisites:
- id: spin-half-systems
  type: hard
builds-toward:
- spin-orbit-coupling
tags:
- spin
- matrices
stage: advanced
status: draft
---

# Pauli Matrices

## Core Idea
The Pauli matrices σₓ, σᵧ, σz are 2×2 matrices representing spin-½ operators via Ŝᵢ = (ℏ/2)σᵢ. They satisfy σᵢσⱼ = δᵢⱼ + iεᵢⱼₖσₖ and form a basis for all 2×2 matrices, encoding the complete structure of spin-½.

## Questions

```yaml
- question: "You know that σz = [[1,0],[0,−1]] has eigenstates |↑⟩ and |↓⟩. What are the eigenstates of σₓ = [[0,1],[1,0]]?"
  type: multiple-choice
  options:
    - "|↑⟩ and |↓⟩ — the same eigenstates, since all Pauli matrices share eigenstates"
    - "(|↑⟩ ± |↓⟩)/√2 — equal real superpositions of spin-up and spin-down"
    - "(|↑⟩ ± i|↓⟩)/√2 — superpositions with a relative phase of ±i"
    - "Only |↑⟩ is an eigenstate of σₓ; |↓⟩ is not"
  answer: 1
  explanation: "Solving σₓ|ψ⟩ = ±|ψ⟩ with |ψ⟩ = (a, b)ᵀ gives b = ±a, so the normalized eigenstates are (|↑⟩ + |↓⟩)/√2 (eigenvalue +1) and (|↑⟩ − |↓⟩)/√2 (eigenvalue −1) — equal superpositions with real coefficients, corresponding to spin pointing in the ±x directions. Option C gives the eigenstates of σᵧ, not σₓ; the imaginary unit i in σᵧ is precisely what encodes the y direction. The Pauli matrices do not share eigenstates (they don't commute), reflecting that spin components along different axes are incompatible observables."

- question: "A student computes σₓσᵧ = iσz and σᵧσₓ = −iσz. What property of the Pauli matrices does this illustrate?"
  type: multiple-choice
  options:
    - "The Pauli matrices commute, since both products give ±iσz (the same magnitude)"
    - "The Pauli matrices anticommute: σₓσᵧ + σᵧσₓ = 0, and also do not commute"
    - "The Pauli matrices fail to close under multiplication and are not a group"
    - "Both products being nonzero means the Pauli matrices are not Hermitian"
  answer: 1
  explanation: "σₓσᵧ = iσz and σᵧσₓ = −iσz, so σₓσᵧ + σᵧσₓ = 0: the anticommutator {σₓ, σᵧ} = 0. Different Pauli matrices anticommute. Also, σₓσᵧ ≠ σᵧσₓ, so they do NOT commute: [σₓ, σᵧ] = 2iσz ≠ 0. The full identity σᵢσⱼ = δᵢⱼI + iεᵢⱼₖσₖ captures both rules simultaneously. The non-commutativity encodes the geometry of 3D rotations and is the algebraic basis for the uncertainty principle between spin components."

- question: "The three Pauli matrices commute with each other (σᵢσⱼ = σⱼσᵢ for i ≠ j)."
  type: true-false
  answer: false
  explanation: "The Pauli matrices anticommute for i ≠ j: {σᵢ, σⱼ} = σᵢσⱼ + σⱼσᵢ = 0, meaning σᵢσⱼ = −σⱼσᵢ. Equivalently, [σᵢ, σⱼ] = 2iεᵢⱼₖσₖ ≠ 0. Non-commutativity is physically significant: measuring spin along x then y is not the same as measuring y then x, and this gives rise to the Robertson-Heisenberg uncertainty relation ΔSₓΔSᵧ ≥ (ℏ/2)|⟨Sz⟩|."

- question: "Any 2×2 Hermitian matrix can be written as a real linear combination of the identity I and the three Pauli matrices {σₓ, σᵧ, σz}."
  type: true-false
  answer: true
  explanation: "The set {I, σₓ, σᵧ, σz} forms a basis for the four-dimensional real vector space of 2×2 Hermitian matrices. Any Hermitian M can be written as M = aI + bσz + cσₓ + dσᵧ with a, b, c, d real. This completeness means any spin-½ density matrix, Hamiltonian, or observable is fully characterized by its four components in this basis. The three Pauli components give the Bloch vector — the direction and magnitude of the spin polarization."

- question: "What physical role does the imaginary unit i play in σᵧ = [[0, −i],[i, 0]]? Why can it not simply be replaced by a real number?"
  type: short-answer
  answer: "The i in σᵧ encodes the phase relationship between z-eigenstates that corresponds to spin pointing along the y axis. The eigenstates of σᵧ are (|↑⟩ ± i|↓⟩)/√2 — the relative phase between up and down components is ±i (a 90° rotation in the complex plane). This phase is what geometrically distinguishes the y direction from x: the eigenstates of σₓ are real superpositions, while the eigenstates of σᵧ have imaginary relative phase. If σᵧ were replaced by a real matrix, it would be linearly dependent on σₓ and σz within the real numbers, and the three matrices would no longer span the space of traceless Hermitian matrices."
  explanation: "More formally: the commutation relations [σᵢ, σⱼ] = 2iεᵢⱼₖσₖ require the commutator to produce an imaginary coefficient times another Pauli matrix. A real σᵧ would violate this algebra. The i is the algebraic necessity that encodes the three-dimensional geometry of spin space — specifically, the fact that 3D rotations form a non-abelian group, which requires complex structure in the 2×2 matrix representation."
```

## Explainer

From your study of spin-½ systems, you know that the spin state lives in a two-dimensional complex vector space — the **spinor space** — with basis vectors |↑⟩ = (1, 0)ᵀ and |↓⟩ = (0, 1)ᵀ. Observable spin components are operators acting on this space, so they must be 2×2 matrices. The constraint that spin observables are Hermitian (real eigenvalues, so physically measurable) and traceless (the two eigenvalues ±ℏ/2 sum to zero) narrows down the candidates dramatically. The **Pauli matrices** are the three canonical Hermitian, traceless, 2×2 matrices: σₓ = [[0,1],[1,0]], σᵧ = [[0,−i],[i,0]], and σz = [[1,0],[0,−1]]. The spin operators are then Ŝᵢ = (ℏ/2)σᵢ, so σz has eigenvalues ±1 corresponding to spin-up and spin-down along z.

Each Pauli matrix captures the physics of spin measurement along its axis. The eigenstates of σz are |↑⟩ and |↓⟩ — states with definite spin along z. The eigenstates of σₓ are |±⟩ = (|↑⟩ ± |↓⟩)/√2 — equal superpositions of up and down, pointing along ±x. The eigenstates of σᵧ involve the imaginary unit i in the off-diagonal entries, which is why they pick out the y direction: |±ᵧ⟩ = (|↑⟩ ± i|↓⟩)/√2. The i in σᵧ is not arbitrary — it is what encodes the phase relationship between z-eigenstates for a spin pointing along y. Changing the sign of i rotates the spin direction in the xy-plane.

The **algebraic identity** σᵢσⱼ = δᵢⱼ I + iεᵢⱼₖσₖ is the heart of the structure. It combines two simpler rules: the anticommutator {σᵢ, σⱼ} = 2δᵢⱼ I (any Pauli matrix squares to the identity, and two different ones anticommute), and the commutator [σᵢ, σⱼ] = 2iεᵢⱼₖσₖ (the commutation relations of angular momentum, scaled by 2). The commutation relations encode the geometry of rotations in 3D space: the fact that rotating about x then y is not the same as rotating about y then x is precisely what [σₓ, σᵧ] ≠ 0 captures. Any calculation involving spin-½ reduces to applying this identity, which is why it is worth memorizing.

The Pauli matrices also span the **full space of 2×2 Hermitian matrices**: any such matrix can be written as aI + b·σ where a is real and b is a real 3-vector. This completeness means that knowing an arbitrary 2×2 density matrix or Hamiltonian is equivalent to knowing its four components in the {I, σₓ, σᵧ, σz} basis. The vector b points along the **Bloch vector** direction — the axis along which the spin is polarized. This geometric picture makes it possible to visualize any spin-½ state as a point on the Bloch sphere, and any Hamiltonian as a rotation on that sphere.
