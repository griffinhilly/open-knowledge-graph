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

## Questions

```yaml
- question: "A 400 N crate slides 5 meters across a frictionless horizontal floor. The normal force from the floor acts upward with magnitude 400 N throughout the motion. How much work does the normal force do?"
  type: multiple-choice
  options:
    - "2000 J — the normal force equals the weight and acts over the full 5-meter displacement"
    - "0 J — the normal force is perpendicular to the displacement, so the dot product is zero"
    - "−2000 J — the normal force opposes the downward weight, doing negative work"
    - "400 J — work equals force magnitude regardless of direction"
  answer: 1
  explanation: "Work is W = ∫ F · dr — the dot product of force and displacement. The normal force acts vertically (upward) while the displacement is horizontal. These are perpendicular, so F · dr = F·dr·cos(90°) = 0. The normal force does zero work, even though it is large and the object is moving. Only force components along the direction of motion contribute to work. This is a critical point: a large force is not sufficient to do work — direction matters."

- question: "A motor outputs 45 kW of power while driving a conveyor belt. The belt moves at 15 m/s. What force does the motor exert on the belt?"
  type: multiple-choice
  options:
    - "675,000 N — multiply power (W) by speed (m/s) to get force"
    - "3000 N — use F = P/v = 45,000/15"
    - "30 N — the power in kW divided by the speed gives force in N directly"
    - "45 N — each kW of power produces 1 N of force per m/s"
  answer: 1
  explanation: "Power P = F · v, so F = P/v = 45,000 W / 15 m/s = 3000 N. The common error (option A) multiplies instead of divides — it confuses the relationship. Always convert power to watts before dividing by speed in m/s to obtain force in newtons."

- question: "A force acting on a moving object can do zero work on that object even if the force is nonzero and the object moves a nonzero distance."
  type: true-false
  answer: true
  explanation: "Work is W = F · d · cos(θ), where θ is the angle between the force and displacement vectors. If θ = 90° (force perpendicular to motion), cos(90°) = 0 and the work is zero regardless of the force magnitude or distance traveled. Common examples include the normal force on a horizontal surface and centripetal force in circular motion — both act perpendicular to velocity and do no work."

- question: "The work done on an object by a constant force equals the magnitude of that force multiplied by the total distance the object travels."
  type: true-false
  answer: false
  explanation: "Work equals the force component along the displacement, multiplied by the displacement: W = F·d·cos(θ). If the force is at an angle to the motion, only its component along the displacement does work — the perpendicular component contributes nothing. For example, a force of 100 N applied at 60° to the direction of motion over 10 m does only 100 × 10 × cos(60°) = 500 J, not 1000 J. 'Force times distance' is only correct when the force is parallel to the displacement."

- question: "Why does the work-energy theorem allow you to solve for a particle's final speed using only the net work done and the initial speed, without tracking what forces did at intermediate points along the path?"
  type: short-answer
  answer: "The work-energy theorem states that W_net = ΔKE = ½mv_f² − ½mv_i². Because work is defined as the integral of the net force along the displacement — a scalar quantity that accumulates all force contributions over the entire path — it condenses the entire force history into a single number. The theorem then maps that accumulated work directly to the change in kinetic energy, which depends only on initial and final speeds. The path shape, the variation in force along the way, and intermediate velocities are all already captured in the work integral and do not need to be tracked separately."
  explanation: "This is what makes energy methods more efficient than applying F = ma directly: instead of solving a differential equation for velocity as a function of position, you integrate force over displacement once (or recognize W = Fd for constant forces) and get the speed change immediately."
```

## Explainer

Newton's second law (F = ma) is powerful, but it gives you acceleration at each instant — to find speed or position changes over a distance, you must integrate. The **work-energy theorem** is what you get when you do that integration: it trades the instantaneous perspective (force and acceleration) for a cumulative one (work done over a path and the resulting change in kinetic energy). This is why energy methods often require far less algebra than Newton's law directly.

**Work** is not simply force times distance — it is the integral of the force component *along* the direction of motion: W = ∫ F · dr. The dot product is essential. A force perpendicular to the motion (like the normal force on a horizontal surface) does zero work, even if it is large. Only the component along the displacement contributes. For a constant force in the same direction as displacement, this simplifies to W = Fd. For a spring, where force varies with position, integration gives W = ½kx². The sign of work matters: positive work increases kinetic energy, negative work (like friction) removes it.

**Kinetic energy** KE = ½mv² is the mechanical energy stored in a moving mass. The work-energy theorem states W_net = ΔKE: the net work done by all forces equals the change in kinetic energy. This is independent of the path taken — only the starting and ending speeds matter (and whatever work was done between them). When you apply this theorem, you never need to know what forces did at intermediate moments: only their total cumulative contribution (work) matters.

**Power** P = dW/dt = F · v is the rate at which work is done. A car engine with high torque at low speed has the same power as one with low torque at high speed if the product F·v matches. This connects back to your kinematics prerequisite: speed v appears directly in both power and kinetic energy, so power and energy are deeply linked. A constant-power engine accelerates a vehicle in a characteristic way — fast at low speeds where kinetic energy grows quickly, slow at high speeds where air resistance absorbs the same power output. These fundamentals directly enable the principle of conservation of mechanical energy and the analysis of conservative force systems you will encounter next.
