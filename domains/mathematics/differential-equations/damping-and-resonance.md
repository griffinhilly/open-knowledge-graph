---
id: damping-and-resonance
title: Damping, Forced Vibrations, and Resonance
domain: mathematics
course: differential-equations
prerequisites:
- id: spring-mass-systems-and-vibrations
  type: hard
- id: undetermined-coefficients
  type: hard
builds-toward:
- rlc-circuits
tags:
- application
- forced-oscillations
- resonance
stage: formal-systems
status: draft
---

# Damping, Forced Vibrations, and Resonance

## Core Idea
Adding a damping term m·y'' + c·y' + k·y = F(t) to the spring-mass equation introduces energy dissipation and external forcing. When the driving frequency matches the natural frequency, resonance occurs, producing large-amplitude oscillations. Damping prevents unbounded growth.

## How It's Best Learned
Solve forced undamped systems (c = 0) to see resonance amplitude → ∞. Then add damping to show how energy loss limits amplification. Explore the phase lag between forcing and response.

## Common Misconceptions
- Thinking resonance only occurs at the natural frequency; damping shifts the resonance frequency slightly. - Confusing Q-factor (sharpness of resonance peak) with energy dissipation rate. - Not recognizing transient versus steady-state behavior in forced systems.
