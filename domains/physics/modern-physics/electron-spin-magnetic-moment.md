---
id: electron-spin-magnetic-moment
title: Electron Spin and Intrinsic Magnetic Moment
domain: physics
course: modern-physics
prerequisites:
- id: spin-angular-momentum
  type: hard
builds-toward:
- zeeman-effect-magnetic-splitting
- stern-gerlach-sequential-measurements
tags:
- spin
- magnetic-moment
- quantum-mechanics
stage: advanced
status: draft
---

# Electron Spin and Intrinsic Magnetic Moment

## Core Idea
Electrons possess intrinsic angular momentum (spin) with magnitude S = ℏ√(s(s+1)) where s = 1/2. The spin z-component is m_s = ±ℏ/2 (spin up or spin down). Spin produces a magnetic moment μ = −g_s(e/2m_e)S, where g_s ≈ 2 (anomalous in comparison to orbital angular momentum). This magnetic moment interacts with magnetic fields and causes level splitting.

## How It's Best Learned
Study spin-1/2 systems using Pauli matrices. Calculate expectation values of spin components. Understand spin as an intrinsic two-state system; appreciate that quantum spin has no classical analog.

## Common Misconceptions
Spin does not mean the electron is literally spinning (quantum spin is intrinsic, not due to rotation). The g-factor ≈ 2 is not exactly 2 due to quantum electrodynamic corrections. Spin-orbit coupling is not due to the spinning electron's magnetic moment interacting with the orbital motion magnetic field (it's a relativistic effect).

## Explainer

You've studied spin angular momentum as an abstract two-state quantum system. Now the physical stakes become clearer: spin isn't just a mathematical curiosity — it generates a real **magnetic dipole moment** that interacts measurably with external magnetic fields and with the electron's own orbital motion. The connection between spin and magnetism is what makes the electron a tiny magnet, and it drives much of the structure of atomic spectra.

The **intrinsic magnetic moment** of the electron is μ = −g_s (e/2m_e) S, where S is the spin angular momentum vector. The factor e/2m_e is the same that appears for orbital angular momentum (the **gyromagnetic ratio**), but the factor g_s ≈ 2 is not — it's the anomalous g-factor. For orbital angular momentum, the magnetic moment and angular momentum have g_L = 1; for spin, g_s ≈ 2.002. This factor of 2 was a complete mystery classically and was correctly predicted only by Dirac's relativistic quantum mechanics. The tiny departure from exactly 2 (the 0.002) is a quantum electrodynamic correction — one of the most precisely measured quantities in physics, tested to 12 significant figures.

In a magnetic field B, the interaction energy is U = −μ·B = g_s (e/2m_e) S·B. Since the z-component of spin is quantized as m_s = ±ℏ/2, the energy levels split into two: E = ±g_s (eℏ/2m_e) B/2 = ±μ_B g_s B/2, where μ_B = eℏ/2m_e is the **Bohr magneton** (≈ 9.27 × 10⁻²⁴ J/T). This splitting is the magnetic energy scale for electrons in atoms. The Stern-Gerlach experiment demonstrated exactly this splitting: silver atoms passed through an inhomogeneous magnetic field split into two beams, corresponding to m_s = +1/2 and m_s = −1/2.

Why does spin have g_s ≈ 2 and not 1, like orbital angular momentum? The short answer is that spin is an intrinsic property of the relativistic electron — it emerges naturally from Dirac's relativistic wave equation as a consequence of special relativity combined with quantum mechanics. There is no classical model: attempts to picture the electron as a spinning charged sphere fail because the equatorial velocity would exceed c for any reasonable electron radius. Spin is genuinely quantum mechanical with no classical analog. This is why the language is "intrinsic angular momentum" — it's a property the electron carries independent of any spatial motion, as fundamental to what an electron is as its charge or mass.
