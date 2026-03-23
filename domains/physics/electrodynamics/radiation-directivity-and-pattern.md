---
id: radiation-directivity-and-pattern
title: Radiation Directivity and Antenna Patterns
domain: physics
course: electrodynamics
prerequisites:
- id: far-field-radiation-limit
  type: hard
- id: higher-multipole-radiation
  type: soft
tags:
- radiation-pattern
- directivity
- antenna-gain
- beamwidth
stage: expert
status: draft
---

# Radiation Directivity and Antenna Patterns

## Core Idea
Radiation patterns describe the angular distribution of radiated power. Directivity D characterizes the ratio of power radiated in the peak direction to isotropic radiation at the same total power. Antenna gain includes efficiency factors; narrow patterns emerge from coherent sources separated by wavelengths.

## Questions

```yaml
- question: "Antenna X has directivity D = 20 and radiation efficiency η = 0.5. Antenna Y has directivity D = 10 and radiation efficiency η = 1.0. Which has greater gain?"
  type: multiple-choice
  options:
    - "Antenna X, because its directivity is twice as high"
    - "They have equal gain — G_X = 0.5 × 20 = 10 and G_Y = 1.0 × 10 = 10"
    - "Antenna Y, because perfect efficiency always wins"
    - "Cannot be determined without knowing the operating frequency"
  answer: 1
  explanation: "Gain G = ηD. For Antenna X: G = 0.5 × 20 = 10. For Antenna Y: G = 1.0 × 10 = 10. They are equal. This illustrates the key distinction: directivity is purely geometric (the shape of the radiation pattern relative to isotropic), while gain incorporates ohmic losses. A highly directive but lossy antenna can deliver the same on-axis power as a less directive but efficient one. Engineers use gain (not directivity) to compute link budgets via the Friis equation."

- question: "An antenna's peak directivity is doubled from D = 10 to D = 20. What happens to the solid angle of its main beam?"
  type: multiple-choice
  options:
    - "It doubles — more directivity means power spreads over a larger solid angle"
    - "It stays the same — directivity and beam solid angle are independent"
    - "It is halved — the beam narrows as directivity increases, since Ω_beam ≈ 4π/D"
    - "It is quartered — the relationship between directivity and beam angle is quadratic"
  answer: 2
  explanation: "The tradeoff is fundamental: Ω_beam ≈ 4π/D. Total radiated power is fixed; concentrating more of it in one direction (higher D) necessarily means a smaller solid angle receives that peak power density. Doubling D halves the beam solid angle. This is the antenna analog of optical diffraction: a wider aperture produces a narrower diffraction lobe. There is no way to have both high directivity and a wide field of view simultaneously."

- question: "An isotropic radiator has directivity D = 1 in every direction."
  type: true-false
  answer: true
  explanation: "Directivity is defined as D(θ,φ) = (dP/dΩ) / (P_total/4π) — the ratio of actual power per steradian in a given direction to what an isotropic radiator would produce at the same total power. By definition, an isotropic antenna distributes power uniformly, so this ratio equals 1 everywhere. D = 1 is the baseline; any real antenna with a non-uniform pattern has D > 1 in its peak direction and D < 1 elsewhere, with the average over the sphere always equal to 1."

- question: "A highly directive antenna with D = 100 necessarily has higher gain than an antenna with D = 5, regardless of their radiation efficiencies."
  type: true-false
  answer: false
  explanation: "Gain G = ηD, so efficiency matters. An antenna with D = 100 and η = 0.01 has gain G = 1, far below an antenna with D = 5 and η = 0.9, which has G = 4.5. A directive but lossy antenna (e.g., a long wire with significant ohmic resistance) can actually deliver less power to a receiver than a simple but efficient dipole. This is why gain — not directivity — is the relevant figure for system-level link budgets."

- question: "Why does increasing directivity necessarily result in a narrower main beam, and what physical mechanism creates high-directivity radiation patterns?"
  type: short-answer
  answer: "Higher directivity means more power concentrated into a smaller solid angle, because total radiated power is conserved — Ω_beam ≈ 4π/D shrinks as D grows. Physically, high directivity arises from coherent interference among multiple current-carrying elements separated by distances comparable to the wavelength. The phase of radiation from each element depends on direction; constructive interference in the desired direction requires phases to align, which is increasingly sensitive to angle as more elements (or larger aperture) are added, creating destructive interference in all other directions. This is the same physics as diffraction from a wide aperture producing a narrow central lobe."
  explanation: "The fundamental limit is Fourier-dual: large aperture ↔ narrow angular spectrum, small aperture ↔ wide angular spread. An aperture of size L at wavelength λ produces a main lobe of angular width ~ λ/L. Equivalently, high directivity requires spatial coherence across a large effective aperture. Dish antennas and phased arrays exploit this by controlling the current distribution across a physical aperture; the antenna pattern is essentially the Fourier transform of the aperture current distribution."
```

## Explainer

From your study of the far-field radiation limit, you know that an oscillating charge distribution radiates power into the surrounding space, and in the far field the radiation looks locally like a plane wave propagating outward. But not all directions receive equal power. A single oscillating electric dipole, for instance, radiates with a sin²θ angular dependence — sending most of its power sideways (perpendicular to the dipole axis) and none along the axis. The **radiation pattern** is just the map of this angular power distribution: a polar plot of the power radiated per unit solid angle, dP/dΩ, as a function of direction (θ, φ).

**Directivity** D converts the radiation pattern into a single figure of merit. It is defined as D(θ,φ) = (dP/dΩ) / (P_total/4π), where the denominator is the power per steradian of a hypothetical **isotropic radiator** — one that spreads its power perfectly uniformly in all directions. D(θ,φ) = 1 everywhere for an isotropic antenna; D > 1 in directions where the antenna concentrates power above the isotropic baseline. The peak directivity is what engineers usually report: a value of 10 means the antenna sends 10× more power per steradian in its best direction than the same total power spread isotropically. Directivity is purely geometric — it describes the shape of the pattern, not the efficiency of the antenna.

**Gain** G = η · D incorporates the antenna's radiation efficiency η ≤ 1, which accounts for ohmic losses in the conductors and other dissipation mechanisms. A perfectly efficient antenna (η = 1) has G = D; a lossy antenna has G < D even if its pattern shape is unchanged. Gain is measured relative to an isotropic reference (expressed in dBi — decibels relative to isotropic) and directly sets how much power reaches a receiver at a given distance for a given transmitted power. This is the key link between antenna theory and the Friis transmission equation used in link budgets.

The mechanism for achieving high directivity is **coherent interference**: multiple current elements separated by distances comparable to the wavelength interfere constructively in some directions and destructively in others. A single short dipole has modest directivity (~1.5); an array of many dipoles fed with controlled phase delays can produce a very narrow beam (high directivity) pointed in any desired direction. The tradeoff is fundamental — the solid angle of the main beam Ω_beam ≈ 4π/D, so higher directivity means a narrower beam and a smaller field of view. Long apertures (dish antennas, antenna arrays) create narrow beams because the path-length difference from one edge to the other is large, making the constructive interference condition sensitive to direction. This is the same physics as optical diffraction: a wider aperture diffracts light into a narrower central lobe, and the product of aperture size and beam angle is set by the wavelength.
