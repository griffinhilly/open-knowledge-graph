---
id: cavity-resonator-quality-factor
title: Quality Factor and Energy Dissipation in Cavities
domain: physics
course: electrodynamics
prerequisites:
- id: cavity-resonator-solutions
  type: hard
- id: em-field-energy-conservation
  type: soft
tags:
- quality-factor
- damping
- bandwidth
- dissipation
stage: advanced
status: draft
---

# Quality Factor and Energy Dissipation in Cavities

## Core Idea
The quality factor Q = ω₀(stored energy)/(dissipated power) characterizes cavity losses. Finite conductivity and dielectric losses broaden resonances; the bandwidth Δω = ω₀/Q relates inverse Q to fractional bandwidth. High-Q cavities are needed for narrowband filtering and frequency standards.

## Explainer

You know from cavity resonator solutions that a perfectly conducting, closed metal box supports discrete modes — standing electromagnetic waves at specific resonant frequencies determined by the cavity geometry. That analysis assumed zero resistance in the walls. Real cavities have finite conductivity, and this small imperfection turns a perfectly sharp resonance into a narrow but finite one. The **quality factor Q** is the single number that characterizes how sharp (or how lossy) that resonance is.

Think first of a mechanical analogy you may know: a guitar string vibrates at a natural frequency and gradually decays. The decay happens because energy is lost to air resistance and internal friction. Define Q = 2π × (energy stored) / (energy lost per cycle). A high-Q oscillator rings for many cycles before its amplitude falls significantly; a low-Q one damps out quickly. For electromagnetic cavities the definition is the same but expressed per radian: **Q = ω₀ × U / P_loss**, where U is the total stored electromagnetic energy (both electric and magnetic) and P_loss is the average power being dissipated. The ω₀ factor converts "per cycle" to "per radian."

Where does the energy go in a cavity? The dominant mechanism is **ohmic loss in the cavity walls**. The magnetic field of the resonant mode penetrates the conducting walls to a depth equal to the skin depth δ = √(2/μσω). The oscillating field in this thin layer drives currents, which dissipate energy via Joule heating. The thinner δ is (i.e., the better the conductor), the less energy is lost per cycle and the higher Q becomes. Dielectric losses in any filling material add a second loss channel through the imaginary part of the permittivity.

The connection between Q and bandwidth is straightforward. Near resonance the cavity's response follows a Lorentzian lineshape, and the **half-power bandwidth** Δω (the frequency range over which stored energy exceeds half its peak value) satisfies Δω = ω₀/Q. A cavity with Q = 10,000 at 10 GHz has a bandwidth of 1 MHz — it responds efficiently only to signals within that window. This is why high-Q cavities are used as frequency-selective filters in microwave systems and as frequency standards in atomic clocks: a higher Q means greater frequency discrimination and lower phase noise. Practical copper cavities achieve Q ~ 10³–10⁴; superconducting cavities reach Q ~ 10¹⁰ by nearly eliminating resistive loss.
