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

## Explainer

From your study of Bose-Einstein condensation, you know that below a critical temperature, a macroscopic fraction of bosons fall into the same single-particle ground state. This condensate is described by an **order parameter** — a complex field Ψ(r) = √(n₀) e^{iφ(r)}, where n₀ is the condensate density and φ is the global phase. Unlike ordinary quantum mechanics, where a single-particle wavefunction describes one particle, this order parameter describes a macroscopic number of particles all locked in the same coherent quantum state. The condensate is quantum mechanics at a macroscopic scale.

The key to superfluidity is **phase rigidity**. When the condensate flows, the superfluid velocity is related to the gradient of the phase: v_s = (ℏ/m)∇φ. This means the flow pattern is entirely determined by the phase field. For irrotational flow, ∇φ is uniform and the superfluid flows without any internal viscosity — there is nothing to generate dissipation because all the particles are moving coherently. Contrast this with a normal fluid, where random thermal motion creates viscosity through momentum exchange between fluid layers. The superfluid component carries no entropy and experiences no friction from container walls below the critical velocity.

Landau's criterion explains why superfluidity requires a minimum critical velocity. For normal fluid flow to become dissipative, the moving fluid must be able to shed energy into excitations (phonons, rotons). If the fluid is moving at velocity v and must create an excitation of energy ε(p) and momentum p, energy-momentum conservation requires v > ε(p)/p. If the excitation spectrum has a **Landau critical velocity** v_c = min[ε(p)/p] > 0, then at speeds below v_c, no excitations can be created and the flow is frictionless. The Bogoliubov spectrum you derived from the Bogoliubov transformation is linear at small momenta — phonon-like — which is what guarantees a nonzero v_c and thus superfluidity. A free ideal Bose gas has a parabolic spectrum with v_c = 0, explaining why ideal BEC is not technically a superfluid despite macroscopic occupation of the ground state.

When a superfluid is rotated, it cannot rotate uniformly like a normal fluid — that would require ∇ × v_s ≠ 0, but v_s = (ℏ/m)∇φ implies ∇ × v_s = 0 in simply connected regions. Instead, rotation is accommodated by **quantized vortices**: topological defects where the phase winds by multiples of 2π around a core. The circulation around a vortex is κ = h/m (one quantum of circulation), and the condensate density vanishes at the vortex core. Under rotation, an array of vortices forms, mimicking solid-body rotation in the large-N limit. This lattice of vortices — the Abrikosov lattice — appears in superfluid ⁴He and has been directly imaged in cold atomic gases. Quantized vortices are the rotating superfluid's answer to the topological constraint imposed by phase coherence.

The connections to other macroscopic quantum phenomena run deep. Superconductivity — your next topic — is superfluidity of Cooper pairs (charged fermion pairs that together behave as bosons). The same order-parameter language, phase rigidity, and quantized vortex structure appear, but with the charge of the condensate coupling to the electromagnetic field, producing the Meissner effect and flux quantization. The common thread across superfluidity, superconductivity, and atomic condensates is **spontaneous symmetry breaking**: the system chooses a definite phase from the continuous family of equivalent ground states, and the resulting rigidity of that broken symmetry gives the macroscopic quantum coherence that underlies all these phenomena.


