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
