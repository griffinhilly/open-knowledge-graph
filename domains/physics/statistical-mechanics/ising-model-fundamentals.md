---
id: ising-model-fundamentals
title: Ising Model Fundamentals
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
builds-toward:
- mean-field-theory
- monte-carlo-methods-stat-mech
tags:
- model-system
- phase-transitions
- spin-systems
stage: advanced
status: draft
---

# Ising Model Fundamentals

## Core Idea
The Ising model describes N spins {σ_i = ±1} on a lattice with energy H = −J Σ σ_i σ_j − h Σ σ_i, where J is coupling strength and h is external field. Despite apparent simplicity, it exhibits a ferromagnetic phase transition in 2D and higher. It is the paradigm model for studying phase transitions and critical phenomena.

## Explainer

You have mastered the canonical ensemble: given a Hamiltonian, compute the partition function Z = Σ exp(−βH), extract the free energy F = −kT ln Z, and derive all thermodynamic quantities by differentiation. The Ising model is the simplest Hamiltonian that exhibits a genuine phase transition, and it applies this machinery to a lattice of interacting binary variables.

Each site i on the lattice holds a **spin** σ_i that can take only two values: +1 (up) or −1 (down). The Hamiltonian is H = −J Σ_{⟨ij⟩} σ_i σ_j − h Σ_i σ_i, where the first sum runs over **nearest-neighbor pairs** ⟨ij⟩. The coupling constant J governs whether alignment is favored: when J > 0, neighboring spins prefer to point the same way (**ferromagnetic**), because the product σ_i σ_j = +1 when aligned, contributing −J to the energy. When J < 0, antiparallel neighbors are preferred (**antiferromagnetic**). The external field h biases all spins toward +1 (if h > 0). At high temperature, entropy wins and spins point randomly; at low temperature, energy wins and spins align spontaneously, giving nonzero average magnetization ⟨m⟩ = (1/N) Σ ⟨σ_i⟩ even when h = 0.

The phase structure depends critically on dimension. In **one dimension**, the 1D Ising model is exactly solvable, and the solution shows no phase transition at any T > 0: thermal fluctuations always disorder the chain. In **two dimensions**, Onsager's 1944 exact solution demonstrates a second-order ferromagnetic phase transition at a critical temperature T_c = 2J / (k ln(1 + √2)) ≈ 2.269 J/k. This was a landmark result, proving that phase transitions can arise from purely local interactions with no long-range forces. In **three dimensions**, no exact solution is known, but numerical methods and the renormalization group give precise values. The importance of the Ising model is that it is the **prototype for universality**: its critical exponents define the "Ising universality class" shared by a huge variety of real systems — liquid-gas, binary alloys, polymer mixtures — that have the same symmetry (a scalar order parameter with Z₂ up/down symmetry) in the same dimension.

The simplest analytic approach is **mean-field theory**: replace the interaction of each spin with its neighbors by an effective field proportional to the average magnetization m. This leads to the self-consistency equation m = tanh(β(Jzm + h)), where z is the coordination number (number of nearest neighbors). This equation has a nonzero solution for m when the temperature drops below T_c^{MF} = Jz/k. Mean-field theory predicts the qualitative behavior correctly — there is a phase transition — but gives wrong critical exponents in low dimensions because it ignores fluctuations. The discrepancy between mean-field predictions and the Onsager exact solution is what ultimately motivated the development of the renormalization group.
