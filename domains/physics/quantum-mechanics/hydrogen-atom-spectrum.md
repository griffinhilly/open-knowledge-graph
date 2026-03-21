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

## Questions

```yaml
- question: "An electron in the 2s state of hydrogen cannot decay directly to the 1s ground state via electric dipole radiation. Why not?"
  type: multiple-choice
  options:
    - "The energy difference is too small to produce a detectable photon"
    - "The 2s and 1s states have the same angular momentum quantum number, violating Δl = ±1"
    - "The 2s state has higher energy than 1s, so emission would violate energy conservation"
    - "The 2s→1s transition is in the infrared and too weak to measure"
  answer: 1
  explanation: "The electric dipole selection rule requires Δl = ±1. Both the 2s (l = 0) and 1s (l = 0) states have the same l value, so Δl = 0 — a forbidden transition. A photon carries one unit of angular momentum, and if the electron's angular momentum doesn't change, angular momentum cannot be conserved. This makes the 2s state metastable; it can only decay via much weaker processes. Comparing to the 2p→1s transition (Δl = −1, allowed): that produces the bright Lyman-alpha line at 121.6 nm."

- question: "The H-β line of the Balmer series corresponds to which transition, and roughly where in the electromagnetic spectrum does it appear?"
  type: multiple-choice
  options:
    - "3→1 transition; ultraviolet"
    - "4→2 transition; visible (blue-green)"
    - "5→3 transition; near-infrared"
    - "4→1 transition; ultraviolet"
  answer: 1
  explanation: "The Balmer series collects all transitions ending at n = 2. H-α is the 3→2 transition (red, 656 nm); H-β is the 4→2 transition (blue-green, ~486 nm). Option A describes a Lyman series line (ends at n = 1, UV). Option C describes a Paschen series line (ends at n = 3, infrared). Option D is also a Lyman line. The Balmer series is the only hydrogen series with lines in the visible range, which is why it was the first to be empirically catalogued."

- question: "The selection rule Δl = ±1 follows from angular momentum conservation: a photon carries exactly one unit of angular momentum, so the electron's orbital angular momentum must change by ±1 in any electric dipole emission."
  type: true-false
  answer: true
  explanation: "This is exactly correct. A photon has spin-1 and carries one unit of angular momentum. When it is emitted, that angular momentum must come from somewhere — the electron's orbital angular momentum quantum number l must change by ±1 to conserve total angular momentum. This is why transitions with Δl = 0 or |Δl| > 1 are forbidden by the electric dipole selection rule, though they can occur through weaker higher-order processes."

- question: "The Lyman series lines appear in the visible part of the electromagnetic spectrum because the hydrogen ground state is at the lowest energy."
  type: true-false
  answer: false
  explanation: "The Lyman series appears in the ultraviolet, not the visible. Because the ground state (n = 1) is the lowest energy level, Lyman series transitions have the largest energy differences of any hydrogen series (the photon must carry away the full gap to or from the ground state). Large energy differences correspond to high-frequency, short-wavelength photons — ultraviolet radiation. The Balmer series (ending at n = 2) produces the visible lines, and the Paschen series (ending at n = 3) falls in the near-infrared."

- question: "Why do excited hydrogen atoms emit only discrete spectral lines rather than a continuous spectrum of wavelengths?"
  type: short-answer
  answer: "Because hydrogen's energy levels are quantized — the electron can only occupy specific allowed energies (En = −13.6 eV / n²). Photon emission occurs when the electron transitions between two levels, and the photon's energy must exactly equal the difference between those levels. Since only discrete level differences are possible, only discrete photon frequencies are emitted. A continuous spectrum would require the electron to occupy continuously variable energies, which is not permitted in quantum mechanics."
  explanation: "This is the central triumph of quantum mechanics applied to the hydrogen atom: the same mathematical framework that quantizes energy levels automatically predicts exactly the spectral line positions observed experimentally. The Rydberg formula, which was empirically known, is derived exactly from E_n = −13.6 eV / n². The discreteness of the spectrum is direct experimental evidence that atomic energy levels are quantized."
```

## Explainer

You have already solved the hydrogen atom and found its energy eigenvalues E_n = −13.6 eV / n² and the corresponding eigenstates labeled by quantum numbers (n, l, m_l). A spectral line is what you observe when the electron transitions between two of these eigenstates, emitting or absorbing a photon whose energy exactly equals the level difference: E_photon = ℏω = |E_n − E_m|. Because the energy levels are discrete, only certain photon frequencies are allowed, producing the sharp lines that characterize atomic spectra.

The spectral lines are organized into **series** based on which lower level the transition ends on. The **Lyman series** collects all transitions ending at n = 1 (the ground state). Because the ground state is the deepest level, these energy differences are the largest, placing Lyman lines in the ultraviolet. The **Balmer series** ends at n = 2 and falls in the visible range — the famous red H-α line at 656 nm corresponds to the 3→2 transition, while H-β (4→2) is blue-green. The **Paschen series** ends at n = 3 and lies in the near-infrared. Each series converges to a **series limit** (the minimum wavelength, corresponding to ionization from that level) as the upper level n → ∞.

Not all transitions between levels are equally probable. **Selection rules** filter which transitions can occur via electric dipole radiation, by far the dominant emission mechanism. The rules Δl = ±1 and Δm_l = 0, ±1 follow from conservation of angular momentum: a photon carries one unit of angular momentum, so the electron's angular momentum quantum number must change by ±1 to balance it. A transition from a 2s state (l = 0) to the 1s ground state (l = 0) has Δl = 0 and is therefore **forbidden** by the electric dipole selection rule — the 2s state is **metastable** because it can only decay by much weaker processes. In contrast, 2p → 1s has Δl = −1 and is allowed; it produces a strong Lyman-alpha line at 121.6 nm.

The perfect match between these quantum-mechanical predictions and measured hydrogen spectral wavelengths was one of the great early triumphs of Schrödinger's equation. Astronomers use hydrogen's spectral series to identify hydrogen in stellar atmospheres, determine stellar temperatures (hotter stars show different series in absorption), and measure radial velocities via Doppler shifts. The hydrogen spectrum remains the benchmark against which all atomic calculations are tested.
