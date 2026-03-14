---
id: nmr-quantum-theory
title: Quantum Theory of NMR Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: nmr-spectroscopy-basics
  type: soft
- id: spin-quantum-number
  type: soft
tags:
- NMR
- spin-1/2
- Zeeman-effect
- chemical-shift
- spin-spin-coupling
- Larmor-frequency
stage: advanced
status: validated
---

# Quantum Theory of NMR Spectroscopy

## Core Idea
NMR spectroscopy exploits the quantum mechanical property of nuclear spin. For spin-1/2 nuclei (e.g., ¹H, ¹³C), two energy states (α and β) split in an external magnetic field B₀ with energy gap ΔE = γℏB₀ (the Zeeman effect). Resonance occurs when the applied radiofrequency matches the Larmor frequency ν = γB₀/(2π). Chemical shielding by electrons shifts the resonance frequency, giving rise to the chemical shift δ (in ppm). J-coupling between nuclei arises from through-bond electron-mediated interactions and is independent of B₀, enabling structural determination. The Bloch equations describe the macroscopic magnetization dynamics underlying pulsed FT-NMR.

## How It's Best Learned
Derive the two-state energy level diagram for a spin-1/2 nucleus in a field, then map it onto real ¹H NMR features: chemical shifts from shielding constants, multiplicities from J-coupling, and peak areas from population differences.

## Common Misconceptions
- Thinking chemical shift is an absolute frequency — it is a dimensionless ratio (ppm) relative to a reference, making it field-independent.
- Confusing J-coupling (through bonds, field-independent) with dipolar coupling (through space, field-dependent, averages to zero in solution).
