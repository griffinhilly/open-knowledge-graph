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
status: validated
---

# Beta Decay and Electron-Antineutrino Emission

## Core Idea
In beta-minus decay, a neutron converts to a proton, emitting an electron (beta particle) and an antineutrino: n → p + e⁻ + ν̄ₑ. The energy is shared stochastically between the electron and antineutrino, explaining the continuous electron energy spectrum. Beta decay occurs in neutron-rich nuclei to increase the proton-neutron ratio toward stability.

## Questions

```yaml
- question: "Before the neutrino was proposed, physicists observed that electrons emitted in beta decay had a continuous range of energies rather than a single fixed value. Why was this deeply troubling?"
  type: multiple-choice
  options:
    - "It suggested that beta particles were not true electrons but heavier, unstable charged particles"
    - "It appeared to violate conservation of energy: in a two-body decay, momentum and energy conservation uniquely fix the energies of both products, giving discrete values—not a spectrum"
    - "It showed the strong force was responsible for beta decay, since only the strong force could produce variable-energy particles"
    - "It implied that the nucleus was gaining mass during the decay, contradicting nuclear stability theory"
  answer: 1
  explanation: "In a two-body decay (parent → product A + product B), conservation of energy and momentum together uniquely determine the energies of both products. Every decay event should yield the same electron energy—a sharp line in the spectrum. The observed continuous spectrum meant electrons were carrying variable energy from zero up to the Q-value, with the 'missing' energy unaccounted for. This appeared to violate conservation of energy, one of physics' most fundamental laws. Pauli's resolution in 1930 was to propose an undetected third particle (the neutrino) that carries the remaining energy, restoring three-body kinematics and saving energy conservation."

- question: "Why is an electron antineutrino (ν̄_e) emitted in beta-minus decay rather than an electron neutrino (ν_e)?"
  type: multiple-choice
  options:
    - "Antineutrinos have lower rest mass than neutrinos and are therefore energetically easier for the nucleus to produce"
    - "Lepton number conservation requires it: the emitted electron carries lepton number L = +1, so a particle with L = −1 (antineutrino) must accompany it to keep the total lepton number at zero"
    - "The weak nuclear force only couples to antineutrinos in beta-minus processes; neutrinos appear only in beta-plus decay by convention"
    - "The antineutrino was named by convention based on its direction of spin relative to momentum, not based on a conserved quantum number"
  answer: 1
  explanation: "Lepton number is a conserved quantity. The initial nucleus contains no leptons (L = 0). An electron carries L = +1. For the total lepton number to remain 0 after the decay, the third particle must carry L = −1: an electron antineutrino (ν̄_e). If a neutrino (L = +1) were emitted instead, the total lepton number would become +2, violating conservation. This is not a convention—it is mandated by the conservation law. Beta-plus decay (p → n + e⁺ + ν_e) is the mirror image: the positron carries L = −1, and a neutrino (L = +1) is emitted to balance."

- question: "The continuous energy spectrum of beta-minus decay is direct evidence that three particles are produced in the final state, not two."
  type: true-false
  answer: true
  explanation: "Correct. This is the logical chain that led Pauli to propose the neutrino. Two-body decay kinematics (fixed by energy and momentum conservation) would produce a discrete electron energy—a sharp spectral line. A continuous spectrum, where the electron can carry any energy from near zero up to the Q-value, can only occur when the available energy is shared among three or more particles whose individual energies are not uniquely constrained by two conservation equations. The endpoint of the spectrum (maximum electron energy ≈ Q-value) occurs when the antineutrino carries nearly zero kinetic energy."

- question: "Beta-minus decay is driven by the strong nuclear force, which is responsible for converting a neutron into a proton within the nucleus."
  type: true-false
  answer: false
  explanation: "False. Beta decay is mediated exclusively by the weak nuclear force. The strong force binds nucleons together and governs alpha decay (via tunneling), but it cannot change quark flavor—which is precisely what happens in beta decay: a down quark in the neutron converts to an up quark, changing it into a proton. Only the weak force (via W⁻ boson exchange) mediates this flavor-changing process. This is why beta decay is so much slower than alpha decay: the weak interaction has a very short range and small coupling constant, producing lifetimes ranging from milliseconds to billions of years depending on the nucleus."

- question: "Explain why the electron energy spectrum in beta decay is continuous rather than discrete, and why this observation historically appeared to violate a fundamental conservation law."
  type: short-answer
  answer: "Beta decay produces three final-state particles: a daughter nucleus, an electron, and an antineutrino. With three particles sharing the total Q-value energy, there are more unknowns than conservation equations, so the energy distribution is not uniquely determined—it is continuous. The electron can carry anywhere from nearly zero to nearly the full Q-value, with the antineutrino carrying the complement. Before the antineutrino was known, only the electron was detected, and the varying electron energies appeared to violate energy conservation (which would require a fixed, discrete energy for a two-body decay). Pauli's 1930 proposal of an undetected third particle resolved the paradox."
  explanation: "The contrast with alpha decay is clarifying: alpha decay is two-body (parent → daughter + alpha), so energy and momentum conservation fully constrain the alpha's energy—producing a sharp, discrete spectrum. Every alpha from a given isotope has the same kinetic energy. The continuous beta spectrum was thus a dramatic anomaly by comparison, suggesting either that energy conservation failed or that something was escaping detection. The neutrino hypothesis chose the latter, and was confirmed experimentally in 1956."
```

## Explainer

You know from nuclear mass and binding energy that a nucleus is stable only if its total mass-energy is less than the sum of its separated parts — and that unstable nuclei release energy by rearranging toward more tightly bound configurations. **Beta-minus decay** occurs when a neutron-rich nucleus finds it energetically favorable to convert a neutron into a proton. The condition is that the atomic mass of the parent must exceed the atomic mass of the daughter: M(parent) > M(daughter). The difference in mass-energy, the **Q-value** Q = [M(parent) − M(daughter)]c², becomes the kinetic energy shared among the decay products.

The process n → p + e⁻ + ν̄_e produces three particles in the final state. This is the key to understanding the electron's energy spectrum. In a two-body decay (like alpha decay), momentum and energy conservation uniquely fix the energies of both products — you get a discrete energy for each. With three final-state particles sharing a fixed total energy, the energy is distributed continuously: the electron can carry anywhere from nearly zero up to nearly the full Q-value, with the antineutrino carrying the remainder. This **continuous spectrum** was deeply puzzling before the neutrino was proposed by Pauli in 1930 — it appeared to violate energy conservation. The endpoint of the spectrum (maximum electron energy) equals the Q-value and is used to measure the neutrino mass.

The **antineutrino** ν̄_e is required by lepton number conservation. The initial nucleus contains no leptons (lepton number L = 0). An electron carries L = +1, so to balance the books, a particle with L = −1 must be emitted: an electron antineutrino. The antineutrino has nearly zero mass and interacts only through the weak force, so it escapes the detector essentially without trace — yet its existence is proved by the continuous spectrum. The "missing" energy and momentum are carried by the invisible antineutrino.

Beta decay is mediated by the **weak nuclear force** — neither the strong force, electromagnetic force, nor gravity can convert a neutron to a proton. This is why beta decay is much slower than alpha decay (which proceeds via the strong force) and produces a range of lifetimes from milliseconds to billions of years depending on the nucleus. Nuclei to the neutron-rich side of the valley of nuclear stability undergo beta-minus decay; those to the proton-rich side undergo beta-plus decay (p → n + e⁺ + ν_e) or electron capture. Both are driven by the same weak interaction and move the nucleus toward the stable valley.
