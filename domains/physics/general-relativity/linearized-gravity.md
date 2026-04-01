---
id: linearized-gravity
title: Linearized Gravity
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: maxwells-equations-overview
  type: soft
tags:
- linearized-gravity
- weak-field
- gravitoelectromagnetism
- gauge-freedom
- transverse-traceless
stage: expert
status: validated
---

# Linearized Gravity

## Core Idea
Linearized gravity is the weak-field approximation of general relativity, where the metric is written as g_μν = η_μν + h_μν with |h_μν| << 1. Expanding the Einstein equations to first order in h_μν yields linear equations resembling Maxwell's equations for electromagnetism — a profound structural parallel known as gravitoelectromagnetism. In the Lorenz (harmonic) gauge, the linearized vacuum equations reduce to a wave equation □h̄_μν = 0 for the trace-reversed perturbation h̄_μν, with solutions that propagate at the speed of light. The residual gauge freedom can be used to impose the transverse-traceless (TT) gauge, isolating the two physical polarizations of gravitational waves. Linearized gravity provides the framework for gravitational wave physics, the post-Newtonian expansion, and the connection between GR and Newtonian gravity.

## Questions

```yaml
- question: "In the Lorenz gauge condition ∂^μ h̄_μν = 0, the linearized vacuum Einstein equations become □h̄_μν = 0. This is analogous to which equation in electromagnetism?"
  type: multiple-choice
  options:
    - "Gauss's law ∇·E = ρ/ε₀"
    - "The wave equation □A_μ = 0 for the electromagnetic four-potential in the Lorenz gauge"
    - "Faraday's law ∇×E = -∂B/∂t"
    - "The Biot-Savart law for magnetic fields"
  answer: 1
  explanation: "The structural parallel is exact: in electromagnetism, the Lorenz gauge ∂^μ A_μ = 0 reduces Maxwell's equations in vacuum to □A_μ = 0. In linearized gravity, the analogous gauge ∂^μ h̄_μν = 0 reduces the linearized Einstein equations in vacuum to □h̄_μν = 0. The gravitational perturbation h̄_μν plays the role of the electromagnetic potential A_μ, with the additional complexity of being a symmetric tensor rather than a vector. This analogy is the foundation of gravitoelectromagnetism."

- question: "The linearized Einstein equations are exact for arbitrarily strong gravitational fields, as long as the correct gauge is chosen."
  type: true-false
  answer: false
  explanation: "Linearization is valid only when |h_μν| << 1 — the perturbation must be small compared to the background Minkowski metric. For strong gravitational fields (near black holes, during the merger phase of binary systems), the nonlinear terms in the Einstein equations become important and linearization breaks down. The quadrupole formula for gravitational wave emission is a linearized-gravity result, valid for sources in the weak-field, slow-motion regime. For the final inspiral and merger of compact binaries, full numerical relativity (solving the nonlinear equations computationally) is required."

- question: "Explain why the transverse-traceless (TT) gauge leaves only two independent components of h_μν, and what physical degrees of freedom they represent."
  type: short-answer
  answer: "The symmetric tensor h_μν has 10 independent components in 4D. The Lorenz gauge condition ∂^μ h̄_μν = 0 provides 4 constraints, reducing to 6 independent components. The residual gauge freedom (coordinate transformations that preserve the Lorenz gauge) removes 4 more, leaving 2 physical degrees of freedom. In the TT gauge (h^{TT}_{0μ} = 0, h^{TT}_{ii} = 0, ∂^j h^{TT}_{ij} = 0), these two degrees of freedom are the plus (h₊) and cross (h×) polarizations of gravitational waves. They correspond to the two helicity-2 states of the graviton in the quantum description."
  explanation: "The counting 10 - 4 (gauge) - 4 (residual) = 2 is the same logic that reduces the 4-component electromagnetic potential A_μ to 2 physical photon polarizations: 4 - 1 (Lorenz gauge) - 1 (residual) = 2. The factor-of-two ratio (2 vs 2 physical degrees of freedom) reflects that gravity and electromagnetism have the same number of propagating modes, despite gravity being a tensor theory."

- question: "In the linearized theory with a source, the field equation becomes □h̄_μν = -16πG T_μν / c⁴. What is the retarded Green's function solution, and what physical principle does it encode?"
  type: short-answer
  answer: "The retarded Green's function solution is h̄_μν(t, x) = (4G/c⁴) ∫ T_μν(t_ret, x')/|x - x'| d³x', where t_ret = t - |x - x'|/c is the retarded time. This is the gravitational analog of the retarded potential in electrodynamics. The physical principle is causality: the gravitational perturbation at a spacetime point depends on the source distribution at the earlier retarded time, with the signal propagating outward at the speed of light. This solution is the starting point for deriving the quadrupole formula and computing gravitational wave emission from astrophysical sources."
  explanation: "The retarded Green's function solution makes explicit that gravitational influences propagate at c, not instantaneously as in Newtonian gravity. The far-field expansion of this integral (keeping the leading multipole terms) yields the quadrupole formula for gravitational radiation."
```

## Explainer

The full Einstein field equations are 10 coupled, nonlinear partial differential equations — too complex to solve analytically except in cases with high symmetry. Linearized gravity tames this complexity by restricting attention to weak gravitational fields, where the spacetime metric is close to the flat Minkowski metric: g_μν = η_μν + h_μν with the perturbation h_μν much smaller than 1 in magnitude. Expanding the Einstein equations to first order in h_μν discards all products of perturbations (h × h terms), producing a set of linear equations for h_μν. This approximation is excellent for the gravitational field of the Sun at the Earth's orbit (h ~ 10⁻⁸), for gravitational waves far from their source (h ~ 10⁻²¹), and for post-Newtonian corrections to planetary orbits.

The linearized equations have a remarkable structural similarity to Maxwell's equations of electromagnetism. Define the trace-reversed perturbation h̄_μν = h_μν - (1/2)η_μν h (where h = η^{μν}h_μν is the trace). The linearized Einstein equations become □h̄_μν - ∂_μ∂^α h̄_αν - ∂_ν∂^α h̄_αμ + η_μν ∂^α∂^β h̄_αβ = -16πG T_μν / c⁴. Imposing the Lorenz gauge condition ∂^μ h̄_μν = 0 (analogous to the Lorenz gauge ∂^μ A_μ = 0 in electromagnetism) simplifies this to □h̄_μν = -16πG T_μν / c⁴ — a wave equation with source, identical in structure to □A_μ = -μ₀ J_μ in electrodynamics. This is gravitoelectromagnetism: the time-time component h̄₀₀ plays the role of the gravitational analog of the electric potential, and the time-space components h̄₀ᵢ play the role of a gravitomagnetic vector potential.

The Lorenz gauge does not completely fix the coordinates — there remains a residual gauge freedom of coordinate transformations x^μ → x^μ + ξ^μ(x) where □ξ^μ = 0. For plane-wave solutions in vacuum, this residual freedom can be used to impose the transverse-traceless (TT) gauge, in which h₀₀ = h₀ᵢ = 0 (no temporal components), h^i_i = 0 (traceless), and k^j h_{ij} = 0 (transverse to the propagation direction k). In this gauge, the 10 original components reduce to just 2 independent physical degrees of freedom: the plus and cross polarizations h₊ and h×. For a wave propagating in the z-direction, h₊ produces differential stretching in the x and y directions, while h× does the same along axes rotated by 45 degrees. These two polarizations are the measurable content of a gravitational wave.

The TT gauge also reveals why gravitational waves are transverse and traceless — these are not arbitrary gauge choices but physical properties. Transversality (no longitudinal component) follows from the gauge constraints and means gravitational waves do not compress space along their direction of travel. Tracelessness means they produce no overall volume change — only shape distortion. Both properties are consequences of the masslessness of the graviton (or equivalently, the fact that gravity propagates at c). In the linearized theory with sources, the retarded-potential solution and its far-field multipole expansion lead to the quadrupole formula for gravitational wave emission, which is the quantitative basis for predicting signals from astrophysical sources and for interpreting LIGO/Virgo observations.
