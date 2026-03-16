---
id: thermal-conductivity-coefficient
title: Thermal Conductivity and Material Properties
domain: physics
course: thermodynamics
prerequisites:
- id: heat-transfer-conduction-fourier
  type: hard
tags:
- thermal-properties
- materials
- conductivity
stage: formal-systems
status: draft
---

# Thermal Conductivity and Material Properties

## Core Idea
Thermal conductivity (k) is a material property that quantifies how readily heat diffuses through a substance. Metals conduct well (high k), while gases and insulators conduct poorly (low k). Conductivity typically increases with temperature in metals but may decrease in insulators.

## Explainer

From Fourier's law of heat conduction, you know that the heat flux (power per unit area) through a material is q = −k ∇T: heat flows down the temperature gradient, and k is the proportionality constant. Now the question is: what is k actually measuring, and why does it vary so widely across materials — from ~400 W/m·K for copper to ~0.02 W/m·K for aerogel, a factor of 20,000?

**Thermal conductivity** k encodes two things simultaneously: how much thermal energy the material can carry per unit temperature difference, and how quickly that energy is transported through the material. At the microscopic level, heat is carried by mobile particles — electrons in metals, phonons (quantized lattice vibrations) in insulators and semiconductors. The product k = (1/3) C_v v_avg λ connects k to three microscopic quantities: C_v is the heat capacity per unit volume (how much energy is stored per degree), v_avg is the average carrier speed, and λ is the **mean free path** (average distance a carrier travels before scattering). Large k requires carriers that are fast, numerous, and rarely scattered.

Metals have high k because free electrons carry heat very effectively: electrons move at ~10⁶ m/s (Fermi velocity), far faster than phonons (~10³ m/s), and their mean free path can be hundreds of nanometers at room temperature. The **Wiedemann-Franz law** (k/σ = L₀T, where σ is electrical conductivity and L₀ is the Lorenz number) reflects that the same electrons carry both heat and charge in metals — measure one and you know the other. In insulators, heat is carried only by phonons. Phonons scatter off impurities, grain boundaries, and each other; their mean free path is much shorter, giving k values 10–100× lower than metals.

Temperature dependence follows from how scattering changes with T. In metals at room temperature, electron-phonon scattering dominates: more phonons at higher T means more scattering, shorter mean free path, and lower k. In insulators, phonon-phonon scattering (Umklapp processes) also intensifies with temperature, decreasing k above room temperature. Near absolute zero, both behaviors reverse: fewer phonons means less scattering, very long mean free paths, and k can peak dramatically at low T. This non-monotonic behavior — low at high T, low at very low T (where carriers are frozen out), with a peak in between — is characteristic of phonon conductors and is important in cryogenic engineering and thermoelectric device design.
