---
id: rotational-spectroscopy-quantum-theory
title: Quantum Rotational Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rigid-rotor-model
  type: hard
- id: rotational-spectroscopy
  type: soft
builds-toward:
- vibrational-overtones-and-transitions
tags:
- spectroscopy
- rotation
- quantum
- energy-levels
stage: advanced
status: draft
---

# Quantum Rotational Spectroscopy

## Core Idea
Rigid rotor quantum mechanics yields rotational energy levels E_J = BJ(J+1), where B is the rotational constant and J is the quantum number. Microwave spectroscopy probes rotational transitions (ΔJ = ±1), revealing bond lengths and moments of inertia with high precision. Centrifugal distortion, nuclear spin coupling, and asymmetry further refine this model for real molecules.

## How It's Best Learned
Derive the rigid rotor Schrödinger equation in spherical coordinates; calculate rotational constants from bond lengths for CO and HCl; compare quantum predictions with experimental microwave spectra; estimate rotational level populations at different temperatures.

## Common Misconceptions
- Assuming all rotational levels are equally populated at room temperature; in reality only low-J states are significantly occupied (Boltzmann weighting). - Confusing rotational constant B (in cm⁻¹) with moment of inertia I; they are inversely related (B ∝ 1/I).

## Explainer

From the rigid rotor model, you already know that a diatomic molecule rotating in free space has its angular momentum quantized — only certain discrete rotational energies are allowed. Quantum rotational spectroscopy takes this mathematical result and connects it to what we can actually measure in the laboratory. The energy levels are given by **E_J = BJ(J+1)**, where J is the rotational quantum number (0, 1, 2, ...) and **B** is the **rotational constant**, a single number that encodes the molecule's moment of inertia. Because B = ℏ²/(2I) and the moment of inertia I depends on bond length and atomic masses, measuring B from a spectrum lets you calculate the bond length to extraordinary precision — often to fractions of a picometer.

The **selection rule** ΔJ = ±1 means that rotational transitions produce a beautifully simple spectrum: a series of equally spaced absorption lines in the microwave region, each separated by 2B. For carbon monoxide, this spacing is about 3.86 cm⁻¹, giving a rotational constant B ≈ 1.93 cm⁻¹ and a bond length of 1.128 Å. The pattern is so regular that identifying a molecule from its pure rotational spectrum is like reading a fingerprint. If you see evenly spaced lines in the microwave, you immediately know you are looking at a rigid diatomic or linear molecule, and the spacing tells you exactly which one.

Real molecules are not perfectly rigid, however. As J increases, the molecule spins faster, centrifugal force stretches the bond slightly, and the moment of inertia increases. This **centrifugal distortion** causes the line spacing to decrease gradually at higher J values. The correction is captured by adding a term −DJ²(J+1)² to the energy expression, where **D** is the centrifugal distortion constant (typically much smaller than B). For polyatomic molecules, the picture grows richer: **symmetric tops** have two rotational constants (B and A or C), **asymmetric tops** have three, and **spherical tops** like methane have just one but show no pure rotational spectrum because they lack a permanent dipole moment — a requirement for microwave absorption.

Temperature plays a critical role in what you actually observe. The population of each rotational level follows the **Boltzmann distribution**, weighted by the degeneracy factor (2J+1). At room temperature, many rotational levels are populated, producing a rich spectrum with an intensity envelope that peaks at an intermediate J value — not at J = 0. This peak shifts to higher J at higher temperatures. Understanding this population distribution is essential for interpreting spectral intensities and for using rotational spectroscopy as a thermometer in environments like interstellar gas clouds, where rotational line intensities reveal the temperature of molecular hydrogen and other species.
