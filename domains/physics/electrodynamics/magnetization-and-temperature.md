---
id: magnetization-and-temperature
title: Temperature Dependence of Magnetization
domain: physics
course: electrodynamics
prerequisites:
- id: ferromagnetism-microscopic-view
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
tags:
- curie-temperature
- phase-transition
- thermal-effects
stage: advanced
status: draft
---

# Temperature Dependence of Magnetization

## Core Idea
Thermal fluctuations compete with exchange interaction; above the Curie temperature ferromagnetic order disappears. The magnetization vanishes as (Tₓ - T)^β near the critical point, characterizing the ferromagnetic-paramagnetic phase transition.

## Explainer

You know from ferromagnetism that neighboring atomic magnetic moments align due to the **exchange interaction** — a quantum mechanical effect arising from the Pauli exclusion principle and electrostatic repulsion. This alignment creates magnetic domains and spontaneous bulk magnetization even without an external field. But thermal energy works against this order: higher temperature means more random thermal fluctuations that knock individual magnetic moments out of alignment with their neighbors. The competition between exchange interaction (which favors order) and thermal energy (which favors disorder) determines whether a material is ferromagnetic.

The **Curie temperature** Tc is the threshold temperature at which this competition tips decisively toward disorder. Below Tc, the exchange interaction wins: thermal fluctuations are not strong enough to break up the long-range alignment, and the material supports spontaneous magnetization. Above Tc, thermal energy dominates: moments fluctuate randomly, there is no long-range order, and the material becomes **paramagnetic** — it can be weakly magnetized by an external field but has no spontaneous order. Iron's Curie temperature is about 1043 K (770°C); nickel's is 627 K. This is why heating a permanent magnet can destroy its magnetism.

The transition at Tc is a **second-order phase transition** (or continuous phase transition). Unlike a first-order transition (like melting ice) where a discontinuous jump in an order parameter occurs at the transition temperature, the ferromagnetic-paramagnetic transition is continuous: the spontaneous magnetization M shrinks smoothly to zero as T approaches Tc from below. Near the critical point, M scales as M ~ (Tc - T)^β, where β is a **critical exponent**. The mean-field theory prediction is β = 1/2, but real materials deviate from this due to fluctuation effects, and the exact value of β depends on dimensionality and the symmetry of the order parameter — this is the domain of the renormalization group and universality classes in statistical mechanics.

Your entropy prerequisite is directly relevant here. The paramagnetic state above Tc has higher entropy: moments are disordered and can point in many directions, giving a large number of accessible microstates. The ferromagnetic state below Tc has lower entropy: moments are aligned, and the system is in a more constrained configuration. The free energy F = U - TS determines which phase is stable: at high T, the entropy term -TS becomes dominant and favors the disordered phase. This framing — order vs. disorder governed by a balance of energy and entropy — generalizes far beyond magnetism to every phase transition in condensed matter physics, from superconductivity to structural phase transitions in crystals.
