---
id: compton-scattering-analysis
title: 'Compton Scattering: Energy and Momentum Analysis'
domain: physics
course: modern-physics
prerequisites:
- id: compton-scattering
  type: soft
- id: photon-model
  type: hard
- id: relativistic-momentum-energy
  type: soft
tags:
- photons
- wave-particle-duality
- scattering
stage: advanced
status: draft
---

# Compton Scattering: Energy and Momentum Analysis

## Core Idea
In Compton scattering, a photon collides with an electron and bounces off at an angle θ, with the electron recoiling. Conservation of energy and momentum gives the Compton formula: λ' − λ = (h/mc)(1 − cosθ), where h/mc ≈ 2.43 pm is the Compton wavelength. The wavelength shift depends on scattering angle but not on initial photon energy, providing direct evidence that photons carry momentum p = E/c.

## How It's Best Learned
Derive the Compton formula from energy-momentum conservation. Work through several scattering angles and compare predicted wavelength shifts with experimental data. Discuss why Compton scattering is compelling evidence for the photon model.

## Common Misconceptions
The wavelength shift depends on the scattering angle, not the type of material. High-energy gamma rays show larger fractional shifts (the absolute shift h/mc is constant).

## Explainer

Before Compton's experiment, the prevailing classical model treated X-rays as waves scattering off electrons. Classical scattering predicts that the scattered wave should have the *same* wavelength as the incident wave — the electron just re-radiates at the driven frequency. Compton measured scattered X-rays at various angles and found that the wavelength increased — the scattered photons had less energy. This "extra" wavelength could not be explained classically. The explanation requires treating X-rays as **photons**: discrete quanta with energy E = hf = hc/λ and momentum p = h/λ = E/c, the relationship you know from the photon model.

The derivation treats the collision as a billiard-ball problem in special relativity. A photon with initial wavelength λ strikes an electron at rest. The photon scatters off at angle θ, with new wavelength λ′; the electron recoils at some angle. Apply conservation of energy (relativistic) and conservation of momentum in both x and y directions — three equations for the unknowns. After algebraic manipulation (the key step is eliminating the electron's recoil angle), you arrive at the **Compton formula**: Δλ = λ′ − λ = (h/mₑc)(1 − cosθ). The factor h/mₑc ≈ 2.43 pm is the **Compton wavelength** of the electron, the natural length scale for electron-photon scattering.

Two features of this formula are worth absorbing deeply. First, Δλ depends only on θ, not on the initial wavelength λ. A low-energy visible photon and a high-energy gamma ray scattering at the same angle produce the *same absolute wavelength shift*. The gamma ray's fractional shift (Δλ/λ) is tiny; the X-ray's fractional shift is significant — which is why Compton saw the effect clearly at X-ray wavelengths and not with visible light. Second, Δλ = 0 at θ = 0° (forward scattering, no collision) and Δλ = 2h/mₑc at θ = 180° (backscattering, maximum energy transfer). This angular dependence is the clean experimental signature that the photon is carrying momentum like a particle.

Compton scattering was decisive evidence for the **particle nature of light** precisely because classical wave theory had no room for a wavelength shift. It also showed that relativistic energy-momentum conservation applies to photons. Combined with the photoelectric effect, it established that electromagnetic radiation exchanges energy and momentum in discrete quanta — photons — that behave as particles in collision events even while exhibiting wave behavior in interference and diffraction. The Compton wavelength h/mc also has a deeper significance: it sets the scale at which quantum mechanics and relativity both become important for a particle of mass m, which is why it appears throughout quantum field theory.
