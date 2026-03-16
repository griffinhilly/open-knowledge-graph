---
id: work-power-energy-fundamentals
title: 'Work, Power, and Energy: Fundamental Definitions'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-rectilinear
  type: soft
- id: dynamics-newtons-second-law
  type: hard
builds-toward:
- work-energy-particles
- potential-energy-conservative-forces
tags:
- work
- power
- energy
- kinetic-energy
stage: formal-systems
status: draft
---

# Work, Power, and Energy: Fundamental Definitions

## Core Idea
Work done by a force is W = ∫ F · dr, the integral of force component along the displacement path. Power is the rate of work: P = dW/dt = F · v. Kinetic energy is KE = ½mv². The work-energy theorem states that net work equals the change in kinetic energy: W_net = ΔKE. These concepts provide energy-based solutions to dynamics problems.

## Explainer

Newton's second law (F = ma) is powerful, but it gives you acceleration at each instant — to find speed or position changes over a distance, you must integrate. The **work-energy theorem** is what you get when you do that integration: it trades the instantaneous perspective (force and acceleration) for a cumulative one (work done over a path and the resulting change in kinetic energy). This is why energy methods often require far less algebra than Newton's law directly.

**Work** is not simply force times distance — it is the integral of the force component *along* the direction of motion: W = ∫ F · dr. The dot product is essential. A force perpendicular to the motion (like the normal force on a horizontal surface) does zero work, even if it is large. Only the component along the displacement contributes. For a constant force in the same direction as displacement, this simplifies to W = Fd. For a spring, where force varies with position, integration gives W = ½kx². The sign of work matters: positive work increases kinetic energy, negative work (like friction) removes it.

**Kinetic energy** KE = ½mv² is the mechanical energy stored in a moving mass. The work-energy theorem states W_net = ΔKE: the net work done by all forces equals the change in kinetic energy. This is independent of the path taken — only the starting and ending speeds matter (and whatever work was done between them). When you apply this theorem, you never need to know what forces did at intermediate moments: only their total cumulative contribution (work) matters.

**Power** P = dW/dt = F · v is the rate at which work is done. A car engine with high torque at low speed has the same power as one with low torque at high speed if the product F·v matches. This connects back to your kinematics prerequisite: speed v appears directly in both power and kinetic energy, so power and energy are deeply linked. A constant-power engine accelerates a vehicle in a characteristic way — fast at low speeds where kinetic energy grows quickly, slow at high speeds where air resistance absorbs the same power output. These fundamentals directly enable the principle of conservation of mechanical energy and the analysis of conservative force systems you will encounter next.
