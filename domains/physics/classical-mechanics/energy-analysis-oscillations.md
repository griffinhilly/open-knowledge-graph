---
id: energy-analysis-oscillations
title: Energy Analysis in Oscillating Systems
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- coupled-oscillator-equations
- driven-harmonic-oscillator
tags:
- oscillations
- energy
- harmonics
stage: formal-systems
status: draft
---

# Energy Analysis in Oscillating Systems

## Core Idea
In simple harmonic motion, kinetic and potential energy continuously exchange, with total energy E = ½mω²A² constant. The energy oscillates between kinetic and potential at twice the frequency of displacement.

## How It's Best Learned
Plot kinetic, potential, and total energy vs. time and position. Verify that maximum kinetic energy equals maximum potential energy. Relate amplitude to total energy.

## Questions

```yaml
- question: "A mass on a spring oscillates with amplitude A. The amplitude is then doubled to 2A with the same spring and mass. What happens to the total mechanical energy?"
  type: multiple-choice
  options:
    - "It doubles, since energy is proportional to amplitude"
    - "It stays the same, since energy depends only on the spring constant and mass"
    - "It quadruples, since total energy E = ½kA² is proportional to A²"
    - "It halves, since the energy is spread over a longer oscillation path"
  answer: 2
  explanation: "Total energy in SHM is E = ½kA², so it scales as the square of amplitude. Doubling the amplitude multiplies energy by 2² = 4. This squared relationship is important: a seemingly small increase in amplitude represents a large increase in energy. Option A (doubling) is the common error from assuming a linear relationship. Options B and D are simply wrong — energy is not conserved when you externally change the amplitude, and path length is irrelevant."

- question: "At what position in its oscillation does a spring-mass system have maximum kinetic energy?"
  type: multiple-choice
  options:
    - "At the turning points (x = ±A), where the spring stores maximum elastic potential energy"
    - "At the equilibrium position (x = 0), where the spring is relaxed and all energy is kinetic"
    - "Halfway between the turning point and equilibrium, where energy is equally divided"
    - "At the same position as maximum potential energy, since they peak together"
  answer: 1
  explanation: "At x = 0 (equilibrium), the spring has zero deformation, so PE = ½kx² = 0. All the energy must be kinetic: KE = E = ½kA². This is also where the mass moves fastest (v_max = Aω). At the turning points (x = ±A), v = 0, so KE = 0 and all energy is potential. Kinetic and potential energy are perfectly out of phase — they trade off completely, never peaking at the same time. Option D is directly wrong."

- question: "The kinetic energy KE(t) and potential energy PE(t) in simple harmonic motion each oscillate at twice the frequency of the displacement x(t)."
  type: true-false
  answer: true
  explanation: "Since x(t) = A cos(ωt), we get PE = ½kA²cos²(ωt) and KE = ½kA²sin²(ωt). Both cos²(ωt) and sin²(ωt) oscillate at frequency 2ω — squaring doubles the frequency. This means energy reaches its maximum (kinetic at equilibrium, potential at turning points) twice per displacement cycle. Displacement has one amplitude maximum per cycle; energy has two. This factor-of-two relationship is a precise mathematical consequence of the squared relationship between energy and displacement."

- question: "In simple harmonic motion, the total mechanical energy is maximum at the turning points (x = ±A) and minimum at equilibrium (x = 0)."
  type: true-false
  answer: false
  explanation: "Total mechanical energy in SHM is CONSTANT — it neither increases nor decreases. E = ½kA² at every point in the motion. What changes between the turning points and equilibrium is the distribution of energy between kinetic and potential forms, not the total. At turning points, all energy is potential; at equilibrium, all energy is kinetic; everywhere else, the sum PE + KE = E is the same constant value."

- question: "A damped oscillator's amplitude decreases by 30% due to friction (from A to 0.70A). By what fraction does the total energy decrease, and why?"
  type: short-answer
  answer: "The total energy decreases to (0.70)² = 0.49 of its original value — a reduction of about 51%. Since E = ½kA², energy is proportional to the square of amplitude. A 30% decrease in amplitude produces a 51% decrease in energy, not a 30% decrease. This squared relationship means energy always falls faster than amplitude when damping is present."
  explanation: "This result has a practical consequence: when monitoring a damped system, a small decrease in the observable amplitude corresponds to a much larger fractional loss of energy. Engineers and physicists use this relationship to infer energy dissipation rates from amplitude measurements. It's also why amplitude is sometimes called 'the energy parameter' — it encodes the system's energy through this precise squared relationship, so knowing one immediately tells you the other."
```

## Explainer

You already know **simple harmonic motion**: a restoring force proportional to displacement (F = −kx) produces sinusoidal oscillations described by x(t) = A cos(ωt + φ), with angular frequency ω = √(k/m) and period T = 2π/ω. You also know **conservation of energy**: in the absence of non-conservative forces, the total mechanical energy of a system is constant. Energy analysis in oscillating systems is what you get when you apply conservation of energy to the specific case of SHM — and the result reveals the oscillation from a completely different angle.

Start with the two forms of energy in a spring-mass system. **Kinetic energy** is KE = ½mv², which is largest when the mass moves fastest. **Potential energy** (elastic potential energy stored in the spring) is PE = ½kx², which is largest when the spring is most compressed or stretched. Now use conservation of energy: KE + PE = E (constant). Substituting x(t) = A cos(ωt) gives PE = ½k A² cos²(ωt) and, since v = −Aω sin(ωt), KE = ½mA²ω² sin²(ωt). Because ω² = k/m, both terms simplify to ½kA² times a squared trig function, and sin²(ωt) + cos²(ωt) = 1 ensures the total is always **E = ½kA²**. Total energy depends only on the amplitude — double the amplitude, quadruple the energy.

The exchange between kinetic and potential energy is continuous and perfectly timed. At the **turning points** (x = ±A), the mass is momentarily at rest: all energy is potential (PE = ½kA², KE = 0). At the **equilibrium position** (x = 0), the spring is relaxed: all energy is kinetic (KE = ½kA² = ½mv²_max, PE = 0). This means the maximum speed v_max = Aω — larger amplitude or higher frequency gives greater maximum speed. Between these extremes, energy sloshes back and forth between kinetic and potential, always summing to E = ½kA².

Notice that while displacement oscillates at frequency ω (one full cycle per period T), the energy functions oscillate at **twice the frequency** — sin²(ωt) and cos²(ωt) each complete two full cycles per period T, because squaring doubles the frequency. This means energy is at maximum twice per oscillation cycle: kinetic energy peaks when the mass passes through equilibrium going in either direction, and potential energy peaks at both turning points. This factor-of-two relationship between displacement frequency and energy frequency is a precise mathematical result worth internalizing.

Finally, connect this to **amplitude as the energy parameter**. When friction or damping is present, energy is gradually removed from the system, and amplitude decreases. The amplitude decay directly tracks the energy loss: since E ∝ A², a 50% reduction in energy corresponds to a 29% reduction in amplitude (since 0.71² ≈ 0.5). This relationship between amplitude and energy is essential for analyzing damped oscillators, resonance, and driven systems in the topics that build on this one.


