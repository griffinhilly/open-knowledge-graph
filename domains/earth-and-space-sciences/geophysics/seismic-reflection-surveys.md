---
id: seismic-reflection-surveys
title: Seismic Reflection Surveys and Common Midpoint Processing
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: hard
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-signal-processing
  type: soft
builds-toward:
- seismic-migration-techniques
- synthetic-seismogram-modeling
tags:
- seismic
- reflection
- survey
- cmp
- processing
stage: advanced
status: validated
---

# Seismic Reflection Surveys and Common Midpoint Processing

## Core Idea
Seismic reflection surveys use reflected waves to image subsurface structure. Common midpoint (CMP) processing groups traces by reflection point, allowing velocity estimation through normal moveout (NMO) analysis and coherent stacking to enhance signal.

## How It's Best Learned
Study real seismic datasets and process them step-by-step: sorting, NMO correction, velocity picking, and stacking. Compare stacked sections from different velocity models.

## Questions

```yaml
- question: "A seismic survey is designed with 60 traces per CMP gather. After NMO correction and stacking, how does the signal-to-noise ratio of the stacked trace compare to a single raw trace, and why?"
  type: multiple-choice
  options:
    - "60× better, because the 60 signals add together perfectly while all noise cancels"
    - "Approximately √60 ≈ 7.7× better, because coherent reflections add constructively while random noise partially cancels"
    - "Unchanged — stacking corrects for moveout but does not affect noise"
    - "Worse than a single trace, because summing traces introduces new noise from the NMO correction"
  answer: 1
  explanation: "When N traces are stacked, coherent signals (reflections) add linearly: N traces each with amplitude A produce a stacked amplitude of N·A. Random noise, however, is statistically independent between traces: when N independent noise samples with standard deviation σ are summed, the combined noise standard deviation grows as √N·σ (by the central limit theorem / random walk statistics). The SNR of the stack is therefore (N·A)/(√N·σ) = √N·(A/σ) — exactly √N times the single-trace SNR. Doubling the fold improves SNR by √2, not by 2. This is why high fold (more traces per CMP) is valuable but shows diminishing returns."

- question: "In a CMP gather, a geologist applies an NMO correction using a velocity that is too high. What will the corrected gather look like?"
  type: multiple-choice
  options:
    - "The reflection event will be perfectly flat — small velocity errors do not affect the NMO-corrected shape"
    - "The reflection will be over-corrected, bending downward at far offsets (a 'smile' or 'hockey stick' shape)"
    - "The reflection will still show residual upward curvature at far offsets, because the insufficient correction leaves part of the moveout unremoved"
    - "The reflection will split into two separate events at near and far offsets"
  answer: 2
  explanation: "Normal moveout creates a hyperbolic increase in travel time with offset. The NMO correction subtracts a time shift calculated from the assumed velocity and offset. If the velocity used is too high, the calculated moveout is too small — the correction is insufficient. The far-offset traces are not shifted up enough, so the event still curves upward at large offsets ('under-corrected' or 'frown' shape). Conversely, a velocity that is too low over-corrects, shifting far-offset traces too far up and creating a downward 'smile.' Velocity analysts search for the velocity that produces the flattest gather — this is velocity picking."

- question: "A CMP (common midpoint) gather groups seismic traces that all share the same midpoint between their source and receiver, so that each trace in the gather recorded a reflection from approximately the same subsurface point."
  type: true-false
  answer: true
  explanation: "This is the defining property of CMP processing. By sorting traces by their common reflection point rather than by source or receiver, geologists isolate multiple measurements of the same subsurface reflector. Different source-receiver pairs sample the same midpoint but with different offsets (source-to-receiver distances), giving the moveout information needed for velocity analysis, while all traces contain the same geological signal from that reflection point. This organization is the foundation of modern reflection seismology."

- question: "A stacked seismic section directly shows the depth of geological reflectors below the surface, so a reflection appearing at 2 seconds on the vertical axis corresponds to a reflector 2 kilometers deep."
  type: true-false
  answer: false
  explanation: "The vertical axis of a stacked section shows two-way travel time (TWT) — the time for a seismic wave to travel from the surface down to a reflector and back up. Depth requires multiplying TWT by velocity and dividing by two, but the velocity varies with depth and lithology. A 2-second TWT reflection could correspond to widely different depths depending on whether the overlying rocks are slow shales (~1.5 km/s) or fast carbonates (~6 km/s). Converting from time to depth requires the velocity model estimated during NMO analysis, often supplemented by well log data. Further geometric corrections (migration) are needed when reflectors are dipping."

- question: "Explain why stacking multiple NMO-corrected CMP traces improves the signal-to-noise ratio, and why the improvement scales as √N rather than N."
  type: short-answer
  answer: "After NMO correction, all traces in a CMP gather show the same reflection at approximately the same arrival time. Stacking (summing) these traces combines coherent signal constructively: N traces each with amplitude A produce a total signal of N·A. Random noise, by contrast, is incoherent — each trace has independent random fluctuations from sources like ground roll, wind, traffic, and electronic noise. When N independent random noise samples are summed, the noise amplitude grows as √N (not N), because the independent fluctuations partially cancel by random walk statistics. The signal-to-noise ratio is therefore (N·A)/(√N·σ) = √N·(A/σ), improving as √N. This is why seismic surveys are designed with high fold: more traces per CMP improve SNR, but with diminishing returns, so there is an economic tradeoff between acquisition cost and image quality."
  explanation: "The √N scaling is the same phenomenon as the standard error of the mean in statistics: averaging N independent measurements reduces uncertainty by √N. In seismology, 'stacking' is the geophysicist's word for this statistical averaging process."
```

## Explainer

From your study of seismic waves and elastic wave propagation, you know that when a wave encounters a boundary between materials with different elastic properties, part of its energy reflects back toward the surface. Seismic reflection surveys exploit this principle to create detailed images of subsurface structure — essentially an ultrasound scan of the Earth. A controlled energy source (an explosive charge, vibroseis truck, or air gun) generates seismic waves at the surface, and an array of receivers (geophones on land, hydrophones at sea) records the reflected arrivals from each subsurface interface.

The raw data from a reflection survey is a collection of **seismograms** — wiggly traces showing amplitude versus time for each source-receiver pair. The challenge is that a single reflected event from one subsurface point appears on many different traces, recorded at different offsets (source-to-receiver distances), each with a slightly different travel time because of the longer path. **Common midpoint (CMP) gathering** organizes the data by grouping all traces that share the same reflection point, regardless of which source-receiver pair produced them. This is the fundamental organizational step that makes modern reflection processing possible.

Within a CMP gather, traces from the same reflector arrive at different times because of the offset-dependent path length. This time difference is called **normal moveout (NMO)** — for a flat reflector, it follows a hyperbolic curve. By measuring the curvature of the hyperbola, you estimate the seismic velocity above the reflector: steeper curvature means slower velocity, flatter means faster. This process of **velocity analysis** is done interactively by testing different velocity values and seeing which one best flattens the hyperbola. Once the correct velocity is applied, the NMO correction shifts each trace so that all offsets show the same arrival time — as if every trace were recorded at zero offset directly above the reflection point.

After NMO correction, the traces in each CMP gather are **stacked** — simply summed together. This is where the power of redundancy pays off. Coherent reflections add constructively, while random noise (which differs from trace to trace) partially cancels out. The signal-to-noise ratio improves roughly as the square root of the number of traces stacked, which is why surveys are designed with high **fold** (many traces per CMP). The result of stacking all CMPs across a survey line is a **stacked section** — an image that approximates a geological cross-section, with the horizontal axis showing surface position and the vertical axis showing two-way travel time. Converting from time to depth requires the velocity model estimated during NMO analysis, and further processing steps like migration correct for the geometric distortions that arise when reflectors are dipping or structures are complex.
