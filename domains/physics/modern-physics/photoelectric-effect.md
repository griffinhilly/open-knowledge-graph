---
id: photoelectric-effect
title: Photoelectric Effect
domain: physics
course: modern-physics
prerequisites:
- id: blackbody-radiation
  type: soft
- id: electromagnetic-waves
  type: hard
- id: electric-potential-energy
  type: hard
builds-toward:
- photon-model
- wave-particle-duality
tags:
- quantum
- photon
- work-function
- Einstein
stage: advanced
status: validated
---

# Photoelectric Effect

## Core Idea
When light shines on a metal surface, electrons are ejected only if the frequency exceeds a threshold value — no matter how intense the light. Einstein explained this in 1905 by treating light as quanta (photons) each with energy E = hf. An electron is ejected only if a single photon carries enough energy to overcome the metal's work function φ; the maximum kinetic energy of the emitted electron is K_max = hf − φ. The intensity determines the number of photons, not their energy, explaining why a dim high-frequency source ejects electrons while a bright low-frequency source does not.

## How It's Best Learned
Map each experimental observation (threshold frequency, instantaneous emission, K_max independent of intensity) to the wave model's prediction and show each failure. Then explain each using the photon model. Millikan's precise measurements confirm the linear K_max vs. f relationship and yield h.

## Common Misconceptions
- Brighter light always ejects more energetic electrons — intensity affects the number of ejected electrons, not their maximum energy.
- The photoelectric effect proves light is a particle — it shows light behaves as particles in this context; interference still demonstrates wave behavior.
- Electrons are stored energy that light 'heats up' — the interaction is a single-photon, single-electron quantum event.

## Questions

```yaml
- question: "You shine intense red light and dim ultraviolet light on the same metal surface. The UV frequency is above the threshold; the red frequency is below it. Which produces ejected electrons?"
  type: multiple-choice
  options:
    - "The intense red light, because greater intensity delivers more total energy to the surface"
    - "The dim UV light, because its photon frequency exceeds the metal's threshold frequency"
    - "Both, because enough total light energy reaches the surface from both sources"
    - "Neither, because both beams are too weak individually to eject electrons"
  answer: 1
  explanation: "Each photon interacts with a single electron in an all-or-nothing event. The red photon energy hf_red < φ, so no single red photon can free an electron — intensity (number of photons) is irrelevant below threshold. The UV photon energy hf_UV > φ, so even a single UV photon can eject an electron. Option A embodies the classical misconception that energy accumulates from many photons; quantum mechanics shows it does not."

- question: "For a fixed frequency above the photoelectric threshold, doubling the light intensity will:"
  type: multiple-choice
  options:
    - "Double the maximum kinetic energy of the ejected electrons"
    - "Double the number of ejected electrons per second"
    - "Raise the threshold frequency for the metal"
    - "Increase the stopping potential required to halt the electrons"
  answer: 1
  explanation: "Intensity equals photon flux — more photons per second, not more energetic photons. Doubling intensity doubles the number of photon-electron collisions and thus the electron ejection rate. Maximum kinetic energy K_max = hf − φ depends only on frequency and the work function, not on intensity. Stopping potential depends on K_max and therefore also doesn't change."

- question: "According to the classical wave model, a very bright low-frequency light source should eventually eject electrons from a metal if given enough time."
  type: true-false
  answer: true
  explanation: "This is what the classical model predicts — and this prediction is wrong. Classical wave theory treats light energy as continuously delivered to the surface, so sufficient time and intensity should always transfer enough energy to free an electron. The photoelectric effect's experimental result — that no electrons are emitted below the threshold frequency regardless of intensity or exposure time — directly refutes this prediction and requires the photon model."

- question: "The maximum kinetic energy of photoelectrons emitted from a metal depends on the frequency of the incident light, not on its intensity."
  type: true-false
  answer: true
  explanation: "K_max = hf − φ. The frequency f determines the energy of each photon; the work function φ is fixed for a given metal. Intensity controls how many photons arrive per second and therefore how many electrons are ejected, but each electron that escapes carries at most hf − φ of kinetic energy. Millikan's precise measurements confirmed this linear K_max versus f relationship and measured Planck's constant h."

- question: "Why does the classical wave model of light fail to explain the photoelectric effect, and what aspect of the photon model resolves each of its failures?"
  type: short-answer
  answer: "Classical waves predict: (1) electrons should accumulate energy over time, so any frequency should eventually eject electrons given enough time — but experiment shows an instantaneous threshold. (2) Higher intensity should produce higher-energy electrons — but K_max is independent of intensity. (3) There should be a delay before emission — but emission is nearly instantaneous. The photon model resolves all three: energy comes in quanta hf, so a single low-frequency photon cannot free an electron no matter how long you wait (resolves 1); intensity sets photon count not photon energy (resolves 2); a single photon-electron collision is instantaneous (resolves 3)."
  explanation: "The failure is structural, not quantitative: the wave model is wrong in kind, not just in degree. Millikan tried for years to disprove Einstein's equation and instead confirmed the linear K_max vs. f relationship and measured h to five significant figures — the same h as in Planck's blackbody law, cementing the photon concept across phenomena."
```

## Explainer

You know from electromagnetic waves that light carries energy, and from your study of electric potential energy how energy is stored in electric fields and required to move charges. The photoelectric effect sits at the intersection of both: it is the experiment that forced physicists to accept that light energy comes in discrete chunks, not a continuous flow. The result contradicted classical physics so sharply that it was one of the experiments that launched quantum mechanics.

The classical prediction for light hitting a metal surface goes like this: the oscillating electric field of the light wave should gradually push electrons, and if you shine the light long enough or make it bright enough, an electron should eventually accumulate enough energy to escape the surface. The energy delivered to an electron should scale with intensity (brighter light = more energy per second) and with how long you wait — but *not* with frequency. Every experimental result contradicts this. Below a threshold frequency, no electrons are emitted regardless of intensity or exposure time. Above the threshold, electrons are emitted almost instantly, even in extremely dim light. And the maximum kinetic energy of the ejected electrons depends only on frequency, not on intensity.

Einstein's 1905 explanation introduced the **photon**: light of frequency f is composed of discrete energy quanta, each carrying energy E = hf. A single photon interacts with a single electron in an all-or-nothing event. The metal holds its surface electrons with a binding energy called the **work function** φ, which depends on the metal but not on the light. If the photon's energy hf exceeds φ, the electron is ejected with maximum kinetic energy K_max = hf − φ; if hf < φ, the photon cannot free the electron no matter how many photons arrive. Intensity controls the number of photons — more photons eject more electrons, but each photon still carries only hf. This explains every anomaly: threshold frequency (hf_threshold = φ), immediate emission (single quantum event, no accumulation time), and K_max linear in f with slope h.

Millikan spent years trying to disprove Einstein's equation, meticulously measuring K_max versus f for different metals. Instead he confirmed the linear relationship and measured h to five significant figures — the same h that appeared in Planck's blackbody formula. This cross-check was decisive: the same constant governs both thermal radiation and the photoelectric effect. The photon concept was not an isolated trick for one experiment but a consistent feature of electromagnetic radiation. The photoelectric effect thus marks the beginning of the particle picture of light, even though light's wave behavior (interference, diffraction) remained equally real. The reconciliation of both behaviors is wave-particle duality — the next territory you will explore — and the photoelectric effect is its first and most historically important foothold.
