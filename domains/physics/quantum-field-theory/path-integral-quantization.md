---
id: path-integral-quantization
title: Path Integral Quantization
domain: physics
course: quantum-field-theory
prerequisites:
- id: classical-field-theory-lagrangian-density
  type: hard
- id: path-integral-formulation
  type: hard
tags:
- path-integral
- functional-integral
- quantization
stage: expert
status: validated
---

# Path Integral Quantization

## Core Idea
Path integral quantization of fields computes quantum amplitudes by summing over all possible field configurations, weighted by e^{iS[phi]}, where S is the classical action. It provides an alternative to canonical quantization that is manifestly Lorentz covariant, naturally handles gauge theories, and is the foundation for non-perturbative methods like lattice QFT.

## Questions

```yaml
- question: "In the path integral for a scalar field, the partition function is Z = integral D[phi] e^{iS[phi]}, where D[phi] denotes integration over all field configurations. What does 'all field configurations' mean concretely?"
  type: multiple-choice
  options:
    - "Integration over all possible values of phi at every spacetime point — an infinite-dimensional integral, one ordinary integral for each point in spacetime"
    - "A sum over all possible particle trajectories"
    - "Integration over the Fourier coefficients of the field"
    - "Both A and C are correct descriptions — they are related by a change of variables from position space to momentum space, and both represent the same infinite-dimensional integral"
  answer: 3
  explanation: "The functional integral D[phi] is an integral over all functions phi(x). This can be thought of as an independent integral over the value of phi at each spacetime point (continuum formulation) or equivalently as an integral over all Fourier modes of the field (momentum space formulation). On a lattice, it becomes a finite (but very high) dimensional integral — one variable per lattice site. The two descriptions are related by a unitary change of basis and give the same physics."

- question: "In the path integral, the classical solution (the field configuration that extremizes S) dominates when S >> hbar. The quantum corrections come from fluctuations around the classical solution."
  type: true-false
  answer: true
  explanation: "When S is large compared to hbar (the classical limit), the phase e^{iS/hbar} oscillates rapidly for configurations far from the classical solution, and their contributions cancel. Only configurations near the stationary point (where delta S = 0, the classical equation of motion) contribute coherently. This is the stationary-phase approximation. Expanding S to second order around the classical solution gives the one-loop correction (a Gaussian integral over fluctuations). Higher orders in the expansion give higher-loop corrections. The path integral therefore naturally organizes the perturbative expansion: tree level = classical, one loop = leading quantum correction, etc."

- question: "The path integral for gauge theories requires a gauge-fixing procedure (Faddeev-Popov). Without gauge fixing, the path integral gives an infinite answer."
  type: true-false
  answer: true
  explanation: "In a gauge theory, distinct field configurations related by gauge transformations describe the same physics. The naive path integral integrates over all configurations, including the infinite volume of gauge-equivalent copies (the gauge orbit). This overcounting gives infinity. The Faddeev-Popov procedure inserts a gauge-fixing condition (like Lorenz gauge) and a corresponding determinant (which can be expressed using ghost fields) to integrate over each physical configuration exactly once. The resulting gauge-fixed path integral gives finite, well-defined answers."

- question: "Explain the advantages of path integral quantization over canonical quantization for gauge theories, and identify one situation where canonical quantization is more natural."
  type: short-answer
  answer: "Path integral advantages: (1) Manifest Lorentz covariance — there is no need to single out a time direction, unlike canonical quantization where equal-time commutation relations break manifest covariance. (2) Gauge theories are handled systematically via the Faddeev-Popov procedure, which is most naturally formulated in the path integral. (3) Non-perturbative effects like instantons (field configurations that tunnel between different vacuum sectors) are naturally included as saddle points of the Euclidean path integral. (4) Lattice field theory directly discretizes the path integral for numerical computation. Canonical quantization is more natural for: understanding the Hilbert space structure, the particle interpretation of the theory, and for systems where Hamiltonian methods are needed (e.g., bound state problems, real-time evolution)."
  explanation: "In practice, most modern QFT calculations use the path integral for deriving Feynman rules and computing scattering amplitudes, while canonical quantization provides the conceptual framework (Fock space, particle states, S-matrix). The two approaches are equivalent but have complementary strengths."
```

## Explainer

Canonical quantization (promoting fields and their conjugate momenta to operators with commutation relations) works well for free fields and for QED, but becomes increasingly cumbersome for gauge theories. **Path integral quantization** provides an alternative approach that is manifestly Lorentz covariant and handles gauge invariance more naturally. The central object is the generating functional Z[J] = integral D[phi] e^{i(S[phi] + integral J phi d^4x)}, where D[phi] denotes integration over all field configurations, S[phi] is the classical action, and J(x) is an external source.

The physical content is simple: the amplitude for any quantum process is obtained by summing over all possible ways it could happen, with each possibility weighted by e^{iS}. The classical path (which extremizes S) dominates in the classical limit; quantum corrections come from nearby paths whose actions differ from the classical action by order hbar. Expanding the action to second order around the classical solution gives a Gaussian integral, which is the one-loop approximation. Higher terms give higher-loop corrections. The path integral thus provides a natural and systematic organization of perturbation theory.

For **gauge theories**, the path integral requires care. The naive integral over all gauge field configurations overcounts because gauge-equivalent configurations represent the same physics. The **Faddeev-Popov procedure** fixes this: it restricts the integral to one representative from each gauge orbit by inserting a gauge-fixing condition and a compensating functional determinant (which can be written as an integral over ghost fields). The resulting gauge-fixed path integral is well-defined and generates the correct Feynman rules, including ghost propagators and vertices.

The path integral also provides access to **non-perturbative physics** that is invisible to canonical perturbation theory. In the Euclidean (imaginary time) formulation, the path integral becomes Z = integral D[phi] e^{-S_E[phi]}, which resembles a statistical mechanics partition function. This connection enables lattice field theory (evaluating the path integral numerically on a discrete spacetime grid), the study of instantons (finite-action solutions of the Euclidean equations of motion that describe tunneling between topologically distinct vacua), and the identification of non-perturbative vacuum structure. The Euclidean path integral is the basis for essentially all non-perturbative calculations in QCD.
