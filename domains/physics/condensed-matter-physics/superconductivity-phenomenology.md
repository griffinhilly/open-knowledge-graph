---
id: superconductivity-phenomenology
title: "Superconductivity: Phenomenology (Meissner, London Equations)"
domain: physics
course: condensed-matter-physics
prerequisites:
- id: drude-sommerfeld-models
  type: hard
- id: maxwell-equations-differential-form
  type: hard
tags:
- superconductivity
- meissner-effect
- london-equations
- perfect-diamagnetism
stage: expert
status: validated
---

# Superconductivity: Phenomenology (Meissner, London Equations)

## Core Idea
Superconductors exhibit two defining properties: zero DC resistance below a critical temperature T_c, and the Meissner effect — complete expulsion of magnetic flux from the interior (B = 0, not just dB/dt = 0). The London equations, curl(J_s) = -(n_s e^2/mc)B and partial J_s/partial t = (n_s e^2/m)E, describe these phenomena phenomenologically. They predict that magnetic fields penetrate only a distance lambda_L = sqrt(mc^2/(4pi n_s e^2)) ~ 10-100 nm into the superconductor, decaying exponentially. The Meissner effect proves that superconductivity is a thermodynamic state (not merely perfect conduction), characterized by a macroscopic quantum wavefunction.

## Questions

```yaml
- question: "A perfect conductor (σ = ∞) and a superconductor both carry current with zero resistance. What experiment distinguishes them?"
  type: multiple-choice
  options:
    - "Measuring the critical temperature"
    - "Apply a magnetic field above T_c, then cool below T_c. A perfect conductor would trap the field inside (dB/dt = 0 prevents change), while a superconductor actively expels the field (Meissner effect: B = 0 regardless of history). The field expulsion on cooling is the unique signature of superconductivity"
    - "Measuring the current-carrying capacity"
    - "A perfect conductor has zero resistance only at T = 0"
  answer: 1
  explanation: "This is the crucial conceptual point. A perfect conductor (hypothetical material with σ → ∞) obeys Faraday's law: dB/dt = 0 inside, so whatever field was present when resistance vanished would be frozen in. A superconductor actively expels field (B → 0) regardless of whether the field was applied before or after cooling through T_c. This means superconductivity is an equilibrium thermodynamic phase with B = 0 as a state variable, not merely a kinetic property (zero resistance). The Meissner effect requires the London equation curl(J) ∝ -B, not just E = ρJ with ρ = 0."

- question: "The London penetration depth λ_L sets the length scale over which magnetic fields decay inside a superconductor. What determines its magnitude?"
  type: multiple-choice
  options:
    - "The crystal lattice spacing"
    - "λ_L = √(mc²/4πn_se²) depends on the superfluid density n_s — higher n_s means more screening current available and shorter penetration depth. Typical values are 20-200 nm, much larger than atomic spacings but much smaller than macroscopic samples"
    - "The mean free path of electrons"
    - "The Debye temperature of the material"
  answer: 1
  explanation: "The London penetration depth is set by the inertia of the superconducting electrons (mass m) versus their ability to screen (charge e and density n_s). Near T_c, n_s → 0 and λ_L → ∞ (the superconductor can no longer screen fields effectively). At T = 0, λ_L has its minimum value, typically 20-50 nm for elemental superconductors. The temperature dependence λ(T)/λ(0) ≈ [1 - (T/T_c)⁴]^{-1/2} (approximately) provides experimental access to the superfluid density."

- question: "The Meissner effect (B = 0 inside a superconductor) proves that superconductivity is a thermodynamic equilibrium state, not merely a kinetic phenomenon (zero resistance)."
  type: true-false
  answer: true
  explanation: "If superconductivity were only zero resistance (perfect conduction), the internal magnetic field would depend on the history — field applied before or after the transition. The Meissner effect shows that B = 0 inside regardless of history: the superconducting state is uniquely defined by (T, H), just like an equilibrium thermodynamic phase. This allows treatment by thermodynamics: the free energy difference between normal and superconducting states determines the critical field H_c via the condensation energy H_c²/8π. Without the Meissner effect, there would be no thermodynamic framework for superconductivity."

- question: "Derive the London penetration depth from the London equation and explain what happens physically at the surface of a superconductor in an applied field."
  type: short-answer
  answer: "Starting from the London equation curl(J_s) = -(n_se²/mc)B and Ampere's law curl(B) = (4π/c)J_s, taking the curl of Ampere's law and substituting gives ∇²B = B/λ_L², with λ_L = √(mc²/4πn_se²). For a flat surface with field B₀ applied parallel, the solution is B(x) = B₀ exp(-x/λ_L). Physically, the applied field induces persistent screening currents in a surface layer of thickness ~λ_L. These currents produce a field that exactly cancels the applied field in the interior. The screening currents flow without resistance (supercurrent) and create the perfect diamagnetic response. The superconductor pays a kinetic energy cost (½mv²n_s per unit volume in the screening layer) to maintain these currents."
  explanation: "The exponential decay of the field — not abrupt cancellation — is key. The penetration depth is measurable by muon spin rotation, microwave surface impedance, or the magnetic field dependence of the London moment in rotating superconductors."
```

## Explainer

Superconductivity, discovered in 1911 by Kamerlingh Onnes in mercury, is defined by two phenomena. The first, **zero resistance**, means that a current once established in a superconducting loop persists indefinitely — experiments have verified persistent currents lasting years with no measurable decay. The second, the **Meissner effect** (discovered 1933), is the complete expulsion of magnetic flux from the interior of a superconductor: B = 0 inside. The Meissner effect is not a consequence of zero resistance — a perfect conductor would freeze any pre-existing flux, not expel it. Flux expulsion proves that B = 0 is an equilibrium property of the superconducting state.

The **London brothers** (1935) captured both phenomena in two equations. The first London equation, partial J_s/partial t = (n_s e^2/m) E, says the supercurrent accelerates freely in an electric field (zero resistance). The second London equation, curl J_s = -(n_s e^2/mc) B, relates the supercurrent directly to the magnetic field (not its time derivative), which forces B = 0 in the bulk. Combined with Maxwell's equations, the London equations predict that magnetic fields penetrate only a characteristic distance lambda_L into the superconductor, decaying exponentially: B(x) = B_0 exp(-x/lambda_L). The **London penetration depth** lambda_L = sqrt(mc^2 / 4 pi n_s e^2) is typically 20-200 nm.

The Meissner effect has a direct thermodynamic consequence: expelling the field costs magnetic energy (H^2/8pi per unit volume of expelled field), so there is a **critical field** H_c above which it is energetically favorable for the material to return to the normal state. The condensation energy — the free energy gained by entering the superconducting state — equals H_c^2/8pi. This thermodynamic framework, developed by Gorter and Casimir, allows the superconducting transition to be analyzed like any other phase transition, with specific heat jumps, latent heat (at finite field), and critical exponents.

The London equations are phenomenological — they describe what happens but not why. The deeper question of why electrons form a superconducting condensate was answered by the BCS theory (1957) and the Ginzburg-Landau theory (1950). But the London equations remain the starting point for understanding superconducting electrodynamics and are exact in the appropriate limits. They also introduce the concept of a **macroscopic quantum wavefunction**: the supercurrent is proportional to the gradient of the phase of a single quantum state that extends across the entire superconductor, a concept that leads directly to flux quantization and the Josephson effect.
