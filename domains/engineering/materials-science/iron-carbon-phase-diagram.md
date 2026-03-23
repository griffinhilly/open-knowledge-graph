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
stage: formal-systems
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

## Questions

```yaml
- question: "An engineer rapidly quenches a 1.0 wt% C steel from the austenite region and obtains an extremely hard microstructure. A colleague argues this must be wrong because martensite doesn't appear on the Fe-Fe₃C phase diagram. Who is correct, and why?"
  type: multiple-choice
  options:
    - "The colleague is correct — only phases shown on the equilibrium diagram can form, so martensite is impossible in any steel"
    - "The engineer is correct — martensite forms during rapid quenching when carbon cannot diffuse and the FCC austenite lattice shears to BCT; it is a non-equilibrium phase that does not appear on the equilibrium diagram"
    - "Neither — rapid quenching of any steel composition always produces pearlite, regardless of cooling rate"
    - "The colleague is correct — martensite only forms in cast irons (above 2.14 wt% C), not in steels"
  answer: 1
  explanation: "The Fe-Fe₃C diagram shows equilibrium phases — what forms when cooling is slow enough for diffusion to reach completion. Martensite is a non-equilibrium phase that forms only when austenite is quenched faster than carbon can diffuse. The FCC lattice undergoes a diffusionless shear transformation to a body-centered tetragonal (BCT) structure with carbon atoms trapped in interstitial sites. Because the phase diagram only records equilibrium, martensite is absent — but this makes it no less real. Understanding that the diagram represents one end-member of a rate-dependent process is essential for applying it to real engineering."

- question: "A hypoeutectoid steel (0.4 wt% C) is slowly cooled from the austenite region through 727°C. What is the expected final microstructure?"
  type: multiple-choice
  options:
    - "Pure pearlite — all steel compositions transform entirely to pearlite at 727°C"
    - "Pure ferrite — the carbon content is below the eutectoid so no pearlite forms"
    - "Proeutectoid ferrite plus pearlite — ferrite forms first at austenite grain boundaries, enriching the remaining austenite in carbon until it reaches 0.76 wt% C and transforms to pearlite"
    - "A mixture of cementite and retained austenite, with no ferrite or pearlite"
  answer: 2
  explanation: "Only the eutectoid composition (0.76 wt% C) transforms entirely to pearlite. A hypoeutectoid steel first enters the two-phase austenite + ferrite region on cooling: proeutectoid ferrite forms at grain boundaries and the remaining austenite becomes progressively richer in carbon. By the time 727°C is reached, the remaining austenite has exactly the eutectoid composition (0.76 wt% C) and transforms fully to pearlite. The result is proeutectoid ferrite (formed above 727°C) plus pearlite (formed at 727°C). The lever rule applied just above 727°C predicts the relative fractions."

- question: "Austenite (FCC iron) can dissolve significantly more carbon than ferrite (BCC iron) at the same temperature because the FCC crystal structure has larger interstitial sites."
  type: true-false
  answer: true
  explanation: "This is the key structural reason behind the eutectoid transformation. BCC ferrite has only very small interstitial sites (tetrahedral and octahedral), giving a maximum carbon solubility of about 0.02 wt% at room temperature. FCC austenite has larger octahedral interstitial sites, accommodating up to 2.14 wt% C at 1148°C. When austenite transforms to ferrite on cooling, it can no longer hold the dissolved carbon, forcing carbon to precipitate as cementite (Fe₃C). The solubility difference is the thermodynamic driver of all steel microstructure development."

- question: "Martensite is the equilibrium phase that forms when steel is slowly cooled from the austenite region through the eutectoid temperature."
  type: true-false
  answer: false
  explanation: "Martensite is a non-equilibrium phase that forms only during rapid (non-equilibrium) quenching. Slow cooling through the eutectoid temperature produces equilibrium phases: ferrite and cementite, arranged as pearlite (for eutectoid composition) or as proeutectoid ferrite/cementite plus pearlite (for hypo/hypereutectoid compositions). Martensite does not appear on the equilibrium Fe-Fe₃C phase diagram at all. This is a critical distinction — the diagram applies to slow (equilibrium) cooling, and deliberate departures from equilibrium (quenching, tempering) are what allow engineers to produce martensite and tune steel properties."

- question: "Why does martensite have such extreme hardness compared to the equilibrium phases (ferrite and pearlite) formed by slow cooling of the same steel?"
  type: short-answer
  answer: "When austenite is quenched rapidly, carbon atoms cannot diffuse out to form cementite. Instead, the FCC iron lattice undergoes a diffusionless shear to a body-centered tetragonal (BCT) structure with carbon atoms trapped in interstitial sites. These trapped carbon atoms severely distort the BCT lattice, creating internal stress fields that block dislocation motion. Since plastic deformation requires dislocations to move, blocking them makes the material very hard and resistant to deformation. Hardness scales with carbon content — more trapped carbon means more lattice distortion and more dislocation pinning. Ferrite and pearlite are softer because carbon has had time to partition into cementite, leaving the iron lattice relatively undistorted and free for dislocation motion."
  explanation: "The mechanism — dislocation pinning by trapped interstitial atoms — is a general hardening principle in materials science. Martensite is the extreme case where a phase transformation traps the solute atom before it can escape. Tempering releases some of this trapped carbon through controlled diffusion, recovering ductility at the cost of some hardness — the engineer's fundamental trade-off."
```

## Explainer

From your prerequisites in binary phase diagrams and the lever rule, you already know how to read a two-component phase diagram: locate your alloy composition, identify which phase region it falls in, read phase compositions from the boundaries using tie-lines, and calculate phase fractions with the lever rule. The iron-carbon diagram applies exactly these skills to the most technologically important binary system in history — every structural beam, automobile, and surgical tool depends on the phase relationships between iron and carbon.

The diagram in the steel range (0 to 2.14 wt% C) contains three key phases. **Ferrite** (α-Fe, BCC structure) is nearly pure iron with almost no dissolved carbon; it is soft and ductile, and it is the stable iron phase at room temperature. **Austenite** (γ-Fe, FCC structure) is stable only at elevated temperatures but can dissolve far more carbon — up to 2.14 wt% at 1148°C. The FCC structure has larger interstitial sites than BCC, which is why austenite holds more carbon. **Cementite** (Fe₃C) is a hard, brittle intermetallic compound that forms when carbon content exceeds the solubility limit of whichever iron phase is present. The critical transformation happens at the **eutectoid point** (0.76 wt% C, 727°C): on slow cooling, austenite of exactly this composition transforms entirely into **pearlite** — a lamellar mixture of ferrite and cementite, alternating at a spacing fine enough to be visible only under a microscope. Pearlite is significantly harder than pure ferrite but more ductile than cementite; it is the workhorse microstructure of mild steel.

To predict the microstructure of any steel, trace its cooling path on the diagram. A **hypoeutectoid** steel (less than 0.76 wt% C) enters the two-phase austenite + ferrite region on cooling: **proeutectoid ferrite** forms first at austenite grain boundaries, and as it grows, the remaining austenite becomes progressively richer in carbon (it is moving along the austenite phase boundary toward the eutectoid). When the temperature reaches 727°C, the remaining austenite — now at exactly 0.76 wt% C — transforms entirely to pearlite. The final microstructure is pearlite islands embedded in a ferrite matrix. Apply the lever rule just above 727°C using the three-phase equilibrium tie-line to find what fraction of the microstructure will be pearlite versus proeutectoid ferrite. A **hypereutectoid** steel (greater than 0.76 wt% C) follows the mirror image: proeutectoid cementite forms first at grain boundaries, depleting the austenite in carbon until it reaches 0.76 wt% C and transforms to pearlite.

The diagram shows equilibrium — slow cooling. Rapid quenching bypasses the equilibrium transformation and produces phases not found on the diagram. The most important non-equilibrium phase is **martensite**: when austenite is quenched faster than carbon can diffuse, the FCC lattice undergoes a diffusionless shear transformation to a body-centered tetragonal (BCT) structure with carbon atoms trapped in interstitial sites. Martensite is extremely hard and brittle because the trapped carbon severely distorts the lattice, blocking dislocation motion. Hardness increases with carbon content — a 0.8 wt% C martensite is far harder than a 0.2 wt% C martensite. **Tempering** — reheating martensite to an intermediate temperature — allows controlled carbon diffusion, partially relieving the lattice strain and recovering ductility. The iron-carbon diagram is therefore the starting map, and the deliberate departure from equilibrium — through quenching, tempering, and other heat treatments — is how engineers dial in any combination of hardness and ductility the application demands.
