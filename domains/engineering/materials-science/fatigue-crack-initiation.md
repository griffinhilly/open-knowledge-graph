---
id: fatigue-crack-initiation
title: Fatigue Crack Initiation Mechanisms
domain: engineering
course: materials-science
prerequisites:
- id: stress-concentration-and-singularities
  type: hard
- id: plastic-deformation-mechanisms
  type: soft
builds-toward:
- fatigue-crack-propagation-and-growth
- fatigue-in-materials
tags:
- fatigue
- crack-initiation
- slip-bands
- surface-damage
stage: advanced
status: draft
---

# Fatigue Crack Initiation Mechanisms

## Core Idea
Fatigue cracks initiate at stress concentrations through cyclic slip creating surface roughening and intrusions/extrusions. Persistent slip bands form from cyclic plastic deformation and act as crack nucleation sites. Initiation typically occupies a significant fraction of fatigue life and depends strongly on surface finish, stress concentration, and microstructural features.

## How It's Best Learned
Examine micrographs of fatigue-initiated surfaces to observe slip-band patterns and surface roughness. Conduct fatigue tests on notched versus smooth specimens to quantify stress concentration effects on initiation life.

## Common Misconceptions
Fatigue is not purely stress-controlled. Fatigue initiation depends on cyclic plastic strain amplitude, not merely stress amplitude, and is controlled by low-cycle fatigue mechanics below 104 cycles.

## Questions

```yaml
- question: "A smooth steel shaft operating at stresses well below its yield strength fractures after 10⁸ cycles. A fractographic examination would most likely reveal that the crack initiated at:"
  type: multiple-choice
  options:
    - "A grain boundary triple junction deep within the bulk material"
    - "A surface stress concentration or persistent slip band intersection with the free surface"
    - "A pre-existing void at the geometric center of the cross-section"
    - "A large carbide precipitate evenly distributed throughout the grain interior"
  answer: 1
  explanation: "Fatigue crack initiation is overwhelmingly a surface phenomenon. Persistent slip bands localize cyclic plastic deformation and create intrusions/extrusions where they intersect the free surface. Even in 'smooth' specimens, microscale surface roughness or slip-band activity at the surface — not bulk defects — nucleates the crack."

- question: "An engineer proposes to extend the fatigue life of a steel crankshaft by shot peening the surface before service. The mechanism by which this improves fatigue performance is:"
  type: multiple-choice
  options:
    - "Shot peening work-hardens the surface, raising yield strength so no plastic deformation can occur during cycling"
    - "Shot peening introduces compressive residual stresses that oppose the opening of fatigue intrusions at the surface"
    - "Shot peening removes surface roughness by plastic deformation, eliminating stress concentrations"
    - "Shot peening creates a fine-grained surface layer with no preferred slip systems, preventing persistent slip band formation"
  answer: 1
  explanation: "Shot peening induces compressive residual stresses by plastically deforming the surface layer. These residual stresses must be overcome before cyclic tension can open an intrusion into a crack — effectively raising the applied stress needed to initiate. While surface roughening occurs, the dominant benefit is the compressive stress field, not surface finish change."

- question: "Polishing the surface of a fatigue test specimen — reducing surface roughness to nearly zero — can significantly increase the number of cycles to failure."
  type: true-false
  answer: true
  explanation: "Since fatigue crack initiation is a surface phenomenon, surface finish has a strong effect on initiation life. A polished surface eliminates microscale stress concentrations where persistent slip bands would preferentially intersect. Industrial fatigue data consistently shows that surface roughness reduces fatigue limit, sometimes by 30–50% relative to polished specimens."

- question: "Fatigue crack initiation is controlled primarily by stress amplitude alone, so a component that survives 10⁷ cycles elastically will never initiate a fatigue crack regardless of how many additional cycles are applied."
  type: true-false
  answer: false
  explanation: "Even when bulk stresses are well below yield, cyclic plastic strain localizes at stress concentrations and within persistent slip bands. Initiation is driven by cyclic plastic strain amplitude, not merely stress amplitude. Below the fatigue limit (for steels), crack initiation is suppressed — but this is because the stress is insufficient to sustain PSB activity, not because there is zero plastic deformation absolutely."

- question: "Why do persistent slip band intersections with the free surface act as preferential crack nucleation sites, even in a specimen with no pre-existing notches or geometric stress concentrations?"
  type: short-answer
  answer: "Repeated shear along the PSB creates surface intrusions — sharp re-entrant grooves that concentrate stress on subsequent cycles, effectively acting as crack embryos"
  explanation: "PSBs undergo back-and-forth shear displacement on each cycle. This pumps material above the surface (extrusions) and pulls re-entrant grooves below (intrusions). An intrusion is geometrically a sharp notch at the surface — a stress concentrator created by the cyclic deformation itself. Once an intrusion reaches roughly one grain diameter in depth, it transitions to Stage I crack growth and the propagation phase begins."
```

## Explainer

Fatigue failure is insidious because it occurs under stresses well below the static yield strength — stresses that, applied once, would cause no visible damage at all. The key is *repetition*. Each loading cycle causes a tiny increment of irreversible plastic deformation, even when the globally applied stress is elastic. Over thousands or millions of cycles, that accumulated microscale damage nucleates a crack, which then grows until the remaining section can no longer carry the load and fracture occurs suddenly. Understanding initiation — the first stage of this process — is critical because it typically consumes the majority of a component's fatigue life.

From your study of stress concentrations, you know that geometric features like notches, holes, and fillets amplify the local stress far above the nominal applied value. The same geometry that concentrates stress also concentrates cyclic plastic strain. Even when the bulk of the material deforms elastically, the highly stressed region at a stress concentration may experience small-scale plastic flow on every cycle. This cyclic plasticity is not randomly distributed — it localizes onto specific crystallographic planes called **persistent slip bands** (PSBs). These bands form because certain slip systems reach a self-organized steady state of repeated, concentrated back-and-forth shear. The material in the PSB deforms far more than the surrounding matrix, and the band "persists" even after annealing attempts, which is why they're called persistent.

The surface where PSBs intersect the free face is where initiation actually happens. Repeated slip along the band pushes material out of the surface on one stroke and pulls adjacent material in on the next. Over many cycles, this creates **extrusions** (ridges above the surface) and **intrusions** (grooves below). An intrusion is geometrically equivalent to a crack embryo: it is a sharp re-entrant notch at the surface that concentrates stress on subsequent cycles. Once the intrusion reaches a depth of roughly a grain diameter, it transitions from Stage I crack growth (shearing along the slip band, ~45° to the stress axis) to Stage II growth (tensile crack opening, perpendicular to the maximum principal stress), and the crack propagation phase begins.

Practical design implications follow directly from this mechanism. Because initiation is a surface phenomenon, **surface finish** matters enormously — a polished surface has dramatically longer initiation life than a rough machined one. **Compressive residual stresses** at the surface (from shot peening, case hardening, or roller burnishing) oppose the opening of intrusions and suppress initiation. **Stress concentration factors** directly reduce initiation life, which is why smooth transitions and generous radii in fillet geometry are specified even when static stress calculations show large margins. The distinction in your misconceptions section is worth internalizing: below roughly 10⁴ cycles, stresses are high enough that macroscopic yielding occurs and strain-based design methods apply; above that, the high-cycle regime is governed by stress amplitude, and the initiation mechanism described here dominates the total life.
