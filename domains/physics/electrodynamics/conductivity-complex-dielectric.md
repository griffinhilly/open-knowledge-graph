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
stage: advanced
status: draft
---

# Complex Conductivity and Dielectric Function

## Core Idea
The complex permittivity ε(ω) = ε'(ω) + iε''(ω) encodes both oscillatory response and dissipation. The imaginary part ε''(ω) directly relates to conductivity and absorption coefficient through Kramers-Kronig relations.

## Explainer

From the Drude model you know that electrons in a conductor respond to an applied electric field with a frequency-dependent conductivity: σ(ω) = σ₀/(1 − iωτ), where τ is the relaxation time and σ₀ is the DC conductivity. At low frequencies the current is nearly in phase with the field; at high frequencies (ωτ ≫ 1) the inertia of electrons causes them to lag, and the response becomes imaginary. This frequency dependence is not a complication — it is the entire physics of how materials interact with electromagnetic waves, and the **complex permittivity** is the unified language for describing it.

The connection between conductivity and permittivity comes directly from Maxwell's equations. When you write ∇ × H = J + ∂D/∂t and allow both a free-current response J = σE and a bound-charge polarization response D = εE, the two contributions combine into an effective complex permittivity: ε_eff(ω) = ε_bound(ω) + iσ(ω)/ω. The **real part ε'** describes the in-phase, reactive response — how much energy is stored per cycle in the polarization of the medium. The **imaginary part ε''** describes the out-of-phase, dissipative response — how much energy is absorbed per cycle. A large ε'' means the medium strongly attenuates electromagnetic waves, which is why metals (with large σ) are opaque.

The **Kramers-Kronig relations** are the deep constraint on ε(ω) that comes from causality: the real and imaginary parts are not independent. Because the polarization response of a medium cannot precede the driving field (no effect before cause), the real and imaginary parts of ε(ω) are related by a Hilbert transform pair: ε'(ω) − 1 = (2/π) P∫₀^∞ ω'ε''(ω')/(ω'² − ω²) dω', and vice versa. The practical consequence is that if you measure absorption (ε'') across all frequencies, you can reconstruct the refractive index (ε') — and this is exactly how optical constants of materials are determined experimentally from reflectance spectra.

The **absorption coefficient** α relates to ε'' through the imaginary part of the wave vector k. When you substitute ε(ω) = ε' + iε'' into the plane-wave dispersion relation k² = ω²ε(ω)/c², you get a complex k, meaning the wave decays exponentially with penetration depth δ = 1/Im(k). This **skin depth** — which you will recognize from conductor behavior — is the electromagnetic expression of the imaginary part of the permittivity. Highly conductive or strongly absorbing materials have large ε'', small skin depths, and reflect most incident radiation. Transparent insulators have ε'' ≈ 0 in their transparency window, and the Kramers-Kronig relations guarantee there are corresponding features in ε' at those same frequencies.

