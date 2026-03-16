---
id: resonance-and-resonance-frequency
title: Resonance and Resonance Frequency
domain: physics
course: classical-mechanics
prerequisites:
- id: driven-harmonic-oscillator
  type: hard
- id: complex-numbers-intro
  type: soft
tags:
- resonance
- oscillations
- frequency
- amplification
stage: formal-systems
status: draft
---

# Resonance and Resonance Frequency

## Core Idea
Resonance occurs when the driving frequency matches the natural frequency (or close to it), producing a large-amplitude steady-state oscillation. The sharpness and height of the resonance peak depend on damping: less damping yields a sharper, taller peak (high quality factor Q). Resonance is exploited in radio tuning and mechanical systems but must be avoided in structures (buildings, bridges) to prevent dangerous vibrations.

## Explainer

From driven harmonic oscillators, you know the setup: a mass-spring system (or equivalent) with natural frequency ω₀, damping coefficient γ, driven by an external periodic force F₀cos(ωt). The steady-state amplitude depends on both ω and ω₀. **Resonance** is the phenomenon that occurs when these frequencies nearly coincide — and understanding why amplitudes become large at resonance is the physical heart of the concept.

The intuition is about energy transfer. When you push a child on a swing, you push in time with the swing's natural motion. Each push adds energy to the oscillation; the amplitude grows. If you pushed randomly — sometimes with the swing, sometimes against it — energy would average out and amplitude would stay small. Resonance is the perfect synchronization of driving force and natural motion: energy pumped in from the driving force is consistently reinforced rather than periodically canceled, so amplitude grows until damping limits it. The **resonance frequency** (strictly, the frequency of maximum amplitude) is close to ω₀ — slightly shifted by damping, but approaching ω₀ as damping decreases toward zero.

The **quality factor Q** encodes the sharpness of resonance. A high-Q oscillator has low damping: it rings for a long time when struck, has a sharp resonance peak (large amplitude near ω₀, small amplitude far from it), and tunes selectively. A radio receiver circuit is a high-Q oscillator tuned to resonate at a specific carrier frequency — it responds strongly to that frequency and weakly to all others, implementing frequency selection. A low-Q oscillator (heavily damped, like a car's shock absorber) has a broad, low resonance peak; it damps vibrations across a wide frequency range rather than selectively amplifying one. Q characterizes both frequency selectivity and the duration of free oscillation: Q ≈ ω₀τ/2 where τ is the decay time.

Complex numbers illuminate resonance cleanly. A sinusoidal driving force can be written as Re[F₀e^{iωt}], and the steady-state response as Re[A(ω)e^{iωt}]. The complex amplitude A(ω) = F₀/m(ω₀² − ω² + iγω) is a rational function of ω. Its magnitude |A(ω)| is the actual oscillation amplitude; its phase gives the lag between force and response. The resonance peak is where the denominator |ω₀² − ω² + iγω| is minimized — visually, where the pole of A(ω) in the complex ω-plane is closest to the real axis. This pole structure elegantly captures both the location and width of the resonance peak.

Resonance is ubiquitous and consequential. In structural engineering it is a hazard: the Tacoma Narrows Bridge collapse (1940) involved wind-driven oscillation near a structural resonance frequency. In medical imaging, nuclear magnetic resonance (NMR/MRI) drives proton spins at their resonance frequency to generate tissue images. In lasers and optical cavities, resonance conditions determine which wavelengths are amplified. In music, resonance amplifies strings, air columns, and drum heads. The principle is always the same: when driving frequency matches natural frequency, small inputs produce large outputs — a feature to exploit or avoid depending on the application.
