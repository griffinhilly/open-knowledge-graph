---
id: rectilinear-motion-particles
title: Rectilinear Motion of Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-rectilinear
  type: soft
builds-toward:
- curvilinear-motion-particles
tags:
- kinematics
- rectilinear
- position
- velocity
- acceleration
- one-dimensional
stage: formal-systems
status: draft
---

# Rectilinear Motion of Particles

## Core Idea
Rectilinear motion is one-dimensional motion along a straight path. Kinematics describes position x(t), velocity v = dx/dt, and acceleration a = dv/dt without reference to forces. For constant acceleration, kinematic equations relate displacement, velocity, time, and acceleration independently of the causing forces, enabling motion prediction.

## Explainer

Rectilinear motion is the gateway from statics — where things are still — to dynamics — where things move. The crucial shift is adding time as an independent variable. You now ask not just "what forces act?" but "where is the particle, how fast is it going, and how is that changing?"

The three **kinematic quantities** — position x(t), velocity v = dx/dt, and acceleration a = dv/dt — form a chain of derivatives. Velocity is the rate of change of position; acceleration is the rate of change of velocity. Moving in the other direction, if you know acceleration as a function of time, you recover velocity by integration (plus an initial condition), and position by integrating again. The chain rule of calculus links all three: given any one quantity as a function of time, the others follow by differentiation or integration. You can also relate velocity and acceleration without time by writing a = v dv/dx, a form useful when acceleration is given as a function of position.

The special and practically important case of **constant acceleration** produces four closed-form equations you can use without integration: v = v₀ + at, x = x₀ + v₀t + ½at², v² = v₀² + 2a(x − x₀), and x = x₀ + ½(v₀ + v)t. These equations form a complete toolkit: each equation omits one of the five quantities {x, v₀, v, a, t}, so you pick the equation that uses your three knowns to find your unknown. Free fall near Earth's surface (a = −g ≈ −9.81 m/s²) is the canonical example, but any problem with constant net force — a block on a frictionless ramp, a puck decelerating uniformly — fits this framework.

A conceptual boundary worth keeping clear: **kinematics** describes motion; **kinetics** explains it using forces. Rectilinear motion equations tell you how a particle moves given its initial state and acceleration, but they make no claim about what caused that acceleration. Forces don't appear in kinematics at all. When you later apply Newton's second law (ΣF = ma), you'll compute a from the forces and then use the kinematic equations to find position and velocity. The two halves — force analysis and motion description — plug together but remain conceptually distinct.
