---
id: seismic-waves
title: Seismic Waves
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: earthquakes-and-seismology
  type: hard
- id: wave-properties-intro
  type: soft
- id: transverse-and-longitudinal-waves
  type: soft
- id: wave-speed-medium
  type: soft
- id: wave-motion-definition
  type: soft
- id: wave-equation-one-dimensional
  type: soft
- id: wave-equation-pde
  type: soft
builds-toward:
- earth-interior-structure
tags:
- seismic-waves
- P-waves
- S-waves
- surface-waves
- travel-time
- refraction
stage: abstract-reasoning
status: validated
---

# Seismic Waves

## Core Idea
Earthquakes generate several types of seismic waves that travel through and along Earth, each with distinct particle motion and velocity. Primary waves (P-waves) are compressional and travel fastest through solids and liquids; secondary waves (S-waves) are shear waves that travel only through solids and arrive later. Surface waves (Love and Rayleigh) travel along Earth's surface and carry most of the destructive energy felt during an earthquake. Seismographs record the arrival times of P-, S-, and surface waves; the S–P arrival-time difference at three or more stations allows triangulation of the epicenter. P-wave and S-wave velocity increases with depth in the mantle (due to increasing rigidity) but drops sharply at the liquid outer core, where S-waves disappear entirely.

## How It's Best Learned
Working through a travel-time curve (distance vs. arrival time for P and S waves) and using the S–P time difference to locate an earthquake's epicenter gives hands-on experience with the core seismological technique. Connecting the absence of S-waves in the shadow zone to the liquid outer core makes Earth's interior structure feel like a deduction, not a fact to memorize.

## Common Misconceptions
- P-waves are not 'primary' because they are more important; the label means they arrive first.
- S-waves cannot travel through liquids, but this does not mean liquids have no seismic waves; P-waves and acoustic waves still propagate.
- Surface waves travel slower than body waves but are larger in amplitude and longer in period, causing most structural damage in distant earthquakes.

## Questions

```yaml
- question: "Why do S-waves fail to travel through Earth's outer core?"
  type: multiple-choice
  options:
    - "The outer core is too hot, and S-waves cannot propagate above a critical temperature"
    - "Shear waves require a material with a non-zero shear modulus; the liquid outer core has no shear resistance"
    - "S-waves are refracted back to the surface by the density contrast before reaching the outer core"
    - "The outer core absorbs all wave energy due to its extremely high density"
  answer: 1
  explanation: "S-waves are shear waves — they deform material sideways relative to the direction of travel. This requires the medium to resist shear deformation (i.e., have a non-zero shear modulus). Liquids flow rather than resist shear, so their shear modulus is zero and S-waves cannot propagate. The observation of an S-wave shadow zone is one of the primary lines of evidence that Earth's outer core is liquid."

- question: "Surface waves arrive at seismograph stations before P-waves and S-waves."
  type: true-false
  answer: false
  explanation: "P-waves are the fastest seismic waves and arrive first; S-waves arrive second; surface waves (Love and Rayleigh) arrive last because they travel slowest. The name 'primary' (P) and 'secondary' (S) reflects arrival order. However, surface waves have the largest amplitude and longest period, so they cause the most structural damage — a common source of confusion between 'first' and 'most destructive'."

- question: "How does the S–P arrival-time difference at a seismograph station allow seismologists to estimate the distance to an earthquake's epicenter?"
  type: short-answer
  answer: "P-waves and S-waves travel at different, known speeds through Earth. The gap between their arrival times grows predictably with distance — the farther the station from the epicenter, the larger the S–P time difference. By reading this gap from a seismogram and consulting travel-time curves (which map S–P interval to distance), seismologists can estimate how far away the earthquake occurred. Three or more stations are then needed to triangulate the exact epicenter location."
  explanation: "This is analogous to estimating how far away lightning struck by timing the gap between the flash and thunder, since light and sound travel at very different speeds. The S–P method works because P and S velocities are well-characterized from decades of seismic data and the physics of elastic wave propagation in Earth's layered interior."
```

## Explainer

When an earthquake ruptures a fault, it releases stored elastic energy that radiates outward as seismic waves — much like ripples spreading from a stone dropped in water, but in three dimensions through a solid planet. These waves come in distinct varieties, each with its own mode of particle motion and propagation speed, and reading their patterns in seismograph records is how geologists learn where earthquakes occur and what Earth's interior looks like.

The fastest seismic waves are P-waves (primary waves), which are compressional: rock is alternately squeezed and extended in the direction the wave travels, like a sound wave in air. Because compression can occur in any medium — solid or liquid — P-waves travel everywhere: through the mantle, through the liquid outer core, even through water and air (where they become acoustic waves). S-waves (secondary waves) arrive second and involve shear motion perpendicular to the direction of travel, like a snake moving sideways. This requires the medium to have shear strength — the ability to resist sideways deformation without flowing. Liquids lack this property, so S-waves are stopped cold at the boundary with Earth's liquid outer core. The observation of a global S-wave shadow zone was a crucial clue that revealed the outer core is molten.

Surface waves travel along Earth's surface rather than through the interior. Love waves move the ground horizontally; Rayleigh waves roll the ground in an elliptical motion, like ocean swells. Surface waves are slower than body waves and arrive last, but their amplitudes are typically larger and their periods longer — meaning they shake the ground for more seconds and at frequencies that resonate with buildings. Most of the structural damage during large, distant earthquakes comes from surface waves, not the faster body waves that passed through minutes earlier.

The S–P time difference is the cornerstone of locating earthquakes. Because P-waves outrun S-waves by a predictable margin that grows with distance, the gap between their arrivals on a seismogram directly encodes how far the station is from the earthquake source. With one station you get a distance (a circle on a map); with three stations you get a unique intersection point — the epicenter. This elegant triangulation technique, refined over a century, is still how earthquake locations are determined today.

A persistent misconception is that "P" means more important than "S." The letters mean primary and secondary arrival — nothing more. S-waves are equally fundamental to understanding Earth's structure: their inability to traverse the outer core revealed that it is liquid, and the contrast between P and S velocities in different Earth layers has been the primary tool for mapping the planet's interior without drilling deeper than a few kilometers.
