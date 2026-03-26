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
stage: expert
status: validated
---

# Mean Field Theory and Self-Consistency

## Core Idea
Mean-field theory replaces interactions between all neighboring spins with an average interaction from a self-consistent field. This drastically simplifies the calculation: each spin sees an effective field proportional to the average magnetization. The approach correctly predicts second-order transitions and provides analytic critical exponents, though it overestimates T_c and misses fluctuation effects.

## Questions

```yaml
- question: "In the mean-field self-consistency equation m = tanh(β(zJm + h)), why does m appear on both sides?"
  type: multiple-choice
  options:
    - "It is a mathematical error that results from approximating the partition function — correctly derived, m would only appear on the left"
    - "The magnetization m determines the effective field each spin sees, and that effective field determines the average magnetization m — the two must be mutually consistent"
    - "Both sides represent different spins: the left-side m is for the spin being considered, and the right-side m is for its neighbors"
    - "m appears on both sides because the external field h and the interaction zJm are equivalent quantities in the mean-field approximation"
  answer: 1
  explanation: "This is what 'self-consistent' means: the effective field that each spin experiences depends on the average magnetization of all spins (right side), and that average magnetization is itself determined by how spins respond to the effective field (left side). The equation is a fixed-point condition — the assumed magnetization must equal the magnetization it produces. The solution is found by finding values of m where input and output agree. This mutual dependence cannot be removed; it is the essence of the approximation."

- question: "Mean-field theory predicts a critical temperature T_c = zJ/k_B for the 2D Ising model. How does the actual critical temperature of the 2D Ising model compare?"
  type: multiple-choice
  options:
    - "The actual T_c is higher than the mean-field prediction, because fluctuations enhance ordering"
    - "The actual T_c equals the mean-field prediction exactly — mean-field theory is exact in 2D"
    - "The actual T_c is lower than the mean-field prediction, because fluctuations destabilize order and make it harder to maintain spontaneous magnetization"
    - "The concept of a critical temperature does not apply in 2D — the Ising model has no phase transition there"
  answer: 2
  explanation: "Mean-field theory overestimates T_c by roughly 30% in 2D because it ignores fluctuations. Near a phase transition, fluctuations are large and long-ranged; they compete with the tendency to order and make the system harder to magnetize. The actual 2D Ising critical temperature (Onsager's exact solution) is T_c = 2J/(k_B ln(1+√2)) ≈ 2.27 J/k_B, while mean-field predicts T_c = zJ/k_B = 4J/k_B for the square lattice (z=4). Mean-field is wrong in the direction of overestimating how easily order forms."

- question: "Mean-field theory fails to predict the existence of a phase transition in the Ising model — it gets the transition temperature wrong and misses the transition mostly."
  type: true-false
  answer: false
  explanation: "Mean-field theory does predict the phase transition correctly at a qualitative level — it predicts both the existence of the transition and that it is continuous (second-order), with the order parameter m growing continuously from zero below T_c. What it gets wrong is the critical temperature (overestimated) and the critical exponents (β = 1/2 instead of 1/8 in 2D). The qualitative story — paramagnet above T_c, ferromagnet below, continuous onset of spontaneous magnetization — is exactly right. This is why mean-field theory remains useful as a first approximation."

- question: "In mean-field theory, each spin in the Ising model experiences the actual fluctuating field from its neighbors, averaged over time."
  type: true-false
  answer: false
  explanation: "This is the key approximation of mean-field theory, and it is not the actual fluctuating field — it is a static average. Each spin is replaced by its mean value ⟨σ⟩ = m, so every spin sees the same smooth effective field h_eff = zJm, regardless of the actual local configuration of its neighbors. The real neighbors fluctuate — sometimes all pointing up, sometimes mixed — but mean-field theory treats them as if they always point in the average direction. This replacement eliminates correlations between spins and is exactly what makes fluctuation effects invisible to mean-field theory."

- question: "Why does mean-field theory become less accurate near the critical point T_c, and in what types of systems is it expected to be most reliable?"
  type: short-answer
  answer: "Near T_c, fluctuations become large and long-ranged — spins become correlated over large distances, and the local environment of each spin deviates significantly from the mean. Mean-field theory assumes each spin sees exactly the mean field of its neighbors, ignoring these correlated fluctuations. The approximation breaks down when fluctuations are the dominant physics. Mean-field theory is most reliable when fluctuations are suppressed: in high-dimensional systems (where each spin has many neighbors, so the law of large numbers makes the local environment close to the mean), and in systems above the upper critical dimension d_c = 4 for the Ising universality class."
  explanation: "The Ginzburg criterion formalizes when mean-field theory fails: fluctuation corrections to the free energy become comparable to the mean-field result when the system is close to T_c in low dimensions. In d ≥ 4, mean-field exponents are exact; in d = 3, they are approximately correct; in d = 2, they are substantially wrong. This is why renormalization group methods — which explicitly track how fluctuations modify the phase transition — are needed for accurate critical exponents in the physically relevant cases of 2D and 3D systems."
```

## Explainer

You already know the Ising model: spins on a lattice, each ±1, with nearest-neighbor interaction energy −J Σ_{⟨ij⟩} σᵢσⱼ minus any external field term. The exact partition function is a sum over 2^N configurations — intractable for large N in two or three dimensions. Mean-field theory cuts this knot with one bold approximation: replace the fluctuating neighbors of each spin with their average value.

Concretely, for spin i, replace the interaction with neighbor j by σᵢ(Jσⱼ) ≈ σᵢ(J⟨σ⟩) = σᵢ(Jm), where m = ⟨σ⟩ is the magnetization. Each spin now sees not the actual fluctuating neighbors, but a smooth **effective field** h_eff = zJm + h, where z is the number of neighbors and h is the external field. The many-body problem decouples into N independent single-spin problems — exactly solvable. Each spin's average value is m = tanh(βh_eff) = tanh(β(zJm + h)). This is the **self-consistency equation**: the magnetization m appears on both sides. Solving it determines the equilibrium state.

The self-consistency equation reveals the phase transition directly. Set h = 0 and ask when m = 0 is the only solution versus when nonzero solutions exist. Near m = 0, tanh(βzJm) ≈ βzJm − (βzJm)³/3 + …. A nonzero solution bifurcates when βzJ = 1, giving the **critical temperature** T_c = zJ/k_B. Above T_c, only m = 0 is stable (paramagnetic phase). Below T_c, two symmetric nonzero solutions ±m(T) appear, representing spontaneous magnetization. The order parameter grows as m ∝ (T_c − T)^{1/2} near T_c — the mean-field critical exponent β = 1/2. Similarly, the susceptibility diverges as χ ∝ |T − T_c|^{−1}, the correlation length exponent ν = 1/2. These are the Bragg-Williams mean-field exponents.

The fundamental failure of mean-field theory is that it ignores **fluctuations**. Near a critical point, fluctuations become large and long-ranged — this is precisely why critical phenomena are interesting. Mean-field theory treats each spin as seeing a uniform average, so it misses the correlated fluctuations that dominate near T_c. The **Ginzburg criterion** identifies when this approximation breaks down: mean-field is accurate when the dimension d > d_c (upper critical dimension, d_c = 4 for Ising). In d = 2, fluctuations are so strong that T_c is reduced from the mean-field value by roughly 30%, and the critical exponents are completely different (β = 1/8, not 1/2). Despite these failures, mean-field theory earns its place because it is analytically tractable, qualitatively correct about the *existence* and *type* of the transition, and the starting point for systematic corrections via renormalization group — the topic this builds toward through Landau theory.
