---
id: waveguide-equations-general
title: Waveguide Field Equations
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: separation-of-variables-elliptic-equations
  type: hard
builds-toward:
- transverse-electric-modes
- transverse-magnetic-modes
tags:
- waveguides
- guided-modes
- dispersion-relations
stage: expert
status: draft
---

# Waveguide Field Equations

## Core Idea
Waveguide modes satisfy Maxwell's equations with boundary conditions on conductor walls. Separating longitudinal and transverse components, modes are determined by transverse field patterns, leading to dispersion relations relating ω and k_z and cutoff frequencies.

## Questions

```yaml
- question: "An engineer wants to transmit a 5 GHz microwave signal through a rectangular waveguide whose dominant mode has a cutoff frequency of 6 GHz. What will happen to the signal?"
  type: multiple-choice
  options:
    - "The signal propagates normally because 5 GHz is close enough to the cutoff"
    - "The signal propagates but at reduced speed compared to free space"
    - "The signal decays exponentially along the waveguide and does not propagate"
    - "The signal reflects back toward the source and sets up a standing wave"
  answer: 2
  explanation: "Below the cutoff frequency ω_c = k_c · c, the dispersion relation k_z² = (ω/c)² − k_c² gives a negative value for k_z², making k_z imaginary. An imaginary k_z means the field varies as e^(−|k_z|z) — exponential decay, not propagation. This is an evanescent mode. The signal does not travel through the waveguide; it is attenuated exponentially from the input. This is the key engineering constraint: waveguide dimensions must be chosen so the operating frequency sits above the dominant-mode cutoff."

- question: "Why can a single hollow rectangular waveguide (one metal tube, no inner conductor) not support a TEM mode?"
  type: multiple-choice
  options:
    - "Because the rectangular geometry forces the fields to be purely transverse"
    - "Because TEM modes require a second conductor to complete the return current path"
    - "Because TEM modes have zero cutoff frequency, which conflicts with the waveguide's boundary conditions"
    - "Because the metal walls absorb transverse field components"
  answer: 1
  explanation: "A TEM (transverse electromagnetic) mode has both E and B purely transverse to the propagation direction. By Ampere's law, a purely transverse B field requires a longitudinal current, which must flow on a conductor. In a coaxial cable, the inner conductor provides this return path. A hollow waveguide with only one conductor (the outer tube) has no inner conductor, so TEM cannot exist. Instead, waveguides support TE modes (E_z = 0, B_z ≠ 0) or TM modes (B_z = 0, E_z ≠ 0), where one field component is longitudinal and drives the transverse fields."

- question: "In a waveguide, once you solve the 2D eigenvalue problem for the single longitudinal field component (E_z for TM or B_z for TE), all transverse field components can be determined from it algebraically."
  type: true-false
  answer: true
  explanation: "This is correct and is one of the most powerful structural features of waveguide analysis. After separating longitudinal and transverse dependencies, Maxwell's equations reduce to a 2D Helmholtz equation for the longitudinal component. Once that equation is solved (giving the mode shape and the cutoff wavenumber k_c), the transverse components E_x, E_y, B_x, B_y follow directly from algebraic relationships involving k_z, k_c, and the longitudinal component and its derivatives. This is why the mode is fully characterized by solving a single scalar PDE."

- question: "The cutoff frequency of a waveguide mode is determined primarily by the length of the waveguide rather than its cross-sectional dimensions."
  type: true-false
  answer: false
  explanation: "The cutoff frequency is determined entirely by the transverse geometry — the cross-sectional shape and dimensions of the waveguide. The cutoff wavenumber k_c is the eigenvalue of the 2D Helmholtz equation solved on the cross-section with boundary conditions on the walls. For a rectangular waveguide of width a and height b, the TE_{mn} cutoff wavenumber is k_c = π√((m/a)² + (n/b)²). Length affects the longitudinal standing wave structure in a cavity resonator, but not the cutoff frequencies of propagating modes."

- question: "What physically happens to an electromagnetic wave whose frequency is below the cutoff frequency of all modes in a waveguide, and why does the dispersion relation predict this?"
  type: short-answer
  answer: "The wave does not propagate — it decays exponentially along the waveguide length (evanescent behavior). The dispersion relation k_z² = (ω/c)² − k_c² gives a negative value when ω < ω_c = k_c·c, so k_z is imaginary. Writing k_z = iα (α real and positive), the longitudinal dependence becomes e^(ikzz) = e^(−αz) — exponential decay rather than oscillation. No energy is transmitted along the waveguide; the field is localized near the input and falls off on a scale of 1/α."
  explanation: "The evanescent nature below cutoff is a direct consequence of the dispersion relation. The transverse eigenvalue k_c² comes from the geometry and boundary conditions; it is fixed. The longitudinal propagation constant k_z must then satisfy k_z² = (ω/c)² − k_c². When the wave frequency ω is too low, (ω/c)² < k_c², and k_z must be imaginary. This is not attenuation due to absorption — a perfect conductor waveguide has no resistive loss — but a geometric constraint: the transverse standing wave pattern requires a minimum frequency to exist as a propagating mode."
```

## Explainer

A waveguide is a metal tube — rectangular, circular, or other cross-section — designed to guide electromagnetic waves along its length. Unlike a coaxial cable which has two conductors, a simple hollow waveguide has only one conductor (the outer tube). This changes the physics fundamentally: a waveguide cannot support a simple TEM (transverse electromagnetic) wave where both E and B are purely transverse, because that mode requires a second conductor for the return current. Instead, waveguides support modes where at least one field component points along the propagation direction.

The general strategy is to write E and B as products of a transverse profile function and a longitudinal traveling wave: **E(x,y,z,t) = E_t(x,y) e^(ikz − iωt)**. Substituting into Maxwell's equations and separating longitudinal (z) and transverse (x,y) components gives a 2D eigenvalue problem for the transverse profile. For **TE modes** (transverse electric, B_z ≠ 0, E_z = 0), you solve ∇²_t B_z + k_c² B_z = 0 with Neumann boundary conditions on the walls. For **TM modes** (transverse magnetic, E_z ≠ 0, B_z = 0), you solve ∇²_t E_z + k_c² E_z = 0 with Dirichlet conditions. Each eigenvalue k_c is a **cutoff wavenumber**, and all transverse components can be derived algebraically from the single z-component once it is known.

The **dispersion relation** for a waveguide mode is k_z² = (ω/c)² − k_c², where k_c is the cutoff wavenumber from the transverse eigenvalue problem. This is the central result. Below the **cutoff frequency** ω_c = k_c · c, the quantity (ω/c)² − k_c² is negative, so k_z is imaginary — the mode does not propagate but decays exponentially (it is evanescent). Above cutoff, k_z is real and the mode propagates. Each geometry has a discrete ladder of cutoff frequencies; the dominant mode (lowest k_c) propagates by itself over a frequency band before the next mode turns on. Microwave engineers design waveguide dimensions specifically so that the operating frequency sits above the dominant mode cutoff but below the next mode cutoff, ensuring single-mode propagation.

The connection to your prerequisites is direct. Separation of variables — which you know for elliptic equations — is precisely what separates the transverse eigenvalue problem from the longitudinal propagation. The transverse equation is a Helmholtz equation on the cross-sectional geometry, and the boundary conditions enforce perfect-conductor conditions (E_tan = 0, B_n = 0). Each solution (mode) is like an eigenfunction of the transverse problem, carrying energy independently of the other modes. When you move to cavity resonators, you add end-cap boundary conditions in the z-direction, quantizing k_z as well and replacing the continuous propagation spectrum with a discrete set of resonant frequencies.
