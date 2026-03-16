---
id: spring-mass-system
title: Spring-Mass Oscillator
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: potential-energy
  type: hard
- id: conservation-of-energy
  type: soft
- id: differential-equations-intro
  type: soft
tags:
- spring
- oscillation
- Hooke-law
- SHM
stage: abstract-reasoning
status: validated
---
# Spring-Mass Oscillator

## Core Idea
A mass on a spring is the canonical SHM system. The spring exerts a restoring force F = −kx (Hooke's law), giving angular frequency ω = √(k/m) and period T = 2π√(m/k). Energy oscillates between kinetic (½mv²) and potential (½kx²) with total mechanical energy E = ½kA². At equilibrium the speed is maximum; at amplitude the speed is zero and PE is maximum.

## How It's Best Learned
Experimentally vary k (using different springs) and m and measure T, then compare to T = 2π√(m/k). Track energy at several positions during a cycle to verify E = ½kA² throughout.

## Common Misconceptions
- Thinking a stiffer spring leads to a longer period: stiffer (larger k) actually increases ω and decreases T.
- Forgetting that T = 2π√(m/k) assumes no damping and that the spring obeys Hooke's law throughout the motion.

## Explainer

The spring-mass oscillator is the simplest physical system that oscillates, and it serves as the template for understanding oscillation everywhere — electrical circuits, molecular vibrations, sound waves, and quantum mechanics. From your prerequisite on **simple harmonic motion**, you know the kinematic description: position varies sinusoidally as x(t) = A·cos(ωt + φ). The spring-mass system explains *why* that description is correct by deriving it from Newton's second law and Hooke's law.

Hooke's law gives the restoring force: F = −kx. When the mass is displaced from equilibrium by distance x, the spring pulls it back with a force proportional to that displacement, always directed toward equilibrium. Applying Newton's second law: −kx = m·a = m·(d²x/dt²), which rearranges to d²x/dt² = −(k/m)·x. This is the equation of simple harmonic motion: acceleration is proportional to, and opposite in sign to, displacement. The proportionality constant is ω² = k/m, giving **angular frequency** ω = √(k/m) and **period** T = 2π/ω = 2π√(m/k). A stiffer spring (larger k) increases ω and *decreases* T — the system oscillates faster, not slower, which is the most common intuition error.

The **energy picture** is equally important and connects directly to your prerequisites on **potential energy** and **conservation of energy**. The spring stores elastic potential energy PE = ½kx². At maximum displacement x = A, all energy is potential: PE = ½kA², KE = 0. At equilibrium x = 0, all energy is kinetic: KE = ½mv_max², PE = 0. Conservation of energy means PE + KE = ½kA² throughout the cycle — the two forms trade off continuously. Setting ½mv_max² = ½kA² gives v_max = A√(k/m) = Aω. The energy stored — and therefore the amplitude — is set by initial conditions; the frequency is set by k and m independently. This means you can change how vigorously the system oscillates without changing how fast it oscillates.

The spring-mass system is a model, not just a specific calculation, because Hooke's law is a **linearization** that applies to *any* stable equilibrium under small displacements. If you have a potential energy minimum — a marble in a bowl, an atom in a crystal lattice, a pendulum hanging at rest — the potential energy near the bottom is well approximated by a parabola: PE ≈ ½kx² for some effective spring constant k. This means every stable equilibrium oscillates like a spring-mass system for small perturbations. Understanding the spring-mass system in full gives you a reusable template: whenever you encounter an oscillating system in physics, chemistry, or engineering, the first question is always "what is the effective k and effective m?" — and then the period, frequency, energy, and velocity relations all follow immediately from the results you know here.
