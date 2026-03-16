---
id: boltzmann-equation-kinetic
title: Boltzmann Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: kinetic-theory-basics
  type: hard
- id: boltzmann-transport-equation
  type: soft
- id: differential-equations-intro
  type: hard
builds-toward:
- chapman-enskog-expansion
tags:
- kinetic-theory
- transport
- non-equilibrium
stage: advanced
status: draft
---

# Boltzmann Equation

## Core Idea
The Boltzmann equation describes the evolution of single-particle distribution f(r,p,t) in phase space, accounting for both free streaming and collisions: ∂f/∂t + (p/m)·∇_r f + F·∇_p f = (∂f/∂t)_collision. Its solutions yield transport properties and show how systems relax toward equilibrium through irreversible processes.

## Explainer

From kinetic theory, you already know that a gas can be described statistically: instead of tracking each particle individually, we characterize the gas by a **distribution function** f(r, p, t) that tells us the density of particles at position r with momentum p at time t. At equilibrium, this is the Maxwell-Boltzmann distribution — a Gaussian in momentum space, uniform in position. The Boltzmann equation answers the much harder question: how does f evolve when the system is *not* at equilibrium? This is the central question of non-equilibrium statistical mechanics.

The equation has three terms on the left side, each with a clear physical interpretation. The ∂f/∂t term is just the rate of change of the distribution. The term (p/m)·∇_r f describes **free streaming**: in the absence of collisions, particles move ballistically, and a particle at position r with momentum p will be at r + (p/m)dt a moment later, so the distribution shifts. The F·∇_p f term describes how an external force (gravity, an electric field) deflects particle trajectories in momentum space. These three terms together give the **collisionless Boltzmann equation** (also called the Vlasov equation), valid when interactions are negligible.

What makes the equation useful — and hard — is the **collision integral** (∂f/∂t)_coll on the right side. This term accounts for particles scattering off each other, changing their momenta. In the simplest approximation (the BGK or relaxation-time approximation), it is replaced by −(f − f_eq)/τ, meaning the distribution relaxes toward equilibrium exponentially with time constant τ. More exact treatments model the binary collision process explicitly, summing over all pairs of incoming momenta that can scatter to produce a given outgoing state. Solving even this simplified equation is a formidable mathematical challenge.

The Boltzmann equation reveals something profound about irreversibility. Boltzmann showed that the quantity H = ∫f ln f d³r d³p decreases monotonically in time as collisions drive f toward equilibrium — this is the **H-theorem**, and it provides the microscopic basis for the second law of thermodynamics. At equilibrium, H is minimized and f is the Maxwell-Boltzmann distribution. Transport coefficients such as viscosity, thermal conductivity, and diffusivity all emerge as solutions: by computing how the distribution responds to small spatial gradients, the Chapman-Enskog expansion systematically extracts these macroscopic properties from the microscopic collision dynamics.
