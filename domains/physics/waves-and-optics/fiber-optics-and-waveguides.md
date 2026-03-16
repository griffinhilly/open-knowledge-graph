---
id: fiber-optics-and-waveguides
title: Fiber Optics and Light Waveguides
domain: physics
course: waves-and-optics
prerequisites:
- id: critical-angle-total-internal-reflection-optical
  type: hard
- id: refractive-index-material-property
  type: soft
tags:
- fiber-optics
- waveguide
- communication
stage: formal-systems
status: draft
---

# Fiber Optics and Light Waveguides

## Core Idea
Optical fibers guide light over long distances through total internal reflection at the core-cladding interface. A step-index fiber has a sharp index discontinuity; a graded-index fiber has continuously varying refractive index. Single-mode fibers support only one propagation mode and maintain coherence over long distances, while multimode fibers support many modes and are used for shorter distances. Fiber optics form the backbone of modern telecommunications.

## Explainer

You already know that total internal reflection (TIR) occurs when light traveling in a dense medium hits a boundary with a less-dense medium at an angle steeper than the **critical angle**. At that point, no light crosses the boundary — it reflects back completely with zero loss. Optical fiber engineering exploits this: by making the fiber's inner **core** slightly denser (higher refractive index) than the surrounding **cladding**, any light ray that enters the fiber at a shallow enough angle will keep hitting the core-cladding boundary below the critical angle and bounce along indefinitely. The light is trapped inside and guided around bends, even over kilometers.

The difference between step-index and graded-index fibers is about how abruptly the refractive index changes at the boundary. In a **step-index** fiber, the index jumps sharply from core to cladding. Light rays at different angles take different-length zigzag paths and arrive at the far end at slightly different times — this spreading of a pulse is called **modal dispersion**. In a **graded-index** fiber, the refractive index varies smoothly from the center outward. Rays traveling near the edge travel through lower-density material where they move faster, compensating for their longer path. The result is that all rays arrive at nearly the same time, greatly reducing pulse spreading and allowing data to travel farther without distortion.

**Single-mode** fibers take the solution further: by making the core extremely narrow (around 8–10 micrometers, comparable to the wavelength of light), only one propagation path — one "mode" — fits. There is no modal dispersion at all. These fibers are used for long-haul telecommunications (undersea cables, intercontinental links) where signal integrity over thousands of kilometers is essential. **Multimode** fibers have larger cores (50–62.5 micrometers) that allow many paths, making them cheaper and easier to connect but limited to shorter runs — typically within buildings or campuses.

The deep reason optical fiber works as a communication medium is that light at near-infrared wavelengths loses very little energy as it travels through ultra-pure silica glass — on the order of 0.2 dB per kilometer. Combine that with TIR ensuring light stays inside, and you have a channel that can carry data at terabit-per-second rates across continents. Every time you stream video or send a message internationally, the data almost certainly travels through fiber using the same total internal reflection principle you already studied.

