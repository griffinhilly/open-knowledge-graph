---
id: electron-correlation-multi-electron-atoms
title: Electron Correlation in Multi-Electron Atoms
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hartree-fock-method
  type: hard
- id: hydrogen-atom-solution-radial-wavefunction
  type: soft
builds-toward:
- variational-method-ground-state
- density-functional-theory-intro
tags:
- electron-correlation
- quantum-chemistry
- multi-electron
- approximations
stage: advanced
status: draft
---

# Electron Correlation in Multi-Electron Atoms

## Core Idea
In multi-electron atoms, electron-electron repulsion cannot be ignored; electrons avoid each other's proximity, lowering energy below Hartree-Fock predictions. Correlation energy represents this stabilization. No simple closed-form solution exists; approximations like configuration interaction or coupled cluster are needed to capture correlation effects.

## How It's Best Learned
Compare Hartree-Fock and experimental ionization energies to quantify correlation energy. Build configuration interaction wave functions by mixing excited configurations and observe energy lowering.

## Explainer

From the Hartree-Fock method, you learned a powerful but imperfect approach to multi-electron atoms: each electron moves in the average electrostatic field created by all the other electrons. This **mean-field approximation** captures roughly 99% of the total electronic energy and gives reasonable orbital shapes and energies. But that remaining ~1% — the **correlation energy** — is chemically significant. It amounts to tens or hundreds of kJ/mol, which is comparable to bond energies and reaction barriers. Getting chemistry right demands accounting for electron correlation.

The physical picture is straightforward. Electrons are negatively charged and repel each other. In the Hartree-Fock picture, electron 1 sees a smeared-out cloud representing the average position of electron 2, but in reality, electron 2 is a point charge that is somewhere specific at each instant. The two electrons actively avoid each other — when electron 1 moves left, electron 2 is more likely to be found on the right. This instantaneous avoidance, called **dynamic correlation**, lowers the energy because the electrons spend less time close together than the mean-field picture predicts, reducing their mutual repulsion. There is also **static correlation**, which arises when the true wavefunction cannot be well-described by a single electron configuration — for example, in bond-breaking processes where two configurations become equally important.

The **correlation energy** is formally defined as the difference between the exact non-relativistic energy and the Hartree-Fock energy in a complete basis set: E_corr = E_exact − E_HF. It is always negative (the true energy is always lower than Hartree-Fock) because including correlation always stabilizes the system. For the helium atom, the correlation energy is about −0.042 hartree (−110 kJ/mol) — small relative to the total energy of −2.904 hartree, but large compared to chemical energy scales.

Recovering this correlation energy is the central challenge of post-Hartree-Fock quantum chemistry. The main approaches you will encounter — configuration interaction, coupled cluster, and Møller-Plesset perturbation theory — all start from the Hartree-Fock reference and add corrections to account for the instantaneous electron-electron interactions that the mean field misses. Each method represents a different tradeoff between accuracy and computational cost, but they all address the same fundamental physics: real electrons are correlated particles, not independent actors in an average field.
