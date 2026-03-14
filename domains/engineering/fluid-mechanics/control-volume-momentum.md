---
id: control-volume-momentum
title: Momentum Equation for Control Volumes
domain: engineering
course: fluid-mechanics
prerequisites:
- id: continuity-equation-fluid
  type: hard
- id: conservation-of-momentum
  type: soft
- id: bernoullis-equation
  type: soft
- id: double-integrals-cartesian
  type: soft
- id: hydrostatic-forces-on-surfaces
  type: soft
builds-toward:
- pipe-system-losses
- hydraulic-machinery-intro
tags:
- control volume
- Reynolds transport theorem
- momentum flux
- reaction forces
stage: formal-systems
status: validated
---
# Momentum Equation for Control Volumes

## Core Idea
The integral momentum equation for a control volume states that the sum of external forces equals the rate of change of momentum inside the CV plus the net momentum flux out: ΣF = d/dt∫∫∫ρV dV + ∫∫ρV(V·n̂) dA. This is the Reynolds Transport Theorem applied to linear momentum. It is especially useful for computing forces on pipe bends, nozzles, turbine blades, and jet deflectors without needing to know the internal flow details.

## How It's Best Learned
Apply to a pipe bend or reducer where both continuity and momentum are needed. Draw a clear control volume, identify all surface forces (pressure, reaction) and body forces (gravity), then apply the momentum equation in x and y components separately. Verify with a simplified Bernoulli-based energy check.

## Common Misconceptions
- External forces on the control volume include both pressure forces at inlet/outlet faces and reaction forces from solid walls — both must be included.
- The momentum flux term involves ρV(V·n̂), not ρV alone; the dot product with the outward normal n̂ gives the correct sign convention.
- For steady flow the time-derivative term vanishes, simplifying the equation considerably.
