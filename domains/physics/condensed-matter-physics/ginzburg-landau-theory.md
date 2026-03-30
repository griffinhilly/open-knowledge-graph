---
id: ginzburg-landau-theory
title: Ginzburg-Landau Theory
domain: physics
course: condensed-matter-physics
prerequisites:
- id: superconductivity-phenomenology
  type: hard
- id: landau-theory
  type: hard
tags:
- ginzburg-landau
- order-parameter
- coherence-length
- superconductivity
stage: expert
status: validated
---

# Ginzburg-Landau Theory

## Core Idea
Ginzburg-Landau (GL) theory describes superconductivity through a complex order parameter psi(r) — a macroscopic wavefunction whose magnitude |psi|^2 gives the superfluid density and whose phase determines the supercurrent. The free energy functional F = integral [alpha|psi|^2 + (beta/2)|psi|^4 + (1/2m*)|(-ihbar nabla - (e*/c)A)psi|^2 + B^2/8pi] d^3r, minimized over psi and A, yields two GL equations that describe the spatial variation of the order parameter and the supercurrent. GL theory introduces two fundamental length scales: the coherence length xi (over which psi varies) and the penetration depth lambda (over which B decays). Their ratio kappa = lambda/xi determines whether the superconductor is Type I (kappa < 1/sqrt(2)) or Type II (kappa > 1/sqrt(2)).

## Questions

```yaml
- question: "The Ginzburg-Landau order parameter ψ(r) is a complex function. What is the physical significance of its phase?"
  type: multiple-choice
  options:
    - "The phase has no physical meaning and can be set to zero"
    - "The gradient of the phase determines the supercurrent: J_s = (e*ħ/m*)|ψ|²∇φ - (e*²/m*c)|ψ|²A. A uniform phase gives zero current; a spatially varying phase drives a supercurrent. Phase coherence across the sample is the defining property of the superconducting state"
    - "The phase determines the energy gap"
    - "The phase encodes the crystal structure of the superconductor"
  answer: 1
  explanation: "The supercurrent is proportional to the gauge-invariant phase gradient (∇φ - e*A/ħc). This has profound consequences: a superconducting ring must have the phase change around a loop equal to 2πn (single-valuedness of ψ), leading to flux quantization Φ = nΦ₀ = nhc/2e. The phase rigidity — the energy cost of varying the phase — is what protects supercurrents from decay. The Josephson effect arises from the phase difference between two superconductors connected by a weak link."

- question: "The GL parameter κ = λ/ξ determines whether a superconductor is Type I or Type II. What is the physical reason for the threshold at κ = 1/√2?"
  type: multiple-choice
  options:
    - "It is an arbitrary convention"
    - "At κ = 1/√2, the surface energy of a normal-superconducting interface changes sign. For κ < 1/√2, the interface has positive energy (unfavorable — Type I prefers complete flux expulsion or complete penetration). For κ > 1/√2, the interface has negative energy (favorable — Type II spontaneously creates flux-carrying vortices in the mixed state)"
    - "It marks where the critical field exceeds the Earth's magnetic field"
    - "It depends on whether the material is an element or a compound"
  answer: 1
  explanation: "The surface energy of a normal-superconducting boundary depends on the competition between the condensation energy (gained over a distance ξ as ψ recovers from zero to its bulk value) and the magnetic energy (saved over a distance λ as B decays). When ξ > λ (κ < 1/√2, Type I), the condensation energy gain dominates and the surface energy is positive — the system minimizes interfaces. When λ > ξ (κ > 1/√2, Type II), the magnetic energy saving dominates, the surface energy is negative, and the system maximizes interface area by creating quantized vortices."

- question: "Ginzburg-Landau theory was developed phenomenologically in 1950, before BCS theory. Gor'kov later showed that GL theory is derivable from BCS theory near T_c."
  type: true-false
  answer: true
  explanation: "GL theory was originally a phenomenological extension of Landau's general theory of second-order phase transitions, applied to superconductivity with a complex order parameter and minimal coupling to the electromagnetic field. In 1959, Gor'kov showed that the GL equations can be derived rigorously from BCS theory in the limit T → T_c (where Δ(r) varies slowly in space). The GL order parameter ψ is proportional to the BCS gap function Δ, the GL coefficients (α, β, m*, e*) are expressed in terms of microscopic BCS parameters, and e* = 2e confirms that the fundamental charge carriers are Cooper pairs. This connection validated GL theory and extended its credibility."

- question: "Explain why Ginzburg-Landau theory is particularly powerful for describing spatially inhomogeneous superconductivity (vortices, boundaries, thin films) where BCS theory is difficult to apply."
  type: short-answer
  answer: "BCS theory is formulated in momentum space for a uniform system — the gap equation involves integrals over k-space assuming translational invariance. Spatial inhomogeneities (vortex cores, surfaces, interfaces, applied field gradients) require solving the Bogoliubov-de Gennes equations, which are computationally expensive. GL theory is formulated in real space as a differential equation for ψ(r) coupled to Maxwell's equations, making it naturally suited to inhomogeneous problems. The two GL equations (analogous to a nonlinear Schrodinger equation) can be solved analytically for simple geometries and numerically for complex ones. Near T_c where GL is exact, it provides a complete description of vortex structure, surface superconductivity, critical fields, and the mixed state."
  explanation: "This is why GL theory remains the standard tool for understanding vortex physics, even though BCS theory is more fundamental. The Abrikosov vortex lattice, the upper and lower critical fields, and surface superconductivity (the Saint-James-de Gennes effect) were all predicted using GL theory."
```

## Explainer

Ginzburg-Landau theory takes a different approach from BCS: instead of building superconductivity from microscopic electron pairing, it describes the superconducting state through a **macroscopic order parameter** psi(r) — a complex field that is zero in the normal state and nonzero in the superconducting state. The theory is built on Landau's general framework for second-order phase transitions: near T_c, the free energy is expanded as a functional of psi, keeping terms consistent with the symmetry (gauge invariance requires the coupling to the electromagnetic vector potential A).

The GL free energy functional contains four terms: the "potential energy" alpha|psi|^2 + (beta/2)|psi|^4 (with alpha changing sign at T_c to drive the transition), the "kinetic energy" |(−ihbar nabla − e*A/c)psi|^2/(2m*) (the gauge-invariant gradient of psi, measuring the supercurrent), and the magnetic field energy B^2/8pi. Minimizing with respect to psi gives the **first GL equation** — a nonlinear Schrodinger equation for the order parameter. Minimizing with respect to A gives the **second GL equation** — the supercurrent in terms of psi and A, which serves as the source for Maxwell's equations.

Two length scales emerge naturally. The **coherence length** xi = hbar/sqrt(2m*|alpha|) is the distance over which psi can vary — it sets the size of vortex cores and the thickness of normal-superconducting boundaries. The **penetration depth** lambda is the distance over which magnetic fields decay, as in London theory. Their ratio **kappa = lambda/xi** is the Ginzburg-Landau parameter and determines the fundamental character of the superconductor. For kappa < 1/sqrt(2) (Type I), the interface between normal and superconducting regions has positive energy, and the material expels flux completely until a first-order transition at H_c. For kappa > 1/sqrt(2) (Type II), the interface energy is negative, and it becomes favorable to admit flux in quantized vortices above a lower critical field H_{c1}.

The most celebrated prediction of GL theory is the **Abrikosov vortex lattice** in Type II superconductors. Between H_{c1} and H_{c2}, magnetic flux penetrates as quantized vortices (each carrying flux quantum Phi_0 = hc/2e), arranged in a triangular lattice. The order parameter vanishes at each vortex core (over a distance ~xi) and the field decays over ~lambda from each core. At H_{c2} = Phi_0/(2pi xi^2), the vortex cores overlap and superconductivity is destroyed. GL theory provides a complete quantitative description of this mixed state, surface superconductivity above H_{c2}, and the critical current at which vortex motion produces dissipation — all essential for superconductor applications.
