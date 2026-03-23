---
id: bose-einstein-condensation
title: Bose-Einstein Condensation
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-einstein-statistics
  type: hard
- id: grand-canonical-ensemble
  type: hard
builds-toward:
- superfluidity
tags:
- bose-gas
- phase-transition
- quantum-statistics
stage: expert
status: validated
---

# Bose-Einstein Condensation

## Core Idea
Below a critical temperature T_c = (2π)^{2/3} (ℏ^2 n / mk_B)^{2/3} / k_B, a macroscopic fraction of bosons occupies the ground state, forming a Bose-Einstein condensate. The transition is a consequence of the finite density of states at k=0 combined with the ability of bosons to occupy the same state. Above T_c, particles are distributed over excited states with average density ∝ T^{3/2}.

## Questions

```yaml
- question: "A student explains BEC by saying: 'Bosons attract each other at low temperatures, causing them to cluster together into a condensate.' What is fundamentally wrong with this explanation?"
  type: multiple-choice
  options:
    - "Bosons repel rather than attract, so clustering requires an external potential"
    - "BEC is a purely quantum-statistical phenomenon that occurs even for ideal, non-interacting bosons — it requires no attractive interactions, only the quantum-statistical indistinguishability of bosons"
    - "The clustering occurs at high temperatures, not low temperatures, because thermal energy drives bosons into the same state"
    - "The explanation is correct for liquid helium but incorrect for solid-state systems"
  answer: 1
  explanation: "BEC is driven entirely by Bose-Einstein statistics — the fact that bosons can (and, in a sense, 'prefer' to) pile into the same quantum state. The first experimental BEC in 1995 was achieved in a dilute atomic gas where interactions were intentionally kept weak, demonstrating that interactions are not required. The condensation is a consequence of the density of states near zero energy combined with the statistical mechanics of indistinguishable bosons, not of any attractive force between them."

- question: "Why must particles accumulate in the ground state below T_c, rather than simply distributing more densely across many low-energy excited states?"
  type: multiple-choice
  options:
    - "Below T_c the chemical potential becomes positive, forcing particles into the ground state by electrostatic repulsion"
    - "The density of states g(ε) ∝ ε^{1/2} → 0 as ε → 0, so excited states near zero energy are sparse; at T_c the total capacity of all excited states reaches a finite maximum, and any excess particles have nowhere to go but the single k=0 ground state"
    - "The ground state has infinite degeneracy below T_c, which allows it to absorb unlimited particles"
    - "Pauli exclusion applies to bosons below T_c, clearing all other states and forcing particles into the ground state"
  answer: 1
  explanation: "The density of states in 3D goes as g(ε) ∝ ε^{1/2}, which vanishes at ε = 0. This means there are very few quantum states available near zero energy. When the grand-canonical calculation is performed, the total number of particles that can fit in ALL excited states has a finite upper bound at any given temperature. When actual particle number exceeds this bound (as T drops below T_c), the excess must go into the single ground state — the only state excluded from the density-of-states counting. This is what makes BEC structurally different from classical clustering."

- question: "Bose-Einstein condensation requires attractive interactions between particles and cannot occur in an ideal, non-interacting gas."
  type: true-false
  answer: false
  explanation: "BEC is a purely quantum-statistical phenomenon. The first experimental realizations of BEC were achieved in dilute alkali atom gases where interactions are deliberately minimized, confirming that interactions are not required. The condensation follows entirely from Bose-Einstein statistics (bosons can share quantum states) combined with the finite density of states near zero energy. Interactions affect the properties of the condensate (e.g., they give it a speed of sound) but are not necessary for condensation itself."

- question: "Below T_c, the condensate fraction N₀/N grows as temperature decreases, reaching 1 (all particles in the ground state) only at absolute zero."
  type: true-false
  answer: true
  explanation: "The condensate fraction below T_c grows as N₀/N = 1 − (T/T_c)³: at T = T_c the fraction is 0, and it increases continuously as T decreases, reaching 1 only at T = 0. This gradual growth is characteristic of a second-order (continuous) phase transition — there is no latent heat, just a smooth order parameter (the condensate fraction) that grows from zero. At absolute zero, all N particles occupy the single k=0 ground state, described by a single macroscopic wavefunction."

- question: "Explain the role of the density of states in triggering BEC. Why does the k=0 ground state specifically accumulate a macroscopic occupation below T_c, rather than the accumulation being spread smoothly across many low-energy states?"
  type: short-answer
  answer: "In 3D, the density of states g(ε) ∝ ε^{1/2}, which goes to zero as ε → 0. The grand-canonical ensemble gives the total number of particles in excited states as an integral of the Bose factor times the density of states. At T_c, the chemical potential μ reaches 0 from below, and this integral reaches a finite maximum — despite there being infinitely many excited states, the vanishing density of states near ε = 0 means they collectively hold only a finite number of particles at T_c. Any additional particles cannot fit in the excited state continuum and must pile into the single k=0 ground state, which is not counted in the density-of-states integral. Below T_c, as temperature decreases, more and more particles are pushed into this one state. The macroscopic occupation of a single state — rather than a smooth distribution — gives the condensate its phase coherence."
  explanation: "The k=0 ground state is special because it sits exactly at the bottom of the spectrum where the density of states vanishes. It is the only state that the continuum integral misses. In 2D, g(ε) = constant rather than ∝ ε^{1/2}, so the integral diverges at μ = 0 and BEC cannot occur for an ideal gas — confirming that the ε^{1/2} density of states is essential to the phenomenon in 3D."
```

## Explainer

You already know from Bose-Einstein statistics that bosons — particles with integer spin — can occupy the same quantum state simultaneously, unlike fermions. At high temperatures this difference is irrelevant: states are sparsely populated anyway, and quantum statistics barely matters. But as you cool a gas of bosons, the thermal de Broglie wavelength grows, quantum effects strengthen, and the competition for low-energy states intensifies. Bose-Einstein condensation is what happens when this competition hits a wall.

The key is the **density of states** near zero energy. In three dimensions, the density of states goes as g(ε) ∝ ε^{1/2} — there are very few states near ε = 0. From the grand-canonical ensemble you know that the average occupation of a state with energy ε is n̄(ε) = 1/(e^{(ε−μ)/k_BT} − 1). For this to be well-defined for all states, the chemical potential μ must stay below the lowest energy, which we set to ε = 0. As you lower T at fixed particle number, μ rises toward zero. At the **critical temperature T_c**, μ hits zero from below. At this point, the number of particles that can be accommodated in *excited* states reaches a maximum (a finite value despite infinite states, because the Bose factor diverges and the density of states vanishes at ε = 0). Any additional particles — or any particles already present when T drops below T_c — *must* go into the ground state.

Below T_c, the ground state develops a **macroscopic occupation**: a finite fraction N₀/N of all N particles pile into the single k = 0 state. This fraction grows as (1 − (T/T_c)³) as the temperature drops, reaching 1 at T = 0. This is qualitatively different from a thermal distribution — a single state captures a nonzero fraction of a macroscopic system. The condensate is described by a single macroscopic wavefunction, giving the system long-range phase coherence. This coherence is the microscopic origin of **superfluidity**: the condensate flows without viscosity because scattering processes that would dissipate momentum require exciting particles out of the condensate, which costs a finite energy even at arbitrarily small flow speeds.

Real Bose-Einstein condensates in dilute atomic gases (first achieved in 1995 with rubidium-87) are extraordinarily cold — hundreds of nanokelvin — because the critical temperature scales with density and mass as T_c ∝ n^{2/3}/m. In these experiments you can directly see the condensate appear as a sharp spike in the velocity distribution at zero momentum, sitting on top of a broad thermal cloud. The sudden appearance of this spike as you cool through T_c is a phase transition with no latent heat (a second-order transition), and it is a direct demonstration that quantum statistics, not interactions, can drive macroscopic order.
