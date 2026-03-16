---
id: kinematics-particles-rectilinear
title: Rectilinear Kinematics of Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-1d
  type: hard
- id: kinematic-equations
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
builds-toward:
- kinematics-particles-curvilinear
- dynamics-newtons-second-law
tags:
- dynamics
- kinematics
- rectilinear motion
- particles
- integration
stage: formal-systems
status: validated
---

# Rectilinear Kinematics of Particles

## Core Idea
Rectilinear kinematics describes particle motion along a straight line through position x(t), velocity v = dx/dt, and acceleration a = dv/dt. Three analysis cases arise: (1) constant acceleration — use the kinematic equations directly; (2) acceleration as a function of time, a(t) — integrate with respect to time; (3) acceleration as a function of position, a(x) — apply the chain rule identity a = v dv/dx to formulate a separable ODE. Selecting the correct method depends on how acceleration is specified.

## How It's Best Learned
Identify which case applies before choosing a solution method. Practice recognizing when to integrate a(t) and when to use a = v dv/dx. Always apply initial conditions after integrating.

## Common Misconceptions
- Using constant-acceleration kinematic equations when acceleration varies with time or position.
- Confusing total distance traveled (always positive, path length) with displacement (signed, net change in position).
- Forgetting initial conditions when integrating to find velocity or position.

## Questions

```yaml
- question: "A particle starts with velocity v(0) = 2 m/s and has acceleration a = 6t m/s². What is the velocity at t = 3 s?"
  type: multiple-choice
  options: ["20 m/s", "29 m/s", "56 m/s", "18 m/s"]
  answer: 1
  explanation: "Since a = 6t is a function of time, integrate: v(t) = ∫6t dt = 3t² + C. Applying the initial condition v(0) = 2 gives C = 2, so v(t) = 3t² + 2. At t = 3: v = 3(9) + 2 = 29 m/s. A common error is to use the constant-acceleration formula v = v₀ + at with a single value of a, which is only valid when a is constant."

- question: "A particle travels 40 m to the right, then reverses and travels 10 m to the left. Its displacement is 30 m and its total distance traveled is also 30 m."
  type: true-false
  answer: false
  explanation: "Displacement is the net change in position (signed): 40 - 10 = 30 m to the right. Total distance traveled is the total path length regardless of direction: 40 + 10 = 50 m. These are equal only when the particle never reverses direction. Confusing displacement and distance is one of the most common errors in kinematics."

- question: "When should you use the identity a = v dv/dx instead of integrating a(t) with respect to time?"
  type: short-answer
  answer: "Use a = v dv/dx when acceleration is given as a function of position, a(x). In that case, integrating a dt is not possible directly because t is not the independent variable in the expression for a. The chain rule identity a = v dv/dx converts the problem into a separable ODE in x, which can be integrated to find v(x)."
  explanation: "The three-case framework is central to rectilinear kinematics: (1) a = constant → use kinematic equations; (2) a = f(t) → integrate with respect to time; (3) a = f(x) → apply a = v dv/dx to get v as a function of x. The identity comes from a = dv/dt = (dv/dx)(dx/dt) = v dv/dx by the chain rule."
```

## Explainer

Rectilinear kinematics answers a deceptively simple question: given how a particle accelerates, where is it and how fast is it moving at any time? The three kinematic quantities — position x(t), velocity v = dx/dt, and acceleration a = dv/dt — are connected by derivatives and integrals, and the solution strategy depends entirely on how the acceleration is specified.

**Case 1: constant acceleration.** If a is a fixed number, the familiar constant-acceleration kinematic equations apply directly: v = v₀ + at, x = x₀ + v₀t + ½at², and v² = v₀² + 2a(x − x₀). These are valid only when a truly does not change. Applying them to a variable-acceleration problem is the single most common error in introductory dynamics.

**Case 2: acceleration as a function of time, a(t).** Integrate once to get velocity: v(t) = ∫a(t) dt + C₁, and apply v(t₀) = v₀ to find C₁. Integrate again to get position: x(t) = ∫v(t) dt + C₂, with x(t₀) = x₀ determining C₂. Initial conditions are not optional — they are required to pin down the unique physical solution from the family of antiderivatives.

**Case 3: acceleration as a function of position, a(x).** Here you cannot integrate a dt because t does not appear explicitly in a. The solution is the chain rule identity: a = dv/dt = (dv/dx)(dx/dt) = v dv/dx. This transforms the equation into v dv = a(x) dx, a separable ODE that you integrate to find v as a function of x. Selecting the correct case before writing any equation is the key skill — it prevents the most common errors and immediately points to the right mathematical tool.

A final distinction worth internalizing: **displacement** is the net change in position (a signed number that can be zero even when the particle has moved far), while **total distance traveled** is the cumulative path length (always non-negative). A particle that travels 5 m right and 5 m back has zero displacement but 10 m of distance. Velocity changes sign when the particle reverses, so you must identify reversal points and split the integral to compute total distance correctly.
