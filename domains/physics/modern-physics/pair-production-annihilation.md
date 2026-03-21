---
id: pair-production-annihilation
title: Pair Production and Annihilation
domain: physics
course: modern-physics
prerequisites:
- id: mass-energy-equivalence
  type: hard
- id: photon-model
  type: hard
tags:
- quantum
- antiparticle
- positron
- pair-production
- annihilation
stage: advanced
status: validated
---

# Pair Production and Annihilation

## Core Idea
A high-energy photon can spontaneously convert into an electron-positron pair (pair production) provided its energy exceeds 2m_e c² ≈ 1.022 MeV; this requires a nearby nucleus to conserve momentum. Conversely, an electron and positron annihilate to produce two back-to-back 0.511 MeV gamma-ray photons (annihilation). Both processes are direct manifestations of mass-energy equivalence and the existence of antimatter. Pair production and annihilation are exploited in PET scanners, where the coincident gamma rays allow precise localization of the annihilation event.

## How It's Best Learned
Apply conservation of energy and momentum to pair production to show why a single photon cannot produce a pair in free space (a nucleus must recoil). Verify that annihilation gamma-ray energies follow directly from E = mc².

## Common Misconceptions
- Pair production violates conservation of charge — the electron carries −e and the positron carries +e, so net charge is zero before and after.
- Positrons are exotic — they are the antiparticle of the electron, produced whenever a sufficiently energetic photon encounters a nucleus; they occur routinely in cosmic ray showers.

## Questions

```yaml
- question: "A student argues: 'A 2 MeV photon has more than enough energy to create an electron-positron pair (which requires only 1.022 MeV), so pair production can occur anywhere in free space.' This is wrong because:"
  type: multiple-choice
  options:
    - "2 MeV is actually insufficient — pair production requires at least 4 MeV to account for the kinetic energy of the products"
    - "A single photon in free space cannot simultaneously conserve both energy and momentum for the reaction — a nearby nucleus must absorb recoil momentum"
    - "Photons can only interact with matter at nuclear surfaces, not in open vacuum"
    - "The photon must have the correct wavelength (not just sufficient energy) to match the electron's de Broglie wavelength"
  answer: 1
  explanation: "The student's error is checking only energy conservation, not momentum conservation simultaneously. A photon has E = pc; an electron-positron pair at rest has E = 2m_e c² and p = 0. No single photon can supply E = 2m_e c² while also having zero momentum — if E > 0, then p = E/c > 0 as well. This is a kinematic impossibility, not an energy insufficiency. A nearby nucleus absorbs recoil momentum, allowing both conservation laws to be satisfied at once. Even a 100 MeV photon cannot pair-produce in free space for this reason."

- question: "In a PET scanner, two photons are detected in coincidence in exactly opposite directions. This back-to-back emission is directly explained by:"
  type: multiple-choice
  options:
    - "The radiotracer emitting photon pairs during its radioactive decay"
    - "Momentum conservation: in the center-of-mass frame of the annihilating electron-positron pair, total momentum is zero, requiring two photons of equal energy in opposite directions"
    - "PET scanner design — detectors are placed opposite each other and only accept anti-coincident signals"
    - "The two photons carrying kinetic energy and rest-mass energy separately, so they travel in perpendicular directions"
  answer: 1
  explanation: "When an electron and positron annihilate (approximately at rest), total three-momentum is zero. The final state must also have zero total momentum. Two photons can achieve this only if they have equal energy and travel in exactly opposite directions (their momenta cancel). A single photon is forbidden by this same argument — it cannot have zero momentum if it has nonzero energy. Three or more photons are allowed but extremely rare. The back-to-back geometry is pure momentum conservation, which is what PET imaging exploits for precise three-dimensional localization."

- question: "An electron and positron annihilating at rest could produce a single photon carrying 1.022 MeV, since this conserves total energy."
  type: true-false
  answer: false
  explanation: "Energy is conserved in this hypothetical, but momentum is not. In the center-of-mass frame, the electron-positron system has zero total momentum. A single photon must carry momentum p = E/c ≠ 0 (since E = 1.022 MeV > 0). The final state (one photon) has nonzero momentum while the initial state has zero total momentum — a violation. Two photons traveling in opposite directions can each carry 0.511 MeV and have their momenta cancel, satisfying both conservation laws. Single-photon annihilation is kinematically forbidden by the same argument as single-photon pair production."

- question: "The positron is the antiparticle of the electron, having the same mass but opposite electric charge."
  type: true-false
  answer: true
  explanation: "The positron has the same mass as the electron (m_e ≈ 9.11 × 10⁻³¹ kg) and the same magnitude of charge (e ≈ 1.6 × 10⁻¹⁹ C) but positive charge rather than negative. This is the defining relationship between a particle and its antiparticle: identical mass, opposite charges (electric and otherwise). When they meet, all rest mass converts entirely to photon energy — 2m_e c² ≈ 1.022 MeV — making annihilation the most complete form of mass-energy conversion possible."

- question: "Why does pair production require a nearby nucleus, even when the incoming photon has more than sufficient energy to create the electron-positron pair?"
  type: short-answer
  answer: "Both energy AND momentum must be conserved simultaneously. A photon has E = pc, so its momentum is p = E/c. An electron-positron pair created at rest has total energy 2m_e c² but zero total momentum. A photon with E = 2m_e c² therefore has momentum p = 2m_e c ≠ 0 — it cannot produce a pair with zero total momentum. This is a kinematic impossibility independent of the photon's energy: even with 100 MeV, a single photon in free space cannot pair-produce. A nearby nucleus resolves this by absorbing the recoil momentum: it moves very slowly (its large mass means it takes little energy), allowing the energy and momentum ledgers to balance simultaneously. The nucleus is a silent participant — it is not consumed, but its presence is required."
  explanation: "The distinction between 'insufficient energy' and 'kinematic impossibility' is the key insight. No amount of energy makes single-photon pair production in free space possible. The nucleus is not a threshold requirement but a structural necessity arising from the simultaneous requirements of two conservation laws."
```

## Explainer

From your study of mass-energy equivalence and the photon model, you know that E = mc² says energy and mass are interconvertible, and that photons carry energy E = hf. **Pair production** is the process that makes this conversion literal: a high-energy photon vanishes and in its place two particles materialize — an electron and its antiparticle, the **positron**. Each has rest-mass energy m_e c² ≈ 0.511 MeV, so the photon must supply at least 2m_e c² ≈ 1.022 MeV just to create the particles at rest, with any excess appearing as kinetic energy.

Why can a single photon not produce a pair in free space? Apply conservation of energy and momentum simultaneously. A photon has E = pc (massless), while the electron-positron pair at rest has E = 2m_e c² and p = 0. You cannot satisfy both E = 2m_e c² and p = 0 with a single photon (which requires E = pc ≠ 0 if E > 0). The numbers simply do not balance — it is a kinematic impossibility, not a matter of energy being insufficient. The way out is a **nucleus nearby**: the nucleus can absorb recoil momentum without taking much energy (its large mass means it moves very slowly), allowing the energy and momentum ledgers to balance simultaneously. The nucleus is a silent participant that enables the reaction without being consumed.

The reverse process, **annihilation**, occurs when an electron and positron meet. They convert entirely into radiation — typically two photons, each carrying exactly 0.511 MeV, emitted in exactly opposite directions. The back-to-back emission follows directly from momentum conservation: in the center-of-mass frame (where the total three-momentum is zero), the final state must also have zero total momentum, which requires two photons of equal energy traveling in opposite directions. A single-photon annihilation is forbidden by the same kinematic argument as single-photon pair production. (Three-photon annihilation is allowed but occurs with much lower probability.)

These processes illustrate antimatter as a genuine physical reality, not a theoretical abstraction. Every particle has a corresponding antiparticle with the same mass but opposite charges. When matter meets antimatter, the rest mass converts entirely to photon energy — the most complete form of mass-energy conversion possible. In medicine, **PET scanning** (Positron Emission Tomography) exploits annihilation directly: a radioactive tracer emits positrons that immediately annihilate with nearby electrons, producing back-to-back 0.511 MeV gamma-ray pairs. Detecting both photons in coincidence locates the annihilation event in three dimensions, revealing metabolically active tissue with millimeter precision.
