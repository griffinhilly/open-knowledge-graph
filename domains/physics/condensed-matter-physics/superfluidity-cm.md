---
id: superfluidity-cm
title: Superfluidity
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bose-einstein-condensation
  type: hard
- id: bose-einstein-statistics
  type: hard
tags:
- superfluidity
- helium-4
- two-fluid-model
- quantized-vortex
stage: expert
status: validated
---

# Superfluidity

## Core Idea
Superfluidity is a macroscopic quantum state in which a fluid flows without viscosity. Helium-4 becomes superfluid below T_lambda = 2.17 K, exhibiting zero viscosity, quantized vortices (circulation = nh/m_4), a two-fluid behavior (superfluid and normal components), and a linear phonon-roton excitation spectrum. The Landau criterion states that superfluidity persists as long as the flow velocity is below a critical velocity v_c = min(epsilon(p)/p) set by the excitation spectrum. Superfluidity is intimately connected to Bose-Einstein condensation, though not identical: in liquid helium-4, only ~8% of atoms are in the condensate at T = 0 due to strong interactions, yet the superfluid fraction is 100%.

## Questions

```yaml
- question: "The Landau criterion for superfluidity requires v_c = min(ε(p)/p) > 0. Why does the ideal Bose gas, despite exhibiting BEC, fail this criterion?"
  type: multiple-choice
  options:
    - "The ideal Bose gas does not have a sharp Fermi surface"
    - "The ideal Bose gas has a quadratic excitation spectrum ε = p²/2m, giving ε(p)/p = p/2m → 0 as p → 0. The critical velocity is zero — any finite flow can create excitations and dissipate. A linear spectrum ε = cp at low momenta (as in interacting helium-4) gives v_c = c > 0, allowing superflow"
    - "The ideal Bose gas is too dilute to exhibit superfluidity"
    - "BEC and superfluidity are completely unrelated phenomena"
  answer: 1
  explanation: "This is a key insight: BEC is necessary but not sufficient for superfluidity. Interactions are essential because they transform the excitation spectrum from quadratic (non-superfluid) to linear (superfluid) at low momenta. In helium-4, the repulsive interactions between atoms create a phonon branch ε = cp at low momenta and a roton minimum at higher momenta. The Landau critical velocity is set by the roton minimum: v_c ≈ Δ_roton/p_roton ≈ 58 m/s. Without interactions, BEC gives a condensate but not a superfluid."

- question: "In the two-fluid model of helium-4 below Tλ, the liquid behaves as if it contains two interpenetrating components: a superfluid (zero viscosity, zero entropy) and a normal fluid (finite viscosity, carries all the entropy). These are not physically separate liquids."
  type: true-false
  answer: true
  explanation: "The two-fluid model (Tisza, Landau) describes the phenomenology but should not be taken too literally. The 'superfluid component' is the fraction of the liquid participating in the macroscopic quantum state (ground state + coherent excitations), while the 'normal component' consists of thermal excitations (phonons and rotons). At T = 0, the superfluid fraction is 100%. At T = Tλ, the normal fraction reaches 100% and superfluidity vanishes. The two-fluid picture successfully explains second sound (temperature waves), the fountain effect, and the mechanocaloric effect."

- question: "Explain why superfluidity in helium-3 (a fermion) requires much lower temperatures than helium-4 (a boson) and involves a fundamentally different pairing mechanism."
  type: short-answer
  answer: "Helium-3 atoms are fermions (nuclear spin 1/2), so they cannot directly undergo BEC. Superfluidity in He-3 requires the atoms to first form Cooper pairs, analogous to electrons in BCS superconductivity. This pairing is driven by spin fluctuations (not phonons) and produces p-wave, spin-triplet pairs — much more fragile than the s-wave pairs in superconductors. The transition temperature T_c ≈ 2.5 mK (versus 2.17 K for He-4) reflects both the weak pairing interaction and the exponential suppression of T_c with coupling strength. The rich internal structure of the p-wave pairs leads to multiple superfluid phases (A-phase and B-phase) with different symmetry-breaking patterns."
  explanation: "He-3 superfluidity, discovered in 1972 (Nobel Prize 1996), is one of the most complex ordered states in nature. The A-phase breaks time-reversal symmetry, the B-phase is fully gapped but anisotropic. Both have topologically protected surface states, making He-3 a model system for studying topological phases of matter."

- question: "What is second sound, and why does it exist only in superfluids?"
  type: short-answer
  answer: "Second sound is a temperature wave (oscillation of entropy density) that propagates through a superfluid. In a normal fluid, temperature disturbances diffuse (Fourier's law) rather than propagate. In a superfluid, the two-fluid nature allows an oscillation mode where the superfluid and normal components move in opposite directions: when the normal fluid (carrying entropy) sloshes one way, the superfluid (zero entropy) sloshes the other, creating a propagating temperature wave without net mass flow. The second sound velocity is c₂ = c₁√(ρ_s T s²/(ρ_n c_p)) where ρ_s/ρ_n is the superfluid-to-normal density ratio. Second sound has been measured in superfluid He-4 (~20 m/s near 1.5 K), confirming the two-fluid model."
  explanation: "First sound is an ordinary pressure/density wave (both components move together). Second sound is a purely thermal wave (components move oppositely). This distinction is unique to superfluids and provides a direct experimental probe of the superfluid fraction."
```

## Explainer

Superfluidity — the flow of a liquid without any viscosity — was discovered in helium-4 by Kapitza and by Allen and Misener in 1938, shortly after the theoretical prediction of Bose-Einstein condensation. Below the **lambda temperature** T_lambda = 2.17 K (named for the lambda-shaped specific heat anomaly), liquid helium-4 enters a state with astonishing properties: it flows through capillaries with zero viscous resistance, it creeps up and over the walls of containers as a thin film, and it supports quantized vortices where the circulation is restricted to integer multiples of h/m_4.

The theoretical framework begins with Landau's **excitation spectrum** for the interacting Bose liquid. At low momenta, the excitations are phonons (ε = cp, with c the speed of sound). At higher momenta, a local minimum in the spectrum — the **roton minimum** — represents a remnant of the tendency toward short-range solidlike order. Landau showed that a superfluid can only lose energy to its surroundings by creating excitations, and this is kinematically possible only if the flow velocity exceeds v_c = min(ε(p)/p). For helium-4, v_c is set by the roton minimum at about 58 m/s — below this velocity, the superfluid cannot dissipate energy and flows without resistance.

The **two-fluid model** describes the phenomenology below T_lambda. The liquid is treated as two interpenetrating components: a superfluid fraction rho_s (zero viscosity, zero entropy, irrotational flow) and a normal fraction rho_n (ordinary viscous fluid carrying all the entropy, consisting of thermally excited phonons and rotons). At T = 0, rho_s = rho and rho_n = 0; at T_lambda, rho_s = 0. This picture explains **second sound** — a propagating temperature wave unique to superfluids, where the normal and superfluid components oscillate out of phase. It also explains the **fountain effect**: a temperature difference drives a superfluid flow (because superfluid carries no entropy, it flows to equalize the free energy, not the pressure).

The connection between superfluidity and BEC is deep but not simple. In an ideal Bose gas, BEC occurs but the critical velocity is zero (quadratic spectrum). In liquid helium-4, strong interactions deplete the condensate to only ~8% of atoms at T = 0, yet 100% of the liquid is superfluid. Interactions convert the spectrum from quadratic to linear, enabling the Landau criterion to be satisfied. The relationship is that superfluidity requires the **phase coherence** associated with a condensate, but the superfluid fraction is determined by the response of the whole system to a velocity field, not by the condensate fraction alone. The discovery of superfluidity in fermionic helium-3 (at 2.5 mK, through Cooper-like pairing) and in ultracold atomic gases has extended these ideas to entirely new physical regimes.
