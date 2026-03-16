---
id: phase-space-trajectories
title: Phase Space Trajectories
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
builds-toward:
- lagrangian-mechanics-intro
tags:
- phase-space
- dynamics
- trajectories
- energy
stage: formal-systems
status: draft
---

# Phase Space Trajectories

## Core Idea
Phase space plots position x vs. momentum p (or velocity v) show the complete instantaneous state of a dynamical system. For a harmonic oscillator, the curve traced out is an ellipse (from E = ½ m v² + ½ k x² = const). Closed curves represent periodic motion; open curves represent unbounded motion. Phase-space trajectories reveal dynamics without solving equations explicitly and are key to analyzing stability and chaos.

## Explainer

You already know **simple harmonic motion**: the position oscillates as x(t) = A cos(ωt) and the velocity as v(t) = −Aω sin(ωt). You are used to plotting these as functions of time — two separate graphs, each a sinusoidal wave. Phase space offers a different representation: instead of asking "where is the particle at each moment in time?", it asks "what is the complete state of the system at each moment, and how does that state evolve?" The state of a one-dimensional mechanical system is fully specified by two numbers: position x and momentum p (or equivalently, velocity v). Phase space is the plane with x on one axis and v (or p) on the other.

To trace the phase-space trajectory of a harmonic oscillator, eliminate time from the parametric equations. You have x = A cos(ωt) and v = −Aω sin(ωt), so x/A = cos(ωt) and v/(Aω) = −sin(ωt). Squaring and adding: (x/A)² + (v/Aω)² = cos²(ωt) + sin²(ωt) = 1. This is the equation of an **ellipse** in the (x, v) plane with semi-major axis A along the x-direction and semi-minor axis Aω along the v-direction. As time advances, the representative point traces this ellipse. Notice what happened: we eliminated t entirely and obtained a closed curve that represents the complete dynamical behavior of the oscillator — all its future and past states lie on this single ellipse.

The ellipse has a direct physical interpretation via energy conservation. The total energy E = ½mv² + ½kx² = constant defines an ellipse in (x, v) space (rescaling by 1/m: v² + (k/m)x² = 2E/m = ω²A²). Different energy levels — different amplitudes — produce different ellipses, all nested around the origin. The origin itself (x = 0, v = 0) is a special point: a **fixed point** of the dynamics, representing a particle sitting at equilibrium with no velocity. It is a **stable equilibrium** because nearby trajectories (small ellipses) stay near it; they do not spiral away. This geometrical picture immediately conveys stability without solving any equations.

The power of phase space becomes clear when you consider other systems. A **damped oscillator** (with friction) loses energy over time: its phase-space trajectory is a spiral that winds inward toward the origin, because each cycle the amplitude shrinks. A **pendulum** with large amplitude shows trajectories that are no longer ellipses but tear-drop shapes, reflecting the nonlinear restoring force. At the critical energy where the pendulum barely reaches the top, the trajectory passes through a **saddle point** — an unstable fixed point. Above that energy, the trajectories are open curves circling all the way around, representing continuous rotation. All of this structure — stability, bifurcations, the difference between oscillation and rotation — is visible geometrically in phase space without solving a single differential equation.

This geometric approach to dynamics is the gateway to Lagrangian and Hamiltonian mechanics, and ultimately to the study of chaos. In chaotic systems, trajectories in phase space do not form simple closed curves or spirals; they fill volumes in complex, fractal patterns that make long-term prediction impossible despite deterministic equations of motion. The key insight phase-space thinking instills is that **dynamics is geometry**: the evolution of a physical system traces a path through a state space, and the global structure of that state space — its fixed points, closed orbits, separatrices — tells you everything about the system's possible behaviors.


