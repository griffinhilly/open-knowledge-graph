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
status: validated
---

# Phase Space Trajectories

## Core Idea
Phase space plots position x vs. momentum p (or velocity v) show the complete instantaneous state of a dynamical system. For a harmonic oscillator, the curve traced out is an ellipse (from E = ½ m v² + ½ k x² = const). Closed curves represent periodic motion; open curves represent unbounded motion. Phase-space trajectories reveal dynamics without solving equations explicitly and are key to analyzing stability and chaos.

## Questions

```yaml
- question: "A harmonic oscillator starts with amplitude A = 2 m. A second identical oscillator starts with amplitude A = 4 m. How do their phase-space trajectories compare?"
  type: multiple-choice
  options:
    - "They trace the same ellipse — amplitude does not affect the shape, only the period"
    - "They trace concentric ellipses — the larger amplitude produces a larger ellipse scaled up from the origin"
    - "They trace the same ellipse at different speeds — the larger amplitude oscillator moves faster around the ellipse"
    - "The 4m oscillator traces a circle; only small-amplitude oscillators trace ellipses"
  answer: 1
  explanation: "Each energy level (and thus each amplitude) corresponds to a distinct ellipse in phase space: (x/A)^2 + (v/Aω)^2 = 1. Different amplitudes give different semi-axes, producing a family of concentric ellipses nested around the origin. The origin itself is a fixed point (equilibrium). This nesting of ellipses by energy level is a key feature of the phase portrait — it immediately shows that all oscillations are periodic (closed curves) and that amplitude is continuously adjustable without qualitative change in behavior."

- question: "A damped harmonic oscillator (with friction) is plotted in phase space. What does its trajectory look like, and what does this reveal about the dynamics?"
  type: multiple-choice
  options:
    - "A closed ellipse — damping only affects the period, not the overall shape"
    - "A larger ellipse than the undamped case — damping adds energy to the system"
    - "An inward spiral toward the origin — each cycle loses energy, reducing amplitude until the system comes to rest"
    - "A straight line toward the origin — damped systems move directly to equilibrium without oscillating"
  answer: 2
  explanation: "Damping dissipates energy, so the amplitude decreases each cycle. In phase space, this means the trajectory spirals inward: each loop is a smaller ellipse than the previous one, converging toward the origin (equilibrium). The spiral structure immediately reveals that energy is being lost (motion is not periodic) and that the system approaches equilibrium asymptotically. The topology of the curve — open spiral vs. closed ellipse — distinguishes undamped from damped behavior at a glance, without solving any equations."

- question: "Two different initial conditions for the same frictionless harmonic oscillator can share the same phase-space trajectory."
  type: true-false
  answer: false
  explanation: "For a frictionless harmonic oscillator, the phase-space trajectory is an ellipse determined solely by total energy E. Two initial conditions with the same energy trace the same ellipse but start at different points on it. Two initial conditions with different energies trace different, non-intersecting ellipses. In general, phase-space trajectories for a deterministic system cannot cross — if two trajectories shared a point, the system would have two different futures from the same state, violating determinism. This non-crossing property is one of phase space's most important structural features."

- question: "A closed curve in phase space indicates that the system's motion is periodic — it repeats the same sequence of states indefinitely."
  type: true-false
  answer: true
  explanation: "A closed curve means the representative point eventually returns to its starting position in phase space — that is, the same (x, v) pair recurs. Since the state completely specifies the system's future evolution, returning to the same state means the subsequent motion is identical. This is exactly the definition of periodic motion. Conversely, open curves (spirals, hyperbolas, unbounded paths) represent non-periodic behavior: the system never returns to its initial state. The topology of phase-space curves — closed vs. open — directly encodes whether motion is periodic."

- question: "What does it mean to say 'dynamics is geometry,' and why is the phase-space representation more powerful than plotting position or velocity against time separately?"
  type: short-answer
  answer: "Saying 'dynamics is geometry' means that the qualitative behavior of a physical system — whether it oscillates, decays, is stable, or becomes chaotic — is encoded in the geometric structure of its phase-space trajectories, without needing to solve differential equations. Plotting position and velocity separately shows each variable's time history, but phase space shows the relationship between them as a single curve whose shape immediately reveals the system's global behavior: closed ellipse = periodic, inward spiral = damped, open curve = unbounded. Fixed points, stability, and qualitative changes in behavior become visible geometric features."
  explanation: "The time-series plots of x(t) and v(t) both require tracking time explicitly; phase space eliminates time to reveal the state-space structure directly. For the harmonic oscillator, the ellipse encapsulates all future and past behavior in a single geometric object. For more complex systems — nonlinear pendulums, chaotic systems — the phase portrait (the collection of all trajectories) reveals basins of attraction, separatrices, and strange attractors that time-series plots cannot show. This geometric viewpoint is the conceptual foundation of Hamiltonian mechanics and modern dynamical systems theory."
```

## Explainer

You already know **simple harmonic motion**: the position oscillates as x(t) = A cos(ωt) and the velocity as v(t) = −Aω sin(ωt). You are used to plotting these as functions of time — two separate graphs, each a sinusoidal wave. Phase space offers a different representation: instead of asking "where is the particle at each moment in time?", it asks "what is the complete state of the system at each moment, and how does that state evolve?" The state of a one-dimensional mechanical system is fully specified by two numbers: position x and momentum p (or equivalently, velocity v). Phase space is the plane with x on one axis and v (or p) on the other.

To trace the phase-space trajectory of a harmonic oscillator, eliminate time from the parametric equations. You have x = A cos(ωt) and v = −Aω sin(ωt), so x/A = cos(ωt) and v/(Aω) = −sin(ωt). Squaring and adding: (x/A)² + (v/Aω)² = cos²(ωt) + sin²(ωt) = 1. This is the equation of an **ellipse** in the (x, v) plane with semi-major axis A along the x-direction and semi-minor axis Aω along the v-direction. As time advances, the representative point traces this ellipse. Notice what happened: we eliminated t entirely and obtained a closed curve that represents the complete dynamical behavior of the oscillator — all its future and past states lie on this single ellipse.

The ellipse has a direct physical interpretation via energy conservation. The total energy E = ½mv² + ½kx² = constant defines an ellipse in (x, v) space (rescaling by 1/m: v² + (k/m)x² = 2E/m = ω²A²). Different energy levels — different amplitudes — produce different ellipses, all nested around the origin. The origin itself (x = 0, v = 0) is a special point: a **fixed point** of the dynamics, representing a particle sitting at equilibrium with no velocity. It is a **stable equilibrium** because nearby trajectories (small ellipses) stay near it; they do not spiral away. This geometrical picture immediately conveys stability without solving any equations.

The power of phase space becomes clear when you consider other systems. A **damped oscillator** (with friction) loses energy over time: its phase-space trajectory is a spiral that winds inward toward the origin, because each cycle the amplitude shrinks. A **pendulum** with large amplitude shows trajectories that are no longer ellipses but tear-drop shapes, reflecting the nonlinear restoring force. At the critical energy where the pendulum barely reaches the top, the trajectory passes through a **saddle point** — an unstable fixed point. Above that energy, the trajectories are open curves circling all the way around, representing continuous rotation. All of this structure — stability, bifurcations, the difference between oscillation and rotation — is visible geometrically in phase space without solving a single differential equation.

This geometric approach to dynamics is the gateway to Lagrangian and Hamiltonian mechanics, and ultimately to the study of chaos. In chaotic systems, trajectories in phase space do not form simple closed curves or spirals; they fill volumes in complex, fractal patterns that make long-term prediction impossible despite deterministic equations of motion. The key insight phase-space thinking instills is that **dynamics is geometry**: the evolution of a physical system traces a path through a state space, and the global structure of that state space — its fixed points, closed orbits, separatrices — tells you everything about the system's possible behaviors.


