---
id: superfluidity
title: Superfluidity
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-einstein-condensation
  type: hard
tags:
- quantum-fluid
- bose-condensate
- quantum-phenomena
stage: advanced
status: draft
---

# Superfluidity

## Core Idea
A superfluid is a fluid with zero viscosity, flowing without dissipation. In Bose-Einstein condensates below T_c, the condensate wavefunction Ψ(r) is coherent and moves as a macroscopic quantum object, suppressing dissipation. This leads to vortex quantization (circulation = nh/m), fountain effects, and persistent currents. Helium-4 becomes superfluid at T_λ ≈ 2.17 K.

## Explainer

From Bose-Einstein condensation, you know that below a critical temperature T_c, a macroscopic fraction of identical bosons occupy the same single-particle ground state. Instead of each particle having its own wavefunction, the entire condensate is described by a single **macroscopic wavefunction** (or order parameter) Ψ(r, t) = √(ρ_s(r)) · e^{iθ(r,t)}, where ρ_s is the local superfluid density and θ is a phase. This coherent many-body wavefunction is the origin of all superfluid phenomena.

The **superfluid velocity** is v_s = (ℏ/m)∇θ — it is the gradient of the phase. This has an immediate consequence: normal viscous flow dissipates energy by transferring momentum to the fluid randomly, creating thermal excitations. But in a superfluid, creating a dissipative excitation requires giving the flowing condensate enough energy to break a Cooper-pair analog or create a quantized vortex. For flows below the **Landau critical velocity**, energy-momentum conservation forbids any dissipative process — there are simply no low-energy excitations available to carry away the momentum. This is why superfluid helium flows through narrow channels without any pressure drop, fills containers by creeping over the rim (the "creeping film"), and maintains persistent currents for years in a ring geometry.

**Vortex quantization** follows directly from the wavefunction structure. If the superfluid flows in a loop, the phase θ must return to itself (mod 2π) after going around the loop, so the circulation ∮v_s · dl = nh/m where n is an integer. Vortices — topological defects where ρ_s = 0 at the core and the phase winds by 2π — are the only way the superfluid can rotate. When a rotating bucket of superfluid helium is observed, it develops an array of these **quantized vortices** rather than the smooth rotation of a classical fluid.

The classic experimental signature is the **fountain effect**: superfluid He-4 flows spontaneously through a capillary packed with fine powder (which blocks normal-fluid viscous flow) toward a heated region, building up a macroscopic pressure difference. The **two-fluid model** of Tisza and Landau captures this — below T_λ, helium behaves as a mixture of a superfluid component (zero viscosity, zero entropy) and a normal component (carrying all the entropy). Heating one end drives superfluid component toward it, creating a pressure fountain. As T → 0, the normal component disappears and the entire fluid becomes superfluid.
