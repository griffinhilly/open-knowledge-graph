---
id: plastic-deformation-slip-systems
title: Mechanisms of Plastic Deformation and Slip
domain: engineering
course: materials-science
prerequisites:
- id: elastic-deformation-moduli
  type: hard
- id: dislocations-types-behavior
  type: hard
builds-toward:
- yield-strength-tensile-properties
tags:
- plastic-deformation
- dislocation-motion
- slip
stage: formal-systems
status: draft
---

# Mechanisms of Plastic Deformation and Slip

## Core Idea
Plastic deformation occurs through dislocation motion along slip planes and slip directions (slip systems), allowing permanent shape changes at applied stresses much lower than predictions from ideal crystal strength. Slip systems are defined by crystallography and vary with crystal structure (FCC, BCC, HCP metals have different numbers and orientations of slip systems). Work hardening occurs as dislocation density increases during deformation, increasing strength but decreasing ductility.

## Explainer

From your study of elastic deformation and dislocations, you know two things: first, elastic deformation is reversible stretching of atomic bonds; second, real crystals contain line defects called dislocations where the crystal lattice is locally disrupted. These two ideas connect here: plastic deformation is permanent shape change caused not by bond rupture across an entire plane, but by the motion of dislocations through the crystal one atomic row at a time.

To see why dislocation motion is so important, consider the theoretical shear stress required to slide one entire atomic plane across another simultaneously. Calculations based on atomic bond strengths give a theoretical shear strength of roughly G/10 to G/30 (where G is the shear modulus). In practice, metals yield at stresses thousands of times lower than this — the measured yield shear stress for pure copper is about G/10,000. The resolution is that dislocations allow planes to slip incrementally, not all at once. Each dislocation sweeps across the slip plane one atom at a time, like a wrinkle moving across a carpet: the wrinkle requires much less force to advance than lifting the entire carpet. The cumulative effect of many dislocations traversing the crystal produces a macroscopic permanent strain.

Dislocations do not move on arbitrary planes. They are confined to specific crystallographic **slip systems** — combinations of a slip plane (typically the most densely packed plane) and a slip direction (the closest-packed direction). FCC metals like aluminum and copper have 12 equivalent {111}⟨110⟩ slip systems, giving them excellent ductility because there are many ways for dislocations to move. BCC metals like iron have more slip systems but less closely packed planes, making slip harder and giving BCC metals higher strength and lower ductility than FCC at room temperature. HCP metals like magnesium have few independent slip systems, severely limiting ductility and making them brittle unless deformation twins supplement slip. **Schmid's law** quantifies this: the resolved shear stress on a slip system is τ = σ cos φ cos λ, where φ and λ are the angles between the loading axis and the slip plane normal and slip direction. Slip occurs when this resolved stress reaches the **critical resolved shear stress** (CRSS), a material constant.

**Work hardening** — the increase in strength that occurs during plastic deformation — follows naturally from this picture. As dislocations multiply and move, they encounter and tangle with each other. Each intersection creates a jog or a sessile dislocation segment that acts as a pinning point for subsequent dislocation motion. The more deformation the material has undergone, the higher the dislocation density, and the harder it becomes for additional dislocations to move through the forest of obstacles. The material strengthens, but because dislocation motion is being suppressed, the capacity for further deformation (ductility) decreases. This tradeoff — strength gained at the cost of ductility — is the defining characteristic of cold work and the starting point for understanding yield strength and tensile properties.
