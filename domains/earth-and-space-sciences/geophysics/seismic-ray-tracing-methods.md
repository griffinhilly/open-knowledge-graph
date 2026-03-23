---
id: seismic-ray-tracing-methods
title: Seismic Ray Tracing and Wave Path Geometry
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-velocity-depth-models
  type: hard
- id: snells-law
  type: hard
builds-toward:
- critical-refraction-and-head-waves
- reflection-seismic-survey-design
tags:
- seismic
- ray-theory
- propagation
- geometric-seismology
stage: expert
status: validated
---

# Seismic Ray Tracing and Wave Path Geometry

## Core Idea
Seismic ray tracing uses Snell's law and geometric principles to predict the paths that seismic waves follow through layered and laterally varying velocity structures. Rays bend toward the vertical in high-velocity zones and away from the vertical in low-velocity zones. This approach enables prediction of travel times, ray takeoff angles, and wave amplitudes essential for earthquake location and seismic imaging.

## Questions

```yaml
- question: "In a region where seismic velocity increases continuously with depth, what happens to the path of a seismic ray emitted from a surface source at an oblique angle?"
  type: multiple-choice
  options:
    - "It travels in a straight line at the takeoff angle, since there are no discrete boundaries to cause bending"
    - "It bends increasingly toward the vertical as it descends into faster material"
    - "It curves in a broad arc, bending away from the vertical as it descends, eventually returning to the surface"
    - "It reflects at depth and returns along the same path it descended"
  answer: 2
  explanation: "Where velocity increases with depth, the ray parameter p = sin(θ)/v must remain constant. As v increases, θ (the angle from vertical) must also increase to keep p constant — the ray bends away from vertical (toward horizontal). In a continuous velocity gradient this produces a smooth arc. Eventually θ approaches 90°, the ray is traveling horizontally, and it then curves back upward — returning to the surface without any discrete reflection boundary."

- question: "Two seismic rays leave the same earthquake source. Ray A has a small ray parameter p; Ray B has a large ray parameter p. Which statement correctly describes their behavior?"
  type: multiple-choice
  options:
    - "Ray A leaves at a shallow angle, stays near the surface, and arrives at a nearby station"
    - "Ray B leaves steeply, penetrates deep into the mantle, and arrives at a distant station"
    - "Ray A leaves steeply, penetrates deeply, and arrives at a distant station; Ray B leaves at a shallow angle and arrives nearby"
    - "Both rays follow the same path because they originate from the same source and travel through the same velocity structure"
  answer: 2
  explanation: "p = sin(θ)/v; a small p means a small takeoff angle θ (steep departure from vertical). A steeply departing ray penetrates deeply before curving back, traveling greater horizontal distance and arriving at a far station. A large p means a large takeoff angle (shallow departure), so the ray stays in shallow crust and arrives nearby. This is counterintuitive — steep launch angle means greater distance traveled, the opposite of a projectile in uniform gravity."

- question: "A seismic shadow zone — a region of the surface that receives no direct seismic waves from a distant earthquake — forms because seismic velocity increases sharply at a boundary, refracting all rays away from that region."
  type: true-false
  answer: false
  explanation: "Shadow zones form where velocity decreases (or drops suddenly), not increases. When rays enter a region of lower velocity, they refract toward the vertical (the low-velocity zone acts like a lens that bends rays inward), leaving a gap on the surface where no direct rays emerge. The classic example is the P-wave shadow zone caused by the sudden drop in velocity at the core-mantle boundary, where seismic energy enters the liquid outer core and bends, creating a shadow zone between about 103° and 143° from the earthquake source."

- question: "The ray parameter p = sin(θ)/v remains constant along the entire path of a seismic ray traveling through a layered or continuously varying Earth velocity structure."
  type: true-false
  answer: true
  explanation: "This is the seismic expression of Snell's law applied to the complete ray path. At every point along the ray, sin(θ)/v is the same constant p. At discrete boundaries, the angle changes precisely to preserve this ratio across the boundary. In a continuous gradient, the angle changes continuously for the same reason. The ray parameter is the ray's fundamental identity: it determines the takeoff angle, the depth of penetration, and the surface arrival distance."

- question: "Explain why seismic rays traveling through an Earth with velocity increasing with depth follow curved paths that return to the surface, rather than continuing downward indefinitely."
  type: short-answer
  answer: "The ray parameter p = sin(θ)/v is conserved along the ray path. As velocity v increases with depth, θ (the angle from vertical) must increase to keep p constant. As θ grows toward 90°, the ray becomes horizontal. Since θ continues increasing past 90° (the ray is now pointing upward), the ray curves back toward the surface. In a continuous velocity gradient, this produces a smooth arc without requiring any reflection boundary."
  explanation: "The ray is not reflected — it is continuously refracted by the velocity gradient. This distinction matters: the curved paths are head-wave-like refraction phenomena, not reflections. The steeper the initial angle (smaller p), the deeper the ray penetrates before curving back, since it needs a higher velocity (deeper depth) to accumulate enough change in θ to reverse direction."
```

## Explainer

You already know Snell's law from optics or wave physics: when a wave crosses a boundary between two media with different velocities, it changes direction according to the ratio of the velocities. You also know from seismic velocity-depth models that the Earth is not uniform — velocity generally increases with depth due to increasing pressure and changing composition, and lateral variations reflect different rock types, temperatures, and structures. **Seismic ray tracing** applies Snell's law systematically through these complex velocity structures to predict exactly where seismic energy travels between a source (an earthquake or explosion) and a receiver (a seismometer).

In the simplest case — a stack of flat, horizontal layers each with a constant velocity — ray tracing is straightforward geometry. A seismic ray leaving a source at some angle hits the first layer boundary and bends according to Snell's law: sin(θ₁)/v₁ = sin(θ₂)/v₂. Since velocity typically increases with depth, the ray bends away from the vertical (θ₂ > θ₁) at each successive boundary, curving the ray path into a broad arc that eventually returns to the surface. The **ray parameter** p = sin(θ)/v is constant along any given ray — this is the seismic version of Snell's law generalized to the entire ray path, and it acts as the ray's identity card. A ray with a small p leaves the source steeply, penetrates deep, and arrives at a distant station. A ray with a large p leaves at a shallow angle, stays in the upper crust, and arrives nearby.

For realistic Earth models where velocity varies continuously rather than in discrete jumps, ray tracing becomes a differential equation problem. The ray path is computed by integrating through the velocity field, with the ray bending continuously rather than at discrete boundaries. In one dimension (velocity varying only with depth), this integration has analytical solutions for common velocity functions like linear increases with depth, producing characteristic curved ray paths. In two or three dimensions — where velocity also varies laterally, as it does near subduction zones, sedimentary basins, or magma chambers — numerical methods are required. Algorithms shoot rays from source to receiver and iteratively adjust the ray parameter until the ray arrives at the correct location, or they solve the **eikonal equation** to compute travel times on a grid.

The practical outputs of ray tracing are **travel time curves** (predicted arrival times as a function of distance), **ray paths** (the geometric trajectories through the Earth), and **amplitude estimates** (how energy spreads or focuses along each path). Travel time predictions are essential for locating earthquakes — by comparing observed arrival times at multiple stations with predictions from a velocity model, the source location and origin time can be determined. Ray paths reveal which parts of the Earth's interior are actually sampled by a given source-receiver pair, which is critical for seismic tomography. And ray geometry explains phenomena like shadow zones (regions where no direct rays arrive because of velocity decreases, as at the core-mantle boundary) and triplications (where multiple rays arrive at the same distance from different paths through a velocity increase).
