---
id: fluorescence-spectroscopy
title: Fluorescence Spectroscopy
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: uv-vis-spectroscopy-analytical
  type: hard
- id: electronic-spectroscopy-theory
  type: soft
- id: photon-model
  type: soft
- id: quantum-mechanics-postulates-core
  type: soft
- id: electronic-transitions-excited-states
  type: soft
tags:
- fluorescence
- phosphorescence
- Jablonski diagram
- quantum yield
- fluorimetry
stage: advanced
status: validated
---

# Fluorescence Spectroscopy

## Core Idea
Fluorescence occurs when a molecule absorbs a photon, reaches an excited singlet state, and emits a lower-energy photon upon returning to the ground state — typically within nanoseconds. The Jablonski diagram maps these energy transitions and distinguishes fluorescence from phosphorescence (which involves intersystem crossing to a triplet state). Fluorimetry is often 100–1000× more sensitive than absorption spectrophotometry because signal is measured against a dark background. Quantum yield, excitation spectrum, and emission spectrum are the key analytical parameters.

## How It's Best Learned
Compare the detection limits of quinine sulfate measured by UV–Vis absorption and by fluorimetry. Investigating quenching mechanisms (inner filter effect, collisional quenching, FRET) builds a practical understanding of interferences unique to fluorescence methods.

## Common Misconceptions
- The excitation spectrum (scanning excitation wavelength while monitoring emission) should resemble the absorption spectrum, not the emission spectrum.
- Inner filter effect causes non-linearity at high concentrations, which is often mistaken for instrument malfunction.

## Explainer

Your understanding of UV-Vis spectroscopy already gives you the foundation: molecules absorb photons at specific wavelengths, promoting electrons from a ground state to an excited state. In absorption spectroscopy, you measure how much light is removed from a beam. **Fluorescence spectroscopy** takes a fundamentally different approach — it measures the light that the molecule emits after absorption. This distinction has a profound consequence for sensitivity: absorption measures a small decrease in a large signal (like noticing one person leaving a packed stadium), while fluorescence detects photons against an essentially dark background (like spotting a single flashlight in a dark field). This is why fluorescence can be 100 to 1000 times more sensitive than absorption for the same analyte.

The physics of fluorescence is best understood through the **Jablonski diagram**, which maps the energy levels and transitions involved. When a molecule absorbs a photon, it jumps to a vibrationally excited level of an upper electronic state. Within picoseconds, vibrational relaxation dissipates some of that energy as heat, dropping the molecule to the lowest vibrational level of the excited state. From there, it can return to the ground state by emitting a photon — this emission is fluorescence. Because energy was lost to vibrational relaxation before emission, the emitted photon always has less energy (longer wavelength) than the absorbed photon. This wavelength difference is the **Stokes shift**, and it is what makes fluorescence measurements practical: you can use optical filters to separate excitation light from emission light, ensuring that only fluorescence reaches the detector.

Not every molecule that absorbs light will fluoresce. The **quantum yield** — the ratio of photons emitted to photons absorbed — depends on the competition between fluorescence and non-radiative pathways like internal conversion, intersystem crossing to triplet states, and collisional quenching. Rigid, planar aromatic molecules (like quinine, fluorescein, and rhodamine) tend to have high quantum yields because their rigid structures limit the molecular vibrations that would otherwise dissipate energy non-radiatively. This is also why fluorescence intensity often increases when temperature decreases or when the molecule is immobilized in a rigid matrix — fewer molecular motions means less energy lost to heat.

The analytical instrument — a **fluorimeter** or spectrofluorometer — has a distinctive right-angle geometry: the excitation beam enters the sample from one direction, and the detector is positioned at 90° to minimize the amount of excitation light reaching it. Two monochromators (or filter sets) are used — one to select the excitation wavelength and one to select the emission wavelength. This dual-wavelength selectivity gives fluorescence a significant advantage in complex mixtures: even if two compounds absorb at the same wavelength, they may emit at different wavelengths, allowing selective detection. However, at high concentrations the **inner filter effect** causes problems — the sample absorbs so much excitation light that molecules deep in the cuvette receive little excitation, and emitted fluorescence is reabsorbed before reaching the detector, causing the calibration curve to plateau and eventually decrease. Working in the dilute regime (absorbance below 0.05) avoids this artifact.
