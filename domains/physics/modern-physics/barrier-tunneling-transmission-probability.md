---
id: barrier-tunneling-transmission-probability
title: Tunneling Probability and Transmission Coefficient Calculations
domain: physics
course: modern-physics
prerequisites:
- id: quantum-tunneling-rectangular-barrier
  type: hard
builds-toward:
- alpha-decay-tunneling-nuclear
tags:
- quantum-mechanics
- tunneling
- probability
stage: advanced
status: draft
---

# Tunneling Probability and Transmission Coefficient Calculations

## Core Idea
The transmission coefficient T ≈ exp(−2κL) for a rectangular barrier (WKB approximation), where κ = √(2m(V₀−E))/ℏ and L is the barrier width. This exponential dependence means small changes in barrier parameters can dramatically affect tunneling rates. For thick or high barriers, T becomes extremely small even if E approaches V₀.

## How It's Best Learned
Apply the WKB approximation to realistic barriers. Calculate transmission coefficients for electrons tunneling through potential steps and compare to exact quantum mechanical results. Discuss how tunneling probability scales with particle mass (relevant to tunneling of different particles).

## Common Misconceptions
The transmission coefficient is not simply related to the fraction of particles at the barrier boundary (it depends exponentially on the integral of the wavefunction decay). Higher mass particles tunnel much less readily than light particles at the same energy.

## Explainer

From your study of the rectangular barrier, you know that a particle with energy E less than a barrier height V₀ has a non-zero probability of being found on the other side — not because it goes over the barrier, but because its wavefunction decays exponentially through the classically forbidden region and emerges with reduced amplitude. The **transmission coefficient** T quantifies what fraction of the incident probability flux makes it through. For a rectangular barrier of width L, the WKB (Wentzel-Kramers-Brillouin) result is T ≈ exp(−2κL), where κ = √(2m(V₀ − E))/ℏ is the decay constant inside the barrier.

The most important feature of this formula is its *exponential* sensitivity. κ appears in the exponent, so small changes in barrier parameters cause enormous changes in T. Double the barrier width L, and T drops by exp(−2κ × L) — multiplied by itself, not halved. Raise V₀ by a small amount, and κ increases, causing another exponential drop. This extreme sensitivity is why tunneling is observable at the atomic scale but completely negligible for macroscopic objects. For an electron (m ≈ 9×10⁻³¹ kg) facing a 1 eV barrier 0.1 nm wide, T is on the order of 0.1 — readily observable. For a proton (1836 times heavier), κ is larger by √1836 ≈ 43, and T plummets. For a grain of sand, tunneling is utterly negligible even over the age of the universe.

The exponential also explains why the scanning tunneling microscope (STM) achieves atomic resolution. The tunneling current between the microscope tip and a conducting surface depends exponentially on tip-to-surface distance. Moving the tip 0.1 nm closer roughly doubles the current; moving it 0.1 nm further roughly halves it. This extreme distance sensitivity means that even a single-atom bump on the surface produces a measurable change in current as the tip scans across — revealing the atomic-scale topography of the surface.

For barriers that are not rectangular, the **WKB approximation** generalizes the result: T ≈ exp(−2∫κ(x)dx), where the integral runs across the forbidden region and κ(x) = √(2m(V(x) − E))/ℏ varies with the local potential. This integral form is the key to calculating tunneling through arbitrary potential shapes — from the triangular barriers in field-emission devices to the Coulomb barrier in alpha decay, where a helium nucleus tunnels out of a nuclear potential well through a tall Coulomb repulsion barrier. Gamow's calculation of alpha decay rates using this formula in 1928 was one of the first triumphs of quantum mechanics applied to nuclear physics.
