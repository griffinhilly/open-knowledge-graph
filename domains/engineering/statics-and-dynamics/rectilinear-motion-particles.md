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

## Questions

```yaml
- question: "A particle's acceleration is given as a function of position, a = f(x). You want to find velocity as a function of position without explicitly solving for x(t). Which relationship is most useful?"
  type: multiple-choice
  options:
    - "v = dx/dt, integrated directly"
    - "a = dv/dt, integrated with respect to time"
    - "a = v dv/dx, which allows separating v and x"
    - "v² = v₀² + 2a(x − x₀), valid for all accelerations"
  answer: 2
  explanation: "When acceleration is a function of position, the chain rule identity a = v dv/dx lets you write f(x) = v dv/dx and separate variables: f(x)dx = v dv, integrating both sides to get v as a function of x directly. The constant-acceleration equation v² = v₀² + 2a(x − x₀) only applies when a is constant. Integrating a = dv/dt with respect to time requires knowing a as a function of t, not x. The a = v dv/dx form is precisely the tool for position-dependent acceleration."

- question: "A car brakes uniformly from v₀ = 30 m/s to rest. The braking distance is 45 m. Which kinematic equation most directly gives the deceleration, and why?"
  type: multiple-choice
  options:
    - "v = v₀ + at, because it directly relates velocity, acceleration, and time"
    - "x = x₀ + v₀t + ½at², because it includes displacement"
    - "v² = v₀² + 2a(x − x₀), because it relates velocity, acceleration, and displacement without needing time"
    - "x = x₀ + ½(v₀ + v)t, because it uses the average velocity"
  answer: 2
  explanation: "Here the knowns are v₀ = 30 m/s, v = 0 m/s, and Δx = 45 m; the unknown is a. The equation v² = v₀² + 2aΔx involves exactly these four quantities and no time — substituting gives 0 = 900 + 90a, so a = −10 m/s². The other equations all involve time (t), which is not given and would require a second step to eliminate. Each of the four constant-acceleration equations omits one of the five kinematic quantities, so choosing the right equation means identifying which quantity is absent."

- question: "The four constant-acceleration kinematic equations are derived by integrating a = constant twice, and each requires initial conditions to determine the constants of integration."
  type: true-false
  answer: true
  explanation: "Starting from a = constant: integrating once gives v = v₀ + at (v₀ is the integration constant, the initial velocity). Integrating again gives x = x₀ + v₀t + ½at² (x₀ is the second integration constant, the initial position). The other two equations (v² = v₀² + 2aΔx and x = ½(v₀+v)t) are algebraic combinations of these two. This derivation shows exactly where the equations come from and why they are limited to constant acceleration — the integration is valid only when a is not a function of t."

- question: "Kinematics requires knowledge of the forces acting on a particle in order to determine its position and velocity over time."
  type: true-false
  answer: false
  explanation: "Kinematics is entirely force-free — it describes motion (position, velocity, acceleration as functions of time) without any reference to what causes the motion. Forces appear in kinetics, not kinematics. In a typical dynamics problem, the two are combined: kinetics (Newton's second law ΣF = ma) provides the acceleration, and kinematics then predicts position and velocity from that acceleration. But the kinematic equations themselves — including the four constant-acceleration equations — make no mention of mass, force, or any physical cause. This separation is conceptually important and practically useful."

- question: "What is the conceptual difference between kinematics and kinetics, and why is it useful to keep them distinct when solving motion problems?"
  type: short-answer
  answer: "Kinematics describes *how* a particle moves — it defines the relationships between position, velocity, acceleration, and time through calculus, without asking why. Kinetics explains *why* the motion occurs — it applies Newton's second law to relate forces and mass to acceleration. In problem-solving, keeping them distinct creates a clean two-step process: (1) use force analysis (kinetics) to determine acceleration from the net force and mass, then (2) use kinematic equations to find position and velocity from that acceleration. Conflating them leads to circular reasoning or skipping force analysis entirely."
  explanation: "The distinction also clarifies what information is needed at each step. The kinematic equations work for *any* motion with a given acceleration profile — they don't care what caused the acceleration. The kinetics step is where physical understanding (friction coefficients, spring constants, gravity) enters. Once you have a(t), a(x), or constant a, kinematics takes over and the physics is done. This modularity is why engineering dynamics courses teach kinematics first, then kinetics — the tools are separate and each must be mastered independently."
```

## Explainer

Rectilinear motion is the gateway from statics — where things are still — to dynamics — where things move. The crucial shift is adding time as an independent variable. You now ask not just "what forces act?" but "where is the particle, how fast is it going, and how is that changing?"

The three **kinematic quantities** — position x(t), velocity v = dx/dt, and acceleration a = dv/dt — form a chain of derivatives. Velocity is the rate of change of position; acceleration is the rate of change of velocity. Moving in the other direction, if you know acceleration as a function of time, you recover velocity by integration (plus an initial condition), and position by integrating again. The chain rule of calculus links all three: given any one quantity as a function of time, the others follow by differentiation or integration. You can also relate velocity and acceleration without time by writing a = v dv/dx, a form useful when acceleration is given as a function of position.

The special and practically important case of **constant acceleration** produces four closed-form equations you can use without integration: v = v₀ + at, x = x₀ + v₀t + ½at², v² = v₀² + 2a(x − x₀), and x = x₀ + ½(v₀ + v)t. These equations form a complete toolkit: each equation omits one of the five quantities {x, v₀, v, a, t}, so you pick the equation that uses your three knowns to find your unknown. Free fall near Earth's surface (a = −g ≈ −9.81 m/s²) is the canonical example, but any problem with constant net force — a block on a frictionless ramp, a puck decelerating uniformly — fits this framework.

A conceptual boundary worth keeping clear: **kinematics** describes motion; **kinetics** explains it using forces. Rectilinear motion equations tell you how a particle moves given its initial state and acceleration, but they make no claim about what caused that acceleration. Forces don't appear in kinematics at all. When you later apply Newton's second law (ΣF = ma), you'll compute a from the forces and then use the kinematic equations to find position and velocity. The two halves — force analysis and motion description — plug together but remain conceptually distinct.
