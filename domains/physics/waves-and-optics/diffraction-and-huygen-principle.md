---
id: diffraction-and-huygen-principle
title: Diffraction and Huygens' Principle
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-and-classification
  type: hard
- id: superposition-principle-waves
  type: soft
builds-toward:
- single-slit-diffraction
- diffraction-gratings
tags:
- diffraction
- huygen-principle
- wave-bending
stage: formal-systems
status: draft
---

# Diffraction and Huygens' Principle

## Core Idea
Huygens' principle states that each point on a wavefront acts as a source of secondary wavelets that propagate in the forward direction. Diffraction occurs when waves bend around obstacles or through openings, which Huygens' principle explains through the interference of secondary wavelets. Diffraction becomes significant when obstacle size is comparable to wavelength.

## Explainer

From your study of wave properties, you know that waves carry energy and oscillate periodically in space. What Huygens' principle adds is a geometric recipe for predicting where a wavefront will be at any future moment. The key idea: you don't need to track the original source — you can treat every point on an existing wavefront as if it were a new, independent point source of spherical (or circular in 2D) wavelets. The new wavefront at the next instant is simply the surface tangent to all those secondary wavelets. This reconstruction works perfectly for straight-line propagation in open space, but it reveals something deeper when a wave encounters an obstacle or opening.

When a plane wave passes through a wide opening, the secondary wavelets near the center reinforce each other in the forward direction and the wavefront continues on its path — no bending apparent. But at the edges of the opening, there are no wavelets from the blocked region to cancel the sideways-propagating components of the edge wavelets. Those edge wavelets spill into the geometric shadow, **bending the wave** around the corner. This bending is diffraction, and its extent depends critically on the ratio of wavelength to opening size. If the opening is much wider than the wavelength, only a thin fringe diffracts at the edges — the wave mostly goes straight. But when the opening is comparable in size to the wavelength, the edge wavelets dominate the whole aperture and the wave fans out broadly in all directions.

The rule of thumb is: **diffraction is significant when λ/d ≈ 1**, where λ is the wavelength and d is the obstacle or opening size. Sound diffracts around a doorframe (wavelength ~0.3 m, doorwidth ~1 m) noticeably — you hear sound in the next room even when the source is not in your line of sight. Visible light (wavelength ~500 nm) does not diffract around everyday objects because doors and furniture are millions of wavelengths across. But pass light through a narrow slit or a diffraction grating with spacing comparable to λ, and diffraction becomes dramatic. This wavelength-size relationship explains why AM radio (wavelength ~300 m) diffracts over hills while visible light travels in straight lines.

The connection to superposition becomes important when multiple openings or multiple sources are present. Each opening generates its own set of Huygens wavelets, and those sets can interfere constructively or destructively at different angles — this is exactly what the superposition principle predicts. Bright fringes appear where path differences produce in-phase reinforcement; dark fringes appear where they produce cancellation. The full mathematical treatment of single-slit diffraction and diffraction gratings you'll encounter next builds directly on this foundation: Huygens gives you the source locations, superposition gives you the interference pattern, and the ratio λ/d governs the scale of the whole phenomenon.


