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
stage: advanced
status: draft
---

# Radiation Directivity and Antenna Patterns

## Core Idea
Radiation patterns describe the angular distribution of radiated power. Directivity D characterizes the ratio of power radiated in the peak direction to isotropic radiation at the same total power. Antenna gain includes efficiency factors; narrow patterns emerge from coherent sources separated by wavelengths.

## Explainer

From your study of the far-field radiation limit, you know that an oscillating charge distribution radiates power into the surrounding space, and in the far field the radiation looks locally like a plane wave propagating outward. But not all directions receive equal power. A single oscillating electric dipole, for instance, radiates with a sin²θ angular dependence — sending most of its power sideways (perpendicular to the dipole axis) and none along the axis. The **radiation pattern** is just the map of this angular power distribution: a polar plot of the power radiated per unit solid angle, dP/dΩ, as a function of direction (θ, φ).

**Directivity** D converts the radiation pattern into a single figure of merit. It is defined as D(θ,φ) = (dP/dΩ) / (P_total/4π), where the denominator is the power per steradian of a hypothetical **isotropic radiator** — one that spreads its power perfectly uniformly in all directions. D(θ,φ) = 1 everywhere for an isotropic antenna; D > 1 in directions where the antenna concentrates power above the isotropic baseline. The peak directivity is what engineers usually report: a value of 10 means the antenna sends 10× more power per steradian in its best direction than the same total power spread isotropically. Directivity is purely geometric — it describes the shape of the pattern, not the efficiency of the antenna.

**Gain** G = η · D incorporates the antenna's radiation efficiency η ≤ 1, which accounts for ohmic losses in the conductors and other dissipation mechanisms. A perfectly efficient antenna (η = 1) has G = D; a lossy antenna has G < D even if its pattern shape is unchanged. Gain is measured relative to an isotropic reference (expressed in dBi — decibels relative to isotropic) and directly sets how much power reaches a receiver at a given distance for a given transmitted power. This is the key link between antenna theory and the Friis transmission equation used in link budgets.

The mechanism for achieving high directivity is **coherent interference**: multiple current elements separated by distances comparable to the wavelength interfere constructively in some directions and destructively in others. A single short dipole has modest directivity (~1.5); an array of many dipoles fed with controlled phase delays can produce a very narrow beam (high directivity) pointed in any desired direction. The tradeoff is fundamental — the solid angle of the main beam Ω_beam ≈ 4π/D, so higher directivity means a narrower beam and a smaller field of view. Long apertures (dish antennas, antenna arrays) create narrow beams because the path-length difference from one edge to the other is large, making the constructive interference condition sensitive to direction. This is the same physics as optical diffraction: a wider aperture diffracts light into a narrower central lobe, and the product of aperture size and beam angle is set by the wavelength.
