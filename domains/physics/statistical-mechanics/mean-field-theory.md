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
stage: expert
status: draft
---

# Mean Field Theory

## Core Idea
Mean field theory replaces the interaction of each spin with a mean field ⟨σ⟩, decoupling the many-body problem. Each spin obeys a single-site effective Hamiltonian. It predicts critical exponents matching Landau theory and provides exact results for infinite-dimensional systems, but overestimates order-parameter fluctuations and critical exponent values.

## Questions

```yaml
- question: "The central approximation in mean field theory for the Ising model is:"
  type: multiple-choice
  options:
    - "Ignoring the externally applied magnetic field h to simplify the Hamiltonian"
    - "Replacing the fluctuating influence of each spin's neighbors with the average magnetization ⟨σ⟩, converting the coupled many-body problem into independent single-site problems"
    - "Assuming spins only interact with next-nearest neighbors rather than nearest neighbors"
    - "Linearizing the partition function in the coupling constant J near T_c"
  answer: 1
  explanation: "Mean field theory's core move is decoupling: instead of each spin experiencing the actual, fluctuating spin values of its neighbors (which are correlated and unknown), each spin sees a fixed effective field equal to J times the average magnetization m = ⟨σ⟩. This turns N coupled equations into N identical single-site problems solvable exactly. The cost is that all information about fluctuations and correlations between neighbors is thrown away."

- question: "A student argues that mean field theory gives its most accurate predictions near the critical temperature T_c, because that is where the large number of correlated spins makes the 'average over neighbors' most reliable. What is wrong?"
  type: multiple-choice
  options:
    - "The student is correct; mean field theory is designed specifically for near-critical behavior"
    - "Near T_c, fluctuations are at their maximum and the correlation length diverges — correlations between neighboring spins are strongest precisely there, making the replacement of actual fluctuating neighbors by their average least valid"
    - "Mean field theory makes no predictions at or near T_c"
    - "The critical temperature is the one point where mean field theory gives exact results"
  answer: 1
  explanation: "This is the key failure mode. Mean field theory averages over neighbor fluctuations and works reasonably when those fluctuations are small and uncorrelated (far from T_c, deep in the ordered or disordered phase). But near T_c, the correlation length diverges — neighboring spins are strongly correlated over long distances, and the actual interaction a spin feels from its neighbors is far from the average. The averaging assumption is worst exactly where it is most needed, which is why mean field critical exponents are quantitatively wrong."

- question: "Mean field theory incorrectly predicts that a one-dimensional Ising chain undergoes a phase transition at finite temperature, even though the exact solution shows no such transition exists."
  type: true-false
  answer: true
  explanation: "This is one of mean field theory's most dramatic failures. The exact solution of the 1D Ising model (by transfer matrix) shows that thermal fluctuations are so powerful in one dimension that they destroy any ordered phase at any finite temperature — long-range order only exists at T = 0. Mean field theory predicts a finite T_c because it ignores fluctuations entirely, and its T_c = Jz/k scales with the coordination number z. In 1D, z = 2, giving a finite (wrong) prediction. The failure worsens as dimensionality decreases."

- question: "Mean field theory becomes exact in the limit of infinite spatial dimensions (or infinite-range interactions) because in that limit every spin truly interacts with an infinite number of others, making the central-limit-theorem-like averaging valid."
  type: true-false
  answer: true
  explanation: "In infinite dimensions, each spin has infinitely many neighbors, and by the law of large numbers, the fluctuating sum of neighbor influences converges to its mean — making the mean field approximation exact, not merely approximate. Infinite-range Ising models (where every spin interacts with every other) realize the same physics. This is why mean field theory is exact for the Curie-Weiss model and why it becomes increasingly accurate as dimensionality grows beyond the upper critical dimension (d = 4 for the Ising universality class)."

- question: "Why does mean field theory fail specifically near the critical point, even though it gives qualitatively correct phase diagrams far from it?"
  type: short-answer
  answer: "Because near the critical point, the correlation length diverges — fluctuations from the average extend across the entire system, and neighboring spins are strongly correlated rather than approximately independent. Mean field theory replaces each spin's actual, fluctuating neighbors with their average, which is only valid when neighbors truly fluctuate independently around that average (as they do far from T_c, deep in the ordered or disordered phase). At T_c, this assumption fails maximally: the thing being averaged over (neighbor fluctuations) is exactly what drives the critical behavior, and discarding it produces wrong critical exponents."
  explanation: "This is why the renormalization group is needed: it is a framework that keeps track of fluctuations at all length scales rather than averaging them away. Far from T_c, mean field is a useful first approximation; near T_c, it is qualitatively misleading about the universality class and the scaling behavior that experiments measure."
```

## Explainer

The central difficulty in the Ising model is that each spin interacts with its neighbors, whose states are themselves fluctuating and correlated with their own neighbors. The interactions couple all the spins together into a genuine many-body problem with no simple exact solution in most dimensions. **Mean field theory** cuts through this complexity with a bold approximation: replace the fluctuating influence of a spin's neighbors with their average value. Each spin then sees a fixed **effective field** proportional to the average magnetization ⟨σ⟩, decoupling the problem into N independent single-site problems.

Concretely, for an Ising spin σ_i with z nearest neighbors each carrying average magnetization m = ⟨σ⟩, the effective Hamiltonian for site i is H_eff = −(Jzm + h)σ_i, where J is the coupling constant and h is an external field. This is just a single spin in an effective magnetic field B_eff = Jzm + h. The self-consistent equation for m follows from computing ⟨σ⟩ in this effective field and requiring it to equal m: m = tanh(β(Jzm + h)). This **self-consistency equation** is the heart of mean field theory — it must be solved simultaneously for m, since m appears on both sides.

At high temperature, the only solution is m = 0 (paramagnetic phase). Below a critical temperature T_c = Jz/k, a nontrivial solution m ≠ 0 appears spontaneously — **spontaneous symmetry breaking** occurs. Near T_c, the order parameter grows as m ∝ (T_c − T)^{1/2}, giving a mean field critical exponent β = 1/2. This matches exactly the prediction of Landau theory, which is no coincidence: both approaches neglect fluctuations in the same way. The connection to Landau theory is direct — expanding the free energy in powers of m near T_c reproduces the Landau form with coefficients determined by the microscopic Ising parameters.

The fundamental weakness of mean field theory is its neglect of **fluctuations**. Near the critical point, correlations between spins extend over the entire system (the correlation length diverges), and the actual interaction with neighbors is wildly different from the average. In low-dimensional systems (d = 1, 2), fluctuations are so strong that they qualitatively change the physics — the 1D Ising model has no phase transition at finite temperature, despite mean field theory predicting one. Mean field theory becomes exact only when every spin interacts with infinitely many others (infinite dimensions, or infinite-range interactions), so that the central-limit-theorem-like averaging is valid. In physical 3D systems, it gives qualitatively correct phase diagrams but quantitatively wrong critical exponents — the true exponents are calculated via the renormalization group.
