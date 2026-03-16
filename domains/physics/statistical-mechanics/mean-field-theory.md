---
id: mean-field-theory
title: Mean Field Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: landau-theory
  type: hard
- id: ising-model-fundamentals
  type: hard
builds-toward:
- renormalization-group-intro
tags:
- approximation
- phase-transitions
- critical-behavior
stage: advanced
status: draft
---

# Mean Field Theory

## Core Idea
Mean field theory replaces the interaction of each spin with a mean field ⟨σ⟩, decoupling the many-body problem. Each spin obeys a single-site effective Hamiltonian. It predicts critical exponents matching Landau theory and provides exact results for infinite-dimensional systems, but overestimates order-parameter fluctuations and critical exponent values.

## Explainer

The central difficulty in the Ising model is that each spin interacts with its neighbors, whose states are themselves fluctuating and correlated with their own neighbors. The interactions couple all the spins together into a genuine many-body problem with no simple exact solution in most dimensions. **Mean field theory** cuts through this complexity with a bold approximation: replace the fluctuating influence of a spin's neighbors with their average value. Each spin then sees a fixed **effective field** proportional to the average magnetization ⟨σ⟩, decoupling the problem into N independent single-site problems.

Concretely, for an Ising spin σ_i with z nearest neighbors each carrying average magnetization m = ⟨σ⟩, the effective Hamiltonian for site i is H_eff = −(Jzm + h)σ_i, where J is the coupling constant and h is an external field. This is just a single spin in an effective magnetic field B_eff = Jzm + h. The self-consistent equation for m follows from computing ⟨σ⟩ in this effective field and requiring it to equal m: m = tanh(β(Jzm + h)). This **self-consistency equation** is the heart of mean field theory — it must be solved simultaneously for m, since m appears on both sides.

At high temperature, the only solution is m = 0 (paramagnetic phase). Below a critical temperature T_c = Jz/k, a nontrivial solution m ≠ 0 appears spontaneously — **spontaneous symmetry breaking** occurs. Near T_c, the order parameter grows as m ∝ (T_c − T)^{1/2}, giving a mean field critical exponent β = 1/2. This matches exactly the prediction of Landau theory, which is no coincidence: both approaches neglect fluctuations in the same way. The connection to Landau theory is direct — expanding the free energy in powers of m near T_c reproduces the Landau form with coefficients determined by the microscopic Ising parameters.

The fundamental weakness of mean field theory is its neglect of **fluctuations**. Near the critical point, correlations between spins extend over the entire system (the correlation length diverges), and the actual interaction with neighbors is wildly different from the average. In low-dimensional systems (d = 1, 2), fluctuations are so strong that they qualitatively change the physics — the 1D Ising model has no phase transition at finite temperature, despite mean field theory predicting one. Mean field theory becomes exact only when every spin interacts with infinitely many others (infinite dimensions, or infinite-range interactions), so that the central-limit-theorem-like averaging is valid. In physical 3D systems, it gives qualitatively correct phase diagrams but quantitatively wrong critical exponents — the true exponents are calculated via the renormalization group.
