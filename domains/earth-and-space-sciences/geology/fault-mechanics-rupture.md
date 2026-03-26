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
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A previously stable fault sits near wastewater disposal wells that have been injecting fluid into the subsurface, raising pore pressure. According to the Coulomb failure criterion, why does seismic risk increase even though tectonic stresses haven't changed?"
  type: multiple-choice
  options:
    - "Injected water chemically weakens fault minerals, reducing cohesion to zero"
    - "Increased pore pressure reduces effective normal stress, lowering frictional resistance toward the pre-existing shear stress"
    - "Fluid injection increases shear stress by altering regional tectonic forces"
    - "Water raises subsurface temperatures, shifting the fault from brittle to ductile behavior"
  answer: 1
  explanation: "The Coulomb criterion states slip occurs when shear stress exceeds (cohesion + μ × effective normal stress), where effective normal stress = total normal stress − pore pressure. Raising pore pressure directly reduces the effective normal stress term, lowering frictional resistance. The fault approaches failure without any change in tectonic loading. This is the mechanism behind injection-induced seismicity — not altered tectonics, but a local reduction in the clamping force holding the fault closed."

- question: "A magnitude 6 earthquake occurs on Fault A. Seismologists observe a cluster of aftershocks on nearby Fault B, which had been locked for decades. What best explains this pattern?"
  type: multiple-choice
  options:
    - "The earthquake on Fault A reduced normal stress everywhere, weakening all faults in the region"
    - "Fault A transferred positive Coulomb stress to Fault B, pushing it closer to its own failure threshold"
    - "The seismic waves physically shook Fault B until it slipped from dynamic loading alone"
    - "Fault B slipped sympathetically because it shares the same fault zone as Fault A"
  answer: 1
  explanation: "Coulomb stress transfer explains why a mainshock on one fault triggers aftershocks on other faults. The earthquake on Fault A rearranges the stress field: some nearby faults receive positive Coulomb stress changes (pushed toward failure) while others receive negative changes (stress shadows, temporarily stabilized). Fault B experienced a positive change — the combination of increased shear stress and/or reduced effective normal stress brought it closer to its own Coulomb threshold. This mechanism is predictive: the 1992 Landers earthquake's stress transfer correctly predicted elevated seismicity at the location of the 1999 Hector Mine earthquake."

- question: "A fault with a low friction coefficient is generally more susceptible to slip than a fault with a high friction coefficient, most else being equal."
  type: true-false
  answer: false
  explanation: "The Coulomb criterion compares shear stress to (cohesion + μ × effective normal stress). A low friction coefficient reduces the resistance term, but whether the fault slips depends on whether shear stress exceeds that resistance. A fault with low friction but also very low shear stress (e.g., oriented at an unfavorable angle to the regional stress field) may remain locked, while a high-friction fault under high shear stress may be closer to failure. Friction coefficient, normal stress, pore pressure, and shear stress all matter — no single parameter determines slip in isolation."

- question: "Earthquake rupture propagates outward from the hypocenter because the slipping fault patch transfers stress to adjacent locked patches, which may then exceed their own failure threshold."
  type: true-false
  answer: true
  explanation: "This is the core physical mechanism of rupture propagation. The hypocenter is the initial failure point; the rupture spreads because a slipping patch concentrates stress at its propagating edge, pushing adjacent locked patches toward their Coulomb threshold. Whether the rupture continues or stops depends on whether this transferred stress exceeds the adjacent patch's resistance. This cascading process determines earthquake magnitude — large earthquakes (M9) propagate hundreds of kilometers because stress transfer kept driving rupture forward; small earthquakes (M5) propagate only kilometers before stress transfer becomes insufficient."

- question: "Explain why increasing pore fluid pressure can trigger slip on a fault that was previously stable, using the Coulomb failure criterion."
  type: short-answer
  answer: "Fault slip occurs when shear stress exceeds frictional resistance, which equals cohesion plus the friction coefficient times the effective normal stress. Effective normal stress equals total normal stress minus pore pressure. Increasing pore pressure directly reduces effective normal stress, which lowers frictional resistance. If tectonic loading has already brought shear stress close to the original resistance, even a modest pore pressure increase can push the fault past failure — without any change in tectonic forces."
  explanation: "This is the mechanism behind induced seismicity from wastewater disposal and geothermal operations. The Coulomb criterion has three adjustable quantities: shear stress (tectonically driven), normal stress (geometry and overburden), and pore pressure (manipulable by fluid injection). By raising pore pressure, engineers inadvertently 'unclamped' faults that were near failure. The key insight is that faults near populated areas may be tectonically loaded close to their threshold — only a small perturbation in any Coulomb term is needed to trigger slip."
```

## Explainer

From your understanding of the brittle-ductile transition, you know that rocks in Earth's upper crust behave as brittle materials — they fracture rather than flow when stressed beyond their strength. Faults are the fractures along which this brittle failure occurs, and understanding when and how they slip is the foundation of earthquake mechanics. The governing principle is deceptively simple: a fault slips when the **shear stress** acting along its surface exceeds its **frictional resistance**.

Frictional resistance on a fault is described by the **Coulomb failure criterion**: the shear stress required for slip equals the cohesion of the fault surface plus the product of the **coefficient of friction** and the **effective normal stress** (the stress pushing the two sides of the fault together, minus pore fluid pressure). This means three factors control whether a fault slips: how hard you push it sideways (shear stress), how tightly the fault surfaces are clamped together (normal stress), and how much fluid pressure reduces that clamping force. This is why injecting fluids into the subsurface — whether for wastewater disposal or geothermal energy — can trigger earthquakes: increasing pore pressure reduces effective normal stress, making it easier for faults to slip.

Once a fault begins to slip at one point, the rupture does not happen everywhere simultaneously. Instead, it **propagates** outward from the initial failure point (the hypocenter) like a crack spreading through glass. As one patch of the fault slips, it transfers stress to adjacent locked patches — the **Coulomb stress transfer**. If the transferred stress pushes a neighboring patch closer to failure, it ruptures too, and the earthquake grows. If the stress transfer is negative (the neighboring patch is unloaded), rupture stops. This cascading process determines earthquake size: a magnitude 5 earthquake ruptures a few kilometers of fault, while a magnitude 9 ruptures hundreds of kilometers, because stress transfer kept propagating the rupture across enormous fault areas.

Coulomb stress transfer also operates between separate faults after an earthquake, not just along a single fault during rupture. When a large earthquake occurs, it changes the stress field on every nearby fault. Faults that receive a positive Coulomb stress change — pushed closer to failure — become more likely to produce their own earthquakes. Faults that receive a negative stress change are temporarily stabilized, creating **stress shadows**. This framework has been remarkably successful at explaining aftershock patterns and earthquake triggering sequences. The 1992 Landers earthquake in California, for example, transferred stress to the fault that produced the 1999 Hector Mine earthquake — a connection predicted by Coulomb stress modeling years before the second event occurred.
