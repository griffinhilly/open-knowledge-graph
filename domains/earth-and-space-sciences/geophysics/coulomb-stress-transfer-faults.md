---
id: coulomb-stress-transfer-faults
title: Coulomb Stress Transfer and Fault Interaction
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: stress-tensor-inversion-from-earthquakes
  type: hard
tags:
- seismic
- stress-transfer
- fault-interaction
stage: advanced
status: draft
---

# Coulomb Stress Transfer and Fault Interaction

## Core Idea
Large earthquakes change the stress field in surrounding rock, bringing some faults closer to failure (stress loading) and others further from failure (unloading). Coulomb stress transfer models use earthquake source parameters and friction coefficients to predict how mainshocks affect aftershock locations and whether nearby faults may be triggered to rupture.

## Questions

```yaml
- question: "A magnitude 7.0 earthquake occurs on a right-lateral strike-slip fault. Where would you expect the highest concentration of aftershocks relative to the mainshock rupture zone?"
  type: multiple-choice
  options:
    - "Directly on the ruptured fault segment, because that is where stress was highest before the mainshock"
    - "In the stress shadow adjacent to the ruptured fault, where the mainshock released the most accumulated stress"
    - "In lobes extending off the ends of the ruptured fault and obliquely away from it, where Coulomb stress increased"
    - "Randomly distributed around the epicenter within a radius proportional to magnitude"
  answer: 2
  explanation: "Coulomb stress transfer produces a specific spatial pattern: lobes of increased stress extending off the ends of the ruptured fault (roughly in the direction of slip) and at angles of ~30–45° from the fault plane. Aftershocks cluster in these positive ΔCFS regions — studies show 85% or more of aftershocks fall where the mainshock increased Coulomb stress. The ruptured fault segment itself is in a stress shadow immediately after the earthquake (the shear stress there was released by the rupture). The distribution is far from random; it reflects the mechanical stress redistribution predicted by elastic dislocation theory."

- question: "The Coulomb failure stress change (ΔCFS) formula includes both a shear stress term and a normal stress term (ΔCFS = Δτ + μ′Δσₙ). Why does a change in normal stress on a receiver fault affect how close it is to failure?"
  type: multiple-choice
  options:
    - "Normal stress increases the fault's temperature, causing thermal weakening that promotes failure"
    - "Normal stress perpendicular to the fault clamps it shut (resists slip) or unclamps it (promotes slip) — reducing normal stress allows the fault to slide at lower shear stress"
    - "Normal stress only matters for thrust faults; for strike-slip faults only shear stress matters"
    - "Normal stress affects the speed of rupture but not whether the fault will fail"
  answer: 1
  explanation: "The Coulomb failure criterion (like frictional sliding) involves both shear stress (driving slip) and normal stress (clamping the fault faces together). Friction resists slip with a force proportional to the normal force clamping the surfaces. Reducing normal stress (unclamping the fault) lowers the friction that must be overcome, so the fault can fail at lower shear stress — it has been brought closer to failure. Increasing normal stress does the opposite: it clamps the fault more tightly and moves it away from failure. This is why the complete ΔCFS formula must include both terms; an earthquake can trigger a nearby fault by reducing normal stress even without adding shear stress."

- question: "A large earthquake can place nearby faults in a stress shadow, reducing the probability of earthquakes on those faults for years or even decades."
  type: true-false
  answer: true
  explanation: "Stress shadows are real and seismically detectable. When a mainshock redistributes stress, some fault segments experience decreased Coulomb stress — they are clamped more tightly or have reduced shear stress in the slip direction. Seismicity rates in stress shadows typically decline below the long-term background rate for years after the mainshock. The 1906 San Francisco earthquake placed much of the surrounding fault network in shadow, and seismicity in shadow zones remained suppressed for decades. This has practical implications for hazard assessment: a major earthquake both increases risk on some faults and decreases it on others, not simply raises risk everywhere."

- question: "After a large earthquake, all stress in the surrounding region is released equally — the ruptured fault and nearby faults are all equally stable because the mainshock reduced stress throughout the area."
  type: true-false
  answer: false
  explanation: "An earthquake does not release stress uniformly — it redistributes it. While the ruptured segment itself experiences a large reduction in shear stress, adjacent regions and faults receive stress transferred from the earthquake. The characteristic Coulomb stress pattern has lobes of increased stress extending off the fault ends and diagonally, while stress shadows flank the sides of the rupture zone. This asymmetric redistribution is why aftershocks cluster in specific spatial patterns rather than being distributed evenly around the mainshock. Assuming uniform stress release would predict random aftershock locations, which contradicts the well-documented clustering in positive ΔCFS lobes."

- question: "Why do aftershock locations cluster in regions of positive Coulomb stress change rather than being randomly distributed around the mainshock?"
  type: short-answer
  answer: "A mainshock redistributes stress by elastic deformation of the surrounding crust — relaxing stress on the ruptured fault but loading adjacent regions. The Coulomb stress change (ΔCFS = Δτ + μ′Δσₙ) quantifies how much closer to failure each point in the surrounding rock has moved. Faults or fault segments where ΔCFS > 0 have been brought closer to their failure threshold; those in regions where pre-existing stress was already near critical will rupture as aftershocks. The spatial pattern of positive ΔCFS lobes reflects the geometry of the mainshock's slip — specifically the direction of stress load transfer from the ends of a strike-slip fault. That ~85% of aftershocks fall in positive ΔCFS regions is strong evidence that stress redistribution, not random chance, governs their locations."
  explanation: "This understanding has direct practical applications: after a large earthquake, Coulomb stress calculations can be performed within hours using source parameters from the focal mechanism, allowing seismologists to identify which fault segments face elevated risk. These rapid assessments inform emergency response and public communication about ongoing hazard. The framework also applies over longer timescales, explaining how sequences of large earthquakes can progressively load unruptured fault segments in a region."
```

## Explainer

From your work with focal mechanisms and stress tensors, you know that the stress state on a fault determines whether it is close to failure. The key insight of **Coulomb stress transfer** is that an earthquake does not simply release stress — it redistributes it. When a fault ruptures, it relaxes shear stress along the ruptured segment, but in doing so it loads adjacent regions of rock with additional stress. Some nearby faults are pushed closer to their breaking point, while others are pushed further from failure. This redistribution follows predictable spatial patterns that can be calculated from the source parameters of the earthquake.

The quantity at the heart of this analysis is the **Coulomb failure stress change** (ΔCFS). It combines two contributions: the change in shear stress resolved onto the plane of a nearby receiver fault (which promotes or resists slip) and the change in normal stress on that fault (which clamps it shut or unclamps it). The formula is ΔCFS = Δτ + μ′Δσₙ, where Δτ is the shear stress change in the slip direction, Δσₙ is the normal stress change (positive for unclamping), and μ′ is the effective coefficient of friction. When ΔCFS is positive on a receiver fault, that fault has been brought closer to failure; when negative, it has been moved further from failure — placed in a **stress shadow**.

The power of this framework becomes clear when you map ΔCFS across a region after a large earthquake. The resulting pattern typically shows lobes of increased Coulomb stress extending off the ends of the ruptured fault and along directions roughly 30–45° from the fault plane, while zones of decreased stress (shadows) lie adjacent to the fault on either side of the slip zone. Aftershock locations overwhelmingly cluster in the positive ΔCFS lobes — often 85% or more of aftershocks fall in regions where the mainshock increased Coulomb stress. This is far better than random chance would predict and provides strong validation that stress transfer governs aftershock triggering.

Beyond aftershocks, Coulomb stress transfer explains fault interaction over longer timescales. A sequence of large earthquakes on a fault system can progressively load segments that have not yet ruptured, creating a stress concentration that makes the next event more likely in a specific location. The 1999 İzmit and Düzce earthquakes on the North Anatolian Fault in Turkey illustrate this: each successive rupture loaded the next segment to the east, and stress transfer calculations correctly identified the zones of heightened hazard before subsequent events occurred. Conversely, stress shadows can delay earthquakes on nearby faults for decades. Coulomb modeling thus provides a physically grounded tool — rooted in the stress tensor analysis you already understand — for assessing where earthquake hazard has increased or decreased following a major event.
