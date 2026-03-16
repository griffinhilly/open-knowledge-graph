---
id: seismic-moment-and-magnitude
title: Seismic Moment and Magnitude Scales
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
tags:
- seismology
- magnitude
- seismic-moment
- energy-release
stage: advanced
status: draft
---

# Seismic Moment and Magnitude Scales

## Core Idea
Seismic moment M₀ = μ × A × D (rigidity × fault area × average slip) quantifies the total energy released by an earthquake and is the most physically meaningful measure of earthquake size. Moment magnitude Mw = (2/3)log₁₀(M₀) − 10.7 is uniform across all frequency ranges and does not saturate at large magnitudes like older scales (local, body, surface wave magnitudes). The moment tensor, a 3×3 symmetric tensor, completely characterizes the radiation pattern and provides information on focal mechanism and stress orientation.

## Explainer

From focal mechanisms, you understand that earthquakes occur when stress exceeds the frictional strength of a fault, producing slip that radiates seismic waves. Seismic moment and magnitude scales give you the tools to quantify *how big* that rupture was — and they do so in a way that is grounded in the physics of the fault itself rather than in the amplitude of a particular seismogram.

The **seismic moment** M₀ = μ × A × D combines three physical quantities: the **rigidity** (shear modulus) μ of the rock surrounding the fault, the **fault area** A that ruptured, and the **average slip** D across that area. Each factor contributes independently to earthquake size. A small fault with large displacement and a large fault with small displacement can have the same moment — it is the product that matters. The units of seismic moment are Newton-meters (the same as torque), and values span an enormous range: a barely-felt magnitude-2 event might have M₀ ≈ 10⁹ N·m, while the 2011 Tōhoku earthquake reached about 5 × 10²² N·m — a factor of 10¹³ larger.

Because seismic moment spans so many orders of magnitude, it is convenient to compress it onto a logarithmic scale. The **moment magnitude** formula Mw = (2/3)log₁₀(M₀) − 10.7 does exactly this, and it was deliberately calibrated to agree with Richter's original local magnitude scale in the range where both are valid (roughly magnitude 3–7). The critical advantage of Mw is that it **does not saturate**. Older scales measured the amplitude of specific seismic wave types at specific frequencies, and for very large earthquakes, those particular waves stop getting bigger even as the fault keeps growing — the scale "clips" like an overloaded microphone. The body-wave magnitude (mb) saturates around 6.5, and the surface-wave magnitude (Ms) around 8.2. The 1960 Chilean earthquake, the largest ever recorded, was Ms 8.5 on the surface-wave scale but Mw 9.5 when measured by seismic moment — a factor of 30 more energy than the saturated scale suggests.

The **moment tensor** generalizes seismic moment into a mathematical object that captures not just the size but the geometry of the source. It is a 3×3 symmetric matrix (six independent components) whose eigenvectors define the orientation of the fault plane and slip direction, and whose eigenvalues define the magnitude and type of deformation (double-couple for simple shear faulting, plus possible non-double-couple components for more complex sources like volcanic explosions or mine collapses). Modern seismology routinely computes moment tensors for significant earthquakes within minutes using long-period waveform data from global seismic networks, providing immediate information on fault geometry, stress orientation, and earthquake size that feeds into tsunami warnings, aftershock forecasts, and tectonic studies.
