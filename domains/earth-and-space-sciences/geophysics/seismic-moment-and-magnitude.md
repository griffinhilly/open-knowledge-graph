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

## Questions

```yaml
- question: "The 1960 Chilean earthquake measured Ms 8.5 on the surface-wave scale but Mw 9.5 on the moment magnitude scale. What is the best physical explanation for this ~30× energy discrepancy?"
  type: multiple-choice
  options:
    - "The two scales use different units, so a direct comparison requires a conversion factor"
    - "The surface-wave magnitude saturates for very large earthquakes — the specific wave amplitudes it measures stop growing even as the fault keeps rupturing larger areas"
    - "Ms 8.5 was a preliminary estimate that was corrected to Mw 9.5 as better seismograph data became available"
    - "The Chilean earthquake had unusually large slip on a small fault, which Mw captures but Ms does not"
  answer: 1
  explanation: "Older scales measure amplitudes of specific wave types at specific frequencies. For giant earthquakes, those waves saturate — the seismograph records the maximum amplitude the wave type can carry at that frequency, even as the fault continues to grow. Mw is derived from seismic moment M₀ = μ × A × D, a direct physical measure with no intrinsic upper bound. As fault area and slip grow, M₀ grows proportionally. The factor of ~30 in energy between Ms 8.5 and Mw 9.5 illustrates how severely saturated scales underestimate the largest earthquakes."

- question: "Two earthquakes have identical seismic moment M₀. Earthquake A ruptured a large fault area with small average slip. Earthquake B ruptured a small fault area with large average slip. Which released more energy?"
  type: multiple-choice
  options:
    - "Earthquake A — larger fault area means more rock displaced and more total energy"
    - "Earthquake B — larger slip means stronger ground shaking and more seismic energy"
    - "They released equal energy — seismic moment is the product μ × A × D, and identical M₀ means identical total elastic energy released"
    - "Cannot be determined without knowing the rock rigidity μ at each fault"
  answer: 2
  explanation: "Seismic moment M₀ = μ × A × D is the single quantity that physically quantifies earthquake size. Identical M₀ (with similar μ) means the same total elastic energy released, regardless of how area and slip are distributed. Both earthquakes have the same Mw. Their different fault geometries may produce different ground-shaking patterns due to directivity, but the fundamental energy measure is identical."

- question: "Moment magnitude Mw was intentionally calibrated to agree with Richter's original local magnitude scale in the magnitude 3–7 range."
  type: true-false
  answer: true
  explanation: "This calibration was deliberate so that historical earthquake catalogs remain comparable. In the range where older scales are reliable (roughly M 3–7), Mw gives equivalent numerical values. Outside this range — especially above M 8 — Mw diverges from saturated scales, correctly capturing the far greater energy release that saturated scales miss."

- question: "A larger seismic moment M₀ necessarily implies a larger fault rupture area, since fault area is the dominant physical factor in the equation M₀ = μ × A × D."
  type: true-false
  answer: false
  explanation: "All three factors — rigidity μ, fault area A, and average slip D — contribute multiplicatively. A large slip on a small fault can produce the same M₀ as a small slip on a large fault (with equal μ). For example: A = 10 km², D = 10 m gives the same M₀ as A = 100 km², D = 1 m. Neither area nor slip alone determines earthquake size; only their product (weighted by rigidity) does."

- question: "Why does moment magnitude Mw not saturate for very large earthquakes, whereas older scales like body-wave magnitude mb and surface-wave magnitude Ms do?"
  type: short-answer
  answer: "Older scales measure the amplitude of specific seismic wave types at specific frequency bands. For giant earthquakes, the fault keeps growing in area and releasing energy primarily at very long periods — outside the measurement band of those scales. The wave amplitudes at the measured frequencies stop growing, 'clipping' the scale. Mw is derived from seismic moment M₀ = μ × A × D, which is a direct physical measure of rupture size with no frequency restriction. As fault area and average slip grow, M₀ grows proportionally, and so does Mw, with no upper bound."
  explanation: "The saturation problem is not an instrument deficiency but a fundamental consequence of using narrow-band wave amplitudes as size proxies. Moment magnitude avoids this by being grounded in source physics — the actual forces and displacements on the fault — rather than filtered seismic wave measurements."
```

## Explainer

From focal mechanisms, you understand that earthquakes occur when stress exceeds the frictional strength of a fault, producing slip that radiates seismic waves. Seismic moment and magnitude scales give you the tools to quantify *how big* that rupture was — and they do so in a way that is grounded in the physics of the fault itself rather than in the amplitude of a particular seismogram.

The **seismic moment** M₀ = μ × A × D combines three physical quantities: the **rigidity** (shear modulus) μ of the rock surrounding the fault, the **fault area** A that ruptured, and the **average slip** D across that area. Each factor contributes independently to earthquake size. A small fault with large displacement and a large fault with small displacement can have the same moment — it is the product that matters. The units of seismic moment are Newton-meters (the same as torque), and values span an enormous range: a barely-felt magnitude-2 event might have M₀ ≈ 10⁹ N·m, while the 2011 Tōhoku earthquake reached about 5 × 10²² N·m — a factor of 10¹³ larger.

Because seismic moment spans so many orders of magnitude, it is convenient to compress it onto a logarithmic scale. The **moment magnitude** formula Mw = (2/3)log₁₀(M₀) − 10.7 does exactly this, and it was deliberately calibrated to agree with Richter's original local magnitude scale in the range where both are valid (roughly magnitude 3–7). The critical advantage of Mw is that it **does not saturate**. Older scales measured the amplitude of specific seismic wave types at specific frequencies, and for very large earthquakes, those particular waves stop getting bigger even as the fault keeps growing — the scale "clips" like an overloaded microphone. The body-wave magnitude (mb) saturates around 6.5, and the surface-wave magnitude (Ms) around 8.2. The 1960 Chilean earthquake, the largest ever recorded, was Ms 8.5 on the surface-wave scale but Mw 9.5 when measured by seismic moment — a factor of 30 more energy than the saturated scale suggests.

The **moment tensor** generalizes seismic moment into a mathematical object that captures not just the size but the geometry of the source. It is a 3×3 symmetric matrix (six independent components) whose eigenvectors define the orientation of the fault plane and slip direction, and whose eigenvalues define the magnitude and type of deformation (double-couple for simple shear faulting, plus possible non-double-couple components for more complex sources like volcanic explosions or mine collapses). Modern seismology routinely computes moment tensors for significant earthquakes within minutes using long-period waveform data from global seismic networks, providing immediate information on fault geometry, stress orientation, and earthquake size that feeds into tsunami warnings, aftershock forecasts, and tectonic studies.
