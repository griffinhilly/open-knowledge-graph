---
id: zeeman-effect-magnetic-splitting
title: 'Zeeman Effect: Magnetic Field Splitting of Energy Levels'
domain: physics
course: modern-physics
prerequisites:
- id: electron-spin-magnetic-moment
  type: hard
- id: orbital-angular-momentum-quantum
  type: soft
builds-toward:
- fine-structure-atomic-splitting
tags:
- magnetic-field
- energy-levels
- atomic-physics
stage: advanced
status: draft
---

# Zeeman Effect: Magnetic Field Splitting of Energy Levels

## Core Idea
In an external magnetic field B, the energy shifts by ΔE = μ_z B = −g(e/2m_e)m B where m is m_ℓ or m_s (or a combination in fine structure). This causes level splitting: a state with angular momentum quantum number j splits into 2j+1 sublevels corresponding to different m_j values. The Zeeman effect is a direct manifestation of space quantization.

## How It's Best Learned
Calculate the Zeeman splitting for hydrogen 1s and 2p states in a known magnetic field. Measure the Zeeman shift spectroscopically. Compare normal Zeeman effect (scalar) with anomalous Zeeman effect (where g ≠ 1).

## Common Misconceptions
All 2j+1 sublevels are equally spaced in magnetic field (linear Zeeman effect). The energy shift is proportional to B, not B². In the anomalous Zeeman effect, the apparent 'magnetic mass' is not actually changed by the field.

## Explainer

You already know that the electron carries a magnetic moment — both from its orbital motion and from its intrinsic spin. A magnetic dipole placed in an external field has energy U = −**μ** · **B**. Since the electron's magnetic moment is proportional to its angular momentum, and angular momentum is quantized, the energy shift in a magnetic field must also be quantized. That is the Zeeman effect in one sentence: a magnetic field turns a single energy level into a ladder of equally spaced sublevels.

For a pure orbital state (spin neglected), the energy shift is **ΔE = m_ℓ μ_B B**, where μ_B = eℏ/2m_e is the **Bohr magneton** and m_ℓ runs from −ℓ to +ℓ. A state with angular momentum quantum number ℓ splits into 2ℓ + 1 equally spaced sublevels. This is the **normal Zeeman effect** — it occurs cleanly for states with zero total spin (S = 0), which happens in two-electron systems where spins pair up. Spectroscopically, you see a single spectral line split into three lines (the Δm_ℓ = 0, ±1 selection rules). The splitting is directly proportional to B, making Zeeman splitting a powerful tool for measuring magnetic field strengths in laboratory and astronomical contexts.

When spin is present, the situation becomes the **anomalous Zeeman effect**, and the pattern is more complex. The issue is that the electron's spin magnetic moment has g_s ≈ 2, not g_s = 1 like the orbital contribution. When orbital and spin angular momenta are coupled into total angular momentum **J**, the effective magnetic moment is neither the purely orbital nor purely spin value — it is set by the **Landé g-factor**, g_J = 1 + [J(J+1) + S(S+1) − L(L+1)] / [2J(J+1)]. The energy shift is then ΔE = g_J m_J μ_B B, where m_J runs from −J to +J. Because g_J differs from 1, different levels within a multiplet shift by different amounts, producing the "anomalous" — meaning non-trivial — splitting pattern that historically caused great confusion until electron spin was properly understood.

The Zeeman effect is a direct experimental demonstration of **space quantization** — the idea that angular momentum can only point in discrete directions relative to an external field axis, not continuously as classical physics would predict. Before the full quantum theory was developed, this splitting was one of the clearest indicators that something fundamentally non-classical was happening in atoms. Today it is used in MRI machines (nuclear Zeeman effect in nuclei), in laser cooling of atoms (exploiting level shifts to create position-dependent forces), and in astrophysics to measure stellar magnetic fields from spectral line splitting observed in light from distant stars.
