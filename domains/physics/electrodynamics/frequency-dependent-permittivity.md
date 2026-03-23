---
id: frequency-dependent-permittivity
title: Frequency-Dependent Permittivity and Dispersion
domain: physics
course: electrodynamics
prerequisites:
- id: dielectric-susceptibility-permittivity
  type: hard
- id: electromagnetic-waves
  type: hard
builds-toward:
- em-waves-anisotropic-media
- conductivity-complex-dielectric
tags:
- dispersion
- refractive-index
- frequency-response
stage: expert
status: validated
---

# Frequency-Dependent Permittivity and Dispersion

## Core Idea
The permittivity ε(ω) becomes frequency-dependent due to the inertia of charges and damping mechanisms. This causes phase velocity to differ from group velocity and enables phenomena like dispersion, anomalous refraction, and material absorption.

## Explainer

From your study of dielectric susceptibility, you know that a static electric field polarizes a dielectric: the bound charges shift slightly, creating dipole moments that reduce the internal field. In the static case, the polarization P follows the field instantaneously because there is no dynamics to consider. But when the applied field oscillates at angular frequency ω, the charges need time to respond — and that inertia changes everything.

The simplest model is the **Lorentz oscillator**: treat each bound electron as a mass on a spring (the restoring force from the nucleus) subject to a driving force (the oscillating electric field) and a damping force (radiation and collisions). The equation of motion is exactly the driven damped harmonic oscillator from classical mechanics: mẍ + mγẋ + mω₀²x = eE(t). Solving in the frequency domain gives x(ω) ∝ E(ω) / (ω₀² − ω² − iγω). The polarization P = nex is proportional to x, so the **susceptibility χ(ω)** and therefore the **permittivity ε(ω) = ε₀[1 + χ(ω)]** inherit this complex frequency dependence. The real part of ε governs dispersion (how refractive index varies with frequency); the imaginary part governs absorption (how quickly a wave's amplitude decays as it propagates).

Three frequency regimes emerge. Far below resonance (ω ≪ ω₀), the electrons follow the field quasi-statically and ε is real and greater than ε₀ — normal transparent behavior. Near resonance (ω ≈ ω₀), the imaginary part peaks, meaning the material strongly absorbs that frequency. Far above resonance (ω ≫ ω₀), the electrons cannot keep up at all; their contribution to polarization vanishes, and in the extreme limit (as in X-rays through glass) ε approaches ε₀, effectively free space. This is why glass is opaque to UV despite being transparent to visible light: UV frequencies hit electronic resonances that X-rays pass right through.

**Dispersion** — the variation of refractive index n(ω) = √(ε(ω)/ε₀) with frequency — has two important consequences for wave propagation that you will need. The **phase velocity** v_p = c/n(ω) is the speed at which a pure monochromatic wave's phase fronts travel, and it varies with ω. The **group velocity** v_g = dω/dk is the speed at which a wavepacket (a superposition of nearby frequencies) travels, and it is this velocity that carries information and energy. In a dispersive medium v_g ≠ v_p, and a short pulse launched into a dispersive medium spreads out as its frequency components travel at different speeds — the phenomenon of **pulse dispersion** that limits bandwidth in optical fibers and is exploited in prisms to separate colors.

## Questions

```yaml
- question: "At frequencies well above all resonances of a material, what happens to the permittivity, and what does this imply for the refractive index?"
  type: short-answer
  answer: "ε(ω) → ε₀ from below as ω → ∞, meaning the real part of ε can drop below ε₀ (and even below zero near plasma frequency for conductors). The refractive index n = √(ε/ε₀) approaches 1. Physically, the charges are too slow to respond, so the material becomes transparent and behaves like vacuum."
  explanation: "This is why high-energy X-rays are transmitted through most materials with little interaction — the photon frequency far exceeds any electronic resonance. The result also explains why the refractive index of glass decreases toward 1 as you go to shorter wavelengths past the UV absorption band."

- question: "A dielectric has a strong absorption resonance at frequency ω₀. Describe qualitatively how the real part of the refractive index behaves just below and just above ω₀."
  type: short-answer
  answer: "Just below ω₀, the real part of n increases with frequency (normal dispersion — common in transparent materials). Just above ω₀, it decreases sharply (anomalous dispersion). This dip in n just above the resonance is accompanied by high absorption. The group velocity can become very small or even negative in the anomalous dispersion region."
  explanation: "This behavior is a signature of any driven resonator: the response function has a characteristic shape where the real part (dispersion) goes through a steep S-curve centered on the resonance while the imaginary part (absorption) peaks at ω₀. In optics, anomalous dispersion is observed in materials excited near absorption lines and is exploited in slow-light experiments."
```
