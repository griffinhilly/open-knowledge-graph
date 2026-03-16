---
id: electromagnetic-waves-in-media
title: Electromagnetic Waves in Dielectric Media
domain: physics
course: electrodynamics
prerequisites:
- id: plane-waves-in-vacuum
  type: hard
- id: boundary-conditions-em-fields
  type: soft
builds-toward:
- dispersion-relations
tags:
- waves
- dielectrics
- propagation
stage: abstract-reasoning
status: draft
---

# Electromagnetic Waves in Dielectric Media

## Core Idea
In dielectrics, D = ε₀εE and B = μ₀μH modify Maxwell's equations. Plane waves satisfy ω²/v_p² = k² where v_p = c/n is the phase velocity. The dispersion relation ω(k) depends on material properties, meaning different frequencies travel at different speeds (dispersion).

## Explainer

In vacuum, you derived plane-wave solutions to Maxwell's equations and found that electromagnetic waves travel at c = 1/√(ε₀μ₀). When the same derivation is done inside a linear dielectric material, the only change is that ε₀ is replaced by ε = ε_r ε₀ and μ₀ by μ = μ_r μ₀, where ε_r and μ_r are the material's relative permittivity and permeability. The wave speed becomes v_p = 1/√(εμ) = c/√(ε_r μ_r). The **index of refraction** is defined as n = c/v_p = √(ε_r μ_r), and for most optical materials μ_r ≈ 1, so n ≈ √ε_r. Glass has n ≈ 1.5, meaning light travels at about 2/3 its vacuum speed inside glass.

The key physics beyond simple slowing is **dispersion**: the index of refraction depends on frequency. Microscopically, this happens because the bound charges in a material are driven oscillators — they respond differently to different driving frequencies. Near a resonance, the material's polarization response changes rapidly with frequency, and so does ε_r(ω). Far from resonances, in the visible range for glass, n increases gently with frequency (shorter wavelengths bend more), which is why a prism separates white light into a rainbow: blue light (higher ω) has a slightly higher n than red light and refracts more at each interface. The general relationship ω(k) in a medium is the **dispersion relation**; in vacuum ω = ck is linear (all frequencies travel at the same speed c), but in a medium this linearity is broken.

At an interface between two media, the boundary conditions you studied constrain how a wave transitions from one material to another. The tangential E and normal D must match, which leads directly to Snell's law: n₁ sin(θ₁) = n₂ sin(θ₂). The same boundary conditions also determine how much of the wave is reflected versus transmitted (the **Fresnel equations**). Both Snell's law and the Fresnel coefficients follow from demanding that boundary conditions are satisfied simultaneously by the incident, reflected, and transmitted plane waves — there is no additional physical input beyond what you already know.

At high frequencies or in conducting media, the picture changes qualitatively. In a conductor, free charges can move and dissipate the wave energy. The permittivity becomes complex: ε = ε' + iε'', and the imaginary part causes the wave amplitude to decay exponentially with depth, defining the **skin depth** δ = √(2/ωμσ). This is why microwave radiation does not penetrate metal walls and why RF signals are shielded by conductive enclosures — the electromagnetic wave is attenuated within one or two skin depths of the conductor surface. The transition from transparent dielectric to absorbing conductor is all captured in the same dispersion relation framework, just with a complex index of refraction.
