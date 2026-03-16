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
stage: advanced
status: draft
---

# Bose-Einstein Condensation

## Core Idea
Below a critical temperature T_c = (2π)^{2/3} (ℏ^2 n / mk_B)^{2/3} / k_B, a macroscopic fraction of bosons occupies the ground state, forming a Bose-Einstein condensate. The transition is a consequence of the finite density of states at k=0 combined with the ability of bosons to occupy the same state. Above T_c, particles are distributed over excited states with average density ∝ T^{3/2}.

## Explainer

You already know from Bose-Einstein statistics that bosons — particles with integer spin — can occupy the same quantum state simultaneously, unlike fermions. At high temperatures this difference is irrelevant: states are sparsely populated anyway, and quantum statistics barely matters. But as you cool a gas of bosons, the thermal de Broglie wavelength grows, quantum effects strengthen, and the competition for low-energy states intensifies. Bose-Einstein condensation is what happens when this competition hits a wall.

The key is the **density of states** near zero energy. In three dimensions, the density of states goes as g(ε) ∝ ε^{1/2} — there are very few states near ε = 0. From the grand-canonical ensemble you know that the average occupation of a state with energy ε is n̄(ε) = 1/(e^{(ε−μ)/k_BT} − 1). For this to be well-defined for all states, the chemical potential μ must stay below the lowest energy, which we set to ε = 0. As you lower T at fixed particle number, μ rises toward zero. At the **critical temperature T_c**, μ hits zero from below. At this point, the number of particles that can be accommodated in *excited* states reaches a maximum (a finite value despite infinite states, because the Bose factor diverges and the density of states vanishes at ε = 0). Any additional particles — or any particles already present when T drops below T_c — *must* go into the ground state.

Below T_c, the ground state develops a **macroscopic occupation**: a finite fraction N₀/N of all N particles pile into the single k = 0 state. This fraction grows as (1 − (T/T_c)³) as the temperature drops, reaching 1 at T = 0. This is qualitatively different from a thermal distribution — a single state captures a nonzero fraction of a macroscopic system. The condensate is described by a single macroscopic wavefunction, giving the system long-range phase coherence. This coherence is the microscopic origin of **superfluidity**: the condensate flows without viscosity because scattering processes that would dissipate momentum require exciting particles out of the condensate, which costs a finite energy even at arbitrarily small flow speeds.

Real Bose-Einstein condensates in dilute atomic gases (first achieved in 1995 with rubidium-87) are extraordinarily cold — hundreds of nanokelvin — because the critical temperature scales with density and mass as T_c ∝ n^{2/3}/m. In these experiments you can directly see the condensate appear as a sharp spike in the velocity distribution at zero momentum, sitting on top of a broad thermal cloud. The sudden appearance of this spike as you cool through T_c is a phase transition with no latent heat (a second-order transition), and it is a direct demonstration that quantum statistics, not interactions, can drive macroscopic order.
