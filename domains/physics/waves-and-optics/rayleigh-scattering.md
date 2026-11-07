---
id: rayleigh-scattering
title: Rayleigh Scattering and the Color of the Sky
domain: physics
course: waves-and-optics
prerequisites:
- id: electromagnetic-waves
  type: hard
- id: electric-dipole-moment
  type: hard
- id: driven-harmonic-oscillator
  type: soft
- id: electric-dipole-radiation
  type: soft
- id: polarization-of-light
  type: soft
builds-toward: []
tags:
- scattering
- dipole-radiation
- atmospheric-optics
- polarization
stage: advanced
status: validated
---

# Rayleigh Scattering and the Color of the Sky

## Core Idea
When light meets particles much smaller than its wavelength, such as air molecules, it drives their electrons to oscillate, and each molecule re-radiates as a small oscillating dipole. The power a dipole radiates grows as the fourth power of frequency, so the scattered intensity varies as 1/λ⁴. Blue light is therefore scattered several times more strongly than red, which makes the daytime sky blue and the setting Sun red. Light scattered at right angles to the incoming sunlight is strongly polarized.

## How It's Best Learned
Shine a white beam through water with a few drops of milk and look from the side and along the beam: the side view looks bluish and the transmitted beam looks orange. Then build the model step by step: an electron bound by a spring-like force, driven well below its resonant frequency, gives a dipole moment proportional to the field. Apply the dipole radiation result P ∝ p₀²ω⁴ to get the 1/λ⁴ law. Use a polarizing filter on the real sky to check the polarization prediction.

## Common Misconceptions
- The sky is blue because it reflects the color of the ocean. (The sky is blue over deserts and land too; the color comes from scattering by air molecules.)
- If scattering goes as 1/λ⁴, the sky should look violet. (Sunlight contains less violet than blue, and human eyes are much less sensitive to violet, so the scattered mix looks sky-blue.)
- Clouds are white because water droplets scatter like air molecules. (Droplets are much larger than the wavelength; their scattering depends only weakly on wavelength, so all colors scatter about equally and clouds look white.)

## Questions

```yaml
- question: "By about what factor is 450 nm blue light scattered more strongly than 700 nm red light by air molecules?"
  type: multiple-choice
  options: ["About 1.6", "About 2.4", "About 5.9", "About 24"]
  answer: 2
  explanation: "Intensity scales as 1/λ⁴. (700/450)⁴ = (1.556)⁴ ≈ 5.9."
- question: "Skylight seen at 90° from the direction of the Sun is strongly linearly polarized."
  type: true-false
  answer: true
  explanation: "The induced dipoles oscillate perpendicular to the incoming sunlight. Viewed at 90°, only the component of oscillation perpendicular to your line of sight radiates toward you, so the scattered light is largely polarized."
- question: "Why does the Sun look red or orange near sunset?"
  type: multiple-choice
  options: ["The Sun's surface cools in the evening", "Sunlight crosses much more air, and blue light is scattered out of the direct beam along the way", "Red light is created by the atmosphere at low angles", "The atmosphere reflects red light from the ground"]
  answer: 1
  explanation: "Near the horizon the path through the atmosphere is many times longer. Short wavelengths are scattered out of the beam, so the light that reaches you directly is depleted in blue."
- question: "Starting from the fact that a dipole of amplitude p₀ oscillating at angular frequency ω radiates power P ∝ p₀²ω⁴, explain why the scattered intensity varies as 1/λ⁴ for molecules."
  type: short-answer
  answer: "For light far below the molecule's resonant frequencies, the induced dipole p₀ is proportional to the field and nearly independent of frequency, so P ∝ ω⁴ ∝ 1/λ⁴."
  explanation: "Electrons in air molecules have resonances in the ultraviolet. Visible light drives them well below resonance, where the response is nearly constant. The ω⁴ factor from radiation then sets the wavelength dependence."
```

## Explainer
Lord Rayleigh worked out the theory of this scattering in 1871 and later papers. The starting point is a molecule in the oscillating electric field of a light wave. The field pushes the molecule's electrons back and forth, creating an oscillating electric dipole p(t) = p₀ cos ωt. An oscillating dipole radiates in all directions except along its own axis, with time-averaged total power

P = p₀²ω⁴ / (12πε₀c³).

Some of the energy in the incoming beam is therefore redirected sideways. That is scattering.

How big is p₀? Model a bound electron as a mass on a spring with natural frequency ω₀, driven at frequency ω. For air molecules, ω₀ lies in the ultraviolet, so visible light drives the electrons well below resonance. In that limit the electron's displacement is nearly the same at every visible frequency, and p₀ is proportional to the field amplitude alone. The whole frequency dependence then comes from the ω⁴ in the radiated power. Written in terms of wavelength, the scattered intensity varies as 1/λ⁴.

The numbers are striking. Blue light at 450 nm is scattered about 5.9 times more than red light at 700 nm. Look at any part of the sky away from the Sun and you see sunlight that has been scattered toward you, rich in short wavelengths, so the sky looks blue. Look at the Sun when it sits low on the horizon and you see the light that was not scattered. Its path through the air is long, much of the blue has been removed, and the Sun looks orange or red.

Scattering also polarizes light. The incoming sunlight is unpolarized, but its electric field always lies perpendicular to its direction of travel, so the induced dipoles oscillate in that plane. An observer looking at 90° to the sunlight receives radiation only from the component of oscillation perpendicular to the line of sight. That light is strongly linearly polarized, which is why polarizing sunglasses darken parts of the sky, and why some insects can navigate by the sky's polarization pattern.

The 1/λ⁴ law holds only for scatterers much smaller than the wavelength. Particles comparable to or larger than the wavelength, such as cloud droplets, scatter in a different way, described by Mie theory. Their scattering depends only weakly on wavelength, so clouds and haze look white or grey.
