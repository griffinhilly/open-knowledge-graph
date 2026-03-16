---
id: nuclear-magnetic-moments
title: Nuclear Magnetic Moments and Hyperfine Structure
domain: physics
course: modern-physics
prerequisites:
- id: spin-angular-momentum
  type: hard
- id: nuclear-structure
  type: soft
builds-toward:
- gamma-emission-nuclear-transitions
tags:
- nuclear-physics
- atomic-physics
stage: advanced
status: draft
---

# Nuclear Magnetic Moments and Hyperfine Structure

## Core Idea
Many nuclei possess intrinsic angular momentum (spin) and associated magnetic moments, analogous to electron spin but typically 1000× smaller. The nuclear magnetic moment creates a magnetic field that interacts weakly with the electron's magnetic field, causing hyperfine splitting: energy level doublets observable as closely spaced lines in atomic spectra. Hyperfine splitting is used to measure nuclear spins and moments, with applications in atomic clocks and NMR spectroscopy.

## Explainer

From your study of spin angular momentum, you know that an electron carries intrinsic spin s = 1/2 and an associated magnetic moment μₑ = −gₑμ_B·S/ħ, where μ_B = eħ/(2mₑ) is the Bohr magneton. This magnetic moment interacts with external fields and with internal orbital magnetic fields, producing fine structure in atomic energy levels. The nucleus follows the same logic — but with important differences that profoundly affect the scale of the effects.

Protons and neutrons are also spin-1/2 particles, and nuclei with odd numbers of protons and/or neutrons have a net nuclear spin I (which can be half-integer or integer depending on the nuclear composition). Each such nucleus carries a **nuclear magnetic moment** μ_N = g_N·μ_N·I/ħ, where μ_N = eħ/(2m_p) is the **nuclear magneton** — identical in form to the Bohr magneton but with the proton mass m_p ≈ 1836 mₑ replacing the electron mass. Because m_p is 1836 times larger, the nuclear magneton is 1836 times *smaller* than the Bohr magneton. This is why nuclear magnetic effects are about three orders of magnitude weaker than electronic ones.

The nuclear magnetic moment creates a tiny magnetic field at the site of the electrons. This field interacts with the magnetic moment of the outermost electrons — specifically their spin and orbital magnetic moments — coupling the nuclear spin I to the total electron angular momentum J. The total atomic angular momentum becomes F = I + J, and the interaction energy splits each electronic energy level into 2·min(I, J) + 1 **hyperfine levels**, closely spaced in energy. These produce the **hyperfine structure** of atomic spectra: lines that appear single at low resolution but reveal closely spaced doublets or multiplets under high-resolution spectroscopy. The energy splittings are typically in the microwave to radio-frequency range (MHz to GHz), far below optical frequencies.

The most famous hyperfine transition is the 21-centimeter hydrogen line: the ground state of hydrogen (n = 1, l = 0, j = 1/2) splits into F = 1 and F = 0 levels separated by 1420 MHz, corresponding to a wavelength of 21 cm. This transition is astrophysically important for mapping hydrogen in galaxies. More practically, the **cesium atomic clock** uses the hyperfine transition in cesium-133 (I = 7/2) at 9.19 GHz as the definition of the second. **NMR spectroscopy** exploits the fact that different nuclear environments (different surrounding molecules) slightly shift the energy of nuclear magnetic transitions — the "chemical shift" — allowing chemists to infer molecular structure from the NMR spectrum. In all these applications, the tiny nuclear magnetic moment, negligible in most atomic physics, becomes the precision probe of choice precisely because its small size makes it sensitive to subtle environmental perturbations.
