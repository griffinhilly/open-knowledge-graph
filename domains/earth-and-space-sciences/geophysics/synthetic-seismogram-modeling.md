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
builds-toward: []
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

## Questions

```yaml
- question: "A geophysicist constructs a reflectivity series from a 1D earth model but finds it does not resemble the actual seismic trace at the well location. What step is most likely missing?"
  type: multiple-choice
  options:
    - "The reflectivity series needs to be transformed to the frequency domain before comparison"
    - "The reflectivity series must be convolved with a source wavelet to produce the synthetic seismogram"
    - "The velocities must be converted from km/s to m/s to match the seismic trace units"
    - "The reflection coefficients must be summed to produce a single composite amplitude"
  answer: 1
  explanation: "The reflectivity series is a spike train showing reflection strengths at each interface — it is not yet a seismogram. A real seismic source emits a wavelet (a short oscillating pulse), not an infinitely sharp spike. The recorded seismogram is the convolution of the reflectivity series with this wavelet: each spike is replaced by a scaled, time-shifted copy of the wavelet, and all copies are summed. Without this convolution, there is no physically meaningful comparison to recorded data. The convolution step is the core of synthetic seismogram generation."

- question: "Two geological layers are separated by 20 meters of depth. The dominant seismic wavelength is 80 meters. What does synthetic seismogram theory predict about resolving these layers as separate reflections?"
  type: multiple-choice
  options:
    - "The layers will be clearly resolved because any interface produces a reflection regardless of spacing"
    - "The layers will appear as a single composite reflection because their spacing is at or below the tuning thickness of one-quarter wavelength"
    - "The layers will produce identical synthetic traces regardless of the wavelet used"
    - "Resolution depends only on acquisition geometry and source energy, not on wavelength"
  answer: 1
  explanation: "The vertical resolution limit for conventional seismic reflection is approximately one-quarter of the dominant wavelength — the tuning thickness. With a dominant wavelength of 80 m, the tuning thickness is ~20 m. Two interfaces separated by 20 m or less produce reflected wavelets that overlap in time, interfering constructively or destructively into a single composite waveform rather than two distinct reflections. This is a fundamental physical limit imposed by wave physics, not an equipment limitation. Synthetic seismograms explicitly model this blending through the convolution operation."

- question: "A synthetic seismogram is computed by convolving the reflection coefficient series with a source wavelet, where reflection coefficients at each interface depend on the acoustic impedance contrast across that boundary."
  type: true-false
  answer: true
  explanation: "This is the complete, correct definition of the synthetic seismogram workflow. Acoustic impedance Z = ρV (density × velocity). Reflection coefficient at each interface R = (Z₂ − Z₁)/(Z₂ + Z₁). The sequence of these R values plotted against two-way travel time is the reflectivity series. Convolving this with the source wavelet produces the synthetic seismogram. Every element in this chain is directly grounded in the physics of elastic wave propagation and the mathematics of linear convolution."

- question: "Synthetic seismograms generated from well-log data are primarily used to predict seismic responses in undrilled areas, because they reveal the geology where no wells exist."
  type: true-false
  answer: false
  explanation: "Synthetic seismograms are generated FROM well data and are used to calibrate the seismic interpretation AT the well location — this is the 'well tie.' By matching the synthetic trace to the actual recorded seismic trace at the known well, interpreters verify which seismic wiggles correspond to which geological boundaries. This verified calibration then allows extending the interpretation AWAY from the well into areas covered by seismic but without wells. Synthetics illuminate geology at a known location, not in unknown undrilled areas."

- question: "Explain why convolution of the reflectivity series with the source wavelet is the central operation in synthetic seismogram generation, and what physical process this convolution represents."
  type: short-answer
  answer: "A real seismic source emits a wavelet — a short oscillating pulse — not an infinitely sharp spike. When this wavelet reaches each subsurface interface, a reflected copy of the wavelet is generated, scaled by the reflection coefficient at that interface. The total seismogram at the surface is the sum of all these scaled, time-shifted wavelet copies. Convolution is precisely the mathematical operation that replaces each spike in the reflectivity series with a scaled wavelet copy and sums them all — representing the physical superposition of reflected waveforms."
  explanation: "Understanding convolution as a physical process rather than a mathematical trick is key. The source emits one pulse; it arrives at many interfaces at different travel times; each interface sends back a reflected copy of that pulse, scaled by the local impedance contrast. The seismometer records the sum of all these reflections arriving over time. When interfaces are closely spaced, their reflected wavelets overlap in time and interfere — this is why thin beds below tuning thickness appear as one composite wiggle. The wavelet's duration sets the temporal resolution limit, and convolution makes this blurring explicit. Sensitivity analysis — changing layer properties and observing how the synthetic changes — directly exploits this relationship to determine what geology is detectable."
```

## Explainer

From your study of seismic waves and elastic wave propagation, you know that when a seismic wave encounters a boundary between layers with different acoustic properties, some energy reflects back. The strength of each reflection depends on the contrast in **acoustic impedance** (the product of velocity and density, Z = ρV) across the boundary. A synthetic seismogram is a computed prediction of what a seismic recording should look like for a given earth model — it is the forward-modeling counterpart to the interpretive task of inferring geology from recorded data.

The construction starts with a **1D earth model**: a stack of horizontal layers, each defined by its P-wave velocity, density, and thickness (often derived from well logs). From these properties, you calculate the **reflection coefficient** at each interface: R = (Z₂ − Z₁)/(Z₂ + Z₁), where Z₁ and Z₂ are the impedances above and below the boundary. A large impedance contrast (like sediment over basement rock) produces a strong reflection; a subtle contrast (like two similar sandstones) produces a weak one. The sequence of reflection coefficients plotted against two-way travel time forms the **reflectivity series** — a spike train showing where reflections originate and how strong they are.

The reflectivity series alone is not what a seismogram looks like, because the seismic source does not produce an infinitely sharp spike. It produces a **wavelet** — a short oscillating pulse with a characteristic frequency content and shape (commonly modeled as a Ricker wavelet or extracted statistically from real data). The synthetic seismogram is produced by **convolving** the reflectivity series with the source wavelet: each spike in the reflectivity series is replaced by a scaled copy of the wavelet, and all the copies are summed. The result is a wiggly trace that mimics what a real seismometer would record, with individual reflections blurred together wherever layers are thinner than about one-quarter of the dominant wavelength.

Synthetic seismograms serve two critical purposes. First, they provide a **well tie**: by generating a synthetic from well-log data and comparing it to the actual seismic trace at the well location, interpreters verify that they are correctly identifying which wiggles correspond to which geological boundaries. If the synthetic matches the recorded data, the velocity-depth model is validated and the interpreter can confidently extend geological interpretations away from the well into areas with seismic data but no wells. Second, synthetics enable **sensitivity analysis**: by varying layer thickness, velocity, or fluid content in the model and observing how the synthetic trace changes, geophysicists learn which geological changes are seismically detectable and which are below resolution — guiding both survey design and interpretation confidence.
