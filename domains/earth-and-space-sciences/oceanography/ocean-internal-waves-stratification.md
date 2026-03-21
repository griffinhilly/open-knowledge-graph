---
id: ocean-internal-waves-stratification
title: Internal Waves and Stratified Flow
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: internal-waves-density-stratification
  type: hard
- id: ocean-stratification-and-mixing
  type: hard
builds-toward:
- ocean-mixing-and-turbulence
- coastal-processes-and-waves
tags:
- internal-waves
- stratification
- mixing
- energy-transfer
stage: advanced
status: draft
---

# Internal Waves and Stratified Flow

## Core Idea
Internal waves form at density discontinuities within the ocean (thermoclines and haloclines) and can grow to amplitudes exceeding surface waves. These waves drive vertical mixing and transfer mechanical energy from tides and currents to small-scale turbulence and heat.

## Questions

```yaml
- question: "Internal waves in the deep ocean can reach amplitudes exceeding 100 meters, far beyond typical surface waves. What primarily explains why such large displacements are possible?"
  type: multiple-choice
  options:
    - "The greater depth of the ocean provides more vertical space for wave oscillation to develop"
    - "Internal waves carry more energy than surface waves because tidal forcing is stronger than wind forcing"
    - "The tiny density contrast between ocean layers means the restoring force is weak, allowing large displacements without requiring proportionally large energy"
    - "Internal waves are not restrained by gravity in the same way surface waves are"
  answer: 2
  explanation: "At the ocean surface, the density contrast between air and water is about 800:1, creating a strong restoring force that limits amplitude. At interior pycnoclines, the density difference between layers is less than 1% — a tiny contrast that means very little energy is needed to displace the interface by large amounts. This is the same physics as surface waves but with a vastly weaker restoring force. The large amplitude is a consequence of that weakness, not of available space or energy source strength."

- question: "What is the primary mechanism by which internal waves are generated in the deep ocean?"
  type: multiple-choice
  options:
    - "Wind stress at the surface drives turbulence that propagates downward as internal oscillations"
    - "Barotropic tidal currents flowing over rough seafloor topography force water columns to oscillate vertically, radiating internal waves"
    - "Thermohaline circulation creates vertical density instabilities that spontaneously radiate wave energy"
    - "Solar heating of the surface layer drives thermal expansion that launches waves along the thermocline"
  answer: 1
  explanation: "When the barotropic (surface) tide flows horizontally over seafloor ridges, seamounts, or shelf edges, the flow is forced upward and downward over the bumps, generating oscillating vertical displacements in the stratified water column. These launch internal waves — called baroclinic tides — that radiate away from the topography. This conversion of tidal energy accounts for roughly half of all tidal dissipation in the deep ocean. Wind-driven oscillations also generate internal waves but are secondary in the deep-ocean energy budget."

- question: "Internal waves travel more slowly than surface waves because the density contrast at interior ocean boundaries is far smaller than the density contrast between water and air."
  type: true-false
  answer: true
  explanation: "Wave speed depends on the density contrast across the interface: a larger contrast produces a stronger restoring force and faster wave propagation. At the ocean surface, the water-air density ratio is about 1025:1.2 ≈ 800:1 — enormous. At an interior pycnocline, the density difference between adjacent layers may be less than 1 kg/m³ out of ~1025 kg/m³ — a ratio under 0.1%. This tiny contrast produces a weak restoring force, yielding internal wave speeds of only centimeters per second compared to meters per second for surface waves."

- question: "The locations where internal waves are generated and where they eventually break and mix the ocean always coincide, because internal waves lose their energy immediately upon formation at seafloor topography."
  type: true-false
  answer: false
  explanation: "Internal waves can travel hundreds to thousands of kilometers from their generation sites before breaking and dissipating. A wave generated at a mid-ocean ridge may propagate across an entire ocean basin, steepening and eventually breaking in an entirely different region. This spatial decoupling matters for ocean circulation: seafloor topography in one location controls mixing rates far away. It also means that local mixing measurements need not reflect local wave generation — the energy may have originated at a distant source."

- question: "Why is the breaking of internal waves important for the large-scale ocean circulation, and what would happen to deep-ocean mixing if internal waves were absent?"
  type: short-answer
  answer: "Internal wave breaking converts organized wave energy into small-scale turbulence, which mixes water across density surfaces — lifting cold, dense deep water upward. This turbulent mixing is essential for closing the thermohaline overturning circulation, which depends on cold bottom water being continuously returned toward the surface. Without internal wave breaking, deep-water mixing rates would be far lower, the overturning circulation would weaken dramatically, and the deep ocean would stagnate."
  explanation: "The thermohaline circulation is driven partly by surface cooling and sinking at high latitudes, but requires an upward return pathway for dense deep water. Without diapycnal (cross-density-surface) mixing, that deep water has no efficient way to return to the surface. Internal wave breaking is the dominant source of diapycnal mixing in the ocean interior away from boundaries — it provides the mechanical energy needed to lift dense water against gravity. Estimates suggest roughly 2 TW of mixing power is needed to sustain the overturning circulation, and internal wave dissipation supplies much of that."
```

## Explainer

From your study of ocean stratification, you know that the ocean is not a uniform fluid — it is layered by density, with warmer, lighter water sitting atop colder, denser water, separated by a sharp transition called the **thermocline** (or **pycnocline** when salinity differences also contribute). Surface waves travel along the boundary between air and water, where the density contrast is enormous. Internal waves obey the same physics but travel along density boundaries *within* the ocean, where the density contrast between layers is much smaller — typically less than 1%. This small density difference has a dramatic consequence: internal waves move slowly (often just centimeters per second compared to meters per second for surface waves) but can achieve enormous amplitudes, sometimes exceeding 100 meters from trough to crest, dwarfing anything seen at the surface.

The primary energy source for internal waves is the **barotropic tide** — the familiar rise and fall of sea level driven by the Moon and Sun. When tidal currents flow over rough seafloor topography such as ridges, seamounts, and continental shelf edges, the interaction between the horizontal flow and the bumpy bottom forces water columns to oscillate vertically, launching internal waves that radiate away from the generation site. This conversion of tidal energy into internal wave energy is called **baroclinic tide generation**, and it accounts for roughly half of all tidal energy dissipation in the deep ocean. Wind-driven near-inertial oscillations and current-topography interactions also generate internal waves, but tidal forcing dominates the deep-ocean energy budget.

As internal waves propagate through the stratified interior, they can steepen, interact with each other, and eventually break — much like surface waves breaking on a beach. When an internal wave breaks, it converts its organized oscillatory energy into small-scale **turbulence**, which mixes water across density surfaces. This turbulent mixing is critical to the ocean's large-scale circulation: it lifts cold, dense deep water upward, helping to close the thermohaline overturning circulation that you encountered in studying ocean stratification and mixing. Without internal wave breaking, the deep ocean would stagnate far more than it does. The regions where internal waves are generated and where they break are not necessarily the same — waves can travel hundreds of kilometers before dissipating — which means that seafloor topography in one location can control mixing rates in distant parts of the ocean.

Internal waves also matter at smaller scales. In coastal waters, large-amplitude internal waves (sometimes called **internal solitary waves** or solitons) generated at the continental shelf break can propagate shoreward, creating sudden pulses of cold, nutrient-rich deep water into shallow environments. These events can deliver nutrients to coral reefs, trigger rapid temperature drops that stress or benefit organisms, and generate strong bottom currents that resuspend sediments. Satellite imagery can actually detect internal waves indirectly: their vertical displacements modulate surface roughness patterns, creating visible bands on radar images. Understanding internal waves thus connects the physics of stratified flow to biological productivity, climate-scale circulation, and practical concerns like submarine navigation and offshore engineering.
