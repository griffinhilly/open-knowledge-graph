---
id: iron-carbon-phase-diagram
title: The Iron-Carbon Phase Diagram and Steel Microstructures
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary
  type: hard
- id: lever-rule
  type: hard
- id: crystal-structure-basics
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: soft
builds-toward:
- heat-treatment-of-steels
tags:
- iron-carbon
- steel
- ferrite
- austenite
- pearlite
- martensite
stage: advanced
status: validated
---

# The Iron-Carbon Phase Diagram and Steel Microstructures

## Core Idea
The Fe-Fe₃C phase diagram governs the microstructures and properties of steels (0–2.14 wt% C) and cast irons (2.14–6.7 wt% C). Key phases include ferrite (α-Fe, BCC, low C solubility), austenite (γ-Fe, FCC, higher C solubility), cementite (Fe₃C, hard, brittle), and the eutectoid mixture pearlite (alternating ferrite and cementite lamellae). The eutectoid point at 0.76 wt% C and 727°C defines the steel composition that transforms entirely to pearlite on slow cooling. Carbon content is the primary lever for controlling the hardness-ductility trade-off in steel.

## How It's Best Learned
Trace cooling paths for hypoeutectoid, eutectoid, and hypereutectoid compositions and predict the resulting microstructure and phase fractions using the lever rule. Sketch expected micrographs for each case.

## Common Misconceptions
- Martensite does not appear on the equilibrium Fe-Fe₃C diagram — it forms only during rapid (non-equilibrium) quenching.
- Cast iron is not simply 'rusty' or degraded steel; it is a distinct class of alloys with different phase behavior and properties.

## Explainer

From your prerequisites in binary phase diagrams and the lever rule, you already know how to read a two-component phase diagram: locate your alloy composition, identify which phase region it falls in, read phase compositions from the boundaries using tie-lines, and calculate phase fractions with the lever rule. The iron-carbon diagram applies exactly these skills to the most technologically important binary system in history — every structural beam, automobile, and surgical tool depends on the phase relationships between iron and carbon.

The diagram in the steel range (0 to 2.14 wt% C) contains three key phases. **Ferrite** (α-Fe, BCC structure) is nearly pure iron with almost no dissolved carbon; it is soft and ductile, and it is the stable iron phase at room temperature. **Austenite** (γ-Fe, FCC structure) is stable only at elevated temperatures but can dissolve far more carbon — up to 2.14 wt% at 1148°C. The FCC structure has larger interstitial sites than BCC, which is why austenite holds more carbon. **Cementite** (Fe₃C) is a hard, brittle intermetallic compound that forms when carbon content exceeds the solubility limit of whichever iron phase is present. The critical transformation happens at the **eutectoid point** (0.76 wt% C, 727°C): on slow cooling, austenite of exactly this composition transforms entirely into **pearlite** — a lamellar mixture of ferrite and cementite, alternating at a spacing fine enough to be visible only under a microscope. Pearlite is significantly harder than pure ferrite but more ductile than cementite; it is the workhorse microstructure of mild steel.

To predict the microstructure of any steel, trace its cooling path on the diagram. A **hypoeutectoid** steel (less than 0.76 wt% C) enters the two-phase austenite + ferrite region on cooling: **proeutectoid ferrite** forms first at austenite grain boundaries, and as it grows, the remaining austenite becomes progressively richer in carbon (it is moving along the austenite phase boundary toward the eutectoid). When the temperature reaches 727°C, the remaining austenite — now at exactly 0.76 wt% C — transforms entirely to pearlite. The final microstructure is pearlite islands embedded in a ferrite matrix. Apply the lever rule just above 727°C using the three-phase equilibrium tie-line to find what fraction of the microstructure will be pearlite versus proeutectoid ferrite. A **hypereutectoid** steel (greater than 0.76 wt% C) follows the mirror image: proeutectoid cementite forms first at grain boundaries, depleting the austenite in carbon until it reaches 0.76 wt% C and transforms to pearlite.

The diagram shows equilibrium — slow cooling. Rapid quenching bypasses the equilibrium transformation and produces phases not found on the diagram. The most important non-equilibrium phase is **martensite**: when austenite is quenched faster than carbon can diffuse, the FCC lattice undergoes a diffusionless shear transformation to a body-centered tetragonal (BCT) structure with carbon atoms trapped in interstitial sites. Martensite is extremely hard and brittle because the trapped carbon severely distorts the lattice, blocking dislocation motion. Hardness increases with carbon content — a 0.8 wt% C martensite is far harder than a 0.2 wt% C martensite. **Tempering** — reheating martensite to an intermediate temperature — allows controlled carbon diffusion, partially relieving the lattice strain and recovering ductility. The iron-carbon diagram is therefore the starting map, and the deliberate departure from equilibrium — through quenching, tempering, and other heat treatments — is how engineers dial in any combination of hardness and ductility the application demands.
