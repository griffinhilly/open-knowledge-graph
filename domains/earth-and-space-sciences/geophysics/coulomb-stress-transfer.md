---
id: coulomb-stress-transfer
title: Coulomb Stress Transfer and Earthquake Triggering
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: earthquakes-and-seismology
  type: hard
tags:
- coulomb-stress
- triggering
- earthquakes
stage: advanced
status: draft
---

# Coulomb Stress Transfer and Earthquake Triggering

## Core Idea
Earthquake ruptures change regional stress, increasing or decreasing Coulomb failure stress on nearby faults. Stress transfer can trigger aftershocks and migrate seismicity; this mechanism explains earthquake clustering and fault-to-fault interactions.

## Explainer

From your study of focal mechanisms and stress tensors, you know that faults slip when the shear stress resolved on the fault plane exceeds the frictional resistance holding it locked. What Coulomb stress transfer adds is the recognition that when one fault ruptures, it does not simply release stress — it *redistributes* it, changing the stress state on every nearby fault. Some faults are pushed closer to failure; others are pushed farther from it. This is the mechanism behind the observation that earthquakes are not random in space and time but tend to cluster and cascade.

The key quantity is the **Coulomb failure stress change** (ΔCFS). It combines two effects: the change in shear stress resolved in the slip direction on a receiving fault, and the change in normal stress clamping the fault shut. The formula is straightforward: ΔCFS = Δτ + μ′Δσₙ, where Δτ is the shear stress change (positive encourages slip), Δσₙ is the normal stress change (positive means unclamping), and μ′ is the effective friction coefficient. A positive ΔCFS means the receiving fault has been brought closer to failure. Remarkably, stress changes as small as 0.1 bar (about one-tenth of atmospheric pressure) have been shown to correlate with triggered seismicity — faults near failure need only a tiny nudge.

Think of it with a physical analogy. Imagine a bookshelf full of books leaning at various angles. If you suddenly pull one book out (the mainshock), the books on either side shift — some lean more precariously and may topple (triggered earthquakes in positive ΔCFS zones), while others settle into more stable positions (stress shadows where seismicity is suppressed). The pattern is not random: it depends on the geometry of the shelf and the orientation of each book, just as Coulomb stress transfer depends on the geometry of the source rupture and the orientation of each receiving fault.

The spatial pattern of ΔCFS creates characteristic **stress lobes**. For a simple strike-slip earthquake, positive lobes extend off the ends of the rupture and on the opposite side of the fault from the slip direction, while negative lobes (called **stress shadows**) form adjacent to the rupture on the near side. Aftershock locations consistently concentrate in positive ΔCFS lobes and are suppressed in stress shadows. This framework has been applied to explain sequential fault ruptures along plate boundaries — for example, the progressive westward migration of large earthquakes along the North Anatolian Fault in Turkey during the twentieth century, where each rupture loaded the next segment closer to failure.

Coulomb stress transfer also operates on longer timescales. After a major earthquake, viscoelastic relaxation in the lower crust and upper mantle continues to redistribute stress over years to decades, a process called **postseismic stress transfer**. This means that the hazard implications of a large earthquake extend well beyond its immediate aftershock sequence. Understanding these stress interactions is now central to seismic hazard assessment, because it shifts the question from "where are faults?" to "which faults have been brought closer to failure by recent earthquakes?"
