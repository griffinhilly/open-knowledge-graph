---
id: moment-tensor-inversion
title: Moment Tensor Inversion
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: earthquake-location-and-hypocenter
  type: soft
tags:
- seismology
- moment-tensor
- source-inversion
- focal-mechanism
stage: advanced
status: draft
---

# Moment Tensor Inversion

## Core Idea
The seismic moment tensor M is a 3×3 symmetric tensor that fully characterizes the earthquake source radiation pattern without assuming a simple double couple. Moment tensor inversion fits observed waveforms (displacement, velocity, or acceleration) by minimizing misfit between data and synthetic seismograms computed via Green's function convolution. The moment tensor eigenvalues and eigenvectors reveal the nodal planes, type of faulting (normal, reverse, strike-slip), and moment magnitude.
