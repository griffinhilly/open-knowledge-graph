---
id: reflection-seismic-survey-design
title: Reflection Seismic Survey Design and Acquisition
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-ray-tracing-methods
  type: hard
- id: potential-field-methods-gravity-magnetics
  type: soft
builds-toward:
- seismic-data-processing-and-filtering
- seismic-migration-techniques
tags:
- seismic
- survey-design
- reflection
- acquisition
stage: advanced
status: draft
---

# Reflection Seismic Survey Design and Acquisition

## Core Idea
Reflection seismic surveys use arrays of sources and receivers to record reflections from subsurface interfaces. Survey parameters such as source-receiver distance, receiver spacing, and line direction must be chosen based on target depth, expected reflection geometry, and spatial resolution requirements. Common-midpoint (CMP) gathers organize the data to enhance signals and suppress noise.

## Questions

```yaml
- question: "Why do seismic surveys deliberately collect many traces with different source-receiver offsets that share the same common midpoint (CMP)?"
  type: multiple-choice
  options:
    - "To simultaneously record reflections from different depths, each best illuminated at a specific offset"
    - "So that after NMO correction, the traces can be stacked to reinforce coherent reflections and cancel random noise"
    - "Because reflections only occur when the source and receiver are equidistant from the reflector"
    - "To measure surface-wave velocities, which are needed to correct for near-surface irregularities"
  answer: 1
  explanation: "The CMP gather organizes traces that all reflect from approximately the same subsurface point but arrive via different ray paths (different offsets). After applying the NMO correction to remove the offset-dependent travel-time increase, all traces in the gather should show the reflection at the same time. Stacking (summing) these aligned traces reinforces the coherent signal while random noise tends to cancel, improving the signal-to-noise ratio by roughly the square root of the fold."

- question: "A geophysicist is designing a survey to image a target at 5 km depth. Compared to a survey targeting a 500 m depth reflector, the deep survey requires:"
  type: multiple-choice
  options:
    - "Shorter maximum offset and higher-frequency sources, to preserve resolution at depth"
    - "Longer maximum offset and more powerful sources, to illuminate deep reflectors and provide velocity discrimination"
    - "Closer receiver spacing only, because deeper targets produce wider Fresnel zones that are easier to sample"
    - "Fewer source activations because seismic energy naturally penetrates deeper with larger shot spacing"
  answer: 1
  explanation: "Deeper targets require longer maximum offsets for two reasons: (1) only long-offset rays reach deep reflectors at wide enough angles to provide useful NMO velocity discrimination needed for accurate stacking, and (2) the reflection hyperbola for a deep target is flatter — close-offset traces look nearly identical in travel time, giving little velocity information. More powerful sources are needed because energy attenuates with depth. By contrast, shallow surveys can use short offsets and high-frequency sources for fine spatial resolution."

- question: "Increasing fold (the number of traces contributing to each CMP stack) always improves seismic data quality, so surveys should maximize fold regardless of cost."
  type: true-false
  answer: false
  explanation: "Higher fold does improve signal-to-noise ratio (SNR improves roughly as √fold), but the returns diminish — going from fold 10 to fold 40 roughly doubles SNR, while going from fold 40 to fold 160 only doubles it again. Meanwhile, cost and field logistics scale roughly linearly with fold. Survey design involves balancing the required SNR against budget, surface access, and time constraints. In many surveys, fold in the range of 60–120 is chosen as a practical optimum, not the theoretical maximum."

- question: "Spatial aliasing in a seismic survey occurs when the receiver spacing is too coarse to adequately sample the apparent wavelength of steeply dipping reflections along the surface."
  type: true-false
  answer: true
  explanation: "The Nyquist sampling criterion requires at least two samples per wavelength. For a steeply dipping reflector, the apparent wavelength at the surface (the horizontal distance between successive wavefront peaks) is shorter than for a flat reflector at the same frequency. If receiver spacing exceeds half this apparent wavelength, the data are spatially aliased — dipping events appear at the wrong apparent dip or fold back into the wrong direction. This is why surveys targeting steep structures (faults, salt flanks) require tighter receiver spacing."

- question: "Explain the purpose of the normal moveout (NMO) correction in CMP processing. Why is it necessary before stacking, and what key parameter must be estimated to apply it correctly?"
  type: short-answer
  answer: "In a CMP gather, the reflection from a flat horizontal layer arrives later at longer offsets because the ray path is longer. This offset-dependent delay follows a hyperbolic relationship: t²(x) = t₀² + x²/v², where t₀ is the zero-offset two-way travel time and v is the stacking velocity. The NMO correction flattens this hyperbola by subtracting the extra travel time at each offset, so the reflection aligns at the same time across all traces. Without this correction, stacking would smear rather than reinforce the reflection. The key parameter is the NMO velocity (or stacking velocity), which must be estimated — typically by testing a range of velocities and selecting the one that produces the flattest, best-aligned gather (velocity semblance analysis). This velocity also provides information about subsurface interval velocities, which can be used for depth conversion."
```

## Explainer

From seismic ray tracing, you understand how seismic waves travel through layered media, reflecting and refracting at interfaces where acoustic impedance changes. A **reflection seismic survey** applies this physics systematically: you generate seismic waves at the surface, record the echoes that bounce off subsurface layers, and use the timing and amplitude of those reflections to build an image of the geology below. The challenge is designing the survey so that the recorded data actually contain the information you need — and this is where survey design becomes critical.

The fundamental geometry involves a **source** (an explosive charge, vibrator truck, or air gun) and an array of **receivers** (geophones on land, hydrophones at sea) laid out along a line or across a grid. Each source activation produces a **shot gather** — a collection of traces recorded at different offsets (source-receiver distances). Short offsets record near-vertical reflections and are most sensitive to shallow, flat-lying layers. Long offsets capture wide-angle reflections that carry information about velocities and deeper structures but are also contaminated by surface waves and refractions. The maximum offset, receiver spacing, and source interval must be chosen to match the target: deeper targets require longer offsets and more powerful sources, while resolving thin layers or small faults demands closer receiver spacing to capture high spatial frequencies.

The key organizational concept is the **common-midpoint (CMP) gather**. Multiple source-receiver pairs share the same midpoint on the surface, meaning their reflections sample approximately the same subsurface point but at different angles. Stacking (summing) these traces after correcting for the extra travel time at longer offsets — the **normal moveout (NMO) correction** — reinforces coherent reflections while canceling random noise, dramatically improving the signal-to-noise ratio. The number of traces that contribute to each CMP is the **fold**; higher fold means more noise suppression but requires more sources and receivers, increasing cost. A typical exploration survey might aim for 60- to 120-fold coverage.

Survey design also involves practical trade-offs between resolution, coverage, cost, and logistics. **Spatial aliasing** occurs when the receiver spacing is too coarse to sample steeply dipping events — the Nyquist criterion requires at least two samples per wavelength of the steepest event. **3D surveys** extend coverage from lines to grids, using multiple parallel receiver lines and source lines to capture reflections from all azimuths, essential for imaging complex structures like salt bodies or fault networks. The design process typically begins with synthetic modeling: ray tracing or wave-equation simulations through an expected geological model predict what the recorded data should look like, allowing the geophysicist to optimize parameters before deploying expensive field equipment.
