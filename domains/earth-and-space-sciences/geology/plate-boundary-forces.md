---
id: plate-boundary-forces
title: 'Forces at Plate Boundaries: Stress Orientation and Motion'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: stress-strain-rock-deformation
  type: hard
- id: plate-boundaries-intro
  type: soft
builds-toward:
- seismic-hazard-assessment
tags:
- plate-boundaries
- stress
- forces
- motion
stage: formal-systems
status: validated
---

# Forces at Plate Boundaries: Stress Orientation and Motion

## Core Idea
Plate boundaries experience distinct stress regimes: divergent boundaries have extension (lowest stress vertical); transform boundaries have strike-slip (highest stress vertical); convergent boundaries have compression. Focal mechanisms of earthquakes reveal stress orientation and help identify which type of plate boundary exists.

## How It's Best Learned
Use focal mechanisms to infer stress orientations. Compare stress tensors to plate motion vectors and boundary geometry.

## Questions

```yaml
- question: "Seismologists analyze earthquakes along an unidentified plate boundary. All focal mechanisms show horizontal T-axes (tension axes), indicating the crust is being pulled apart horizontally. What type of boundary is this, and what fault style is expected?"
  type: multiple-choice
  options:
    - "A convergent boundary with thrust faulting — horizontal tension is typical of compressional settings"
    - "A transform boundary with strike-slip faulting — horizontal tension drives lateral shear motion"
    - "A divergent boundary with normal faulting — extension makes σ₃ horizontal and σ₁ (the weight of overlying rock) vertical"
    - "A subduction zone with reverse faulting — the descending slab creates horizontal tension in the overriding plate"
  answer: 2
  explanation: "Horizontal T-axes (tension axes) indicate that σ₃ (minimum compressive stress) is horizontal — the crust is being pulled apart. This is the stress regime at divergent boundaries, where σ₁ is vertical (the weight of overlying rock) and σ₃ is the horizontal extensional direction. With σ₁ vertical, crustal blocks drop downward along normal faults. Convergent boundaries show horizontal P-axes (σ₁ horizontal, thrust faulting). Transform boundaries show both P and T axes horizontal with σ₂ vertical, producing strike-slip motion. The focal mechanism is the definitive remote tool for reading the stress regime."

- question: "At a subduction zone, which orientation of the maximum compressive stress (σ₁) produces the characteristic reverse and thrust faulting observed?"
  type: multiple-choice
  options:
    - "Vertical — the weight of the subducted slab pushes downward, producing compressive stress that drives reverse faulting"
    - "Horizontal, directed perpendicular to the trench in the convergence direction — plates pushing together makes σ₁ horizontal"
    - "Horizontal and parallel to the trench axis — lateral mantle flow creates trench-parallel compression"
    - "Oblique at 45° to the surface, where the subducting and overriding plates meet"
  answer: 1
  explanation: "At convergent boundaries, plates push toward each other, making σ₁ (maximum compressive stress) horizontal in the convergence direction. With σ₁ horizontal and σ₃ vertical, rocks fail by reverse or thrust faulting — material is pushed up along low-angle fault planes because lateral compression exceeds the vertical load. This horizontal compression builds mountain ranges and generates the great megathrust earthquakes at subduction zones. Option A confuses σ₁ orientation: a vertical σ₁ produces normal faulting (divergent setting), not reverse faulting."

- question: "At transform boundaries, the maximum compressive stress (σ₁) is vertical — the weight of the overlying rock — which drives the horizontal strike-slip motion characteristic of these faults."
  type: true-false
  answer: false
  explanation: "At transform boundaries, the intermediate stress (σ₂) is vertical, while both σ₁ and σ₃ are horizontal, oriented at approximately 45° to the fault trace. This is the stress regime that drives pure horizontal (strike-slip) motion. A vertical σ₁ would produce normal faulting (the divergent boundary case). The three boundary types map to three different orientations of the vertical principal stress: divergent → σ₁ vertical (blocks drop); transform → σ₂ vertical (blocks slide); convergent → σ₃ vertical (rocks thrust upward). Each setting has a characteristic Anderson's faulting regime."

- question: "Focal mechanism solutions derived from earthquake first-motion data can reveal the orientation of the regional stress field at the earthquake's location."
  type: true-false
  answer: true
  explanation: "A focal mechanism solution shows the fault plane orientation and slip direction, from which the principal stress axes can be inferred: the compressional quadrants indicate the maximum stress direction (P-axis) and the tensional quadrants indicate the minimum stress direction (T-axis). By inverting populations of focal mechanisms in a region, geologists map the full regional stress tensor — determining not just fault type but the absolute orientation of σ₁, σ₂, and σ₃ throughout the crust. This is why focal mechanisms are among the most powerful remote-sensing tools in structural geology and seismic hazard assessment."

- question: "Explain why convergent boundaries produce thrust and reverse faults while divergent boundaries produce normal faults, in terms of which principal stress axis is vertical at each boundary type."
  type: short-answer
  answer: "At divergent boundaries, plates pull apart horizontally, making σ₃ (minimum stress) horizontal. The vertical stress (weight of overlying rock) becomes σ₁ — the dominant stress. Rocks fail by sinking along normal faults because vertical stress dominates and blocks drop along the easiest failure direction. At convergent boundaries, plates push together, making σ₁ (maximum stress) horizontal in the convergence direction and σ₃ vertical. With horizontal compression dominating, rocks are thrust upward along low-angle reverse faults because it is easier to push rock up than to overcome lateral compression."
  explanation: "This is Anderson's theory of faulting: σ₁ vertical → normal faults; σ₂ vertical → strike-slip faults; σ₃ vertical → thrust/reverse faults. The key is that the vertical principal stress is always a principal axis (the free surface imposes this), and its rank (1st, 2nd, or 3rd) determines the fault style. Plate boundary type sets which stress axis becomes vertical, which determines the fault geometry, which determines the focal mechanism — connecting plate tectonics, stress analysis, and seismology in a single coherent framework."
```

## Explainer

From your study of stress and strain in rock deformation, you know that stress has three principal axes — the maximum, intermediate, and minimum compressive stresses (σ₁, σ₂, σ₃) — and that the orientation of these axes determines what kind of faulting occurs. At plate boundaries, the type of relative motion between plates dictates the stress regime, and earthquakes along these boundaries broadcast that information through their **focal mechanisms**.

At **divergent boundaries** (mid-ocean ridges, continental rifts), plates pull apart. The dominant stress is extensional: the minimum compressive stress (σ₃) is horizontal and perpendicular to the ridge axis, while the maximum stress (σ₁) is vertical — the weight of the overlying rock. This produces normal faulting, where blocks drop down along steeply dipping fault planes. On a focal mechanism diagram (the "beachball" pattern derived from seismic first motions), normal faults appear with the tension axis (T) horizontal, confirming that the boundary is being stretched apart.

At **convergent boundaries** (subduction zones, collision belts), the situation reverses. Plates push together, making the maximum compressive stress (σ₁) horizontal and directed toward the overriding plate, while the minimum stress (σ₃) is vertical. This produces reverse and thrust faulting, where rock is pushed up and over itself along low-angle fault planes. Focal mechanisms at subduction zones show compression axes aligned with the direction of plate convergence. The stress field can be complex — the subducting slab pulls downward under its own weight (slab pull), while the overriding plate is compressed — but the net effect is shortening and crustal thickening.

**Transform boundaries** are the third case. Here, plates slide horizontally past each other, and the stress field is dominated by shear. The maximum and minimum compressive stresses are both horizontal, oriented at 45° to the fault trace, while the intermediate stress (σ₂) is vertical. This produces strike-slip faulting — pure horizontal displacement with no significant vertical motion. The San Andreas Fault is the textbook example: focal mechanisms along it consistently show horizontal T and P axes rotated ~45° from the fault strike, confirming lateral shear.

The practical power of this framework is that stress orientation at any point on Earth's surface can be inferred from earthquake focal mechanisms, and that information feeds directly into hazard assessment. A region showing consistent thrust-fault mechanisms is accumulating compressive strain and may be building toward a large earthquake. A region showing normal-fault mechanisms is extending and thinning. By mapping focal mechanisms across a plate boundary zone, geologists can identify not only the boundary type but also where stress is concentrated, where strain is partitioned across multiple faults, and where the next major rupture is most likely to occur.
