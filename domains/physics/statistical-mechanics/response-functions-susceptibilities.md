---
id: response-functions-susceptibilities
title: Response Functions and Susceptibilities
domain: physics
course: statistical-mechanics
prerequisites:
- id: linear-response-theory
  type: hard
- id: partition-function-definition
  type: soft
tags:
- response
- fluctuations
- thermodynamics
stage: advanced
status: draft
---

# Response Functions and Susceptibilities

## Core Idea
Response functions relate observables to applied fields: susceptibility χ = ∂⟨m⟩/∂h connects magnetization to field in a magnetic system. By fluctuation-dissipation, χ relates to equilibrium magnetization fluctuations χ ∝ ⟨(ΔM)^2⟩. Compressibility κ_T, thermal expansion α, heat capacity C_P and C_V are all response functions derived from the free energy.

## Explainer

From linear response theory, you know that a system's reaction to a weak external perturbation is proportional to the perturbation, with the proportionality constant called the **response function** or **susceptibility**. Now we build a systematic catalog: all the familiar macroscopic coefficients of a thermodynamic system — heat capacities, compressibility, thermal expansion — are response functions, and they are all encoded in the partition function through successive derivatives of the free energy.

Start with the **magnetic susceptibility** χ = ∂⟨M⟩/∂h, the slope of the magnetization curve at zero applied field. This measures how easily the material magnetizes. From the partition function, ⟨M⟩ = k_BT ∂(ln Z)/∂h, and taking one more derivative gives χ = (1/k_BT) [⟨M²⟩ − ⟨M⟩²] = ⟨(ΔM)²⟩/(k_BT). This is the **fluctuation-dissipation** relation for susceptibility: the magnetic response equals the variance of the magnetization divided by thermal energy. A system that fluctuates strongly between different magnetization states (large ⟨(ΔM)²⟩) also responds strongly to applied fields. Near a ferromagnetic phase transition, fluctuations diverge, and so does χ — a hallmark of critical phenomena.

The same logic applies to every conjugate pair in thermodynamics. The **isothermal compressibility** κ_T = −(1/V) ∂V/∂P|_T measures volume response to pressure and equals ⟨(ΔN)²⟩/(k_BT N²ρ) in the grand canonical ensemble — volume fluctuations encode compressibility. The **heat capacity** C_V = ∂⟨E⟩/∂T|_V = ⟨(ΔE)²⟩/(k_BT²) — energy fluctuations encode heat capacity. The **thermal expansion coefficient** α connects volume response to temperature. All of these are second derivatives of the appropriate thermodynamic potential (free energy F, Gibbs free energy G, grand potential Ω) with respect to their natural variables.

This systematic structure is powerful for two reasons. First, it means you can measure fluctuations (using scattering experiments, for instance) to determine response functions without ever applying a perturbation. Second, it means that near phase transitions, where fluctuations become anomalously large, all response functions diverge together in characteristic ways described by critical exponents. The interrelations between C_P and C_V (through the identity C_P − C_V = TVα²/κ_T) and between different susceptibilities are consequences of the underlying free energy structure, not independent results — they are all windows into the same thermodynamic potential.
