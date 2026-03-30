---
id: adm-formalism
title: ADM Formalism (Introduction)
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: hamiltonian-mechanics-intro
  type: hard
tags:
- adm-formalism
- initial-value-problem
- 3+1-decomposition
- hamiltonian-gravity
- lapse-shift
- numerical-relativity
stage: expert
status: validated
---

# ADM Formalism (Introduction)

## Core Idea
The ADM (Arnowitt-Deser-Misner) formalism recasts general relativity as an initial-value (Cauchy) problem by decomposing four-dimensional spacetime into a foliation of three-dimensional spatial hypersurfaces evolving in time. The spacetime metric is decomposed into the spatial 3-metric γ_ij (geometry of each slice), the lapse function N (rate of proper time flow between slices), and the shift vector N^i (how spatial coordinates slide between slices). The Einstein equations split into constraint equations (Hamiltonian and momentum constraints, which the initial data must satisfy) and evolution equations (which propagate the data forward). The canonical variables are (γ_ij, π^{ij}), where π^{ij} is the conjugate momentum related to the extrinsic curvature K_ij. The ADM formalism is the foundation of numerical relativity (computational solution of Einstein's equations) and the starting point for canonical quantization of gravity.

## Questions

```yaml
- question: "In the ADM formalism, the lapse function N and shift vector N^i are:"
  type: multiple-choice
  options:
    - "Dynamical degrees of freedom that propagate as gravitational waves"
    - "Gauge variables that specify how the coordinate system evolves from one spatial slice to the next, with no dynamical content"
    - "Components of the stress-energy tensor"
    - "Determined by the spatial metric γ_ij through the constraint equations"
  answer: 1
  explanation: "The lapse N specifies how much proper time elapses between adjacent spatial hypersurfaces at each point, and the shift N^i specifies how spatial coordinates shift laterally between slices. They encode the four coordinate degrees of freedom (gauge freedom) of GR and can be freely chosen — different choices correspond to different coordinate systems (slicing conditions). They have no dynamical content: they do not appear with time derivatives in the action, and their equations of motion are the constraint equations (which constrain the initial data, not the evolution). The physical degrees of freedom reside entirely in the spatial metric γ_ij and its conjugate momentum π^{ij}."

- question: "The ADM constraint equations must be satisfied only on the initial time slice — they are automatically preserved by the evolution equations."
  type: true-false
  answer: true
  explanation: "The Hamiltonian constraint H = 0 and momentum constraints H_i = 0 are conditions on the initial data (γ_ij, π^{ij}) on a single spatial slice. The evolution equations (derived from the remaining Einstein equations) propagate the data forward in time, and the Bianchi identities guarantee that if the constraints are satisfied initially, they remain satisfied at all later times. This structure is analogous to electromagnetism, where Gauss's law (∇·E = ρ/ε₀) is a constraint on the initial data that is preserved by Maxwell's evolution equations."

- question: "Explain why the ADM formalism is essential for numerical relativity."
  type: short-answer
  answer: "Numerical relativity requires solving the Einstein equations on a computer, which means evolving initial data forward in time step by step. The covariant form of the Einstein equations (G_μν = 8πG T_μν /c⁴) is not directly suitable for time evolution because it mixes space and time without a clear notion of 'initial data' and 'time stepping.' The ADM formalism provides the 3+1 decomposition needed: it identifies the initial data (γ_ij, K_ij on a spatial slice), the constraints the data must satisfy, and the evolution equations that advance the data in time. The lapse and shift provide the gauge freedom needed to choose computationally stable coordinate conditions. Modern numerical relativity codes (e.g., those used to predict LIGO waveforms for binary black hole mergers) are all based on the ADM decomposition or its refinements (BSSN formulation, generalized harmonic coordinates)."
  explanation: "The first successful numerical simulation of binary black hole mergers (Pretorius, 2005; Campanelli et al., 2006; Baker et al., 2006) was a breakthrough that required decades of work on the ADM framework, stable gauge conditions, and computational infrastructure. These simulations now provide the gravitational wave templates used by LIGO/Virgo for signal detection and parameter estimation."

- question: "How many physical degrees of freedom does the gravitational field have per spatial point, and how does the ADM counting arrive at this number?"
  type: short-answer
  answer: "The spatial metric γ_ij has 6 independent components (symmetric 3×3 matrix). Each has a conjugate momentum π^{ij}, giving 12 phase-space variables per point. The 4 constraint equations (1 Hamiltonian + 3 momentum) remove 4 phase-space degrees of freedom. The 4 gauge degrees of freedom (lapse + 3 shift components) remove another 4 through gauge-fixing. This leaves 12 - 4 - 4 = 4 phase-space variables, corresponding to 2 physical configuration-space degrees of freedom per point. These are the two polarizations of gravitational waves — the only true propagating degrees of freedom of the gravitational field."
  explanation: "The ADM counting confirms from the Hamiltonian perspective what the linearized theory shows from the wave perspective: gravity has exactly two propagating degrees of freedom. This is the same number as electromagnetism (two photon polarizations), despite the gravitational field having a much larger number of metric components."
```

## Explainer

The Einstein field equations G_μν = (8πG/c⁴)T_μν are 10 coupled, nonlinear partial differential equations that treat space and time on equal footing — they are covariant, with no preferred time direction. But physical problems often require initial-value formulations: given the state of the gravitational field at one moment, predict its future evolution. The ADM formalism, developed by Arnowitt, Deser, and Misner in 1959-1962, provides exactly this by decomposing 4D spacetime into a sequence of 3D spatial slices (a foliation), each labeled by a time coordinate t.

The 4D metric is decomposed in terms of quantities on each slice. The spatial 3-metric γ_ij describes the intrinsic geometry of each slice (distances, angles, curvature within the slice). The extrinsic curvature K_ij describes how each slice is embedded in the surrounding 4D spacetime — roughly, it measures how the slice is "bent." The lapse function N specifies the proper time between adjacent slices (how fast time flows at each point), and the shift vector N^i specifies how spatial coordinates slide sideways between slices. The 4D line element becomes ds² = -N²c²dt² + γ_ij(dx^i + N^i c dt)(dx^j + N^j c dt). The lapse and shift are gauge variables — freely choosable — corresponding to the four coordinate degrees of freedom in GR.

The Einstein equations decompose into two types. The constraint equations — the Hamiltonian constraint and three momentum constraints — involve only the spatial metric γ_ij and the extrinsic curvature K_ij (no time derivatives). They must be satisfied on every spatial slice and correspond to the G_{0μ} components of the Einstein equations. The evolution equations — corresponding to the G_{ij} components — contain time derivatives and propagate (γ_ij, K_ij) from one slice to the next. The Bianchi identity guarantees that if the constraints are satisfied on the initial slice, the evolution equations preserve them automatically. This separation into constraints and evolution is the key structural insight that makes the initial-value problem well-defined.

The ADM formalism casts GR as a Hamiltonian system with canonical variables (γ_ij, π^{ij}), where π^{ij} is the momentum conjugate to γ_ij (related to K_ij by π^{ij} = √γ(K^{ij} - γ^{ij}K)). The Hamiltonian is a sum of constraints: H = ∫(NH + N^i H_i) d³x, where H = 0 and H_i = 0 are the constraint equations. This "vanishing Hamiltonian" structure is a consequence of the diffeomorphism invariance of GR and lies at the heart of the "problem of time" in quantum gravity — the Hamiltonian generates gauge transformations (coordinate changes) rather than physical time evolution. The ADM formalism is the starting point for both numerical relativity (where the 3+1 decomposition is implemented computationally to simulate black hole mergers, neutron star collisions, and cosmological dynamics) and canonical quantum gravity (where γ_ij and π^{ij} are promoted to operators, leading to the Wheeler-DeWitt equation).
