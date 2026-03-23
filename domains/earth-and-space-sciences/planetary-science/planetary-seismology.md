---
id: planetary-seismology
title: Planetary Seismology and Interior Structure
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: seismic-waves
  type: hard
- id: planetary-interior-dynamics
  type: soft
tags:
- seismology
- interior-structure
- waves
stage: expert
status: validated
---

# Planetary Seismology and Interior Structure

## Core Idea
Seismic waves from quakes and impacts propagate through planetary interiors, reflecting and refracting at boundaries with different acoustic properties. Analysis of waveforms (P-waves, S-waves, surface waves) reveals interior velocity structure and compositional boundaries without requiring direct sampling. Seismology has revolutionized understanding of lunar and Martian interiors.

## Questions

```yaml
- question: "A seismometer on a distant planetary station records P-waves arriving from a large quake but detects no S-waves. What does this most directly imply about the interior the waves traveled through?"
  type: multiple-choice
  options:
    - "The planet has no seismic activity strong enough to generate S-waves"
    - "The waves traveled through a liquid region, which transmits P-waves but blocks S-waves"
    - "The planet's crust is too thin to sustain S-wave propagation"
    - "The seismometer is too far from the quake source to detect S-waves"
  answer: 1
  explanation: "S-waves are shear waves that require a solid medium; they cannot propagate through liquids. An S-wave shadow zone is therefore direct evidence of a liquid layer in the wave path. This is exactly how Earth's liquid outer core was discovered — and the same logic applies to any planetary body. Distance alone does not prevent S-wave detection; both wave types attenuate with distance, but the key difference is physical state of the medium."

- question: "Lunar seismograms from Apollo show signals ringing for over an hour after a quake, far longer than on Earth. What explains this?"
  type: multiple-choice
  options:
    - "The Moon experiences much stronger quakes than Earth"
    - "The dry, fractured lunar crust scatters seismic energy rather than absorbing it, prolonging the signal"
    - "The Moon's large liquid core amplifies and re-emits seismic energy"
    - "Apollo seismometers were more sensitive than modern Earth instruments"
  answer: 1
  explanation: "On Earth, water-saturated rocks in the crust absorb seismic energy quickly, damping the signal. The Moon's crust is dry and highly fractured, so energy scatters rather than dissipates — the signal bounces around for a very long time. The Moon's crust having no liquid core to speak of, and seismometer sensitivity being a design choice unrelated to signal duration, make the other options incorrect."

- question: "The InSight mission determined that Mars has a liquid iron-alloy core with a radius of about 1,830 km without any drill reaching it."
  type: true-false
  answer: true
  explanation: "InSight's single broadband seismometer detected marsquakes whose seismic wave travel times and reflections revealed interior velocity boundaries, including the core-mantle boundary. The liquid state was inferred from seismic behavior (P-waves can pass through, S-waves cannot), just as Earth's liquid outer core was discovered seismically decades before any direct sampling was even conceivable. This is the power of seismology: access to interiors that are otherwise completely unreachable."

- question: "Having only one seismometer on a planet makes it impossible to determine anything meaningful about planetary interior structure."
  type: true-false
  answer: false
  explanation: "InSight operated with a single seismometer on Mars and still resolved crustal thickness, mantle seismic velocities, and core radius. Techniques such as surface wave dispersion analysis, receiver functions, and using independently located sources (like meteorite impacts) extract interior information from a single station. Fewer stations mean more uncertainty and creative analysis, but not a complete absence of information."

- question: "Why can seismology reveal the interior structure of a planet without any direct sampling or drilling?"
  type: short-answer
  answer: "Seismic waves change speed and direction whenever they cross a boundary between materials with different densities or elastic properties. P-waves and S-waves reflect, refract, and convert at these boundaries, and the arrival times and waveforms recorded at the surface encode the entire path traveled. Because S-waves cannot pass through liquids, their absence from certain azimuths identifies liquid regions. By analyzing which phases arrive when, scientists reconstruct the layered velocity structure — and thus the composition and physical state — of the deep interior."
  explanation: "The key principle is that wave behavior at boundaries is diagnostic: reflections indicate boundary depth, refraction angles indicate velocity contrast, and the absence of S-waves indicates liquid. This works across any planet because it depends only on the physics of wave propagation in elastic media, not on any planet-specific assumption."
```

## Explainer

You already know that **seismic waves** travel through rock at speeds determined by the material's density and elastic properties, and that P-waves (compressional) and S-waves (shear) behave differently — P-waves travel through both solids and liquids, while S-waves propagate only through solids. On Earth, this difference is what revealed the liquid outer core: S-waves vanish in a "shadow zone" because they cannot pass through molten iron. Planetary seismology extends exactly the same logic to other worlds, using quakes, impacts, or artificial sources to illuminate interiors that are otherwise completely inaccessible.

The Apollo missions placed seismometers on the Moon between 1969 and 1972, providing the first extraterrestrial seismic dataset. Lunar seismology revealed a crust about 30–45 km thick, a mantle with distinct upper and lower regions, and a small, partially molten core. The Moon turned out to be a surprisingly noisy body — **deep moonquakes** occur in clusters at specific depths around 700–1,100 km, triggered by tidal stresses from Earth's gravity. These repeating sources acted as natural controlled experiments, since waves from the same location but recorded at different stations illuminated different interior paths. One striking feature of lunar seismograms is their extreme duration: seismic signals ring for over an hour because the dry, fractured lunar crust scatters energy rather than absorbing it, unlike Earth's water-saturated rocks that damp vibrations quickly.

NASA's InSight mission, which landed on Mars in 2018, brought planetary seismology into the modern era. Its single broadband seismometer, SEIS, detected over a thousand **marsquakes** during its operational lifetime. The data revealed that Mars has a thick crust (24–72 km depending on location), a mantle with seismic velocities suggesting an olivine-rich composition similar to Earth's upper mantle, and a liquid iron-alloy core with a radius of roughly 1,830 km — larger and less dense than expected, implying a significant fraction of light elements like sulfur dissolved in the core. This finding reshaped models of Martian formation and thermal history. InSight also recorded seismic signals from meteorite impacts, providing both seismic data and independently located sources, which tightened constraints on crustal structure.

The fundamental challenge of planetary seismology is working with far fewer stations than Earth-based networks. Earth has thousands of seismometers; the Moon had four simultaneously active stations at best; Mars had one. With fewer stations, locating quake sources and resolving interior structure requires creative techniques — using surface wave dispersion, reflected phases, and receiver functions to extract maximum information from limited data. Despite these constraints, seismology remains the most powerful tool for determining what lies beneath a planetary surface, and future missions to Europa, Titan, and Venus all include seismic instrumentation in their concept studies.
