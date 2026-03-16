---
id: refraction-interface-snell-relation
title: Refraction at Boundaries and Snell's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relation
  type: hard
builds-toward:
- grazing-angle-critical-condition
- wavelength-color-refractive-index
tags:
- refraction
- optics
stage: formal-systems
status: draft
---

# Refraction at Boundaries and Snell's Law

## Core Idea
When a wave enters a new medium with different speed, its direction bends according to Snell's law: n₁ sin(θ₁) = n₂ sin(θ₂). The refractive index n = c/v is the ratio of light speed in vacuum to speed in the medium. Refraction arises because the wavelength changes while frequency remains constant, causing a direction change to maintain phase continuity at the interface.

## How It's Best Learned
Derive Snell's law using the Huygens-Fresnel principle: wavelets from the interface must add constructively to the refracted ray.

## Common Misconceptions
Light does not 'change speed' in the usual sense—rather, light speed in a medium is the definition of the medium's refractive index.

## Explainer

You already know that waves have a speed, frequency, and wavelength linked by v = fλ. When a wave crosses from one medium into another — say, from air into glass — something has to give. The frequency cannot change: it is set by the source, and the wave cannot pile up or thin out at the interface (that would require creating or destroying cycles of oscillation). So when the wave slows down in the denser medium, it is the **wavelength** that shortens to compensate. Shorter wavelength, same frequency, lower speed — v = fλ still holds.

This wavelength change is what causes **refraction**, the bending of the wave's direction. Picture a column of soldiers marching in a line at an angle toward muddy ground. The soldiers who hit the mud first slow down, while those still on firm ground continue at full speed. The rank swings around — the direction of travel rotates. Waves behave identically: the part of the wavefront that enters the slower medium first falls behind, pivoting the wavefront toward the normal. **Snell's law** formalizes this: n₁ sin θ₁ = n₂ sin θ₂, where n = c/v is the **refractive index** (a dimensionless measure of how much slower light travels in that medium relative to vacuum).

The law tells you the direction of bending unambiguously. When light enters a denser medium (n₂ > n₁), the right side of the equation must produce a smaller sin θ₂ — so θ₂ < θ₁, meaning the ray bends toward the normal. When light exits the dense medium back into air, it bends away from the normal. This asymmetry is why a straw in a glass of water appears bent: light from the underwater portion of the straw bends away from the normal as it exits the water into air, causing the apparent position of the straw to shift upward.

The refractive index also depends slightly on wavelength — a phenomenon called **dispersion**. Glass has a slightly higher n for violet light than for red light, so violet bends more steeply. A prism exploits this to spread white light into a rainbow; raindrops do the same thing to produce natural rainbows. You will encounter this dispersion again when studying wavelength and color. For now, Snell's law in its basic form treats n as a constant, which is an excellent approximation for monochromatic (single-wavelength) light and the foundation for all of geometrical optics that follows.
