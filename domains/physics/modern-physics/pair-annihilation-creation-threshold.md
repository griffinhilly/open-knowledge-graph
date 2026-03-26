---
id: pair-annihilation-creation-threshold
title: Pair Production and Annihilation Thresholds
domain: physics
course: modern-physics
prerequisites:
- id: four-momentum-energy-conservation
  type: hard
- id: pair-production-annihilation
  type: soft
tags:
- quantum-field-theory
- particle-physics
- energy-momentum
stage: advanced
status: validated
---

# Pair Production and Annihilation Thresholds

## Core Idea
Pair creation and annihilation are governed by energy-momentum conservation. A photon must have energy at least 2mc² to create an electron-positron pair; at threshold, the pair is created at rest. Conversely, electron-positron annihilation produces photons whose energy and momentum satisfy conservation laws, with minimum 1.022 MeV needed per pair.

## How It's Best Learned
Use four-momentum conservation to derive threshold energy for pair production by a high-energy photon. Calculate photon frequencies in annihilation for different initial momentum configurations.

## Common Misconceptions
A single photon cannot create a pair and conserve both energy and momentum simultaneously (a nucleus is needed to absorb recoil). The threshold energy is not simply 2mc² in the lab frame if the incident photon has momentum.

## Questions

```yaml
- question: "A photon with energy 5 MeV (well above the 1.022 MeV threshold) travels through empty space with no nearby matter. Can it spontaneously create an electron-positron pair?"
  type: multiple-choice
  options:
    - "Yes — it has more than enough energy to supply the rest masses of both particles"
    - "No — a single photon has zero invariant mass squared, but the minimum invariant mass of an electron-positron pair is nonzero; four-momentum conservation cannot be satisfied regardless of photon energy"
    - "No — only photons above 10 MeV can create pairs in vacuum"
    - "Yes, but only if the photon's spin angular momentum equals the pair's combined spin"
  answer: 1
  explanation: "The constraint is not just energy but four-momentum conservation. A photon's invariant mass squared is pᵘpᵤ = (E/c)² − |p|² = 0 (since E = pc for photons). An electron-positron pair has minimum invariant mass squared (2mₑc)² ≠ 0. These cannot be equal, regardless of how large the photon energy is. Energy alone is insufficient; the invariant mass is a Lorentz scalar that must match in initial and final states. This is why a nucleus is required — it changes the total invariant mass of the initial system."

- question: "When an electron-positron pair annihilates at rest, what is the minimum number of photons produced and why?"
  type: multiple-choice
  options:
    - "One — a single photon with energy 1.022 MeV carries away all the rest-mass energy"
    - "Two — one photon would have zero invariant mass squared, but the initial pair has nonzero invariant mass; two back-to-back photons can satisfy four-momentum conservation"
    - "Three — conservation of spin requires three photons in the final state"
    - "Four — two photons from each particle separately"
  answer: 1
  explanation: "A single final-state photon would have invariant mass squared = 0, but the initial e⁺e⁻ pair at rest has invariant mass = 2mₑ ≠ 0 — same invariant mass argument as pair production, run in reverse. Two back-to-back photons (in the CM frame) can have zero total invariant mass when they carry equal and opposite momenta, while their energies sum to 2mₑc² = 1.022 MeV. The 511 keV gamma pairs are the signature used in PET imaging."

- question: "A photon with energy greater than 1.022 MeV can create an electron-positron pair without any nearby nucleus, provided its energy exceeds the threshold."
  type: true-false
  answer: false
  explanation: "This is the key misconception. The energy threshold 1.022 MeV is necessary but not sufficient for pair production by a single photon. A photon in vacuum always has zero invariant mass squared, while any electron-positron pair has positive invariant mass squared. Four-momentum conservation is violated for single-photon pair production regardless of photon energy. A nucleus (or other particle to absorb recoil) is always required to provide the additional four-momentum that reconciles the invariant masses."

- question: "In positron emission tomography (PET), the two annihilation gamma rays usually have exactly equal energies in the lab frame when detected by the scanner."
  type: true-false
  answer: false
  explanation: "When the positron has kinetic energy before annihilation (as it does in PET — it is emitted with some energy from beta decay), the center-of-mass frame is not at rest in the lab. The two 511 keV photons are back-to-back in the CM frame but are Doppler-shifted in the lab, so they arrive with slightly different energies and a small time-of-flight difference. It is precisely this asymmetry that allows PET scanners to localize the annihilation site along the line of response."

- question: "Why must a nucleus be present for pair production by a photon, given that the nucleus contributes negligible energy to the reaction?"
  type: short-answer
  answer: "The nucleus is needed to absorb vector recoil momentum, not energy. A photon has invariant mass squared p² = (E/c)² − |p|² = 0. An electron-positron pair has minimum invariant mass squared (2mₑc)². Since invariant mass is a Lorentz scalar conserved in reactions, a single photon cannot produce a pair — the invariant masses can never match. The nucleus adds its own four-momentum to the initial state, raising the total invariant mass to accommodate the pair. Because the nucleus is so heavy, it absorbs the momentum kick with negligible kinetic energy, so the photon's energy is almost entirely available for rest-mass creation."
  explanation: "This is a fundamental application of four-momentum invariants to threshold problems. The key insight is that energy conservation alone is insufficient — invariant mass conservation (a frame-independent constraint) rules out single-photon pair production absolutely, not just at low energies."
```

## Explainer

From your study of four-momentum you know that every particle carries a four-momentum pᵘ = (E/c, **p**), and the invariant mass is defined by pᵘpᵤ = (E/c)² − |**p**|² = (mc)². This invariant mass-squared is the same in every inertial frame, which makes it the most powerful tool for threshold calculations. For a photon, m = 0, so E = pc exactly.

Consider **pair production**: a high-energy photon converts into an electron-positron pair (γ → e⁺ + e⁻). To find the minimum photon energy needed, you must simultaneously conserve both energy and momentum. In the lab frame the nucleus is at rest and the photon carries momentum, so the created pair cannot simply be at rest — the total momentum of the system before the reaction is the photon's momentum, and that must equal the momentum of the products. The threshold condition is met when all the collision energy goes into rest-mass creation, with the products moving together in the center-of-mass frame. The invariant technique: the four-momentum of the initial state is pᵘ_γ + pᵘ_nucleus. At threshold, the final state has minimum invariant mass squared equal to (2mₑ + M)²c², where M is the nucleus mass. In practice the nucleus is so heavy it recoils negligibly, and the threshold photon energy in the lab frame works out to be just above 2mₑc² = 1.022 MeV for the electron-positron pair.

Why can a single photon not create a pair without the nucleus? Suppose γ → e⁺ + e⁻ in vacuum with no other particles present. The initial four-momentum squared is (E/c)² − (E/c)² = 0 (since E = pc for a photon). The final state invariant mass squared is at least (2mₑ)²c². These cannot be equal: zero ≠ (2mₑ)²c². Four-momentum conservation is violated regardless of how much energy the photon has. The nucleus supplies the missing momentum: it absorbs the vector recoil while scarcely changing its energy (because it is so heavy), allowing the total invariant mass of the created pair to equal 2mₑc².

**Pair annihilation** (e⁺ + e⁻ → 2γ) is the time-reverse. Two photons are required — not one — for the same reason: a single photon in the final state would have zero invariant mass squared, but the initial electron-positron pair has invariant mass at least 2mₑ. The two-photon final state is back-to-back in the center-of-mass frame (to conserve momentum), each carrying energy mₑc² = 0.511 MeV when the pair annihilates at rest. If the pair has kinetic energy before annihilation, the photons are Doppler-shifted and no longer exactly equal in energy in the lab frame — this is used in **positron emission tomography (PET)** to locate the annihilation site from the slight energy asymmetry and time-of-flight difference between the two 511 keV gamma rays.
