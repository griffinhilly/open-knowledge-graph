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
status: draft
---

# Pair Production and Annihilation Thresholds

## Core Idea
Pair creation and annihilation are governed by energy-momentum conservation. A photon must have energy at least 2mc² to create an electron-positron pair; at threshold, the pair is created at rest. Conversely, electron-positron annihilation produces photons whose energy and momentum satisfy conservation laws, with minimum 1.022 MeV needed per pair.

## How It's Best Learned
Use four-momentum conservation to derive threshold energy for pair production by a high-energy photon. Calculate photon frequencies in annihilation for different initial momentum configurations.

## Common Misconceptions
A single photon cannot create a pair and conserve both energy and momentum simultaneously (a nucleus is needed to absorb recoil). The threshold energy is not simply 2mc² in the lab frame if the incident photon has momentum.

## Explainer

From your study of four-momentum you know that every particle carries a four-momentum pᵘ = (E/c, **p**), and the invariant mass is defined by pᵘpᵤ = (E/c)² − |**p**|² = (mc)². This invariant mass-squared is the same in every inertial frame, which makes it the most powerful tool for threshold calculations. For a photon, m = 0, so E = pc exactly.

Consider **pair production**: a high-energy photon converts into an electron-positron pair (γ → e⁺ + e⁻). To find the minimum photon energy needed, you must simultaneously conserve both energy and momentum. In the lab frame the nucleus is at rest and the photon carries momentum, so the created pair cannot simply be at rest — the total momentum of the system before the reaction is the photon's momentum, and that must equal the momentum of the products. The threshold condition is met when all the collision energy goes into rest-mass creation, with the products moving together in the center-of-mass frame. The invariant technique: the four-momentum of the initial state is pᵘ_γ + pᵘ_nucleus. At threshold, the final state has minimum invariant mass squared equal to (2mₑ + M)²c², where M is the nucleus mass. In practice the nucleus is so heavy it recoils negligibly, and the threshold photon energy in the lab frame works out to be just above 2mₑc² = 1.022 MeV for the electron-positron pair.

Why can a single photon not create a pair without the nucleus? Suppose γ → e⁺ + e⁻ in vacuum with no other particles present. The initial four-momentum squared is (E/c)² − (E/c)² = 0 (since E = pc for a photon). The final state invariant mass squared is at least (2mₑ)²c². These cannot be equal: zero ≠ (2mₑ)²c². Four-momentum conservation is violated regardless of how much energy the photon has. The nucleus supplies the missing momentum: it absorbs the vector recoil while scarcely changing its energy (because it is so heavy), allowing the total invariant mass of the created pair to equal 2mₑc².

**Pair annihilation** (e⁺ + e⁻ → 2γ) is the time-reverse. Two photons are required — not one — for the same reason: a single photon in the final state would have zero invariant mass squared, but the initial electron-positron pair has invariant mass at least 2mₑ. The two-photon final state is back-to-back in the center-of-mass frame (to conserve momentum), each carrying energy mₑc² = 0.511 MeV when the pair annihilates at rest. If the pair has kinetic energy before annihilation, the photons are Doppler-shifted and no longer exactly equal in energy in the lab frame — this is used in **positron emission tomography (PET)** to locate the annihilation site from the slight energy asymmetry and time-of-flight difference between the two 511 keV gamma rays.
