---
id: seismic-surface-waves-rayleigh-love
title: 'Seismic Surface Waves: Rayleigh and Love Waves'
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
builds-toward:
- seismic-anisotropy-shear-wave-splitting
tags:
- seismology
- surface-waves
- dispersion
- wave-propagation
stage: advanced
status: draft
---

# Seismic Surface Waves: Rayleigh and Love Waves

## Core Idea
Surface waves are confined to the upper layers of the Earth and decay exponentially with depth. Rayleigh waves involve coupled P and S motion in a retrograde elliptical pattern; Love waves are horizontally polarized shear waves. Both travel slower than body waves but dominate earthquake damage and global seismograms because they carry large amplitude and propagate with minimal attenuation.

## Explainer

From elastic wave propagation and seismic body waves, you know that P-waves compress and expand material along the direction of travel, while S-waves shear it perpendicular to the direction of travel. Both are body waves — they radiate outward through the interior of the Earth in all directions. **Surface waves** are fundamentally different: they are guided by the free surface of the Earth (or by internal boundaries), and their energy is concentrated in the shallow subsurface rather than spreading through the full volume. This confinement is why surface waves carry more energy at a given distance from the source and why they dominate seismograms of distant earthquakes.

**Rayleigh waves** exist wherever there is a free surface — they require no layering. The particle motion is a retrograde ellipse in the vertical plane containing the propagation direction: at the surface, particles move backward (opposite to the wave's travel direction) at the top of their elliptical path, much like a point on the surface of an ocean wave but in reverse. This coupled vertical and horizontal motion involves both P and SV (vertically polarized shear) wave components interacting at the free surface. Rayleigh wave velocity in a uniform half-space is about 0.92 times the shear wave velocity, making them slower than both P and S body waves. In the real Earth, where velocity increases with depth, Rayleigh waves exhibit **dispersion**: longer-period waves penetrate deeper, sampling faster material, and therefore travel faster than shorter-period waves. This dispersion is not a nuisance — it is an extraordinarily useful property, because measuring how Rayleigh wave velocity varies with period reveals how shear velocity varies with depth.

**Love waves** require a low-velocity layer overlying a higher-velocity substrate — a condition easily met by Earth's crust over the mantle. They are horizontally polarized shear waves (SH motion) that become trapped in the low-velocity layer through total internal reflection. The particle motion is horizontal and perpendicular to the propagation direction — purely side-to-side, with no vertical component. Like Rayleigh waves, Love waves are dispersive in a layered Earth: longer periods sample deeper, faster material. Love waves are typically faster than Rayleigh waves and often arrive first in the surface-wave train on a seismogram.

The dispersion of surface waves makes them one of the most powerful tools in global seismology for imaging Earth's interior. By measuring the **group velocity** (the speed of the wave packet's envelope) and **phase velocity** (the speed of individual wave crests) as functions of period, seismologists construct dispersion curves that are then inverted for shear-velocity structure as a function of depth. Short-period surface waves (5–20 seconds) constrain crustal structure; intermediate periods (20–100 seconds) resolve the lithosphere and asthenosphere; long periods (100–300 seconds) sense the upper mantle transition zone. Surface-wave tomography using earthquake data from global seismic networks has produced detailed three-dimensional maps of shear velocity in the upper mantle, revealing features like cratonic roots, subducting slabs, and mantle plumes. For engineers, surface waves matter for a different reason: their large amplitudes and low frequencies couple efficiently with buildings and infrastructure, making them the primary cause of earthquake damage at moderate to large distances from the epicenter.
