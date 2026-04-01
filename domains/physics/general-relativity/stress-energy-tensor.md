---
id: stress-energy-tensor
title: The Stress-Energy Tensor
domain: physics
course: general-relativity
prerequisites:
- id: tensor-calculus-gr
  type: hard
- id: special-relativity-postulates
  type: hard
tags:
- stress-energy
- energy-momentum
- perfect-fluid
- matter-source
- conservation-law
stage: expert
status: validated
---

# The Stress-Energy Tensor

## Core Idea
The stress-energy tensor T_μν is the source term in Einstein's field equations — it encodes the density and flux of energy and momentum for all non-gravitational matter and fields. T_{00} is the energy density, T_{0i} is the momentum density (or equivalently the energy flux), and T_{ij} is the stress (momentum flux, including pressure and shear). For a perfect fluid, T_μν = (ρ + p/c²)u_μ u_ν + p g_μν, where ρ is the energy density, p is the pressure, and u^μ is the four-velocity. The local conservation law ∇^μ T_μν = 0 generalizes energy-momentum conservation to curved spacetime and is automatically enforced by the Einstein equations through the contracted Bianchi identity. The stress-energy tensor is symmetric (T_μν = T_νμ), which ensures conservation of angular momentum.

## Questions

```yaml
- question: "In the stress-energy tensor of a perfect fluid, the pressure p contributes to the gravitational field. In what physical situation does this pressure contribution become important?"
  type: multiple-choice
  options:
    - "Whenever the fluid is in hydrostatic equilibrium"
    - "Only in fluids moving close to the speed of light"
    - "When the pressure is comparable to the energy density ρc², as in neutron star interiors or the early universe"
    - "Only in the presence of viscosity and shear stress"
  answer: 2
  explanation: "In the stress-energy tensor T_μν = (ρ + p/c²)u_μ u_ν + p g_μν, the pressure appears alongside the energy density as a source of gravity. For ordinary matter, p << ρc², so the pressure contribution is negligible. But in neutron stars (where degeneracy pressure is enormous), in the early universe (where radiation pressure equals ρc²/3), and near the core of collapsing stars, the pressure contribution is significant and can even accelerate gravitational collapse — a purely relativistic effect with no Newtonian analog."

- question: "The equation ∇^μ T_μν = 0 in curved spacetime means that total energy is globally conserved in general relativity."
  type: true-false
  answer: false
  explanation: "∇^μ T_μν = 0 is a local conservation law: it says energy-momentum is locally conserved in the sense that the covariant divergence vanishes. However, in curved spacetime, a covariant divergence cannot generally be integrated into a global conservation law because there is no coordinate-invariant way to add up energy densities at different points (parallel transport is path-dependent). Global energy conservation holds in spacetimes with time-translation symmetry (Killing vectors), but in general — for example, in an expanding universe — total energy is not a well-defined conserved quantity."

- question: "Explain why the stress-energy tensor must be symmetric (T_μν = T_νμ) and what physical property this symmetry ensures."
  type: short-answer
  answer: "The symmetry T_μν = T_νμ is required for consistency with the Einstein field equations, since the Einstein tensor G_μν is symmetric. Physically, the symmetry of T_μν ensures conservation of angular momentum. The component T_{0i} represents both momentum density and energy flux — their equality is the relativistic statement that the flow of energy carries momentum. The spatial components T_{ij} = T_{ji} mean that shear stresses are symmetric, which is the standard condition for the absence of intrinsic torques (no 'couple stresses') in the continuum."
  explanation: "In special relativity, the symmetry of T_μν can be derived from the Belinfante-Rosenfeld procedure for the canonical energy-momentum tensor. In GR, defining T_μν as the variational derivative of the matter action with respect to g^{μν} automatically produces a symmetric tensor."

- question: "For electromagnetic radiation, T_{μν} is traceless (g^{μν}T_{μν} = 0). What does this imply about the relationship between energy density and pressure of a photon gas?"
  type: short-answer
  answer: "For a photon gas treated as a perfect fluid, the stress-energy tensor T_μν = (ρ + p/c²)u_μ u_ν + p g_μν has trace T = g^{μν}T_μν = -ρc² + 3p (in the -+++ convention). Setting T = 0 gives p = ρc²/3, the radiation equation of state. This means the pressure of a photon gas is exactly one-third of its energy density. This result is also derivable from kinetic theory (massless particles moving isotropically exert pressure equal to one-third of the energy density) and is crucial for cosmology, where it determines how radiation energy density scales with the expansion of the universe (as a^{-4})."
  explanation: "The tracelessness of the electromagnetic stress-energy tensor reflects the conformal invariance of Maxwell's equations in four dimensions — massless fields have no intrinsic length or energy scale. This property extends to any massless field, and the equation of state p = ρc²/3 is universal for radiation."
```

## Explainer

The stress-energy tensor is the object that tells spacetime how to curve. In Newtonian gravity, the source of the gravitational field is mass density ρ, a single scalar. In general relativity, a single scalar is insufficient: the source must be a symmetric (0,2) tensor T_μν to match the Einstein tensor on the other side of the field equations. This is because energy, momentum, and stress all contribute to gravity in relativity. A moving object has more energy (and therefore more gravitational effect) than a stationary one. Pressure contributes to the gravitational field. Stresses — internal forces within a material — contribute. All of this information is packaged into T_μν.

The physical interpretation of the components is clearest in a local inertial frame. T_{00} is the energy density (including rest-mass energy). T_{0i} = T_{i0} is the momentum density in the i-direction, which is equivalently the flux of energy in the i-direction — this equivalence is a consequence of the symmetry T_μν = T_νμ and is a relativistic identity (energy flow carries momentum). T_{ij} is the flux of i-momentum in the j-direction, which is the stress tensor from continuum mechanics: the diagonal components T_{ii} are the pressures (normal stress), and the off-diagonal components T_{ij} (i ≠ j) are the shear stresses.

The most important special case is the perfect fluid: a fluid with no viscosity or heat conduction, characterized entirely by its energy density ρ, pressure p, and four-velocity u^μ. Its stress-energy tensor is T_μν = (ρ + p/c²)u_μ u_ν + p g_μν. In the fluid's rest frame, this reduces to T_{00} = ρ, T_{ij} = p δ_{ij}, with no momentum density or shear stress. The perfect fluid model describes the matter content in most cosmological models, the interior of stars, and many other astrophysical situations. For dust (pressureless matter), p = 0 and T_μν = ρ u_μ u_ν. For radiation, p = ρc²/3, which follows from the tracelessness of the electromagnetic stress-energy tensor.

The conservation law ∇^μ T_μν = 0 is the curved-spacetime generalization of energy-momentum conservation. In flat spacetime with Cartesian coordinates, it reduces to ∂^μ T_μν = 0, which can be integrated over a spatial volume to give global conservation of energy and momentum. In curved spacetime, the covariant divergence cannot generally be converted to a global conservation law because there is no coordinate-invariant way to compare vectors (including momentum vectors) at different points. Global energy conservation is recovered only in spacetimes with special symmetries — specifically, those possessing a timelike Killing vector field. In an expanding universe, for example, the energy of photons decreases as they redshift, and there is no compensating increase elsewhere. This is not a violation of ∇^μ T_μν = 0 — the local law is satisfied everywhere — but rather a reflection of the fact that total energy is not a meaningful concept in a general curved spacetime.
