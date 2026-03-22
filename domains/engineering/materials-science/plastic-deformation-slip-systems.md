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
stage: advanced
status: draft
---

# Mechanisms of Plastic Deformation and Slip

## Core Idea
Plastic deformation occurs through dislocation motion along slip planes and slip directions (slip systems), allowing permanent shape changes at applied stresses much lower than predictions from ideal crystal strength. Slip systems are defined by crystallography and vary with crystal structure (FCC, BCC, HCP metals have different numbers and orientations of slip systems). Work hardening occurs as dislocation density increases during deformation, increasing strength but decreasing ductility.

## Questions

```yaml
- question: "The theoretical shear strength of a perfect copper crystal is roughly G/10 (where G is the shear modulus). In practice, pure copper yields at roughly G/10,000 — a factor of 1000 lower. What is the correct explanation for this enormous discrepancy?"
  type: multiple-choice
  options:
    - "Copper always contains impurity atoms that reduce its strength far below the theoretical ideal"
    - "Dislocations allow slip to propagate one atomic row at a time rather than simultaneously across an entire plane, requiring far less stress — analogous to moving a wrinkle across a carpet rather than lifting the whole carpet"
    - "Thermal vibrations at room temperature provide sufficient energy to overcome the theoretical barrier"
    - "The theoretical calculation assumes simple cubic geometry; the FCC structure of copper is inherently weaker by a factor of 1000"
  answer: 1
  explanation: "The wrinkle analogy is the key insight. Sliding one entire plane over another requires every bond across that plane to stretch and break simultaneously, demanding very high stress. Dislocation motion advances the slip by one Burgers vector at a time — only a small number of bonds are stressed at once. The dislocation sweeps across the entire slip plane incrementally, producing the same macroscopic strain at a tiny fraction of the theoretical stress. This explains why real metals are ductile rather than brittle, and why dislocation theory was such a transformative insight in materials science."

- question: "FCC metals like aluminum are generally much more ductile than HCP metals like magnesium at room temperature. Which explanation is most consistent with slip system theory?"
  type: multiple-choice
  options:
    - "FCC metals have weaker interatomic bonds, so dislocations require less energy to move"
    - "FCC metals have 12 equivalent {111}⟨110⟩ slip systems, providing many orientations for dislocation motion; HCP metals have very few independent slip systems, severely restricting how the crystal can accommodate shape change"
    - "FCC metals work-harden more slowly, so they retain ductility after initial deformation"
    - "HCP planes are more closely packed than FCC planes, making dislocation motion on HCP slip planes inherently more difficult"
  answer: 1
  explanation: "The number of independent slip systems directly controls ductility. With 12 equivalent slip systems, FCC metals can accommodate deformation in almost any direction — there is nearly always a well-oriented slip system to activate. HCP metals have only 3 easily activated basal slip systems at room temperature, all nearly parallel, so they cannot accommodate arbitrary shape changes without cracking. This is why magnesium alloys require elevated temperature (which activates additional prismatic and pyramidal slip systems) for significant ductility."

- question: "Work hardening increases a metal's yield strength because plastic deformation increases dislocation density, and a higher dislocation density makes it harder for further dislocations to move."
  type: true-false
  answer: true
  explanation: "True. As dislocations multiply during plastic deformation, they intersect and tangle with each other, forming jogs and sessile segments that act as pinning points. The stress required to push additional dislocations through this 'forest' of obstacles increases with dislocation density. Macroscopically, the material requires greater applied stress to continue deforming — it has work-hardened. The trade-off is that suppressing dislocation motion also reduces the capacity for further deformation, decreasing ductility."

- question: "Plastic deformation in metals occurs when the applied stress is large enough to simultaneously rupture all atomic bonds across a slip plane."
  type: true-false
  answer: false
  explanation: "False — this describes the theoretical strength, which is orders of magnitude higher than actual yield stresses. Real plastic deformation occurs through dislocation motion: a dislocation sweeps across the slip plane one Burgers vector at a time, with only a small region of bonds stressed at any moment. The carpet wrinkle analogy captures this: moving a wrinkle takes a fraction of the force needed to lift the entire carpet. If plastic deformation required simultaneous bond rupture, metals would be brittle rather than ductile."

- question: "What does Schmid's law predict, and why does it mean that differently oriented grains in a polycrystal will begin to yield at different applied stresses?"
  type: short-answer
  answer: "Schmid's law states that the resolved shear stress on a slip system is τ = σ cos φ cos λ, where σ is the applied tensile stress, φ is the angle between the loading axis and the slip plane normal, and λ is the angle between the loading axis and the slip direction. Slip initiates when τ reaches the critical resolved shear stress (CRSS), a material constant. The Schmid factor cos φ cos λ varies between 0 and 0.5 depending on grain orientation relative to the loading axis. A grain with a favorably oriented slip system (Schmid factor near 0.5) will activate slip at a much lower applied stress than a grain oriented with all slip systems nearly parallel or perpendicular to the loading direction. This is why polycrystals yield progressively — grain by grain — rather than all at once."
  explanation: "Schmid's law is the crystallographic equivalent of resolving a force onto a plane: only the component of stress acting in the slip direction on the slip plane can drive dislocation motion. Grains most favorably aligned (so-called 'soft orientations') yield first and transfer stress to neighboring grains, which then yield in turn. This grain-by-grain yielding underlies the gradual onset of plastic flow seen in the stress-strain curves of polycrystalline metals."
```

## Explainer

From your study of elastic deformation and dislocations, you know two things: first, elastic deformation is reversible stretching of atomic bonds; second, real crystals contain line defects called dislocations where the crystal lattice is locally disrupted. These two ideas connect here: plastic deformation is permanent shape change caused not by bond rupture across an entire plane, but by the motion of dislocations through the crystal one atomic row at a time.

To see why dislocation motion is so important, consider the theoretical shear stress required to slide one entire atomic plane across another simultaneously. Calculations based on atomic bond strengths give a theoretical shear strength of roughly G/10 to G/30 (where G is the shear modulus). In practice, metals yield at stresses thousands of times lower than this — the measured yield shear stress for pure copper is about G/10,000. The resolution is that dislocations allow planes to slip incrementally, not all at once. Each dislocation sweeps across the slip plane one atom at a time, like a wrinkle moving across a carpet: the wrinkle requires much less force to advance than lifting the entire carpet. The cumulative effect of many dislocations traversing the crystal produces a macroscopic permanent strain.

Dislocations do not move on arbitrary planes. They are confined to specific crystallographic **slip systems** — combinations of a slip plane (typically the most densely packed plane) and a slip direction (the closest-packed direction). FCC metals like aluminum and copper have 12 equivalent {111}⟨110⟩ slip systems, giving them excellent ductility because there are many ways for dislocations to move. BCC metals like iron have more slip systems but less closely packed planes, making slip harder and giving BCC metals higher strength and lower ductility than FCC at room temperature. HCP metals like magnesium have few independent slip systems, severely limiting ductility and making them brittle unless deformation twins supplement slip. **Schmid's law** quantifies this: the resolved shear stress on a slip system is τ = σ cos φ cos λ, where φ and λ are the angles between the loading axis and the slip plane normal and slip direction. Slip occurs when this resolved stress reaches the **critical resolved shear stress** (CRSS), a material constant.

**Work hardening** — the increase in strength that occurs during plastic deformation — follows naturally from this picture. As dislocations multiply and move, they encounter and tangle with each other. Each intersection creates a jog or a sessile dislocation segment that acts as a pinning point for subsequent dislocation motion. The more deformation the material has undergone, the higher the dislocation density, and the harder it becomes for additional dislocations to move through the forest of obstacles. The material strengthens, but because dislocation motion is being suppressed, the capacity for further deformation (ductility) decreases. This tradeoff — strength gained at the cost of ductility — is the defining characteristic of cold work and the starting point for understanding yield strength and tensile properties.
