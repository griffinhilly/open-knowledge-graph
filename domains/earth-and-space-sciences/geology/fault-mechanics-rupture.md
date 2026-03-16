---
id: fault-mechanics-rupture
title: 'Fault Mechanics: Friction and Earthquake Rupture'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: brittle-ductile-transition
  type: hard
- id: earthquakes-and-seismology
  type: soft
builds-toward:
- seismic-hazard-assessment
tags:
- faults
- rupture
- friction
- Coulomb
- stress
stage: abstract-reasoning
status: draft
---

# Fault Mechanics: Friction and Earthquake Rupture

## Core Idea
Faults slip when shear stress exceeds the frictional strength (normal stress × friction coefficient). Rupture propagates when stress is transferred to adjacent patches, which explains earthquake cascades. Coulomb stress change on nearby faults predicts whether an earthquake will trigger others.

## How It's Best Learned
Calculate Coulomb stress changes from earthquake slip models. Predict fault stability using friction laws.

## Common Misconceptions
- Earthquakes rupture instantly everywhere on a fault.
- All faults have the same friction coefficient.
- Faults with low friction always slip.

## Explainer

From your understanding of the brittle-ductile transition, you know that rocks in Earth's upper crust behave as brittle materials — they fracture rather than flow when stressed beyond their strength. Faults are the fractures along which this brittle failure occurs, and understanding when and how they slip is the foundation of earthquake mechanics. The governing principle is deceptively simple: a fault slips when the **shear stress** acting along its surface exceeds its **frictional resistance**.

Frictional resistance on a fault is described by the **Coulomb failure criterion**: the shear stress required for slip equals the cohesion of the fault surface plus the product of the **coefficient of friction** and the **effective normal stress** (the stress pushing the two sides of the fault together, minus pore fluid pressure). This means three factors control whether a fault slips: how hard you push it sideways (shear stress), how tightly the fault surfaces are clamped together (normal stress), and how much fluid pressure reduces that clamping force. This is why injecting fluids into the subsurface — whether for wastewater disposal or geothermal energy — can trigger earthquakes: increasing pore pressure reduces effective normal stress, making it easier for faults to slip.

Once a fault begins to slip at one point, the rupture does not happen everywhere simultaneously. Instead, it **propagates** outward from the initial failure point (the hypocenter) like a crack spreading through glass. As one patch of the fault slips, it transfers stress to adjacent locked patches — the **Coulomb stress transfer**. If the transferred stress pushes a neighboring patch closer to failure, it ruptures too, and the earthquake grows. If the stress transfer is negative (the neighboring patch is unloaded), rupture stops. This cascading process determines earthquake size: a magnitude 5 earthquake ruptures a few kilometers of fault, while a magnitude 9 ruptures hundreds of kilometers, because stress transfer kept propagating the rupture across enormous fault areas.

Coulomb stress transfer also operates between separate faults after an earthquake, not just along a single fault during rupture. When a large earthquake occurs, it changes the stress field on every nearby fault. Faults that receive a positive Coulomb stress change — pushed closer to failure — become more likely to produce their own earthquakes. Faults that receive a negative stress change are temporarily stabilized, creating **stress shadows**. This framework has been remarkably successful at explaining aftershock patterns and earthquake triggering sequences. The 1992 Landers earthquake in California, for example, transferred stress to the fault that produced the 1999 Hector Mine earthquake — a connection predicted by Coulomb stress modeling years before the second event occurred.
