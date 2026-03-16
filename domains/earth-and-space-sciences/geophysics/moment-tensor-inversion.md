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

## Explainer

From focal mechanisms, you know that the pattern of first motions recorded around an earthquake — which stations see compressional arrivals and which see dilatational ones — can be divided into quadrants by two perpendicular nodal planes, one of which is the actual fault plane. The familiar "beach ball" diagram encodes this pattern. The **moment tensor** is the mathematical generalization of this idea: instead of just recording the polarity pattern, it captures the full amplitude and waveform of the seismic radiation, allowing you to characterize sources that are more complex than a simple fault slip.

The **seismic moment tensor M** is a 3×3 symmetric matrix with six independent components. Each component represents a force couple — a pair of opposing forces offset from each other — acting in a particular orientation. For a pure fault slip (a **double-couple source**), the moment tensor has a specific structure: its three eigenvalues are +M₀, 0, and −M₀, where M₀ is the scalar seismic moment (the product of rigidity, fault area, and average slip). But the moment tensor framework can also represent sources that are not pure fault slip: volcanic explosions produce **isotropic** components (equal expansion in all directions), and tensile crack openings produce **compensated linear vector dipole (CLVD)** components. Decomposing a moment tensor into its double-couple, CLVD, and isotropic parts reveals whether the source is a simple earthquake or something more exotic.

**Moment tensor inversion** determines the six components of M from recorded seismograms. The procedure relies on **Green's functions** — the theoretical seismograms that would be produced by each of the six elementary force couples acting at the source location and recorded at each station. These are computed from a velocity model using synthetic seismogram codes. The observed waveforms at multiple stations are then expressed as a linear combination of these Green's functions, weighted by the unknown moment tensor components. Because the problem is linear in the moment tensor elements, it can be solved by least-squares fitting: find the six values of M that minimize the misfit between observed and synthetic waveforms across all stations and components simultaneously.

The quality of the solution depends on several factors: the accuracy of the velocity model (which controls the Green's functions), the azimuthal coverage of the recording stations (poor coverage leaves some components poorly constrained), and the frequency band used (lower frequencies are less sensitive to small-scale velocity heterogeneities and are therefore more robust). The resulting moment tensor yields the **moment magnitude** Mw from the scalar moment, the orientations of the nodal planes from the eigenvectors, and the style of faulting from the eigenvalue ratios. Global agencies like the USGS and Global CMT project routinely compute moment tensors for earthquakes above magnitude ~5, providing the standard characterization of earthquake sources worldwide.
