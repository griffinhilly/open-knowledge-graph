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
stage: advanced
status: draft
---

# Seismic Ray Tracing and Wave Path Geometry

## Core Idea
Seismic ray tracing uses Snell's law and geometric principles to predict the paths that seismic waves follow through layered and laterally varying velocity structures. Rays bend toward the vertical in high-velocity zones and away from the vertical in low-velocity zones. This approach enables prediction of travel times, ray takeoff angles, and wave amplitudes essential for earthquake location and seismic imaging.

## Explainer

You already know Snell's law from optics or wave physics: when a wave crosses a boundary between two media with different velocities, it changes direction according to the ratio of the velocities. You also know from seismic velocity-depth models that the Earth is not uniform — velocity generally increases with depth due to increasing pressure and changing composition, and lateral variations reflect different rock types, temperatures, and structures. **Seismic ray tracing** applies Snell's law systematically through these complex velocity structures to predict exactly where seismic energy travels between a source (an earthquake or explosion) and a receiver (a seismometer).

In the simplest case — a stack of flat, horizontal layers each with a constant velocity — ray tracing is straightforward geometry. A seismic ray leaving a source at some angle hits the first layer boundary and bends according to Snell's law: sin(θ₁)/v₁ = sin(θ₂)/v₂. Since velocity typically increases with depth, the ray bends away from the vertical (θ₂ > θ₁) at each successive boundary, curving the ray path into a broad arc that eventually returns to the surface. The **ray parameter** p = sin(θ)/v is constant along any given ray — this is the seismic version of Snell's law generalized to the entire ray path, and it acts as the ray's identity card. A ray with a small p leaves the source steeply, penetrates deep, and arrives at a distant station. A ray with a large p leaves at a shallow angle, stays in the upper crust, and arrives nearby.

For realistic Earth models where velocity varies continuously rather than in discrete jumps, ray tracing becomes a differential equation problem. The ray path is computed by integrating through the velocity field, with the ray bending continuously rather than at discrete boundaries. In one dimension (velocity varying only with depth), this integration has analytical solutions for common velocity functions like linear increases with depth, producing characteristic curved ray paths. In two or three dimensions — where velocity also varies laterally, as it does near subduction zones, sedimentary basins, or magma chambers — numerical methods are required. Algorithms shoot rays from source to receiver and iteratively adjust the ray parameter until the ray arrives at the correct location, or they solve the **eikonal equation** to compute travel times on a grid.

The practical outputs of ray tracing are **travel time curves** (predicted arrival times as a function of distance), **ray paths** (the geometric trajectories through the Earth), and **amplitude estimates** (how energy spreads or focuses along each path). Travel time predictions are essential for locating earthquakes — by comparing observed arrival times at multiple stations with predictions from a velocity model, the source location and origin time can be determined. Ray paths reveal which parts of the Earth's interior are actually sampled by a given source-receiver pair, which is critical for seismic tomography. And ray geometry explains phenomena like shadow zones (regions where no direct rays arrive because of velocity decreases, as at the core-mantle boundary) and triplications (where multiple rays arrive at the same distance from different paths through a velocity increase).
