---
id: superfluidity-bosons
title: Superfluidity and Quantum Condensation
domain: physics
course: statistical-mechanics
prerequisites:
- id: bogoliubov-transformation
  type: hard
- id: bose-einstein-condensation-statmech
  type: hard
builds-toward:
- superconductivity-bcs-theory
tags:
- superfluidity
- condensation
- quantum-order
stage: advanced
status: draft
---

# Superfluidity and Quantum Condensation

## Core Idea
Superfluidity in bosonic systems (⁴He, Bose condensates) results from macroscopic quantum coherence where many particles occupy the same single-particle state. The condensate order parameter confers phase rigidity, enabling frictionless flow. Thermal excitations are Goldstone phonons; quantized vortices carry angular momentum.

## Questions

```yaml
- question: "Liquid helium-4 flows through a narrow capillary at very low velocity with no measurable pressure drop. The correct explanation is:"
  type: multiple-choice
  options:
    - "At low temperatures, helium atoms move slowly enough that they cannot transfer momentum to the capillary walls"
    - "The zero-point motion of helium atoms prevents them from forming the clusters needed for viscous drag"
    - "The flow velocity is below the Landau critical velocity, so the superfluid cannot shed energy into phonon excitations — dissipation is energetically forbidden"
    - "The condensate fraction is so large that inter-atomic collisions are suppressed, eliminating the source of viscosity"
  answer: 2
  explanation: "The Landau criterion is the correct physical explanation. Frictionless flow is not merely due to slow atomic motion or suppressed collisions — it follows from the excitation spectrum. For the moving superfluid to lose energy (to dissipate), it must create excitations. Energy-momentum conservation requires the flow speed to exceed ε(p)/p for some excitation. If the minimum of ε(p)/p (the Landau critical velocity v_c) is nonzero, no excitations can be created below that speed and the flow is frictionless. The linear (phonon) excitation spectrum from interactions gives v_c > 0, which is what makes ⁴He superfluid."

- question: "An ideal (non-interacting) Bose gas undergoes Bose-Einstein condensation at low temperature, with a macroscopic fraction of atoms in the ground state. Yet it is not technically a superfluid. Why?"
  type: multiple-choice
  options:
    - "The condensate fraction in an ideal gas is too small to support coherent flow"
    - "An ideal Bose gas lacks quantized vortices, which are required for superfluidity by definition"
    - "Without interactions, the excitation spectrum is parabolic (ε ∝ p²), giving a Landau critical velocity of zero — the gas can shed energy into excitations at any flow speed, so flow is never truly frictionless"
    - "BEC requires a periodic lattice, which blocks the long-range phase coherence needed for superfluidity"
  answer: 2
  explanation: "This is a subtle and important distinction. BEC (macroscopic ground-state occupation) is necessary but not sufficient for superfluidity. The Landau critical velocity v_c = min[ε(p)/p] for a free Bose gas is zero because the parabolic spectrum ε = p²/2m gives ε(p)/p = p/2m → 0 as p → 0. This means the gas can always create excitations at arbitrarily small flow speeds — there is no protection against dissipation. Interactions are essential: they convert the parabolic spectrum into a linear (phonon-like) spectrum at small momenta, raising v_c above zero and enabling genuine superfluidity."

- question: "A rotating superfluid accommodates angular momentum through an array of quantized vortices rather than through uniform rotation, because the phase coherence of the condensate constrains the allowed velocity fields."
  type: true-false
  answer: true
  explanation: "The superfluid velocity is vs = (ℏ/m)∇φ, which is the gradient of a scalar (the phase). This means ∇ × vs = 0 everywhere except at singularities — the superfluid cannot have uniform rigid-body rotation (which requires ∇ × v ≠ 0). The solution is vortices: topological defects where the phase winds by 2π around a core, the condensate density vanishes at the core, and the circulation around each vortex is exactly h/m. Under rotation, many such vortices form an array that mimics rigid-body rotation on average. Quantization of circulation is a direct consequence of the phase structure of the order parameter."

- question: "The superfluid order parameter is simply a number proportional to the condensate density — it carries no phase information relevant to the flow properties of the superfluid."
  type: true-false
  answer: false
  explanation: "The order parameter is a complex field Ψ(r) = √(n₀) e^{iφ(r)}, and the phase φ(r) is the physically crucial part for flow. The superfluid velocity is entirely determined by the phase gradient: vs = (ℏ/m)∇φ. The amplitude √(n₀) sets the condensate density, but all flow, quantized vortices, and the Josephson effect arise from the phase. Phase rigidity — the tendency of the phase to be spatially uniform in the ground state — is what makes the superfluid resistant to creating the phase gradients associated with excitations, which is the microscopic origin of frictionless flow."

- question: "What is the role of the order parameter's phase in superfluidity, and why does phase rigidity lead to frictionless flow?"
  type: short-answer
  answer: "The superfluid order parameter is a complex field Ψ(r) = √(n₀) e^{iφ(r)}. The superfluid velocity is vs = (ℏ/m)∇φ — it is entirely determined by the spatial gradient of the phase. Phase rigidity means that in the ground state, the phase is spatially uniform, and deforming it costs energy. Frictionless flow follows from the Landau criterion: for flow to dissipate, the superfluid must create phonon or other excitations by transferring energy and momentum to the fluid. The linear (phonon) excitation spectrum produced by interactions sets a minimum threshold for this process — the Landau critical velocity. Below this speed, energy-momentum conservation forbids excitation creation, so the phase gradient (and hence the flow) remains unchanged. Flow is frictionless because phase rigidity and the excitation spectrum together make dissipation energetically impossible at low velocities."
  explanation: "This connects BEC to superfluidity precisely: BEC creates the order parameter (and hence the phase), but interactions are what shape the excitation spectrum into the linear form that guarantees a nonzero Landau critical velocity. Without interactions, the phase exists but v_c = 0, and no frictionless flow results."
```

## Explainer

From your study of Bose-Einstein condensation, you know that below a critical temperature, a macroscopic fraction of bosons fall into the same single-particle ground state. This condensate is described by an **order parameter** — a complex field Ψ(r) = √(n₀) e^{iφ(r)}, where n₀ is the condensate density and φ is the global phase. Unlike ordinary quantum mechanics, where a single-particle wavefunction describes one particle, this order parameter describes a macroscopic number of particles all locked in the same coherent quantum state. The condensate is quantum mechanics at a macroscopic scale.

The key to superfluidity is **phase rigidity**. When the condensate flows, the superfluid velocity is related to the gradient of the phase: v_s = (ℏ/m)∇φ. This means the flow pattern is entirely determined by the phase field. For irrotational flow, ∇φ is uniform and the superfluid flows without any internal viscosity — there is nothing to generate dissipation because all the particles are moving coherently. Contrast this with a normal fluid, where random thermal motion creates viscosity through momentum exchange between fluid layers. The superfluid component carries no entropy and experiences no friction from container walls below the critical velocity.

Landau's criterion explains why superfluidity requires a minimum critical velocity. For normal fluid flow to become dissipative, the moving fluid must be able to shed energy into excitations (phonons, rotons). If the fluid is moving at velocity v and must create an excitation of energy ε(p) and momentum p, energy-momentum conservation requires v > ε(p)/p. If the excitation spectrum has a **Landau critical velocity** v_c = min[ε(p)/p] > 0, then at speeds below v_c, no excitations can be created and the flow is frictionless. The Bogoliubov spectrum you derived from the Bogoliubov transformation is linear at small momenta — phonon-like — which is what guarantees a nonzero v_c and thus superfluidity. A free ideal Bose gas has a parabolic spectrum with v_c = 0, explaining why ideal BEC is not technically a superfluid despite macroscopic occupation of the ground state.

When a superfluid is rotated, it cannot rotate uniformly like a normal fluid — that would require ∇ × v_s ≠ 0, but v_s = (ℏ/m)∇φ implies ∇ × v_s = 0 in simply connected regions. Instead, rotation is accommodated by **quantized vortices**: topological defects where the phase winds by multiples of 2π around a core. The circulation around a vortex is κ = h/m (one quantum of circulation), and the condensate density vanishes at the vortex core. Under rotation, an array of vortices forms, mimicking solid-body rotation in the large-N limit. This lattice of vortices — the Abrikosov lattice — appears in superfluid ⁴He and has been directly imaged in cold atomic gases. Quantized vortices are the rotating superfluid's answer to the topological constraint imposed by phase coherence.

The connections to other macroscopic quantum phenomena run deep. Superconductivity — your next topic — is superfluidity of Cooper pairs (charged fermion pairs that together behave as bosons). The same order-parameter language, phase rigidity, and quantized vortex structure appear, but with the charge of the condensate coupling to the electromagnetic field, producing the Meissner effect and flux quantization. The common thread across superfluidity, superconductivity, and atomic condensates is **spontaneous symmetry breaking**: the system chooses a definite phase from the continuous family of equivalent ground states, and the resulting rigidity of that broken symmetry gives the macroscopic quantum coherence that underlies all these phenomena.


