---
id: refractive-index-and-dispersion
title: Refractive Index and Dispersion
domain: physics
course: electrodynamics
prerequisites:
- id: dispersion-relations-em-waves
  type: hard
- id: electromagnetic-waves-in-dielectrics
  type: hard
tags:
- refractive-index
- dispersion
- material-response
stage: advanced
status: draft
---

# Refractive Index and Dispersion

## Core Idea
The refractive index n(ω) describes how fast electromagnetic waves propagate in a medium relative to vacuum, embodying the material's electromagnetic response. The frequency-dependence n(ω) (normal dispersion: dn/dω > 0, or anomalous: dn/dω < 0) causes different colors to refract differently, explaining chromatic aberration, prism spectra, and material absorption. Real refractive indices exhibit rich frequency dependence connecting to atomic resonances and electronic band structure.

## Explainer

You already know that electromagnetic waves in a dielectric propagate at a speed v = c/√(εᵣμᵣ), where εᵣ and μᵣ are the relative permittivity and permeability of the medium. For most optical materials μᵣ ≈ 1, so v ≈ c/√εᵣ. The **refractive index** n is defined as n = c/v, so n = √εᵣ for these materials. Because εᵣ is not a simple constant — it depends on frequency — so does n. This frequency dependence is **dispersion**, and it arises because the medium's electric polarization response is not instantaneous.

The physical picture comes from the **dispersion relation** you studied: the bound electrons in the material behave like harmonic oscillators with natural resonance frequencies ω₀. When a wave drives them at angular frequency ω, their oscillation amplitude and phase depend on how close ω is to ω₀. Far below resonance, the electrons follow the driving field with a small phase lag, and they reinforce the polarization in a way that slows the wave (n > 1). This is **normal dispersion**: n increases with frequency (dn/dω > 0), which means shorter wavelengths (higher frequency, bluer colors) travel more slowly. Far above resonance, the electrons can barely follow the rapidly oscillating field; the refractive index approaches 1 from below and eventually n < 1 near resonance (phase velocity exceeds c, which is allowed because no information travels at phase velocity).

Near a resonance, the behavior becomes dramatic: n changes rapidly and the imaginary part of the dielectric function (absorption) peaks. This region of **anomalous dispersion** (dn/dω < 0) is associated with strong absorption. Between resonances, the medium returns to normal dispersion. For glass in the visible spectrum, all the important resonances lie in the ultraviolet, so glass shows normal dispersion throughout the visible range: blue light has higher n than red, meaning blue refracts more. This is why a prism spreads white light into a spectrum with violet on the high-n (high-angle) side, and why lenses suffer from **chromatic aberration** — different colors focus at slightly different points.

The dispersion also connects to signal propagation. A **phase velocity** v_phase = c/n tells you how fast a particular frequency component travels. But a real pulse contains many frequencies, and its energy envelope travels at the **group velocity** v_group = dω/dk = c/(n + ω dn/dω). In normal dispersion (dn/dω > 0), the group velocity is less than the phase velocity — the pulse travels more slowly than the wave crests within it. In anomalous dispersion near a resonance, the group velocity can exceed c or even become negative (the peak of the pulse appears to exit the medium before it enters), though this never violates causality because the signal is distorted. Mastering the distinction between phase and group velocity, and the role of n(ω) in each, is the gateway to understanding optical fibers, ultrashort pulse propagation, and the material basis of color.
