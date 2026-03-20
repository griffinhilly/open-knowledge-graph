---
id: control-volume-momentum-applications
title: 'Control Volume Momentum Equation: Forces from Flow'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: control-volume-steady-flow-mass
  type: hard
builds-toward:
- flow-around-cylinders-spheres
- jet-mixing-and-entrainment
tags:
- momentum
- forces
- control-volume
- thrust
stage: advanced
status: draft
---

# Control Volume Momentum Equation: Forces from Flow

## Core Idea
The momentum equation for a control volume relates the net force on the control surface to the net momentum flux leaving minus entering. ΣF = Σ(ṁ_out * v_out) - Σ(ṁ_in * v_in). This principle explains forces exerted by flowing fluids on bends, nozzles, and jet-impacting surfaces without requiring detailed velocity field analysis.

## How It's Best Learned
Apply to simple cases: jet hitting a flat plate, flow through a 90° bend, rocket nozzle exit. Draw momentum diagrams showing velocity vectors and their magnitude differences.

## Explainer

You already know that the control volume approach to mass conservation says: what flows in must flow out under steady conditions. The momentum equation is the direct extension of that same bookkeeping idea to Newton's second law. Momentum is a vector quantity — it has both magnitude and direction — so momentum *flux* through a surface depends not just on how much mass crosses the boundary but on the velocity vector of that mass.

The governing statement is simply Newton's second law applied to a fluid volume: **net force = rate of change of momentum**. For steady flow with discrete inlets and outlets, this collapses to ΣF = Σ(ṁ_out · **v**_out) − Σ(ṁ_in · **v**_in). Each term is a mass flow rate multiplied by a velocity vector. The forces on the left side include pressure forces acting on the control surfaces, body forces like gravity, and the unknown reaction force you're usually solving for (the force a pipe elbow exerts on the fluid, for example).

Consider a jet of water hitting a stationary flat plate and deflecting sideways. The incoming jet carries momentum in the x-direction; the deflected flow carries none (it leaves perpendicular). The x-momentum that was in the incoming jet must have been destroyed by a force — the plate pushes back on the fluid in the −x direction, and by Newton's third law, the fluid pushes the plate in the +x direction. The magnitude of that force is simply ṁ · V_in, the mass flow rate times the inlet velocity. No integration over a velocity field is needed; only the conditions at the inlet and outlet of the control surface matter.

The real power of the method appears in problems where internal flow details are complex but boundary conditions are known. A rocket nozzle converts high-pressure combustion products into a high-velocity jet. The thrust is the reaction force on the nozzle walls — but you never need to know how the flow accelerates internally. You only need the mass flow rate and exit velocity, plus any pressure difference at the exit plane from ambient. Similarly, forces on pipe bends, jet pumps, and turbine blades can all be found by applying momentum flux accounting at the control surface boundaries, treating the interior as a black box.
