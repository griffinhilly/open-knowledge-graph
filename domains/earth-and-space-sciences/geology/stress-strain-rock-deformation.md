---
id: stress-strain-rock-deformation
title: 'Stress and Strain: Rock Deformation Fundamentals'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: plate-tectonics-driving-forces
  type: hard
- id: youngs-modulus-elasticity
  type: soft
builds-toward:
- brittle-ductile-transition
- fault-mechanics-rupture
tags:
- stress
- strain
- deformation
- mechanics
stage: advanced
status: draft
---

# Stress and Strain: Rock Deformation Fundamentals

## Core Idea
Stress (force per unit area) applied to rock causes strain (deformation). Stress is a 3D tensor with principal stresses oriented in three directions; strain relates to changes in shape and volume. The stress field orientation determines which existing faults will slip and in what direction.

## How It's Best Learned
Draw Mohr circles to analyze stress states. Use focal mechanisms from earthquakes to infer crustal stress orientations.

## Common Misconceptions
- Stress and pressure are identical.
- Rocks deform uniformly in all directions under stress.
- Strain is always permanent.

## Explainer

From your understanding of plate tectonics and the forces driving plate motion, you know that enormous forces act on Earth's lithosphere — ridge push, slab pull, mantle drag. These forces create **stress** within the rock, and the rock's response to that stress — its **strain** — produces the faults, folds, and fractures that geologists map in the field. Understanding the relationship between stress and strain is the gateway to structural geology and earthquake mechanics.

**Stress** is force per unit area, but unlike simple pressure (which pushes equally in all directions), tectonic stress is directional. It is described mathematically as a **tensor** — a quantity that captures force intensity in every direction simultaneously. At any point in the crust, the stress state can be resolved into three mutually perpendicular **principal stresses**: σ₁ (the maximum), σ₂ (the intermediate), and σ₃ (the minimum). No shear stress acts along these principal directions — they represent the orientations where stress is purely compressional or tensional. The relative magnitudes and orientations of these three principal stresses determine what kind of deformation occurs. When σ₁ is vertical (lithostatic load dominates), normal faults form. When σ₁ is horizontal, you get reverse faults (if σ₃ is vertical) or strike-slip faults (if σ₂ is vertical). This framework — formalized as **Anderson's theory of faulting** — connects the stress field directly to fault type.

**Strain** is the deformation that results from applied stress. It can be **elastic** (reversible, like stretching a rubber band — remove the stress and the rock returns to its original shape), **plastic** (permanent deformation without fracture, like bending a metal bar), or **brittle** (fracture and discrete displacement along faults). Whether a rock deforms elastically, plastically, or brittly depends on the rock type, temperature, pressure, strain rate, and presence of fluids. At shallow depths in the upper crust, rocks are cold and under low confining pressure, so they behave brittly — they fracture. At greater depths, higher temperature and pressure promote plastic flow. This is why earthquakes are concentrated in the upper 15–20 km of the crust: below that, rocks deform by flowing rather than breaking.

The tool that ties stress and strain together visually is the **Mohr circle** — a graphical representation of the stress state on planes of all possible orientations within a rock. On a Mohr diagram, you plot normal stress on the horizontal axis and shear stress on the vertical axis. The circle defined by σ₁ and σ₃ shows the stress resolved on every plane. When the circle touches the **failure envelope** (defined by the rock's cohesion and internal friction angle), fracture occurs on the plane corresponding to that point. This predicts both the stress conditions required for failure and the orientation of the resulting fracture. Mohr circles make abstract tensor mathematics tangible: you can see how increasing pore fluid pressure (which shifts the circle leftward toward the failure envelope) promotes faulting, or how increasing confining pressure (expanding the circle rightward) suppresses it.
