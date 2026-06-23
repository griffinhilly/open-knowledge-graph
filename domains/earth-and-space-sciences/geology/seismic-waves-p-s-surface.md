---
id: seismic-waves-p-s-surface
title: 'Seismic Waves: Body Waves and Surface Waves'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: earthquake-mechanisms-stress-release
  type: hard
- id: wave-properties-intro
  type: hard
- id: earthquakes-and-faults
  type: soft
builds-toward:
- earthquake-location-and-hypocenter
tags:
- seismology
- waves
- crustal-structure
stage: formal-systems
status: validated
---

# Seismic Waves: Body Waves and Surface Waves

## Core Idea
Earthquakes generate body waves (P and S waves) and surface waves (Rayleigh and Love) that propagate through and along the Earth. Wave velocities depend on rock composition and density; travel-time differences constrain hypocenter location, focal depth, and Earth's internal structure.

## Questions

```yaml
- question: "Seismograph stations on the opposite side of the Earth from a major earthquake record P waves but fail to record S waves at certain angular distances. What does this S-wave shadow zone tell us about Earth's interior?"
  type: multiple-choice
  options:
    - "The earthquake was too weak to generate S waves that could travel the full distance"
    - "S waves are absorbed by the mantle while P waves pass through, indicating a partially molten mantle"
    - "Earth's outer core is liquid; S waves require a solid medium and cannot propagate through it"
    - "S waves were converted to P waves at the core-mantle boundary and arrived as P waves"
  answer: 2
  explanation: "S waves are shear waves that require a medium capable of resisting shear deformation — liquids cannot sustain shear stress and therefore cannot transmit S waves. When seismologists mapped the angular distances where S waves are completely absent (the S-wave shadow zone, roughly 105°–140° from the epicenter), they concluded that S waves must be passing through a region that cannot transmit shear — Earth's liquid outer core. P waves (compressional) can travel through both solids and liquids, so they continue through the outer core, though refracted. The S-wave shadow zone is the primary seismological evidence for the liquid outer core."

- question: "During an earthquake, which wave type typically causes the most structural damage to buildings?"
  type: multiple-choice
  options:
    - "P waves, because they arrive first and cause instantaneous compression damage"
    - "S waves, because their shear motion acts perpendicular to the propagation direction"
    - "Surface waves, because they carry the most energy and produce the largest, most sustained ground displacements"
    - "Rayleigh waves exclusively, since Love waves cancel out within structures"
  answer: 2
  explanation: "Surface waves are the most destructive. They travel more slowly than body waves but carry substantially more energy and generate far larger ground displacements. Rayleigh waves produce a rolling elliptical motion particularly damaging to structures; Love waves cause horizontal shearing. Because surface waves are confined near the surface where buildings exist, their energy is concentrated where it causes maximum damage. P waves produce a brief compression jolt, and S waves shake the ground transversely, but surface waves sustain large-amplitude shaking for a longer duration as the slower wave train arrives."

- question: "S waves cannot propagate through Earth's outer core because that region is liquid and has no resistance to shear deformation."
  type: true-false
  answer: true
  explanation: "True. Shear waves require that the medium resist shear deformation — the restoring force that sustains transverse oscillation. Liquids flow rather than restoring to their original shape under shear stress; there is no restoring force to propagate a shear wave. Therefore S waves cannot travel through liquids at all. The existence of a global S-wave shadow zone maps the size of Earth's liquid outer core precisely, because S waves reaching this region are blocked while those that miss the core arrive normally on the far side."

- question: "P waves cause more ground shaking and structural damage than surface waves during an earthquake."
  type: true-false
  answer: false
  explanation: "False. P waves arrive first, often producing a brief thump or jolt, but they carry relatively little energy compared to surface waves and produce small ground displacements. Surface waves arrive later (traveling more slowly) but bring far larger amplitudes and sustained shaking. Most building damage and seismic hazard in earthquake-prone areas is attributed to surface wave motion. This is why earthquake engineering focuses on how structures respond to the low-frequency, large-amplitude shaking of surface waves rather than the initial P-wave arrival."

- question: "Explain how recording P and S wave arrival times at multiple seismograph stations allows geologists to determine where an earthquake occurred."
  type: short-answer
  answer: "P waves always travel faster than S waves, so the P–S arrival time gap at any station grows with distance from the earthquake. Measuring this time gap at one station gives the distance to the epicenter (but not the direction). With three or more stations at different locations, geologists draw a circle of calculated radius around each station; the earthquake epicenter is the unique point where all circles intersect (triangulation). Focal depth is constrained by comparing body-wave travel times with surface-wave arrivals and by the directional pattern of wave amplitudes."
  explanation: "This method works because P and S wave speeds in different rock types are known from studying thousands of previous earthquakes. The P–S time gap is like hearing thunder 10 seconds after lightning — it tells you the storm is ~3 km away, but not in which direction. Three stations provide three distance circles with a unique intersection. Modern seismological networks use hundreds of stations and sophisticated waveform inversion to locate earthquakes within kilometers of their true epicenter and depth, providing near-real-time location estimates within minutes of any significant earthquake."
```

## Explainer

From your study of wave properties and elastic wave propagation, you know that waves transmit energy through a medium by displacing particles from their equilibrium positions, and that the speed of propagation depends on the medium's elastic properties and density. When an earthquake ruptures a fault, it converts stored elastic strain energy into seismic waves that radiate outward in all directions. These waves fall into two fundamental categories: **body waves** that travel through Earth's interior, and **surface waves** that travel along the boundary between the Earth and the atmosphere.

**Body waves** come in two types. **P waves** (primary waves) are compressional — they push and pull particles in the same direction the wave travels, exactly like a sound wave in air or the compression pulse you can send down a Slinky by pushing one end. Because they involve volume changes (compression and expansion), P waves can travel through solids, liquids, and gases, and they are the fastest seismic waves, typically moving at 5–8 km/s in crustal rocks. **S waves** (secondary waves) are shear waves — they displace particles perpendicular to the direction of propagation, like the sideways wiggle that travels down a rope when you flick one end. Shear deformation requires a material that resists shape change, which liquids do not, so S waves cannot propagate through liquids. This single fact is how we know Earth's outer core is liquid: S waves generated by earthquakes on one side of the planet are absent from seismograms on the other side at specific angular distances, creating an **S-wave shadow zone** that maps the liquid core's boundary.

**Surface waves** are generated when body waves interact with Earth's free surface. **Rayleigh waves** produce an elliptical rolling motion — particles move both vertically and horizontally in the direction of propagation, like ocean waves but in solid rock. **Love waves** produce purely horizontal shearing motion perpendicular to the direction of travel. Surface waves are slower than body waves but carry more energy and produce larger ground displacements, which is why they cause the most damage during earthquakes. They also have a property called **dispersion**: longer-wavelength surface waves penetrate deeper into the Earth and travel faster than shorter-wavelength ones, so a surface wave train spreads out as it propagates. Seismologists exploit this dispersion to map how velocity changes with depth in the crust and upper mantle.

The practical power of seismic waves lies in their **travel-time differences**. Because P waves always arrive before S waves at any given station, and the time gap between them increases with distance from the earthquake, recording the P–S arrival time difference at three or more seismograph stations allows geologists to triangulate the earthquake's location and depth. Beyond locating earthquakes, the way seismic wave velocities change with depth — speeding up in denser rock, slowing in partially molten zones, vanishing (for S waves) in liquid — provides the primary evidence for Earth's layered internal structure: crust, mantle, liquid outer core, and solid inner core. Seismology is essentially using earthquakes as a natural source of illumination to image the deep Earth, much as medical ultrasound uses sound waves to image the body's interior.
