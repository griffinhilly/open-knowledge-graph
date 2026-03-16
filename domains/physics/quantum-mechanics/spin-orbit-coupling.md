---
id: spin-orbit-coupling
title: Spin-Orbit Coupling
domain: physics
course: quantum-mechanics
prerequisites:
- id: spin-half-systems
  type: hard
- id: angular-momentum-quantization
  type: hard
tags:
- spin
- coupling
- interactions
stage: abstract-reasoning
status: draft
---

# Spin-Orbit Coupling

## Core Idea
Spin-orbit coupling arises from the relativistic interaction H_SO ∝ L·S between the electron's spin magnetic moment and the magnetic field from its orbital motion. This coupling causes fine structure splitting in atomic energy levels and demonstrates that orbital and spin angular momenta cannot be independently conserved.

## Explainer

From your study of angular momentum quantization, you know that orbital angular momentum L is quantized with magnitude √(l(l+1))ℏ and z-component m_l ℏ. From spin, you know that an electron carries an intrinsic angular momentum S with s = 1/2 and z-component m_s = ±1/2, and that spin has an associated magnetic moment μ_S = −gₛ(e/2m)S. Spin-orbit coupling asks: what happens when these two angular momenta interact? The answer produces one of the most important corrections to the hydrogen energy levels and is foundational to atomic structure beyond the simplest approximation.

The physical picture is best understood in the electron's rest frame. From the electron's perspective, the proton is orbiting around it, creating a current loop and hence a magnetic field B at the electron's location. This magnetic field interacts with the electron's spin magnetic moment, adding a perturbation H_SO ∝ **L**·**S** to the Hamiltonian. The dot product **L**·**S** = (1/2)(J² − L² − S²), where **J** = **L** + **S** is the **total angular momentum**. This identity is the key to finding the energy correction. Because H_SO contains L² and S², the eigenstates of L_z and S_z (labeled by m_l and m_s) are no longer the right basis — H_SO mixes states with different m_l and m_s while preserving their sum m_j = m_l + m_s. The good quantum numbers become n, l, s, and j, where j = l ± 1/2 labels the total angular momentum.

The energy correction from spin-orbit coupling is ΔE_SO ∝ [j(j+1) − l(l+1) − s(s+1)]/2. For a given l, j can be either l + 1/2 or l − 1/2, giving two different energy shifts. This **fine structure splitting** breaks the degeneracy between states that differed only in relative orientation of L and S. For example, in hydrogen the 2p level (l = 1) splits into 2p₁/₂ (j = 1/2) and 2p₃/₂ (j = 3/2), separated by about 4.5 × 10⁻⁵ eV — small compared to the gross structure (~10 eV) but measurable spectroscopically. The subscript notation n l_j encodes the coupling: 2p₃/₂ means n = 2, l = 1 (p orbital), j = 3/2.

The deeper lesson is about what is conserved. Before spin-orbit coupling, L_z and S_z individually commuted with H, so m_l and m_s were good quantum numbers. The coupling H_SO breaks those individual symmetries: [H_SO, L_z] ≠ 0 and [H_SO, S_z] ≠ 0, meaning m_l and m_s are no longer conserved. However, **J**² and J_z still commute with the full H, because spin-orbit coupling is rotationally invariant — it depends on **L**·**S**, which is a scalar. So j and m_j are the conserved quantum numbers, while m_l and m_s fluctuate. Physically: the spin and orbital angular momenta precess around the fixed total angular momentum vector **J**, while **J** itself precesses around the z-axis at rate m_j. This precession picture is the semiclassical view of what spin-orbit coupling does to the electron's motion in an atom.
