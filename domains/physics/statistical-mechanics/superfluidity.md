---
id: superfluidity
title: Superfluidity
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-einstein-condensation
  type: hard
tags:
- quantum-fluid
- bose-condensate
- quantum-phenomena
stage: expert
status: validated
---

# Superfluidity

## Core Idea
A superfluid is a fluid with zero viscosity, flowing without dissipation. In Bose-Einstein condensates below T_c, the condensate wavefunction Ψ(r) is coherent and moves as a macroscopic quantum object, suppressing dissipation. This leads to vortex quantization (circulation = nh/m), fountain effects, and persistent currents. Helium-4 becomes superfluid at T_λ ≈ 2.17 K.

## Questions

```yaml
- question: "Why can superfluid helium-4 flow through a narrow capillary without any pressure drop, even though it is a real physical substance with mass?"
  type: multiple-choice
  options:
    - "Its molecules are so small that they slip through gaps without interacting with the walls"
    - "At very low temperatures, all thermal motion ceases, eliminating friction"
    - "Below the Landau critical velocity, energy-momentum conservation forbids any dissipative excitation — there are no available low-energy states for the flow to scatter into"
    - "The fluid becomes so dense that it self-lubricates, reducing viscosity to zero"
  answer: 2
  explanation: "Superfluidity is not simply 'very low friction' — it is the complete absence of dissipation arising from macroscopic quantum coherence. The condensate is described by a single coherent wavefunction, and creating a dissipative excitation (such as scattering off a wall or creating a phonon) requires exceeding the Landau critical velocity. Below this threshold, energy-momentum conservation simply does not permit any process that would slow the flow — there are no available low-energy excitations. Option B is wrong: some thermal motion remains below T_λ in the normal component. Option A is classical reasoning that misses the quantum mechanism entirely."

- question: "When a bucket of superfluid helium-4 is rotated, what happens instead of the uniform solid-body rotation seen in classical fluids?"
  type: multiple-choice
  options:
    - "The superfluid does not rotate at all — it remains stationary while the bucket spins around it"
    - "The entire fluid rotates as a solid body, just as a classical viscous fluid would"
    - "An array of quantized vortices forms, each carrying circulation in integer multiples of h/m"
    - "The fluid rotates only in the outermost layer while the interior remains still"
  answer: 2
  explanation: "Vortex quantization follows directly from the single-valuedness of the macroscopic wavefunction. Because the superfluid velocity is v_s = (ℏ/m)∇θ, the circulation around any closed loop must equal nh/m for integer n — it cannot vary continuously. Solid-body rotation (option B) would require continuously varying circulation, which is topologically forbidden. Instead, the superfluid accommodates rotation only through discrete quantized vortex lines, each carrying exactly one quantum of circulation, arranged in a regular array. This is direct experimental evidence of macroscopic quantum coherence."

- question: "A superfluid can rotate as a solid body, exactly like a classical fluid in a spinning bucket."
  type: true-false
  answer: false
  explanation: "This is precisely what the quantization of circulation rules out. The superfluid velocity v_s = (ℏ/m)∇θ must satisfy the quantization condition ∮v_s · dl = nh/m around any closed path. Solid-body rotation would require v_s proportional to the radius, giving continuously varying circulation — forbidden by the quantum constraint. Superfluids accommodate rotation only through arrays of quantized vortices, each a topological defect where the superfluid density drops to zero at the core and the phase winds by 2π. This is a defining experimental signature of the superfluid state."

- question: "Superfluidity is ultimately a consequence of macroscopic quantum coherence, not merely of being at very low temperature."
  type: true-false
  answer: true
  explanation: "Temperature alone does not cause superfluidity — the phase transition requires Bose-Einstein condensation, in which a macroscopic fraction of bosons occupy the same ground state, forming a single coherent wavefunction Ψ(r,t). It is this coherence — not merely the low temperature — that forbids dissipation (Landau criterion), quantizes vortices, and produces the fountain effect. This is why superfluidity is a distinctly quantum phenomenon: a classical fluid at the same temperature would still scatter, dissipate, and rotate without quantized vortices."

- question: "Why does the fountain effect occur in superfluid helium-4, and what does it reveal about the two-fluid model?"
  type: short-answer
  answer: "In the fountain effect, superfluid He-4 flows spontaneously through a narrow capillary toward a heated region, building up a pressure difference. This occurs because the two-fluid model treats helium below T_λ as a mixture of a superfluid component (zero viscosity, zero entropy) and a normal component (carrying all entropy). Heating one end increases the entropy there. Since the superfluid component carries no entropy, it flows toward the heated region to equalize entropy, creating a macroscopic pressure fountain. The capillary blocks the normal (viscous) component but allows the superfluid through."
  explanation: "The fountain effect is striking because it appears to violate thermodynamic intuition — a fluid flowing from cold to hot. But the two-fluid model makes it sensible: only the superfluid component (the condensate) flows through the fine capillary, driven not by pressure but by entropy gradients. The superfluid carries zero entropy and moves to minimize the system's free energy. This reveals that below T_λ, helium is not a single uniform fluid but a superposition of two components with completely different transport properties — a consequence of macroscopic quantum coherence."
```

## Explainer

From Bose-Einstein condensation, you know that below a critical temperature T_c, a macroscopic fraction of identical bosons occupy the same single-particle ground state. Instead of each particle having its own wavefunction, the entire condensate is described by a single **macroscopic wavefunction** (or order parameter) Ψ(r, t) = √(ρ_s(r)) · e^{iθ(r,t)}, where ρ_s is the local superfluid density and θ is a phase. This coherent many-body wavefunction is the origin of all superfluid phenomena.

The **superfluid velocity** is v_s = (ℏ/m)∇θ — it is the gradient of the phase. This has an immediate consequence: normal viscous flow dissipates energy by transferring momentum to the fluid randomly, creating thermal excitations. But in a superfluid, creating a dissipative excitation requires giving the flowing condensate enough energy to break a Cooper-pair analog or create a quantized vortex. For flows below the **Landau critical velocity**, energy-momentum conservation forbids any dissipative process — there are simply no low-energy excitations available to carry away the momentum. This is why superfluid helium flows through narrow channels without any pressure drop, fills containers by creeping over the rim (the "creeping film"), and maintains persistent currents for years in a ring geometry.

**Vortex quantization** follows directly from the wavefunction structure. If the superfluid flows in a loop, the phase θ must return to itself (mod 2π) after going around the loop, so the circulation ∮v_s · dl = nh/m where n is an integer. Vortices — topological defects where ρ_s = 0 at the core and the phase winds by 2π — are the only way the superfluid can rotate. When a rotating bucket of superfluid helium is observed, it develops an array of these **quantized vortices** rather than the smooth rotation of a classical fluid.

The classic experimental signature is the **fountain effect**: superfluid He-4 flows spontaneously through a capillary packed with fine powder (which blocks normal-fluid viscous flow) toward a heated region, building up a macroscopic pressure difference. The **two-fluid model** of Tisza and Landau captures this — below T_λ, helium behaves as a mixture of a superfluid component (zero viscosity, zero entropy) and a normal component (carrying all the entropy). Heating one end drives superfluid component toward it, creating a pressure fountain. As T → 0, the normal component disappears and the entire fluid becomes superfluid.
