---
id: fluid-kinematics
title: 'Fluid Kinematics: Describing Flow'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
- id: vector-fields
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- continuity-equation-fluid
- navier-stokes-equations
- potential-flow-theory
tags:
- streamlines
- pathlines
- velocity field
- Lagrangian
- Eulerian
- material derivative
stage: formal-systems
status: draft
---

# Fluid Kinematics: Describing Flow

## Core Idea
Fluid kinematics describes fluid motion without reference to forces. The Eulerian description tracks field quantities (velocity, pressure) at fixed points in space, while the Lagrangian description follows individual fluid parcels. The material derivative D/Dt = ∂/∂t + (V·∇) converts between the two, capturing both local acceleration and convective acceleration. Streamlines are tangent to the velocity field at an instant; pathlines trace actual particle trajectories; streaklines connect particles that passed through a common point.

## How It's Best Learned
Visualize the three line types using dye injection and smoke-wire experiments. Compute the material derivative for simple velocity fields analytically. Practice distinguishing steady vs. unsteady flow and recognizing when streamlines, pathlines, and streaklines coincide (only in steady flow).

## Common Misconceptions
- Streamlines and pathlines are the same only in steady flow; in unsteady flow they differ.
- The convective acceleration term (V·∇)V can be nonzero even in steady flow — a fluid particle can accelerate through a converging nozzle at steady conditions.
- Local acceleration (∂V/∂t) is zero in steady flow, but total acceleration need not be.
