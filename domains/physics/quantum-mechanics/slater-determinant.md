---
id: slater-determinant
title: Slater Determinants
domain: physics
course: quantum-mechanics
prerequisites:
- id: fermions-and-bosons
  type: hard
tags:
- identical-particles
- antisymmetry
stage: abstract-reasoning
status: draft
---

# Slater Determinants

## Core Idea
A Slater determinant is an antisymmetric N-electron wavefunction written as a determinant of single-particle orbitals. It automatically enforces the Pauli principle and forms the basis of Hartree-Fock theory.

## Explainer

You know from studying fermions that any valid multi-electron wavefunction must be antisymmetric: swapping two electrons must change the sign of the total wavefunction. For a single electron, you have a single-particle orbital ψ(r, σ) — a spatial wavefunction times a spin state. The challenge is: given N electrons occupying N single-particle orbitals φ₁, φ₂, ..., φ_N, how do you build an N-particle wavefunction that is automatically antisymmetric under any exchange? The **Slater determinant** is the answer.

Write the N orbitals as rows and the N electrons as columns in an N×N matrix, then take the determinant. In formal notation: Ψ(1, 2, ..., N) = (1/√N!) det[φᵢ(j)]. The factor 1/√N! normalizes the result. The determinant structure automatically handles antisymmetry because swapping two electrons (swapping two columns of the matrix) changes the sign of a determinant — exactly the property required for fermions. Moreover, if two electrons occupy the same orbital (two identical rows in the matrix), the determinant is zero: the state doesn't exist. This is the Pauli exclusion principle emerging as a mathematical identity, not an additional assumption.

A simple example makes this concrete. For two electrons in orbitals φ_a and φ_b:
Ψ(1,2) = (1/√2)[φ_a(1)φ_b(2) − φ_a(2)φ_b(1)]. The first term has electron 1 in φ_a and electron 2 in φ_b; the second term has them swapped, with a minus sign. This is the antisymmetric combination you construct by hand for two electrons — the Slater determinant generalizes this to any N automatically.

The Slater determinant is the foundational ansatz of **Hartree-Fock theory**: the best possible approximation to the true many-electron wavefunction that keeps electrons in independent orbitals. It captures exchange effects (the Pauli principle) exactly, but misses **correlation** — the fact that electrons avoid each other beyond what the Pauli principle requires. The difference in energy between Hartree-Fock and the exact ground-state energy is called the correlation energy, and computing it accurately is the central challenge of modern quantum chemistry and density functional theory. All of that advanced machinery starts from the Slater determinant as its reference point.
