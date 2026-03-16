---
id: alpha-decay-tunneling-nuclear
title: Alpha Decay and Tunneling Through the Coulomb Barrier
domain: physics
course: modern-physics
prerequisites:
- id: barrier-tunneling-transmission-probability
  type: hard
- id: radioactive-decay
  type: hard
tags:
- alpha-decay
- tunneling
- nuclear-physics
stage: advanced
status: draft
---

# Alpha Decay and Tunneling Through the Coulomb Barrier

## Core Idea
In alpha decay, a nucleus emits an alpha particle (helium nucleus) and transforms to a lighter nucleus. The Coulomb barrier between the alpha particle and daughter nucleus is several MeV high, yet alpha particles are emitted with 4–9 MeV kinetic energy. This is only possible through quantum tunneling. The half-life is exponentially sensitive to the tunneling probability, explaining huge variations (from microseconds to billions of years) in alpha-decay rates.

## How It's Best Learned
Calculate the Coulomb barrier height and width for an alpha-emitting nucleus. Use WKB tunneling probability to estimate the alpha decay rate and half-life. Compare with experimental values and understand order-of-magnitude agreements and discrepancies.

## Common Misconceptions
The alpha particle is not ejected due to centrifugal effects overcoming the barrier (tunneling is quantum-mechanical). The Q-value (kinetic energy available from mass-energy) is less than the barrier height, yet decay occurs due to tunneling. Increasing the barrier thickness dramatically reduces the decay rate (exponentially).

## Explainer

From your study of barrier tunneling, you know that a quantum particle can penetrate a potential energy barrier even when its total energy is less than the barrier height — the transmission probability depends exponentially on the barrier's width and height. From radioactive decay, you know that certain unstable nuclei emit particles with characteristic half-lives. Alpha decay is where these two ideas collide: the enormous puzzle of how an alpha particle escapes the nucleus is resolved entirely by quantum tunneling, producing one of the most dramatic demonstrations of exponential sensitivity in all of physics.

Inside the nucleus, the alpha particle (a helium-4 nucleus: 2 protons, 2 neutrons, tightly bound) is held in by the **strong nuclear force**, which creates a deep potential well extending to the nuclear radius (~1–10 fm). Outside the nucleus, the strong force turns off abruptly, and the alpha particle experiences only **Coulomb repulsion** from the daughter nucleus — a barrier that rises steeply as the alpha approaches from outside. The barrier peak is typically 25–30 MeV for heavy nuclei, yet the alpha's kinetic energy (the Q-value set by mass-energy conservation) is only 4–9 MeV. Classically, the alpha is permanently trapped. Quantum mechanically, its wavefunction has nonzero amplitude in the classically forbidden region, decaying exponentially through the barrier but emerging with a small but finite amplitude on the outside — corresponding to a finite probability of escape per unit time.

The **Gamow factor** G = exp(−2∫κ(r) dr) captures the tunneling probability, where κ(r) = √(2m[V(r)−E])/ℏ is the local inverse decay length inside the barrier. For the Coulomb barrier, this integral can be evaluated analytically using the WKB approximation, giving the **Gamow-Sommerfeld factor** that decreases steeply with decreasing alpha energy. The extraordinary feature is exponential sensitivity: a small change in alpha energy produces a huge change in the tunneling exponent, and thus in the half-life. This explains the **Geiger-Nuttall law** — the empirical observation that alpha-decay half-lives span 25 orders of magnitude (from microseconds for some transuranic nuclei to 4.5 billion years for uranium-238) while the emitted alpha energies vary by only a factor of two (4–9 MeV). The exponential in the Gamow factor amplifies tiny energy differences into astronomical half-life ratios.

The physical picture is vivid: the alpha particle rattles around inside the nucleus at nuclear velocities (~0.01c), striking the Coulomb barrier roughly 10²¹ times per second. Each attempt has a small tunneling probability T ≈ exp(−2G), and the decay rate is λ = ν × T where ν is the attempt frequency. For uranium-238, T is so small (~10⁻³⁸) that the average wait before escape is ~4.5 billion years. For polonium-212, a slightly higher alpha energy reduces the barrier integral enough to make T many orders of magnitude larger — and the half-life shrinks to 300 nanoseconds. Both nuclei decay by exactly the same mechanism; only the Gamow factor differs, and that difference, amplified exponentially, accounts for the entire 25-order-of-magnitude range. This is quantum tunneling operating at its most dramatic scale.
