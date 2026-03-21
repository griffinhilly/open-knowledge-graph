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

## Questions

```yaml
- question: "A moment tensor solution for a seismic event shows that all three diagonal components are large and equal, with near-zero off-diagonal elements. What does this indicate about the source?"
  type: multiple-choice
  options:
    - "A pure strike-slip fault, because all principal stresses are equal"
    - "A pure thrust fault, because the equal diagonal components indicate horizontal compression"
    - "A volumetric (isotropic) source such as a volcanic explosion or implosion, not a fault slip"
    - "A double-couple source with M₀ = the diagonal value"
  answer: 2
  explanation: "A pure double-couple (fault slip) produces eigenvalues of +M₀, 0, −M₀ — not equal values. Equal and same-sign diagonal components of the moment tensor represent isotropic expansion (or contraction) — volume change in all directions. This is the signature of a volcanic explosion, a collapsing magma chamber, or an underground explosion. The moment tensor framework is valuable precisely because it can detect these non-fault sources that the traditional focal mechanism (which assumes double-couple) cannot represent."

- question: "Why must moment tensor inversion use recordings from seismic stations distributed at many different azimuths around the earthquake, rather than a cluster of stations all in one direction?"
  type: multiple-choice
  options:
    - "Distant stations record fewer noise artifacts and produce cleaner waveforms"
    - "The moment tensor has six independent components, and each station constrains a different linear combination of them — poor azimuthal coverage leaves some components underdetermined"
    - "Seismic waves travel faster in certain directions and need multiple stations to average out the velocity variation"
    - "Regulations require station coverage for legal attribution of fault responsibility"
  answer: 1
  explanation: "Each observed seismogram at a given station is a linear combination of the six moment tensor components, weighted by the Green's functions for that particular source-station geometry. Different azimuths sample different combinations of these components. If all stations are in the same direction, many combinations are not independently sampled, and several components remain poorly constrained — the inversion is underdetermined. Good azimuthal coverage is essential for resolving all six components simultaneously."

- question: "For a pure double-couple earthquake source, the three eigenvalues of the seismic moment tensor are +M₀, 0, and −M₀, where M₀ is the scalar seismic moment."
  type: true-false
  answer: true
  explanation: "This eigenvalue structure is the mathematical signature of a double-couple: two equal and opposite principal moments with a null axis. It reflects the force-couple geometry of shear faulting — equal amounts of compression and tension at 45° to the fault, with a null axis perpendicular to the fault plane. When a moment tensor is decomposed and the null eigenvalue is exactly zero, the source is consistent with pure fault slip. Non-zero null eigenvalues indicate CLVD or isotropic components, signaling a more complex source."

- question: "Moment tensor inversion determines which of the two nodal planes is the actual fault plane, because the seismic radiation pattern differs between the fault plane and the auxiliary plane."
  type: true-false
  answer: false
  explanation: "This is a fundamental limitation of the moment tensor: the seismic radiation pattern from a pure double-couple is identical whether you treat either nodal plane as the fault. The moment tensor cannot distinguish the true fault plane from the auxiliary plane on the basis of far-field seismic data alone. Resolving this ambiguity requires additional information: surface rupture observations, aftershock distribution along one of the planes, geological context, or local geodetic data (GPS, InSAR). This is one reason why moment tensor solutions always report two possible nodal planes."

- question: "What are Green's functions in the context of moment tensor inversion, and why does the accuracy of the Earth velocity model affect the quality of the moment tensor solution?"
  type: short-answer
  answer: "Green's functions are the theoretical seismograms that would be recorded at each station if a single elementary force couple (one of the six basis force systems) acted at the source location. They encode how seismic waves travel through the Earth's crust from that source to each recording station. In moment tensor inversion, the observed waveforms are modeled as weighted sums of these Green's functions, and the weights — the six moment tensor components — are solved by least-squares. If the velocity model used to compute the Green's functions is inaccurate, the predicted wave arrival times and amplitudes will not match the observed waveforms well, and the inversion will distribute the mismatch into incorrect moment tensor components. Better velocity models produce more accurate Green's functions and therefore more reliable moment tensor solutions."
  explanation: "This is why moment tensor inversions for small earthquakes (where local velocity structure matters most) are harder than for large events (where long-period waves average over larger volumes and are less sensitive to local heterogeneity). Global agencies use long-period waveforms partly to reduce sensitivity to imperfect velocity models."
```

## Explainer

From focal mechanisms, you know that the pattern of first motions recorded around an earthquake — which stations see compressional arrivals and which see dilatational ones — can be divided into quadrants by two perpendicular nodal planes, one of which is the actual fault plane. The familiar "beach ball" diagram encodes this pattern. The **moment tensor** is the mathematical generalization of this idea: instead of just recording the polarity pattern, it captures the full amplitude and waveform of the seismic radiation, allowing you to characterize sources that are more complex than a simple fault slip.

The **seismic moment tensor M** is a 3×3 symmetric matrix with six independent components. Each component represents a force couple — a pair of opposing forces offset from each other — acting in a particular orientation. For a pure fault slip (a **double-couple source**), the moment tensor has a specific structure: its three eigenvalues are +M₀, 0, and −M₀, where M₀ is the scalar seismic moment (the product of rigidity, fault area, and average slip). But the moment tensor framework can also represent sources that are not pure fault slip: volcanic explosions produce **isotropic** components (equal expansion in all directions), and tensile crack openings produce **compensated linear vector dipole (CLVD)** components. Decomposing a moment tensor into its double-couple, CLVD, and isotropic parts reveals whether the source is a simple earthquake or something more exotic.

**Moment tensor inversion** determines the six components of M from recorded seismograms. The procedure relies on **Green's functions** — the theoretical seismograms that would be produced by each of the six elementary force couples acting at the source location and recorded at each station. These are computed from a velocity model using synthetic seismogram codes. The observed waveforms at multiple stations are then expressed as a linear combination of these Green's functions, weighted by the unknown moment tensor components. Because the problem is linear in the moment tensor elements, it can be solved by least-squares fitting: find the six values of M that minimize the misfit between observed and synthetic waveforms across all stations and components simultaneously.

The quality of the solution depends on several factors: the accuracy of the velocity model (which controls the Green's functions), the azimuthal coverage of the recording stations (poor coverage leaves some components poorly constrained), and the frequency band used (lower frequencies are less sensitive to small-scale velocity heterogeneities and are therefore more robust). The resulting moment tensor yields the **moment magnitude** Mw from the scalar moment, the orientations of the nodal planes from the eigenvectors, and the style of faulting from the eigenvalue ratios. Global agencies like the USGS and Global CMT project routinely compute moment tensors for earthquakes above magnitude ~5, providing the standard characterization of earthquake sources worldwide.
