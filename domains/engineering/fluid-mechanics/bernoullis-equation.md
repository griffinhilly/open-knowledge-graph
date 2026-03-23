---
id: bernoullis-equation
title: Bernoulli's Equation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: continuity-equation-fluid
  type: hard
- id: conservation-of-energy
  type: soft
- id: fluid-statics-pressure
  type: hard
- id: work-and-energy
  type: soft
- id: energy-conservation-mechanical-systems
  type: soft
- id: conservation-of-energy-mechanical-systems
  type: hard
- id: energy-conservation-applications
  type: hard
- id: pressure-and-forces-in-fluids
  type: hard
builds-toward:
- flow-measurement-methods
- pipe-system-losses
- open-channel-flow
- potential-flow-theory
- hydraulic-machinery-intro
tags:
- Bernoulli
- energy equation
- ideal flow
- pressure-velocity tradeoff
stage: formal-systems
status: validated
---

# Bernoulli's Equation

## Core Idea
Bernoulli's equation, P + ½ρV² + ρgz = constant along a streamline, is an energy balance for steady, incompressible, inviscid flow along a streamline. It states that as fluid speed increases, static pressure decreases, and vice versa — a direct consequence of energy conservation. Bernoulli's equation can also be written as total head H = P/(ρg) + V²/(2g) + z = constant, making it useful for pipe and open-channel analysis.

## How It's Best Learned
Apply to venturi tubes, nozzles, and flow over airfoils to see the pressure-velocity tradeoff. Always check whether the assumptions hold (steady, incompressible, along one streamline, inviscid). Practice converting between pressure, velocity, and elevation heads using piezometer readings.

## Common Misconceptions
- Bernoulli's equation applies along a streamline only, not between streamlines in rotational flow.
- It cannot account for viscous losses; a real pipe flow requires the energy equation with a head loss term.
- Higher velocity does not always mean lower pressure in all situations — the equation requires all three terms to balance.

## Questions

```yaml
- question: "Water flows through a pipe that narrows from a large diameter to a small diameter. According to Bernoulli's equation, what happens to the static pressure in the narrow section?"
  type: multiple-choice
  options: ["It increases, because the water is more compressed", "It stays the same, because mass is conserved", "It decreases, because velocity increases and total energy is constant", "It increases, because more fluid passes through per second"]
  answer: 2
  explanation: "By the continuity equation, flow speed must increase in the narrower section to conserve mass. Bernoulli's equation then requires that an increase in the kinetic energy term (½ρV²) must be offset by a decrease in the pressure term P (assuming constant elevation). This is the classic venturi effect: faster flow, lower static pressure. Options A and D reflect common intuitions about compression and flow rate that do not apply to incompressible flow."

- question: "Bernoulli's equation can be used to calculate pressure losses in a long pipe with significant friction."
  type: true-false
  answer: false
  explanation: "Bernoulli's equation applies only to inviscid (frictionless) flow. In a real pipe, viscous friction dissipates mechanical energy as heat, so the total head is not conserved. For real pipe flow you must use the full energy equation, which includes a head loss term (h_L) accounting for friction and minor losses. Using Bernoulli's equation on a frictional system will overestimate downstream pressure."

- question: "State the four key assumptions that must hold for Bernoulli's equation to be valid."
  type: short-answer
  answer: "The flow must be (1) steady (not changing with time), (2) incompressible (constant density), (3) inviscid (no viscous friction), and (4) applied along a single streamline."
  explanation: "Each assumption eliminates a term or effect that would otherwise appear in the more general energy equation. Unsteady flow adds a time-derivative term; compressible flow changes density; viscosity introduces energy dissipation; and applying the equation across streamlines is invalid in rotational flow where the Bernoulli constant differs between streamlines. Checking these assumptions is the first step before applying the equation to any problem."
```

## Explainer

Bernoulli's equation is, at its core, a statement about energy conservation applied to a parcel of flowing fluid. Recall from mechanics that the total mechanical energy of an object is the sum of its kinetic energy, potential energy, and any work done by pressure forces. For a small packet of incompressible, inviscid fluid moving steadily along a streamline, those same three energy contributions appear: the static pressure P (energy per unit volume stored in the pressure field), the kinetic energy per unit volume ½ρV² (where ρ is fluid density and V is speed), and the gravitational potential energy per unit volume ρgz (where z is elevation). Bernoulli's equation says their sum is constant along the streamline: P + ½ρV² + ρgz = constant.

The most important practical consequence is the pressure-velocity tradeoff. If you follow a streamline from a wide pipe section to a narrow one, the continuity equation (which you already know) tells you the fluid must speed up in the narrow section to keep the same volume flow rate passing through. Bernoulli's equation then says that if ½ρV² increases, P must decrease — and it does, measurably so. This is the venturi effect, the physical basis for carburetors, aspirators, and venturi meters. The same principle explains why air moving over the curved top of an airplane wing travels faster (and therefore at lower pressure) than air moving under the flat bottom, generating lift.

Bernoulli's equation is also often written in head form by dividing every term by ρg: P/(ρg) + V²/(2g) + z = H, where H is the total head. This form is convenient because each term has units of meters (or feet), representing an equivalent height of fluid. Pressure head, velocity head, and elevation head sum to a constant total head. Engineers use this form when analyzing pipe systems and comparing readings from piezometers and pitot tubes.

Understanding the assumptions is as important as understanding the equation. The flow must be steady (no time variation), incompressible (no density changes — valid for most liquids and low-speed gases), inviscid (no friction — an idealization), and the equation applies along a single streamline only. Real pipe flows violate the inviscid assumption: friction converts mechanical energy to heat, so total head decreases along the pipe. Real fluids also have turbulence and secondary flows. When these effects matter, you extend Bernoulli into the full energy equation by adding a head loss term h_L on one side, which you will do when you study pipe system losses.

The power of Bernoulli's equation is not that it models every real flow accurately — it does not — but that it identifies the right variables and the right tradeoffs. Every more advanced fluid mechanics topic you encounter, from flow measurement to pump selection to aerodynamics, begins by asking whether Bernoulli applies and, if not, what correction terms are needed.
