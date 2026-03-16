---
id: work-energy-particles
title: Work-Energy Principle for Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: work-energy-theorem
  type: hard
- id: kinetic-energy
  type: hard
- id: potential-energy
  type: soft
- id: conservation-of-energy
  type: soft
- id: dot-product
  type: soft
builds-toward:
- impulse-momentum-particles
tags:
- dynamics
- work
- energy
- kinetic energy
- potential energy
- conservation
stage: formal-systems
status: validated
---

# Work-Energy Principle for Particles

## Core Idea
The work-energy principle states that net work done on a particle equals its change in kinetic energy: U₁₋₂ = T₂ − T₁, where T = ½mv². Work by a force along a path is U = ∫F·dr. Conservative forces (gravity, springs) have associated potential energy: V_g = mgh, V_e = ½kx². For conservative systems, total mechanical energy is conserved: T₁ + V₁ = T₂ + V₂. When non-conservative forces (friction, applied forces) act, the work they do modifies the energy balance: T₁ + V₁ + U₁₋₂(nc) = T₂ + V₂.

## How It's Best Learned
Classify every force as conservative or non-conservative. For conservative systems, apply energy conservation directly between two states without integrating equations of motion. For problems with friction or variable applied forces, compute work integrals explicitly.

## Common Misconceptions
- Normal forces and forces perpendicular to displacement do zero work — forgetting this inflates the work calculation.
- Applying conservation of energy when friction is present without including the energy dissipation term.
- Using the spring energy formula ½kx² with x measured incorrectly (x must be the spring deformation from natural length).

## Questions

```yaml
- question: "A spring with stiffness k = 400 N/m is first compressed 0.2 m from its natural length, then compressed 0.4 m. How do the stored potential energies compare?"
  type: multiple-choice
  options:
    - "The second compression stores twice the energy"
    - "The second compression stores three times the energy"
    - "The second compression stores four times the energy"
    - "The second compression stores the same energy because k is unchanged"
  answer: 2
  explanation: "Spring potential energy is V_e = ½kx², which is quadratic in deformation x. Doubling x multiplies the energy by 2² = 4: V_e(0.4) = ½(400)(0.16) = 32 J versus V_e(0.2) = ½(400)(0.04) = 8 J. This quadratic relationship means small increases in deformation cause disproportionately large increases in stored energy."

- question: "When friction acts on a sliding particle, total mechanical energy T + V is conserved as long as the particle eventually returns to its starting position."
  type: true-false
  answer: false
  explanation: "Friction is non-conservative: it converts mechanical energy to heat regardless of path or final position. Each pass over the surface dissipates energy, so the particle always arrives back with less mechanical energy than it started with. Conservation of energy T + V = constant holds only when all forces are conservative (gravity, ideal springs). With friction the correct form is T₁ + V₁ + U₁₋₂(nc) = T₂ + V₂, where U₁₋₂(nc) is the (negative) work done by friction."

- question: "A particle slides down a rough incline from rest. You want to find its speed at the bottom using the work-energy principle. What term must you include that you could omit if the surface were frictionless?"
  type: short-answer
  answer: "The work done by friction, U(nc) = −f·d (negative, since friction opposes motion), must be added to the left side of the energy equation. Without it the calculation overcounts the energy available to become kinetic energy."
  explanation: "On a frictionless incline, T₁ + V₁ = T₂ + V₂ suffices because all forces are conservative. Friction does negative work equal to the friction force times the distance traveled along the slope, reducing the final kinetic energy. Omitting this term would predict a speed higher than actually occurs."
```

## Explainer

Newton's second law and the work-energy principle are two ways to analyze the same motion, but they are not equally convenient for every problem. Newton's law requires tracking acceleration at each instant; work-energy connects two states — a start and an end — using scalar energy quantities, avoiding vectors and integration of force over time. Whenever you care only about how fast a particle is moving at one point given its speed at another, work-energy is usually faster.

The central equation is U₁₋₂ = T₂ − T₁, where U₁₋₂ = ∫F·dr is the net work done on the particle between states 1 and 2, and T = ½mv² is kinetic energy. Work is a dot product: only the component of force along the displacement contributes. This is why a normal force — always perpendicular to motion along a surface — does zero work. Gravity does work equal to mg times the vertical drop, regardless of the path taken; this path-independence is the hallmark of a conservative force.

For conservative forces (gravity and ideal springs), we define potential energy so that work can be expressed as a change in stored energy: U_gravity = −ΔV_g = −mgΔh, U_spring = −ΔV_e = −Δ(½kx²). When only conservative forces act, T + V = constant, which is the conservation of mechanical energy. This is a powerful shortcut: pick any two points on the path, write the energy balance, and solve — no need to integrate equations of motion.

When non-conservative forces act — friction, air drag, applied motors — they add or remove mechanical energy. The modified equation is T₁ + V₁ + U₁₋₂(nc) = T₂ + V₂. Friction always contributes a negative U(nc) equal to the friction force times the distance slid. The key habit is first classifying every force: conservative (gets a potential energy term) or non-conservative (its work must be computed explicitly and added to the equation). Missing a friction term, or including the normal force as a contributor, are the two most common sources of wrong answers.

Spring problems carry an additional trap: the deformation x in ½kx² must be measured from the spring's natural (unstretched) length, not from an arbitrary reference position. If the spring is pre-compressed by x₀ and then further compressed to x₁, the change in spring potential energy is ½k(x₁² − x₀²), not ½k(x₁ − x₀)². Computing ½k(Δx)² instead of Δ(½kx²) is a systematic error that gives wrong answers whenever the spring has any initial deformation.
