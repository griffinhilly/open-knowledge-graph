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
stage: advanced
status: draft
---

# Dislocations: Types and Movement

## Core Idea
Dislocations are line defects where the crystal lattice structure is disrupted along a line; edge and screw dislocations are the primary types, differing in geometry and stress response. Dislocations move through crystals under applied stress via glide and climb mechanisms, enabling plastic deformation at stresses orders of magnitude lower than theoretical predictions. Understanding dislocation mechanics is fundamental to explaining material strength, work hardening, and creep behavior.

## Explainer

From your study of point defects, you know that crystal lattices are never perfect — vacancies, interstitials, and substitutional atoms create local distortions. Dislocations are a different category of imperfection: they are **line defects**, meaning the disruption extends along a one-dimensional line through the crystal rather than being localized to a single lattice site. The two fundamental types are defined by the relationship between the **Burgers vector** b (the magnitude and direction of lattice distortion) and the dislocation line direction.

An **edge dislocation** can be pictured as an extra half-plane of atoms wedged into the upper portion of a crystal. The Burgers vector is perpendicular to the dislocation line. Under shear stress, an edge dislocation moves by shifting the extra half-plane one atomic spacing at a time — the bonds on one side break and reform on the other — so the dislocation line advances while the overall crystal extends by one Burgers vector. A **screw dislocation** has its Burgers vector parallel to the dislocation line, creating a helical arrangement of atomic planes (if you walk around the dislocation in a closed loop, you end up one lattice spacing higher or lower). Real dislocations in crystals are often **mixed dislocations** with both edge and screw character, curving through the lattice. Both types move primarily by **glide** — motion within a specific crystallographic slip plane — but edge dislocations can also **climb** perpendicular to their glide plane by absorbing or emitting vacancies, a thermally activated process important for creep at high temperatures.

The most important insight dislocations provide is resolving the enormous discrepancy between theoretical and observed yield strength. If you calculate the stress needed to slide two halves of a perfect crystal past each other (breaking all bonds simultaneously along the slip plane), you get values around G/10 to G/30, where G is the shear modulus — roughly 1–10 GPa for metals. But real metals yield at 10–100 MPa, a factor of 10–1000 lower. The resolution is that dislocations allow slip to propagate **sequentially** rather than simultaneously. Imagine moving a heavy rug across a floor: dragging the whole rug at once requires enormous force, but creating a small wrinkle (a "dislocation") and pushing the wrinkle forward requires far less. Each bond breaks and reforms locally as the dislocation passes; the net effect is the same macroscopic slip, but achieved at a fraction of the theoretical stress.

**Dislocation density** ρ (the total length of dislocation line per unit volume, in m/m³ = m⁻²) determines mechanical behavior. Annealed metals have ρ ≈ 10¹⁰–10¹² m⁻², while heavily cold-worked metals reach 10¹⁵–10¹⁶ m⁻². As density increases, dislocations interact and tangle, impeding each other's motion — this is the mechanism of **work hardening**: the more you deform a metal, the harder it becomes to deform further. Every strengthening mechanism in metals ultimately works by making dislocation motion more difficult, either by creating obstacles (precipitates, grain boundaries), generating internal stress fields (solute atoms), or multiplying dislocation density to create a tangled network that locks itself in place.
