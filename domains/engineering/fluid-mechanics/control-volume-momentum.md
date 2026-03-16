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
- id: newtons-second-law
  type: hard
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

## Explainer

Newton's second law says that force equals rate of change of momentum. You already know how to apply this to a particle or rigid body. Applying it to a flowing fluid requires a conceptual shift: instead of tracking individual fluid particles (which would be hopeless), you draw an imaginary box — a **control volume** — around a region of space and ask: what forces act on this box, and how does momentum flow in and out? This is the essence of the Reynolds Transport Theorem applied to momentum.

The resulting equation is ΣF = d/dt∫∫∫ ρV dV + ∫∫ ρV(V·n̂) dA. Read it left to right: the net external force on the control volume equals the rate of accumulation of momentum inside the volume plus the net rate of momentum flux leaving through its surfaces. The first right-hand-side term vanishes for **steady flow**, which is the case you will encounter most often. The momentum flux term ρV(V·n̂) requires careful attention to signs: V·n̂ is positive where flow exits (n̂ points outward) and negative where flow enters, so the term automatically gives positive flux out and negative flux in.

The forces in ΣF include everything acting on the control volume: pressure forces at inlet and outlet faces (force = pressure × area, directed inward on the fluid), reaction forces from walls or support structures, body forces like gravity, and viscous stresses at walls (often negligible for turbulent engineering flows at high Reynolds number). A common setup error is to forget the pressure forces at the inlet and outlet faces — they are surface forces on the control volume boundary, not just "background" pressures.

Consider a pipe bend as a concrete example. Draw the control volume enclosing the fluid inside the bend. At each inlet/outlet face, write the pressure force (p·A, acting inward on the fluid). Write the continuity equation first to find velocities. Then apply the x- and y-momentum equations separately: the difference in momentum flux between outlet and inlet plus any change in direction must be balanced by the net force, which includes both the pressure forces at the faces and the reaction force R from the pipe wall on the fluid. The force the fluid exerts on the pipe — which is what you want for structural design — is equal and opposite to R.

The power of this approach is that you never need to know what happens inside the control volume. The flow inside the bend may be turbulent, three-dimensional, and complex — but the integral momentum equation only cares about conditions at the inlet and outlet faces and the net external forces. This is what makes the control volume method indispensable in engineering: it delivers accurate force calculations from inlet/outlet measurements alone.
