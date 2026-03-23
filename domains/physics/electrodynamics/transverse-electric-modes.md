---
id: transverse-electric-modes
title: Transverse Electric (TE) Modes
domain: physics
course: electrodynamics
prerequisites:
- id: waveguide-equations-general
  type: hard
builds-toward:
- rectangular-waveguide-propagation
- circular-waveguide-propagation
tags:
- te-modes
- guided-waves
- cutoff-frequency
stage: expert
status: validated
---

# Transverse Electric (TE) Modes

## Core Idea
TE modes have zero longitudinal electric field (Ez = 0) but nonzero Hz. They exist for all frequencies above a cutoff frequency ωc, determined by boundary conditions. Below cutoff, the longitudinal wave vector becomes imaginary and modes are evanescent.

## Questions

```yaml
- question: "A rectangular waveguide is excited at a frequency between the cutoff of TE₁₀ and TE₂₀. A higher-order mode like TE₂₀ is also launched into the guide. What happens to the TE₂₀ mode?"
  type: multiple-choice
  options:
    - "It propagates but at a lower phase velocity than TE₁₀"
    - "It reflects back toward the source and interferes with the incident TE₁₀ mode"
    - "It decays exponentially along the guide, dying out within a few 'skin depths'"
    - "It propagates at the speed of light c, unlike the TE₁₀ mode"
  answer: 2
  explanation: "Below its cutoff frequency, the longitudinal wavenumber of TE₂₀ becomes imaginary: kz = iγ. The mode field then goes as e^(−γz) — evanescent decay, not propagation. No power is transported by the evanescent mode; it simply dies out over a short distance. This is directly analogous to quantum tunneling below a potential barrier or total internal reflection in optics. Single-mode operation exploits this: the guide is designed so only the dominant TE₁₀ is above cutoff, keeping all higher modes evanescent and the signal clean."

- question: "A TE mode in a rectangular waveguide is found to have a phase velocity of 1.8c at a particular frequency. Is this consistent with special relativity?"
  type: multiple-choice
  options:
    - "No — special relativity forbids any velocity exceeding c, so this is physically impossible"
    - "Yes — the phase velocity can exceed c because phase velocity does not carry information or energy; the group velocity remains below c"
    - "Yes — Maxwell's equations in guided structures supersede special relativity"
    - "No — a phase velocity above c means the mode is below its cutoff frequency and actually evanescent"
  answer: 1
  explanation: "Phase velocity vph = ω/kz > c is entirely consistent with special relativity. What special relativity forbids is transmitting *information* or *energy* faster than c. In a waveguide, energy travels at the group velocity vg = c²/vph, which is always less than c when vph > c. The phase velocity describes the rate at which a constant-phase surface moves — not the speed of any physical carrier. This is the same reason that the 'bright spot' from a spinning laser pointer can sweep a distant wall faster than c without violating relativity."

- question: "Increasing the cross-sectional width (a) of a rectangular waveguide lowers the cutoff frequency of the dominant TE₁₀ mode."
  type: true-false
  answer: true
  explanation: "The cutoff frequency for the TE_mn mode in a rectangular waveguide is ωc,mn = cπ√((m/a)² + (n/b)²). For TE₁₀ (m=1, n=0), this simplifies to ωc = cπ/a. Since ωc is inversely proportional to a, making the guide wider lowers the cutoff frequency. A larger guide supports lower frequencies in its dominant mode — which is why microwave waveguides for lower frequencies (e.g., the 1–2 GHz L band) are physically larger than those for millimeter waves."

- question: "A hollow metallic rectangular waveguide can support TEM modes (with both Ez = 0 and Hz = 0) if operated at sufficiently high frequencies."
  type: true-false
  answer: false
  explanation: "TEM modes require two separate conductors between which a static-like electric field can exist (as in coaxial cable). A hollow single-conductor waveguide cannot support TEM modes at any frequency. TEM modes require a zero cutoff frequency and a static solution between two conductors; a single hollow tube has no inner conductor for field lines to terminate on. This is why a hollow rectangular guide only supports TE and TM modes, never TEM — a fundamental topological constraint, not just an engineering limitation."

- question: "Explain what cutoff frequency means for a TE mode in a waveguide and what physically distinguishes operation above cutoff from operation below cutoff."
  type: short-answer
  answer: "Cutoff frequency is the minimum frequency at which a TE mode can propagate as a traveling wave. It arises from the discrete eigenvalues of the transverse Helmholtz equation imposed by the boundary conditions. Above cutoff, the longitudinal wavenumber kz = √(ω²/c² − kc²) is real — the mode carries power as a traveling wave. Below cutoff, kz becomes imaginary (iγ), and the mode decays exponentially as e^(−γz) — it is evanescent and carries no net power along the guide."
  explanation: "The cutoff is not an arbitrary design choice but a mathematical consequence of the boundary conditions. Each mode has its own characteristic transverse wavenumber kc,mn (the eigenvalue), and propagation requires ω > c·kc,mn. Below this threshold, the guide acts like a high-pass filter for that mode. The physical picture: the mode is trying to bounce between the walls at an angle, and below cutoff the geometry simply does not allow a self-consistent traveling pattern to form — only a spatially decaying one."
```

## Explainer

From your prerequisite on waveguide equations, you know that a hollow metallic waveguide supports guided waves by confining the electromagnetic field between conducting walls. The general solution strategy is to decompose the field into a longitudinal part (along the propagation axis z) and transverse parts (in the xy-plane), then classify modes by which longitudinal components are nonzero. **Transverse electric (TE) modes** are defined by the condition Ez = 0: the electric field has no component along the propagation direction, but the magnetic field does (Hz ≠ 0). This is in contrast to TM modes (Hz = 0, Ez ≠ 0) and TEM modes (both zero, which require two separate conductors).

The defining feature of TE modes is the **cutoff frequency**. Substituting Ez = 0 into Maxwell's equations and applying the conducting boundary conditions (tangential E = 0 at the walls) forces Hz to satisfy a two-dimensional Helmholtz equation in the cross-section with Neumann boundary conditions (∂Hz/∂n = 0 at the walls). The eigenvalues of this problem are discrete, labeled by integers (m, n) for a rectangular guide, and each eigenvalue determines a **cutoff frequency** ωc,mn. For a rectangular waveguide of dimensions a × b, the cutoff frequencies are ωc,mn = c·π√((m/a)² + (n/b)²). The mode with the lowest cutoff is called the **dominant mode** — for a rectangular guide it is TE₁₀.

Above the cutoff frequency, the longitudinal wavenumber kz = √(ω²/c² − kc²) is real and positive, meaning the mode propagates along the guide as a traveling wave with phase velocity vph = ω/kz > c. (The group velocity vg = c²/vph < c; information travels at group velocity.) Below cutoff, kz becomes imaginary: kz = iγ with γ real and positive. The mode decays exponentially as e^(−γz) — it is **evanescent** rather than propagating. This is analogous to total internal reflection in optics or quantum tunneling below a barrier: the mode tries to propagate but is forbidden by the boundary geometry, and instead decays within a few skin depths.

In practice, a waveguide is typically operated in a frequency range where only the dominant TE₁₀ mode propagates, while all higher modes are below their cutoffs and thus evanescent. This single-mode operation avoids interference between modes and preserves signal integrity. Understanding TE modes — how to identify them, compute their cutoff frequencies, and determine their field patterns — is foundational for designing microwave components including filters, horns, cavities, and antenna feeds.
