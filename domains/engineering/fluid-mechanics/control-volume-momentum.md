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
stage: expert
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

## Questions

```yaml
- question: "Water flows steadily through a horizontal 90° pipe bend. The inlet and outlet pressures are equal, and the flow speed is the same at inlet and outlet. Is there a net force on the bend from the fluid?"
  type: multiple-choice
  options:
    - "No — since pressure and speed are equal at inlet and outlet, the momentum flux is the same at both faces and cancels out"
    - "Yes — even though the speed is unchanged, the direction of momentum flux changes by 90°, requiring a net force to redirect the flow"
    - "No — for steady flow, the time-derivative term vanishes and no force is needed"
    - "Yes — but only because of gravity acting on the fluid inside the bend"
  answer: 1
  explanation: "Momentum is a vector, not a scalar. Even if the speed (magnitude) is unchanged, a 90° direction change means the x-component of momentum flux goes from maximum to zero, and the y-component goes from zero to maximum. The net change in momentum flux must be balanced by a net external force — provided by the pipe walls acting on the fluid. This is the key insight: direction changes cost force even if speed doesn't change. The steady-flow simplification only eliminates the time-derivative term (d/dt∫∫∫ρV dV = 0); the momentum flux term is still nonzero."

- question: "In the control volume momentum equation ΣF = d/dt∫∫∫ρV dV + ∫∫ρV(V·n̂)dA, for steady flow through a pipe bend, which forces must be included in ΣF?"
  type: multiple-choice
  options:
    - "Only the reaction force from the pipe walls — pressure forces are internal to the fluid and cancel"
    - "Only the pressure forces at the inlet and outlet faces — wall reaction forces are structural, not fluid forces"
    - "Pressure forces at inlet and outlet faces, the wall reaction force on the fluid, and body forces like gravity"
    - "Only the net pressure difference between inlet and outlet, multiplied by the cross-sectional area"
  answer: 2
  explanation: "ΣF includes all external forces on the control volume: (1) pressure forces at each inlet and outlet face (p·A, acting inward on the fluid at inlet, outward at outlet — careful with signs); (2) the reaction force R from the pipe walls on the fluid (what you solve for); and (3) body forces like gravity if the bend is not horizontal. All three must be accounted for. A common error is to forget the pressure forces at the inlet/outlet faces, treating them as 'background' rather than as surface forces on the CV boundary."

- question: "For steady flow, the time-derivative term d/dt∫∫∫ρV dV in the momentum equation is zero, so the net force on the control volume equals only the net momentum flux out."
  type: true-false
  answer: true
  explanation: "For steady flow, the momentum stored inside the control volume does not change with time (same velocity field at every instant), so d/dt∫∫∫ρV dV = 0. The momentum equation simplifies to ΣF = ∫∫ρV(V·n̂)dA — the net external force equals the net momentum flux leaving through the control surface. This is the standard form used for pipe bends, nozzles, and turbine blade analysis. Unsteady problems (like a filling tank or accelerating flow) require the full equation with the storage term."

- question: "In the momentum flux term ρV(V·n̂)dA, the dot product V·n̂ is positive at both inlets and outlets when using the convention that n̂ points outward."
  type: true-false
  answer: false
  explanation: "With n̂ pointing outward from the control volume, V·n̂ is positive where fluid exits (flow and normal point in the same direction) and negative where fluid enters (flow opposes the outward normal). At an inlet, V points into the CV while n̂ points outward, so V·n̂ < 0, making the momentum flux contribution negative — correctly representing momentum flowing in. This sign convention is built into the integral and automatically gives the correct direction: outflow adds to the flux, inflow subtracts. Getting this sign wrong is the most common computational error in CV momentum problems."

- question: "Explain what information you do NOT need to calculate the force on a pipe bend using the control volume momentum method, and why this makes the method so powerful."
  type: short-answer
  answer: "You do not need to know the velocity field, pressure distribution, or turbulence structure inside the bend. The CV method requires only: inlet and outlet velocities (from continuity), pressures at the inlet and outlet faces, the flow density, and the geometry (direction of flow at each face). The internal flow — which may be turbulent, swirling, and three-dimensional — is irrelevant. This is powerful because it replaces an intractable internal fluid mechanics problem with a simple accounting of what enters and exits the CV boundary."
  explanation: "This is the core engineering value of the Reynolds Transport Theorem applied to a control volume: it converts a field problem (requiring knowledge everywhere) into a boundary problem (requiring knowledge only at the inlet and outlet faces). The complex internal flow in a real pipe bend cannot realistically be solved analytically, but the external force can be calculated exactly from inlet/outlet measurements. This is why CV analysis is the workhorse of hydraulic and aerodynamic force calculations in engineering practice."
```

## Explainer

Newton's second law says that force equals rate of change of momentum. You already know how to apply this to a particle or rigid body. Applying it to a flowing fluid requires a conceptual shift: instead of tracking individual fluid particles (which would be hopeless), you draw an imaginary box — a **control volume** — around a region of space and ask: what forces act on this box, and how does momentum flow in and out? This is the essence of the Reynolds Transport Theorem applied to momentum.

The resulting equation is ΣF = d/dt∫∫∫ ρV dV + ∫∫ ρV(V·n̂) dA. Read it left to right: the net external force on the control volume equals the rate of accumulation of momentum inside the volume plus the net rate of momentum flux leaving through its surfaces. The first right-hand-side term vanishes for **steady flow**, which is the case you will encounter most often. The momentum flux term ρV(V·n̂) requires careful attention to signs: V·n̂ is positive where flow exits (n̂ points outward) and negative where flow enters, so the term automatically gives positive flux out and negative flux in.

The forces in ΣF include everything acting on the control volume: pressure forces at inlet and outlet faces (force = pressure × area, directed inward on the fluid), reaction forces from walls or support structures, body forces like gravity, and viscous stresses at walls (often negligible for turbulent engineering flows at high Reynolds number). A common setup error is to forget the pressure forces at the inlet and outlet faces — they are surface forces on the control volume boundary, not just "background" pressures.

Consider a pipe bend as a concrete example. Draw the control volume enclosing the fluid inside the bend. At each inlet/outlet face, write the pressure force (p·A, acting inward on the fluid). Write the continuity equation first to find velocities. Then apply the x- and y-momentum equations separately: the difference in momentum flux between outlet and inlet plus any change in direction must be balanced by the net force, which includes both the pressure forces at the faces and the reaction force R from the pipe wall on the fluid. The force the fluid exerts on the pipe — which is what you want for structural design — is equal and opposite to R.

The power of this approach is that you never need to know what happens inside the control volume. The flow inside the bend may be turbulent, three-dimensional, and complex — but the integral momentum equation only cares about conditions at the inlet and outlet faces and the net external forces. This is what makes the control volume method indispensable in engineering: it delivers accurate force calculations from inlet/outlet measurements alone.
