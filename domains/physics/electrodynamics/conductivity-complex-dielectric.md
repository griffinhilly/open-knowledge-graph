---
id: conductivity-complex-dielectric
title: Complex Conductivity and Dielectric Function
domain: physics
course: electrodynamics
prerequisites:
- id: drude-model-conductivity
  type: hard
- id: frequency-dependent-permittivity
  type: hard
builds-toward:
- em-waves-anisotropic-media
tags:
- complex-permittivity
- kramers-kronig
- absorption
stage: expert
status: validated
---

# Complex Conductivity and Dielectric Function

## Core Idea
The complex permittivity ε(ω) = ε'(ω) + iε''(ω) encodes both oscillatory response and dissipation. The imaginary part ε''(ω) directly relates to conductivity and absorption coefficient through Kramers-Kronig relations.

## Questions

```yaml
- question: "A material's reflectance is measured across a wide frequency range, yielding the absorption spectrum ε''(ω). What else can be determined from this data alone, and why?"
  type: multiple-choice
  options:
    - "Nothing — the refractive index and absorption coefficient are independent material properties"
    - "The DC conductivity, but not the frequency-dependent permittivity"
    - "The real part of the permittivity ε'(ω), because Kramers-Kronig relations link ε' and ε'' via causality"
    - "The density of free electrons, because absorption is proportional to carrier concentration"
  answer: 2
  explanation: "The Kramers-Kronig relations state that ε'(ω) and ε''(ω) are a Hilbert transform pair — knowing one across all frequencies determines the other. This connection arises from causality: the material's polarization response cannot precede the driving field. In practice, measuring absorption across a broad spectrum and applying Kramers-Kronig integration gives the refractive index spectrum. This is how optical constants of real materials are determined experimentally from reflectance data alone."

- question: "The imaginary part of the complex permittivity ε''(ω) is physically associated with:"
  type: multiple-choice
  options:
    - "The energy stored per cycle in the polarization of the medium — the reactive, in-phase response"
    - "The energy dissipated per cycle as the electromagnetic wave propagates through the medium"
    - "The phase velocity of electromagnetic waves in the medium"
    - "The number density of free charge carriers contributing to conduction"
  answer: 1
  explanation: "ε''(ω) describes the out-of-phase, dissipative component of the medium's response to the driving field — the part that converts electromagnetic energy into heat. A large ε'' means strong absorption per cycle and rapid attenuation of the wave (short skin depth). ε'(ω) (the real part) describes the in-phase, reactive response — energy stored and returned per cycle — which governs the phase velocity and refractive index."

- question: "A material transparent in the visible range (ε'' ≈ 0 at visible frequencies) must have a structurally featureless real permittivity ε'(ω) at those same frequencies, since there is no local absorption to drive any dispersion."
  type: true-false
  answer: false
  explanation: "The Kramers-Kronig relations guarantee the opposite: absorption features (peaks in ε'') at other frequencies — in the UV or IR — produce dispersive features in ε' at those frequencies, and the integral over all frequencies determines ε' everywhere, including in the transparent window. A material can be transparent at visible frequencies while having absorption bands elsewhere that, through Kramers-Kronig, create detectable structure in ε' even in the transparent region."

- question: "The real and imaginary parts of the complex permittivity ε(ω) are independent functions that must each be measured separately to fully characterize a material's electromagnetic response."
  type: true-false
  answer: false
  explanation: "The Kramers-Kronig relations, derived from causality, relate ε'(ω) and ε''(ω) by a Hilbert transform pair. Knowing ε'' across all frequencies determines ε', and vice versa. This is why measuring absorption over a broad spectral range is sufficient to reconstruct the full complex permittivity. The interdependence is not an approximation — it is an exact consequence of the requirement that effects follow causes."

- question: "Why does causality — the requirement that a material's polarization response cannot precede the driving electromagnetic field — constrain the relationship between ε'(ω) and ε''(ω)?"
  type: short-answer
  answer: "Causality in the time domain means P(t) can only depend on E at earlier times, not future times. When you Fourier transform this causal constraint, it forces ε(ω) to be analytic in the upper half of the complex frequency plane. By the Cauchy integral theorem, analyticity in the upper half-plane is equivalent to the real and imaginary parts being a Hilbert transform pair — the Kramers-Kronig relations. So KK relations are not empirical regularities but mathematical consequences of time-ordering."
  explanation: "The physical intuition is that a response that anticipated its cause would violate time-ordering. This physical requirement, expressed in frequency space, forces a deep algebraic relationship between the dispersive (ε') and absorptive (ε'') responses that cannot be violated by any physical material — making Kramers-Kronig universally applicable."
```

## Explainer

From the Drude model you know that electrons in a conductor respond to an applied electric field with a frequency-dependent conductivity: σ(ω) = σ₀/(1 − iωτ), where τ is the relaxation time and σ₀ is the DC conductivity. At low frequencies the current is nearly in phase with the field; at high frequencies (ωτ ≫ 1) the inertia of electrons causes them to lag, and the response becomes imaginary. This frequency dependence is not a complication — it is the entire physics of how materials interact with electromagnetic waves, and the **complex permittivity** is the unified language for describing it.

The connection between conductivity and permittivity comes directly from Maxwell's equations. When you write ∇ × H = J + ∂D/∂t and allow both a free-current response J = σE and a bound-charge polarization response D = εE, the two contributions combine into an effective complex permittivity: ε_eff(ω) = ε_bound(ω) + iσ(ω)/ω. The **real part ε'** describes the in-phase, reactive response — how much energy is stored per cycle in the polarization of the medium. The **imaginary part ε''** describes the out-of-phase, dissipative response — how much energy is absorbed per cycle. A large ε'' means the medium strongly attenuates electromagnetic waves, which is why metals (with large σ) are opaque.

The **Kramers-Kronig relations** are the deep constraint on ε(ω) that comes from causality: the real and imaginary parts are not independent. Because the polarization response of a medium cannot precede the driving field (no effect before cause), the real and imaginary parts of ε(ω) are related by a Hilbert transform pair: ε'(ω) − 1 = (2/π) P∫₀^∞ ω'ε''(ω')/(ω'² − ω²) dω', and vice versa. The practical consequence is that if you measure absorption (ε'') across all frequencies, you can reconstruct the refractive index (ε') — and this is exactly how optical constants of materials are determined experimentally from reflectance spectra.

The **absorption coefficient** α relates to ε'' through the imaginary part of the wave vector k. When you substitute ε(ω) = ε' + iε'' into the plane-wave dispersion relation k² = ω²ε(ω)/c², you get a complex k, meaning the wave decays exponentially with penetration depth δ = 1/Im(k). This **skin depth** — which you will recognize from conductor behavior — is the electromagnetic expression of the imaginary part of the permittivity. Highly conductive or strongly absorbing materials have large ε'', small skin depths, and reflect most incident radiation. Transparent insulators have ε'' ≈ 0 in their transparency window, and the Kramers-Kronig relations guarantee there are corresponding features in ε' at those same frequencies.

