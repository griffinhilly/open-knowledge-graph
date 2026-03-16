---
id: hydrogen-atom-spectrum
title: Hydrogen Atom Spectral Series
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-quantum
  type: hard
builds-toward:
- fine-structure-splitting
tags:
- hydrogen-spectrum
- transitions
- spectroscopy
stage: advanced
status: draft
---

# Hydrogen Atom Spectral Series

## Core Idea
Transitions between hydrogen energy levels En and E_m emit or absorb photons with frequency ω = |E_n - E_m|/ℏ. Different series correspond to transitions ending at different n: Lyman (n=1), Balmer (n=2), Paschen (n=3). Selection rules Δl = ±1 and Δm_l = 0, ±1 govern allowed transitions. Quantum mechanics explains spectral line positions perfectly, validating the theory.

## Explainer

You have already solved the hydrogen atom and found its energy eigenvalues E_n = −13.6 eV / n² and the corresponding eigenstates labeled by quantum numbers (n, l, m_l). A spectral line is what you observe when the electron transitions between two of these eigenstates, emitting or absorbing a photon whose energy exactly equals the level difference: E_photon = ℏω = |E_n − E_m|. Because the energy levels are discrete, only certain photon frequencies are allowed, producing the sharp lines that characterize atomic spectra.

The spectral lines are organized into **series** based on which lower level the transition ends on. The **Lyman series** collects all transitions ending at n = 1 (the ground state). Because the ground state is the deepest level, these energy differences are the largest, placing Lyman lines in the ultraviolet. The **Balmer series** ends at n = 2 and falls in the visible range — the famous red H-α line at 656 nm corresponds to the 3→2 transition, while H-β (4→2) is blue-green. The **Paschen series** ends at n = 3 and lies in the near-infrared. Each series converges to a **series limit** (the minimum wavelength, corresponding to ionization from that level) as the upper level n → ∞.

Not all transitions between levels are equally probable. **Selection rules** filter which transitions can occur via electric dipole radiation, by far the dominant emission mechanism. The rules Δl = ±1 and Δm_l = 0, ±1 follow from conservation of angular momentum: a photon carries one unit of angular momentum, so the electron's angular momentum quantum number must change by ±1 to balance it. A transition from a 2s state (l = 0) to the 1s ground state (l = 0) has Δl = 0 and is therefore **forbidden** by the electric dipole selection rule — the 2s state is **metastable** because it can only decay by much weaker processes. In contrast, 2p → 1s has Δl = −1 and is allowed; it produces a strong Lyman-alpha line at 121.6 nm.

The perfect match between these quantum-mechanical predictions and measured hydrogen spectral wavelengths was one of the great early triumphs of Schrödinger's equation. Astronomers use hydrogen's spectral series to identify hydrogen in stellar atmospheres, determine stellar temperatures (hotter stars show different series in absorption), and measure radial velocities via Doppler shifts. The hydrogen spectrum remains the benchmark against which all atomic calculations are tested.
