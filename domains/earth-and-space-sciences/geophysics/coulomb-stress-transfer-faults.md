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

## Explainer

From your work with focal mechanisms and stress tensors, you know that the stress state on a fault determines whether it is close to failure. The key insight of **Coulomb stress transfer** is that an earthquake does not simply release stress — it redistributes it. When a fault ruptures, it relaxes shear stress along the ruptured segment, but in doing so it loads adjacent regions of rock with additional stress. Some nearby faults are pushed closer to their breaking point, while others are pushed further from failure. This redistribution follows predictable spatial patterns that can be calculated from the source parameters of the earthquake.

The quantity at the heart of this analysis is the **Coulomb failure stress change** (ΔCFS). It combines two contributions: the change in shear stress resolved onto the plane of a nearby receiver fault (which promotes or resists slip) and the change in normal stress on that fault (which clamps it shut or unclamps it). The formula is ΔCFS = Δτ + μ′Δσₙ, where Δτ is the shear stress change in the slip direction, Δσₙ is the normal stress change (positive for unclamping), and μ′ is the effective coefficient of friction. When ΔCFS is positive on a receiver fault, that fault has been brought closer to failure; when negative, it has been moved further from failure — placed in a **stress shadow**.

The power of this framework becomes clear when you map ΔCFS across a region after a large earthquake. The resulting pattern typically shows lobes of increased Coulomb stress extending off the ends of the ruptured fault and along directions roughly 30–45° from the fault plane, while zones of decreased stress (shadows) lie adjacent to the fault on either side of the slip zone. Aftershock locations overwhelmingly cluster in the positive ΔCFS lobes — often 85% or more of aftershocks fall in regions where the mainshock increased Coulomb stress. This is far better than random chance would predict and provides strong validation that stress transfer governs aftershock triggering.

Beyond aftershocks, Coulomb stress transfer explains fault interaction over longer timescales. A sequence of large earthquakes on a fault system can progressively load segments that have not yet ruptured, creating a stress concentration that makes the next event more likely in a specific location. The 1999 İzmit and Düzce earthquakes on the North Anatolian Fault in Turkey illustrate this: each successive rupture loaded the next segment to the east, and stress transfer calculations correctly identified the zones of heightened hazard before subsequent events occurred. Conversely, stress shadows can delay earthquakes on nearby faults for decades. Coulomb modeling thus provides a physically grounded tool — rooted in the stress tensor analysis you already understand — for assessing where earthquake hazard has increased or decreased following a major event.
