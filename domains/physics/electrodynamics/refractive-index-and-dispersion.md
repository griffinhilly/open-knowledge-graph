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
stage: expert
status: draft
---

# Refractive Index and Dispersion

## Core Idea
The refractive index n(ω) describes how fast electromagnetic waves propagate in a medium relative to vacuum, embodying the material's electromagnetic response. The frequency-dependence n(ω) (normal dispersion: dn/dω > 0, or anomalous: dn/dω < 0) causes different colors to refract differently, explaining chromatic aberration, prism spectra, and material absorption. Real refractive indices exhibit rich frequency dependence connecting to atomic resonances and electronic band structure.

## Questions

```yaml
- question: "A glass prism separates white light into a spectrum. Which color exits the prism at the largest deflection angle, and what property of the glass causes this?"
  type: multiple-choice
  options:
    - "Red light, because red has the longest wavelength and is therefore deflected most by wave-mechanical effects"
    - "Violet/blue light, because glass exhibits normal dispersion in the visible range — higher frequency means higher refractive index, so blue light refracts more"
    - "Red light, because higher energy photons penetrate deeper into the glass and are deflected by more interactions"
    - "All colors exit at the same angle; the spectrum is created by internal interference effects, not differential refraction"
  answer: 1
  explanation: "In glass, all important atomic resonances lie in the ultraviolet — well above visible frequencies. This places the entire visible spectrum in the normal dispersion regime (dn/dω > 0), where higher-frequency (shorter-wavelength, bluer) light experiences a higher refractive index. A higher n means a greater phase velocity reduction (v = c/n), and by Snell's law, a larger refraction angle. So violet/blue light bends more than red at the glass-air interface, and exits at a larger angle relative to the original beam direction. The spectrum with violet on the high-angle side is characteristic of normal dispersion in glass."

- question: "In a medium with normal dispersion (dn/dω > 0), how does the group velocity of a pulse compare to the phase velocity of the individual frequency components?"
  type: multiple-choice
  options:
    - "Group velocity equals phase velocity; dispersion affects wavelength but not propagation speed"
    - "Group velocity is greater than phase velocity, because the pulse envelope moves faster than the wave crests"
    - "Group velocity is less than phase velocity; the pulse envelope moves more slowly than the wave crests within it"
    - "Group velocity exceeds the speed of light c, because the interference of dispersed frequencies accelerates the envelope"
  answer: 2
  explanation: "Group velocity is v_group = dω/dk = c/(n + ω dn/dω). In normal dispersion, dn/dω > 0, so the denominator n + ω(dn/dω) is larger than n alone, meaning v_group = c/(larger number) < c/n = v_phase. The pulse envelope travels more slowly than the individual wave crests it contains — you can imagine the crests 'walking through' the pulse envelope from the back to the front. This has practical consequences for fiber optic communication: a pulse containing multiple frequencies spreads out in time as it travels, because different frequency components move at different phase velocities."

- question: "The frequency-dependence of the refractive index — dispersion — arises because the bound electrons in a material cannot respond instantaneously to the oscillating electromagnetic field."
  type: true-false
  answer: true
  explanation: "The physical origin of dispersion is the resonance behavior of bound electrons modeled as harmonic oscillators. When driven at frequency ω, their oscillation amplitude and phase depend on the proximity of ω to the natural resonance ω₀. The response is not instantaneous: electrons have inertia and a restoring force, so their displacement lags behind the driving field by a frequency-dependent phase. This phase lag determines the polarization response of the medium, which is encoded in the complex permittivity ε(ω), and hence in n(ω). If the response were instantaneous (perfect following), n would be frequency-independent and there would be no dispersion."

- question: "Near an atomic resonance frequency, a material exhibits anomalous dispersion (dn/dω < 0) and low optical absorption, since the energy is being used to drive the resonance rather than being absorbed."
  type: true-false
  answer: false
  explanation: "Near resonance, anomalous dispersion (dn/dω < 0) and *strong* absorption occur together — they are two manifestations of the same resonance phenomenon. When the driving frequency ω is close to ω₀, the electrons are driven efficiently and absorb energy from the field (high imaginary part of ε). The rapid change in refractive index (anomalous dispersion) and the absorption peak are both consequences of the resonance response. Far from resonance — in the transparent regions between resonances — the material exhibits normal dispersion and low absorption. The misconception arises from thinking dispersion and absorption are independent; the Kramers-Kronig relations formally connect them."

- question: "Explain why the group velocity of a pulse in a dispersive medium differs from the phase velocity of its individual frequency components, and what determines whether the group velocity is larger or smaller than the phase velocity."
  type: short-answer
  answer: "Phase velocity v_phase = c/n(ω) is the speed at which a single-frequency wave crest propagates. A real pulse contains a range of frequencies, and its energy envelope travels at the group velocity v_group = dω/dk. Since k = nω/c, we get v_group = c/(n + ω dn/dω). In normal dispersion (dn/dω > 0), the extra term ω dn/dω is positive, making the denominator larger than n, so v_group < v_phase. In anomalous dispersion (dn/dω < 0), the denominator is smaller, so v_group > v_phase — the envelope moves faster than individual crests. This is not a violation of relativity: information cannot travel faster than c because anomalous dispersion is always accompanied by absorption that distorts the pulse."
  explanation: "The distinction between phase and group velocity is fundamental to understanding how signals propagate in real media. Phase velocity tells you how fast a pattern of oscillations moves; group velocity tells you how fast the modulation (information) moves. In a non-dispersive medium (dn/dω = 0), they are equal. Dispersion separates them, and this separation has engineering consequences: pulse spreading (group velocity dispersion) limits the bandwidth of optical fiber communications, and designers must engineer dispersion-shifted fibers to minimize pulse broadening over long distances."
```

## Explainer

You already know that electromagnetic waves in a dielectric propagate at a speed v = c/√(εᵣμᵣ), where εᵣ and μᵣ are the relative permittivity and permeability of the medium. For most optical materials μᵣ ≈ 1, so v ≈ c/√εᵣ. The **refractive index** n is defined as n = c/v, so n = √εᵣ for these materials. Because εᵣ is not a simple constant — it depends on frequency — so does n. This frequency dependence is **dispersion**, and it arises because the medium's electric polarization response is not instantaneous.

The physical picture comes from the **dispersion relation** you studied: the bound electrons in the material behave like harmonic oscillators with natural resonance frequencies ω₀. When a wave drives them at angular frequency ω, their oscillation amplitude and phase depend on how close ω is to ω₀. Far below resonance, the electrons follow the driving field with a small phase lag, and they reinforce the polarization in a way that slows the wave (n > 1). This is **normal dispersion**: n increases with frequency (dn/dω > 0), which means shorter wavelengths (higher frequency, bluer colors) travel more slowly. Far above resonance, the electrons can barely follow the rapidly oscillating field; the refractive index approaches 1 from below and eventually n < 1 near resonance (phase velocity exceeds c, which is allowed because no information travels at phase velocity).

Near a resonance, the behavior becomes dramatic: n changes rapidly and the imaginary part of the dielectric function (absorption) peaks. This region of **anomalous dispersion** (dn/dω < 0) is associated with strong absorption. Between resonances, the medium returns to normal dispersion. For glass in the visible spectrum, all the important resonances lie in the ultraviolet, so glass shows normal dispersion throughout the visible range: blue light has higher n than red, meaning blue refracts more. This is why a prism spreads white light into a spectrum with violet on the high-n (high-angle) side, and why lenses suffer from **chromatic aberration** — different colors focus at slightly different points.

The dispersion also connects to signal propagation. A **phase velocity** v_phase = c/n tells you how fast a particular frequency component travels. But a real pulse contains many frequencies, and its energy envelope travels at the **group velocity** v_group = dω/dk = c/(n + ω dn/dω). In normal dispersion (dn/dω > 0), the group velocity is less than the phase velocity — the pulse travels more slowly than the wave crests within it. In anomalous dispersion near a resonance, the group velocity can exceed c or even become negative (the peak of the pulse appears to exit the medium before it enters), though this never violates causality because the signal is distorted. Mastering the distinction between phase and group velocity, and the role of n(ω) in each, is the gateway to understanding optical fibers, ultrashort pulse propagation, and the material basis of color.
