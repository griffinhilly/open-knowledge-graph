---
id: synthetic-seismogram-modeling
title: Synthetic Seismogram Generation and Forward Modeling
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: hard
- id: elastic-wave-propagation-in-solids
  type: hard
builds-toward:
- seismic-reflection-surveys
tags:
- seismic
- modeling
- forward
- synthetic
stage: advanced
status: draft
---

# Synthetic Seismogram Generation and Forward Modeling

## Core Idea
Synthetic seismograms are calculated from 1D earth models using convolution of the seismic wavelet with the reflection coefficient series. They allow prediction of seismic responses before data acquisition and assist in interpretation.

## How It's Best Learned
Compare synthetic traces to field data. Experiment with varying wavelets, velocities, and density contrasts to understand sensitivity.

## Explainer

From your study of seismic waves and elastic wave propagation, you know that when a seismic wave encounters a boundary between layers with different acoustic properties, some energy reflects back. The strength of each reflection depends on the contrast in **acoustic impedance** (the product of velocity and density, Z = ρV) across the boundary. A synthetic seismogram is a computed prediction of what a seismic recording should look like for a given earth model — it is the forward-modeling counterpart to the interpretive task of inferring geology from recorded data.

The construction starts with a **1D earth model**: a stack of horizontal layers, each defined by its P-wave velocity, density, and thickness (often derived from well logs). From these properties, you calculate the **reflection coefficient** at each interface: R = (Z₂ − Z₁)/(Z₂ + Z₁), where Z₁ and Z₂ are the impedances above and below the boundary. A large impedance contrast (like sediment over basement rock) produces a strong reflection; a subtle contrast (like two similar sandstones) produces a weak one. The sequence of reflection coefficients plotted against two-way travel time forms the **reflectivity series** — a spike train showing where reflections originate and how strong they are.

The reflectivity series alone is not what a seismogram looks like, because the seismic source does not produce an infinitely sharp spike. It produces a **wavelet** — a short oscillating pulse with a characteristic frequency content and shape (commonly modeled as a Ricker wavelet or extracted statistically from real data). The synthetic seismogram is produced by **convolving** the reflectivity series with the source wavelet: each spike in the reflectivity series is replaced by a scaled copy of the wavelet, and all the copies are summed. The result is a wiggly trace that mimics what a real seismometer would record, with individual reflections blurred together wherever layers are thinner than about one-quarter of the dominant wavelength.

Synthetic seismograms serve two critical purposes. First, they provide a **well tie**: by generating a synthetic from well-log data and comparing it to the actual seismic trace at the well location, interpreters verify that they are correctly identifying which wiggles correspond to which geological boundaries. If the synthetic matches the recorded data, the velocity-depth model is validated and the interpreter can confidently extend geological interpretations away from the well into areas with seismic data but no wells. Second, synthetics enable **sensitivity analysis**: by varying layer thickness, velocity, or fluid content in the model and observing how the synthetic trace changes, geophysicists learn which geological changes are seismically detectable and which are below resolution — guiding both survey design and interpretation confidence.
