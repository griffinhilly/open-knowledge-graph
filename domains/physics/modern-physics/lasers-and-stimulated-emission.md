---
id: lasers-and-stimulated-emission
title: Stimulated Emission and Lasers
domain: physics
course: modern-physics
prerequisites:
- id: photon-absorption-emission
  type: hard
- id: planck-einstein-relation
  type: hard
- id: emission-absorption-spectra
  type: soft
- id: standing-waves
  type: soft
- id: einstein-coefficients-light-absorption-emission
  type: soft
builds-toward:
- coherent-states
tags:
- lasers
- stimulated-emission
- population-inversion
- optics
- quantum
stage: advanced
status: validated
---

# Stimulated Emission and Lasers

## Core Idea
An atom in an excited state can emit a photon spontaneously, or it can be stimulated to emit by a passing photon of the right energy. A stimulated photon matches the stimulating one in frequency, direction, phase, and polarization, so light can be amplified. Amplification needs a population inversion, with more atoms in the upper level than the lower one, which never happens in thermal equilibrium. A laser combines such a gain medium, a pumping source that maintains the inversion, and a mirrored cavity that feeds light back through the medium.

## How It's Best Learned
List the three processes (absorption, spontaneous emission, stimulated emission) with an energy-level diagram for each. Use the Boltzmann factor to show that thermal populations always favor the lower level. Then explain why two levels cannot give a steady inversion and how three- and four-level schemes get around this. Finish with the cavity: standing-wave modes, mode spacing c/2L, and the partly transmitting output mirror.

## Common Misconceptions
- Laser light is defined by being very powerful. (Many lasers are weak; a laser pointer emits a few milliwatts. What sets laser light apart is its coherence, narrow spectrum, and tight beam.)
- Pumping a two-level system hard enough will make the upper level more populated. (Strong pumping can only bring the two populations toward equality, because the pump light causes stimulated emission as fast as absorption.)
- A stimulated photon leaves in a random direction like a spontaneous one. (It copies the direction and phase of the photon that triggered it, which is why the beam builds up along the cavity axis.)

## Questions

```yaml
- question: "Why must a laser medium have a population inversion?"
  type: multiple-choice
  options: ["So that spontaneous emission stops", "So that stimulated emission outpaces absorption and the light is amplified", "So that the atoms stay in their ground state", "So that the cavity mirrors reflect more light"]
  answer: 1
  explanation: "A photon passing through the medium can be absorbed by a lower-level atom or trigger emission from an upper-level atom. Net gain needs more atoms in the upper level."
- question: "Steady optical pumping of a simple two-level system can produce more atoms in the upper level than in the lower level."
  type: true-false
  answer: false
  explanation: "In a two-level system the pump light both excites and de-excites atoms. The populations can approach equality but cannot invert. Practical lasers use three or four levels."
- question: "A laser cavity is 30 cm long. What is the frequency spacing between neighbouring longitudinal modes, c/2L?"
  type: multiple-choice
  options: ["50 MHz", "500 MHz", "1 GHz", "5 GHz"]
  answer: 1
  explanation: "c/2L = (3.0 × 10⁸ m/s)/(0.60 m) = 5.0 × 10⁸ Hz = 500 MHz."
- question: "At room temperature (kT ≈ 0.026 eV), estimate the ratio of atoms in an excited level 2.0 eV above the ground state to atoms in the ground state, assuming equal degeneracies."
  type: short-answer
  answer: "About 10⁻³⁴, essentially zero."
  explanation: "N₂/N₁ = exp(−ΔE/kT) = exp(−2.0/0.026) ≈ exp(−77) ≈ 10⁻³⁴. Thermal excitation cannot produce an inversion; it must be created by pumping."
```

## Explainer
In 1917 Albert Einstein studied how atoms and radiation reach thermal equilibrium. He found that absorption and spontaneous emission were not enough to reproduce Planck's blackbody law. A third process was needed: stimulated emission, in which a photon of energy hν = E₂ − E₁ causes an excited atom to drop to the lower level and emit a second photon. The new photon has the same frequency, direction, phase, and polarization as the first. One photon in, two identical photons out: light can be amplified.

In thermal equilibrium, though, the populations follow the Boltzmann factor, N₂/N₁ = (g₂/g₁) exp(−ΔE/kT). For a visible transition at room temperature this ratio is around 10⁻³⁴. Almost every atom sits in the lower level, so a passing photon is far more likely to be absorbed than to stimulate emission. To amplify, the medium needs a population inversion, N₂ > N₁ for equal degeneracies.

An inversion cannot be held steady with only two levels, because the pump light itself drives stimulated emission. Laser media use more levels. In a three-level laser such as ruby, atoms are pumped to a high level, drop quickly to a long-lived middle level, and lase from there to the ground state. More than half the atoms must leave the ground state, which takes strong pumping. In a four-level laser, the lower laser level lies above the ground state and empties quickly, so even a small upper population gives an inversion. Nd:YAG and helium-neon lasers work this way.

Gain alone is not enough; the light must pass through the medium many times. Two mirrors facing each other form an optical cavity. Light bouncing between them builds up in standing-wave modes whose lengths fit L = mλ/2, spaced in frequency by c/2L. One mirror transmits a small fraction of the light, which forms the output beam. Lasing starts when the gain per round trip exceeds the losses.

The first maser, using ammonia molecules and microwaves, was built by Charles Townes and colleagues in 1954. Theodore Maiman built the first laser in 1960, a ruby crystal pumped by a flash lamp, emitting at 694.3 nm. The helium-neon laser's familiar red line is at 632.8 nm. Today lasers read barcodes, carry data through optical fibres, cut metal, and measure distances with high precision.
