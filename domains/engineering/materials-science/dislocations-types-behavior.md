---
id: dislocations-types-behavior
title: 'Dislocations: Types and Movement'
domain: engineering
course: materials-science
prerequisites:
- id: point-defects-in-materials
  type: hard
- id: stress-strain-behavior
  type: soft
builds-toward:
- plastic-deformation-slip-systems
- grain-boundaries-interfaces
tags:
- dislocations
- defects
- line-defects
stage: formal-systems
status: validated
---

# Dislocations: Types and Movement

## Core Idea
Dislocations are line defects where the crystal lattice structure is disrupted along a line; edge and screw dislocations are the primary types, differing in geometry and stress response. Dislocations move through crystals under applied stress via glide and climb mechanisms, enabling plastic deformation at stresses orders of magnitude lower than theoretical predictions. Understanding dislocation mechanics is fundamental to explaining material strength, work hardening, and creep behavior.

## Questions

```yaml
- question: "A theoretical calculation predicts that a pure aluminum crystal should require ~1 GPa to yield plastically, but real aluminum yields at roughly 10 MPa. What is the primary explanation for this discrepancy?"
  type: multiple-choice
  options:
    - "Aluminum bonds are weaker than models assume, so less stress is needed to break them"
    - "Stress concentrates at grain boundaries, locally exceeding the theoretical threshold"
    - "Dislocations allow slip to propagate sequentially — one bond breaks and reforms at a time — rather than simultaneously across the entire slip plane"
    - "Real aluminum crystals are not truly periodic at the atomic scale, so the theoretical model is inapplicable"
  answer: 2
  explanation: "The theoretical yield stress assumes all atomic bonds along a slip plane break simultaneously (like lifting the entire rug), requiring ~G/10. Dislocations act like a wrinkle in the rug: only the bonds near the dislocation core break at any instant, propagating slip one atomic spacing at a time at a tiny fraction of the theoretical stress. The macroscopic slip is identical, but achieved incrementally."

- question: "As a metal is cold-worked (repeatedly deformed), it becomes progressively harder to deform further. What mechanism is primarily responsible for this work hardening?"
  type: multiple-choice
  options:
    - "Grain boundaries fill with precipitates during deformation, blocking dislocation motion"
    - "Dislocations multiply and tangle, creating a network that impedes further dislocation motion"
    - "The Burgers vector grows with each deformation cycle, requiring more energy to move each dislocation"
    - "Screw dislocations convert to edge dislocations during cold working, and edge dislocations move more slowly"
  answer: 1
  explanation: "Cold working dramatically increases dislocation density (from ~10¹² to ~10¹⁶ m⁻²). At high density, dislocations interact and tangle, generating stress fields that obstruct each other's glide. The material strengthens because there are too many tangled dislocations to move easily — every strengthening mechanism in metals ultimately works by making dislocation motion more difficult."

- question: "For an edge dislocation, the Burgers vector is perpendicular to the dislocation line direction."
  type: true-false
  answer: true
  explanation: "An edge dislocation is defined by having its Burgers vector (the lattice distortion direction) perpendicular to the dislocation line. This contrasts with a screw dislocation, where the Burgers vector is parallel to the dislocation line. Mixed dislocations have both edge and screw character."

- question: "A heavily cold-worked metal is typically weaker than an annealed metal of the same composition, because cold working creates many defects that disrupt the lattice."
  type: true-false
  answer: false
  explanation: "Cold working makes a metal stronger, not weaker. The high dislocation density produced by cold working causes dislocations to tangle and impede each other, raising the yield stress. Annealed metals have low dislocation density and are relatively soft. This is precisely why work hardening is a useful industrial process — repeated deformation progressively increases strength."

- question: "Using the 'rug wrinkle' analogy, explain why pushing a wrinkle across a rug requires less force than dragging the whole rug — and how this maps onto why real metals yield at stresses far below the theoretical prediction."
  type: short-answer
  answer: "Dragging the entire rug simultaneously means overcoming all friction at once. Pushing a wrinkle moves only a small region at a time, requiring much less local force. In a crystal, the theoretical yield stress requires all bonds along the slip plane to break simultaneously. A dislocation allows slip to propagate by breaking and reforming bonds one at a time near the dislocation core, just like advancing the wrinkle. The full lattice displacement (one Burgers vector) still occurs, but the stress required is orders of magnitude lower because only a tiny fraction of bonds are strained at any instant."
  explanation: "The analogy captures the key insight: sequential bond breaking vs. simultaneous bond breaking. The dislocation mechanism means the required stress scales with the local distortion energy near the core, not with the energy needed to shear an entire perfect plane — hence the factor-of-1000 reduction from theoretical to observed yield strength."
```

## Explainer

From your study of point defects, you know that crystal lattices are never perfect — vacancies, interstitials, and substitutional atoms create local distortions. Dislocations are a different category of imperfection: they are **line defects**, meaning the disruption extends along a one-dimensional line through the crystal rather than being localized to a single lattice site. The two fundamental types are defined by the relationship between the **Burgers vector** b (the magnitude and direction of lattice distortion) and the dislocation line direction.

An **edge dislocation** can be pictured as an extra half-plane of atoms wedged into the upper portion of a crystal. The Burgers vector is perpendicular to the dislocation line. Under shear stress, an edge dislocation moves by shifting the extra half-plane one atomic spacing at a time — the bonds on one side break and reform on the other — so the dislocation line advances while the overall crystal extends by one Burgers vector. A **screw dislocation** has its Burgers vector parallel to the dislocation line, creating a helical arrangement of atomic planes (if you walk around the dislocation in a closed loop, you end up one lattice spacing higher or lower). Real dislocations in crystals are often **mixed dislocations** with both edge and screw character, curving through the lattice. Both types move primarily by **glide** — motion within a specific crystallographic slip plane — but edge dislocations can also **climb** perpendicular to their glide plane by absorbing or emitting vacancies, a thermally activated process important for creep at high temperatures.

The most important insight dislocations provide is resolving the enormous discrepancy between theoretical and observed yield strength. If you calculate the stress needed to slide two halves of a perfect crystal past each other (breaking all bonds simultaneously along the slip plane), you get values around G/10 to G/30, where G is the shear modulus — roughly 1–10 GPa for metals. But real metals yield at 10–100 MPa, a factor of 10–1000 lower. The resolution is that dislocations allow slip to propagate **sequentially** rather than simultaneously. Imagine moving a heavy rug across a floor: dragging the whole rug at once requires enormous force, but creating a small wrinkle (a "dislocation") and pushing the wrinkle forward requires far less. Each bond breaks and reforms locally as the dislocation passes; the net effect is the same macroscopic slip, but achieved at a fraction of the theoretical stress.

**Dislocation density** ρ (the total length of dislocation line per unit volume, in m/m³ = m⁻²) determines mechanical behavior. Annealed metals have ρ ≈ 10¹⁰–10¹² m⁻², while heavily cold-worked metals reach 10¹⁵–10¹⁶ m⁻². As density increases, dislocations interact and tangle, impeding each other's motion — this is the mechanism of **work hardening**: the more you deform a metal, the harder it becomes to deform further. Every strengthening mechanism in metals ultimately works by making dislocation motion more difficult, either by creating obstacles (precipitates, grain boundaries), generating internal stress fields (solute atoms), or multiplying dislocation density to create a tangled network that locks itself in place.
