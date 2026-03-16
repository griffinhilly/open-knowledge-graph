---
id: seismic-body-waves-p-and-s
title: Seismic P and S Waves
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-waves
  type: soft
builds-toward:
- focal-mechanisms-and-stress-tensors
- earthquake-location-and-hypocenter
- seismic-tomography-velocity-imaging
tags:
- seismology
- body-waves
- wave-modes
- elastic-waves
stage: advanced
status: draft
---

# Seismic P and S Waves

## Core Idea
P (primary/compressional) waves are longitudinal elastic waves where particles oscillate parallel to the propagation direction; they travel fastest and arrive first at seismometers. S (secondary/shear) waves are transverse waves where particles oscillate perpendicular to propagation, travel slower, and cannot propagate through fluids. The ratio of P to S velocities constrains composition, temperature, and pressure state of crustal and mantle materials.

## How It's Best Learned
Study wave equations for both modes, plot particle motion in P and S waves, and examine seismograms from real earthquakes to identify and time P and S arrivals.

## Common Misconceptions
P waves are not faster than S waves in the same medium due to wavelength; the speed difference arises from the physical mechanisms (compression vs. shear). S waves do not become P waves; they are distinct wave types. The speeds are not constants—they depend strongly on rock type and physical conditions.

## Questions

```yaml
- question: "Why are S waves unable to propagate through Earth's outer core?"
  type: multiple-choice
  options: ["S waves are absorbed by the high temperatures in the outer core", "S waves require a solid medium to transmit shear stress, and the outer core is liquid", "S waves travel too slowly to penetrate that depth before being refracted", "S waves are converted entirely to surface waves at the core-mantle boundary"]
  answer: 1
  explanation: "Shear waves require a material with a non-zero shear modulus — in other words, the medium must resist deformation by shearing. Liquids cannot sustain shear stress, so their shear modulus is zero and S waves cannot propagate. The discovery of the S-wave shadow zone was the key evidence that Earth's outer core is liquid."

- question: "P waves travel faster than S waves in the same material because P waves have longer wavelengths."
  type: true-false
  answer: false
  explanation: "Wavelength does not determine wave speed in this context. P-wave velocity depends on the bulk modulus (resistance to compression) plus the shear modulus, divided by density: Vp = sqrt((K + 4G/3) / ρ). S-wave velocity depends only on the shear modulus: Vs = sqrt(G / ρ). Because the bulk modulus adds to the numerator for P waves, Vp > Vs regardless of wavelength. The speed difference is a consequence of the physical restoring forces, not wave geometry."

- question: "A seismograph records a P-wave arrival at time 0 and an S-wave arrival 50 seconds later. What does this S-P time interval tell a seismologist, and what additional information would be needed to locate the earthquake?"
  type: short-answer
  answer: "The 50-second S-P interval gives the distance from the seismograph to the earthquake source (epicentral distance), since P and S waves travel at known but different speeds. To locate the earthquake, you need S-P intervals from at least three seismograph stations; the intersection of three distance circles (trilateration) pinpoints the epicenter."
  explanation: "The S-P interval is a distance measurement, not a direction. Knowing that the earthquake was, say, 400 km away only places the source somewhere on a circle of radius 400 km around that station. Three such circles from three stations intersect at a unique point, yielding the epicenter. This is the basis of classical earthquake location methods."
```

## Explainer

When you studied elastic wave propagation in solids, you learned that disturbances travel through materials by transferring energy between neighboring particles via elastic restoring forces. Seismic body waves are exactly this: elastic disturbances radiating outward from an earthquake source through the solid (and partly liquid) Earth. There are two distinct modes, and understanding how each moves its particles is the key to everything else.

P waves — primary or compressional waves — are longitudinal: particles oscillate back and forth in the same direction the wave travels. As a P wave passes, the rock alternately compresses (particles push together) and rarefies (particles pull apart), like sound waves in air. Because the restoring force involves both the bulk modulus (resistance to volume change) and the shear modulus, P waves are fast — roughly 6–8 km/s in the crust. They arrive first at seismometers, which is why they are called "primary." Crucially, P waves can travel through solids, liquids, and gases, since all materials resist compression.

S waves — secondary or shear waves — are transverse: particles oscillate perpendicular to the propagation direction, like a wave on a rope. The restoring force is purely the shear modulus — resistance to shape change without volume change. Since fluids (liquids and gases) have zero shear modulus, S waves cannot propagate through them. This is not a matter of speed; it is a fundamental physical impossibility. S waves travel roughly 60% as fast as P waves in the same rock. When seismologists noticed a global "S-wave shadow zone" in the 1900s, they inferred that Earth must contain a liquid outer core — one of the most important deductions in geophysical history.

The difference in arrival times between P and S waves at a seismometer — the S-P interval — grows with distance from the earthquake. Since both wave types leave the source simultaneously but travel at different speeds, a longer travel path means a larger gap between arrivals. This interval is a distance measurement: it places the seismometer somewhere on a sphere of a certain radius centered on the earthquake. With S-P intervals from three or more stations, seismologists can triangulate the epicenter precisely.

Beyond location, the velocities of P and S waves — and how they change with depth — encode the composition and physical state of every layer they traverse. Higher velocities indicate denser, stiffer material; a drop in Vs to zero marks a liquid zone. Modern seismic tomography uses millions of wave-arrival times to build three-dimensional images of mantle structure, much like a medical CT scan — but using earthquake waves instead of X-rays.
