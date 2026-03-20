---
id: photon-model
title: 'The Photon: Light as Quanta'
domain: physics
course: modern-physics
prerequisites:
- id: photoelectric-effect
  type: hard
- id: blackbody-radiation
  type: hard
builds-toward:
- compton-scattering
- wave-particle-duality
- pair-production-annihilation
tags:
- quantum
- photon
- energy
- momentum
- E=hf
stage: advanced
status: validated
---

# The Photon: Light as Quanta

## Core Idea
A photon is the quantum of the electromagnetic field — a discrete packet carrying energy E = hf = hc/λ and momentum p = h/λ = E/c. Photons have zero rest mass and always travel at c. Despite behaving as particles in interactions (absorption, emission, scattering), they exhibit wave interference and diffraction. The photon picture unifies the results of blackbody radiation and the photoelectric effect and is the foundation for quantum electrodynamics.

## Common Misconceptions
- Photons travel at different speeds in different media — the speed in a medium is c/n, but individual photons are absorbed and re-emitted; the photon itself always moves at c between interactions.
- Higher intensity means higher photon energy — more intense light means more photons per second, not more energetic ones (at fixed frequency).

## Questions

```yaml
- question: "A red laser and a blue laser deliver the same beam intensity (same power per unit area). Which statement correctly compares their photons?"
  type: multiple-choice
  options: ["Blue photons have more energy per photon and there are more of them per second", "Red photons have more energy per photon because red light carries more heat", "Blue photons have more energy per photon, but fewer blue photons are emitted per second than red photons at equal intensity", "Red and blue photons have the same energy since intensity is equal"]
  answer: 2
  explanation: "Photon energy depends on frequency: E = hf. Blue light has higher frequency than red, so each blue photon carries more energy. But intensity is total power per area — if the blue beam delivers the same power with higher-energy photons, it must emit fewer photons per second to compensate. This directly targets the misconception that intensity determines per-photon energy."

- question: "When light travels through glass (apparent speed c/n), each individual photon is slowing down from c to c/n inside the glass."
  type: true-false
  answer: false
  explanation: "Photons always travel at c in vacuum between interactions. The apparent slowing in a medium results from photons being absorbed and re-emitted by atoms in the material. The light pulse as a whole travels at c/n, but each individual photon moves at c between those absorption/re-emission events."

- question: "Explain why the classical wave model of light was insufficient to explain the photoelectric effect, and what the photon model adds."
  type: short-answer
  answer: "The classical wave model predicts that increasing intensity (at any frequency) should eventually eject electrons, since energy builds up continuously. But experiment shows that below a threshold frequency, no electrons are ejected regardless of intensity. The photon model resolves this: ejection requires a single photon with energy E = hf exceeding the metal's work function. Intensity controls how many photons arrive per second, not their individual energies."
  explanation: "This gets at the core reason the photon model was necessary: energy transfer is quantized, not continuous. A billion low-frequency photons cannot eject a single electron if none individually has enough energy to overcome the work function. The photon model explains this directly; the classical wave model cannot."
```

## Explainer

By the early 1900s, two experiments had stubborn results that classical physics could not explain. Blackbody radiation — the glow emitted by hot objects — required energy to be emitted in discrete chunks. The photoelectric effect showed that light could only eject electrons from metals if its frequency exceeded a threshold, with intensity below that threshold making no difference at all. Einstein's 1905 insight unified both: light itself comes in discrete packets called photons, each carrying energy E = hf, where h is Planck's constant and f is the frequency.

The energy formula E = hf is the cornerstone of the photon model. Frequency — not intensity — determines how much energy each photon carries. A blue photon (high frequency) carries more energy than a red photon (low frequency). When you double the intensity of a laser, you double the number of photons arriving per second, but each photon still carries exactly the same energy as before. This distinction explains why only high-frequency light can eject electrons in the photoelectric effect: no amount of dim-but-frequent low-frequency photons compensates for each one individually lacking the energy to overcome the work function.

Photons also carry momentum, given by p = h/λ = E/c. Despite having zero rest mass, a photon has both energy and momentum — a feature you will need when studying Compton scattering, where photons collide with electrons like billiard balls and transfer measurable momentum. Photons always travel at c in vacuum; in a medium, the apparent speed is reduced because photons are repeatedly absorbed and re-emitted by atoms, but each individual photon travels at c between those interactions.

The strange and essential feature of photons is that they do not fit neatly into "wave" or "particle" categories. They interfere with themselves through double slits — a wave behavior — yet they deposit energy at discrete points on a detector — a particle behavior. This wave-particle duality is not a paradox to resolve but a feature of quantum reality to accept. The wavelength λ determines energy and momentum; the intensity determines the rate of photon arrival. Both descriptions are necessary.

The photon concept is the entry point into quantum electrodynamics (QED), the most precisely tested theory in physics. More immediately, it provides the tools to understand atomic emission spectra, laser operation, and photovoltaic cells — all phenomena that depend on energy being transferred in discrete quanta rather than continuously. The photon model is where classical electromagnetism ends and quantum mechanics begins.
