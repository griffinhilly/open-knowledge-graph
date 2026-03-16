---
id: magnetic-dipole-anomalies
title: Magnetic Dipole Anomalies and 3D Modeling
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: magnetic-field-reduction-pole
  type: hard
tags:
- magnetic
- dipole
- anomaly
- 3d-modeling
stage: advanced
status: draft
---

# Magnetic Dipole Anomalies and 3D Modeling

## Core Idea
Magnetic sources are modeled as dipoles whose anomalies depend on magnetization direction, moment, and position. 3D forward modeling of magnetic blocks and inversions recover source location and moment from observed anomalies.

## Explainer

From your work with Earth's magnetic dipole field, you know that Earth's background field is approximately that of a large dipole. When we conduct a magnetic survey, what we actually measure are small deviations from this background — **anomalies** caused by rocks with contrasting magnetic properties. The fundamental building block for interpreting these anomalies is the **magnetic dipole**, the simplest possible magnetic source, which produces a characteristic spatial pattern that depends on its strength, depth, and the direction it points.

Unlike gravity anomalies, which are always positive for excess mass and negative for mass deficits, magnetic anomalies are inherently more complex because magnetic fields are **dipolar**. Every magnetic source has both a north and south pole, and the anomaly it produces has both positive and negative lobes. The shape of these lobes depends critically on the **inclination** (the angle of Earth's background field from horizontal) and the **declination** (the deviation from geographic north). At the magnetic poles, where the field is vertical, a buried magnetized body produces a symmetric anomaly centered directly above it. At the magnetic equator, where the field is horizontal, the anomaly is antisymmetric — the positive and negative lobes are side by side, and the peak is offset from the source. At intermediate latitudes, you get an asymmetric combination that can be quite confusing to interpret without correction.

This is why **reduction to the pole** (a prerequisite concept) is so valuable — it mathematically transforms the data as if the survey were conducted at the north magnetic pole, simplifying anomaly shapes into symmetric patterns centered over their sources. Once reduced, interpretation becomes more intuitive. **Forward modeling** takes the opposite approach: you propose a 3D body with specified magnetization (direction and intensity), geometry, and depth, then calculate what anomaly it would produce at the surface and compare with observations. By iteratively adjusting the model, you converge on a geologically plausible source. **Inversion** automates this process, systematically searching for the distribution of magnetization that best explains the observed data subject to regularization constraints.

The practical power of dipole modeling lies in its scalability. A large ore body, an igneous intrusion, or even a buried archaeological artifact can each be approximated as one or a few dipoles for initial analysis. The magnetic moment (product of magnetization and volume) tells you how much magnetic material is present, while the anomaly width constrains depth — wider anomalies come from deeper sources, following the same geometric spreading that governs all potential fields. For detailed work, complex bodies are discretized into many small blocks, each treated as a dipole, and the total anomaly is computed as a superposition. This approach connects directly to 3D magnetic inversion, where the goal is to recover a magnetization model of the subsurface from thousands of surface measurements.
