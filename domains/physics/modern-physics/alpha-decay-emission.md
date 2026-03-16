---
id: alpha-decay-emission
title: Alpha Decay and Helium Nucleus Emission
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-mass-binding-energy
  type: hard
- id: quantum-tunneling
  type: hard
builds-toward:
- decay-constant-half-life-exponential
tags:
- nuclear
- radioactivity
- decay
stage: abstract-reasoning
status: draft
---

# Alpha Decay and Helium Nucleus Emission

## Core Idea
In alpha decay, a nucleus emits an alpha particle (⁴₂He nucleus), transforming into a lighter nucleus. Alpha particles are highly stable due to strong binding energy, making alpha emission favorable for heavy nuclei. The process occurs via quantum tunneling through the Coulomb barrier; the alpha particle's existence inside the nucleus is unstable due to electrostatic repulsion.

## Explainer

From your study of nuclear mass and binding energy, you know that nuclei are held together by the strong nuclear force competing against the electromagnetic repulsion between protons. The strong force is short-range (a few femtometers) and very powerful; Coulomb repulsion is long-range and grows as Z increases. For light and medium nuclei, the strong force wins comfortably. For very heavy nuclei (Z > 82 or so), the nucleus is large enough that the short-range strong force cannot effectively bind every nucleon pair across the full diameter, while Coulomb repulsion among the growing number of protons keeps increasing. These nuclei are energetically unstable against shedding mass.

Why emit an alpha particle specifically — two protons plus two neutrons — rather than a single proton, two protons, or some other fragment? The answer lies in binding energy. The alpha particle (⁴He nucleus) has an exceptionally high binding energy per nucleon (~7.07 MeV), the result of a fully filled nuclear shell with all spins paired. Emitting an alpha releases substantially more energy per nucleon removed than emitting, say, a single proton. The **Q-value** — the difference in total binding energy between the parent and the alpha-plus-daughter system — is positive for heavy nuclei, meaning the products are more tightly bound than the parent. This energy appears as kinetic energy of the emitted alpha and recoiling daughter. Energetically favorable does not yet mean it happens, however.

This is where **quantum tunneling** — your other prerequisite — becomes essential. Plot the potential energy of an alpha particle as a function of its distance from the center of the parent nucleus. Inside the nucleus, the strong force creates a potential well — the alpha is bound. Outside, the Coulomb repulsion creates a tall positive barrier, rising from the nuclear surface and declining as the alpha moves farther away. Between the nuclear surface and the distance where the Coulomb barrier drops back to the alpha's energy, there is a classically forbidden region: the alpha's total energy is *less* than the potential energy of the barrier. Classically, it cannot escape. Quantum mechanically, the alpha's wavefunction does not abruptly vanish at the barrier — it decays exponentially through the classically forbidden region and emerges on the other side with nonzero amplitude. There is a small but real probability of finding the alpha outside the nucleus at any moment. This leakage is alpha decay.

The decay rate depends exponentially on the barrier integral, through a factor known as the **Gamow factor**: G ~ exp(−2∫√(2m(V(r)−E)/ℏ²) dr). Because this integral is in the exponent, small changes in the alpha's energy Q lead to enormous changes in decay rate. This extreme sensitivity is captured by the **Geiger-Nuttall law**: a log-log plot of decay constant versus alpha energy gives a straight line across many orders of magnitude. Uranium-238 has a Q-value of ~4.3 MeV, a tall thick barrier, and a half-life of 4.5 billion years. Polonium-212 has Q ~ 8.95 MeV, a thinner barrier, and decays in 300 nanoseconds. The same mechanism, differing only in barrier geometry, spans 23 orders of magnitude in half-life — one of the most striking quantitative successes of early quantum mechanics applied to nuclear physics.
