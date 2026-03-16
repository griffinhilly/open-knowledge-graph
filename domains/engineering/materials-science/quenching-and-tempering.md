---
id: quenching-and-tempering
title: Quenching and Tempering
domain: engineering
course: materials-science
prerequisites:
- id: heat-treatment-of-steels
  type: hard
- id: iron-carbon-phase-diagram
  type: hard
builds-toward:
- case-hardening-surface-treatments
tags:
- martensite-formation
- quench-media
- tempering
- ttt-diagram
- cct-diagram
- hardenability
stage: formal-systems
status: draft
---

# Quenching and Tempering

## Core Idea
Quenching and tempering is the two-step heat treatment used to produce steels with high strength and adequate toughness. In quenching, steel is heated into the austenite region (above the A3 or Acm line) and then rapidly cooled — in water, oil, polymer solution, or forced air — fast enough to suppress the diffusion-controlled formation of pearlite or bainite, trapping carbon in the iron lattice to form martensite. Martensite is a body-centered tetragonal (BCT) structure supersaturated with carbon; it is extremely hard but brittle. Time-Temperature-Transformation (TTT) diagrams and Continuous-Cooling-Transformation (CCT) diagrams map the kinetics of these phase transformations, showing the cooling rates needed to avoid the "nose" of the pearlite/bainite C-curve and achieve full martensitic transformation. In the tempering step, the as-quenched martensite is reheated to a temperature between 150 and 650 degrees C, allowing carbon to diffuse out and form fine carbide precipitates. This reduces hardness but substantially improves toughness and ductility. The choice of tempering temperature controls the final balance: low-temperature tempering retains high hardness (for cutting tools), while high-temperature tempering maximizes toughness (for structural components). Hardenability — the depth to which martensite forms during quenching — depends on alloy composition, with elements like Mn, Cr, Mo, and Ni shifting the TTT nose to longer times and enabling through-hardening of thicker sections.

## How It's Best Learned
Overlay cooling curves for water, oil, and air quenches onto a TTT diagram for a specific steel (e.g., 1080 or 4340) to predict the resulting microstructure. Then examine a hardness-versus-tempering-temperature plot to see the hardness-toughness trade-off quantitatively. Compare Jominy end-quench test results for plain-carbon versus alloy steels to understand hardenability differences.

## Common Misconceptions
- The quench medium does not directly harden the steel — it controls the cooling rate, which determines whether the austenite transforms to martensite (fast) or pearlite (slow).
- Tempering does not weaken the steel in a detrimental sense; it deliberately trades some hardness for greatly improved toughness, producing a more useful engineering material.
- All steels are not equally hardenable — low-carbon steels cannot form much martensite regardless of quench rate because there is insufficient carbon to distort the lattice.

## Explainer

The iron-carbon phase diagram you mastered as a prerequisite shows you what phases are thermodynamically stable — but thermodynamic stability is only half the story in heat treatment. The other half is **kinetics**: how fast do those stable phases actually form? When you heat steel into the austenite region and then rapidly cool it, you are racing against the clock. The austenite wants to decompose into ferrite and cementite (pearlite), but doing so requires carbon atoms to diffuse — and diffusion takes time. If you cool fast enough, you outrun the diffusion and the austenite has no choice but to transform to martensite, a metastable phase that captures all the carbon in a strained lattice.

The **TTT (Time-Temperature-Transformation) diagram** makes this concrete. It plots temperature on the y-axis and (logarithmic) time on the x-axis, and it shows C-shaped "nose" curves that mark when pearlite and bainite begin and finish forming at each temperature. The nose of the pearlite C-curve represents the temperature where transformation is fastest — typically around 550°C for plain carbon steels — because it balances two competing factors: the thermodynamic driving force (larger at lower temperature) and atomic diffusivity (faster at higher temperature). To form martensite, your cooling curve on this diagram must pass to the left of the pearlite nose without touching it. The **critical cooling rate** is the minimum rate that achieves this. Water quenching produces steep cooling curves that easily miss the nose; oil quenching is slower and may only just miss it; air cooling is usually too slow for plain carbon steels.

**CCT (Continuous-Cooling-Transformation) diagrams** are more directly applicable to real practice because they account for the changing transformation kinetics as temperature drops continuously, rather than isothermally. The CCT diagram shifts the C-curves to longer times and lower temperatures compared to the TTT diagram, and it shows what microstructure — martensite, bainite, pearlite, or mixtures — results from different cooling rates. Overlaying actual cooling curves (from thermocouple measurements at different depths in a quenched bar) onto the CCT diagram predicts the microstructure at each location. This is why large cross-sections are a problem: the surface cools faster than the center, potentially giving martensite at the surface and softer pearlite in the core.

**Hardenability** quantifies how deeply martensite forms during quenching, and it explains why alloy steels exist. Alloying elements like Mn, Cr, Mo, and Ni slow down pearlite and bainite formation — they shift the TTT nose to longer times — making it easier for slower cooling rates to achieve martensite. A 4340 alloy steel can be through-hardened in a 50 mm bar with an oil quench; a 1080 plain carbon steel of the same size might only harden a few millimeters from the surface. The **Jominy end-quench test** standardizes this measurement: a bar is water-quenched at one end only, and hardness is plotted as a function of distance from the quench end. The resulting **hardenability band** is tabulated for each steel grade. Selecting a steel for a structural component involves matching the hardenability to the required cross-section — too little hardenability leaves soft spots, too much is unnecessary cost. Tempering then calibrates the final property balance: low-temperature tempering (150–250°C) for tools requiring maximum hardness, high-temperature tempering (500–650°C) for structural parts requiring toughness.
