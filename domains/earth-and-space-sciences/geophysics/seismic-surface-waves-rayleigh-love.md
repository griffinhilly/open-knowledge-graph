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
stage: expert
status: validated
---

# Seismic Surface Waves: Rayleigh and Love Waves

## Core Idea
Surface waves are confined to the upper layers of the Earth and decay exponentially with depth. Rayleigh waves involve coupled P and S motion in a retrograde elliptical pattern; Love waves are horizontally polarized shear waves. Both travel slower than body waves but dominate earthquake damage and global seismograms because they carry large amplitude and propagate with minimal attenuation.

## Questions

```yaml
- question: "A seismograph records waves with purely horizontal, side-to-side particle motion perpendicular to the wave propagation direction. What type of seismic wave is this?"
  type: multiple-choice
  options:
    - "Rayleigh waves — retrograde elliptical motion in the vertical plane"
    - "P-waves — compressional motion along the propagation direction"
    - "Love waves — horizontally polarized SH motion perpendicular to propagation"
    - "S-waves — shear motion that can be either horizontal or vertical"
  answer: 2
  explanation: "The purely horizontal, transverse (perpendicular to propagation direction) motion with no vertical component is the diagnostic signature of Love waves. Rayleigh waves produce retrograde elliptical motion in the vertical plane (both vertical and horizontal components in the direction of travel). S-waves can be either SH or SV, but as body waves they radiate through the interior, not as guided surface waves. The distinction between Love and Rayleigh is fundamentally about polarization: Love = horizontal SH, Rayleigh = retrograde ellipse in the vertical plane."

- question: "Rayleigh waves are observed traveling at different speeds for different periods: longer-period waves arrive earlier than shorter-period waves. What does this indicate about the medium?"
  type: multiple-choice
  options:
    - "The medium is homogeneous — all periods travel at the same speed in a uniform half-space"
    - "The medium is layered with seismic velocity increasing with depth, causing longer-period waves (which sample deeper) to travel faster"
    - "The source was more energetic at long periods, causing those waves to outrun shorter-period waves"
    - "Love waves are contaminating the Rayleigh wave record and arriving at a different speed"
  answer: 1
  explanation: "This is the definition of dispersion and its physical interpretation. Longer-period surface waves penetrate deeper into the Earth, sampling material at greater depth. In the real Earth, seismic velocity generally increases with depth, so longer-period waves travel through faster material on average and arrive sooner. This dispersion is not a complication — it is the key property that makes surface waves useful for imaging Earth structure. By measuring how velocity varies with period, seismologists can invert for how shear velocity varies with depth."

- question: "Rayleigh waves require a low-velocity layer overlying a higher-velocity substrate in order to exist."
  type: true-false
  answer: false
  explanation: "This describes the requirement for Love waves, not Rayleigh waves. Rayleigh waves exist wherever there is a free surface — they require no layering at all and occur even in a perfectly homogeneous half-space. Love waves, by contrast, require a low-velocity layer over a higher-velocity substrate because they are sustained by total internal reflection within the low-velocity layer. Getting these requirements reversed is a common misconception; remembering that Rayleigh waves involve the free surface directly (retrograde ellipse at the surface) while Love waves are trapped in a layer helps keep the distinction straight."

- question: "Surface waves travel more slowly than body waves but carry more energy at large distances from the earthquake source."
  type: true-false
  answer: true
  explanation: "Surface waves are slower than both P and S body waves — Rayleigh wave velocity in a uniform half-space is about 0.92 times the shear wave velocity. Despite arriving later, they dominate seismograms of distant earthquakes because their energy is confined to the shallow subsurface rather than spreading through the full volume. Body waves spread in three dimensions (amplitude decays as 1/r), while surface waves spread in two dimensions along the surface (amplitude decays as 1/√r). This geometric spreading difference means surface waves retain much higher amplitude at large distances, which is also why they cause the majority of earthquake damage far from the epicenter."

- question: "Why are surface wave dispersion curves useful for imaging Earth's interior, and what physical property do they constrain?"
  type: short-answer
  answer: "Surface wave dispersion is useful because different periods sample different depths: short-period waves are sensitive to shallow structure, long-period waves penetrate deeper. By measuring how phase velocity and group velocity vary with period, seismologists construct dispersion curves that are then inverted mathematically to recover shear-wave velocity as a function of depth. Short periods (5–20 s) constrain crustal thickness and velocity; intermediate periods (20–100 s) resolve the lithosphere and asthenosphere; long periods (100–300 s) sense the upper mantle. The physical property constrained is primarily shear velocity (Vs) structure, because both Rayleigh and Love waves are shear-dominated."
  explanation: "Surface wave tomography has produced some of the highest-resolution images of the upper mantle, revealing cratonic roots, subducting slabs, and plumes. The power of the method comes from the depth sensitivity being tunable simply by measuring different periods — you do not need different types of seismic sources or receivers, just a broad-band seismograph and a distant earthquake."
```

## Explainer

From elastic wave propagation and seismic body waves, you know that P-waves compress and expand material along the direction of travel, while S-waves shear it perpendicular to the direction of travel. Both are body waves — they radiate outward through the interior of the Earth in all directions. **Surface waves** are fundamentally different: they are guided by the free surface of the Earth (or by internal boundaries), and their energy is concentrated in the shallow subsurface rather than spreading through the full volume. This confinement is why surface waves carry more energy at a given distance from the source and why they dominate seismograms of distant earthquakes.

**Rayleigh waves** exist wherever there is a free surface — they require no layering. The particle motion is a retrograde ellipse in the vertical plane containing the propagation direction: at the surface, particles move backward (opposite to the wave's travel direction) at the top of their elliptical path, much like a point on the surface of an ocean wave but in reverse. This coupled vertical and horizontal motion involves both P and SV (vertically polarized shear) wave components interacting at the free surface. Rayleigh wave velocity in a uniform half-space is about 0.92 times the shear wave velocity, making them slower than both P and S body waves. In the real Earth, where velocity increases with depth, Rayleigh waves exhibit **dispersion**: longer-period waves penetrate deeper, sampling faster material, and therefore travel faster than shorter-period waves. This dispersion is not a nuisance — it is an extraordinarily useful property, because measuring how Rayleigh wave velocity varies with period reveals how shear velocity varies with depth.

**Love waves** require a low-velocity layer overlying a higher-velocity substrate — a condition easily met by Earth's crust over the mantle. They are horizontally polarized shear waves (SH motion) that become trapped in the low-velocity layer through total internal reflection. The particle motion is horizontal and perpendicular to the propagation direction — purely side-to-side, with no vertical component. Like Rayleigh waves, Love waves are dispersive in a layered Earth: longer periods sample deeper, faster material. Love waves are typically faster than Rayleigh waves and often arrive first in the surface-wave train on a seismogram.

The dispersion of surface waves makes them one of the most powerful tools in global seismology for imaging Earth's interior. By measuring the **group velocity** (the speed of the wave packet's envelope) and **phase velocity** (the speed of individual wave crests) as functions of period, seismologists construct dispersion curves that are then inverted for shear-velocity structure as a function of depth. Short-period surface waves (5–20 seconds) constrain crustal structure; intermediate periods (20–100 seconds) resolve the lithosphere and asthenosphere; long periods (100–300 seconds) sense the upper mantle transition zone. Surface-wave tomography using earthquake data from global seismic networks has produced detailed three-dimensional maps of shear velocity in the upper mantle, revealing features like cratonic roots, subducting slabs, and mantle plumes. For engineers, surface waves matter for a different reason: their large amplitudes and low frequencies couple efficiently with buildings and infrastructure, making them the primary cause of earthquake damage at moderate to large distances from the epicenter.
