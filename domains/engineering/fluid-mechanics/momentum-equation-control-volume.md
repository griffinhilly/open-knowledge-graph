---
id: momentum-equation-control-volume
title: Momentum Equation and Control Volume Analysis
domain: engineering
course: fluid-mechanics
prerequisites:
- id: control-volume-mass-balance
  type: hard
- id: navier-stokes-equations
  type: soft
- id: conservation-of-momentum
  type: hard
- id: conservation-of-linear-momentum
  type: hard
- id: momentum-and-impulse
  type: hard
builds-toward:
- energy-equation-steady-flow
- aerodynamic-forces-lift-drag-coefficients
tags:
- dynamics
- control-volume
- forces
stage: formal-systems
status: draft
---

# Momentum Equation and Control Volume Analysis

## Core Idea
Newton's second law applied to a control volume yields: ΣF = ṁ(V_out − V_in), relating external forces to momentum change of flowing fluid. This equation is crucial for calculating forces on pipe bends, analyzing jet propulsion, and determining reaction forces on hydraulic structures without needing detailed internal flow information.

## How It's Best Learned
Apply the momentum equation to simple configurations like jets hitting flat plates, flow through elbows, and rocket nozzles. Calculate forces and compare with experimental results to build confidence in the method.

## Common Misconceptions
- The momentum equation applies only to moving control volumes (it applies to fixed control volumes in inertial reference frames).
- Force calculated is the force exerted by the fluid (calculated force is the force that must be applied externally; by Newton's third law, the fluid exerts the equal and opposite force).

## Explainer

You already know Newton's second law: ΣF = ma, and you have used control volume analysis to track mass flowing through a region. The momentum equation is simply Newton's second law applied to a fixed region of space through which fluid continuously flows — a powerful generalization that lets you calculate forces on pipes, turbines, and aircraft without knowing anything about the flow details inside.

**The core idea.** For steady flow through a control volume, the net external force equals the rate at which momentum leaves the control volume minus the rate at which it enters: ΣF = ṁ·V_out − ṁ·V_in. Momentum flux (ṁ·V) replaces the ma term because instead of accelerating a fixed mass, you are continuously replacing old fluid with new fluid moving at a different velocity. The control volume exchanges momentum with its surroundings at the inlet and outlet ports; the external forces must supply whatever momentum change is required. This is the fluid analog of the impulse-momentum theorem you learned in mechanics.

**Setting up the problem.** Choose a control volume that cuts through surfaces where you know the velocity and pressure. For a pipe elbow, cut at the inlet and outlet cross-sections. For a jet striking a flat plate, let the control volume enclose the entire deflection zone. The key steps are: (1) define positive directions for x and y; (2) sum all external forces on the fluid inside the CV — this includes pressure forces at inlet/outlet faces, body weight, and the reaction force from the structure; (3) write the momentum equation in each coordinate direction; (4) solve for the unknown force. The force you calculate is what the structure must exert on the fluid. By Newton's third law, the fluid exerts the equal and opposite force on the structure — this is what loads the pipe bracket, bends the elbow, or thrusts the rocket.

**A worked mental model.** Consider a garden hose nozzle spraying a jet horizontally. The water enters the nozzle vertically downward and exits horizontally. Its x-momentum changes from zero to ṁ·V_jet, and the nozzle body must supply that x-momentum to the fluid (reaction: the jet "kicks back" the hose horizontally). Its y-momentum changes from ṁ·V_in downward to zero; the nozzle must supply an upward y-force to cancel that. The total reaction force on the nozzle is the vector sum of these two components. This is the reasoning behind rocket propulsion, where the expelled gas's momentum change equals the thrust force — no need to know anything about the complex combustion interior.

**Sign conventions and pressure terms.** Gauge pressures at the inlet and outlet faces generate forces on the control volume boundary that must be included in ΣF. At an outlet, the gauge pressure force acts in the direction of flow (pushing fluid out); at an inlet, it acts against the incoming flow direction (you must push fluid in). Forgetting these pressure terms is the most common calculation error. Once you include them consistently, the momentum equation gives the net mechanical force that the structure (pipe wall, nozzle body, blade row) must exert — the number a structural engineer needs to size bolts, welds, and supports.
