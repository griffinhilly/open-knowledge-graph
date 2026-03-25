---
id: fresnel-reflection-transmission
title: 'Fresnel Equations: Reflection and Transmission at Interfaces'
domain: physics
course: waves-and-optics
prerequisites:
- id: snells-law
  type: hard
- id: electromagnetic-waves
  type: soft
- id: impedance-matching-and-reflection
  type: soft
builds-toward:
- total-internal-reflection
- thin-film-interference
tags:
- fresnel-equations
- reflection
- transmission
stage: advanced
status: validated
---
# Fresnel Equations: Reflection and Transmission at Interfaces

## Core Idea
Fresnel equations describe the amplitude reflection and transmission coefficients for electromagnetic waves at a dielectric interface, accounting for polarization. They explain why reflection depends on angle of incidence, polarization direction, and the refractive index ratio between media.

## Questions

```yaml
- question: "Unpolarized light strikes a glass surface at Brewster's angle. A polarizing filter oriented to transmit s-polarized light is placed in the reflected beam. What does the filter transmit?"
  type: multiple-choice
  options:
    - "Nothing — at Brewster's angle all light is transmitted into the glass, so no reflected beam exists"
    - "Half the original intensity — Brewster's angle only reduces one polarization component"
    - "Essentially all of the reflected beam — at Brewster's angle the reflected light is entirely s-polarized"
    - "p-polarized light — Brewster's angle eliminates s-polarization from the reflection"
  answer: 2
  explanation: "At Brewster's angle, p-polarized light has zero reflectance — none of it reflects. The reflected beam therefore consists entirely of s-polarized light. A filter oriented to pass s-polarization transmits essentially all of the reflected beam. This is why polarizing sunglasses work: reflected glare from flat surfaces (roads, water) near Brewster's angle is strongly s-polarized, and the glasses' vertically-oriented polarizer (oriented to block s-polarized horizontal glare) eliminates it. The common misconception in option D reverses which polarization is eliminated."

- question: "Light travels from glass (n₁ = 1.5) toward air (n₂ = 1.0) at an angle greater than the critical angle. What do the Fresnel equations predict about the transmitted beam?"
  type: multiple-choice
  options:
    - "The transmitted beam has reduced intensity but still propagates into the air"
    - "The Fresnel transmission coefficient goes to zero — total internal reflection occurs and no energy is transmitted"
    - "The transmitted beam has the same intensity but a different polarization state"
    - "Snell's law determines whether reflection occurs; the Fresnel equations only describe partial reflection below the critical angle"
  answer: 1
  explanation: "Total internal reflection is the condition where the Fresnel transmission amplitude goes to zero: beyond the critical angle, no energy propagates into the second medium. The Fresnel equations provide the complete quantitative picture — they predict partial reflection below the critical angle and complete reflection above it. This is the physical basis of fiber optics: the glass-air interface is designed so that light hits it beyond the critical angle, and the Fresnel amplitude for transmission vanishes, confining light within the fiber. Option D is wrong: the Fresnel equations are fully general and contain Snell's law as a special case."

- question: "For s-polarized light, the reflectance increases smoothly from its normal-incidence value toward 100% as the angle of incidence approaches 90°."
  type: true-false
  answer: true
  explanation: "The s-polarization Fresnel reflectance is a monotonically increasing function of angle of incidence, starting at the normal-incidence reflectance (about 4% for air-glass) and reaching 100% at grazing incidence (90°). This contrasts sharply with p-polarization, which dips to zero at Brewster's angle before rising to 100% at 90°. The smooth monotonic behavior of s-polarization is why, at angles near but below Brewster's angle, reflected light is predominantly s-polarized — s-polarization reflects more while p-polarization reflects less (or nothing, exactly at Brewster's angle)."

- question: "Snell's law predicts what fraction of light is reflected when it hits a dielectric interface at normal incidence."
  type: true-false
  answer: false
  explanation: "Snell's law tells you only the direction of the transmitted (refracted) ray — it predicts the angle of refraction from the angle of incidence and the refractive indices. It says nothing about the amplitude or intensity of the reflected and transmitted beams. That is precisely the problem the Fresnel equations solve. At normal incidence on a glass-air interface (n = 1.5), Snell's law correctly predicts no bending (since incidence is 0°), but it takes the Fresnel equations to show that approximately 4% of the intensity reflects and 96% transmits."

- question: "Why does p-polarized light have zero reflectance at Brewster's angle, while s-polarized light always has nonzero reflectance at the same interface?"
  type: short-answer
  answer: "At Brewster's angle, the reflected and refracted rays are exactly 90° apart. The physical reason for zero p-polarized reflectance lies in how oscillating dipoles radiate: the electric field of p-polarized light drives charge oscillations in the plane of incidence, and dipoles do not radiate along their oscillation axis. At Brewster's angle, the direction of the putative reflected ray coincides with the dipole oscillation direction, so no light can be emitted in that direction — reflectance goes to zero. S-polarized light oscillates perpendicular to the plane of incidence, so its dipoles always radiate in the reflected direction regardless of angle, giving nonzero reflectance at all angles below 90°."
  explanation: "The key insight is that Brewster's angle is not an arbitrary coincidence — it arises from the geometry of electromagnetic wave emission by induced dipoles. The condition θ_B = arctan(n₂/n₁) is exactly the condition for the reflected and refracted rays to be perpendicular, which is exactly the condition for dipole radiation to vanish in the reflected direction for p-polarization. S-polarization lacks this geometric alignment and therefore always reflects partially."
```

## Explainer

Snell's law told you *where* light goes at an interface — how the angle changes based on the refractive index ratio. But Snell's law says nothing about *how much* light reflects versus transmits. That is what the Fresnel equations answer. When light hits a glass surface at normal incidence (straight on), roughly 4% reflects and 96% transmits. This partial reflection happens at every dielectric interface, and the Fresnel equations tell you exactly what fraction reflects and transmits as a function of the angle of incidence, the refractive indices, and — crucially — the **polarization** of the light.

Polarization refers to the direction in which the electric field of the light wave oscillates. The Fresnel equations treat two orthogonal polarization cases separately. **s-polarization** (also called TE, for transverse electric) has its electric field oscillating perpendicular to the plane of incidence. **p-polarization** (also called TM, for transverse magnetic) has its electric field oscillating parallel to the plane of incidence. These two cases behave very differently as the angle of incidence changes. For s-polarized light, reflectance increases smoothly from its normal-incidence value toward 100% as the angle approaches 90°. For p-polarized light, something remarkable happens: reflectance first drops to zero at a special angle, then rises back to 100%.

This special angle where p-polarized reflectance goes to zero is **Brewster's angle** (θ_B = arctan(n₂/n₁)). At this angle, the reflected and refracted rays are exactly 90° apart, and the geometry of how oscillating dipoles radiate means p-polarized light cannot reflect. This is why polarizing sunglasses reduce glare: sunlight reflected off a flat road or water surface is preferentially s-polarized near Brewster's angle, and the glasses' vertical polarizer blocks it. The phenomenon has a clean geometric explanation, but the Fresnel equations predict it with mathematical precision.

The Fresnel equations also explain why anti-reflection coatings on glasses and camera lenses work: thin films create destructive interference between reflections from two surfaces, canceling the ~4% reflective loss at each glass boundary. The same physics underlies fiber optics — cables are designed so that light hits the glass-air boundary beyond the critical angle (total internal reflection), and the Fresnel amplitude coefficients go to zero for transmitted light. Starting from Snell's law and the wave behavior of electromagnetic fields, the Fresnel equations are the complete quantitative description of what happens at every optical interface.
