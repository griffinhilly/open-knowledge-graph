---
id: earthquake-stress-inversion
title: Stress Inversion and Focal Mechanism Analysis
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: moment-tensor-inversion
  type: hard
tags:
- earthquake
- stress
- inversion
- focal-mechanism
stage: expert
status: validated
---

# Stress Inversion and Focal Mechanism Analysis

## Core Idea
Focal mechanisms from earthquake catalogs can be inverted for the regional stress tensor. Bootstrap and other statistical methods test solution robustness, and results reveal principal stress directions and magnitudes controlling seismicity.

## Questions

```yaml
- question: "A seismologist obtains a precise focal mechanism for a single well-recorded earthquake. Can she determine the regional stress tensor from this alone?"
  type: multiple-choice
  options:
    - "Yes, because the focal mechanism uniquely specifies the stress field that caused slip on the fault"
    - "No, for two reasons: the focal mechanism has a fault-plane ambiguity (two planes fit equally), and even knowing the fault plane, infinitely many stress states could produce that observed slip direction"
    - "Yes, if the earthquake has a pure double-couple mechanism, the principal stress axes are directly readable from the compressional and dilatational quadrants"
    - "No, because focal mechanisms only constrain the P and T axes, which do not correspond to any physical stress axis"
  answer: 1
  explanation: "Stress inversion from a single focal mechanism is impossible for two compounding reasons. First, the focal mechanism has an inherent ambiguity: a double-couple source has two nodal planes, and seismology alone cannot identify which one actually slipped. Second, even knowing the fault plane, the Wallace-Bott hypothesis still allows infinitely many stress tensors to predict the same slip direction on that plane — there are six independent stress components but only two angles of slip. Stress inversion only becomes tractable when many focal mechanisms are combined, making the problem overdetermined."

- question: "What does the stress ratio R = (σ₂ − σ₃)/(σ₁ − σ₃) recovered by stress inversion describe?"
  type: multiple-choice
  options:
    - "The magnitude of the maximum compressive stress relative to lithostatic pressure"
    - "The shape of the stress ellipsoid — whether the intermediate stress σ₂ is closer to the maximum or minimum principal stress"
    - "The ratio of horizontal to vertical stress, which determines whether faulting is normal, reverse, or strike-slip"
    - "The fraction of differential stress released as seismic energy versus heat"
  answer: 1
  explanation: "The stress ratio R (0 ≤ R ≤ 1) describes the shape of the stress ellipsoid: where the intermediate stress σ₂ falls between σ₁ and σ₃. When R ≈ 0, σ₂ ≈ σ₃; when R ≈ 1, σ₂ ≈ σ₁. R is one of the four parameters stress inversion can recover (along with the three principal stress orientations). Crucially, stress inversion from focal mechanisms cannot recover absolute stress magnitudes — only orientations and relative magnitudes encoded in R. Focal mechanisms constrain slip directions, not force magnitudes, making absolute magnitudes inaccessible from this data type alone."

- question: "Stress inversion can recover the absolute magnitudes of the principal stresses (in units of MPa) from focal mechanism data."
  type: true-false
  answer: false
  explanation: "Focal mechanisms record the geometry of fault slip — the direction of slip — not the magnitude of forces involved. Under the Wallace-Bott hypothesis, slip direction is invariant under uniform scaling of all stress components: scaling all three principal stresses by the same factor does not change any predicted slip direction. Therefore, focal mechanisms constrain only stress *orientations* and the *relative* magnitudes encoded in the stress ratio R, not absolute values in Pascals. Absolute stress magnitudes require independent measurements such as borehole breakouts, hydraulic fracturing, or in-situ strain gauges."

- question: "The Wallace-Bott hypothesis is the foundational assumption of stress inversion: each earthquake's fault slipped in the direction of maximum resolved shear stress on that fault plane."
  type: true-false
  answer: true
  explanation: "This is the central assumption that makes stress inversion tractable. Under the Wallace-Bott hypothesis, the observed slip vector on each fault plane equals the predicted slip vector — the direction the tectonic stress would push a frictionless fault of that orientation. The inversion then minimizes the angular misfit between predicted and observed slip directions across many earthquakes. The assumption breaks down when faults have heterogeneous properties, when earthquake interactions significantly perturb local stress, or when the catalog mixes earthquakes from multiple stress regimes."

- question: "Why is bootstrap resampling used to assess stress inversion results, and what does a scattered bootstrap distribution indicate?"
  type: short-answer
  answer: "Bootstrap resampling tests solution robustness by repeatedly solving the inversion on different random subsets of the focal mechanism catalog and examining how much the recovered stress parameters vary. If the stress tensor is well-constrained — consistent information across all earthquakes — bootstrap solutions cluster tightly, confirming the result is not driven by a few unusual focal mechanisms. A scattered distribution means the solution is poorly constrained: data may be insufficient, contain large measurement errors, or mix earthquakes from regions with different stress states. In the latter case, systematic spatial patterns in the misfits guide subdivision into distinct stress zones."
  explanation: "Statistical testing is essential because focal mechanisms contain measurement uncertainties and the regional stress assumption is an idealization. Bootstrap resampling provides an honest uncertainty assessment for the stress tensor solution — determining whether results can reliably be used to interpret tectonic loading directions or Coulomb stress transfer calculations."
```

## Explainer

You already know that a focal mechanism describes the geometry of fault slip for a single earthquake — the orientation of the fault plane, the direction of slip, and the pattern of compressional and dilatational first motions. You also know that moment tensor inversion recovers the full seismic source tensor from waveform data. **Stress inversion** takes the next step: given a collection of focal mechanisms from many earthquakes in a region, what is the underlying stress field that produced all of them?

The key insight is that a single focal mechanism cannot uniquely determine the stress tensor. Each focal mechanism has an inherent ambiguity (the fault plane vs. the auxiliary plane), and even if you knew which plane slipped, infinitely many stress states could have produced that particular slip direction. But when you have dozens or hundreds of focal mechanisms from a region, the problem becomes overdetermined. The assumption is that all these earthquakes occurred under the same regional stress field, and that slip on each fault was in the direction of maximum resolved shear stress on that plane. This is called the **Wallace-Bott hypothesis** — faults slip in the direction that the tectonic stress pushes them, not in some arbitrary direction.

The inversion algorithm searches for the stress tensor (specifically, the orientations of the three **principal stresses** σ₁, σ₂, σ₃ and the **stress ratio** R = (σ₂ − σ₃)/(σ₁ − σ₃)) that best predicts the observed slip directions across all focal mechanisms. The stress ratio R captures the shape of the stress ellipsoid — whether the intermediate stress is closer to the maximum or the minimum. Methods like the **Michael (1984) linear inversion** solve this efficiently by linearizing the relationship between the stress tensor and predicted slip vectors, then minimizing the angular misfit between predicted and observed slip directions across the earthquake population.

Because real data contain measurement errors and the regional stress assumption may not hold perfectly, statistical testing is essential. **Bootstrap resampling** — repeatedly solving the inversion on random subsets of the focal mechanism catalog — reveals how stable the solution is. Tight clustering of bootstrap results means the stress tensor is well constrained; a scattered distribution warns that the data may be insufficient or that multiple stress regimes are mixed in the catalog. Practitioners also check whether systematic misfits correlate with spatial location, which can indicate that the region should be subdivided into zones with distinct stress states.

The results have direct tectonic significance. The orientation of σ₁ (maximum compressive stress) reveals the direction of tectonic loading — perpendicular to a subduction trench, parallel to a transform fault, or radial to a rift zone. Changes in stress orientation with depth or across fault boundaries illuminate how stress is partitioned in the lithosphere. Stress inversion results are also essential inputs for Coulomb stress transfer calculations, which model how one earthquake changes the stress state on neighboring faults and helps forecast where future seismicity is most likely.
