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
stage: abstract-reasoning
status: draft
---

# Pauli Matrices

## Core Idea
The Pauli matrices σₓ, σᵧ, σz are 2×2 matrices representing spin-½ operators via Ŝᵢ = (ℏ/2)σᵢ. They satisfy σᵢσⱼ = δᵢⱼ + iεᵢⱼₖσₖ and form a basis for all 2×2 matrices, encoding the complete structure of spin-½.

## Explainer

From your study of spin-½ systems, you know that the spin state lives in a two-dimensional complex vector space — the **spinor space** — with basis vectors |↑⟩ = (1, 0)ᵀ and |↓⟩ = (0, 1)ᵀ. Observable spin components are operators acting on this space, so they must be 2×2 matrices. The constraint that spin observables are Hermitian (real eigenvalues, so physically measurable) and traceless (the two eigenvalues ±ℏ/2 sum to zero) narrows down the candidates dramatically. The **Pauli matrices** are the three canonical Hermitian, traceless, 2×2 matrices: σₓ = [[0,1],[1,0]], σᵧ = [[0,−i],[i,0]], and σz = [[1,0],[0,−1]]. The spin operators are then Ŝᵢ = (ℏ/2)σᵢ, so σz has eigenvalues ±1 corresponding to spin-up and spin-down along z.

Each Pauli matrix captures the physics of spin measurement along its axis. The eigenstates of σz are |↑⟩ and |↓⟩ — states with definite spin along z. The eigenstates of σₓ are |±⟩ = (|↑⟩ ± |↓⟩)/√2 — equal superpositions of up and down, pointing along ±x. The eigenstates of σᵧ involve the imaginary unit i in the off-diagonal entries, which is why they pick out the y direction: |±ᵧ⟩ = (|↑⟩ ± i|↓⟩)/√2. The i in σᵧ is not arbitrary — it is what encodes the phase relationship between z-eigenstates for a spin pointing along y. Changing the sign of i rotates the spin direction in the xy-plane.

The **algebraic identity** σᵢσⱼ = δᵢⱼ I + iεᵢⱼₖσₖ is the heart of the structure. It combines two simpler rules: the anticommutator {σᵢ, σⱼ} = 2δᵢⱼ I (any Pauli matrix squares to the identity, and two different ones anticommute), and the commutator [σᵢ, σⱼ] = 2iεᵢⱼₖσₖ (the commutation relations of angular momentum, scaled by 2). The commutation relations encode the geometry of rotations in 3D space: the fact that rotating about x then y is not the same as rotating about y then x is precisely what [σₓ, σᵧ] ≠ 0 captures. Any calculation involving spin-½ reduces to applying this identity, which is why it is worth memorizing.

The Pauli matrices also span the **full space of 2×2 Hermitian matrices**: any such matrix can be written as aI + b·σ where a is real and b is a real 3-vector. This completeness means that knowing an arbitrary 2×2 density matrix or Hamiltonian is equivalent to knowing its four components in the {I, σₓ, σᵧ, σz} basis. The vector b points along the **Bloch vector** direction — the axis along which the spin is polarized. This geometric picture makes it possible to visualize any spin-½ state as a point on the Bloch sphere, and any Hamiltonian as a rotation on that sphere.
