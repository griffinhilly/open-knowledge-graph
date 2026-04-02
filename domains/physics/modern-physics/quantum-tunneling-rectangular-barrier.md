---
id: quantum-tunneling-rectangular-barrier
title: Quantum Tunneling Through Rectangular Barriers
domain: physics
course: modern-physics
prerequisites:
- id: quantum-tunneling
  type: hard
- id: schrodinger-equation-intro
  type: hard
builds-toward:
- barrier-tunneling-transmission-probability
tags:
- quantum-mechanics
- tunneling
- barriers
stage: expert
status: validated
---

# Quantum Tunneling Through Rectangular Barriers

## Core Idea
When a quantum particle encounters a potential barrier higher than its energy, the wavefunction does not abruptly vanish—it decays exponentially inside the barrier. If the barrier has finite width, the wavefunction is non-zero on the far side, giving a non-zero probability of finding the particle there. The tunneling probability is exponentially sensitive to barrier width and height.

## How It's Best Learned
Solve the time-independent Schrödinger equation in three regions (before, inside, and after the barrier) and match boundary conditions to find transmission coefficients. Calculate tunneling probability for specific barriers and particle energies.

## Common Misconceptions
Tunneling requires the particle energy to be below the barrier top (it happens when E < V, not E > V). The particle does not gain energy inside the barrier; it is temporary and violates energy conservation only by ΔE ~ ℏ/Δt consistent with uncertainty principle.

## Questions

```yaml
- question: "Barrier A has width d and transmission probability T₀. Barrier B is identical but has width 2d. Using the approximation T ≈ e^(−2κd), what is the transmission probability through barrier B?"
  type: multiple-choice
  options:
    - "T₀/2, because doubling the width halves the transmission"
    - "T₀², because doubling the width doubles the exponent, squaring the probability"
    - "2T₀, because the particle has twice as far to travel and thus passes through more slowly"
    - "0, because a barrier twice as wide is classically impenetrable and quantum effects vanish"
  answer: 1
  explanation: "T ≈ e^(−2κd), so for width 2d: T_B ≈ e^(−2κ·2d) = e^(−4κd) = (e^(−2κd))² = T₀². Doubling the width squares the probability — this is the exponential sensitivity that makes tunneling so sharply dependent on geometry. This is why the STM can resolve individual atoms: a 1 Å change in tip-surface distance changes the tunneling current by roughly a factor of 10."

- question: "A particle with energy E = 0.8 eV approaches a rectangular barrier of height V₀ = 1.0 eV. What form does the wavefunction take inside the barrier, and why?"
  type: multiple-choice
  options:
    - "Oscillatory (sinusoidal), because the particle still has positive total energy"
    - "A plane wave, because the particle propagates through the barrier at reduced speed"
    - "Real exponentials (growing and decaying), because kinetic energy is negative inside the barrier"
    - "Zero everywhere inside the barrier, because the particle cannot enter a classically forbidden region"
  answer: 2
  explanation: "Inside the barrier, E < V₀, so the kinetic energy E − V₀ is negative. The Schrödinger equation becomes d²ψ/dx² = κ²ψ where κ = √(2m(V₀−E))/ℏ. This has real exponential solutions Ce^(κx) + De^(−κx), not sinusoidal ones. The decaying exponential (De^(−κx)) is the key: it fades toward the far side but remains nonzero for finite width d, allowing nonzero amplitude — and thus nonzero transmission probability — on the other side. Option A applies when E > V₀ (above-barrier transmission)."

- question: "A particle that tunnels through a rectangular barrier emerges on the far side with less energy than it had before, because some energy was 'used up' penetrating the barrier."
  type: true-false
  answer: false
  explanation: "Energy is conserved in quantum tunneling. The transmitted particle has exactly the same energy E as the incident particle — it did not gain or lose energy crossing the barrier. What changes is the probability amplitude: most of the wavefunction reflects back and only a fraction transmits. The transmitted fraction still carries the original energy. The barrier does not absorb energy; it is a potential energy landscape that the particle propagates through."

- question: "The tunneling transmission probability is exponentially sensitive to barrier width, meaning a small increase in barrier width produces a disproportionately large decrease in transmission probability."
  type: true-false
  answer: true
  explanation: "T ≈ e^(−2κd) is exponentially decreasing in d. Adding even a small increment Δd multiplies T by e^(−2κΔd), which can be very small. This exponential sensitivity is not just a mathematical fact — it is physically exploited in the scanning tunneling microscope, where a ~1 Å change in tip-surface distance changes the tunneling current by about an order of magnitude, enabling atomic-resolution imaging."

- question: "Why doesn't the wavefunction simply drop to zero at the boundary of a classically forbidden region?"
  type: short-answer
  answer: "The Schrödinger equation requires that both ψ and its derivative dψ/dx are continuous across any boundary. If ψ were forced to zero at the boundary, continuity would require the wavefunction to approach zero from the incoming side as well, which contradicts the non-zero incident wavefunction. Instead, ψ smoothly transitions into an exponentially decaying form inside the barrier, consistent with the boundary conditions on both sides."
  explanation: "The matching conditions at the boundary — continuity of ψ and dψ/dx — are what make tunneling possible. They prevent an abrupt cutoff and force the wavefunction to 'leak' into the classically forbidden region. This is the mathematical origin of tunneling: not a violation of the Schrödinger equation, but a direct consequence of it combined with the requirement that solutions must be smooth."
```

## Explainer

From your study of quantum tunneling, you know that a particle can pass through a classically forbidden region. The rectangular barrier makes this quantitative. Imagine a particle moving in the +x direction toward a wall of height V₀ and width d, where the particle's total energy E is less than V₀. In classical mechanics, the particle simply bounces back — it can never enter the region where kinetic energy would be negative. In quantum mechanics, the particle is described by a wavefunction, and wavefunctions don't hard-stop at boundaries.

The tool for calculating what happens is the time-independent Schrödinger equation, which you solved for infinite and finite wells. For the rectangular barrier, divide space into three regions: Region I (before the barrier, x < 0), Region II (inside the barrier, 0 < x < d), and Region III (after the barrier, x > d). In Regions I and III, E > 0 and the kinetic energy is positive, so the Schrödinger equation gives oscillatory solutions — plane waves of the form Ae^{ikx} + Be^{-ikx}, where ℏk = √(2mE). These represent incoming, reflected, and transmitted waves.

Inside the barrier, E < V₀, so the kinetic energy is negative. The Schrödinger equation becomes d²ψ/dx² = κ²ψ where κ = √(2m(V₀−E))/ℏ. The solutions are real exponentials: Ce^{κx} + De^{-κx}. This exponential decay is the key to tunneling — the wavefunction doesn't vanish abruptly but fades. If the barrier is thin enough, a non-zero amplitude survives to Region III, meaning there is a non-zero probability of finding the particle on the far side.

The **transmission coefficient** T is found by matching ψ and dψ/dx at both boundaries x=0 and x=d. Matching at both interfaces gives four equations relating the amplitudes. After solving, the result for E < V₀ is approximately T ≈ e^{−2κd}, where κ = √(2m(V₀−E))/ℏ. This single formula captures why tunneling is exponentially sensitive to barrier width d and height (V₀−E): doubling the width roughly squares the transmission probability, and a taller barrier increases κ, suppressing T even faster.

This exponential sensitivity has profound physical applications. In alpha decay, a nucleus emits an alpha particle that tunnels through the Coulomb barrier — tiny changes in barrier height explain why some isotopes have half-lives of microseconds while others have half-lives of billions of years. The **scanning tunneling microscope** (STM) exploits the same sensitivity: a metallic tip brought nanometers from a surface passes a tunneling current that falls by a factor of ~10 for each additional ångström of distance, allowing atomic-resolution imaging. Tunnel diodes use controlled barrier engineering for fast electronic switching. In all these cases, the physics is the same rectangular-barrier calculation you've now learned to solve.


