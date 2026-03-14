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
stage: abstract-reasoning
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
