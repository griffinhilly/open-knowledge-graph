---
id: bohr-model-to-quantum
title: From Bohr Model to Quantum Mechanics
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
builds-toward:
- hydrogen-quantum-energy-levels
tags:
- atomic-structure
- history
stage: advanced
status: draft
---

# From Bohr Model to Quantum Mechanics

## Core Idea
Bohr's model explained hydrogen's line spectrum by quantizing angular momentum (L = nℏ) and assuming discrete circular orbits without radiation loss. However, Bohr's model failed for multi-electron atoms and rested on ad hoc assumptions. Quantum mechanics explains the same phenomena more fundamentally: electrons are described by wavefunctions in potential wells, with energy levels emerging from boundary conditions, without assuming orbits or radiation suppression.

## Explainer

The Bohr model was a remarkable achievement for 1913: it produced hydrogen's energy levels E_n = −13.6 eV/n² from first principles and correctly predicted the spectral line positions that had puzzled physicists for decades. But the model rested on two ad hoc rules with no classical justification: angular momentum must be quantized as L = nℏ, and electrons in allowed orbits magically stop radiating despite undergoing centripetal acceleration. Classical electrodynamics — which Bohr otherwise accepted — says any accelerating charge *must* radiate. Bohr essentially said "trust the rule; don't ask why."

The conceptual bridge was de Broglie's 1924 insight: if light has particle properties (photons), perhaps matter has wave properties. An electron in a circular orbit would then be a matter wave, and the quantization rule L = nℏ simply says that the electron's wavelength must fit an integer number of times around the orbit — a standing wave condition. This reframes quantization from an arbitrary postulate to a boundary condition on a physical wave. But de Broglie's picture still retained the notion of orbits; full quantum mechanics would discard even that.

The Schrödinger equation (1926) replaced orbits with **wavefunctions** ψ satisfying −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ. For the hydrogen atom, V(r) = −e²/(4πε₀r), and demanding that ψ be normalizable (square-integrable, finite everywhere) automatically restricts E to discrete values: exactly E_n = −13.6 eV/n². No ad hoc quantization rule is needed — quantization emerges from the mathematics of the boundary conditions on the wavefunction in a Coulomb potential. The same machinery applies to any potential well, including multi-electron atoms, molecules, and quantum dots.

The conceptual shift from Bohr to quantum mechanics is profound. In Bohr's picture, electrons travel on definite circular paths — you could in principle watch the electron orbit. In quantum mechanics, the electron has no definite trajectory. The wavefunction ψ(r) describes a **probability amplitude**: the electron simply has a certain probability of being found at any given location, and asking "which orbit is it on?" becomes a category error. What Bohr's model called the n=1 orbit becomes the 1s orbital — a spherically symmetric probability cloud centered on the nucleus. The Bohr model was right about the *energies* but wrong about the *picture*, and the picture matters enormously for understanding chemistry, molecular bonding, and everything beyond hydrogen.
