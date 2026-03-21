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

## Questions

```yaml
- question: "A particle tunnels through a barrier of width L with transmission coefficient T. The barrier width is doubled to 2L. How does T change?"
  type: multiple-choice
  options:
    - "T is halved — T is proportional to 1/L"
    - "T drops to T² — doubling L doubles the exponent in exp(−2κL), squaring the original T"
    - "T drops by a factor of exp(−2κL) — the same factor as the original T"
    - "T is unchanged if the particle energy stays the same"
  answer: 1
  explanation: "T ≈ exp(−2κL). If L doubles, the exponent becomes −2κ(2L) = −4κL = 2 × (−2κL). So the new T = exp(−4κL) = [exp(−2κL)]² = T². The transmission coefficient is squared, not halved. This exponential sensitivity is the defining feature of tunneling: linear changes in barrier parameters produce exponential changes in T. A naive linear-scaling intuition (T ∝ 1/L) would dramatically overestimate the tunneling probability for wider barriers."

- question: "The scanning tunneling microscope achieves atomic resolution because of which property of quantum tunneling?"
  type: multiple-choice
  options:
    - "Tunneling current depends linearly on tip-to-surface distance, giving a sensitive but smooth signal"
    - "Only specific atoms at the surface are quantum-mechanically allowed to contribute to tunneling current"
    - "Tunneling current depends exponentially on tip-to-surface distance, so even a single-atom height change produces a measurable current change"
    - "The tunneling wavefunction is concentrated at atomic positions, creating a map of electron density"
  answer: 2
  explanation: "The STM's extraordinary resolution comes directly from the exponential dependence of tunneling current on distance. Moving the tip 0.1 nm closer roughly doubles the current; 0.1 nm farther roughly halves it. A single-atom bump — a height change of ~0.2 nm — changes the current by roughly a factor of four. This extreme sensitivity means the STM effectively traces the atomic-scale topography of the surface. If the dependence were linear, height changes of 0.1 nm would produce much smaller fractional current changes and atomic resolution would be impossible."

- question: "A proton and an electron, both with the same kinetic energy, approach an identical potential barrier. The proton has much lower transmission probability than the electron."
  type: true-false
  answer: true
  explanation: "The decay constant κ = √(2m(V₀−E))/ℏ depends on particle mass m. A proton is about 1836 times heavier than an electron, so its κ is larger by √1836 ≈ 43. The transmission coefficient T ≈ exp(−2κL) falls exponentially with κ, so the proton's T is astronomically smaller than the electron's T for the same barrier. This mass dependence explains why quantum tunneling is observable at atomic and nuclear scales for light particles (electrons, alpha particles) but completely negligible for macroscopic objects."

- question: "For a particle with energy E approaching a barrier of height V₀, if E is very close to but still below V₀, the transmission coefficient T approaches 1."
  type: true-false
  answer: false
  explanation: "T ≈ exp(−2κL) with κ = √(2m(V₀−E))/ℏ. As E → V₀ from below, κ → 0, so exp(−2κL) → exp(0) = 1. For a thin barrier, T does indeed approach 1 as E → V₀. However, for a thick barrier (large L), even with small κ, the exponent −2κL can still be large and T can remain small. The claim that T 'approaches 1' requires either a thin barrier or E very close to V₀. The exponential dependence on L means T can be very small even when E is nearly equal to V₀ if the barrier is thick enough."

- question: "Explain why the exponential dependence of the transmission coefficient on barrier parameters means that quantum tunneling is observable at the atomic scale but completely negligible for macroscopic objects."
  type: short-answer
  answer: "T ≈ exp(−2κL) where κ = √(2m(V₀−E))/ℏ. For macroscopic objects, the mass m is enormous — say 10⁻³ kg versus 10⁻³⁰ kg for an electron. Since κ ∝ √m, the macroscopic κ is roughly 10¹³ times larger than for an electron. With even a nanometer-wide barrier, 2κL becomes a number so large that exp(−2κL) is effectively zero — far smaller than 1/10^(10^26). The exponential amplifies the mass difference into an utterly negligible probability. For electrons, κ is small enough that T is measurable for barriers a few nanometers wide."
  explanation: "The core insight is that the exponential function amplifies small differences in the exponent into astronomical differences in T. A factor-of-13 difference in κ (say, between a proton and an electron) leads to a factor of exp(−26L) difference in T — for any moderate L, this is an incomprehensibly small number. For macroscopic masses, the exponent is so large that tunneling is not merely rare but physically impossible on any timescale relevant to observation."
```

## Explainer

From your study of the rectangular barrier, you know that a particle with energy E less than a barrier height V₀ has a non-zero probability of being found on the other side — not because it goes over the barrier, but because its wavefunction decays exponentially through the classically forbidden region and emerges with reduced amplitude. The **transmission coefficient** T quantifies what fraction of the incident probability flux makes it through. For a rectangular barrier of width L, the WKB (Wentzel-Kramers-Brillouin) result is T ≈ exp(−2κL), where κ = √(2m(V₀ − E))/ℏ is the decay constant inside the barrier.

The most important feature of this formula is its *exponential* sensitivity. κ appears in the exponent, so small changes in barrier parameters cause enormous changes in T. Double the barrier width L, and T drops by exp(−2κ × L) — multiplied by itself, not halved. Raise V₀ by a small amount, and κ increases, causing another exponential drop. This extreme sensitivity is why tunneling is observable at the atomic scale but completely negligible for macroscopic objects. For an electron (m ≈ 9×10⁻³¹ kg) facing a 1 eV barrier 0.1 nm wide, T is on the order of 0.1 — readily observable. For a proton (1836 times heavier), κ is larger by √1836 ≈ 43, and T plummets. For a grain of sand, tunneling is utterly negligible even over the age of the universe.

The exponential also explains why the scanning tunneling microscope (STM) achieves atomic resolution. The tunneling current between the microscope tip and a conducting surface depends exponentially on tip-to-surface distance. Moving the tip 0.1 nm closer roughly doubles the current; moving it 0.1 nm further roughly halves it. This extreme distance sensitivity means that even a single-atom bump on the surface produces a measurable change in current as the tip scans across — revealing the atomic-scale topography of the surface.

For barriers that are not rectangular, the **WKB approximation** generalizes the result: T ≈ exp(−2∫κ(x)dx), where the integral runs across the forbidden region and κ(x) = √(2m(V(x) − E))/ℏ varies with the local potential. This integral form is the key to calculating tunneling through arbitrary potential shapes — from the triangular barriers in field-emission devices to the Coulomb barrier in alpha decay, where a helium nucleus tunnels out of a nuclear potential well through a tall Coulomb repulsion barrier. Gamow's calculation of alpha decay rates using this formula in 1928 was one of the first triumphs of quantum mechanics applied to nuclear physics.
