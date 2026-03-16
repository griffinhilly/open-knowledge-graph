---
id: gamma-decay-emission
title: Gamma Decay and Photon Emission from Nuclei
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-mass-binding-energy
  type: hard
- id: photon-concept-quanta
  type: hard
builds-toward:
- decay-constant-half-life-exponential
tags:
- nuclear
- radioactivity
- photons
stage: abstract-reasoning
status: draft
---

# Gamma Decay and Photon Emission from Nuclei

## Core Idea
Gamma decay is the emission of a high-energy photon from an excited nucleus without changing Z or A. The nucleus transitions between energy levels, releasing the excess energy as a photon. Gamma rays are typically produced following alpha or beta decay when the daughter nucleus is left in an excited state. Gamma decay is electromagnetically mediated and does not change nuclear composition.

## Explainer

You already know from the photon concept that when a quantum system transitions between discrete energy levels, it emits a photon whose energy equals the energy difference: E_photon = hν = E_upper − E_lower. In atomic physics, these transitions involve electron energy levels and produce visible light or UV/X-ray photons with energies from a few eV to tens of keV. Nuclei have an exactly analogous level structure, but the energy scale is vastly higher — nuclear excited states typically lie hundreds of keV to several MeV above the ground state. The photons emitted in nuclear de-excitation are therefore **gamma rays**, distinguished from X-rays not by their physical nature (both are photons) but by their origin and energy range.

The mechanism is the same as atomic emission. After an alpha or beta decay, the daughter nucleus is often produced in an excited state — a configuration of nucleons that is not the lowest available energy arrangement. The nucleus then de-excites on a timescale that can range from femtoseconds to years, emitting one or more gamma-ray photons. The nucleus after gamma emission has the same Z and A as before (no protons or neutrons are emitted), but its internal energy and nuclear spin may change. Because nuclear energy levels are quantized, the emitted gamma-ray photons have sharply defined energies, forming a **discrete spectrum** characteristic of the specific nucleus — just as optical spectra fingerprint atoms, gamma spectra fingerprint nuclides.

The binding energy you know from nuclear mass-energy calculations is directly relevant: the mass of the excited nucleus equals the mass of the ground-state nucleus plus E_excited/c², and the emitted gamma carries away that excess mass-energy. Because the nucleus must also recoil to conserve momentum, the gamma energy is very slightly less than the level spacing by the **nuclear recoil correction** ΔE = E_γ²/(2Mc²). For heavy nuclei this correction is tiny and negligible in most contexts, but it becomes important in the **Mössbauer effect**, where nuclei embedded in a crystal recoil collectively as a solid rather than individually, dramatically reducing the recoil energy and allowing resonant absorption of gamma rays — the basis for precision spectroscopy and tests of general relativity.

Gamma decay competes with a process called **internal conversion**: instead of emitting a photon, the excited nucleus can transfer its energy directly to an inner-shell electron, ejecting it from the atom. The ratio of internal conversion to gamma emission depends on the nuclear transition type (electric or magnetic multipole) and the nuclear charge Z. Internal conversion is more likely for low-energy transitions in heavy nuclei. Both processes leave Z and A unchanged. Gamma spectroscopy — measuring the energies of emitted gamma photons from radioactive sources — is one of the primary tools in nuclear physics for mapping nuclear energy level structure, in medical imaging (gamma cameras in nuclear medicine), and in security applications for identifying radioisotopes.

