---
id: rectangular-waveguide-propagation
title: Propagation in Rectangular Waveguides
domain: physics
course: electrodynamics
prerequisites:
- id: transverse-electric-modes
  type: hard
- id: transverse-magnetic-modes
  type: hard
- id: circular-waveguide-propagation
  type: soft
tags:
- rectangular-waveguide
- tmn-modes
- temn-modes
- dominant-mode
stage: expert
status: validated
---
# Propagation in Rectangular Waveguides

## Core Idea
In rectangular guides with dimensions a and b, TE and TM modes are labeled by integers m,n. The dominant TE₁₀ mode has the lowest cutoff frequency fc = c/(2a). Field patterns are products of sines/cosines in each transverse direction, satisfying boundary conditions.

## Questions

```yaml
- question: "A rectangular waveguide has width a = 2 cm and height b = 1 cm. What is the cutoff frequency of the dominant TE₁₀ mode, and what frequency range supports single-mode propagation?"
  type: multiple-choice
  options:
    - "f_c = c/a = 15 GHz; single-mode operation above 15 GHz"
    - "f_c = c/(2a) = 7.5 GHz; single-mode operation between 7.5 GHz and 15 GHz"
    - "f_c = c/(2b) = 15 GHz; single-mode operation between 15 GHz and 30 GHz"
    - "f_c = c/(a + b) ≈ 10 GHz; single-mode operation above 10 GHz"
  answer: 1
  explanation: "The cutoff frequency of the TE_mn mode is f_c = (c/2)√[(m/a)² + (n/b)²]. For TE₁₀ (m=1, n=0): f_c = c/(2a) = (3×10¹⁰ cm/s)/(2×2 cm) = 7.5 GHz. The next lowest cutoff is TE₂₀ at c/a = 15 GHz (or TE₀₁ at c/(2b) = 15 GHz). Single-mode operation — only TE₁₀ propagating — requires operating above 7.5 GHz but below 15 GHz. Below 7.5 GHz, no mode propagates; above 15 GHz, multiple modes coexist."

- question: "Measurements show that the phase velocity of the TE₁₀ mode in a waveguide slightly exceeds the speed of light c. What does this imply?"
  type: multiple-choice
  options:
    - "The measurement is in error — special relativity forbids any signal from exceeding c"
    - "The phase velocity can exceed c near cutoff, but the group velocity (energy velocity) remains less than c, so no information or energy travels faster than light"
    - "Both phase and group velocity exceed c in waveguides, since the mode travels in a guided medium"
    - "The waveguide is malfunctioning — in normal operation, phase velocity never exceeds c"
  answer: 1
  explanation: "Phase velocity v_p = c/√[1 − (f_c/f)²] exceeds c for all frequencies above cutoff, approaching infinity as f → f_c. This is not a violation of special relativity because phase velocity is not the velocity of energy or information. The group velocity v_g = c√[1 − (f_c/f)²] is always less than c and represents the actual speed of energy transport. The product v_p × v_g = c² — a fundamental waveguide relation. Near cutoff, phase velocity is very large while group velocity is near zero; at very high frequencies, both approach c."

- question: "A mode whose operating frequency is below its cutoff frequency does not propagate through the waveguide — its fields decay exponentially along the propagation direction."
  type: true-false
  answer: true
  explanation: "Below cutoff, the propagation constant k_z = (2π/λ)√[1 − (f_c/f)²] becomes imaginary, since (f_c/f)² > 1. An imaginary propagation constant means the fields decay as e^(−|k_z|z) — exponential attenuation along the guide rather than oscillatory propagation. These are called evanescent modes. They still exist as near-field patterns near a source or discontinuity, but they carry no net power down the guide. This is why choosing an operating frequency below the dominant mode's cutoff completely prevents propagation."

- question: "The TM₁₀ mode exists in a rectangular waveguide and has the same cutoff frequency as the TE₁₀ dominant mode."
  type: true-false
  answer: false
  explanation: "The TM₁₀ mode does not exist. TM modes require E_z = sin(mπx/a)·sin(nπy/b). With n = 0, this becomes sin(mπx/a)·sin(0) = 0 identically — no field exists. The same applies to TM_m0 and TM_0n modes: at least one of m and n must be nonzero for TM modes to exist. The lowest-order TM mode is TM₁₁. This is why TE₁₀ is the unique dominant mode — there is no TM counterpart at the same cutoff frequency."

- question: "Why is single-mode operation desirable in a rectangular waveguide, and how do the dimensions a and b determine the frequency range over which it is achievable?"
  type: short-answer
  answer: "Single-mode operation means only one field pattern (TE₁₀) propagates down the guide. This is desirable because multiple coexisting modes travel at different phase velocities, causing modal dispersion — signal distortion as different modes arrive at different times — and modal interference, which creates unpredictable field patterns. The frequency range for single-mode operation is determined by the gap between the TE₁₀ cutoff (c/2a) and the next mode's cutoff. For a guide with b ≤ a/2, the next mode is TE₂₀ at c/a, giving a usable bandwidth of c/(2a) to c/a (a factor of 2 in frequency). Making a larger lowers the single-mode band to lower frequencies but keeps the factor-of-2 bandwidth. Making b smaller raises TE₀₁ above TE₂₀, maximizing the single-mode range."
  explanation: "The choice of waveguide dimensions is an engineering tradeoff: larger a supports lower frequencies but also allows more modes at higher frequencies. Standard waveguide families (WR-90, WR-62, etc.) are specified with a ≈ 2b to place the TE₀₁ cutoff at the same frequency as TE₂₀, maximizing the single-mode bandwidth to a factor of 2. Real systems operate well within the single-mode band (not close to either edge) to avoid the high attenuation near cutoff and the risk of exciting the next mode due to manufacturing tolerances."
```

## Explainer

From your study of TE and TM modes, you know that inside a metallic waveguide, electromagnetic waves cannot propagate as plane waves — the conducting walls impose boundary conditions that force the transverse field components to vanish at the metal surfaces. The fields must form standing wave patterns in the transverse directions, and only waves whose transverse pattern fits the geometry can propagate. In a rectangular guide of width a (along x) and height b (along y), the transverse structure must satisfy E_tangential = 0 at all four walls.

The solution separates beautifully. For a **TE_mn mode**, the longitudinal magnetic field component H_z takes the form cos(mπx/a) · cos(nπy/b), where m and n are non-negative integers counting the number of half-wave variations in the x and y directions respectively. The boundary conditions (no tangential E at the walls) are automatically satisfied by this cosine form. For **TM_mn modes**, the longitudinal electric field E_z takes the form sin(mπx/a) · sin(nπy/b) — sines, because E_z itself must vanish at the walls (it is tangential there). The transverse field components are derived from these by differentiation.

Each integer pair (m, n) labels a distinct mode with its own transverse field pattern and its own **cutoff frequency**: f_c = (c/2)√[(m/a)² + (n/b)²]. Below f_c, the mode is **evanescent** — it decays exponentially along the guide rather than propagating. Above f_c, the mode propagates with phase velocity v_p = c/√[1 − (f_c/f)²], which exceeds c near cutoff (though the energy velocity, the group velocity, remains less than c). The **propagation constant** is k_z = (2π/λ)√[1 − (f_c/f)²], going to zero at cutoff and approaching the free-space value k at high frequencies.

The **dominant mode** is TE₁₀, which has m = 1, n = 0 — one half-wave variation across the width a and none across the height b. Its cutoff frequency is f_c = c/(2a), and it has the lowest cutoff of all modes. In practical systems, the operating frequency is chosen in the range c/(2a) < f < c/a (or c/(2b) if b < a/2), ensuring only the TE₁₀ mode propagates while all higher modes are cut off. This **single-mode operation** gives clean, predictable transmission: only one field pattern travels down the guide, avoiding the modal dispersion and interference that would occur if multiple modes coexisted. Standard waveguide dimensions (e.g., WR-90 with a = 22.86 mm, used at 8–12 GHz) are chosen precisely to single-mode the frequencies of interest.
