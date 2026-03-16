---
id: near-surface-geophysics-methods
title: Near-Surface Geophysics Methods
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: soft
- id: gravity-potential-theory-earths-field
  type: soft
tags:
- near-surface
- shallow-geophysics
- exploration
- environmental
stage: advanced
status: draft
---

# Near-Surface Geophysics Methods

## Core Idea
Near-surface geophysics applies seismic refraction/reflection, ground-penetrating radar (GPR), electrical resistivity, and other techniques to image the upper 10–100 m for engineering, environmental, and archaeological applications. Seismic resolution depends on wavelength (high frequency = short wavelength = high resolution); GPR uses radar waves that attenuate rapidly in conductive media. Electrical and electromagnetic methods map groundwater, contaminant plumes, and subsurface voids; integration with borehole data constrains properties and improves model reliability.

## Explainer

Near-surface geophysics adapts the same physical principles you studied in elastic wave propagation and gravity theory but operates at a completely different scale — imaging the top 10 to 100 meters of the Earth rather than kilometers-deep crustal structures. The targets are correspondingly different: buried utilities, the water table, contamination plumes, sinkholes, archaeological ruins, and foundation conditions. The methods are chosen to match the target's physical contrast with its surroundings.

**Seismic methods** at the near surface include refraction and shallow reflection surveys. In a refraction survey, you lay out a line of geophones and record the arrival times of waves that travel along layer boundaries. Because seismic velocity generally increases with depth and compaction, waves refracted along faster deeper layers arrive before the direct wave at sufficient offset distances. Plotting travel time versus distance reveals the velocity and depth of each layer — a direct application of Snell's law. Shallow reflection surveys use higher-frequency sources and tighter geophone spacing than deep surveys to resolve thin layers. The fundamental tradeoff is that **higher frequencies give better resolution but attenuate faster**, limiting penetration depth.

**Ground-penetrating radar (GPR)** transmits pulses of electromagnetic energy (typically 25 MHz to 1 GHz) into the ground and records reflections from interfaces where the dielectric constant changes — such as transitions between dry and wet soil, or soil and bedrock. GPR offers centimeter-scale resolution in favorable materials like dry sand, gravel, or ice, making it excellent for locating buried pipes, rebar, and archaeological features. However, **electrically conductive materials** like clay or saltwater rapidly absorb radar energy, limiting penetration to less than a meter in the worst cases. **Electrical resistivity imaging** fills this gap: by injecting current through electrodes pushed into the ground and measuring voltage differences, you build a cross-section of subsurface resistivity. Clay, saturated zones, and saltwater are highly conductive (low resistivity), while bedrock and dry sand are resistive — exactly the contrast GPR struggles with.

The key insight in near-surface work is that **no single method images everything**. Each technique responds to a different physical property (seismic velocity, dielectric constant, electrical conductivity, density), and each has characteristic strengths and blind spots. A contamination plume might be invisible to seismic methods but light up on resistivity profiles. A buried tunnel might reflect GPR beautifully in dry limestone but disappear in wet clay. Experienced practitioners combine multiple methods and tie them to borehole control — direct ground-truth from drilling — to build a coherent subsurface model. This integrated approach is what makes near-surface geophysics effective for the practical, high-stakes decisions it supports: where to build a foundation, whether a landfill is leaking, or where to dig for an archaeological excavation.
