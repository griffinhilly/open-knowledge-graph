---
id: simple-harmonic-motion
title: Simple Harmonic Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: circular-motion-kinematics
  type: soft
- id: derivatives-of-trigonometric-functions
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: amplitude-period-phase-shift
  type: soft
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- spring-mass-system
- simple-pendulum
tags:
- SHM
- oscillation
- restoring-force
- sinusoidal
stage: abstract-reasoning
status: validated
---

# Simple Harmonic Motion

## Core Idea
Simple harmonic motion (SHM) occurs when a restoring force is proportional to displacement from equilibrium: F = −kx. The resulting motion is sinusoidal: x(t) = A cos(ωt + φ), where A is amplitude, ω = √(k/m) is angular frequency, and φ is phase. Period T = 2π/ω depends only on system parameters (mass, spring constant), not amplitude. SHM is the mathematical archetype for all oscillatory behavior.

## How It's Best Learned
Derive the equations by applying F = ma to F = −kx: m(d²x/dt²) = −kx, then verify that x = A cos(ωt) is a solution. Connect SHM to circular motion: projecting uniform circular motion onto one axis produces SHM.

## Common Misconceptions
- Thinking larger amplitude means faster oscillation: period T is independent of amplitude in ideal SHM.
- Confusing angular frequency ω (rad/s) with ordinary frequency f (Hz): ω = 2πf.
- Assuming SHM equations apply when the restoring force is not proportional to displacement.
