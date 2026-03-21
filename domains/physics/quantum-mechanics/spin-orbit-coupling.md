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
stage: advanced
status: draft
---

# Spin-Orbit Coupling

## Core Idea
Spin-orbit coupling arises from the relativistic interaction H_SO ∝ L·S between the electron's spin magnetic moment and the magnetic field from its orbital motion. This coupling causes fine structure splitting in atomic energy levels and demonstrates that orbital and spin angular momenta cannot be independently conserved.

## Questions

```yaml
- question: "Spin-orbit coupling is added to the hydrogen Hamiltonian. Which set of quantum numbers correctly describes the new good quantum numbers for the electron?"
  type: multiple-choice
  options:
    - "n, l, m_l, m_s — the same as the unperturbed hydrogen atom"
    - "n, l, s, j, m_j — because H_SO commutes with J² and J_z but not with L_z or S_z individually"
    - "n, j, m_j only — because spin-orbit coupling destroys all other quantum numbers"
    - "n, l, m_l, j — a hybrid set that mixes the old and new bases"
  answer: 1
  explanation: "Spin-orbit coupling H_SO ∝ L·S does not commute with L_z or S_z individually, so m_l and m_s are no longer conserved. However, L·S is rotationally invariant (it is a scalar), so it commutes with J² = (L + S)² and with J_z = L_z + S_z. The quantum numbers n (from the radial equation), l (from L²), s = 1/2 (unchanged), j (from J²), and m_j (from J_z) all remain good. The key change is replacing the pair (m_l, m_s) with the pair (j, m_j)."

- question: "Why is the identity L·S = (1/2)(J² − L² − S²) essential for computing the energy correction from spin-orbit coupling?"
  type: multiple-choice
  options:
    - "It converts L·S into a form involving only position operators, making it easier to compute expectation values"
    - "It expresses L·S in terms of J², L², and S², whose eigenvalues ℏ²j(j+1), ℏ²l(l+1), ℏ²s(s+1) are known in the |n,l,s,j,m_j⟩ basis, giving a direct formula for ΔE_SO"
    - "It eliminates the coupling between spin and orbital motion, reducing the problem to two independent angular momenta"
    - "It is only needed for states with l > 1; for l = 0 and l = 1 states, L·S can be computed directly"
  answer: 1
  explanation: "The identity L·S = (1/2)(J² − L² − S²) is powerful because J², L², and S² all commute with H_SO and with each other in the coupled basis |n,l,s,j,m_j⟩. Their eigenvalues are ℏ²j(j+1), ℏ²l(l+1), ℏ²s(s+1) respectively. Therefore ⟨L·S⟩ = (ℏ²/2)[j(j+1) − l(l+1) − s(s+1)], which directly gives the perturbative energy correction without any complicated matrix computation. Without this identity, computing ⟨L·S⟩ would require evaluating off-diagonal matrix elements between m_l and m_s states."

- question: "The spin-orbit energy correction ΔE_SO takes different values for j = l + 1/2 and j = l − 1/2 states with the same n and l, splitting what was previously a degenerate level."
  type: true-false
  answer: true
  explanation: "For j = l + 1/2: j(j+1) − l(l+1) − s(s+1) = (l + 1/2)(l + 3/2) − l(l+1) − 3/4 = l. For j = l − 1/2: the analogous calculation gives −(l+1). Since l ≠ −(l+1) for l > 0, the two j values give different energy shifts, breaking the degeneracy. For example, the hydrogen 2p level splits into 2p₁/₂ (j = 1/2) and 2p₃/₂ (j = 3/2) with different energies. This fine structure splitting is one of the key experimental consequences of spin-orbit coupling."

- question: "In the electron's rest frame, the orbiting proton creates an electric field at the electron's location, and it is the interaction of this electric field with the electron's charge that produces spin-orbit coupling."
  type: true-false
  answer: false
  explanation: "The electric field produced by the orbiting proton exerts a Coulomb force on the electron's charge — this is the dominant (unperturbed) Hamiltonian, not the spin-orbit coupling. Spin-orbit coupling arises from the *magnetic* field that the orbiting proton produces in the electron's rest frame. A moving charge creates a magnetic field, and the proton's orbital motion (as seen from the electron's frame) generates a magnetic field B at the electron's location. This magnetic field then interacts with the electron's *spin magnetic moment* μ_S, giving H_SO ∝ μ_S · B ∝ L·S."

- question: "Explain why L_z and S_z are no longer individually conserved when spin-orbit coupling is present, and what quantity is conserved instead."
  type: short-answer
  answer: "Spin-orbit coupling adds H_SO ∝ L·S to the Hamiltonian. This term does not commute with L_z or S_z individually: [L·S, L_z] = [L_xS_x + L_yS_y + L_zS_z, L_z] ≠ 0, because L_x and L_y do not commute with L_z. Physically, H_SO mixes states with different (m_l, m_s) pairs that have the same m_j = m_l + m_s, so individual m_l and m_s fluctuate while their sum is preserved. What is conserved is the total angular momentum: J² and J_z commute with H_SO because L·S is rotationally invariant. The good quantum numbers are therefore j and m_j rather than m_l and m_s."
  explanation: "The semiclassical picture is that L and S each precess around the fixed total angular momentum vector J. Neither L_z nor S_z is individually stable — they oscillate as L and S precess — but J_z = L_z + S_z remains constant. This precession picture explains why (l, s, j, m_j) are the right quantum numbers: j characterizes the magnitude of J (which is fixed by the energy eigenstate), and m_j characterizes its projection on the z-axis (which is conserved). The individual projections m_l and m_s average to well-defined values only in special cases."
```

## Explainer

From your study of angular momentum quantization, you know that orbital angular momentum L is quantized with magnitude √(l(l+1))ℏ and z-component m_l ℏ. From spin, you know that an electron carries an intrinsic angular momentum S with s = 1/2 and z-component m_s = ±1/2, and that spin has an associated magnetic moment μ_S = −gₛ(e/2m)S. Spin-orbit coupling asks: what happens when these two angular momenta interact? The answer produces one of the most important corrections to the hydrogen energy levels and is foundational to atomic structure beyond the simplest approximation.

The physical picture is best understood in the electron's rest frame. From the electron's perspective, the proton is orbiting around it, creating a current loop and hence a magnetic field B at the electron's location. This magnetic field interacts with the electron's spin magnetic moment, adding a perturbation H_SO ∝ **L**·**S** to the Hamiltonian. The dot product **L**·**S** = (1/2)(J² − L² − S²), where **J** = **L** + **S** is the **total angular momentum**. This identity is the key to finding the energy correction. Because H_SO contains L² and S², the eigenstates of L_z and S_z (labeled by m_l and m_s) are no longer the right basis — H_SO mixes states with different m_l and m_s while preserving their sum m_j = m_l + m_s. The good quantum numbers become n, l, s, and j, where j = l ± 1/2 labels the total angular momentum.

The energy correction from spin-orbit coupling is ΔE_SO ∝ [j(j+1) − l(l+1) − s(s+1)]/2. For a given l, j can be either l + 1/2 or l − 1/2, giving two different energy shifts. This **fine structure splitting** breaks the degeneracy between states that differed only in relative orientation of L and S. For example, in hydrogen the 2p level (l = 1) splits into 2p₁/₂ (j = 1/2) and 2p₃/₂ (j = 3/2), separated by about 4.5 × 10⁻⁵ eV — small compared to the gross structure (~10 eV) but measurable spectroscopically. The subscript notation n l_j encodes the coupling: 2p₃/₂ means n = 2, l = 1 (p orbital), j = 3/2.

The deeper lesson is about what is conserved. Before spin-orbit coupling, L_z and S_z individually commuted with H, so m_l and m_s were good quantum numbers. The coupling H_SO breaks those individual symmetries: [H_SO, L_z] ≠ 0 and [H_SO, S_z] ≠ 0, meaning m_l and m_s are no longer conserved. However, **J**² and J_z still commute with the full H, because spin-orbit coupling is rotationally invariant — it depends on **L**·**S**, which is a scalar. So j and m_j are the conserved quantum numbers, while m_l and m_s fluctuate. Physically: the spin and orbital angular momenta precess around the fixed total angular momentum vector **J**, while **J** itself precesses around the z-axis at rate m_j. This precession picture is the semiclassical view of what spin-orbit coupling does to the electron's motion in an atom.
