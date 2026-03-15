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
