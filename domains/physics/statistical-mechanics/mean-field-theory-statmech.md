---
id: mean-field-theory-statmech
title: Mean Field Theory and Self-Consistency
domain: physics
course: statistical-mechanics
prerequisites:
- id: ising-model-statmech
  type: hard
- id: order-parameter-phase-transition
  type: soft
builds-toward:
- landau-theory-phase-transitions
- spontaneous-symmetry-breaking
tags:
- mean-field-theory
- self-consistency
- bragg-williams
stage: advanced
status: draft
---

# Mean Field Theory and Self-Consistency

## Core Idea
Mean-field theory replaces interactions between all neighboring spins with an average interaction from a self-consistent field. This drastically simplifies the calculation: each spin sees an effective field proportional to the average magnetization. The approach correctly predicts second-order transitions and provides analytic critical exponents, though it overestimates T_c and misses fluctuation effects.

## Explainer

You already know the Ising model: spins on a lattice, each ±1, with nearest-neighbor interaction energy −J Σ_{⟨ij⟩} σᵢσⱼ minus any external field term. The exact partition function is a sum over 2^N configurations — intractable for large N in two or three dimensions. Mean-field theory cuts this knot with one bold approximation: replace the fluctuating neighbors of each spin with their average value.

Concretely, for spin i, replace the interaction with neighbor j by σᵢ(Jσⱼ) ≈ σᵢ(J⟨σ⟩) = σᵢ(Jm), where m = ⟨σ⟩ is the magnetization. Each spin now sees not the actual fluctuating neighbors, but a smooth **effective field** h_eff = zJm + h, where z is the number of neighbors and h is the external field. The many-body problem decouples into N independent single-spin problems — exactly solvable. Each spin's average value is m = tanh(βh_eff) = tanh(β(zJm + h)). This is the **self-consistency equation**: the magnetization m appears on both sides. Solving it determines the equilibrium state.

The self-consistency equation reveals the phase transition directly. Set h = 0 and ask when m = 0 is the only solution versus when nonzero solutions exist. Near m = 0, tanh(βzJm) ≈ βzJm − (βzJm)³/3 + …. A nonzero solution bifurcates when βzJ = 1, giving the **critical temperature** T_c = zJ/k_B. Above T_c, only m = 0 is stable (paramagnetic phase). Below T_c, two symmetric nonzero solutions ±m(T) appear, representing spontaneous magnetization. The order parameter grows as m ∝ (T_c − T)^{1/2} near T_c — the mean-field critical exponent β = 1/2. Similarly, the susceptibility diverges as χ ∝ |T − T_c|^{−1}, the correlation length exponent ν = 1/2. These are the Bragg-Williams mean-field exponents.

The fundamental failure of mean-field theory is that it ignores **fluctuations**. Near a critical point, fluctuations become large and long-ranged — this is precisely why critical phenomena are interesting. Mean-field theory treats each spin as seeing a uniform average, so it misses the correlated fluctuations that dominate near T_c. The **Ginzburg criterion** identifies when this approximation breaks down: mean-field is accurate when the dimension d > d_c (upper critical dimension, d_c = 4 for Ising). In d = 2, fluctuations are so strong that T_c is reduced from the mean-field value by roughly 30%, and the critical exponents are completely different (β = 1/8, not 1/2). Despite these failures, mean-field theory earns its place because it is analytically tractable, qualitatively correct about the *existence* and *type* of the transition, and the starting point for systematic corrections via renormalization group — the topic this builds toward through Landau theory.
