---
id: flow-visualization-techniques
title: Flow Visualization Techniques
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: flow-measurement-methods
  type: soft
tags:
- streamlines
- pathlines
- streaklines
- PIV
- dye injection
- schlieren
- flow visualization
stage: formal-systems
status: draft
---
# Flow Visualization Techniques

## Core Idea
Flow visualization makes invisible fluid motion visible, connecting mathematical descriptions to physical reality. Three fundamental line types describe fluid motion: streamlines (tangent to the velocity field at an instant), pathlines (the trajectory a single fluid particle traces over time), and streaklines (the locus of all particles that have passed through a given point). In steady flow, all three coincide; in unsteady flow, they differ and each reveals different information. Experimental techniques include dye injection and hydrogen bubbles (for water), smoke wires and tufts (for air), and optical methods like schlieren and shadowgraph (which visualize density gradients in compressible flows without introducing tracers). Modern quantitative methods, especially Particle Image Velocimetry (PIV), seed the flow with tracer particles, illuminate a plane with a laser sheet, and cross-correlate successive images to extract full two-dimensional velocity fields with high spatial resolution.

## How It's Best Learned
Begin by sketching streamlines, pathlines, and streaklines for a simple unsteady flow (e.g., an oscillating source) to see how they diverge. Watch classic flow visualization videos (NCFMF series, Van Dyke's Album of Fluid Motion) showing dye injection around cylinders, airfoils, and in boundary layers. Set up a simple experiment: inject dye or food coloring into a steady pipe flow and a vortex to observe streaklines. Study PIV output images to understand how velocity vectors are extracted from particle displacement between frames, and appreciate the resolution advantages over point measurements like hot-wire anemometry or Pitot tubes.

## Common Misconceptions
- Streamlines, pathlines, and streaklines are identical only in steady flow. In unsteady flows, a smoke trail (streakline) does not show the instantaneous velocity direction (streamlines) and does not trace the path any single particle follows (pathline). Confusing them leads to incorrect flow interpretation.
- Dye injection and smoke visualization show streaklines, not streamlines. This distinction matters in unsteady flows like vortex shedding, where the smoke pattern can look very different from the instantaneous streamline pattern.
- PIV measures the velocity of tracer particles, not the fluid itself. The assumption that particles faithfully follow the flow (Stokes number << 1) must be verified, especially in high-speed or multiphase flows where particle inertia can cause the particles to deviate from fluid streamlines.
