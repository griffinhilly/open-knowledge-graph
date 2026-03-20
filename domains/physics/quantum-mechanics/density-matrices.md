---
id: density-matrices
title: Density Matrices and the Density Operator
domain: physics
course: quantum-mechanics
prerequisites:
- id: kets-and-bras
  type: hard
- id: observables-and-operators
  type: hard
builds-toward:
- pure-and-mixed-states
tags:
- density-matrices
- mixed-states
stage: formal-systems
status: draft
---

# Density Matrices and the Density Operator

## Core Idea
Density matrix ρ = |ψ⟩⟨ψ| (pure) or ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ| (mixed) encodes complete state information. Expectation values: ⟨Â⟩ = Tr(ρÂ).

## Explainer

From your work with kets and observables, you know how to compute expectation values for a system in a definite quantum state |ψ⟩. But what if you don't know the exact state? This happens routinely: a beam of atoms might be 40% spin-up and 60% spin-down without any quantum superposition — just classical ignorance about which state each atom is in. The **density operator** (or **density matrix** ρ) is the tool that handles both cases within a single formalism.

For a system you know to be in state |ψ⟩, the density operator is the **pure state** form ρ = |ψ⟩⟨ψ|. This is an outer product — a matrix, not a number. Its diagonal entries in any basis give the probabilities of measuring the corresponding eigenvalues. Its off-diagonal entries encode **coherences**: quantum interferences between different states. A pure state always satisfies ρ² = ρ and Tr(ρ²) = 1. You can verify this: (|ψ⟩⟨ψ|)² = |ψ⟩⟨ψ|ψ⟩⟨ψ| = |ψ⟩⟨ψ| since ⟨ψ|ψ⟩ = 1.

For a system that is in state |ψᵢ⟩ with classical probability pᵢ, the **mixed state** density operator is ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ|, where Σᵢ pᵢ = 1. For mixed states, ρ² ≠ ρ and Tr(ρ²) < 1 — a useful diagnostic. The probabilities pᵢ are classical (a coin flip about which state the system is in), not quantum amplitudes. This is the critical distinction: a superposition of |↑⟩ and |↓⟩ has off-diagonal coherences in ρ, while a 50/50 mixture of |↑⟩ and |↓⟩ has ρ proportional to the identity matrix with no coherences.

The power of the density operator is the universal expectation value formula: ⟨Â⟩ = Tr(ρÂ). The **trace** sums the diagonal elements of the matrix product ρÂ, giving a basis-independent scalar. This single formula handles pure states, mixed states, and degenerate cases uniformly — you never need to track individual quantum states separately. Density matrices become indispensable when studying open quantum systems, quantum entanglement (where subsystems have mixed states even if the whole is pure), and quantum statistical mechanics where thermal states are represented by ρ ∝ e^(−βH).
