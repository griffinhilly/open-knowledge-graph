---
id: beta-decay-emission
title: Beta Decay and Electron-Antineutrino Emission
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-mass-binding-energy
  type: hard
- id: radioactive-decay
  type: soft
builds-toward:
- decay-constant-half-life-exponential
tags:
- nuclear
- radioactivity
- decay
stage: advanced
status: draft
---

# Beta Decay and Electron-Antineutrino Emission

## Core Idea
In beta-minus decay, a neutron converts to a proton, emitting an electron (beta particle) and an antineutrino: n → p + e⁻ + ν̄ₑ. The energy is shared stochastically between the electron and antineutrino, explaining the continuous electron energy spectrum. Beta decay occurs in neutron-rich nuclei to increase the proton-neutron ratio toward stability.

## Explainer

You know from nuclear mass and binding energy that a nucleus is stable only if its total mass-energy is less than the sum of its separated parts — and that unstable nuclei release energy by rearranging toward more tightly bound configurations. **Beta-minus decay** occurs when a neutron-rich nucleus finds it energetically favorable to convert a neutron into a proton. The condition is that the atomic mass of the parent must exceed the atomic mass of the daughter: M(parent) > M(daughter). The difference in mass-energy, the **Q-value** Q = [M(parent) − M(daughter)]c², becomes the kinetic energy shared among the decay products.

The process n → p + e⁻ + ν̄_e produces three particles in the final state. This is the key to understanding the electron's energy spectrum. In a two-body decay (like alpha decay), momentum and energy conservation uniquely fix the energies of both products — you get a discrete energy for each. With three final-state particles sharing a fixed total energy, the energy is distributed continuously: the electron can carry anywhere from nearly zero up to nearly the full Q-value, with the antineutrino carrying the remainder. This **continuous spectrum** was deeply puzzling before the neutrino was proposed by Pauli in 1930 — it appeared to violate energy conservation. The endpoint of the spectrum (maximum electron energy) equals the Q-value and is used to measure the neutrino mass.

The **antineutrino** ν̄_e is required by lepton number conservation. The initial nucleus contains no leptons (lepton number L = 0). An electron carries L = +1, so to balance the books, a particle with L = −1 must be emitted: an electron antineutrino. The antineutrino has nearly zero mass and interacts only through the weak force, so it escapes the detector essentially without trace — yet its existence is proved by the continuous spectrum. The "missing" energy and momentum are carried by the invisible antineutrino.

Beta decay is mediated by the **weak nuclear force** — neither the strong force, electromagnetic force, nor gravity can convert a neutron to a proton. This is why beta decay is much slower than alpha decay (which proceeds via the strong force) and produces a range of lifetimes from milliseconds to billions of years depending on the nucleus. Nuclei to the neutron-rich side of the valley of nuclear stability undergo beta-minus decay; those to the proton-rich side undergo beta-plus decay (p → n + e⁺ + ν_e) or electron capture. Both are driven by the same weak interaction and move the nucleus toward the stable valley.
